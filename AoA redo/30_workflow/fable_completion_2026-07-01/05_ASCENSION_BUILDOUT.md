# 05 — ASCENSION: FULL BUILDOUT (spine → complete, the endgame)

**Owner:** Fable (structure/quests/weaves) → Opus (prose) → CC (age-discipline + softlock review).
**Prepend:** `01_MASTER_PREAMBLE.md`. **Depends on:** `LEDGER.md` signed, OW buildout (04)
merged (Ascension roots on the OW→Ascension grant).
**Density:** Ascension is currently 7 chapters / **40 quests** (2–11 each). This is the
final age — it should feel like a prestige capstone, not a machine grind, but every
Ascension-tier mod must be fully fleshed out and reach a real, earned end. Endgame-calibrated
depth: fewer but heavier nodes, each a real build.

---

## Step 1 — CENSUS (verify each id against the jar)
`grep` `aoa_astages_01*.js` for everything gated to `ascension`. Expect:
- **Draconic Evolution** awakened + chaotic tier: draconic reactor (the fusion-style power
  apex), chaotic core, awakened gear/tools, chaos crystal. Reactor is a whole sub-system.
- **Re:Avaritia** — infinity catalyst → infinity ingot → infinity tools/armor; the
  cosmic/neutron collector chain; Skull altar. Prestige capstone materials.
- **Extended Crafting** elite/ultimate/**crystaltine** tier — the big autocraft tables that
  gate the Avaritia/Draconic recipes.
- Any Mekanism/AE2/MI top prestige tier not consumed at OW.
Confirm which nodes already exist in asc1–asc7 (40 nodes) and extend, never duplicate.

## Step 2 — CHAPTER PLAN (keep the 7 files + intent; build to a real endgame)
- **asc1_the_table_of_infinities** (8) — Extended Crafting elite→ultimate→crystaltine table
  progression + the Avaritia crafting substrate. This unlocks everything downstream; build
  the full table ladder.
- **asc2_the_philosophers_dream** (6) — the Avaritia collector/catalyst economy: cosmic
  meatball / neutron collector → infinity catalyst. Long-haul resource apex.
- **asc3_the_impossible_machine** (6) — Draconic + top-tier tech convergence: the machine
  that shouldn't be buildable. Fusion crafting (Draconic energy infuser), cross-mod apex
  components.
- **asc4_singularity** (2 → deepen) — the Draconic **reactor** + max energy core: the
  singularity is the reactor going critical-but-controlled. Big multiblock, big payoff.
- **asc5_the_draconic_heart** (5) — awakened/chaotic Draconic gear + the chaos crystal from
  the Guardian. Bridges into the final fight.
- **asc6_bosses_rise** (11) — **the Apex Boss Gauntlet** (canon): every apex boss from every
  boss mod + every boss from the 1–2-boss mods on the path to the Chaos Dragon. Verify the
  full boss roster from `aoa_astages_08_mob_boss_restrictions.js` + `boss_progression_proof.js`;
  each apex is a `kill` (MQT `kill_entity`) node with its proof drop. This is the endgame
  content wall. Lay it as a gauntlet converging on asc7.
- **asc7_ascension** (2) — the FINAL node. Kill `draconicevolution:draconic_guardian`
  (Chaos/Draconic Guardian) via MQT `kill_entity` (NOT a proof-item drop — the boss lock
  message is "The Chaos Dragon does not answer to an unfinished age"). Final grant:
  `/aoa reward grant_team` + `/advancement grant` + `asc_capstone_complete` + `aoa_complete`.
  This is the win screen — make it earned and singular.

## Step 3 — CROSS-WEAVES + EDGE CASES (prompt 06)
Author `aoa_recipes_ascension_weaves.js`. Ascension is where recipe softlocks are most
dangerous (everything gates everything). Handle:
- Avaritia infinity chain: confirm every input has a legal Ascension-tier source; the
  cosmic/neutron collectors are slow — make sure the quest doesn't require an amount that's
  impossible without a machine that isn't unlocked yet.
- Extended Crafting table tiers must unlock in order and BEFORE the recipes that need them
  (elite table before an elite recipe, etc.) — a classic self-softlock.
- Draconic reactor components ↔ chaos crystal (from the Guardian) circular-dependency check:
  the Guardian is the FINAL boss, so nothing pre-final may require a chaos crystal.
- Re:Avaritia + Extended Crafting recipe collisions (both add giant tables) — dedupe via the
  `zz_aoa_recipe_output_policy.js` pattern.

## Step 4 — WIRE + LAYOUT
- Root on the `otherworldly → ascension` grant (the OW capstone node in `ow6`).
- Crossing-free. The gauntlet (asc6) will be dense — lay it as parallel lanes converging, not
  a crossing web.
- asc7 is the single terminal node of the entire pack. Nothing depends on it.

## Deliverables
- 7 Ascension chapters built to endgame depth, crossing-free, VERIFICATION LOG per node.
- Full apex-gauntlet roster in asc6 verified against the boss scripts.
- `aoa_recipes_ascension_weaves.js` (`node --check` PASS).
- Census + before/after counts → `LEDGER.md`.
- Stub lang keys + teaching briefs (Opus fills via 07).
- Final-graph dependency sketch for CC audit.
