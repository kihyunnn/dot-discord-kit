# Dot Discord Kit setup prompt

Give this repository URL and this prompt to your coding agent.

```text
You are onboarding Dot Discord Kit on this computer.

PHASE 1 — DISCOVER, READ ONLY
- Read README.md and this prompt.
- Inspect only safe metadata: OS, runtime versions, installed commands,
  repository names, Discord Bot configuration presence, loopback CDP reachability,
  DevSpace/Omonya markers, existing bridge processes/routes, and memory/config
  filenames that the user has made available.
- Never read or print cookies, browser profiles, tokens, passwords, private
  messages, raw environment output, or credential files.
- Emit schemas/discovery.schema.json with observed, missing, redacted, and unknown
  values. Unknown is a valid result; never guess.

PHASE 2 — DIAGNOSE AND RECOMMEND
- Explain what was observed and what was not observable.
- Recommend one profile and two alternatives with reasons, capabilities,
  limitations, required human consent, and rollback steps.
- Ask the user to choose. Do not mutate anything before the choice.

PHASE 3 — CONSENT CHECKPOINTS
- Before every install, file edit, config write, service change, external post,
  or credential-related step, show the exact action and ask for confirmation.
- Discord account/application/Bot/guild creation, OAuth consent, Bot-token entry,
  and Dot login are human-only steps. The agent may generate the official URL and
  verify the result, but must not create, approve, or scrape them.

PHASE 4 — APPLY AND VERIFY
- Apply only the approved profile.
- Verify Bot identity, guild membership, selected channel, thread permission,
  intents, route ownership, Dot/CDP availability, and exactly one result writer.
- `SETUP_READY` is allowed only after independent verification; opening a URL or
  clicking a button is not proof.
- Run a harmless canary and record PASS/FAIL plus rollback instructions.

HARD BOUNDARIES
- Official Bot only. Never use a Discord user token, QR user sign-in, session
  extraction, or self-bot. With Agent Messenger, use only agent-discordbot.
- Read docs/licenses-and-terms.md, summarize the Agent Messenger, OmO, Discord,
  and OpenAI terms for the user, and do not copy third-party source into any
  published repository.
- Raw CDP is loopback-only. Never expose it publicly.
- Discord threads do not create independent Dot model contexts.
- A click without a provider receipt is UNKNOWN; do not blindly resend.
- Default access is owner-only.
- Do not enable DevSpace without explicit approval.
- Keep files text-only/metadata-only until byte-level retrieval is proven.
- Do not publish, commit, or send messages externally unless the user explicitly
  asks for that final action.
```
