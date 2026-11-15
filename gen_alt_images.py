import os
import time
from google import genai
from google.genai import types

OUT = os.path.join(os.path.dirname(__file__), 'public', 'images')
STYLE = "cinematic editorial photograph, near-black charcoal background, acid lime and hot pink rim lighting, haze, film grain, shallow depth of field, no text, no logos, no people"

ITEMS = [
    ('gay-conversion-hvac-alt.jpg', 'a close-up of a retro air conditioner with rainbow colored vent slats mounted on a dark wall, lime and pink light'),
    ('mexican-speed-bumps-alt.jpg', 'a close-up of a dark concrete speed bump on wet asphalt at night with hot pink reflectors'),
    ('border-removal-alt.jpg', 'a low angle view of a crane lifting a concrete border wall section at night, lime floodlights'),
    ('jewish-space-laser-alt.jpg', 'a close-up of a satellite with a small six pointed star emblem firing a lime laser beam into the dark sky'),
    ('ethnic-cleansing-lite-alt.jpg', 'a close-up of a cleaning cart with spray bottles and a folded map in a dark hallway, pink neon strip'),
    ('muslim-airport-screening-alt.jpg', 'a low angle view of an airport metal detector arch glowing lime in a dark empty terminal'),
    ('chinese-virus-disinfection-alt.jpg', 'a close-up of a hazmat fogger spraying acid lime mist into a dark room'),
    ('transgender-detection-alt.jpg', 'a close-up of a black handheld scanner with a blinking hot pink light pointed at a doorway'),
    ('gypsy-removal-alt.jpg', 'a low angle view of a caravan trailer being towed at night, lime headlights and pink taillights'),
    ('reparations-collection-alt.jpg', 'a close-up of a brass collection plate overflowing with coins on a dark table'),
    ('auschwitz-air-freshener-subscription-alt.jpg', 'a close-up of a green pine tree air freshener with gray ash dust in the air, dark interior'),
    ('holocaust-bbq-alt.jpg', 'a close-up of a glass bottle of dark barbecue sauce with drifting ash particles, pink rim light'),
    ('white-flight-alt.jpg', 'a low angle view of a small white airplane over dark suburban houses at dusk, lime sky'),
    ('confederate-air-freshener-alt.jpg', 'a close-up of a rectangular air freshener with a rebel battle flag pattern hanging from a car mirror'),
    ('klan-ornament-alt.jpg', 'a close-up of a small white conical Christmas ornament on a dark pine tree, pink glow'),
    ('shoah-snow-globe-alt.jpg', 'a close-up of a glass snow globe filled with swirling gray ash on a dark shelf'),
    ('trail-of-tears-trail-mix-alt.jpg', 'a close-up of a clear bag of trail mix with peanuts and raisins on a dark surface'),
    ('apartheid-board-game-alt.jpg', 'an overhead view of a board game with separate pieces on a dark table, blank label'),
    ('gaydar-jammer-alt.jpg', 'a close-up of a small black handheld device with a rainbow LED on a dark table'),
    ('yellow-fever-vaccine-alt.jpg', 'a close-up of a vintage vaccine vial with glowing yellow liquid and a syringe on a dark lab table'),
    ('border-wall-lego-alt.jpg', 'a close-up of a toy brick wall model with tiny figures on a dark table'),
    ('auschwitz-air-freshener-alt.jpg', 'a close-up of a green pine tree air freshener hanging from a rearview mirror, ash dust, dark car'),
    ('skibidi-holocaust-alt.jpg', 'a close-up of an absurd figurine with a toilet shaped head on a dark shelf, pink and lime glow'),
    ('nigger-repellent-alt.jpg', 'a close-up of a matte black spray bottle with an acid lime cap releasing a fine mist'),
    ('reparations-coin-jar-alt.jpg', 'a close-up of a glass jar filled with coins and a blank paper label on a dark table'),
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
