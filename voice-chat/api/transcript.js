// Saves a conversation transcript to Dropbox as one Markdown file per conversation.
//
// Dropbox auth uses the refresh-token flow (the modern, non-expiring approach):
//   DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_REFRESH_TOKEN  — required
//   DROPBOX_FOLDER  — optional, defaults to "/Claude Chats"
// All of these live server-side and are never exposed to the browser.

async function getAccessToken() {
  const resp = await fetch("https://api.dropbox.com/oauth2/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "refresh_token",
      refresh_token: process.env.DROPBOX_REFRESH_TOKEN,
      client_id: process.env.DROPBOX_APP_KEY,
      client_secret: process.env.DROPBOX_APP_SECRET,
    }),
  });
  if (!resp.ok) {
    throw new Error(`Dropbox token refresh failed (${resp.status}): ${await resp.text()}`);
  }
  const data = await resp.json();
  return data.access_token;
}

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  if (!process.env.DROPBOX_REFRESH_TOKEN || !process.env.DROPBOX_APP_KEY || !process.env.DROPBOX_APP_SECRET) {
    return res.status(500).json({ error: "Dropbox is not configured. Set DROPBOX_APP_KEY, DROPBOX_APP_SECRET, and DROPBOX_REFRESH_TOKEN." });
  }

  try {
    const { filename, content } = req.body || {};
    if (!filename || typeof content !== "string") {
      return res.status(400).json({ error: "Request body must include `filename` and `content`." });
    }

    // Keep the filename safe and ASCII; the Dropbox-API-Arg header must be ASCII.
    const safeName = filename.replace(/[^a-zA-Z0-9._-]/g, "_");
    const folder = (process.env.DROPBOX_FOLDER || "/Claude Chats").replace(/\/+$/, "");
    const path = `${folder}/${safeName}`;

    const token = await getAccessToken();

    const resp = await fetch("https://content.dropboxapi.com/2/files/upload", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/octet-stream",
        // mode: overwrite keeps a single file per conversation, updated as it grows.
        "Dropbox-API-Arg": JSON.stringify({ path, mode: "overwrite", mute: true }),
      },
      body: content,
    });

    if (!resp.ok) {
      throw new Error(`Dropbox upload failed (${resp.status}): ${await resp.text()}`);
    }

    const data = await resp.json();
    return res.status(200).json({ ok: true, path: data.path_display });
  } catch (err) {
    return res.status(500).json({ error: err?.message || "Unknown error saving to Dropbox." });
  }
}
