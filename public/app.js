const audio = new Audio();
const wave = document.querySelector('.wave');

function toast(msg) {
  let el = document.querySelector('.toast');
  if (!el) {
    el = document.createElement('div');
    el.className = 'toast';
    document.body.appendChild(el);
  }
  el.textContent = msg;
  el.classList.add('show');
  clearTimeout(el._t);
  el._t = setTimeout(() => el.classList.remove('show'), 2200);
}

function makeWave() {
  if (!wave) return;
  wave.innerHTML = '';
  for (let i = 0; i < 24; i++) {
    const bar = document.createElement('i');
    bar.style.animationDuration = `${0.28 + Math.random() * 0.5}s`;
    wave.appendChild(bar);
  }
}

makeWave();

async function speak(text, voice, btn) {
  if (btn) {
    btn.classList.add('loading');
    btn.dataset.label = btn.textContent;
    btn.textContent = 'LOADING';
  }
  try {
    const res = await fetch('/api/speak', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, voice })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'speech failed');
    audio.src = data.url;
    audio.currentTime = 0;
    audio.play();
    if (wave) wave.classList.add('on');
    if (btn) btn.textContent = 'PLAYING';
    audio.onplay = () => { if (btn) btn.textContent = 'PLAYING'; };
    audio.onended = () => {
      if (wave) wave.classList.remove('on');
      if (btn) btn.textContent = btn.dataset.label || 'HEAR IT';
    };
    toast(data.cached ? 'PLAYING CACHED AUDIO. ZERO NEW CREDITS.' : `GENERATED ${data.chars} CHARACTERS.`);
  } catch (e) {
    toast('VOICE FAILURE: ' + e.message);
    if (btn) btn.textContent = btn.dataset.label || 'HEAR IT';
  } finally {
    if (btn) btn.classList.remove('loading');
  }
}

document.querySelectorAll('[data-speak]').forEach((btn) => {
  btn.addEventListener('click', () => {
    speak(btn.dataset.speak, btn.dataset.voice || 'TX3LPaxmHKxFdv7VOQHJ', btn);
  });
});

const cartBtn = document.querySelector('.cart');
let count = Number(localStorage.getItem('brm-cart') || 0);
function renderCart() {
  if (cartBtn) cartBtn.textContent = `CART [${count}]`;
}
renderCart();

document.querySelectorAll('[data-add]').forEach((btn) => {
  btn.addEventListener('click', () => {
    count += 1;
    localStorage.setItem('brm-cart', String(count));
    renderCart();
    toast('ADDED TO CART. NO REFUNDS.');
  });
});

if (cartBtn) {
  cartBtn.addEventListener('click', () => {
    toast(count ? `${count} HORRORS IN CART. CHECKOUT IS A MYTH.` : 'CART EMPTY. FIX THAT.');
  });
}

