#!/usr/bin/env python3
"""Generate GNOME accent variants, leaving the shared base theme intact."""
from pathlib import Path
import shutil

# GNOME/libadwaita system accent colors:
# https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/enum.AccentColor.html
ACCENTS = {
    'blue': '#3584e4', 'teal': '#2190a4', 'green': '#3a944a',
    'yellow': '#c88800', 'orange': '#ed5b00', 'red': '#e62d42',
    'pink': '#d56199', 'purple': '#9141ac', 'slate': '#6f8396',
}


def lighter(color):
    channels = [int(color[i:i + 2], 16) for i in (1, 3, 5)]
    return '#' + ''.join(f'{round(value + (255 - value) * .25):02x}' for value in channels)


def build(dist):
    base = dist / 'Lyra-OS-Icons'
    for name, color in ACCENTS.items():
        target = dist / f'Lyra-OS-Icons-{name}'
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(base, target, symlinks=True)
        index = (base / 'index.theme').read_text()
        index = index.replace('Name=Lyra OS Icons', f'Name=Lyra OS Icons ({name})')
        index = index.replace('Comment=Flat sapphire icon theme for Lyra OS', f'Comment=GNOME {name} accent icons for Lyra OS')
        index = index.replace('Inherits=adwaita-xfce,Adwaita,hicolor', 'Inherits=Lyra-OS-Icons,Adwaita,hicolor')
        (target / 'index.theme').write_text(index)
        for svg in target.rglob('*.svg'):
            if not svg.is_symlink():
                svg.write_text(svg.read_text().replace('#2AC7FD', lighter(color)).replace('#BE49FD', color))


if __name__ == '__main__':
    build(Path(__file__).resolve().parents[1] / 'dist')
