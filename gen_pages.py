import os
from pages_services import PAGES as SERVICES
from pages_products import PAGES as PRODUCTS

ALL = SERVICES + PRODUCTS
OUT = os.path.join(os.path.dirname(__file__), 'public')

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_plain} | BRAINROT MART</title>
<meta name="description" content="{lede}">
<link rel="stylesheet" href="/styles.css">
</head>
<body>

<header class="site-header">
  <a class="logo" href="/"><span class="mark">BM</span> BRAINROT MART</a>
  <nav class="nav">
    <a href="/">HOME</a>
    <a href="/services.html"{services_active}>SERVICES</a>
    <a href="/products.html"{products_active}>PRODUCTS</a>
    <a href="/jokes.html">JOKES</a>
  </nav>
  <button class="cart" type="button">CART [0]</button>
</header>

<main class="page-wrap">
  <section class="split" style="padding-top:52px;">
    <div>
      <div class="kicker" style="font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:0.2em;color:var(--lime);margin-bottom:14px;">{kicker}</div>
      <h1 class="page-title">{title_html}</h1>
      <p class="lede">{lede}</p>
      <div class="tag-row">{tags}</div>
      <div class="hero-actions" style="margin-top:24px;">
        <span class="price" style="font-size:22px;color:var(--cream);">{price}</span>
        <button class="btn pink" data-add>{cta}</button>
      </div>
    </div>
    <div class="hero-art" style="min-height:400px;">
      <span class="sticker rot-a">{sticker_a}</span>
      <span class="sticker rot-b">{sticker_b}</span>
      <div class="poster"><img src="/images/{image}" alt="{alt}"></div>
    </div>
  </section>

  <section>
    <div class="section-head">
      <h2>{pitch_title}</h2>
      <p>{pitch_sub}</p>
    </div>
    <div class="split">
      <div class="panel">
        <ul style="margin:0;padding-left:18px;font-size:14px;line-height:1.8;color:#c9c2b5;">
          {points}
        </ul>
      </div>
      <div class="panel">
        <table class="spec-table">
          {specs}
        </table>
      </div>
    </div>
  </section>

  <section>
    <div class="section-head">
      <h2>FIELD NOTES</h2>
      <p>{notes_sub}</p>
    </div>
    <div class="photo-band">
      <figure>
        <img src="/images/{alt_image}" alt="{alt_caption}">
        <figcaption>{alt_caption}</figcaption>
      </figure>
      <figure>
        <img src="/images/{band_image}" alt="{band_caption}">
        <figcaption>{band_caption}</figcaption>
      </figure>
    </div>
  </section>

  <section>
    <div class="section-head">
      <h2>{how_title}</h2>
      <p>{how_sub}</p>
    </div>
    <div class="panel">
      <div class="steps">
        {steps}
      </div>
    </div>
  </section>

  <section>
    <div class="section-head">
      <h2>TESTIMONIALS</h2>
      <p>Verified by nobody, repeated by everyone</p>
    </div>
    <div class="quote-grid">
      {quotes}
    </div>
  </section>

  <section>
    <div class="section-head">
      <h2>FREQUENTLY ASKED</h2>
      <p>Answers we are legally allowed to give</p>
    </div>
    <div class="faq">
      {faqs}
    </div>
  </section>
</main>

<div class="wave"></div>

<footer class="footer">
  <div>
    <div class="credit">BRAINROT MART</div>
    <p class="fine">A fake {kind}. Images generated with Google Imagen. No refunds. No thoughts. Results may vary by zip code, surname density, and mood.</p>
  </div>
  <div class="credit">MADE IN OHIO</div>
</footer>

<script src="/app.js"></script>
</body>
</html>
'''

for item in ALL:
    tags = ''.join(f'<span class="tag">{t}</span>' for t in item['tags'])
    points = ''.join(f'<li>{p}</li>' for p in item['points'])
    specs = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in item['specs'])
    steps = ''.join(f'<div class="step"><span class="num">0{i+1}</span><p>{p}</p></div>' for i, p in enumerate(item['steps']))
    quotes = ''.join(f'<div class="quote"><p>"{q}"</p><span class="who">{w}</span></div>' for q, w in item['quotes'])
    faqs = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in item['faqs'])
    is_service = item['cat'] == 'services'
    html = TEMPLATE.format(
      title_plain=item['title_plain'],
      lede=item['lede'],
      services_active=' class="active"' if is_service else '',
      products_active=' class="active"' if not is_service else '',
      kicker=item['kicker'],
      title_html=item['title_html'],
      tags=tags,
      price=item['price'],
      cta=item['cta'],
      sticker_a=item['sticker_a'],
      sticker_b=item['sticker_b'],
      image=item['image'],
      alt=item['alt'],
      pitch_title='THE PITCH' if is_service else 'WHAT YOU ARE BUYING',
      pitch_sub='What the service promises, roughly' if is_service else 'The product, described honestly for once',
      points=points,
      specs=specs,
      notes_sub='From the service bay' if is_service else 'From the warehouse',
      alt_image=item['alt_image'],
      alt_caption=item['alt_caption'],
      band_image=item['band_image'],
      band_caption=item['band_caption'],
      how_title='HOW IT WORKS' if is_service else 'HOW TO USE IT',
      how_sub='Four steps, zero witnesses' if is_service else 'Four steps, zero common sense',
      steps=steps,
      quotes=quotes,
      faqs=faqs,
      kind='service page' if is_service else 'product page'
    )
    path = os.path.join(OUT, item['slug'] + '.html')
    with open(path, 'w') as f:
        f.write(html)
    print('wrote', item['slug'] + '.html')
