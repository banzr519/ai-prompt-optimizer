"""Local filesystem tests; no provider calls, real home edits or fixture repairs."""
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('installer', ROOT / 'scripts/manage_install.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='apo-test-')
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve()
        self.home = self.base / '用户 home'
        self.home.mkdir()
        self.source = self.base / 'source'
        self.source.mkdir()
        for rel in m.inventory(ROOT, public_only=True):
            p = self.source / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, p)
        self.manager = m.Manager(home=self.home, codex_home=self.home / '.codex')
        self.provenance = {'kind': 'local', 'commit': None}

    def install(self, **kwargs):
        return self.manager.install(self.source, self.provenance, **kwargs)

    def test_fresh_install_and_uninstall_preserve_user_rules(self):
        path = self.manager.guidance_root / 'AGENTS.md'
        path.parent.mkdir(parents=True)
        original = '用户规则\r\n保留原文\r\n'.encode()
        path.write_bytes(original)
        status = self.install()
        self.assertEqual(status['problems'], [])
        self.assertEqual(status['session_verification'], 'not-run')
        self.assertTrue(path.read_bytes().startswith(original))
        self.assertIn(b'\r\n<!--', path.read_bytes())
        self.manager.uninstall()
        self.assertEqual(path.read_bytes(), original)
        self.assertFalse(self.manager.target.exists())

    def test_repeat_is_idempotent(self):
        self.install()
        state = self.manager.state_file.read_bytes()
        before = list((self.manager.store / 'backups').iterdir())
        self.assertEqual(self.install()['problems'], [])
        self.assertEqual(self.manager.state_file.read_bytes(), state)
        self.assertEqual(list((self.manager.store / 'backups').iterdir()), before)

    def test_host_mode_leaves_no_guidance(self):
        result = self.install(mode='host')
        self.assertEqual(result['policy'], 'host-default')
        self.assertFalse((self.manager.guidance_root / 'AGENTS.md').exists())
        self.manager.configure('on-demand')
        self.manager.configure('host')
        self.assertFalse((self.manager.guidance_root / 'AGENTS.md').exists())

    def test_existing_personal_rule_is_not_duplicated(self):
        path = self.manager.guidance_root / 'AGENTS.md'
        path.parent.mkdir(parents=True)
        data = b'Use ai-prompt-optimizer when useful.\n'
        path.write_bytes(data)
        result = self.install()
        self.assertEqual(result['policy'], 'existing-user-guidance-review-needed')
        self.assertTrue(result['warnings'])
        self.assertIn('Review existing guidance', result['next_step'])
        self.assertEqual(path.read_bytes(), data)
        self.manager.uninstall()
        self.assertEqual(path.read_bytes(), data)

    def test_custom_codex_home_and_override(self):
        self.manager = m.Manager(home=self.home, codex_home=self.base / '配置目录')
        p = self.manager.guidance_root / 'AGENTS.override.md'
        p.parent.mkdir(parents=True)
        p.write_bytes(b'Override.\n')
        result = self.install()
        self.assertEqual(result['guidance_path'], str(p))
        self.assertFalse((self.home / '.codex').exists())

    def test_override_added_later_and_migration(self):
        self.install()
        base = self.manager.guidance_root / 'AGENTS.md'
        override = self.manager.guidance_root / 'AGENTS.override.md'
        override.write_bytes(b'Other rule.\n')
        self.assertIn('managed-guidance-shadowed-by-override', self.manager.status()['problems'])
        self.manager.configure('on-demand')
        self.assertFalse(base.exists())
        self.assertIn(m.BEGIN, override.read_text())
        self.manager.uninstall()
        self.assertEqual(override.read_bytes(), b'Other rule.\n')

    def test_project_install_is_scoped(self):
        project = self.base / '项目'
        project.mkdir()
        self.manager = m.Manager(home=self.home, codex_home=self.home / '.codex', project=project)
        self.install()
        self.assertTrue((project / 'AGENTS.md').exists())
        self.assertFalse((self.home / '.agents').exists())
        self.assertFalse((self.home / '.codex/AGENTS.md').exists())

    def test_modified_installed_file_blocks_update_and_uninstall(self):
        self.install()
        p = self.manager.target / 'SKILL.md'
        p.write_bytes(p.read_bytes() + b'\nMy change.\n')
        with self.assertRaises(m.InstallError): self.install(update=True)
        with self.assertRaises(m.InstallError): self.manager.uninstall()
        self.assertTrue(p.read_bytes().endswith(b'My change.\n'))

    def test_extra_private_file_is_preserved(self):
        self.install()
        p = self.manager.target / '.env'
        p.write_bytes(b'personal settings')
        with self.assertRaises(m.InstallError): self.install(update=True)
        self.assertTrue(p.exists())

    def test_changed_managed_rule_blocks_removal(self):
        self.install()
        p = self.manager.guidance_root / 'AGENTS.md'
        p.write_text(p.read_text().replace('on-demand preference', 'my preference'))
        with self.assertRaises(m.InstallError): self.manager.uninstall()
        self.assertTrue(self.manager.target.exists())

    def test_unowned_marker_refused(self):
        p = self.manager.guidance_root / 'AGENTS.md'
        p.parent.mkdir(parents=True)
        p.write_text(m.BEGIN + '\nunknown\n' + m.END)
        with self.assertRaises(m.InstallError): self.install()
        self.assertFalse(self.manager.target.exists())

    def test_duplicate_is_not_overwritten(self):
        other = self.home / '.codex/skills/ai-prompt-optimizer'
        other.mkdir(parents=True)
        (other / 'SKILL.md').write_text('custom')
        with self.assertRaises(m.InstallError): self.install()
        self.assertEqual((other / 'SKILL.md').read_text(), 'custom')

    def test_unknown_existing_directory_refused(self):
        self.manager.target.mkdir(parents=True)
        (self.manager.target / 'SKILL.md').write_text('unknown')
        with self.assertRaises(m.InstallError): self.install(adopt=True)
        self.assertEqual((self.manager.target / 'SKILL.md').read_text(), 'unknown')

    def test_identical_zip_can_be_adopted(self):
        shutil.copytree(self.source, self.manager.target)
        result = self.install(adopt=True)
        self.assertEqual(result['problems'], [])
        self.assertTrue((Path(result['backup']) / 'skill/SKILL.md').exists())

    def git_clone(self):
        source = self.base / 'legacy'
        shutil.copytree(self.source, source)
        def run(*args, cwd=source):
            return subprocess.check_output(['git', *args], cwd=cwd, stderr=subprocess.DEVNULL)
        run('init', '-b', 'main')
        run('config', 'user.name', 'Installer Test')
        run('config', 'user.email', 'test@example.invalid')
        run('add', '.')
        run('commit', '-m', 'Legacy baseline')
        self.manager.target.parent.mkdir(parents=True)
        run('clone', str(source), str(self.manager.target))
        run('remote', 'set-url', 'origin', 'https://github.com/' + m.REPO + '.git', cwd=self.manager.target)
        return run

    def test_clean_git_migration_keeps_history_in_backup(self):
        self.git_clone()
        result = self.install(adopt=True)
        self.assertTrue((Path(result['backup']) / 'skill/.git').is_dir())
        self.assertFalse((self.manager.target / '.git').exists())

    def test_ignored_git_file_blocks_migration(self):
        self.git_clone()
        (self.manager.target / '.env').write_text('local')
        with self.assertRaises(m.InstallError): self.install(adopt=True)
        self.assertTrue((self.manager.target / '.env').exists())

    def test_same_version_update_with_changed_source(self):
        self.install()
        p = self.source / 'references/examples.md'
        p.write_text(p.read_text() + '\nUpdated example.\n')
        result = self.install(update=True)
        self.assertEqual(result['problems'], [])
        self.assertEqual((self.manager.target / 'references/examples.md').read_bytes(), p.read_bytes())

    def test_downgrade_is_blocked(self):
        self.install()
        p = self.source / 'github-metadata.json'
        meta = json.loads(p.read_text()); meta['release_version'] = '2.3.0';p.write_text(json.dumps(meta))
        with self.assertRaises(m.InstallError): self.install(update=True)

    def test_failure_rolls_back_skill_guidance_and_state(self):
        self.install()
        state = self.manager.state_file.read_bytes()
        skill = (self.manager.target / 'SKILL.md').read_bytes()
        guidance = (self.manager.guidance_root / 'AGENTS.md').read_bytes()
        p = self.source / 'SKILL.md'; p.write_bytes(p.read_bytes() + b'\nNew.\n')
        real = m.atomic_write
        failed = []
        def fail_once(path, data):
            if path == self.manager.state_file and not failed:
                failed.append(True)
                raise OSError('simulated disk failure')
            return real(path, data)
        with patch.object(m, 'atomic_write', side_effect=fail_once):
            with self.assertRaises(OSError): self.install(update=True, mode='host')
        self.assertEqual(self.manager.state_file.read_bytes(), state)
        self.assertEqual((self.manager.target / 'SKILL.md').read_bytes(), skill)
        self.assertEqual((self.manager.guidance_root / 'AGENTS.md').read_bytes(), guidance)
        self.assertEqual(self.manager.status()['problems'], [])

    def test_symlink_target_rejected(self):
        self.manager.target.parent.mkdir(parents=True)
        self.manager.target.symlink_to(self.source, target_is_directory=True)
        with self.assertRaises(m.InstallError): m.Manager(home=self.home, codex_home=self.home / '.codex')

    def test_lock_and_interruption_are_reported(self):
        self.manager.store.mkdir(parents=True)
        (self.manager.store / 'lock').mkdir()
        with self.assertRaises(m.InstallError): self.install()
        self.assertIn('operation-in-progress-or-stale-lock', self.manager.status()['problems'])
        (self.manager.store / 'lock').rmdir()
        (self.manager.store / 'transaction.json').write_text('{}')
        with self.assertRaises(m.InstallError): self.install()
        self.assertFalse(self.manager.target.exists())

    def test_plugin_config_does_not_create_second_skill(self):
        result = self.manager.configure('on-demand', str(self.source))
        self.assertEqual(result['provider'], 'plugin')
        self.assertFalse(self.manager.target.exists())
        with self.assertRaises(m.InstallError): self.install(update=True)
        self.manager.uninstall()
        self.assertTrue((self.source / 'SKILL.md').exists())

    def test_download_failure_changes_nothing(self):
        args = type('Args', (), {'source': None, 'ref': None})()
        with patch.object(m, 'request', side_effect=OSError('network unavailable')):
            with self.assertRaises(OSError):
                with m.source(args): pass
        self.assertFalse(self.manager.target.exists())
        self.assertFalse(self.manager.store.exists())

    def test_malicious_archives_rejected(self):
        for name in ['root/../../outside', '/absolute', 'root/..\\outside', 'root/C:drive']:
            data = io.BytesIO()
            with zipfile.ZipFile(data, 'w') as z: z.writestr(name, 'x')
            with self.assertRaises(m.InstallError): m.extract_archive(data.getvalue(), self.base / 'extract')
        self.assertFalse((self.base / 'outside').exists())

    def test_added_git_history_is_preserved(self):
        self.install()
        (self.manager.target / '.git').mkdir()
        (self.manager.target / '.git/personal-history').write_text('keep')
        with self.assertRaises(m.InstallError): self.install(update=True)
        with self.assertRaises(m.InstallError): self.manager.uninstall()
        self.assertTrue((self.manager.target / '.git/personal-history').exists())

    def test_missing_runtime_reference_is_rejected(self):
        (self.source / 'references/semantic-patterns.md').unlink()
        with self.assertRaises(m.InstallError): self.install()
        self.assertFalse(self.manager.target.exists())

    def test_removed_plugin_can_still_clear_preference(self):
        self.manager.configure('on-demand', str(self.source))
        shutil.rmtree(self.source)
        result = self.manager.uninstall()
        self.assertIn('preference-removed', result['installation'])
        self.assertFalse((self.manager.guidance_root / 'AGENTS.md').exists())

    def test_archive_symlink_and_case_collision_rejected(self):
        data = io.BytesIO()
        with zipfile.ZipFile(data, 'w') as z:
            info = zipfile.ZipInfo('root/link'); info.create_system = 3
            info.external_attr = 0o120777 << 16
            z.writestr(info, '/outside')
        with self.assertRaises(m.InstallError): m.extract_archive(data.getvalue(), self.base / 'extract')
        data = io.BytesIO()
        with zipfile.ZipFile(data, 'w') as z:
            z.writestr('root/A', 'first'); z.writestr('root/a', 'second')
        with self.assertRaises(m.InstallError): m.extract_archive(data.getvalue(), self.base / 'extract2')

    def test_online_source_pins_resolved_commit(self):
        sha = 'a' * 40
        data = io.BytesIO()
        with zipfile.ZipFile(data, 'w') as z: z.writestr('root/README.md', 'download')
        calls = []
        def fetch(url):
            calls.append(url)
            return json.dumps({'sha': sha}).encode() if len(calls) == 1 else data.getvalue()
        args = type('Args', (), {'source': None, 'ref': None})()
        with patch.object(m, 'request', side_effect=fetch):
            with m.source(args) as (root, provenance):
                self.assertEqual(provenance['commit'], sha)
                self.assertEqual((root / 'README.md').read_text(), 'download')
        self.assertEqual(calls[1], 'https://codeload.github.com/' + m.REPO + '/zip/' + sha)

    def test_source_private_files_not_copied(self):
        (self.source / '.env').write_text('secret')
        self.install()
        self.assertFalse((self.manager.target / '.env').exists())


if __name__ == '__main__':
    unittest.main()
