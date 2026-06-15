# Talk to Claude — voice + text chat with Dropbox transcripts

A small web app you can open on your phone or computer to chat with Claude by
**typing or speaking**. Claude replies in text and reads the reply aloud, and
**every conversation is saved to a folder in your Dropbox** automatically.

```
voice-chat/
├── public/index.html   ← the chat UI (text + voice, browser-native speech)
├── api/chat.js         ← secure proxy to the Claude API (holds your API key)
├── api/transcript.js   ← saves each conversation to Dropbox
├── package.json
├── vercel.json
└── .env.example        ← the secrets you need to fill in
```

## How it works

- **Voice in / out** uses your browser's built-in speech recognition and
  speech synthesis — no extra accounts or per-minute cost. Works in Chrome,
  Edge, and Safari. (If a browser doesn't support voice input, the mic button
  is disabled and you can still type.)
- **The two small functions in `api/`** run on Vercel and hold your secrets
  (Claude API key, Dropbox token). The keys never reach the browser, so the
  page is safe to expose publicly.
- **Transcripts** are written as one Markdown file per conversation, named by
  date and time (e.g. `2026-06-12-1430.md`), and updated as the conversation
  grows. Tap **＋ New** to start a fresh conversation (and a fresh file).

---

## Setup

You need two sets of credentials: a **Claude API key** and **Dropbox app
credentials**. Then you deploy to Vercel.

### 1. Claude API key

1. Go to <https://console.anthropic.com> → **Settings → API Keys**.
2. Create a key and copy it (starts with `sk-ant-`).

### 2. Dropbox credentials

Dropbox uses short-lived access tokens, so we set up a **refresh token** once
and the app renews access automatically.

1. Go to <https://www.dropbox.com/developers/apps> → **Create app**.
   - Choose **Scoped access**.
   - Choose **App folder** (transcripts go in a dedicated folder Dropbox
     creates for the app) or **Full Dropbox** (you pick any folder).
   - Name it anything, e.g. `claude-transcripts`.
2. On the app's **Permissions** tab, enable **`files.content.write`** (and
   `files.content.read` if you want). Click **Submit**.
3. On the **Settings** tab, copy the **App key** and **App secret**.
4. Get a refresh token (one-time). In a terminal, replace `APP_KEY` and run:

   ```bash
   # a) Open this URL in a browser, approve, and copy the "access code" it shows:
   echo "https://www.dropbox.com/oauth2/authorize?client_id=APP_KEY&token_access_type=offline&response_type=code"

   # b) Exchange that code for a refresh token (replace APP_KEY, APP_SECRET, AUTH_CODE):
   curl https://api.dropbox.com/oauth2/token \
     -d code=AUTH_CODE \
     -d grant_type=authorization_code \
     -d client_id=APP_KEY \
     -d client_secret=APP_SECRET
   ```

   The JSON response contains `"refresh_token": "..."` — copy that value.

### 3. Deploy to Vercel

From this `voice-chat/` folder:

```bash
npm install
npx vercel        # first run links/creates the project
```

Then add the environment variables (Vercel dashboard → your project →
**Settings → Environment Variables**, or via CLI):

```bash
npx vercel env add ANTHROPIC_API_KEY
npx vercel env add DROPBOX_APP_KEY
npx vercel env add DROPBOX_APP_SECRET
npx vercel env add DROPBOX_REFRESH_TOKEN
# optional:
npx vercel env add DROPBOX_FOLDER       # e.g. /Claude Chats
npx vercel env add CLAUDE_MODEL         # e.g. claude-sonnet-4-6
```

Deploy to production:

```bash
npx vercel --prod
```

Open the URL Vercel gives you, on your phone or computer, and start talking.

> **Note:** Browsers only allow microphone access over **HTTPS** (or
> `localhost`). Vercel URLs are HTTPS, so voice works out of the box once
> deployed.

---

## Local development

```bash
npm install
cp .env.example .env      # fill in your keys
npx vercel dev            # serves the page + functions at http://localhost:3000
```

## Customizing

- **Model:** set `CLAUDE_MODEL`. Default is `claude-opus-4-8`. For snappier,
  cheaper voice replies, `claude-sonnet-4-6` is a great choice.
- **Reply style / length:** edit the `SYSTEM` prompt in `api/chat.js`.
- **Transcript folder:** set `DROPBOX_FOLDER`.
- **Voice / language:** edit `recognition.lang` and the `SpeechSynthesisUtterance`
  settings in `public/index.html`.
