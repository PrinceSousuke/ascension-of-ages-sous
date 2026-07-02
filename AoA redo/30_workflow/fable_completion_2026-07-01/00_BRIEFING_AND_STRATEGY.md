# 00 — BRIEFING + STRATEGY: using Fable to finish the AoA questlines

_Compiled 2026-07-01. Every number verified on disk this session (agents + independent
recount). Supersedes the 2026-06-10 memory claim that Atomic/OW/Ascension prose was still
placeholder — that work has since shipped._

---

## The one-paragraph version
The premise "finish the prose" is mostly already true: IR, Gilded, and Atomic are done and
dense (1,052 quests, ~99.6% real prose). The real remaining work is four buckets — (1)
Otherworldly + Ascension are **spines, not chapters** (~40 quests each vs 270–410 for the
lower ages); (2) the **Create add-on rollout is mid-flight** (Phases 1/2/4 shipped, **Phase 3
= Gilded flight/propulsion never started**, Aeronautics + Stuff & Additions fully unquested
AND ungated); (3) a short **defect list** (87 em dashes in the lang file, 4 missing g6
descriptions, one misnamed chapter); (4) a **real tier/softlock audit** has never run (only
a surface check). And the key strategic correction from you: **Fable authors structure,
quests, and cross-weaves; Opus writes prose; Fable does not spend cycles on language.**

## Verified state (recounted on disk)

| Age | Chapters | Quests | Real prose | Status |
|---|---:|---:|---|---|
| Industrial Revolution | 9 | 411 | 100% | Done, dense |
| Gilded | 7 | 368 | 98.9% | Done except 4 missing descs in `g6` |
| Atomic | 7 | 273 | 100% | Done, dense |
| Otherworldly | 6 | **39** | 100% real | **Spine only** — build out |
| Ascension | 7 | **40** | 100% real | **Spine only** — build out |

Create add-ons: 20 installed + doc'd, all jars present. Coverage is partial and uneven.
Confirmed **zero-coverage AND ungated:** `create-aeronautics-bundled`,
`create-stuff-additions`. Thin/partial: Create 6.0 Factory Logistics, New Age entry rung,
Metalwork alloy-by-pour, Aquatic Ambitions mechanics, Propulsion (~97% open). Correctly
un-questable (no items): `create_ultimate_factory`, `create_cold_sweat`.

Canon state is **mixed, not shipped**: Neo Vitae is the live magic spine but capstone
anchor A1 still points at Forbidden & Arcanus; Hephaestus Forge tier gating is non-monotonic
(likely a bug); the Renaissance redistribution + Apotheosis tier moves are still a runbook,
not executed. These are flagged for canon calls, not silently "fixed."

Note on your ask: the **AoA redo folder is inside the workspace**, not outside it, and it's
now small — only `30_workflow/` (invasions) and `40_create_addons/`. The old
`fable5_completion_2026-06-09` folder was cleaned up (gitignored → gone). This pack replaces
it.

---

## The strategy: four models, one lane each

You told me Fable should build and Opus should write. That inverts the usual "Fable = prose"
assumption, and it works here because of one structural fact about this pack: **prose and
structure live in different files.** Structure is in
`config/ftbquests/quests/chapters/*.snbt`; every player-facing string is in
`config/ftbquests/quests/lang/en_us.snbt`, keyed by quest id. So the models can't step on
each other.

| Model | Lane | Why |
|---|---|---|
| **Fable** | Structure: quest-node graphs, dependency wiring, AStages gates, cross-weave recipe scripts, mod fleshing-out, edge cases. Emits stub lang keys with teaching briefs. | Fast, follows structured mechanical specs. Its ID-hallucination hazard is contained by the mandatory verify-first protocol + logs. |
| **Opus** | Prose: writes `en_us.snbt` from Fable's briefs. Voice QA. | Quality spent where players actually read. Never touches structure. |
| **Codex** | Deterministic bulk: mass find/replace, format normalization, `node --check` sweeps, crossing computation, gate-audit runs. | Long-context deterministic transforms; boring at scale. |
| **Claude Code** | Reasoning verification: age-discipline review, softlock re-audit, canon-call judgment, final merge gate. | Judgment + independent verification, per the canon "always verify before reading back." |

**The safety spine (this is what makes it OK to let Fable author structure):** every
structural deliverable ships a VERIFICATION LOG — for each item id, the grep + the file/jar
that proves it exists + the AStages line proving it's legal at that age; for each script, a
`node --check` PASS. No log = rejected. Then CC independently re-verifies a sample. This is
how you use a hallucination-prone model on high-stakes work without eating softlocks.

## The handshake, per unit of work
```
Fable (structure + stub briefs + verification log)
   → Opus (fills prose from briefs, lang file only)
      → Codex (normalize format, node --check, crossing math)
         → CC (age-discipline re-audit + capstone-chain + merge gate)
```

---

## How to run it (sequence)

1. **`02_VERIFICATION_PASS`** — FIRST. Produces `LEDGER.md`: the real tier/softlock audit,
   Create coverage delta, Neo Vitae anchor status, defect list. Nothing else starts until
   CC signs the ledger. This is your "does the current questline make sense" answer.
2. **`03_CREATE_GAPS_AND_QA`** — close all Create gaps (Phase 3 flight, Stuff & Additions,
   Factory Logistics, New Age, Metalwork, Aquatic) + gate the two ungated add-ons + QA read.
3. **`04_OTHERWORLDLY_BUILDOUT`** then **`05_ASCENSION_BUILDOUT`** — spine → full, in order
   (Ascension roots on OW's capstone). Census-verify each age's mods first.
4. **`06_CROSS_WEAVES`** — runs alongside 03/04/05; a chapter needing a cross-mod item is
   only safe once its recipe path is legal at that age.
5. **`07_PROSE_PASS_OPUS`** — Opus fills every stub + clears the 87 em dashes + the 4 g6
   descs.
6. **`08_CLEANUP_AND_FINAL_VALIDATION`** — Codex deterministic cleanup; CC final merge gate.

`01_MASTER_PREAMBLE` prepends every prompt. Prompts are model-agnostic paste blocks — drop
the preamble + the task file into whichever model owns that lane.

## What I did NOT do
I did not edit a single quest file. This session is research + strategy + the prompt pack, so
you can delegate the actual authoring the way you asked. Everything above is verified; the
canon-call items are surfaced, not decided.
