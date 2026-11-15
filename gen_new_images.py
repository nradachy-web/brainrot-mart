import os
import io
import math
import random
from PIL import Image, ImageDraw, ImageFilter

OUT = os.path.join(os.path.dirname(__file__), 'public', 'images')
W, H = 1280, 720
INK = (10, 10, 13)
SIL = (5, 5, 7)
LINE = (26, 26, 31)
LIME = (200, 255, 46)
PINK = (255, 45, 120)
CREAM = (242, 236, 220)

ITEMS = {
    'ball-and-chain': [
        ('dark concrete floor, a heavy cast iron ball and chain coiled on the ground, one end a metal manacle, acid lime and hot pink rim light'),
        ('close up of a riveted iron chain link and a metal manacle on a dark floor, lime and pink rim light'),
    ],
    'herstory-correction-fluid': [
        ('a vintage glass bottle of white correction fluid beside a fine brush and a typed document covered in white-out strokes, dark table'),
        ('close up of a brush laying thick white fluid over small printed text on paper'),
    ],
    'italian-time-zone-clock': [
        ('a round analog wall clock with blurred hands suggesting lateness, dark room, acid lime glow behind it'),
        ('close up of a clock face with the hour hand decorative and the minute hand smudged out of position'),
    ],
    'gender-reveal-cannon': [
        ('a small brass confetti cannon firing a burst of blue confetti into a dark room, hot pink rim light'),
        ('close up of blue confetti rounds stacked in dark wooden crates'),
    ],
    'stepford-microwave': [
        ('a retro 1970s microwave with a single dial and a soft interior glow, dark kitchen, lime light from inside'),
        ('close up of a microwave interior with a lazy susan plate turning in soft lime light'),
    ],
    'mansplaining-removal': [
        ('a large chalk speech bubble on a dark wall being scraped clean by a wide scraper, dust falling, lime rim light'),
        ('close up of a metal scraper blade removing chalk lines from a dark board, pink rim light'),
    ],
    'irish-wake-crew': [
        ('three lit candles on a dark wooden pub table beside a dark stout in a glass, warm flicker, pink rim light'),
        ('close up of candle wax dripping on a dark wooden table with a pint glass blurred behind'),
    ],
    'scottish-invoice-audit': [
        ('a long paper receipt held by metal tongs over a sealed glass jar with a few coins, dark desk, lime glow'),
        ('close up of a sealed glass jar holding three coins and a folded receipt, dark table'),
    ],
    'italian-wedding-rsvp': [
        ('a stack of wedding invitations tied with ribbon, a fork stabbed into the top envelope, dark table, pink glow'),
        ('close up of a handwritten RSVP list overflowing off the paper, fork resting on it'),
    ],
}


def glow(img, pos, color, r, a):
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.ellipse([pos[0] - r, pos[1] - r, pos[0] + r, pos[1] + r], fill=color + (a,))
    layer = layer.filter(ImageFilter.GaussianBlur(r * 0.6))
    img.paste(Image.alpha_composite(img.convert('RGBA'), layer).convert('RGB'), (0, 0))


def arc(d, box, color, start, end, w):
    d.arc(box, start=start, end=end, fill=color, width=w)


def base(corner=0):
    img = Image.new('RGB', (W, H), INK)
    corners = [(180, 160, LIME), (1100, 560, PINK), (1100, 160, PINK), (180, 560, LIME)]
    c1, c2 = corners[corner], corners[(corner + 1) % 4]
    glow(img, (c1[0], c1[1]), c1[2], 260, 70)
    glow(img, (c2[0], c2[1]), c2[2], 220, 55)
    return img


def ball_and_chain(d, zoom):
    cx, cy = 540, 470
    r = 175
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SIL)
    arc(d, [cx - r, cy - r, cx + r, cy + r], LIME, 150, 250, 10)
    arc(d, [cx - r, cy - r, cx + r, cy + r], PINK, 320, 70, 7)
    for i in range(5):
        lx, ly = cx + 150 + i * 95, cy - 110 - i * 68
        rr = 46
        d.ellipse([lx - rr, ly - rr, lx + rr, ly + rr], outline=(14, 14, 17), width=20)
        arc(d, [lx - rr, ly - rr, lx + rr, ly + rr], LIME, 160, 240, 5)
    d.ellipse([cx - 120, cy - r - 30, cx + 120, cy - r + 26], outline=(16, 16, 19), width=16)
    arc(d, [cx - 120, cy - r - 30, cx + 120, cy - r + 26], PINK, 180, 330, 5)


