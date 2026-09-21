#!/usr/bin/env python3
"""Prepare News photos, or import photos alongside articles with --prepare."""
import argparse
import datetime
import io
import re
from pathlib import Path

import yaml
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener

register_heif_opener(thumbnails=False)
ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = {'.heic', '.heif', '.jpg', '.jpeg', '.png', '.webp'}


class FrontMatterDumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def encode(source):
    with Image.open(source) as original:
        if original.format != 'HEIF' and getattr(original, 'is_animated', False):
            raise ValueError(f'Animated images are not supported: {source}')
        photo = ImageOps.exif_transpose(original).convert('RGBA')
        icc = photo.info.get('icc_profile')
        photo.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
        photo.info.clear()
        encoded = io.BytesIO()
        photo.save(encoded, 'WEBP', quality=85, method=6,
                   **({'icc_profile': icc} if icc else {}))
        return encoded.getvalue(), photo.width, photo.height


def next_target(folder):
    number = 1
    while (folder / f'photo-{number:02d}.webp').exists():
        number += 1
    return folder / f'photo-{number:02d}.webp'


def read_article(index):
    if not index.exists():
        match = re.match(r'\d{4}-\d{2}-\d{2}', index.parent.name)
        date = datetime.date.fromisoformat(match[0]) if match else datetime.date.today()
        return {'layout': 'news_article', 'title': index.parent.name,
                'date': date, 'published': False, 'photos': []}, '\nWrite a short update here.\n'
    match = re.fullmatch(r'---\r?\n(.*?)\r?\n---\r?\n(.*)', index.read_text(), flags=re.S)
    if not match:
        raise ValueError(f'Expected YAML front matter: {index}')
    data = yaml.safe_load(match[1])
    if not isinstance(data, dict) or data.get('layout') != 'news_article':
        raise ValueError(f'Expected layout: news_article in {index}')
    if not isinstance(data.get('photos', []), list):
        raise ValueError(f'Expected a photos list in {index}')
    return data, match[2]


def write_article(index, data, body):
    front = yaml.dump(data, Dumper=FrontMatterDumper, sort_keys=False, allow_unicode=True)
    temporary = index.with_name('.index.md.tmp')
    temporary.write_text(f'---\n{front}---\n{body}')
    temporary.replace(index)


def natural_key(path):
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', path.name)]


def prepare(folder):
    candidates = sorted((p for p in folder.iterdir() if p.is_file()
                         and p.suffix.lower() in EXTENSIONS), key=natural_key)
    if not candidates:
        return
    index = folder / 'index.md'
    data, body = read_article(index)
    photos = data.setdefault('photos', [])
    registered = {photo['file'] for photo in photos}
    for source in candidates:
        # Registered WebP files already belong to the article; never recompress them.
        if source.suffix.lower() == '.webp' and source.name in registered:
            continue
        encoded, width, height = encode(source)
        target = next_target(folder)
        with target.open('xb') as output:
            output.write(encoded)
        with Image.open(target) as check:
            check.load()
            if check.size != (width, height):
                raise ValueError(f'Unexpected output dimensions: {target}')
        entry = next((photo for photo in photos if photo['file'] == source.name), None)
        if entry is None:
            entry = {'alt': ''}
            photos.append(entry)
        entry.update(file=target.name, width=width, height=height)
        try:
            write_article(index, data, body)
        except OSError:
            target.unlink()
            raise
        # Delete the input only after verifying the WebP and updating the article.
        source.unlink()
        print(f'{folder.name}: {source.name} -> {target.name} ({width}x{height})')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare', action='store_true', help='Import photos in all News folders')
    parser.add_argument('slug', nargs='?', help='News folder, e.g. 2026-08-24_lab-join')
    parser.add_argument('images', type=Path, nargs='*')
    args = parser.parse_args()
    try:
        if args.prepare:
            if args.slug or args.images:
                parser.error('--prepare does not take a slug or image paths')
            for folder in sorted((ROOT / 'news').iterdir()):
                if folder.is_dir():
                    prepare(folder)
            return
        if not args.slug or not args.images:
            parser.error('Provide a slug and images, or use --prepare')
        if not re.fullmatch(r'[a-z0-9]+(?:[-_][a-z0-9]+)*', args.slug):
            parser.error('Use lowercase letters, numbers, hyphens and underscores for the slug')
        output = ROOT / 'news' / args.slug
        output.mkdir(parents=True, exist_ok=True)
        photos = []
        for source in args.images:
            encoded, width, height = encode(source)
            target = next_target(output)
            with target.open('xb') as destination:
                destination.write(encoded)
            photos.append({'file': target.name, 'alt': '', 'width': width, 'height': height})
        print(yaml.dump({'photos': photos}, Dumper=FrontMatterDumper, sort_keys=False))
    except (OSError, ValueError, yaml.YAMLError) as error:
        parser.exit(1, f'News images: {error}\n')


if __name__ == '__main__':
    main()
