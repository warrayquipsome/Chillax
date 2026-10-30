# Changelog

## BTcord 1.0.0 — 2026-10-30

First BTcord release: the Chillax 2.1.3 fork (`9536ba1`) updated for Discord's
Visual Refresh UI, rebranded with BT Studio's identity, and repointed at its
own repository.

### Breaking / migration

- **Install `btcord.theme.css` instead of `chillax.theme.css`.** The old file
  remains as a forwarding shim, so existing installs keep working.
- **All imports now load from `bt-studio-dev.github.io/BTcord`.** Previously
  every URL pointed at upstream `warrayquipsome.github.io/Chillax`, meaning
  this fork's files had no effect at all. Requires GitHub Pages on `main`
  (see README).
- Default accent changed from Chillax red `#fb5454` to BT violet `#6d5cff`
  (one variable pair restores the red — see README).

### Fixed for the new Discord (Visual Refresh)

- Themed the Visual Refresh design tokens (`--background-base-*`,
  `--background-surface-*`, `--text-strong/default/subtle`, `--border-*`,
  `--input-background-default`, `--interactive-text/icon/background-*`, …).
  Previously only pre-Refresh variables were set, so new Discord surfaces
  rendered solid grey. Old variable names now alias to the new ones.
- Dark styles also match Discord's `.theme-darker` and `.theme-midnight`
  appearance variants, not just `.theme-dark`.
- App font now actually applies app-wide via `--font-primary` /
  `--font-display` / `--font-headline`.
- New compatibility layer at the end of `chillax.css`: guild bar, page
  container, topic subtitle strip, search-results panel, thread sidebar,
  profile v2 popouts (stable `.user-profile-popout` classes), layer-container
  menus, slash-command autocomplete, settings radios, status-menu
  separators, typing dots and role dots — using current and hash-resistant
  (`[class^="name_"]`) selectors.
- Variable usages now degrade gracefully where Discord dropped a variable
  (e.g. `--button-secondary-background` → `--control-secondary-*`,
  `--brand-experiment`, `--info-danger-background`, elevations).

### Removed (dead for years — pre-2023 Discord unless noted)

- 120+ rules targeting removed hashed classes (`.userPopout-…`,
  `.mainContent-…`, tooltips, status picker, appearance-preview cards,
  "Twitter-like forum", the "sus link" modal, perks modal, legacy switches…).
  Working features were re-implemented with current selectors (see above).
- Third-party hotlinked images: Imgur default-avatar swap, Flaticon NSFW
  swap, Among Us cursor image, expired Discord CDN attachment previews,
  and an unrelated loading GIF host.
- Imports: NFLD99 `DiscordFont.css` (Whitney-era, conflicts with the theme
  font), the archived CreArts Friends-Grid remote CSS (2023; this repo's own
  `FriendGrid.css` is used), and the empty `ChillaxTag.css` request.
- Upstream support-server custom icons (not a BTcord server).

### BTcord identity (upstream credit retained per licence terms)

- Title-bar wordmark: **btcord** (hover: "btcord x chillax"); Settings info
  line reads "BTcord …"; Chillax Squad stays in `@author`, the credits block
  and this repo's README. BetterDiscord card styling covers `#BTcord-card`
  in addition to `#Chillax-card`.
- Unread-divider gradient and other hardcoded Chillax-red values now read
  `--accentcolorV2` / `--bt-accent-2`.

### Performance & housekeeping

- Google Fonts: 5 requests → 1, only weights the theme uses.
- Default wallpaper re-encoded 5.3 MB PNG → optimised JPG
  (`Wallpapers/btcord-default.jpg`); original retained.
- `HideAnnoyingElements`: matches Visual Refresh `<button>` elements and
  can also hide the GIF picker, Apps button and Activities entry.
- `ColoredLinks`: X (`x.com`), Bluesky and Reddit added; Discord links use
  modern blurple `#5865f2`.
- Reduced-motion support (`prefers-reduced-motion`), visible
  `:focus-visible` outlines, themed text selection.
- Fixed invalid CSS found along the way (`width: 100;`, `rgb(0, 0, 0.9)`).
- Added `btcord.bundle.theme.css`: a single-file build (via
  `scripts/build-bundle.py`) with a direct raw-GitHub download/Online-Themes
  link that works without GitHub Pages.
- Added `.nojekyll`, `preview.html` mock, and `scripts/check-css.py`
  (syntax + dead-selector checker for future Discord updates).

---

_upstream history before this fork: [warrayquipsome/Chillax](https://github.com/warrayquipsome/Chillax) (last synced commit `9536ba1`, "fix: fixed friend list avatar decoration cropping")._
