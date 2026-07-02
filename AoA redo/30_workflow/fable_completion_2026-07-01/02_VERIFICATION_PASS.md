# 02 — THE ONE LARGE VERIFICATION PASS (run this FIRST)

**Owner:** Fable (author of the ledger) → CC re-verifies a sample independently.
**Prepend:** `01_MASTER_PREAMBLE.md`.
**Output:** a single prioritized **DEFECT LEDGER** file at
`AoA redo/30_workflow/fable_completion_2026-07-01/LEDGER.md`. No fixes in this pass — audit
only. Every finding must cite the command + file:line that proves it.

Do this before any buildout. It tells us what "make sense" means concretely, and it
protects the buildout from inheriting existing defects.

---

## Scope — six audits, one ledger

### A. Item→stage tier / softlock audit (the real one, not a surface check)
For every `type: "item"` task in every chapter in `config/ftbquests/quests/chapters/*.snbt`:
1. extract the item id and the chapter's age (resolve age via the chapter `group:` field
   against `chapter_groups.snbt` — do NOT trust the filename; `entering_the_iron_era.snbt`
   is a Dark Ages chapter despite its name).
2. look up that item's unlock stage in the `aoa_astages_01*.js` scripts.
3. flag any item whose unlock stage is LATER than its chapter's age (this is a softlock).
Build or reuse a script for this (memory references `aoa_gate_audit.py` — verify whether it
exists on disk first; if not, write a fresh one and save it under this folder). Output: a
table of `chapter | quest id | item | item unlock stage | chapter age | VERDICT`.

### B0. Whole-roster coverage reconciliation (the big one)
Load `AoA redo/30_workflow/mod_quest_coverage_census_2026-07-02.md` (546 jars, 303 content
mods, 216 not fully done) and `02a_COMPLETION_BACKLOG.md`. Re-verify a 15% random sample of
its PARTIAL/ZERO verdicts by grepping the chapters yourself (the census can go stale as
authoring proceeds). Confirm the foundation gaps by hand: `ae2:controller`, `ae2:drive`,
`refinedstorage:controller`, `mekanism:enrichment_chamber`, `oritech:machine_core_1`,
`immersiveengineering:blast_furnace`, `spectrum:pedestal_moonstone`,
`avaritia:extreme_crafting_table` should all still be 0 across chapters. Refresh the backlog
with any drift. This reconciliation is the coverage baseline for every per-age prompt.

### B. Create machine coverage reconciliation
Cross-reference `AoA redo/40_create_addons/*.md` (the per-mod research) against actual quest
coverage (`grep` the chapters for each Create namespace). Confirm every installed Create
machine is either (a) quested, (b) intentionally deferred per the doc, or (c) a gap. Produce
the delta vs the docs (the docs predate the Phase 1/2/4 rollout, so several "0 quested"
verdicts in them are now stale — report the CURRENT state). Explicitly confirm the two
zero-coverage, **ungated** add-ons: `create-aeronautics-bundled` and
`create-stuff-additions` (neither has an AStages gate — verify with
`grep -rniE 'aeronautic|create_sa|createstuff' kubejs/` and note that substring "simulated"
false-matches Integrated Farming's hydroponic bed — do not count that).

### C. Neo Vitae spine integrity
- Confirm anchor A1 status: does `ren_magic_foundations.snbt` still route F&A node
  `0B03101000000039` into capstone aggregator `0B0310100000CAFE`? (Expected: yes, still
  unfixed.) Report the exact lines.
- Confirm `#aoa:magic_feedstock` tag membership (`kubejs/data/aoa/tags/item/magic_feedstock.json`)
  and that `ir_native_capstone_recipes.js` + `magic_spine_bridges.js` consume the tag.
- Report the Hephaestus Forge non-monotonic tier gating (T1 ren / T2 IR / T3 gilded / T4 ren
  / T5 ren) from `aoa_astages_01m_magic.js` and flag it for a canon call.

### D. Cross-weave integrity
For each `kubejs/server_scripts/aoa_recipes_*_weaves.js` and the bridge scripts
(`magic_spine_bridges.js`, `ir_magic_feedstock_bridges.js`, `ir_native_capstone_recipes.js`,
`aoa_recipes_capstone_convergence.js`, `aoa_oil_spine_weaves.js`): `node --check` it, and
scan every recipe's input/output ids — flag any id that does not resolve to an installed
mod (grep the jar list). A weave that outputs or consumes a non-existent id is a silent
break. Report `script | recipe | bad id`.

### E. Structural defect sweep (known list — confirm + extend)
Confirm and precisely locate these already-suspected defects, and hunt for more of each kind:
- **87 em dashes** in `en_us.snbt` (canon bans them). Report count + the quest ids.
- **4 missing `quest_desc`** in `g6_circuits_and_current.snbt`: ids `051AB096CA0848B4`,
  `A818144300D946A8`, `7C0AC10000000001`, `7C0AC10000000002` (+ 6 more out-of-scope in
  Renaissance/Medieval — list them too).
- **`entering_the_iron_era.snbt`** filename ≠ age (it's Dark Ages). Note the `filename:`
  field inside and any cross-references before anyone renames it.
- **7 non-array `quest_desc`** in `ow6_beyond_the_veil` (single-string form) — normalize
  target.
- **`at6` numbering gap** (no `at6_*.snbt` on disk) — confirm intentional or a missing file.

### F. Dependency-graph sanity (whole pack, quick)
Parse every quest's `dependencies:` and resolve against the global id map. Report any
dangling dependency (points at a non-existent id) and any orphan cluster (a quest reachable
from nothing and gating nothing). Prior pass found ZERO dangling deps in IR→Ascension —
confirm that still holds and extend to Dark→Renaissance.

---

## Ledger format

```
## DEFECT LEDGER — 2026-07-01
| # | severity | class | location (file:line / quest id) | finding | owner | proof cmd |
|---|----------|-------|----------------------------------|---------|-------|-----------|
```
Severity: `SOFTLOCK` > `BROKEN` (dangling dep / bad weave id) > `CANON` (tier/voice
violation) > `HYGIENE` (naming/format). Owner: which model fixes it (Fable/Opus/Codex/CC).
Sort by severity. End with a one-paragraph plain-English summary: is the pack currently
coherent, and what are the top 5 things to fix before buildout.

---

## CC re-verification (defense in depth — required by canon)
After Fable produces `LEDGER.md`, CC independently re-checks: (1) every `SOFTLOCK` row by
hand, (2) a random 10% sample of the tier-audit rows, (3) the Neo Vitae A1 claim. CC signs
off or bounces the ledger. Do not start buildout until the ledger is signed.
