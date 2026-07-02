# 00 — BRIEFING + STRATEGY: finishing EVERY not-done mod in AoA

_Compiled 2026-07-01, expanded to the full roster 2026-07-02. Census + depth audit verified on
disk (546 jars) and hand-spot-checked. This supersedes the earlier Create-only framing._

---

## The one-paragraph version
The pack is far less finished than a chapter-by-chapter glance suggests. The *chapters that
exist* are prose-complete, but **216 of 303 content mods (71%) are not fully quested**, and the
gap is systemic: the big tech mods have dense **endgame** chapters while their **mid-game
onboarding is missing**. A player following quests never learns to place an AE2 controller, a
Refined Storage grid, a Mekanism enrichment chamber, an Oritech machine core, or an Immersive
Engineering blast furnace — all hand-verified at **0 quests**. Avaritia's compression tables,
the entire reason that mod exists, are unquested. Spectrum's pedestal front door is unquested.
On top of that, **139 content mods have no stage gate at all**. This is the real body of work,
and your instinct to use Fable to *build* it (structure/quests/cross-weaves) with Opus on prose
is the right division.

## Verified reality
| Bucket | Count | Meaning |
|---|---:|---|
| Content mods | 303 | mods with a questable surface (items/machines/mobs/structures) |
| DONE | 87 | broad task coverage |
| PARTIAL | 56 | some quests, major features/foundations missing |
| ZERO | 160 | questable, no quests at all |
| **Not fully done** | **216 (71%)** | the completion program's scope |
| Ungated | 139 | no AStages entry — **not a to-do:** gating is closed (registry Policy 1) |
| Non-questable | 252 | libraries / APIs / perf / compat / pure decor — correctly skipped |

**Standing scope (2026-07-02):** `AOA_QUEST_SCOPE_REGISTRY.md` (repo root, wired into canon §9)
is the authoritative list of mods that are OUT of scope + the "no coverage-driven gating" policy.
23 mods are excluded from questing there (RPG/skill/spell cluster, decor/QoL, flight, etc.). Any
census flagging those as "not done," or proposing gates for ungated mods, is reconciled against
that file — not re-raised. The real 216-not-done figure shrinks once the registry exclusions are
subtracted; re-run the census denominator against the registry before quoting a number.

The five ages I earlier called "done" are done *as written chapters*, not *as mods*: IR/Gilded/
Atomic carry the endgame; the foundations underneath them are the largest gap in the pack.
Otherworldly + Ascension remain thin spines (~40 quests each) needing full buildout, and there
Avaritia + Draconic top tiers are unquested. Full data:
`AoA redo/30_workflow/mod_quest_coverage_census_2026-07-02.md` + `02a_COMPLETION_BACKLOG.md`.

## The dominant defect: endgame without onboarding
This keeps recurring, so it's the organizing principle of the whole program:

| Mod | Endgame taught? | Foundation quested? |
|---|---|---|
| AE2 | yes (molecular assembler, spatial, quantum) | **no** — controller/drive/cells = 0 |
| Refined Storage | yes (autocrafter, wireless) | **no** — controller/grid/disk drive = 0 |
| Mekanism | yes (uranium, Mekasuit, QIO) | **no** — enrichment/purification spine = 0 |
| Oritech | yes (atomic forge convergence) | **no** — machine cores 1–3 = 0, no IR home chapter |
| Immersive Engineering | yes (arc furnace, Gilded tier) | **no** — blast furnace/crusher/squeezer = 0 |
| Avaritia | partial (singularity chain) | **no** — the compression tables = 0 |
| Spectrum | yes (fusion shrine, Deeper Down) | **no** — pedestal crafting = 0 |

"Foundations-first" is now rule 6 of the master preamble: author the entry rungs, then re-wire
the existing endgame quests to depend on them so the graph teaches in order.

## Strategy: four models, one lane each (unchanged, and validated by this scope)
Because prose lives in `en_us.snbt` and structure in the `.snbt` chapters, the models never
collide. **Fable** builds structure, quests, gates, and cross-weaves; **Opus** writes prose from
Fable's stub briefs; **Codex** does deterministic bulk + `node --check`; **Claude Code** does
age-discipline/softlock review + the merge gate. The safety spine: every Fable structural output
ships a verification log (grep-proof of each id + the gate proving its age), and CC re-verifies a
sample. This is what makes it safe to point a fast, hallucination-prone model at high-stakes
structural authoring across 216 mods.

## How to run it (sequence)
1. `02_VERIFICATION_PASS` → `LEDGER.md` (now includes a whole-roster coverage re-check).
2. `02a_COMPLETION_BACKLOG` is the target list for everything below.
3. Per-age completion, foundations-first, in order:
   `02b` Renaissance + earlier → `02c` **IR foundations (the big one)** → `02d` Gilded →
   `02e` Atomic → `04` Otherworldly buildout → `05` Ascension buildout.
4. `08_CREATE_GAPS_AND_QA` — the Create sub-program (Phase 3 flight + the rest), runs with the
   Gilded/IR ages.
5. `06_CROSS_WEAVES` alongside all authoring; `07_PROSE_PASS_OPUS` fills language.
6. `08_CLEANUP_AND_FINAL_VALIDATION` — Codex cleanup (incl. the `aoacore` duplicate-jar),
   the **canon decision queue** (gating now closed; only content decisions remain — Neo Vitae
   A1, Depths of Malum quest-or-skip, etc.), and CC's final merge gate.

## What I did NOT do
No quest files were edited. This is research + strategy + the prompt pack, so you can delegate
the authoring. Every gap above is verified; every judgment call is surfaced to the decision
queue, not decided for you.
