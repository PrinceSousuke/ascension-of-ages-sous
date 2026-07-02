# 04 — OTHERWORLDLY: FULL BUILDOUT (spine → complete)

**Owner:** Fable (structure/quests/weaves) → Opus (prose) → CC (age-discipline + softlock review).
**Prepend:** `01_MASTER_PREAMBLE.md`. **Depends on:** `LEDGER.md` signed.
**Density benchmark:** Atomic (7 chapters, 273 quests, dense + crossing-free). OW is
currently 6 chapters / **39 quests** — a spine, not a set of chapters. Build it out to a
comparable, endgame-calibrated depth. Quality over count, but these chapters must actually
teach and reward the OW-tier mods, not stub them.

---

## Step 1 — CENSUS (verify before authoring; produce a census table)

Derive the OW content set yourself from disk — do not trust this list blind, verify each:
1. `grep` the `aoa_astages_01*.js` scripts for every id gated to `otherworldly`. Expect:
   **Stellaris** (rocket, space cables/tanks/banks, planets), **Draconic Evolution** base +
   wyvern tier (crafting_core, energy_core, wyvern gear/tools), **Modern Industrialization**
   quantum/plasma/superconductor + **fusion** tier, **ballistix** antimatter/darkmatter,
   **Mekanism** quantum/multiversal, **advanced_ae** quantum (needs `ae2:singularity`),
   **industrial_foregoing** supreme-frame, dimension `the_afterdark`, Stellaris planets.
2. For each, confirm the item ids against the jar (`unzip -l` the mod jar → `data/<ns>/`).
3. Cross-check what's ALREADY quested in ow1–ow6 (39 nodes) so you extend, never duplicate
   (first-placement-wins).
Output a census table: `mod | OW-tier items | already quested? | target chapter`.

## Step 2 — CHAPTER PLAN (keep the 6 existing files + their intent; deepen each)

Read each chapter's existing nodes to lock its theme, then build it to full depth:

- **ow1_launch_window** (currently 4) — Rocketry / Stellaris launch infrastructure. Build:
  rocket assembly multiblock, fuel loop, launch pad, first orbital/planet reach. Gate the
  planet-dimension access here.
- **ow2_strange_dimension_operations** (5) — operating in `the_afterdark` + planet dims:
  life support, power-in-a-dimension, resource extraction off-world, hazard mitigation.
- **ow3_dragon_technology** (5) — **Draconic Evolution base + wyvern tier**: draconic core
  crafting, energy core (tiered storage multiblock), wyvern tools/armor, particle
  generator/energy infuser. This is a big mod — give it real depth (it's the OW showpiece).
- **ow4_the_dyson_project** (5) — megascale energy: MI fusion/plasma tier, Dyson-swarm
  framing, ballistix high-tier reactors, mass energy banking (Stellaris banks / Draconic
  energy core convergence).
- **ow5_the_digital_cosmos** (7) — endgame digital: AE2 advanced_ae quantum tier
  (`ae2:singularity` → quantum bridge), Refined Storage INFINITE tier, Mekanism
  quantum/multiversal QIO-style logistics, autocrafting-at-scale.
- **ow6_beyond_the_veil** (13, has the Neo Vitae OW wing already) — the OW capstone chapter.
  Extend the Neo Vitae apex wing, then the **Leviathan** capstone: kill `cataclysm:the_leviathan`,
  proof `cataclysm:tidal_claws`, grant `ascension` + `ow_capstone_complete`. Also normalize
  the 7 non-array `quest_desc` here (ledger defect) — hand to Codex.

If depth demands it, you MAY add a new OW chapter (e.g. an `ow7_*` for a mod that doesn't fit
the six), but only with explicit justification in the census; prefer deepening existing
chapters to avoid group-graph churn.

## Step 3 — CROSS-WEAVES + EDGE CASES (see prompt 06 for the full spec)
OW is where several mod economies collide. Author `aoa_recipes_otherworldly_weaves.js`
following the `aoa_recipes_<age>_weaves.js` pattern. Handle at minimum:
- `ae2:singularity` availability for the advanced_ae quantum gate (is it obtainable at OW?
  if not, weave a route or re-gate — flag as canon call).
- Draconic energy core ↔ MI/Mekanism power interop (RF/FE bridge sanity).
- Stellaris fuel ↔ oil/petrochem chain (does the fuel have a legal OW-tier recipe path?).
- any OW-tier recipe that secretly requires an Ascension-only material = softlock; re-source
  or re-gate.

## Step 4 — WIRE + LAYOUT
- Every chapter roots on the previous OW chapter or the Gilded→Atomic→OW spine; the age
  entry is the `atomic → otherworldly` grant. Confirm the incoming dependency id.
- Crossing-free (hard). Compute crossings before finishing; if any cross, re-lay.
- `ow6` capstone node must carry the `/aoa reward grant_team` + `/advancement grant` +
  `ascension` stage grant (mirror the Atomic capstone `at7` node as the template).

## Deliverables
- 6 (or 7) OW chapters built to depth, crossing-free, VERIFICATION LOG per node.
- `aoa_recipes_otherworldly_weaves.js` (`node --check` PASS).
- Census table + before/after quest counts appended to `LEDGER.md`.
- Stub lang keys + teaching briefs for every new node (Opus fills via prompt 07).
- A dependency-flow sketch (even ASCII) of the final OW chapter graph so the crossing-free
  claim is auditable by CC.
