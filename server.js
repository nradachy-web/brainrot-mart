const http = require('http');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execFileSync } = require('child_process');

const PORT = process.env.PORT || 4181;
const PUBLIC = path.join(__dirname, 'public');
const AUDIO = path.join(PUBLIC, 'audio');
fs.mkdirSync(AUDIO, { recursive: true });

const MODEL = 'eleven_multilingual_v2';
const VOICES = new Set([
  'TX3LPaxmHKxFdv7VOQHJ',
  'pNInz6obpgDQGcFmaJgB',
  'FGY2WhTYpPnrIDTdsKH5',
  'SOYHLrjzK2X1ezoPC6cr',
  'IKne3meq5aSn9XLyUdCD',
  'N2lVS1w4EtoT3dr4eOWO',
  'cgSgspJ2msm6clMCkdW9',
  'JBFqnCBsd6RMkjVDRZzb',
  'Xb7hH8MSUJpSbSDYk0k2'
]);

let apiKey = null;
function getKey() {
  if (!apiKey) {
    apiKey = process.env.ELEVENLABS_API_KEY;
    if (!apiKey) {
      apiKey = execFileSync('python3', [path.join(__dirname, 'getkey.py')], {
        encoding: 'utf8',
        timeout: 20000
      }).trim();
    }
  }
  return apiKey;
}

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mp3': 'audio/mpeg',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.webp': 'image/webp',
  '.ico': 'image/x-icon',
  '.json': 'application/json'
};

function sendJson(res, code, obj) {
  const body = JSON.stringify(obj);
  res.writeHead(code, { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' });
  res.end(body);
}

async function synth(text, voice) {
  const clean = String(text).slice(0, 500);
  const id = crypto.createHash('sha1').update(`${voice}|${MODEL}|${clean}`).digest('hex');
  const file = path.join(AUDIO, `${id}.mp3`);
  if (fs.existsSync(file)) return { id, cached: true, chars: clean.length };

  const url = `https://api.elevenlabs.io/v1/text-to-speech/${voice}?output_format=mp3_44100_128`;
  const payload = JSON.stringify({
    text: clean,
    model_id: MODEL,
    voice_settings: {
      stability: 0.32,
      similarity_boost: 0.85,
      style: 0.7,
      use_speaker_boost: true
    }
  });
  const r = await fetch(url, {
    method: 'POST',
    headers: { 'xi-api-key': getKey(), 'Content-Type': 'application/json' },
    body: payload
  });
  if (!r.ok) {
    const t = await r.text();
    throw new Error(`${r.status} ${t.slice(0, 300)}`);
  }
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(file, buf);
  return { id, cached: false, chars: clean.length };
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const pathname = decodeURIComponent(url.pathname);

  if (req.method === 'POST' && pathname === '/api/speak') {
    let body = '';
    req.on('data', (c) => { body += c; if (body.length > 4000) req.destroy(); });
    req.on('end', async () => {
      try {
        const data = JSON.parse(body || '{}');
        const voice = VOICES.has(data.voice) ? data.voice : 'TX3LPaxmHKxFdv7VOQHJ';
        if (!data.text || !String(data.text).trim()) return sendJson(res, 400, { error: 'text required' });
        const out = await synth(data.text, voice);
        sendJson(res, 200, { url: `/audio/${out.id}.mp3`, cached: out.cached, chars: out.chars });
      } catch (e) {
        sendJson(res, 500, { error: String(e.message || e) });
      }
    });
    return;
  }

  if (pathname === '/api/voices') {
    return sendJson(res, 200, { voices: [...VOICES] });
  }

  let rel = pathname === '/' ? '/index.html' : pathname;
  const file = path.join(PUBLIC, rel);
  if (!file.startsWith(PUBLIC)) return sendJson(res, 403, { error: 'forbidden' });
  fs.readFile(file, (err, data) => {
    if (err) {
      fs.readFile(path.join(PUBLIC, '404.html'), (e2, d2) => {
        res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(e2 ? 'Not found' : d2);
      });
      return;
    }
    const ext = path.extname(file).toLowerCase();
    res.writeHead(200, {
      'Content-Type': MIME[ext] || 'application/octet-stream',
      'Cache-Control': ext === '.mp3' ? 'public, max-age=31536000, immutable' : 'no-cache'
    });
    res.end(data);
  });
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`BRAINROT MART running at http://127.0.0.1:${PORT}`);
});
