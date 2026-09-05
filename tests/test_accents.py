from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = spec_from_file_location('accents', ROOT / 'scripts/build-accent-icons.py')
accents = module_from_spec(spec)
spec.loader.exec_module(accents)


class AccentIconsTests(unittest.TestCase):
    def test_all_accents_produce_valid_distinct_icons_without_changing_base(self):
        with tempfile.TemporaryDirectory() as directory:
            dist = Path(directory)
            base = dist / 'Lyra-OS-Icons'
            shutil.copytree(ROOT / 'src/icons', base)
            alias = base / 'scalable/places/folder-download.svg'
            alias.symlink_to('folder.svg')
            original = {p.relative_to(base): p.read_bytes() for p in base.rglob('*') if p.is_file()}
            accents.build(dist)
            folders = set()
            self.assertEqual(len(list(dist.iterdir())), 10)
            for name, color in accents.ACCENTS.items():
                variant = dist / f'Lyra-OS-Icons-{name}'
                index = (variant / 'index.theme').read_text()
                self.assertIn('Inherits=Lyra-OS-Icons,Adwaita,hicolor', index)
                self.assertTrue((variant / alias.relative_to(base)).is_symlink())
                for svg in variant.rglob('*.svg'):
                    ET.parse(svg)
                    self.assertNotIn('#BE49FD', svg.read_text())
                folder = (variant / 'scalable/places/folder.svg').read_text()
                self.assertIn(color, folder)
                folders.add(folder)
            self.assertEqual(len(folders), 9)
            for path, content in original.items():
                self.assertEqual((base / path).read_bytes(), content)
            # A rebuild must remove obsolete files instead of shipping them.
            stale = dist / 'Lyra-OS-Icons-blue/scalable/places/obsolete.svg'
            stale.touch()
            accents.build(dist)
            self.assertFalse(stale.exists())


if __name__ == '__main__':
    unittest.main()