const jokes = [
  { text: 'Why did the black guy get stopped by the police? Because he was walking.', voice: 'pNInz6obpgDQGcFmaJgB' },
  { text: 'What do you call a Mexican with a lawnmower? Employed.', voice: 'TX3LPaxmHKxFdv7VOQHJ' },
  { text: 'How do you stop a Mexican from drowning? Take your foot off his head.', voice: 'SOYHLrjzK2X1ezoPC6cr' },
  { text: 'Why do Jews play hide and seek so badly? They already know where the attic is.', voice: 'IKne3meq5aSn9XLyUdCD' },
  { text: 'Whats the difference between a Jew and a pizza? The pizza does not complain about the oven.', voice: 'pNInz6obpgDQGcFmaJgB' },
  { text: 'Why did the Holocaust happen? Because Germany ran out of gas.', voice: 'SOYHLrjzK2X1ezoPC6cr' },
  { text: 'What do you call a black man in a suit? The defendant.', voice: 'TX3LPaxmHKxFdv7VOQHJ' },
  { text: 'Why did the black guy get fired from the cotton field? He kept taking the cotton home.', voice: 'FGY2WhTYpPnrIDTdsKH5' },
  { text: 'How many Jews fit in a car? Two in front, three in back, four in the ashtray.', voice: 'IKne3meq5aSn9XLyUdCD' },
  { text: 'What is a Mexicans favorite sport? Crossing.', voice: 'N2lVS1w4EtoT3dr4eOWO' },
  { text: 'Why are Asian people so good at math? They count everything twice.', voice: 'cgSgspJ2msm6clMCkdW9' },
  { text: 'What do you call a Mexican with a stethoscope? A wetback doctor.', voice: 'SOYHLrjzK2X1ezoPC6cr' },
  { text: 'Why did the black neighborhood get gentrified? Because the rent was cheap.', voice: 'pNInz6obpgDQGcFmaJgB' },
  { text: 'My IQ is lower than the number of Jews I have met.', voice: 'TX3LPaxmHKxFdv7VOQHJ' },
  { text: 'Jewish seeking missile. The only weapon that apologizes after impact.', voice: 'pNInz6obpgDQGcFmaJgB' },
  { text: 'I told my wife she was drawing her eyebrows too high. She looked surprised.', voice: 'TX3LPaxmHKxFdv7VOQHJ' },
  { text: 'My wife said I never listen. Or something like that.', voice: 'FGY2WhTYpPnrIDTdsKH5' },
  { text: 'What is the difference between my wife and the tax man? The tax man only takes half.', voice: 'pNInz6obpgDQGcFmaJgB' },
  { text: 'Marriage. The only contract where both partners are the plaintiff and the property.', voice: 'N2lVS1w4EtoT3dr4eOWO' },
  { text: 'My girlfriend said I treat her like an appliance. So I turned up the heat and asked why dinner was late.', voice: 'IKne3meq5aSn9XLyUdCD' },
  { text: 'How do I know my marriage is strong? We are yelling at the same time.', voice: 'SOYHLrjzK2X1ezoPC6cr' },
  { text: 'What do a feminist and a clitoris have in common? They both exist, and your grandfather died denying it.', voice: 'N2lVS1w4EtoT3dr4eOWO' },
  { text: 'How many feminists does it take to change a lightbulb? That is not funny.', voice: 'FGY2WhTYpPnrIDTdsKH5' },
  { text: 'I asked God for a bike. I know God does not give bikes, so I stole a bike and asked for forgiveness.', voice: 'SOYHLrjzK2X1ezoPC6cr' },
  { text: 'How many Irish does it take to change a lightbulb? None. They drink in the dark until the pub opens.', voice: 'TX3LPaxmHKxFdv7VOQHJ' },
  { text: 'Why does the Scotsman lock the fridge twice? One lock keeps the food in, the other keeps the money out.', voice: 'N2lVS1w4EtoT3dr4eOWO' },
  { text: 'Why did the Italian show up to his own wedding two hours late? The invitation said around five.', voice: 'cgSgspJ2msm6clMCkdW9' },
  { text: 'Why did the French waiter quit? He refused to work on a day the kitchen was open.', voice: 'pNInz6obpgDQGcFmaJgB' },
  { text: 'A German joke walks into a bar. It arrives exactly on time. Nobody laughs.', voice: 'FGY2WhTYpPnrIDTdsKH5' },
  { text: 'How do you keep a black man on his feet? Tie a string to his wallet and pull it away.', voice: 'TX3LPaxmHKxFdv7VOQHJ' },
  { text: 'Why does the Jewish shop put up a twenty four hour sign? So nobody can catch him sleeping.', voice: 'pNInz6obpgDQGcFmaJgB' },
  { text: 'How many Muslims does it take to change a lightbulb? None. The lightbulb is American and it is already guilty.', voice: 'IKne3meq5aSn9XLyUdCD' },
  { text: 'How many gay guys does it take to change a lightbulb? Three. One to change it, one to say it was better before, and one to adopt the bulb.', voice: 'N2lVS1w4EtoT3dr4eOWO' },
  { text: 'I went out with a trans woman once. Nice person. The bulb used to be hot.', voice: 'SOYHLrjzK2X1ezoPC6cr' },
  { text: 'Why are Asians so good at Connect Four? They let you think you are winning.', voice: 'cgSgspJ2msm6clMCkdW9' },
  { text: 'What do a wife and an alarm clock have in common? Both scream at six and neither explains why.', voice: 'TX3LPaxmHKxFdv7VOQHJ' },
  { text: 'My doctor said I need more iron. My wife said I need more money. The doctor was the optimistic one.', voice: 'pNInz6obpgDQGcFmaJgB' }
];

const output = document.querySelector('.joke-output');
const tellBtn = document.querySelector('[data-joke]');
let lastJoke = null;

function rollJoke() {
  if (!output) return;
  let j = jokes[Math.floor(Math.random() * jokes.length)];
  if (lastJoke && jokes.length > 1) {
    while (j.text === lastJoke.text) j = jokes[Math.floor(Math.random() * jokes.length)];
  }
  lastJoke = j;
  output.textContent = j.text;
  speak(j.text, j.voice, tellBtn);
}

if (tellBtn) {
  tellBtn.textContent = 'TELL ME A HORROR';
  tellBtn.addEventListener('click', rollJoke);
}

const list = document.querySelector('.joke-list');
if (list) {
  jokes.forEach((j) => {
    const row = document.createElement('div');
    row.className = 'joke-item';
    const p = document.createElement('p');
    p.style.margin = '0';
    p.textContent = j.text;
    const b = document.createElement('button');
    b.className = 'audio-btn';
    b.textContent = 'SAY IT';
    b.addEventListener('click', () => speak(j.text, j.voice, b));
    row.appendChild(p);
    row.appendChild(b);
    list.appendChild(row);
  });
}

document.querySelectorAll('form[data-fake-form]').forEach((form) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    form.reset();
    toast('BOOKED. A CREW WILL ARRIVE BETWEEN 2 AND 4 AM.');
  });
});
