# AoA Public Bug Tracker + Roadmap — Setup Runbook

Created 2026-06-27. Covers the Ascension of Ages (AOA) Linear team as a player-facing bug tracker and roadmap, how to make it public, and how to wire it into Discord. Kept deliberately simple for a first pass.

## 1. What lives where

- **AOA team (Linear):** your private triage home. Separate from the Rustbucket (RUST) game team. Issues read AOA-1, AOA-2, and so on.
- **Public roadmap (Linear shared view):** a read-only link players open in a browser with no account. Shows what is planned, in progress, and shipped.
- **Discord:** intake and notifications layer. Players report, you file, the channel sees progress.

## 2. The three seed issues

| Ticket | Area | Status |
|--------|------|--------|
| Quest visibility | Quests | Open (bug) |
| Quest / age progression | Progression | Open (bug) |
| Modonomicon crash | Crash | Done (fixed) |

The Modonomicon crash starts in Done so the board shows from day one that fixes get shipped and closed. That is the "room for fixes performed" you asked for: completed work stays visible in the Done / Shipped column rather than disappearing.

## 3. Making the roadmap public (Linear native)

Linear Standard plan and up supports read-only sharing of a view.

1. In the AOA team, open the **Roadmap** project (or a saved board/timeline view).
2. Filter it to player-facing items only. Hide anything internal. A simple rule: only items carrying a `public` label appear on the shared view, so nothing leaks by accident.
3. Use the **Share** control on that view and enable a public read-only link.
4. Post that link in Discord, on the CurseForge page, and anywhere players gather.

**Caveat to know going in.** The shared link is read-only. Players can view per-issue progress and the roadmap, but they cannot submit or upvote through it. That is fine for "here is the roadmap and here is what shipped." If you later want player-submitted reports with upvotes and "notify me when fixed," see section 6.

Exact menu labels in Linear shift over time. If a control is not where described, check Linear's own docs at https://linear.app/docs for the current path.

## 4. Discord integration — the simple, first-party path (recommended)

Linear ships an official Discord integration. No custom bot or code required. Steps below are verified against Linear's docs as of 2026-06-27.

**Part A. Enable in Linear (admin, one time)**
1. Be in the rustbucket workspace, then open Settings > Features > Integrations > Discord. Direct link: https://linear.app/settings/integrations/discord
2. Click to enable/connect Discord. As workspace admin this turns it on for the whole workspace.
3. Linear sends you to Discord to authorize. Pick your Ascension of Ages server, review permissions (it needs Read Message History to attach Discord messages to issues), and approve. This adds the Linear app to that server.

**Part B. Link each account (per user, one time)**
On the same Settings > Integrations > Discord page, every person who will file tickets connects their own Discord account once. It is per-user, not workspace-wide.

**Part C. Commands (in any Discord channel)**
- `/linear issue` files a ticket. Set Title and Team (pick Ascension of Ages). Optionally set description, status, assignee, and project (drop bugs into Quests & Progression or Stability & Performance).
- `/linear search` finds an issue by ID (e.g. AOA-2) or keywords and posts a rich card to the channel.
- `/linear wrap` posts a summary of what you started or finished in the last 24h. Good as a quick public progress drop.

**Known limitation:** the integration does NOT auto-post status changes back to Discord (no automatic "your bug was fixed" pings; confirmed in Linear's docs FAQ). Shipped-fix announcements are manual via `/linear wrap` or a changelog post. For automatic notifications, use the upgrade paths in sections 5 and 6.

Docs: https://linear.app/docs/discord and https://linear.app/integrations/discord

### Optional dedicated bug channel pattern
Create a `#bug-reports` channel with a pinned template (what happened, steps, modpack version, log link). Moderators triage and run `/linear issue` on the good ones. This keeps noise out of your AOA board while still giving players a front door.

## 5. Discord — the upgrade path (only if you outgrow the above)

If you want players filing tickets directly without a moderator, or AI that prefills title and priority from the conversation, use a workflow tool or custom bot against Linear's API:

- **n8n**, **BuildShip**, or **Latenode** can watch a Discord channel or a slash command and call Linear to create issues, with custom logic in between.
- A custom Discord bot using Linear's GraphQL API gives full control (button to report, modal form, auto-tagging by channel).

These are real work to stand up and maintain. Skip until the first-party path proves too limited.

## 6. Public intake upgrade path (optional, later)

If you decide you want a true public board where players submit and upvote bugs and feature requests, and get auto-notified when something ships, the standard move is to layer a feedback portal on top of Linear rather than replace it:

- **Featurebase**, **Productlane**, **Feedvote**, or **Canny** all sync two-way with Linear. Players use the portal; their items become Linear issues; status flows back to the portal automatically.
- You keep triaging in Linear. Players never see your internal mess.

This is the answer to "is there a better website for this." Linear is the right brain for triage. A feedback portal is the right face for public intake. You do not need it on day one.

## 7. Quick reference links

- Linear Discord integration: https://linear.app/integrations/discord
- Linear Discord docs: https://linear.app/docs/discord
- Building a public roadmap on Linear (guide): https://blog.feedvote.app/how-to-build-a-public-roadmap-in-linear-2026-guide/
- Featurebase Linear integration: https://www.featurebase.app/integrations/linear
- Productlane on Linear: https://linear.app/integrations/productlane
