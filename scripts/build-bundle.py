#!/usr/bin/env python3
"""Build the single-file BTcord theme: btcord.bundle.theme.css

Why this exists
---------------
The normal BTcord install (btcord.theme.css) is modular: it @imports the
core/components/addons from GitHub Pages. That needs Pages enabled on this
repo. The bundle inlines every local file into ONE .css file, so it works
from any direct link (e.g. the raw.githubusercontent.com URL on `main`) or
as a local file via Vencord/BetterDiscord "Upload Theme" -- no Pages needed.

Usage
-----
    python3 scripts/build-bundle.py

What it does
------------
* Inlines every `bt-studio-dev.github.io/BTcord/...` @import recursively.
* Hoists the remaining third-party @imports (Google Fonts, DevilBro,
  Discolored, RadialStatus) to the top of the file -- CSS requires all
  @imports before any other rules. They keep auto-updating upstream.
* Rewrites remaining asset URLs (wallpapers) from GitHub Pages to the
  raw.githubusercontent.com `main` branch so images load without Pages.
* Copies the BetterDiscord/Vencord metadata block from btcord.theme.css.

Re-run this after editing any source .css file, then commit the bundle.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRY = ROOT / 'btcord.theme.css'
OUT = ROOT / 'btcord.bundle.theme.css'

PAGES_BASE = 'https://bt-studio-dev.github.io/BTcord/'
ASSET_BASE = 'https://raw.githubusercontent.com/BT-Studio-dev/BTcord/main/'

IMPORT_RE = re.compile(r'^\s*@import\s+url\(["\']([^"\']+)["\']\)\s*;\s*$')

hoisted = []       # third-party @imports, in first-seen order
inlined = []       # local files inlined, in order
_seen_files = set()
_seen_urls = set()


def process_file(path: Path, label: str) -> str:
    if path in _seen_files:
        return f'/* (already inlined above: {label}) */\n'
    _seen_files.add(path)
    inlined.append(label)
    out = [f'\n/* ===== inlined: {label} ===== */\n']
    for line in path.read_text(errors='ignore').splitlines(keepends=True):
        m = IMPORT_RE.match(line.rstrip('\n'))
        if not m:
            out.append(line)
            continue
        url = m.group(1)
        if url.startswith(PAGES_BASE):
            rel = url[len(PAGES_BASE):]
            out.append(process_file(ROOT / rel, rel))
        else:
            if url not in _seen_urls:
                _seen_urls.add(url)
                hoisted.append(url)
            out.append(f'/* (@import hoisted to top: {url}) */\n')
    return ''.join(out)


def main():
    entry = ENTRY.read_text(errors='ignore')

    # --- metadata block (first /** ... */) ---
    m = re.search(r'/\*\*.*?\*/', entry, flags=re.S)
    if not m:
        sys.exit('metadata block not found in btcord.theme.css')
    meta = m.group(0)
    meta = meta.replace(
        '@description BTcord -',
        '@description BTcord (single-file bundle) -',
    ).replace(
        '@updateUrl https://raw.githubusercontent.com/BT-Studio-dev/BTcord/main/btcord.theme.css',
        '@updateUrl https://raw.githubusercontent.com/BT-Studio-dev/BTcord/main/btcord.bundle.theme.css',
    )

    # --- entry body after the metadata block ---
    tmp = ROOT / '.bundle-entry.tmp.css'
    tmp.write_text(entry[m.end():])
    try:
        body = process_file(tmp, 'btcord.theme.css (variables)')
    finally:
        tmp.unlink(missing_ok=True)

    # --- asset URLs: Pages -> raw main (wallpapers etc.) ---
    body = body.replace(PAGES_BASE, ASSET_BASE)
    if PAGES_BASE in body:
        sys.exit(f'error: {PAGES_BASE} still present in bundle body')

    banner = (
        '/* ======================================================================\n'
        '   GENERATED FILE -- do not edit by hand.\n'
        '   Built from btcord.theme.css + chillax.css + Components/ + Addons/\n'
        '   by scripts/build-bundle.py. Edit the source files, then re-run it.\n'
        '   This single-file build needs no GitHub Pages and works from a\n'
        '   direct link (Vencord Online Themes) or as an uploaded local file.\n'
        '   ====================================================================== */\n'
    )
    imports = ''.join(f'@import url("{u}");\n' for u in hoisted)

    OUT.write_text(meta + '\n\n' + banner + imports + body)
    print(f'wrote {OUT.name}: {OUT.stat().st_size // 1024} KiB, '
          f'{len(inlined)} local files inlined, {len(hoisted)} third-party imports hoisted')
    for label in inlined:
        print(f'  inlined: {label}')
    for url in hoisted:
        print(f'  hoisted: {url}')


if __name__ == '__main__':
    main()
