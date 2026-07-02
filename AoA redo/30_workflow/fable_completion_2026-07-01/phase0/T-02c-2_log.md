# T-02c-2 log — `ir_mekanism_ore_works` (NEW chapter)

**Task:** Create the new Mekanism IR ore-works chapter (5-stage enrichment→injection ore
chain + PRC/evaporation + basic factory tier). Resolves ledger row 11 (Mekanism's missing IR
home). IR group `3F77A31B7D30C0AA`.

**Files touched (contract file set — disjoint):**
- `config/ftbquests/quests/chapters/ir_mekanism_ore_works.snbt` (NEW)
- `AoA redo/30_workflow/fable_completion_2026-07-01/phase0/stubs/T-02c-2_stubs.txt` (NEW sidecar)
- `AoA redo/30_workflow/fable_completion_2026-07-01/phase0/T-02c-2_log.md` (this log)

No other files edited. No git commands run.

## Chapter-level fields
- `filename: "ir_mekanism_ore_works"`, `group: "3F77A31B7D30C0AA"` (industrial_revolution),
  `id: "4954110000000000"` (grep-confirmed unused across all chapters), `order_index: 10`
  (existing IR chapters occupy 0..8; plan assigns 9/10/11 to the three new chapters — this is T2 = 10).
- Chapter icon `mekanism:enrichment_chamber` (signature entry machine).
- Header/footer/node shape mirrored byte-for-byte from sibling `ir_power_motion_and_grid.snbt`.

## Nodes created (14 total; all task type `item`, icon = task item)

**Main spine (5-stage doubling chain + PRC + evap capstone):**
| node id | item | x | y | deps |
|---|---|---|---|---|
| 4954111000000001 | mekanism:enrichment_chamber | 0.0 | 0.0 | ["0B0310A0000000F0"] (IR gateway = chapter root) |
| 4954111000000002 | mekanism:crusher | 2.0 | 0.0 | [4954111000000001] |
| 4954111000000003 | mekanism:energized_smelter | 3.5 | 1.0 | [4954111000000002] |
| 4954111000000004 | mekanism:osmium_compressor | 3.5 | -1.0 | [4954111000000002] |
| 4954111000000005 | mekanism:purification_chamber | 5.5 | 0.0 | [4954111000000004] |
| 4954111000000006 | mekanism:electrolytic_separator | 5.5 | -1.5 | [4954111000000004] |
| 4954111000000007 | mekanism:chemical_injection_chamber | 7.5 | 0.0 | [4954111000000005, 4954111000000006] |
| 4954111000000008 | mekanism:chemical_infuser | 7.5 | -1.5 | [4954111000000006] |
| 4954111000000009 | mekanism:pressurized_reaction_chamber | 9.5 | 0.0 | [4954111000000007] |
| 495411100000000A | mekanism:metallurgic_infuser | 0.0 | 2.0 | [4954111000000001] |
| **495411100000000B** | mekanism:thermal_evaporation_controller | 11.0 | 0.0 | [4954111000000009] | **SPINE CAPSTONE (multiblock; block+valve in prose only)** |

**Factory-tier side lane (basic tier only):**
| node id | item | x | y | deps |
|---|---|---|---|---|
| 4954111000000010 | mekanism:basic_smelting_factory | 2.0 | 3.0 | [4954111000000003] |
| 4954111000000011 | mekanism:basic_enriching_factory | 3.5 | 3.5 | [4954111000000010] |
| 4954111000000012 | mekanism:basic_crushing_factory | 5.0 | 3.0 | [4954111000000011] |

**Deviation from plan coords:** plan placed metallurgic_infuser (`...000A`) at (3.5, 2.0). That
produced ONE crossing: edge enrichment(0,0)→infuser(3.5,2.0) crossed edge
energized_smelter(3.5,1.0)→basic_smelting_factory(2.0,3.0). Re-laid infuser to (0.0, 2.0) — a clean
vertical stub off the root at x=0. All other coords match the plan verbatim. Crossings now 0.