def herstory(d, zoom):
    x0, y = 380, 250
    for i in range(6):
        wln = 520 if i != 2 else 300
        d.rectangle([x0, y, x0 + wln, y + 12], fill=(70, 68, 62))
        y += 46
    d.rectangle([x0 - 30, 268, x0 + 560, 310], fill=(232, 230, 226))
    d.polygon([(x0 + 560, 268), (x0 + 600, 289), (x0 + 560, 310)], fill=(120, 118, 114))
    d.rectangle([x0 - 40, 470, x0 + 60, 560], fill=(30, 30, 34))
    d.rectangle([x0 - 30, 440, x0 + 50, 472], fill=(20, 20, 24))
    glow_note = None


def clock(d, zoom):
    cx, cy, r = 620, 360, 190
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(16, 16, 20), outline=(34, 34, 40), width=10)
    for i in range(12):
        a = math.radians(i * 30 - 90)
        x1, y1 = cx + math.cos(a) * (r - 24), cy + math.sin(a) * (r - 24)
        x2, y2 = cx + math.cos(a) * (r - 6), cy + math.sin(a) * (r - 6)
        d.line([x1, y1, x2, y2], fill=(90, 88, 80), width=6)
    for off in range(10):
        a = math.radians(200 - off * 3)
        d.line([cx, cy, cx + math.cos(a) * 150, cy + math.sin(a) * 150], fill=(242, 236, 220, 90), width=5)
    d.line([cx, cy, cx + 60, cy + 24], fill=CREAM, width=12)
    d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=PINK)


def cannon(d, zoom):
    bx, by = 420, 470
    d.rectangle([bx - 90, by - 40, bx + 240, by + 40], fill=(28, 22, 20))
    arc(d, [bx - 90, by - 46, bx + 240, by + 46], PINK, 300, 355, 6)
    d.rectangle([bx + 240, by - 52, bx + 300, by + 52], fill=(36, 30, 26))
    d.polygon([(bx - 60, by + 40), (bx - 110, by + 150), (bx - 40, by + 150)], fill=(18, 18, 20))
    d.polygon([(bx + 120, by + 40), (bx + 80, by + 150), (bx + 160, by + 150)], fill=(18, 18, 20))
    rnd = random.Random(7)
    for i in range(70):
        t = rnd.random()
        x = bx + 300 + t * 520 + rnd.randint(-40, 40)
        y = by - t * 320 + rnd.randint(-160, 120)
        rr = rnd.randint(3, 9)
        col = (74, 168, 255) if rnd.random() > 0.18 else (200, 255, 46)
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=col)
    glow_note = (bx + 520, by - 260, (74, 168, 255), 200, 60)


