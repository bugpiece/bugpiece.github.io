# Repository Guidelines

## Project Structure & Module Organization
Content lives in `_pages`, `_posts`, `_portfolio`, `_talks`, and `_teaching`, each driven by layouts in `_layouts` and reusable snippets in `_includes`. Styles sit under `_sass`, while source scripts belong in `assets/js/_main.js` and compile to `assets/js/main.min.js`; treat `_site/` as disposable output. Use the `markdown_generator/` helpers only when bulk-importing data and keep ad hoc assets in `assets/` or `files/` so links remain stable.

## Build, Test, and Development Commands
Install Ruby gems with `bundle install` and JavaScript dependencies with `npm install` when working on assets. Run `bundle exec jekyll serve --livereload --host localhost` for a live preview at http://localhost:4000 and quick feedback on build issues. Before pushing, run `bundle exec jekyll build` for a clean production render and `npm run build:js` whenever anything under `assets/js/` changes to refresh the minified bundle.

## Coding Style & Naming Conventions
Keep YAML front matter keys lowercase with underscores (e.g., `layout`, `permalink`) and indent nested lists in Markdown by two spaces to match existing posts. Aim for ~100-character lines, prefer reference-style links, and lean on the theme’s utility classes instead of bespoke inline HTML. SCSS additions should extend the partials in `_sass/`, while JavaScript follows the existing IIFE pattern in `_main.js` for compatibility with `uglify`.

## Testing Guidelines
Treat `bundle exec jekyll build` as the baseline regression test and resolve any warnings or missing-asset notices. For visual changes, preview with `bundle exec jekyll serve`, then spot-check the home, about, teaching, and talks pages on both desktop and mobile widths. If navigation, search, or other scripts change, rerun `npm run build:js` and verify the console stays clean before shipping.

## Commit & Pull Request Guidelines
Write concise, action-oriented commit messages mirroring the current history (e.g., `Fix typo in excerpt for SUBARU project description`) and keep unrelated work in separate commits. Pull requests should summarize intent, reference any GitHub issue, and note the commands used for verification. Include screenshots or GIFs for layout changes and mention new content paths so reviewers can reproduce your checks quickly.

## Content Authoring Tips
Store structured lists (publications, talks, courses) in `_data/` to reduce duplication across pages. Place downloads in `files/` and reference them with `/files/<filename>` links to keep URLs consistent. Use front-matter flags (such as `header` or `sidebar`) instead of inline styling so future theme updates remain drop-in.
