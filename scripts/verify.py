"""Verify a generated repository without installing extra dependencies."""
import hashlib
import json
import pathlib
import sys
import tomllib
import xml.etree.ElementTree as ET

root = pathlib.Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'kokedera.json').read_text(encoding='utf-8'))
errors = []
for name, expected in manifest['files'].items():
    path = (root / name).resolve()
    if not path.is_relative_to(root):
        errors.append(f'Unsafe path: {name}')
        continue
    if not path.is_file():
        errors.append(f'Missing: {name}')
        continue
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        errors.append(f'Changed: {name}')
    try:
        if path.suffix == '.json':
            json.loads(raw)
        elif path.suffix == '.toml':
            tomllib.loads(raw.decode('utf-8'))
        elif path.suffix.lower() in ('.xml', '.svg', '.tmtheme', '.itermcolors', '.terminal', '.xccolortheme'):
            ET.fromstring(raw)
    except Exception as exc:
        errors.append(f'Invalid format: {name}: {exc}')
if len(manifest['variants']) != 9 or sum(p['scheme'] == 'light' for p in manifest['variants']) != 2:
    errors.append('Expected all nine variants, including two light themes')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Verified {len(manifest['files'])} files and nine palettes in {manifest['repository']}.")