def microwave(d, zoom):
    x0, y0, x1, y1 = 400, 220, 900, 520
    d.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=(16, 16, 19), outline=(30, 30, 35), width=6)
    d.rounded_rectangle([x0 + 34, y0 + 34, x1 - 220, y1 - 34], radius=10, fill=(7, 7, 11), outline=(26, 26, 30), width=4)
    d.ellipse([x0 + 150, y0 + 190, x0 + 300, y0 + 230], outline=(120, 150, 60), width=4)
    d.line([x0 + 120, y1 - 60, x1 - 250, y1 - 60], fill=(40, 44, 32), width=4)
    d.ellipse([x1 - 150, y0 + 60, x1 - 80, y0 + 130], fill=(24, 24, 28), outline=PINK, width=4)
    d.rounded_rectangle([x1 - 150, y0 + 170, x1 - 80, y0 + 220], radius=8, fill=(22, 22, 26))
    d.rounded_rectangle([x1 - 150, y0 + 240, x1 - 80, y0 + 290], radius=8, fill=(22, 22, 26))
    glow_note = (x0 + 250, (y0 + y1) // 2, LIME, 120, 60)


def bubble(d, zoom):
    d.rounded_rectangle([380, 210, 900, 440], radius=34, fill=(14, 14, 18), outline=(40, 40, 46), width=6)
    d.polygon([(470, 440), (430, 540), (540, 440)], fill=(14, 14, 18), outline=(40, 40, 46))
    y = 260
    for i in range(4):
        d.line([420, y, 420 + (430 - i * 60), y], fill=(210, 206, 198), width=9)
        y += 44
    d.rectangle([700, 190, 820, 470], fill=(224, 222, 218))
    d.rectangle([700, 470, 820, 520], fill=(36, 36, 40))
    for i in range(6):
        x = 720 + i * 14
        d.line([x, 500, x + 40, 640], fill=(120, 118, 112), width=3)


def wake(d, zoom):
    for i, x in enumerate((520, 620, 720)):
        hh = 150 - i * 24
        d.rectangle([x - 18, 520 - hh, x + 18, 520], fill=(226, 220, 206))
        fx, fy = x, 520 - hh - 26
        d.ellipse([fx - 10, fy - 20, fx + 10, fy + 20], fill=(242, 201, 76))
        d.ellipse([fx - 4, fy - 10, fx + 4, fy + 6], fill=(255, 240, 200))
    px0, px1 = 840, 950
    d.polygon([(px0, 320), (px1, 320), (px1 - 14, 540), (px0 + 14, 540)], fill=(24, 16, 14))
    d.polygon([(px0, 320), (px1, 320), (px1 - 6, 400), (px0 + 6, 400)], fill=(58, 26, 18))
    d.rounded_rectangle([px0 - 10, 300, px1 + 10, 330], radius=8, fill=(220, 214, 200))
    d.rectangle([300, 540, 1000, 560], fill=(18, 18, 20))
    glow_note = (620, 330, (242, 201, 76), 170, 48)


def audit(d, zoom):
    rx0, ry0 = 560, 230
    d.rectangle([rx0, ry0, rx0 + 200, ry0 + 380], fill=(216, 212, 202))
    for i in range(7):
        yy = ry0 + 40 + i * 42
        d.line([rx0 + 20, yy, rx0 + 180 - (i % 3) * 40, yy], fill=(90, 88, 82), width=5)
    zx = rx0
    pts = [(zx, ry0 + 380)]
    while zx < rx0 + 200:
        zx += 20
        pts.append((zx, ry0 + 380 + (14 if (zx // 20) % 2 else 0)))
    d.polygon(pts + [(rx0 + 200, ry0 + 372), (rx0, ry0 + 372)], fill=(216, 212, 202))
    d.line([rx0 - 60, ry0 - 180, rx0 + 30, ry0 + 6], fill=(60, 62, 66), width=10)
    d.line([rx0 + 260, ry0 - 180, rx0 + 170, ry0 + 6], fill=(60, 62, 66), width=10)
    d.ellipse([rx0 + 40, ry0 - 210, rx0 + 160, ry0 - 150], fill=(24, 24, 28))
    jx, jy = 340, 430
    d.rounded_rectangle([jx, jy, jx + 170, jy + 190], radius=20, outline=(46, 46, 52), width=8)
    d.rectangle([jx + 30, jy - 24, jx + 140, jy], fill=(30, 30, 34))
    for i in range(3):
        d.ellipse([jx + 30 + i * 34, jy + 120, jx + 66 + i * 34, jy + 156], fill=(255, 210, 74))


def rsvp(d, zoom):
    ex, ey = 430, 250
    d.rectangle([ex, ey, ex + 420, ey + 280], fill=(232, 228, 220))
    d.line([ex, ey, ex + 210, ey + 150], fill=(150, 146, 138), width=6)
    d.line([ex + 420, ey, ex + 210, ey + 150], fill=(150, 146, 138), width=6)
    d.rectangle([ex - 60, ey + 60, ex + 30, ey + 330], fill=(222, 218, 210))
    d.rectangle([ex + 400, ey + 90, ex + 480, ey + 340], fill=(214, 210, 202))
    d.line([ex + 640, ey - 60, ex + 560, ey + 220], fill=(120, 122, 128), width=10)
    for i in range(4):
        d.line([ex + 640 + i * 18, ey - 60, ex + 628 + i * 18, ey + 10], fill=(120, 122, 128), width=6)
    y = ey + 330
    for i in range(3):
        d.rectangle([300 + i * 30, y, 470 + i * 30, y + 8], fill=(255, 45, 120))
    glow_note = (ex + 210, ey + 380, PINK, 190, 50)


FN = {
    'ball-and-chain': ball_and_chain,
    'herstory-correction-fluid': herstory,
    'italian-time-zone-clock': clock,
    'gender-reveal-cannon': cannon,
    'stepford-microwave': microwave,
    'mansplaining-removal': bubble,
    'irish-wake-crew': wake,
    'scottish-invoice-audit': audit,
    'italian-wedding-rsvp': rsvp,
}
NOTES = {'gender-reveal-cannon': (940, 210, (74, 168, 255), 220, 70),
         'stepford-microwave': (620, 370, LIME, 120, 55),
         'irish-wake-crew': (620, 350, (242, 201, 76), 170, 45),
         'italian-wedding-rsvp': (640, 630, PINK, 200, 55)}


def grain(img):
    noise = Image.effect_noise((W, H), 26).convert('L')
    img = img.convert('RGBA')
    img.putalpha(255)
    dark = Image.merge('RGBA', (Image.new('L', (W, H), 0), Image.new('L', (W, H), 0), Image.new('L', (W, H), 0), noise.point(lambda p: int(p * 0.30))))
    img = Image.alpha_composite(img, dark)
    return img.convert('RGB')


def render(slug):
    img = base(corner=random.Random(slug).randrange(4))
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    FN[slug](ImageDraw.Draw(layer), 1)
    img = Image.alpha_composite(img.convert('RGBA'), layer)
    if slug in NOTES:
        glow(img, (NOTES[slug][0], NOTES[slug][1]), NOTES[slug][2], NOTES[slug][3], NOTES[slug][4])
    img = grain(img.convert('RGB'))
    img.save(os.path.join(OUT, slug + '.webp'), 'WEBP', quality=82)
    zoom = 1.6
    cw, ch = int(W / zoom), int(H / zoom)
    box = ((W - cw) // 2, (H - ch) // 2, (W + cw) // 2, (H + ch) // 2)
    alt = img.crop(box).resize((W, H)).filter(ImageFilter.GaussianBlur(0.6))
    alt = grain(alt)
    alt.save(os.path.join(OUT, slug + '-alt.webp'), 'WEBP', quality=82)
    print(slug, 'webp done')


def photos():
    from google import genai
    from google.genai import types
    import time
    STYLE = 'cinematic editorial photograph, near-black charcoal background, acid lime and hot pink rim lighting, haze, film grain, shallow depth of field, no text, no logos, no people'
    client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
    for slug, prompts in ITEMS.items():
        for name, subject in ((slug + '.jpg', prompts[0]), (slug + '-alt.jpg', prompts[1])):
            try:
                r = client.models.generate_content(
                    model='gemini-3.1-flash-image-preview',
                    contents=f'{STYLE}. {subject}.',
                    config=types.GenerateContentConfig(
                        response_modalities=['IMAGE'],
                        image_config=types.ImageConfig(aspect_ratio='16:9')
                    )
                )
                for p in r.candidates[0].content.parts:
                    if getattr(p, 'inline_data', None):
                        img = Image.open(io.BytesIO(p.inline_data.data)).convert('RGB')
                        img.save(os.path.join(OUT, name.replace('.jpg', '.webp')), 'WEBP', quality=82)
                        print(name, 'saved as webp')
                        break
            except Exception as e:
                print(name, 'ERROR', str(e)[:200])
            time.sleep(1.2)


if __name__ == '__main__':
    if os.environ.get('GEMINI_API_KEY'):
        photos()
    else:
        for slug in ITEMS:
            render(slug)
