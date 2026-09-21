# Repository Guidelines

## What this repository is

Personal academic website for Daichi Kusumoto, built with **Jekyll** and
deployed to **GitHub Pages** at <https://bugpiece.github.io>. It started from the
academicpages theme with these main pages:

- **Home** — `_pages/about.md` (`permalink: /`); bio plus the Education and
  Research Experience blocks.
- **Publications** — `_pages/publications.md`; rendered from data.
- **News** — `_pages/news.md`; short updates from `news/<slug>/index.md`.
  Each article keeps its WebP photos in the same folder. See `docs/news.md`.

The header also links a **CV** entry directly to a PDF in `files/`. The old demo
collections (blog posts, talks, teaching, portfolio) and their tooling have been
removed.

## Project structure

- `_pages/` — the live pages only: `about.md`, `publications.md`, `404.md`,
  `sitemap.md`.
- `_data/` — structured content:
  - `publications.yml` — journal/conference entries (the source of the
    Publications page).
  - `navigation.yml` — the header menu (`main:` list).
  - `authors.yml`, `ui-text.yml`, `comments/` — theme data.
- `_includes/`, `_layouts/` — theme templates. `_includes/minifeature_row`
  renders the Education / Research Experience items on the home page.
- `_sass/` — styles. `_archive.scss` holds the minifeature + date-column layout;
  `_pub.scss` holds Publications-page tweaks.
- `assets/` — compiled CSS/JS (`assets/js/main.min.js`); `images/`; `files/`
  (PDFs: CV, master thesis, slides).
- `_config.yml` — site configuration. `.github/workflows/jekyll.yml` — the
  deploy workflow. `_site/` — generated output; disposable and gitignored.

Note: `_config.yml` still declares `teaching`/`publications`/`portfolio`/`talks`
collections, but those directories were deleted and only `publications.yml`
data is actually used.

## Common edits

- **Add a publication:** append an entry to `_data/publications.yml`
  (`type: journal|conference`, `date`, `title`, `authors`, `venue`, optional
  `note` / `location`). `publications.md` groups entries by year automatically.
- **Add news:** copy `docs/news-template.md` to `news/<slug>/index.md`.
  Put HEIC/JPEG/PNG/WebP photos beside the article; `sh scripts/jekyll.sh build`
  converts them to WebP (long edge at most 1200px), registers them in front matter,
  and deletes input originals only after verifying the WebP and updating the article.
  Keep the folder name stable: it defines the article URL.
- **Edit bio / Education / Research Experience:** `_pages/about.md` — the
  `feature_*` front-matter blocks and the page body.
- **Header menu:** `_data/navigation.yml`. Keep the `main:` list clean — a
  commented-out or empty list item still renders as a blank tab.
- **Update the CV:** put the new PDF in `files/` and point the `CV` entry's
  `url` in `navigation.yml` at it (remove the old PDF).

## Build and preview

- Ruby **3.1.4** (`.ruby-version`). Install gems with `bundle install`.
- Local commands use the existing `gh auth login` session through `scripts/jekyll.sh`;
  credentials are passed in memory, never saved in the repository.
- Live preview: `sh scripts/jekyll.sh serve --livereload` → <http://localhost:4000>.
- Production build check: `sh scripts/jekyll.sh build` (writes to `_site/`);
  resolve any warnings.
- There is **no Node/JS build step** anymore (`package.json` and the JS tooling
  were removed). `assets/js/main.min.js` is committed as-is; editing
  `assets/js/_main.js` will not regenerate it without reintroducing a toolchain.

## Deploy

Pushing to `master` triggers `.github/workflows/jekyll.yml`, which builds with
Jekyll (`JEKYLL_ENV=production`) and publishes to GitHub Pages. No manual build
or upload is needed — check the **Actions** tab for status.

## Conventions

- YAML front-matter keys stay lowercase with underscores; indent nested lists by
  two spaces.
- Store downloads in `files/` and link them as `/files/<name>`; images in
  `images/`, except News photos, which live alongside their article.
- Extend styles through the `_sass/` partials rather than inline CSS.
- Links use the text color normally (including visited links); use `#38609C`
  only on hover site-wide.
  `_sass/_links.scss` enforces this across theme components.
- Write concise, action-oriented commit messages (e.g. "Fix CV nav position by
  removing empty menu entries"). Commit or push only when the maintainer asks.
