# Repository Guidelines

## What this repository is

Personal academic website for Daichi Kusumoto, built with **Jekyll** and
deployed to **GitHub Pages** at <https://bugpiece.github.io>. It started from the
academicpages theme but has been trimmed down to two live pages:

- **Home** — `_pages/about.md` (`permalink: /`); bio plus the Education and
  Research Experience blocks.
- **Publications** — `_pages/publications.md`; rendered from data.

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
- **Edit bio / Education / Research Experience:** `_pages/about.md` — the
  `feature_*` front-matter blocks and the page body.
- **Header menu:** `_data/navigation.yml`. Keep the `main:` list clean — a
  commented-out or empty list item still renders as a blank tab.
- **Update the CV:** put the new PDF in `files/` and point the `CV` entry's
  `url` in `navigation.yml` at it (remove the old PDF).

## Build and preview

- Ruby **3.1.4** (`.ruby-version`). Install gems with `bundle install`.
- Live preview: `bundle exec jekyll serve --livereload` → <http://localhost:4000>.
- Production build check: `bundle exec jekyll build` (writes to `_site/`);
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
  `images/`.
- Extend styles through the `_sass/` partials rather than inline CSS.
- Write concise, action-oriented commit messages (e.g. "Fix CV nav position by
  removing empty menu entries"). Commit or push only when the maintainer asks.
