#!/usr/bin/env sh
# Zip each skill for upload to claude.ai (Customize > Skills > Upload a skill).
# Each zip holds one folder named after the skill, with SKILL.md inside.
set -eu
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for dir in skills/*/; do
  name=$(basename "$dir")
  (cd skills && zip -qr "../dist/$name.zip" "$name")
  echo "dist/$name.zip"
done
