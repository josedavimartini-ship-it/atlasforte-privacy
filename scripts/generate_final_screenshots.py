"""Generate higher-fidelity 1080x1920 screenshots with captions and a subtle device frame.

Usage: python scripts/generate_final_screenshots.py -s assets/store_listing/final/icon_source.png
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import argparse

SURFACE_BG = (250, 250, 248)
ACCENT = (15, 44, 51)
TEXT = (20, 28, 36)

CAPS = [
    ('Visão geral e saldo', 'Veja seu saldo e principais métricas em um relance'),
    ('Registrar despesas', 'Registre transações em segundos'),
    ('Orçamentos & metas', 'Crie orçamentos e acompanhe seu progresso'),
    ('Relatórios & insights', 'Relatórios detalhados e insights inteligentes')
]


def make_device_frame(img: Image.Image) -> Image.Image:
    w, h = img.size
    # create a simple rounded rectangle mask to simulate a phone inset
    frame = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    margin = 40
    radius = 40
    draw.rounded_rectangle([margin, margin, w - margin, h - margin], radius=radius, fill=(255,255,255,255))
    # add shadow
    shadow = Image.new('RGBA', (w, h), (0,0,0,0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([margin+4, margin+8, w-margin-4, h-margin+4], radius=radius, fill=(0,0,0,100))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    out = Image.alpha_composite(shadow, frame)
    out = Image.alpha_composite(out, img.convert('RGBA'))
    return out


def fit_into(img: Image.Image, w:int, h:int):
    scale = min(w/img.width, h/img.height)
    return img.resize((int(img.width*scale), int(img.height*scale)), Image.LANCZOS)


def generate(source: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Image.open(source).convert('RGBA')

    title_font = None
    sub_font = None
    try:
        title_font = ImageFont.truetype('arialbd.ttf', 56)
        sub_font = ImageFont.truetype('arial.ttf', 28)
    except Exception:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

    for i, (cap, sub) in enumerate(CAPS, start=1):
        bg = Image.new('RGB', (1080, 1920), SURFACE_BG)
        draw = ImageDraw.Draw(bg)
        # gradient header
        for y in range(0, 360):
            r = int(230 - (y/360)*60)
            g = int(230 - (y/360)*80)
            b = int(230 - (y/360)*80)
            draw.line([(0,y),(1080,y)], fill=(r,g,b))
        # paste a big circular hero using the source
        hero = fit_into(src, 720, 720).convert('RGBA')
        # create circular mask
        mask = Image.new('L', hero.size, 0)
        ImageDraw.Draw(mask).ellipse([0,0,hero.size[0], hero.size[1]], fill=255)
        x = 180
        y = 220
        bg.paste(hero, (x,y), mask)
        # add title and subtitle
        tx = 540
        ty = 260
        draw.text((tx, ty), cap, fill=TEXT, font=title_font)
        draw.text((tx, ty+80), sub, fill=TEXT, font=sub_font)
        # optional CTA pill
        pill_w, pill_h = 420, 80
        pill_x, pill_y = (540, 400)
        draw.rounded_rectangle([pill_x, pill_y, pill_x+pill_w, pill_y+pill_h], radius=40, fill=ACCENT)
        draw.text((pill_x+30, pill_y+18), 'Abra o Atlas Fortis', fill=(255,255,255), font=sub_font)

        # place the mock phone frame composite
        framed = make_device_frame(bg)
        out_path = out_dir / f'screenshot_final{i}_1080x1920.png'
        framed.convert('RGB').save(out_path, quality=90)
        print('Wrote', out_path)

    # Update README note
    readme = out_dir.parent / 'README_STORE_ASSETS_FINAL.md'
    text = readme.read_text() if readme.exists() else ''
    note = '\nFinal screenshots: screenshot_final1_1080x1920.png .. screenshot_final4_1080x1920.png\n'
    if note.strip() not in text:
        readme.write_text(text + '\n' + note)
        print('Appended final screenshots note to', readme)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-s', '--source', required=True)
    p.add_argument('-o', '--out', default='assets/store_listing/final')
    args = p.parse_args()
    generate(Path(args.source), Path(args.out))
