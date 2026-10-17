#!/usr/bin/env python3
"""Install and maintain AI Prompt Optimizer. Python 3.9+, standard library only."""
import argparse
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import urllib.request
from urllib.parse import urlparse
import uuid
import zipfile

NAME = 'ai-prompt-optimizer'
REPO = 'banzr519/' + NAME
BEGIN = '<!-- ai-prompt-optimizer:begin -->'
END = '<!-- ai-prompt-optimizer:end -->'
RULE = '''## AI Prompt Optimizer — on-demand preference

- For ambiguous, complex or multi-constraint tasks, or prompt refinement/audit requests,
  read and apply the available ai-prompt-optimizer skill. Reuse it if already read.
- Answer clear simple tasks, questions, casual conversation and literal translations directly.
- Preserve the user's intent, numbers, constraints, specified methods and authorization.
- When execution is requested, clarify only consequential unknowns and continue the work;
  do not stop at an improved prompt or ask again for authorization already provided.
- For “refine only”, return a reusable prompt without executing it. Honor “skip optimization”.
- Keep the process concise; surface only material assumptions, conflicts or missing inputs.
'''
PUBLIC_DIRS = {'agents', 'assets', 'references', 'docs', 'evals', 'locales', 'scripts', 'tests', 'packaging'}
PUBLIC_FILES = {'SKILL.md', 'LICENSE', '.gitignore', 'github-metadata.json', 'install.sh', 'install.ps1'}
SKIP_DIRS = {'.git', '.codegraph', '__pycache__', '.pytest_cache', '.cache', '.venv', 'node_modules'}
LIMIT = 32 * 1024 * 1024


class InstallError(Exception):
    pass


def require(ok, message):
    if not ok:
        raise InstallError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return path.read_bytes() if path.exists() else None


def no_links(path):
    for part in [path, *path.parents]:
        require(not part.is_symlink(), 'Symlink path requires manual review: ' + str(part))


