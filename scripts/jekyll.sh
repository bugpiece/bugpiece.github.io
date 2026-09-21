#!/bin/sh
# Reuse GitHub CLI credentials in memory; never write tokens to the repository.
set -eu
set +x

cd "$(dirname "$0")/.."

case "${1:-}" in
  build|serve|s)
    if [ ! -x local/news-venv/bin/python ]; then
      python3 -m venv local/news-venv
    fi
    if ! local/news-venv/bin/python -c 'import PIL, pillow_heif, yaml' 2>/dev/null; then
      local/news-venv/bin/python -m pip install -r scripts/news-requirements.txt
    fi
    local/news-venv/bin/python scripts/news-images.py --prepare
    ;;
esac

if [ -z "${JEKYLL_GITHUB_TOKEN:-}" ]; then
  JEKYLL_GITHUB_TOKEN="$(gh auth token --hostname github.com)"
  export JEKYLL_GITHUB_TOKEN
fi

exec bundle exec jekyll "$@"
