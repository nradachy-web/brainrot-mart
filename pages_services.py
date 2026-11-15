import os

PAGES = [
  {
    'slug': 'gay-conversion-hvac',
    'cat': 'services',
    'title_html': 'GAY CONVERSION<br><span class="thin">HVAC</span>',
    'title_plain': 'Gay Conversion HVAC',
    'kicker': 'CLIMATE CONTROL WITH A MORAL AGENDA',
    'lede': 'A retro HVAC system that cools your home and straightens your son. Installation takes one afternoon. Results may take a lifetime.',
    'tags': ['INSTALLED IN 1 DAY', 'RAINBOW VENTS', 'NO REFUNDS'],
    'price': '$89.00',
    'cta': 'ADD TO CART',
    'image': 'gay-conversion-hvac.webp',
    'alt': 'Retro air conditioner with rainbow vents',
    'sticker_a': 'MORAL CLIMATE',
    'sticker_b': 'ONE DAY INSTALL',
    'points': [
      'Cools any room to a socially acceptable temperature.',
      'Rainbow vent slats are included and then covered with duct tape.',
      'The compressor runs on disapproval, which is renewable.',
      'One free thermostat calibration to your personal beliefs.',
      'Warranty void if the house becomes too welcoming.'
    ],
    'specs': [('Install', 'One afternoon'), ('Vents', 'Rainbow, coverable'), ('Power', 'Disapproval'), ('Warranty', 'Void if welcoming')],
    'alt_image': 'gay-conversion-hvac-alt.webp',
    'alt_caption': 'THE UNIT IN ITS NATURAL HABITAT',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE SERVICE BAY',
    'steps': [
      'We install the unit while you pretend not to watch.',
      'The unit emits a low hum that sounds like a sermon.',
      'Your son adjusts. Your daughter does not. That is not covered.',
      'We leave. You pay. The unit remains.'
    ],
    'quotes': [
      ('My son came back straight. The house is also colder.', 'Homeowner, 49, Ohio'),
      ('I heard the hum and felt judged. Five stars.', 'Customer, 37, Michigan')
    ],
    'faqs': [
      ('Does it work on adults?', 'Results are slower and more expensive.'),
      ('Is it energy efficient?', 'It runs on spite, which is renewable.'),
      ('Can I keep the rainbow vents?', 'Yes, but they must be painted beige.')
    ]
  },
  {
    'slug': 'mexican-speed-bumps',
    'cat': 'services',
    'title_html': 'MEXICAN<br><span class="thin">SPEED BUMPS</span>',
    'title_plain': 'Mexican Speed Bumps',
    'kicker': 'BULK PEDESTRIAN CONVERSION',
    'lede': 'Turn an entire block of pedestrians into traffic calming devices. Installation crew arrives on foot. No permits. No questions.',
    'tags': ['BUY ONE GET TWELVE', 'INSTALLED AT NIGHT', 'NO PERMITS'],
    'price': '$12.00',
    'cta': 'ADD TO CART',
    'image': 'mexican-speed-bumps.webp',
    'alt': 'Dark speed bumps with pink reflectors',
    'sticker_a': 'BUY ONE GET 12',
    'sticker_b': 'INSTALLED AT NIGHT',
    'points': [
      'Each bump is hand-shaped by a licensed traffic engineer.',
      'Bulk discount: buy one, receive twelve. The extra eleven are optional.',
      'Works best on streets with no crosswalks.',
      'The crew arrives on foot, which is the only ironic part.',
      'No permits required, because the bumps are technically pedestrians.'
    ],
    'specs': [('Unit price', '$12'), ('Bulk deal', '1 plus 11'), ('Install', 'Night only'), ('Permits', 'None')],
    'alt_image': 'mexican-speed-bumps-alt.webp',
    'alt_caption': 'A SINGLE UNIT, CLOSE UP',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE CREW ARRIVES ON FOOT',
    'steps': [
      'We survey the street and count the pedestrians.',
      'We convert them into bumps one at a time.',
      'We paint pink reflectors on the resulting bumps.',
      'We invoice you. The crew walks home.'
    ],
    'quotes': [
      ('The bumps are working. Nobody crosses the street anymore.', 'Neighborhood Association, Anon'),
      ('The crew arrived on foot, which I found inspiring.', 'Customer, 44, Ohio')
    ],
    'faqs': [
      ('Are they permanent?', 'Until someone complains.'),
      ('Can I choose the pedestrians?', 'Yes, at checkout.'),
      ('Do they slow cars?', 'That is the point.')
    ]
  },
  {
    'slug': 'border-removal',
    'cat': 'services',
    'title_html': 'BORDER<br><span class="thin">REMOVAL</span>',
    'title_plain': 'Border Removal',
    'kicker': 'BORDER RELOCATION',
    'lede': 'We remove the border, then put it back somewhere else. Relocation included. Consent not included.',
    'tags': ['CRANE INCLUDED', 'NIGHT WORK', 'NO CONSENT'],
    'price': '$8,500',
    'cta': 'REQUEST QUOTE',
    'image': 'border-removal.webp',
    'alt': 'Crane lifting a border wall at night',
    'sticker_a': 'CRANE INCLUDED',
    'sticker_b': 'NO CONSENT',
    'points': [
      'A forty foot section is lifted and moved to a better neighborhood.',
      'The crane is unmarked because we forgot to mark it.',
      'The border is reinstalled facing the other way.',
      'One free border adjustment if the new location complains.',
      'The original location is left with a gap and a story.'
    ],
    'specs': [('Section', '40 feet'), ('Crane', 'Included'), ('Time', 'Night'), ('Consent', 'Not included')],
    'alt_image': 'border-removal-alt.webp',
    'alt_caption': 'THE LIFT, BEFORE THE MOVE',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE NIGHT CREW',
    'steps': [
      'We survey the wall.',
      'We lift the wall.',
      'We move the wall.',
      'We put the wall down and invoice you.'
    ],
    'quotes': [
      ('The wall is now in a better neighborhood. My property value agrees.', 'Developer, 52, Arizona'),
      ('I did not consent, but the gap is lovely.', 'Resident, 39, Texas')
    ],
    'faqs': [
      ('Does it stop migration?', 'It stops it in one direction only.'),
      ('Can I keep the gap?', 'Yes, gaps are complimentary.'),
      ('Is the crane insured?', 'The crane is insured by vibes.')
    ]
  },
  {
    'slug': 'jewish-space-laser',
    'cat': 'services',
    'title_html': 'JEWISH SPACE<br><span class="thin">LASER</span>',
    'title_plain': 'Jewish Space Laser Maintenance',
    'kicker': 'ORBITAL WEATHER CONTROL',
    'lede': 'Annual maintenance for the space laser. Includes oil change, weather control, and one apology to the atmosphere.',
    'tags': ['ANNUAL PLAN', 'ORBITAL', 'WEATHER INCLUDED'],
    'price': '$450 / YEAR',
    'cta': 'SUBSCRIBE',
    'image': 'jewish-space-laser.webp',
    'alt': 'Satellite firing a lime laser beam',
    'sticker_a': 'ORBITAL SERVICE',
    'sticker_b': 'WEATHER INCLUDED',
    'points': [
      'The laser is calibrated to your local weather preferences.',
      'Oil change included. The oil is not explained.',
      'One controlled storm per quarter.',
      'The satellite is painted with a small star emblem for identification.',
      'Technicians are not allowed to look directly at the beam.'
    ],
    'specs': [('Orbit', 'Low and judgmental'), ('Service', 'Annual oil change'), ('Weather', 'One storm per quarter'), ('Beam', 'Lime')],
    'alt_image': 'jewish-space-laser-alt.webp',
    'alt_caption': 'THE BEAM, CLOSE UP',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE GROUND STATION',
    'steps': [
      'We inspect the satellite.',
      'We change the oil.',
      'We test the beam on a cloudy day.',
      'We apologize to the sky.'
    ],
    'quotes': [
      ('The weather is finally under control. My lawn agrees.', 'Subscriber, 58, Florida'),
      ('They apologized to the atmosphere. I found that polite.', 'Customer, 33, Ohio')
    ],
    'faqs': [
      ('Is it real?', 'The laser is real. The weather is negotiable.'),
      ('Can I aim it?', 'Aiming is an upgrade.'),
      ('Does it affect airplanes?', 'Only the ones that deserve it.')
    ]
  },
  {
    'slug': 'ethnic-cleansing-lite',
    'cat': 'services',
    'title_html': 'ETHNIC CLEANSING<br><span class="thin">LITE</span>',
    'title_plain': 'Ethnic Cleansing Lite',
    'kicker': 'HALF THE CRUELTY, ALL THE RESULTS',
    'lede': 'Half the cruelty, all the results. For neighborhoods on a budget and families in a hurry.',
    'tags': ['BUDGET TIER', 'SAME RESULTS', 'LESS CRUELTY'],
    'price': '$299',
    'cta': 'ADD TO CART',
    'image': 'ethnic-cleansing-lite.webp',
    'alt': 'Cleaning cart with spray bottles and map',
    'sticker_a': 'BUDGET TIER',
    'sticker_b': 'SAME RESULTS',
    'points': [
      'Uses the same outcome with fifty percent less discomfort.',
      'The budget tier removes one group at a time.',
      'Results are delivered in a plain envelope.',
      'No historical documentation included.',
      'One free follow-up if the neighborhood notices.'
    ],
    'specs': [('Cruelty', '50 percent less'), ('Groups', 'One at a time'), ('Delivery', 'Plain envelope'), ('Follow up', 'One free')],
    'alt_image': 'ethnic-cleansing-lite-alt.webp',
    'alt_caption': 'THE CART, LOADED',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE SERVICE AISLE',
    'steps': [
      'Pick a group.',
      'We remove them.',
      'We call it relocation.',
      'You pay.'
    ],
    'quotes': [
      ('It was cheaper than the full version and just as effective.', 'Customer, 47, Ohio'),
      ('The plain envelope was a nice touch.', 'Customer, 35, Michigan')
    ],
    'faqs': [
      ('Is it fast?', 'Yes.'),
      ('Is it ethical?', 'That is a separate product.'),
      ('Can I upgrade later?', 'Yes, but the cruelty is non refundable.')
    ]
  },
  {
    'slug': 'muslim-airport-screening',
    'cat': 'services',
    'title_html': 'MUSLIM AIRPORT<br><span class="thin">SCREENING</span>',
    'title_plain': 'Muslim Airport Screening',
    'kicker': 'TERMINAL LEVEL SECURITY',
    'lede': 'We screen your airport for Muslims. Results may include a full terminal and a new security policy.',
    'tags': ['TERMINAL WIDE', 'METAL DETECTORS', 'NEW POLICY'],
    'price': '$2,000',
    'cta': 'REQUEST QUOTE',
    'image': 'muslim-airport-screening.webp',
    'alt': 'Airport metal detector arch glowing lime',
    'sticker_a': 'TERMINAL WIDE',
    'sticker_b': 'NEW POLICY',
    'points': [
      'Every archway is calibrated to your personal threat level.',
      'Screening is performed by a machine that has never met a Muslim.',
      'Results are shared with the airline, the terminal, and the internet.',
      'One free policy revision if the terminal complains.',
      'The scanner glows lime, which is reassuring.'
    ],
    'specs': [('Coverage', 'Whole terminal'), ('Arches', 'Lime calibrated'), ('Policy', 'One free revision'), ('Results', 'Shared widely')],
    'alt_image': 'muslim-airport-screening-alt.webp',
    'alt_caption': 'THE ARCH, LOW ANGLE',
    'band_image': 'horror-band-2.webp',
    'band_caption': 'THE CHECKPOINT',
    'steps': [
      'Install arches.',
      'Screen everyone.',
      'Remove the ones who look like the brochure.',
      'Write a policy.'
    ],
    'quotes': [
      ('The terminal is safer now. Nobody looks like the brochure.', 'Airport Official, Anon'),
      ('The lime glow is calming. Five stars.', 'Traveler, 29, Texas')
    ],
    'faqs': [
      ('Does it catch everyone?', 'It catches everyone it is calibrated to catch.'),
      ('Can I screen only one terminal?', 'That is the standard package.'),
      ('Is the policy permanent?', 'Until the next policy.')
    ]
  },
  {
    'slug': 'chinese-virus-disinfection',
    'cat': 'services',
    'title_html': 'CHINESE VIRUS<br><span class="thin">DISINFECTION</span>',
    'title_plain': 'Chinese Virus Disinfection',
    'kicker': 'SPRAY EVERYTHING. BLAME EVERYONE.',
    'lede': 'A full room fogging service. Spray everything. Blame everyone. Evidence of origin not included.',
    'tags': ['ROOM FOGGING', 'LIME MIST', 'NO ORIGIN'],
    'price': '$150 / ROOM',
    'cta': 'ADD TO CART',
    'image': 'chinese-virus-disinfection.webp',
    'alt': 'Hazmat fogger spraying lime mist',
    'sticker_a': 'LIME MIST',
    'sticker_b': 'BLAME INCLUDED',
    'points': [
      'We fog the room with acid lime mist until it looks clean.',
      'The mist smells like blame and citrus.',
      'One free blame assignment per room.',
      'Disinfection is guaranteed for twenty four hours or until someone sneezes.',
      'Origin of the virus is available as a separate consulting product.'
    ],
    'specs': [('Room', 'One'), ('Mist', 'Acid lime'), ('Blame', 'Free assignment'), ('Guarantee', '24 hours')],
    'alt_image': 'chinese-virus-disinfection-alt.webp',
    'alt_caption': 'THE FOGGER, CLOSE UP',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE SEALED ROOM',
    'steps': [
      'Seal the room.',
      'Fog the room.',
      'Blame a country.',
      'Unseal and invoice.'
    ],
    'quotes': [
      ('The room smelled like blame and citrus. I felt clean.', 'Customer, 48, Ohio'),
      ('They blamed the right country. Five stars.', 'Customer, 36, Florida')
    ],
    'faqs': [
      ('Is it safe?', 'The mist is safe. The blame is not.'),
      ('Can I fog a whole house?', 'Yes, at a bulk rate.'),
      ('Does it kill the virus?', 'It kills the conversation.')
    ]
  },
  {
    'slug': 'transgender-detection',
    'cat': 'services',
    'title_html': 'TRANSGENDER<br><span class="thin">DETECTION</span>',
    'title_plain': 'Transgender Detection Service',
    'kicker': 'FIND THEM BEFORE YOU DO',
    'lede': 'A handheld scanner that detects transgender people before you notice them. Discretion guaranteed. The scanner is calibrated to your personal beliefs.',
    'tags': ['HANDHELD', 'DISCREET', 'PERSONAL CALIBRATION'],
    'price': '$75 / SCAN',
    'cta': 'ADD TO CART',
    'image': 'transgender-detection.webp',
    'alt': 'Handheld scanner with pink light',
    'sticker_a': 'DISCREET',
    'sticker_b': 'PERSONAL CALIBRATION',
    'points': [
      'The scanner emits a hot pink light when it finds someone.',
      'It has never been wrong, according to its manufacturer.',
      'Calibration takes five minutes and one uncomfortable conversation.',
      'The scanner can be used at parties, weddings, and school events.',
      'Results are delivered as a vibration, not a sound.'
    ],
    'specs': [('Form', 'Handheld'), ('Signal', 'Pink light'), ('Calibration', 'Five minutes'), ('Accuracy', 'User defined')],
    'alt_image': 'transgender-detection-alt.webp',
    'alt_caption': 'THE SCANNER, CLOSE UP',
    'band_image': 'horror-band-2.webp',
    'band_caption': 'THE SCAN IN PROGRESS',
    'steps': [
      'Calibrate to your beliefs.',
      'Point at a crowd.',
      'Follow the pink light.',
      'Do not ask questions.'
    ],
    'quotes': [
      ('It found three people I had not noticed. I was impressed.', 'Customer, 45, Ohio'),
      ('The vibration was discreet. The pink light was not.', 'Customer, 31, Michigan')
    ],
    'faqs': [
      ('Is it accurate?', 'Accuracy is defined by the user.'),
      ('Can I scan myself?', 'Yes, but results may be surprising.'),
      ('Does it work at a distance?', 'It works at the distance of your beliefs.')
    ]
  },
  {
    'slug': 'gypsy-removal',
    'cat': 'services',
    'title_html': 'GYPSY<br><span class="thin">REMOVAL</span>',
    'title_plain': 'Gypsy Removal',
    'kicker': 'NIGHTTIME RELOCATION',
    'lede': 'We relocate the Roma. Spelling varies by contract. Trailers towed at night for maximum surprise.',
    'tags': ['NIGHT TOWING', 'SPELLING VARIES', 'NO REFUNDS'],
    'price': '$1,500',
    'cta': 'ADD TO CART',
    'image': 'gypsy-removal.webp',
    'alt': 'Caravan trailer towed at night',
    'sticker_a': 'NIGHT TOWING',
    'sticker_b': 'SPELLING VARIES',
    'points': [
      'Trailers are towed at two AM so the neighborhood can claim it was asleep.',
      'The removal is called relocation in the invoice.',
      'One free spelling correction per contract.',
      'The caravan is returned to a different postcode.',
      'No witnesses. No paperwork. No apology.'
    ],
    'specs': [('Time', '2 AM'), ('Method', 'Tow'), ('Invoice', 'Relocation'), ('Postcode', 'Different')],
    'alt_image': 'gypsy-removal-alt.webp',
    'alt_caption': 'THE TOW, LOW ANGLE',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE NIGHT CREW',
    'steps': [
      'Locate the caravan.',
      'Hook it up.',
      'Tow it.',
      'Send a postcard.'
    ],
    'quotes': [
      ('The trailer was gone by morning. The postcard arrived by noon.', 'Resident, 56, Ohio'),
      ('The spelling on the invoice was corrected. Very professional.', 'Customer, 42, Michigan')
    ],
    'faqs': [
      ('Is it legal?', 'The invoice says relocation.'),
      ('Can I keep the trailer?', 'Only if it is empty.'),
      ('Do you tow at night?', 'Yes, for maximum surprise.')
    ]
  },
  {
    'slug': 'reparations-collection',
    'cat': 'services',
    'title_html': 'REPARATIONS<br><span class="thin">COLLECTION</span>',
    'title_plain': 'Reparations Collection Agency',
    'kicker': 'HISTORY AS INVOICE',
    'lede': 'We collect reparations from people who never paid them. Fifteen percent commission. History is the invoice.',
    'tags': ['15% COMMISSION', 'NO STATUTE', 'HISTORY INCLUDED'],
    'price': '15% COMMISSION',
    'cta': 'BOOK COLLECTION',
    'image': 'reparations-collection.webp',
    'alt': 'Brass collection plate with coins',
    'sticker_a': 'HISTORY AS INVOICE',
    'sticker_b': '15% COMMISSION',
    'points': [
      'We calculate what you owe using a proprietary formula.',
      'The formula is based on vibes and a calendar.',
      'Collection is polite at first and less polite later.',
      'Fifteen percent is our fee. The rest is the past.',
      'One free receipt for your records.'
    ],
    'specs': [('Fee', '15 percent'), ('Formula', 'Proprietary'), ('Tone', 'Polite then less'), ('Receipt', 'One free')],
    'alt_image': 'reparations-collection-alt.webp',
    'alt_caption': 'THE PLATE, CLOSE UP',
    'band_image': 'horror-band-2.webp',
    'band_caption': 'THE COLLECTION DESK',
    'steps': [
      'We calculate.',
      'We ask politely.',
      'We ask less politely.',
      'We collect.'
    ],
    'quotes': [
      ('They collected more than I expected. History is expensive.', 'Debtor, 50, Ohio'),
      ('The receipt was free. The debt was not.', 'Customer, 38, Florida')
    ],
    'faqs': [
      ('Who owes?', 'Everyone.'),
      ('How much?', 'More than you think.'),
      ('Is there a statute of limitations?', 'The past does not have one.')
    ]
  },
  {
    'slug': 'auschwitz-air-freshener-subscription',
    'cat': 'services',
    'title_html': 'AUSCHWITZ AIR<br><span class="thin">FRESHENER SUBSCRIPTION</span>',
    'title_plain': 'Auschwitz Air Freshener Subscription',
    'kicker': 'MONTHLY SCENT PROGRAM',
    'lede': 'Pine scent. Ash notes. Monthly delivery to your car, your home, and your conscience.',
    'tags': ['MONTHLY', 'PINE AND ASH', 'NO REFUNDS'],
    'price': '$5.99 / MO',
    'cta': 'SUBSCRIBE',
    'image': 'auschwitz-air-freshener.webp',
    'alt': 'Pine air freshener with ash dust',
    'sticker_a': 'MONTHLY',
    'sticker_b': 'PINE AND ASH',
    'points': [
      'Each freshener is shaped like a pine tree and smells like history.',
      'Ash notes are added by hand.',
      'Delivery is monthly, discreet, and impossible to cancel.',
      'The scent lasts thirty days or until someone notices.',
      'One free replacement if the ash clumps.'
    ],
    'specs': [('Delivery', 'Monthly'), ('Scent', 'Pine and ash'), ('Cancel', 'After the year'), ('Replacement', 'One free')],
    'alt_image': 'auschwitz-air-freshener-subscription-alt.webp',
    'alt_caption': 'THE MONTHLY DELIVERY',
    'band_image': 'horror-band-2.webp',
    'band_caption': 'THE SUBSCRIPTION DESK',
    'steps': [
      'Subscribe.',
      'Hang the tree.',
      'Smell the past.',
      'Pay monthly.'
    ],
    'quotes': [
      ('It smells like a lesson. I keep it in the car.', 'Subscriber, 44, Ohio'),
      ('The ash clumped. They replaced it for free.', 'Subscriber, 37, Michigan')
    ],
    'faqs': [
      ('Does it smell good?', 'It smells like a lesson.'),
      ('Can I cancel?', 'Cancellation is available after the year.'),
      ('Is the ash real?', 'The ash is added by hand, which is close enough.')
    ]
  },
  {
    'slug': 'mansplaining-removal',
    'cat': 'services',
    'title_html': 'MANSPAINING<br><span class="thin">REMOVAL</span>',
    'title_plain': 'Mansplaining Removal',
    'kicker': 'EXTRACTED ON SITE, THEN EXPLAINED',
    'lede': 'A certified technician removes the mansplaining from your meeting, your garage, or your marriage. Then they explain, at length, how the removal was performed.',
    'tags': ['SAME DAY', 'EXPLAINED TO YOU', 'DIAGRAM INCLUDED'],
    'price': '$75 / HR',
    'cta': 'BOOK THE CREW',
    'image': 'mansplaining-removal.webp',
    'alt': 'Speech bubble being scraped clean',
    'sticker_a': 'SAME DAY',
    'sticker_b': 'THEN EXPLAINED',
    'points': [
      'The removal takes one hour. The explanation of the removal takes two.',
      'The technician confirms they understood you correctly while not listening.',
      'Includes one diagram, drawn without being asked for one.',
      'The subject may reattach within the week. Repeat visits are discounted.',
      'We do not remove the confidence. That one is structural.'
    ],
    'specs': [('Duration', 'One hour plus explanation'), ('Diagram', 'Included'), ('Reattachment', 'Likely'), ('Confidence', 'Not covered')],
    'alt_image': 'mansplaining-removal-alt.webp',
    'alt_caption': 'THE DIAGRAM, UNSOLICITED',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE SERVICE BAY',
    'steps': [
      'You call. A man arrives.',
      'He removes the mansplaining while performing a mansplaining.',
      'He hands you an invoice, and a diagram of the invoice.',
      'You pay for the explanation of the removal.'
    ],
    'quotes': [
      ('They removed it, then explained the removal twice, then fixed my sink.', 'Customer, 42, Michigan'),
      ('My husband hired them. He enjoyed the explanation of the technician more than the repair.', 'Customer, 39, Ohio')
    ],
    'faqs': [
      ('Can the technician be a woman?', 'Then the service is called being interrupted properly.'),
      ('Does it work on podcasts?', 'Podcasts are the source, not the symptom.'),
      ('Is my marriage covered?', 'Marriages are covered. Poorly, but covered.')
    ]
  },
  {
    'slug': 'irish-wake-crew',
    'cat': 'services',
    'title_html': 'IRISH<br><span class="thin">WAKE CREW</span>',
    'title_plain': 'Irish Wake Attendance Crew',
    'kicker': 'PROFESSIONAL GRIEF, LOUD AND LOCAL',
    'lede': 'We attend your funeral, we cry like we knew him, and we stay for the second, third, and fourth round. Keening is billed by the minute.',
    'tags': ['CRY GUARANTEED', 'KEENING ADD-ON', 'STAYS FOR ROUND FOUR'],
    'price': '$300 / FUNERAL',
    'cta': 'BOOK THE CREW',
    'image': 'irish-wake-crew.webp',
    'alt': 'Candles and a dark pub table',
    'sticker_a': 'CRY GUARANTEED',
    'sticker_b': 'LOUD AND LOCAL',
    'points': [
      'Every mourner is trained in three grades of sob, from sniffle to howl.',
      'They will call the deceased the best man of a wedding nobody else remembers.',
      'They drink in memory, at volume, at whatever speed the venue allows.',
      'The keening add-on: one woman, one lung capacity, no ceiling.',
      'They never met your uncle. They will tell you that they did.'
    ],
    'specs': [('Cry grades', 'One to three'), ('Keening', 'Add-on'), ('Rounds', 'Four and up'), ('Relation to deceased', 'None claimed')],
    'alt_image': 'irish-wake-crew-alt.webp',
    'alt_caption': 'THE FRONT ROW, CLAIMED',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE SERVICE BAY',
    'steps': [
      'You book the crew.',
      'They arrive before the family and claim the front row.',
      'They out-cry the family with technical skill.',
      'They tip the bar. They do not tip you.'
    ],
    'quotes': [
      ('The crew outcried my mother. My uncle cried from pure respect.', 'Client, 46, Boston'),
      ('They told me they knew him, and I believed them. They were more tired than I was.', 'Client, 52, Chicago')
    ],
    'faqs': [
      ('Do they know the deceased?', 'They know the bar. The deceased is a colleague by then.'),
      ('Is the stout included?', 'The stout is on the house for a short, violent window.'),
      ('What if the wake gets rowdy?', 'The rowdiness is not a defect. It is billed extra.')
    ]
  },
  {
    'slug': 'scottish-invoice-audit',
    'cat': 'services',
    'title_html': 'SCOTTISH<br><span class="thin">INVOICE AUDIT</span>',
    'title_plain': 'Scottish Invoice Audit',
    'kicker': 'RECOVERING MONEY YOU DID NOT KNOW YOU SPENT',
    'lede': 'We audit your bills with forensic thrift and recover what is owed to you. Our fee is ninety percent, because we found it.',
    'tags': ['NO WIN NO FEE', '90 PERCENT FEE', 'TONGS INCLUDED'],
    'price': '$150 + 90%',
    'cta': 'BOOK THE AUDIT',
    'image': 'scottish-invoice-audit.webp',
    'alt': 'Receipt held by metal tongs over a jar of coins',
    'sticker_a': 'NO WIN NO FEE',
    'sticker_b': '90 PERCENT',
    'points': [
      'The audit is run on a calculator that has survived three recessions.',
      'Recovered funds are held in a jar until the mood is right.',
      'The fee is ninety percent. The other ten is a gift, which is a strong word.',
      'The tongs used to handle the money are not included and are not returned.',
      'No win, no fee. Losing is mathematically difficult for us.'
    ],
    'specs': [('Fee', '90 percent'), ('Method', 'Tongs'), ('Recovery', 'Reluctant'), ('Jar location', 'Sealed')],
    'alt_image': 'scottish-invoice-audit-alt.webp',
    'alt_caption': 'THE JAR, SEALED',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE SERVICE BAY',
    'steps': [
      'You send us every bill you have ever received.',
      'We return a check with a small number on it.',
      'We keep a large number.',
      'You learn to read contracts, too late.'
    ],
    'quotes': [
      ('They recovered eleven dollars and kept nine. Very fair. Very Scottish.', 'Client, 57, Glasgow'),
      ('My phone company apologized. The crew apologized back. Both apologies were about money.', 'Client, 61, Edinburgh')
    ],
    'faqs': [
      ('Why the tongs?', 'Touching money is a commitment. We avoid commitments.'),
      ('Is the jar taxed?', 'The jar is unincorporated. The jar answers to no one.'),
      ('Can the fee be negotiated?', 'You can ask. The ninety will remain.')
    ]
  },
  {
    'slug': 'italian-wedding-rsvp',
    'cat': 'services',
    'title_html': 'ITALIAN WEDDING<br><span class="thin">RSVP AGENCY</span>',
    'title_plain': 'Italian Wedding RSVP Agency',
    'kicker': 'EIGHTY SAY YES, THREE HUNDRED COME',
    'lede': 'We run the list for the wedding that was never small. Yeses multiply, nos evaporate, and two funerals are rescheduled around the reception.',
    'tags': ['YES MULTIPLIES', 'NO VANISHES', 'COUSIN UNINVITED'],
    'price': '$200 / EVENT',
    'cta': 'BOOK THE AGENCY',
    'image': 'italian-wedding-rsvp.webp',
    'alt': 'Envelope with a fork stuck in it on a dark table',
    'sticker_a': 'YES MULTIPLIES',
    'sticker_b': 'NO VANISHES',
    'points': [
      'We confirm eighty guests and seat three hundred, including a cousin nobody invited.',
      'The caterer is told to feed everyone. The catering is told to hope.',
      'The schedule lists four times. None of the times are correct.',
      'Two funerals and one baptism may be moved around the reception.',
      'The list is not a list. The list is a rumor with a font.'
    ],
    'specs': [('Confirmed', '80'), ('Attending', '300'), ('Uninvited cousins', 'At least one'), ('Schedule', 'Rumor based')],
    'alt_image': 'italian-wedding-rsvp-alt.webp',
    'alt_caption': 'THE RUMOR, IN A FONT',
    'band_image': 'horror-band-1.webp',
    'band_caption': 'THE SERVICE BAY',
    'steps': [
      'You send the invitations.',
      'We count the responses twice.',
      'Nobody responds. Everyone attends.',
      'We seat the room by rumor and instinct.'
    ],
    'quotes': [
      ('We invited eighty. The priest recognized four hundred and stayed.', 'Client, 36, New Jersey'),
      ('The agency found my cousin in the third row. My cousin had a plate and a speech.', 'Client, 41, Brooklyn')
    ],
    'faqs': [
      ('Can we cap the number?', 'The number does not cap. The number is a suggestion of the family.'),
      ('Is the food enough?', 'The food is a conversation. The conversation lasts longer.'),
      ('What about the funerals?', 'The funerals are flexible. The dead understand.')
    ]
  }
]
