import Anthropic from "@anthropic-ai/sdk";

// The Claude API key is read from the ANTHROPIC_API_KEY environment variable.
// It lives here on the server and is never sent to the browser.
const client = new Anthropic();

// Default to the most capable Opus model. Override with the CLAUDE_MODEL env var
// (e.g. "claude-sonnet-4-6" for faster, cheaper replies in a voice chat).
const MODEL = process.env.CLAUDE_MODEL || "claude-opus-4-8";

// Replies are read aloud, so keep them conversational and tight. The final-answer
// instruction keeps reasoning out of the spoken response when thinking is off.
const SYSTEM = `You are a friendly, helpful voice assistant having a spoken conversation.
Keep replies conversational and concise — a sentence or two unless more detail is genuinely needed.
Respond directly with your answer; do not narrate your reasoning or use headings, bullet lists, or markdown formatting, since the reply will be read aloud.`;

export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  try {
    const { messages } = req.body || {};
    if (!Array.isArray(messages) || messages.length === 0) {
      return res.status(400).json({ error: "Request body must include a non-empty `messages` array." });
    }

    const response = await client.messages.create({
      model: MODEL,
      max_tokens: 2048,
      system: SYSTEM,
      messages,
    });

    const text = response.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");

    return res.status(200).json({ text, model: response.model });
  } catch (err) {
    const status = typeof err?.status === "number" ? err.status : 500;
    return res.status(status).json({ error: err?.message || "Unknown error calling Claude." });
  }
}
