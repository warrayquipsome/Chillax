<h1 align="center">BTcord</h1>

<p align="center">
  A glass Discord theme by <b>BT Studio</b>, forked from <a href="https://github.com/warrayquipsome/Chillax">Chillax</a> and updated for Discord's <b>Visual Refresh</b> UI (2026).<br/>
  <i>Where calm meets customization.</i>
</p>

<p align="center">
  <a href="https://bt-studio-dev.github.io/BTcord/preview.html"><b>▶ Live preview</b></a> ·
  <a href="#installation"><b>Install</b></a> ·
  <a href="#customise">Customise</a> ·
  <a href="CHANGELOG.md">Changelog</a> ·
  <a href="#credits">Credits</a>
</p>

![BTcord preview](Wallpapers/modern-dark-bg.png)

> **New in BTcord 1.0** — rebuilt for the new Discord: dead pre-2023 selectors removed, Visual Refresh design tokens (`--background-base-*`, `--text-*`, `--border-*`…) themed, Darker/Midnight variants supported, BT violet/cyan identity, and every file now loads from **this** repo (the old fork silently loaded upstream Chillax, so edits here changed nothing). Full list: [CHANGELOG.md](CHANGELOG.md).

# Installation

You need a client mod. Install **one** of [Vencord](https://vencord.dev/), [BetterDiscord](https://betterdiscord.app/), Vesktop or Legcord, then:

### ⚡ Fastest: direct download link (single file, no GitHub Pages needed)

Paste this link into **Vencord → Settings → Themes → Online Themes** and click **Add**, then enable **BTcord** under *Installed Themes*:

```
https://raw.githubusercontent.com/BT-Studio-dev/BTcord/main/btcord.bundle.theme.css
```

Or [download `btcord.bundle.theme.css`](https://raw.githubusercontent.com/BT-Studio-dev/BTcord/main/btcord.bundle.theme.css) and use **Upload Theme** / drop it in your themes folder. It's one self-contained file (rebuilt with `python3 scripts/build-bundle.py`).

The modular install below (small file, editable variables, auto-updates per file) needs GitHub Pages enabled on this repo.

<details>
<summary><b>Vencord / Vesktop (recommended)</b></summary>

1. Open Discord → **Settings → Vencord → Themes → Online Themes**.
2. Paste this URL and press Enter:
   ```
   https://bt-studio-dev.github.io/BTcord/btcord.theme.css
   ```
3. Done — BTcord loads and updates automatically with this repo.

To customise: download [`btcord.theme.css`](btcord.theme.css), edit the variables, and import it as a **local** theme instead (Vesktop: Settings → Vesktop → Open Themes Folder).

</details>

<details>
<summary><b>BetterDiscord</b></summary>

1. Download [`btcord.theme.css`](https://github.com/BT-Studio-dev/BTcord/raw/main/btcord.theme.css).
2. Discord → **User Settings → Themes → Open Themes Folder**.
3. Drop the file in, go back, and enable **BTcord**.

BetterDiscord users migrating from the old `chillax.theme.css` file: it still works (it forwards to the new file), but please switch to `btcord.theme.css` so you can edit the variables.

</details>

<details>
<summary><b>QuickCSS / raw link</b></summary>

```css
@import url("https://bt-studio-dev.github.io/BTcord/btcord.theme.css");
```

Raw-link users get updates automatically but can't keep custom variable edits — put your own `:root { … }` overrides *below* the `@import` line in QuickCSS instead.

</details>

**Disclaimer:** BT Studio is not affiliated with Discord Inc. or with the client mods above. Client mods are against Discord's Terms of Service; use at your own discretion.

# Customise

Everything lives at the top of [`btcord.theme.css`](btcord.theme.css) — no need to touch the core files:

| Variable | What it does | BTcord default |
|---|---|---|
| `--bt-accent` / `--bt-accent-rgb` | Main accent colour everywhere | `#6d5cff` / `109, 92, 255` |
| `--bt-accent-2` | Secondary accent (gradients, unread divider) | `#22c8ee` |
| `--wallpaper` | Background image URL | `Wallpapers/btcord-default.jpg` |
| `--window-margin` / `--window-blur` / `--window-border-radius` | The floating glass window | `20px` / `5px` / `10px` |
| `--font-name` | App-wide font (wired into Discord's `--font-primary`) | `Poppins` |
| `--user-name` | Name in the "Greetings …!" splash | `"King"` |
| `--rs-online-color` etc. | RadialStatus ring colours | upstream values |

Want the **classic Chillax red** back? Set `--bt-accent-rgb: 251, 84, 84;` and `--bt-accent: #fb5454;`.

Addons are one `@import` line each in `btcord.theme.css` — delete a line to remove that feature. The opt-in `HideAnnoyingElements` addon (hides gift/GIF/sticker/Apps buttons and Nitro/Shop/Quests/Activities nav entries) is commented out by default; uncomment it to enable.

# What if Discord updates and something breaks?

Discord rotates its internal CSS class hashes regularly. BTcord's critical rules use hash-resistant selectors where possible, but things will still break eventually. When they do:

1. Run `python3 scripts/check-css.py` — it flags dead legacy selectors, stale upstream URLs and CSS syntax errors.
2. Inspect the broken element (`Ctrl+Shift+I` in Discord) and update the hashed class in the matching component file.
3. Open an issue or PR here, or check [upstream Chillax](https://github.com/warrayquipsome/Chillax/issues) for a fix to port.

# Maintainers: GitHub Pages (required once)

All `@import` URLs point at `https://bt-studio-dev.github.io/BTcord/…`. For those links to work, enable Pages **once**: repo **Settings → Pages → Deploy from a branch → `main` / `/ (root)`**. The `.nojekyll` file in this repo makes Pages serve the CSS as-is. Until the BTcord branch is merged into `main`, the links serve the old code.

Repository layout:

```
btcord.theme.css      ← modular install (variables + imports, needs GitHub Pages)
btcord.bundle.theme.css ← single-file install (direct link above, no Pages needed; generated)
chillax.css             core theme (upstream Chillax core + BTcord VR layer at the end)
btcord.css              convenience forward to the core
chillax.theme.css       compatibility forward to btcord.theme.css (old installs)
Components/             title bar, chat area, user area, embeds, emoji picker, channel header
Addons/                 optional features (one @import each)
Wallpapers/             background images
preview.html            static Discord mock for screenshot/preview
scripts/check-css.py    CSS syntax + dead-selector checker
scripts/build-bundle.py rebuilds btcord.bundle.theme.css from the sources
```

# Credits

BTcord is a fork. Per upstream's terms, Chillax authorship and watermark are retained.

## Upstream — Chillax Squad

- **[Wq](https://github.com/warrayquipsome)** — Chillax owner & dev
- [LofiTurtle](https://github.com/LofiTurtle) — dev & maintainer
- [Inmoresentum](https://github.com/Inmoresentum) — dev & maintainer
- [Demented Elmo](https://github.com/Demented-Elmo) — helper

Upstream repo & support server: <https://github.com/warrayquipsome/Chillax> · <https://discord.gg/DrfX6286kF>
(Please file BTcord-specific issues **here**, not upstream.)

## This fork

- **[BT Studio](https://github.com/BT-Studio-dev)** — BTcord maintainer (Visual Refresh update)

## Snippet & addon authors

Embeds — Alexis WyvernZu · Active Now / member-list hover — Cedrick · Hide user buttons, centred profile — Commie Axolotl · Account Details Grid — Dablulite · BlurpleRecolor, EmojiReplace, SettingsIcons — DevilBro (mwittrien) · Connection Issue Let Me Be — Disease · RadialStatus — Gibbu / DiscordStyles · About Me clamp — ItMeSarah · Jump-to-present / mark-as-read buttons — Lonk · IconPack — Lavender · Discolored — Nyri4 · Better Spotify control — Uri

<p align="center">Copyright © 2022–present <a href="https://github.com/warrayquipsome">Wq</a> and the Chillax Squad · BTcord fork © 2026 BT Studio</p>
