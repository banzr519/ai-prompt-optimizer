#!/usr/bin/env python3
"""Build reproducible standalone and plugin-preview ZIPs from one reviewed source tree."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('apo_installer', ROOT / 'scripts/manage_install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


def archive(path, files):
    with zipfile.ZipFile(path, 'x', compression=zipfile.ZIP_DEFLATED) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (0o100755 if name.endswith('.sh') else 0o100644) << 16
            z.writestr(info, data)


def build(output):
    output = Path(output).expanduser().resolve()
    if output.exists():
        raise ValueError('Choose a new output directory; existing artifacts are never overwritten')
    if output.is_relative_to(ROOT):
        raise ValueError('Build outside the source/skill directory')
    version = installer.version(ROOT)
    manifest = json.loads((ROOT / 'packaging/plugin.json').read_text(encoding='utf-8'))
    if manifest['version'] != version or manifest['skills'] != './skills/':
        raise ValueError('Plugin metadata does not match source')
    files = {rel: (ROOT / rel).read_bytes() for rel in installer.inventory(ROOT, public_only=True)}
    output.mkdir(parents=True)
    standalone = output / ('ai-prompt-optimizer-' + version + '.zip')
    plugin = output / ('ai-prompt-optimizer-plugin-preview-' + version + '.zip')
    archive(standalone, {'ai-prompt-optimizer/' + p: data for p, data in files.items()})
    prefix = 'ai-prompt-optimizer-plugin/'
    plugin_files = {prefix + 'skills/ai-prompt-optimizer/' + p: data for p, data in files.items()}
    plugin_files[prefix + '.codex-plugin/plugin.json'] = (ROOT / 'packaging/plugin.json').read_bytes()
    plugin_files[prefix + 'LICENSE'] = (ROOT / 'LICENSE').read_bytes()
    plugin_files[prefix + 'skills/ai-prompt-optimizer-setup/SKILL.md'] = (ROOT / 'packaging/onboarding/SKILL.md.in').read_bytes()
    archive(plugin, plugin_files)
    for name, data in files.items():
        with zipfile.ZipFile(plugin) as z:
            if z.read(prefix + 'skills/ai-prompt-optimizer/' + name) != data:
                raise ValueError('Plugin core differs from standalone')
    checksum = ''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n' for p in (standalone, plugin))
    (output / 'SHA256SUMS.txt').write_text(checksum, encoding='utf-8')
    report = {'version': version, 'standalone_files': len(files), 'shared_core': 'byte-identical', 'plugin_status': 'packaging-preview-not-client-tested', 'publication_status': 'not-published-by-this-build', 'archives': [standalone.name, plugin.name]}
    (output / 'BUILD-REPORT.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, help='New directory outside this source tree')
    print(json.dumps(build(parser.parse_args().output), indent=2))
