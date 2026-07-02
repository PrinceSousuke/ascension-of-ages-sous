# Fable Completion Pack — 2026-07-01

Delegation prompt set to verify and finish the AoA questlines, using Fable for structure,
Opus for prose, Codex/CC as the deterministic + verification backstops. All state verified
on disk 2026-07-01.

## Files (run in this order)
- **00_BRIEFING_AND_STRATEGY.md** — read first. State of pack + the four-model strategy.
- **01_MASTER_PREAMBLE.md** — prepend to EVERY prompt below. Guardrail card + verify-first
  protocol + model lanes + per-age legal tech + capstone chain.
- **02_VERIFICATION_PASS.md** — the one large audit. Produces `LEDGER.md`. Run FIRST.
- **03_CREATE_GAPS_AND_QA.md** — close all Create add-on gaps + QA (Fable→Opus→CC).
- **04_OTHERWORLDLY_BUILDOUT.md** — OW spine → full (Fable→Opus→CC).
- **05_ASCENSION_BUILDOUT.md** — Ascension spine → full endgame (Fable→Opus→CC).
- **06_CROSS_WEAVES_AND_EDGECASES.md** — cross-mod recipe bridges + softlock edge cases
  (Fable→CC→Codex). Runs alongside 03/04/05.
- **07_PROSE_PASS_OPUS.md** — Opus authors all language from Fable's stub briefs.
- **08_CLEANUP_AND_FINAL_VALIDATION.md** — Codex deterministic cleanup + CC final merge gate.

## Generated during execution (not yet present)
- **LEDGER.md** — the running defect ledger + decisions-needed queue, created by prompt 02
  and closed out by prompt 08.

## Model lanes (one line)
Fable = structure/quests/weaves/gates · Opus = prose · Codex = deterministic bulk +
`node --check` · CC = age-discipline + softlock + merge gate.

## Hard rules that get broken most (full list in 01)
8-age tier discipline · verify-first (no invented ids; log every id) · crossing-free layout ·
`.snbt` byte preservation (never strip `SkillsLevel`) · prose voice (no em dashes, no AI-isms)
· mount can lie about truncation — `node --check`/Desktop Commander is ground truth.
