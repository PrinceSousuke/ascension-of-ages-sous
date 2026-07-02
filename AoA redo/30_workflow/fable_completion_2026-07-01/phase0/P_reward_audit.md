# Phase 0 — Quest Reward Audit (age-leak + trivialization)

**Scope:** every `rewards:` block in `config/ftbquests/quests/chapters/*.snbt` (56 files) and
every table in `config/ftbquests/quests/reward_tables/*.snbt` (65 files).
**Method:** scripted — `phase0/reward_audit.py` (data dump `phase0/_reward_dump.json`).
**Age authority:** `kubejs/server_scripts/aoa_astages_*.js`, most-restrictive-wins (3470 item
locks + 35 tag locks parsed from the explicit `[stage, id, kind]` lock arrays and
`softItemLock/addOreRestriction` literal calls). Chapter→age from `SHARED_CONTEXT.md`.
**Verdict:** No age-leaks. Reward economy is age-scoped and conservative. Findings are
low-severity trivialization/hygiene notes plus a large body of pre-authored-but-unreferenced
tables that will matter during buildout.

---

## Headline numbers

| Metric | Value |
|---|---|
| Age-leaks (reward stage later than granting chapter's age) | **0** |
| Trivialization findings | **6** (all CONFIDENCE: LOW–MED; none SOFTLOCK/BROKEN) |
| Non-standard command rewards | **0** (all 79 are `/astages add` or `/advancement grant`) |
| Reward tables total / referenced / unreferenced | 65 / **16** / **49** |
| Direct item rewards (chapters) | 88 (81 distinct) |

---

## 1. AGE-LEAK CHECK — result: CLEAN

No reward (direct item **or** reward-table entry reachable from a lower-age chapter) resolves
to an AStages stage later than its source chapter's age. Two things were checked:

- **Direct item rewards:** 22 of 88 direct item rewards match a locked id. All 22 are
  atomic-tier uranium/thorium/plutonium items rewarded **inside atomic chapters**
  (`at1_nuclear_dawn`, `at2_the_periodic_table`) — same-age, legal. Proof:
  `python phase0/reward_audit.py` → `=== LEAKS ===` prints nothing.
- **Reward-table entries reachable from a lower age:** every referenced table's gated contents
  sit at or below the lowest referencing chapter's age. The industrial caches
  (`7500000000000003`, `7500000000000001`, `7400000000000001`) hold only IR/Medieval-legal
  Create/PneumaticCraft/MI items; `nuclear_random_cache` (`7600000000000001`) is referenced only
  by atomic chapters and its highest item is atomic. Proof: the table-vs-lowest-ref comparison in
  the script yields an empty leak list.

**Leak table:** *(empty — no rows)*

---

## 2. TRIVIALIZATION CHECK (judgment)

The clean baseline here is real: reward tables use small `loot_size` (1–2), low weights on the
few "power" items, and modest stack counts. Findings below are the only ones worth a canon call,
all low severity.

| # | Finding | Confidence | Detail |
|---|---|---|---|
| T1 | `at1_nuclear_dawn` rewards raw/dust uranium for the quest that tasks gathering it | LOW | HYGIENE. Quests `4E44011000000100` / `4E4401100000010D` reward `alltheores:uranium_dust`, `mekanism:block_raw_uranium`, `createnuclear:raw_uranium_block` (x1–x4) — the same ids the quest's own `item` task requires. This is a self-reward (you keep a token of what you just processed), not a skip of a *later* quest. Cosmetically it reads as "handing you back your input." Not a progression break. |
| T2 | `industrial_random_cache` can drop `pneumaticcraft:printed_circuit_board` while `ir_pneumaticcraft_pressure_plastic` tasks building the PCB line | MED | The PCB is the taught centerpiece of the PneumaticCraft chapter (thermopneumatic/UV process). A random cache handing a finished PCB slightly undercuts that lesson. Mitigated: weight 0.6 (lowest in the table), x1, loot_size 2 — a rare single unit, not a bypass. Same pattern for `pneumaticcraft:electrostatic_compressor` (w2.0) and `create:mechanical_crafter` (w0.5) in `industrial_loot_cache`. |
| T3 | `automation_random_cache` / `industrial_loot_cache` drop `create:mechanical_arm`, `create:rotation_speed_controller`, `create:mechanical_crafter` | LOW | These Create automation blocks are tasked in Create chapters. Weights are deliberately tiny (0.5–1.2). Acceptable "nice pull" variety, not a skip. |
| T4 | `minecolonies_common` swamps early economy with bulk commodities | MED | 58 entries incl. `minecraft:cobblestone x64`, `stone/granite/diorite/andesite x64`, `glass x32`, `white_wool x32`, `torch x32`, `oak_log/leaves x16`. This is a genuinely large free-material pool. Defensible because MineColonies is an **age-agnostic Annex** built around bulk construction supply, and it is referenced only by `minecolonies.snbt`. Flag for a canon call only if MineColonies rewards should be metered rather than bulk. |
| T5 | `stone_loot_cache` includes `minecraft:golden_apple` (w0.4) | LOW | A golden apple in Dark Ages is a small power spike, but the weight is the lowest in the pool and loot_size is 2. Borderline; keep. |
| T6 | `g6_circuits_and_current` hands full `aquaculture:neptunium_*` armor set + tools and `hybrid-aquatic` gear as direct rewards for the same chapter's ocean branch | LOW | These are the quest branch's *own* completion rewards (make the gear → the node that tasks it rewards a spare/kit), not an earlier node granting the endgame set. Age-legal (gilded). No skip of a later age. Noted only because it is a full armor set delivered as reward. |

**No trivialization finding rises to a bypass or softlock.** The reward tables were clearly tuned
with progression in mind (power items down-weighted, commodities bulk only where age-agnostic).

---

## 3. TABLE-BY-TABLE BREAKDOWN

### Referenced tables (16) — these actually fire from quests

| hexid | file | loot_size | #entries | lowest ref age | power range / note |
|---|---|---|---|---|---|
| 7ACE4BD2F80103E3 | choice_compost | 1 | 5 | dark_ages | seeds/bonemeal, trivial |
| 3FCE6C893B181A17 | choice_food | 1 | 27 | dark_ages | food/crops x8–16, no gear |
| 7100000000000002 | stone_choice_cache | 1 | 7 | dark_ages | early tools/food |
| 7100000000000003 | stone_loot_cache | 2 | 10 | dark_ages | farmersdelight/cold_sweat + `golden_apple` w0.4 (T5) |
| 7100000000000001 | stone_random_cache | 2 | 8 | dark_ages | cold_sweat waterskin/boiler, comforts |
| 7400000000000001 | automation_random_cache | 2 | 8 | industrial_revolution | Create automation, low-weight arm/RSC (T3) |
| 7500000000000003 | industrial_loot_cache | 2 | 10 | industrial_revolution | PneumaticCraft/MI; compressor/crafter low-weight (T2/T3) |
| 7500000000000001 | industrial_random_cache | 2 | 9 | industrial_revolution | circuits; `printed_circuit_board` w0.6 (T2) |
| 7600000000000001 | nuclear_random_cache | 2 | 8 | atomic | Mek/nuclearscience, all atomic-legal |
| 732BC3249916AB5F | choice_crush | 1 | 5 | (minecolonies) | crushed materials |
| 6BECD56C7F7B27C5 | choice_flowers | 1 | 13 | (minecolonies) | flowers |
| 44D355363D3500BF | choice_hospital | 1 | 6 | (minecolonies) | food/medical |
| 7207C95EDFE6DFFD | choice_logs | 1 | 8 | (minecolonies) | logs |
| 14C4691141636B06 | choice_sapling | 1 | 7 | (minecolonies) | saplings |
| 11DC90A8AF7A34C3 | choice_stone | 1 | 7 | (minecolonies) | stone types |
| 23A030D0854BAACF | minecolonies_common | 1 | 58 | (minecolonies) | **bulk commodities x16–64 (T4)** |

*(minecolonies / choice_* tables belong to the age-agnostic MineColonies Annex; treated as
no-age-constraint per SHARED_CONTEXT. They are internally consistent but bulk-heavy — T4.)*

### Unreferenced tables (49) — authored, no quest points at them yet

These exist in `reward_tables/` but **zero quests reference them** (no `table_id` match). They
are dormant. They matter for buildout: when later-age chapters get their reward blocks authored,
these are the intended pools and each will need its own leak re-check.

`ascension_bundle_common/prestige/rare/useful`, `ascension_choice_relic`, `ascension_loot_relic`,
`ascension_random_relic`, `automation_bundle_common/rare/useful`, `automation_choice_cache`,
`automation_loot_cache`, `automation_obsidilith_cache`, `expedition_bundle_*` (3),
`expedition_choice_cache`, `expedition_loot_cache`, `expedition_maledictus_cache`,
`expedition_random_cache`, `industrial_bundle_*` (3), `industrial_choice_cache`,
`industrial_void_titan_cache`, `mechanical_bundle_*` (3), `mechanical_choice_cache`,
`mechanical_loot_cache`, `mechanical_random_cache`, `nuclear_bundle_*` (3), `nuclear_choice_cache`,
`nuclear_geburah_prestige_cache`, `nuclear_loot_cache`, `nuclear_macabre_cache`,
`space_bundle_*` (3), `space_choice_cache`, `space_leviathan_prestige_cache`, `space_loot_cache`,
`space_random_cache`, `stone_bundle_common/rare/useful`, `wda_food`.

> **Buildout note:** the naming implies a per-age tier system (`_bundle_common/useful/rare` +
> `_random/_choice/_loot_cache` + boss `_prestige/_cache`) that is only wired for stone / automation
> (IR) / nuclear (atomic) random-caches so far. The bundle tiers and all the boss-prestige caches
> are dormant. Prestige/relic pools (`ascension_*`, `*_prestige_cache`) are the highest-power tables
> and must be re-audited for leakage the moment a chapter references them.

---

## 4. COMMAND REWARDS — result: CLEAN

79 command rewards total across all chapters. Every one is either:
- `/astages add {p} <stage> true true` (age/proof stage grants), or
- `/advancement grant ...`

**No** command reward grants items, effects, xp, or anything beyond the sanctioned
stage/advancement pattern. No `/give`, `/effect`, `/xp`, `/gamerule`, etc. Proof:
`reward_audit.py` `=== COMMAND REWARDS ===` prints nothing (empty after the standard-prefix
filter), and the distinct-prefix dump shows only those two verbs.

---

## 5. BASELINE REWARD-ECONOMY SHAPE (pre-buildout)

Rewards resolved per age (item + xp + loot/random/choice + command reward objects; `null` = the
age-agnostic Journey/MineColonies files):

| Age | reward objects | xp total |
|---|---|---|
| dark_ages | 21 | 75 |
| medieval_times | 223 | 15,750 |
| the_renaissance | 318 | 4,700 |
| industrial_revolution | 814 | 10,770 |
| gilded_age | 517 | 26,770 |
| atomic | 445 | 34,000 |
| otherworldly | 39 | 2,550 |
| ascension | 24 | 3,500 |
| (age-agnostic) | 122 | 1,090 |

Shape observations (for buildout planning, not defects):
- **Otherworldly (39) and Ascension (24) are thin** vs their neighbors — consistent with the known
  under-authored upper ages. The dormant `space_*` and `ascension_*` tables are the intended fill.
- **XP is lumpy:** atomic (34k) and gilded (26.8k) dwarf renaissance (4.7k) and IR (10.8k) despite
  IR having by far the most reward objects. Not a leak, but a balance note — xp-level rewards are
  concentrated in the mid-late tech ages.
- Dark Ages is intentionally sparse (75 xp) — survival minimalism per canon.

---

## 6. FIX LIST

Nothing here is a merge blocker. Ordered by value:

1. **(MED, T2)** Consider removing `pneumaticcraft:printed_circuit_board` and
   `pneumaticcraft:electrostatic_compressor` from the IR random/loot caches, or gating those pulls
   behind the PneumaticCraft chapter capstone, so the taught centerpiece is not handed out early by
   RNG. Currently mitigated by w0.6/w2.0 + loot_size 2 (rare), so this is polish.
2. **(MED, T4)** Canon call on `minecolonies_common`: keep bulk (MineColonies is build-supply by
   design) or meter the x64 commodity stacks. No age impact either way.
3. **(LOW, T1)** Cosmetic: the at1 uranium self-rewards read as "handing back your input." Optional
   swap to a downstream token (e.g. a small xp or a processing byproduct) if desired.
4. **(BUILDOUT)** Before any upper-age chapter is wired to the dormant `space_*`, `ascension_*`,
   `*_prestige_cache`, or `*_bundle_*` tables, re-run `phase0/reward_audit.py` — those pools are the
   highest-power and currently untested against a live referencing age.
5. **(LOW, T5)** Optional: drop `minecraft:golden_apple` from `stone_loot_cache` if Dark Ages is
   meant to be strictly pre-gold-apple. Weight is already minimal.

---

### Verification / reproduce
- `python "AoA redo/30_workflow/fable_completion_2026-07-01/phase0/reward_audit.py"`
- Data: `phase0/_reward_dump.json`, full run log `phase0/_run.txt`.
- Lock source of truth: `kubejs/server_scripts/aoa_astages_01*.js` (item/machine locks),
  `_03_` (dimensions), `_06_` (ores/materials), `_08_` (bosses). Most-restrictive-wins.

### Method limitation (disclosed)
The lock map is built from the explicit `[stage, id, kind]` arrays and literal
`softItemLock/addOreRestriction` calls (3470 ids). The programmatic ore-material family expansion
in `_06_` (`addAdvancedMaterialTags`) generates `c:` tag locks by material token; those are captured
as tag locks but are not resolved back onto every concrete ingot/dust item id. In practice this does
not change the verdict: the only gated items appearing as rewards are the explicitly-locked
uranium/thorium ids (all same-age), and no rewarded ingot fell into a leaked-material gap. If a future
reward hands a raw modded ore/ingot of a gated material, resolve it against the `_06_` material→stage
table by hand.
