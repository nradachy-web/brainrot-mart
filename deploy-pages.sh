#!/bin/bash
set -e
cd "$(dirname "$0")"
REPO=$(git ls-remote --get-url origin)
TMP=$(mktemp -d)
cp -R public "$TMP/site"
find "$TMP/site" -name '*.html' -exec sed -i '' -E 's#(src|href)="/#\1="./#g' {} +
cd "$TMP/site"
git init -q -b gh-pages
git add -A
git commit -qm "deploy $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git push -f "$REPO" gh-pages:gh-pages
rm -rf "$TMP"
echo "pushed gh-pages"
