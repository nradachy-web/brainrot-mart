import os
import time
from google import genai
from google.genai import types

OUT = os.path.join(os.path.dirname(__file__), 'public', 'images')
os.makedirs(OUT, exist_ok=True)

STYLE = "cinematic editorial photograph, near-black charcoal background, acid lime and hot pink rim lighting, haze, film grain, shallow depth of field, no text, no logos, no people"

ITEMS = [
    ('home-hero.jpg', 'a dark industrial warehouse filled with stacked crates and one sleek white ballistic missile under acid lime spotlights, ominous product display'),
    ('jewish-seeking-missiles.jpg', 'a sleek white ballistic missile with hot pink fins and a small six pointed star emblem standing upright on a concrete floor in a dark warehouse, acid lime spotlight'),
    ('nigger-removal.jpg', 'a heavy industrial spray can with a black nozzle and acid lime bands on a dark concrete floor, an unmarked black van blurred in the background'),
    ('gay-conversion-hvac.jpg', 'a retro air conditioner unit with rainbow colored vent slats mounted on a dark wall, acid lime glow from below'),
    ('mexican-speed-bumps.jpg', 'a row of dark concrete speed bumps on wet asphalt at night, hot pink warning reflectors and acid lime street light'),
    ('holocaust-bbq.jpg', 'a glass bottle of thick dark barbecue sauce with drifting gray ash particles around it on a black table, hot pink rim light'),
    ('white-flight.jpg', 'a small white propeller airplane flying low over a dark suburban neighborhood at dusk, acid lime sky and hot pink horizon'),
    ('holocaust-denial-hotline.jpg', 'a vintage black rotary telephone sitting on a pile of gray ash in a dark office, acid lime rim light'),
    ('gay-conversion-camp.jpg', 'a wooden summer camp cabin at dusk with a small rainbow flag on the porch, dark forest, hot pink light'),
    ('border-removal.jpg', 'a section of concrete border wall being lifted by a crane at night, acid lime floodlights and hot pink warning beacons'),
    ('jewish-space-laser.jpg', 'a satellite with a small six pointed star emblem firing a bright lime laser beam down at a dark landscape from orbit'),
    ('ethnic-cleansing-lite.jpg', 'a minimalist cleaning cart with spray bottles and a folded neighborhood map in a dark hallway, hot pink neon strip'),
    ('muslim-airport-screening.jpg', 'an airport security metal detector arch glowing acid lime in a dark empty terminal, hot pink accents'),
    ('chinese-virus-disinfection.jpg', 'a hazmat worker silhouette fogging a dark room with acid lime mist from a sprayer, no face visible'),
    ('transgender-detection.jpg', 'a handheld black scanner with a blinking hot pink light pointed at a dark doorway, acid lime glow'),
    ('gypsy-removal.jpg', 'a small caravan trailer being towed away at night by an unmarked truck, acid lime headlights and hot pink taillights'),
    ('reparations-collection.jpg', 'a brass collection plate overflowing with coins on a dark wooden table, acid lime rim light'),
    ('auschwitz-air-freshener.jpg', 'a green pine tree air freshener hanging from a car rearview mirror with gray ash dust in the air, dark car interior, hot pink light'),
    ('confederate-air-freshener.jpg', 'a rectangular air freshener with a rebel battle flag pattern hanging from a car mirror, dark interior, acid lime light, blank label'),
    ('klan-ornament.jpg', 'a small white pointed hood shaped Christmas ornament hanging on a dark pine tree, hot pink glow, no face'),
    ('shoah-snow-globe.jpg', 'a glass snow globe filled with swirling gray ash on a dark shelf, acid lime rim light'),
    ('trail-of-tears-trail-mix.jpg', 'a clear bag of peanuts and raisins trail mix on a dark surface with a small tear shaped pendant beside it, hot pink light'),
    ('apartheid-board-game.jpg', 'a board game box and separate game pieces on a dark table, blank label, acid lime and hot pink lighting'),
    ('gaydar-jammer.jpg', 'a small black handheld device with a short antenna and a rainbow LED on a dark table, acid lime rim light'),
    ('yellow-fever-vaccine.jpg', 'a vintage glass vaccine vial filled with glowing yellow liquid beside a syringe on a dark laboratory table, hot pink light'),
    ('border-wall-lego.jpg', 'a toy brick wall model with tiny figures on a dark table, acid lime spotlight'),
    ('skibidi-holocaust.jpg', 'an absurd collectible figurine with a toilet shaped head on a dark shelf, hot pink and acid lime glow'),
    ('nigger-repellent.jpg', 'a matte black spray bottle with an acid lime cap releasing a fine mist on a dark porch, hot pink rim light'),
    ('reparations-coin-jar.jpg', 'a glass jar filled with coins and a blank paper label on a dark table, acid lime rim light'),
    ('horror-band-1.jpg', 'a wide dark warehouse aisle lined with ominous crates and one glowing acid lime display case'),
    ('horror-band-2.jpg', 'a dark checkout counter with a hot pink cash register and acid lime price tags, no text, ominous retail scene'),
]

client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

for name, subject in ITEMS:
    prompt = f"{STYLE}. {subject}."
    try:
        r = client.models.generate_content(
            model='gemini-3.1-flash-image-preview',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE'],
                image_config=types.ImageConfig(aspect_ratio='16:9')
            )
        )
        saved = False
        for p in r.candidates[0].content.parts:
            if getattr(p, 'inline_data', None):
                data = p.inline_data.data
                with open(os.path.join(OUT, name), 'wb') as f:
                    f.write(data)
                print(name, len(data))
                saved = True
                break
        if not saved:
            print(name, 'NO IMAGE')
    except Exception as e:
        print(name, 'ERROR', str(e)[:220])
    time.sleep(1.2)
