"""Check delivered bytes, reproducibility and navigation rather than snapshotting prose."""
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('distribution', ROOT / 'scripts/build_distribution.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class DistributionTests(unittest.TestCase):
    def test_archives_reproducible_and_core_identical(self):
        with tempfile.TemporaryDirectory() as temp:
            first, second = Path(temp) / 'first', Path(temp) / 'second'
            report = builder.build(first)
            builder.build(second)
            for archive in report['archives']:
                self.assertEqual((first / archive).read_bytes(), (second / archive).read_bytes())
            with zipfile.ZipFile(first / report['archives'][0]) as standalone, zipfile.ZipFile(first / report['archives'][1]) as plugin:
                for name in standalone.namelist():
                    self.assertNotIn('/.git/', name)
                    self.assertNotIn('__pycache__', name)
                    self.assertNotIn('/.env', name)
                    rel = name.split('/', 1)[1]
                    self.assertEqual(standalone.read(name), plugin.read('ai-prompt-optimizer-plugin/skills/ai-prompt-optimizer/' + rel))
                manifest = json.loads(plugin.read('ai-prompt-optimizer-plugin/.codex-plugin/plugin.json'))
                self.assertEqual(manifest['version'], report['version'])
                self.assertIn('ai-prompt-optimizer-plugin/skills/ai-prompt-optimizer-setup/SKILL.md', plugin.namelist())

    def test_existing_output_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / 'valuable.txt'; p.write_text('keep')
            with self.assertRaises(ValueError): builder.build(Path(temp))
            self.assertEqual(p.read_text(), 'keep')

    def test_localization_stays_in_sync(self):
        subprocess.run([sys.executable, str(ROOT / 'scripts/build_localized_docs.py'), '--check'], check=True, capture_output=True)
        catalog = json.loads((ROOT / 'locales/catalog.json').read_text())
        self.assertEqual(len(catalog['locales']), 30)
        levels = [x['documentation_level'] for x in catalog['locales']]
        self.assertEqual(levels.count('primary-full'), 2)
        self.assertEqual(levels.count('localized-starter-and-guide'), 27)
        self.assertEqual(levels.count('experimental-bilingual-starter'), 1)

    def test_relative_links_and_anchors(self):
        def anchors(path):
            text = re.sub(r'```[^\n]*\n.*?```', '', path.read_text(), flags=re.S)
            result, seen = set(), {}
            for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
                slug = re.sub(r'[^\w\-\s]', '', title.lower()).replace(' ', '-')
                n = seen.get(slug, 0); seen[slug] = n + 1
                result.add(slug if n == 0 else slug + '-' + str(n))
            return result
        for rel in builder.installer.inventory(ROOT, public_only=True):
            path = ROOT / rel
            if path.suffix != '.md': continue
            text = re.sub(r'```[^\n]*\n.*?```', '', path.read_text(), flags=re.S)
            for href in re.findall(r'\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)', text):
                u = urlsplit(href.strip('<>'))
                if u.scheme or u.netloc: continue
                target = (path.parent / unquote(u.path)).resolve() if u.path else path
                with self.subTest(source=rel, link=href):
                    self.assertTrue(target.is_relative_to(ROOT), 'Link escapes repository')
                    self.assertTrue(target.is_file(), 'Missing local file')
                    if u.fragment and target.suffix == '.md':
                        self.assertIn(unquote(u.fragment), anchors(target), 'Missing heading anchor')


if __name__ == '__main__':
    unittest.main()
