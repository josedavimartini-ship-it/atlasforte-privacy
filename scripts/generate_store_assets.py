"""
Generate Play Store assets from a single source icon image.

Usage examples:
  python scripts/generate_store_assets.py -s assets/store_listing/final/icon_source.png
  python scripts/generate_store_assets.py --source path/to/new_icon.png --out assets/store_listing/final --force

Outputs (by default to `assets/store_listing/final`):
 - icon_512.png (512x512)
 - feature_1024x500.png (1024x500)
 - screenshot1..4_1080x1920.png
 - README_STORE_ASSETS_FINAL.md (updated with generation note)

Requires: Pillow
"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys

try:
    from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
except Exception as e:
    print('This script requires Pillow. Install with: pip install pillow')
    raise

SURFACE_BG = (231, 228, 223, 255)  # neutral background
ACCENT = (15, 44, 51, 255)
TEXT_MAIN = (31, 36, 40)
TEXT_SUB = (74, 84, 93)

CAPTIONS_PT = [
    'Visão geral e saldo',
    'Registrar despesas em segundos',
    'Orçamentos e metas',
    'Relatórios e insights'
]


def fit_into(img: Image.Image, box_w: int, box_h: int) -> Image.Image:
    w, h = img.size
    scale = min(box_w / w, box_h / h)
    new = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    return new


def load_font(preferred: str, size: int):
    try:
        return ImageFont.truetype(preferred, size)
    except Exception:
        try:
            return ImageFont.truetype('arial.ttf', size)
        except Exception:
            return ImageFont.load_default()


def generate(source: Path, out_dir: Path, force=False, skip_screens=False):
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Image.open(source).convert('RGBA')

    # icon_512
    icon512 = Image.new('RGBA', (512, 512), SURFACE_BG)
    resized = fit_into(src, 420, 420)
    icon512.paste(resized, ((512 - resized.width) // 2, (512 - resized.height) // 2), resized)
    # subtle vignette
    mask = Image.new('L', (512, 512), 0)
    ImageDraw.Draw(mask).ellipse([12, 12, 500, 500], fill=255)
    shadow = ImageOps.invert(mask).filter(ImageFilter.GaussianBlur(40))
    icon512 = Image.composite(icon512, Image.new('RGBA', (512, 512), ACCENT), shadow)
    icon_path = out_dir / 'icon_512.png'
    if not icon_path.exists() or force:
        icon512.save(icon_path)
        print('Wrote', icon_path)
    else:
        print('Exists, skipping', icon_path)

    # feature graphic 1024x500
    feat = Image.new('RGBA', (1024, 500), SURFACE_BG)
    feat_thumb = fit_into(src, 420, 420)
    feat.paste(feat_thumb, (40, (500 - feat_thumb.height) // 2), feat_thumb)
    draw = ImageDraw.Draw(feat)
    title_font = load_font('arialbd.ttf', 48)
    sub_font = load_font('arial.ttf', 18)
    text_x = 420
    draw.text((text_x, 160), 'Atlas Fortis Financial', fill=TEXT_MAIN, font=title_font)
    draw.text((text_x, 210), 'Atlas Forte Financeiro — Fortis, o guardião do tesouro', fill=TEXT_SUB, font=sub_font)
    feat_path = out_dir / 'feature_1024x500.png'
    if not feat_path.exists() or force:
        feat.save(feat_path)
        print('Wrote', feat_path)
    else:
        print('Exists, skipping', feat_path)

    # screenshots
    if not skip_screens:
        cap_font = load_font('arialbd.ttf', 36)
        for i, cap in enumerate(CAPTIONS_PT, start=1):
            sc = Image.new('RGBA', (1080, 1920), SURFACE_BG)
            d = ImageDraw.Draw(sc)
            d.rectangle([0, 0, 1080, 160], fill=ACCENT)
            thumb = fit_into(src, 360, 360)
            sc.paste(thumb, (60, 220), thumb)
            # caption
            try:
                bbox = d.textbbox((0, 0), cap, font=cap_font)
                w = bbox[2] - bbox[0]
            except Exception:
                w = d.textlength(cap)
            d.text(((1080 - w) // 2, 1620), cap, fill=TEXT_MAIN, font=cap_font)
            sc_path = out_dir / f'screenshot{i}_1080x1920.png'
            if not sc_path.exists() or force:
                sc.save(sc_path)
                print('Wrote', sc_path)
            else:
                print('Exists, skipping', sc_path)

    # README note
    readme = out_dir.parent / 'README_STORE_ASSETS_FINAL.md'
    note = '\nGenerated with scripts/generate_store_assets.py from: {}\n'.format(source.name)
    if readme.exists():
        txt = readme.read_text()
        if note.strip() not in txt:
            readme.write_text(txt + '\n' + note)
            print('Appended generation note to', readme)
    else:
        readme.write_text('''Final store assets generated from user source icon.\n\nFiles created:\n- icon_source.png (original provided)\n- icon_512.png (512x512 app icon)\n- feature_1024x500.png (feature graphic)\n- screenshot1_1080x1920.png .. screenshot4_1080x1920.png (phone screenshots)\n\nUpload instructions:\n- App icon: upload icon_512.png (PNG, 512x512)\n- Feature graphic: upload feature_1024x500.png\n- Screenshots: upload the 4 phone screenshots\n\n''')
        print('Wrote', readme)


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument('-s', '--source', required=True, help='Path to source icon PNG')
    p.add_argument('-o', '--out', default='assets/store_listing/final', help='Output directory')
    p.add_argument('-f', '--force', action='store_true', help='Overwrite existing outputs')
    p.add_argument('--skip-screens', action='store_true', help='Skip generating screenshots')
    args = p.parse_args(argv)

    src = Path(args.source)
    if not src.exists():
        print('Source file not found:', src)
        sys.exit(2)
    try:
        generate(src, Path(args.out), force=args.force, skip_screens=args.skip_screens)
    except Exception as e:
        print('Error generating assets:', e)
        raise


if __name__ == '__main__':
    main()