def atomic_write(path, data):
    no_links(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.apo-', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'wb') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if path.exists():
            os.chmod(temporary, stat.S_IMODE(path.stat().st_mode))
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def encode(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def version(root):
    for name in ('SKILL.md', 'github-metadata.json', 'LICENSE', 'agents/openai.yaml'):
        no_links(root / name)
        require((root / name).is_file(), 'Incomplete skill payload: ' + name)
    metadata = json.loads((root / 'github-metadata.json').read_text(encoding='utf-8'))
    value = metadata['release_version']
    require(re.fullmatch(r'\d+\.\d+\.\d+', value), 'Unsupported version: ' + value)
    require(metadata['repository_name'] == NAME, 'Unexpected repository name')
    text = (root / 'SKILL.md').read_text(encoding='utf-8')
    require(re.search(r'^name: ai-prompt-optimizer\s*$', text, re.M), 'Skill name is invalid')
    for href in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if '://' not in href and not href.startswith('#'):
            target = (root / href.split('#', 1)[0]).resolve()
            require(target.is_relative_to(root.resolve()) and target.is_file(), 'Missing/unsafe skill reference: ' + href)
    return value


def inventory(root, public_only=False):
    result = {}
    require(root.is_dir(), 'Directory missing: ' + str(root))
    for current, dirs, names in os.walk(root, followlinks=False):
        base = Path(current)
        for name in dirs + names:
            require(not (base / name).is_symlink(), 'Symlink in source/install: ' + str(base / name))
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in names:
            p = base / name
            rel = p.relative_to(root)
            if name.endswith(('.pyc', '.pyo')) or name == '.DS_Store':
                continue
            if public_only:
                allowed = (len(rel.parts) == 1 and (name in PUBLIC_FILES or re.fullmatch(r'README(?:\.[\w-]+)?\.md', name))) or (len(rel.parts) > 1 and rel.parts[0] in PUBLIC_DIRS)
                if not allowed:
                    continue
                require(not any(x.startswith('.') for x in rel.parts) or str(rel) == '.gitignore', 'Private file in public payload: ' + str(rel))
                require(not name.lower().endswith(('.pem', '.key')) and not re.match(r'(?i)(credentials|secrets)(\.|$)', name), 'Credential file in payload: ' + str(rel))
            result[rel.as_posix()] = digest(p.read_bytes())
    return result


def request(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': NAME + '-installer'}), timeout=30) as response:
        require(urlparse(response.url).hostname in {'api.github.com', 'codeload.github.com', 'github.com'}, 'Unexpected download host')
        data = response.read(LIMIT + 1)
    require(len(data) <= LIMIT, 'Download exceeds size limit')
    return data


def extract_archive(data, target):
    total = 0
    seen = set()
    roots = set()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        for item in archive.infolist():
            parts = PurePosixPath(item.filename).parts
            require(parts and not item.filename.startswith('/') and '\\' not in item.filename and ':' not in item.filename and '..' not in parts, 'Unsafe archive path')
            roots.add(parts[0])
            key = item.filename.rstrip('/').casefold()
            require(key not in seen, 'Duplicate archive path')
            seen.add(key)
            mode = item.external_attr >> 16
            require(not stat.S_ISLNK(mode), 'Symlink in archive')
            require(not mode or stat.S_IFMT(mode) in (0, stat.S_IFREG, stat.S_IFDIR), 'Special file in archive')
            total += item.file_size
            require(total <= LIMIT, 'Expanded archive exceeds size limit')
            path = target.joinpath(*parts)
            if item.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(archive.read(item))
    require(len(roots) == 1, 'Expected one archive root')
    return target / roots.pop()


@contextlib.contextmanager
def source(args):
    if args.source:
        p = Path(args.source).expanduser().absolute()
        no_links(p)
        yield p, {'kind': 'local', 'commit': None}
    else:
        ref = args.ref
        if ref:
            require(re.fullmatch('[0-9a-f]{40}', ref), '--ref must be a full commit SHA')
        else:
            ref = json.loads(request('https://api.github.com/repos/' + REPO + '/commits/main'))['sha']
            require(re.fullmatch('[0-9a-f]{40}', ref), 'Invalid resolved commit')
        with tempfile.TemporaryDirectory(prefix='apo-download-') as tmp:
            archive = request('https://codeload.github.com/' + REPO + '/zip/' + ref)
            # System temp roots may be aliases (for example /var on macOS).
            # Canonicalize only our own temporary directory, not user-supplied sources.
            root = extract_archive(archive, Path(tmp).resolve())
            yield root, {'kind': 'github', 'commit': ref, 'archive_sha256': digest(archive)}


class Manager:
    def __init__(self, home=None, codex_home=None, project=None):
        self.home = Path(home or Path.home()).expanduser().resolve()
        self.codex = Path(codex_home or os.environ.get('CODEX_HOME') or self.home / '.codex').expanduser().absolute()
        self.project = Path(project).expanduser().absolute() if project else None
        if self.project:
            require(self.project.is_dir(), 'Project directory does not exist')
        base = self.project or self.home
        self.target = base / '.agents/skills' / NAME
        self.guidance_root = self.project or self.codex
        key = digest(str(self.target).encode())[:16]
        self.store = self.codex / 'ai-prompt-optimizer' / key
        self.state_file = self.store / 'state.json'
        for p in (self.target, self.guidance_root, self.store):
            no_links(p)

    def load(self):
        value = read(self.state_file)
        if not value:
            return None
        state = json.loads(value)
        require(state.get('schema') == 1 and state.get('scope_target') == str(self.target), 'State scope/schema mismatch')
        return state

    @contextlib.contextmanager
    def lock(self):
        no_links(self.store)
        self.store.mkdir(parents=True, exist_ok=True, mode=0o700)
        lock = self.store / 'lock'
        try:
            lock.mkdir()
        except FileExistsError:
            raise InstallError('Another operation or interrupted operation holds the lock: ' + str(lock))
        self._holding_lock = True
        try:
            require(not (self.store / 'transaction.json').exists(), 'Interrupted transaction; inspect backups and transaction.json before continuing: ' + str(self.store))
            yield
        finally:
            self._holding_lock = False
            lock.rmdir()

    def effective_guidance(self):
        override = self.guidance_root / 'AGENTS.override.md'
        no_links(override)
        if read(override) and read(override).strip():
            return override
        return self.guidance_root / 'AGENTS.md'

    def duplicates(self, target=None):
        target = target or self.target
        candidates = {self.home / '.agents/skills' / NAME, self.home / '.codex/skills' / NAME, self.codex / 'skills' / NAME, self.target}
        return sorted(str(p) for p in candidates if p != target and (p / 'SKILL.md').exists())

    def plan_guidance(self, state, mode):
        before, after = {}, {}
        record = (state or {}).get('guidance')
        if record:
            p = Path(record['path'])
            require(p.parent == self.guidance_root and p.name in ('AGENTS.md', 'AGENTS.override.md'), 'Unexpected guidance state path')
            no_links(p)
            old = read(p)
            require(old is not None and old.count(record['text'].encode()) == 1, 'Managed guidance was edited or removed; preserve it and resolve manually: ' + str(p))
            before[p] = old
            restored = old.replace(record['text'].encode(), b'', 1)
            after[p] = None if not restored and not record['existed'] else restored
        result, status = None, 'host-default'
        if mode == 'on-demand':
            p = self.effective_guidance()
            no_links(p)
            before.setdefault(p, read(p))
            original = after.get(p, before[p])
            text = (original or b'').decode('utf-8')
            require(BEGIN not in text and END not in text, 'Unowned managed marker found; manual review required')
            if NAME in text:
                status = 'existing-user-guidance-review-needed'
            else:
                nl = '\r\n' if '\r\n' in text else '\n'
                block = (BEGIN + '\n' + RULE + END + '\n').replace('\n', nl)
                separator = '' if not text else (nl if text.endswith(nl) else nl + nl)
                addition = separator + block
                result = {'path': str(p), 'text': addition, 'existed': original is not None}
                after[p] = (text + addition).encode('utf-8')
                status = 'managed-on-demand'
        return {p: (before[p], data) for p, data in after.items() if before[p] != data}, result, status

    def check_owned(self, state):
        require(state is not None, 'No managed installation; use install first')
        if state['provider'] == 'standalone':
            require(not (self.target / '.git').exists(), 'A Git history was added to the managed installation; preserve it before replacing files')
            require(inventory(self.target) == state['files'], 'Installed files were modified, added or removed. Back up/reconcile changes before updating or uninstalling.')
        else:
            require(Path(state['skill_path']).is_dir(), 'Plugin skill missing; remove its preference with configure --mode host after restoring the plugin')

    def adopt(self, source_root, files, enabled):
        require(enabled, 'Existing unmanaged installation. Review it first, then use --adopt-existing; no files changed.')
        require(not self.duplicates(), 'Duplicate installation requires review')
        if (self.target / '.git').is_dir():
            def git(*args):
                return subprocess.check_output(['git', '-C', str(self.target), *args], text=True).strip()
            remote = git('remote', 'get-url', 'origin')
            require(remote in {'https://github.com/' + REPO + '.git', 'https://github.com/' + REPO, 'git@github.com:' + REPO + '.git'}, 'Unknown Git origin')
            require(not git('status', '--porcelain', '--untracked-files=all'), 'Git installation has local changes')
            # Do not discard clean but unpushed commits either.
            require(git('rev-parse', 'HEAD') == git('rev-parse', 'origin/main'), 'Local commit differs from tracked origin/main')
            actual = inventory(self.target)
            tracked = set(git('ls-files').splitlines())
            require(set(actual) == tracked, 'Untracked or ignored personal files exist; preserve/reconcile them before adoption')
        else:
            require(inventory(self.target) == files, 'Unknown ZIP/local content differs from the supplied version; preserve it and migrate manually')

    def transaction(self, stage, state, changes, remove=False):
        """Normal exceptions restore prior files; a hard interruption leaves a journal/backup."""
        token = uuid.uuid4().hex
        backup = self.store / 'backups' / token
        backup.mkdir(parents=True, mode=0o700)
        state_before = read(self.state_file)
        old_target = self.target.exists() and (stage is not None or remove)
        parked = self.target.parent.parent / ('.apo-previous-' + token)
        for p, (before, _) in changes.items():
            require(read(p) == before, 'Guidance changed during operation; retry after review')
        if old_target:
            shutil.copytree(self.target, backup / 'skill')
        if state_before is not None:
            (backup / 'state.json').write_bytes(state_before)
        for n, (p, (before, _)) in enumerate(changes.items()):
            if before is not None:
                (backup / ('guidance-' + str(n))).write_bytes(before)
        journal = {'backup': str(backup), 'target': str(self.target), 'parked': str(parked), 'guidance': [str(p) for p in changes], 'note': 'Hard interruption: retain these files; inspect before recovery.'}
        atomic_write(self.store / 'transaction.json', encode(journal))
        moved, swapped, written = False, False, []
        try:
            if old_target:
                os.replace(self.target, parked)
                moved = True
            if stage is not None:
                self.target.parent.mkdir(parents=True, exist_ok=True)
                os.replace(stage, self.target)
                swapped = True
            for p, (_, after) in changes.items():
                if after is None:
                    p.unlink(missing_ok=True)
                else:
                    atomic_write(p, after)
                written.append(p)
            if state is None:
                self.state_file.unlink(missing_ok=True)
            else:
                state['last_backup'] = str(backup)
                atomic_write(self.state_file, encode(state))
        except BaseException:
            if swapped:
                shutil.rmtree(self.target)
            if moved:
                os.replace(parked, self.target)
            for p in reversed(written):
                before = changes[p][0]
                if before is None:
                    p.unlink(missing_ok=True)
                else:
                    atomic_write(p, before)
            if state_before is not None:
                atomic_write(self.state_file, state_before)
            else:
                self.state_file.unlink(missing_ok=True)
            (self.store / 'transaction.json').unlink()
            raise
        (self.store / 'transaction.json').unlink()
        if moved:
            shutil.rmtree(parked)
        return str(backup)

    def install(self, root, provenance, mode=None, adopt=False, update=False):
        new_version = version(root)
        files = inventory(root, public_only=True)
        require('scripts/manage_install.py' in files, 'Source predates the managed installer; choose v2.4.0 or newer')
        require(not root.resolve().is_relative_to(self.target.resolve()), 'Use a separate source directory, not the active installation')
        with self.lock():
            state = self.load()
            require(not self.duplicates(), 'Duplicate skill installations: ' + ', '.join(self.duplicates()))
            if state:
                require(state['provider'] == 'standalone', 'Plugin content is managed by the host; update it there')
                self.check_owned(state)
                require(tuple(map(int, new_version.split('.'))) >= tuple(map(int, state['version'].split('.'))), 'Refusing version downgrade')
            elif self.target.exists():
                self.adopt(root, files, adopt)
            else:
                require(not update, 'No installation to update; use install')
            selected_mode = mode or (state or {}).get('mode') or 'on-demand'
            changes, guidance, policy = self.plan_guidance(state, selected_mode)
            if state and state['files'] == files and not changes and state['mode'] == selected_mode:
                return self.status()
            self.target.parent.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(prefix='.apo-stage-', dir=str(self.target.parent.parent)) as tmp:
                stage = Path(tmp) / NAME
                stage.mkdir()
                for rel in files:
                    dest = stage / rel
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(root / rel, dest)
                require(inventory(stage) == files, 'Source changed during staging')
                new = {'schema': 1, 'scope_target': str(self.target), 'provider': 'standalone', 'skill_path': str(self.target), 'version': new_version, 'files': files, 'source': provenance, 'mode': selected_mode, 'guidance': guidance, 'policy': policy}
                self.transaction(stage, new, changes)
        return self.status()

    def configure(self, mode, plugin_path=None):
        with self.lock():
            state = self.load()
            if plugin_path:
                require(state is None or state['provider'] == 'plugin', 'Existing standalone install; resolve before enabling plugin')
                p = Path(plugin_path).expanduser().absolute()
                no_links(p)
                require(not self.duplicates(p), 'Standalone duplicate exists; resolve before configuring plugin')
                ver = version(p)
                if not state:
                    state = {'schema': 1, 'scope_target': str(self.target), 'provider': 'plugin', 'skill_path': str(p), 'version': ver, 'files': {}, 'source': {'kind': 'host-plugin'}}
                else:
                    state.update(skill_path=str(p), version=ver)
            require(state is not None, 'Install first, or provide the installed --plugin-path')
            changes, guidance, policy = self.plan_guidance(state, mode)
            new = dict(state, mode=mode, guidance=guidance, policy=policy)
            if new != state or changes:
                self.transaction(None, new, changes)
        return self.status()

    def uninstall(self):
        with self.lock():
            state = self.load()
            require(state is not None, 'No managed installation')
            if state['provider'] == 'standalone':
                self.check_owned(state)
            changes, _, _ = self.plan_guidance(state, 'host')
            backup = self.transaction(None, None, changes, remove=state['provider'] == 'standalone')
        return {'installation': 'uninstalled' if state['provider'] == 'standalone' else 'preference-removed-use-host-to-uninstall-plugin', 'backup': backup, 'user_guidance': 'preserved', 'session_verification': 'not-run'}

    def status(self):
        state = self.load()
        problems = []
        if (self.store / 'transaction.json').exists():
            problems.append('interrupted-transaction-needs-recovery')
        if (self.store / 'lock').exists() and not getattr(self, '_holding_lock', False):
            problems.append('operation-in-progress-or-stale-lock')
        duplicates = self.duplicates(Path(state['skill_path']) if state else None)
        if duplicates:
            problems.append('duplicate-installations')
        if not state:
            return {'installation': 'unmanaged' if self.target.exists() else 'not-installed', 'path': str(self.target), 'duplicates': duplicates, 'problems': problems, 'session_verification': 'not-run'}
        try:
            self.check_owned(state)
        except (InstallError, OSError) as e:
            problems.append(str(e))
        record = state.get('guidance')
        if record:
            p = Path(record['path'])
            if (read(p) or b'').count(record['text'].encode()) != 1:
                problems.append('managed-guidance-changed')
            if p != self.effective_guidance():
                problems.append('managed-guidance-shadowed-by-override')
        warnings = []
        next_step = 'Open a new Codex chat and verify discovery; installation checks do not prove invocation.'
        if state['policy'] == 'existing-user-guidance-review-needed':
            warnings.append('Skill installed; requested default is NOT verified. Review the existing user-written rule; it may prohibit automatic use.')
            next_step = 'Review existing guidance before claiming on-demand refinement is enabled.'
        return {'installation': 'managed', 'provider': state['provider'], 'version': state['version'], 'path': state['skill_path'], 'policy': state['policy'], 'guidance_path': record['path'] if record else None, 'duplicates': duplicates, 'problems': problems, 'session_verification': 'not-run', 'warnings': warnings, 'next_step': next_step, 'backup': state.get('last_backup')}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['install', 'update', 'status', 'configure', 'uninstall'])
    parser.add_argument('--source', help='Local reviewed source folder; otherwise resolve GitHub main once to a commit')
    parser.add_argument('--ref', help='Full GitHub commit SHA; cannot be combined with --source')
    parser.add_argument('--mode', choices=['on-demand', 'host'], help='on-demand adds a preference; host adds none (implicit matching may still occur)')
    parser.add_argument('--project', help='Explicit existing project root; otherwise install for current user')
    parser.add_argument('--codex-home', help='Custom Codex configuration directory; defaults to CODEX_HOME or ~/.codex')
    parser.add_argument('--plugin-path', help='Host-installed skill path; configure only, never copy a second skill')
    parser.add_argument('--adopt-existing', action='store_true', help='Adopt a reviewed clean Git clone or identical ZIP, preserving a backup')
    parser.add_argument('--yes', action='store_true', help='Apply already-authorized changes without interactive confirmation')
    args = parser.parse_args(argv)
    try:
        require(not (args.source and args.ref), 'Choose --source or --ref')
        require(not args.plugin_path or args.action == 'configure', '--plugin-path is only for configure')
        manager = Manager(codex_home=args.codex_home, project=args.project)
        if args.source:
            args.source = str(Path(args.source).expanduser().absolute())
        if args.plugin_path:
            args.plugin_path = str(Path(args.plugin_path).expanduser().absolute())
        # Release a process working directory inside the target before Windows directory swaps.
        if args.action != 'status':
            os.chdir(manager.home)
        if args.action != 'status' and not args.yes:
            print('Action:', args.action, '\nSkill:', manager.target, '\nConfiguration:', manager.guidance_root)
            print('On-demand configuration may append a managed preference; existing files and rules are preserved.')
            require(sys.stdin.isatty(), 'Non-interactive run: review the command and supply --yes when authorized')
            require(input('Continue? [y/N] ').strip().lower() in {'y', 'yes'}, 'Cancelled; no changes made')
        if args.action in {'install', 'update'}:
            with source(args) as (root, provenance):
                result = manager.install(root, provenance, mode=args.mode, adopt=args.adopt_existing, update=args.action == 'update')
        elif args.action == 'configure':
            require(args.mode is not None, 'configure requires --mode on-demand or --mode host')
            result = manager.configure(args.mode, args.plugin_path)
        elif args.action == 'uninstall':
            result = manager.uninstall()
        else:
            result = manager.status()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2 if result.get('problems') else 0
    except (InstallError, OSError, ValueError, KeyError, zipfile.BadZipFile, subprocess.SubprocessError) as e:
        print(json.dumps({'error': str(e), 'session_verification': 'not-run'}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