**Bare-material items NOT tasked (referenced in prose per plan):** `mekanism:ingot_steel`,
`ingot_bronze`, `ingot_osmium`, `steel_casing`, `basic_control_circuit`, and the multiblock parts
`thermal_evaporation_block`/`thermal_evaporation_valve` (bundled into `...000B`'s prose).

## Rewards
Each node: `xp: 25` + a `loot` reward drawing `table_id: 8430738502437568513L`
(= industrial_random_cache, id `7500000000000001`), mirroring sibling IR chapters. Reward/task ids
use the chapter scheme: task `4954112...`, reward-xp `4954113...`, reward-loot `4954114...` (all 16-hex).

## Re-wires
None. Plan §T-02c-2 explicitly states no structural re-wire is needed for Mekanism (Atomic factory
tiers are gated a full age later and reachable only after this IR chapter by progression; extraction
found no Atomic Mek node reachable before this chapter).

## VERIFICATION

**Item-id + AStages-legality proof (jar `Mekanism-1.21.1-10.7.19.85.jar`, lang
`assets/mekanism/lang/en_us.json`; AStages `aoa_astages_01_item_restrictions.js`):**
All 14 task items + 2 multiblock parts confirmed present in jar lang (`block.mekanism.*`) and all
IR-locked at the cited line:
- enrichment_chamber :288, crusher :289, energized_smelter :290, osmium_compressor :291,
  purification_chamber :293, chemical_injection_chamber :294, chemical_infuser :295,
  electrolytic_separator :296, pressurized_reaction_chamber :297, metallurgic_infuser :287,
  thermal_evaporation_controller :327 (block :326, valve :328),
  basic_smelting_factory :315, basic_enriching_factory :316, basic_crushing_factory :317.

**tier_audit.py:** ran; regenerated `A_tier_softlock_table.md`. All 14 `ir_mekanism_ore_works` rows
= **OK** (item age = chapter age = industrial_revolution). Zero SOFTLOCK/ILLEGAL rows from this
chapter. (The 2 SOFTLOCK rows in the table belong to `ir_digital_storage_foundations` = T-02c-1,
not this task.)

**ef_audit.py:** `DUP ids: {}` (0 duplicates), `DANGLING dep sources: 0`, `BACKWARD-age deps: 0`.
The single ORPHAN reported is pre-existing (`3400000000009000` in `stone_water_weather_and_wounds`),
not from this chapter — my root correctly deps on the IR gateway.

**Duplicate-item scan (pack-wide):** grep of entire `chapters/` for all 14 Mekanism task ids
BEFORE authoring = zero pre-existing tasks. No item duplicated.

**Anchored id-collision scan:** all 57 ids in the file are exactly 16 hex, unique within-file, and
zero collisions against every other chapter (checked all node/task/reward ids).

**Byte discipline:** CRLF 634 / LF 634 / bare-CR 0 (pure CRLF). Braces balanced (114/114), brackets
balanced (58/58). Tab indentation. `SkillsLevel`/`PlayerSpells` blocks copied byte-for-byte from
sibling `ir_power_motion_and_grid.snbt` (never hand-typed, never stripped). Coords on 0.5 grid, `d` suffix.

**CROSSING STATEMENT:** 0 crossings. Computed with a segment-intersection checker over all 14
internal dependency edges (excluding shared endpoints), plus a node-on-edge overlap check: both
returned 0. Main spine flows left-to-right in y∈[-1.5,0]; oxygen-loop stubs (6→7, 6→8) stay in a
single column gap; metallurgic_infuser is a vertical stub at x=0 (0,0)→(0,2); factory lane sits at
y≥3 flowing off energized_smelter. No dependency line crosses another.

**No KubeJS touched** → no `node --check` required.

## STATUS: DONE
