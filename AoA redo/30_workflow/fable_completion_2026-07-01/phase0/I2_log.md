# I2 log — seam wires + small fills (wave I2)

STATUS: DONE. All 5 sub-tasks landed. tier_audit 0 SOFTLOCK, ef_audit 0 dup / 0 dangling /
0 backward-age, all files pure CRLF + brace/bracket balanced, 0 new crossings.

Tooling note: the harness `Edit` tool refused multi-line matches on these CRLF `.snbt` files
(repeated "String to replace not found" on byte-identical context). Per CLAUDE.md §6, used
Desktop Commander `edit_block` as ground truth for every edit; it matched and preserved the
file's real tab depth + CRLF exactly (verified byte-for-byte below).

## File set (contract-scoped, disjoint from all other tasks)
- EDITED `config/ftbquests/quests/chapters/g4_the_infinite_grid.snbt` (sub-task 1)
- EDITED `config/ftbquests/quests/chapters/atomic_oritech_convergence.snbt` (sub-task 2)
- EDITED `config/ftbquests/quests/chapters/ir_immersive_engineering_early_factory.snbt` (sub-task 3)
- EDITED `config/ftbquests/quests/chapters/ir_create_industrial_addons.snbt` (sub-task 4)
- EDITED `config/ftbquests/quests/chapters/ir_automation_safety_and_routing.snbt` (sub-task 5)
- CREATED this log + `phase0/stubs/I2_stubs.txt` (3 new-node lang stubs; sub-tasks 4+5 only)
- Did NOT touch en_us.snbt, any KubeJS file, or any new-chapter file (T-02c-1/4 outputs read-only
  for capstone-id confirmation).

## Capstone ids confirmed on disk before wiring (from wave-I1 logs + grep)
- AE2 IR capstone quest `495410100000000E` = `ae2:pattern_encoding_terminal`
  (ir_digital_storage_foundations.snbt:607). NOTE: T-02c-1 re-tiered the AE2 capstone from the
  plan's `pattern_provider` (Gilded) to `pattern_encoding_terminal` (IR-legal). This matches my
  dispatch prompt's "pure ADD-DEP" revision of T-02c-9a.
- RS IR capstone quest `495410100000002A` = `refinedstorage:disk_interface`
  (ir_digital_storage_foundations.snbt:1102). Also a T-02c-1 re-tier (from Gilded `autocrafter`).
- Oritech IR capstone quest `4954121000000009` = `oritech:machine_core_3`
  (ir_oritech_foundry.snbt:353).
- IE mb_crusher pointer quest `2902E58DB70F9451` = `immersiveengineering:crusher`
  (metallurgy.snbt:1692) — the T-02b-3 pointer.

## Sub-task 1 — g4 seam (T-02c-9a, pure ADD-DEP, no deletions)
- g4 `4D4E011000000001` (`ae2:molecular_assembler`): deps `["4D4D011000000003"]`
  -> `["4D4D011000000003","495410100000000E"]`. Verified target quest exists.
- g4 `4D4E011000000006` (`refinedstorage:autocrafter`): deps `["4D4E011000000005"]`
  -> `["4D4E011000000005","495410100000002A"]`. Verified target quest exists.
- No g4 node deleted or retasked. Both added deps point to nodes in ANOTHER chapter
  (ir_digital_storage_foundations), so they are cross-chapter edges — they do NOT render as
  in-chapter dependency lines and add NO in-chapter edge. Confirmed: neither `495410100000000E`
  nor `495410100000002A` lives in g4.

## Sub-task 2 — Oritech seam (T-02c-9b)
- atomic_oritech_convergence root/entry `4F43010000010000` (`oritech:machine_processing_addon`,
  x0 y0, the in-chapter graph root, 8 children): deps `["4D53010000010003"]`
  -> `["4D53010000010003","4954121000000009"]`. Existing external chapter-entry dep kept
  (AND-combines). Added dep is cross-chapter (ir_oritech_foundry) -> no in-chapter edge.

## Sub-task 3 — IE continuity wire
- ir_immersive_engineering_early_factory root/entry `4954011000000001`
  (`immersiveengineering:craftingtable`, x0 y0): deps `["0B0310A0000000F0"]`
  -> `["0B0310A0000000F0","2902E58DB70F9451"]`. Gateway dep kept; metallurgy mb_crusher pointer
  added for foundation->fleet continuity. Cross-chapter (metallurgy) -> no in-chapter edge.
  (Precedent: this chapter already carries a metallurgy cross-chapter dep `2902E58DB70F9422` on
  node `4954011000000003`.)

## Sub-task 4 — IP gas_generator node (NEW node)
- Added node `4954071000000103` task `immersivepetroleum:gas_generator` ("Portable Generator").
- Dep: `["4954071000000003"]` (pumpjack) — same parent flarestack uses; the well extracts the
  gas the portable generator burns, so the rig->power beat reads. Coords x7.0 y-1.0
  (right of pumpjack, empty band). shape rsquare, xp25 + loot table 8430738502437568513L,
  hide_until_deps_visible, SkillsLevel/PlayerSpells copied byte-for-byte from the sibling
  flarestack node. Reward ids `4954073000103000/001`, task id `4954072000103000`.
- JAR RE-VERIFICATION (plan §E claimed this id "does not exist" — that claim is WRONG):
  `ImmersivePetroleum-1.21.1-4.4.1-37.jar` contains
  `block.immersivepetroleum.gas_generator` = "Portable Generator" (lang), plus
  blockstates/gas_generator.json, models/block+item, data/.../recipe/gas_generator.json,
  loot_table, advancement. Recipe = 8x `c:plates/iron` + `immersiveengineering:generator` (IR-
  locked 01d_immersive.js:36) + `immersiveengineering:capacitor_lv`, all IR-tier -> IR ceiling.
  It is ALSO explicitly AStages IR-locked at `aoa_astages_01_item_restrictions.js:675`
  (tier_audit row: OK, IR/IR). Fully IR-legal; my dispatch prompt was correct, the plan was not.
- Duplicate scan: `immersivepetroleum:gas_generator` = 0 other occurrences pack-wide before add.

## Sub-task 5 — EnderIO tanks pair (2 NEW nodes)
- Host chapter chosen by density grep: `ir_automation_safety_and_routing.snbt` (group IR
  `3F77A31B7D30C0AA`, 36 `enderio:` occurrences = the densest IR EnderIO lane). Extended the
  EnderIO machine cluster off the Vat (the fluid-processing machine).
- Added `49540A1000000039` `enderio:fluid_tank` (x7.5 y-8.0), dep `["49540A1000000028"]` (vat).
- Added `49540A100000003A` `enderio:pressurized_fluid_tank` (x9.0 y-8.0), dep
  `["49540A1000000039"]`. Dep-chained pair.
- Both nodes: shape rsquare, xp25 + loot 8430738502437568513L, hide_until_deps_visible,
  SkillsLevel/PlayerSpells copied byte-for-byte from the sibling vat node.
- JAR verify: `enderio-8.2.11-beta.jar` -> `block.enderio.fluid_tank` = "Fluid Tank",
  `block.enderio.pressurized_fluid_tank` = "Pressurized Fluid Tank"; both have item models +
  crafting recipes. AStages IR-locked at `aoa_astages_01l_tech_stragglers.js:39` and `:40`.
- Duplicate scan: both items = 0 occurrences pack-wide before add (both previously unquested).
- Fresh ids: highest existing `49540A1` quest suffix was `...038`; used `...039` + `...03A`
  (confirmed free pack-wide).

## Re-wires old->new
None. Sub-tasks 1-3 are pure ADD-DEP (existing deps preserved). No node deleted/retasked anywhere.

## Verification outputs

### tier_audit.py
Ran `python "AoA redo/30_workflow/fable_completion_2026-07-01/phase0/tier_audit.py"`.
Regenerated `A_tier_softlock_table.md`: **SOFTLOCK count = 0** pack-wide. My 3 new item nodes:
- `49540A1000000039` enderio:fluid_tank | IR/IR | **OK** | 01l_tech_stragglers.js:39
- `49540A100000003A` enderio:pressurized_fluid_tank | IR/IR | **OK** | 01l_tech_stragglers.js:40
- `4954071000000103` immersivepetroleum:gas_generator | IR/IR | **OK** | 01_item_restrictions.js:675

### ef_audit.py
Ran `python "AoA redo/30_workflow/fable_completion_2026-07-01/phase0/ef_audit.py"`.
- DUP ids: `{}` (0)
- DANGLING dep sources: 0 ; total dangling edges: 0  (all 4 seam deps + 3 new-node deps resolve)
- BACKWARD-age deps: 0
- ORPHANS: 1 = pre-existing `3400000000009000` (stone_water_weather_and_wounds), NOT mine.
- MISSING quest_desc: 62 (includes my 3 new nodes; prose is Opus's job via I2_stubs.txt).
- EM DASH: 3 (pre-existing; none in my nodes — my nodes carry no prose yet).

### Era check (preamble §3)
All 3 new task items are IR-tier (gas_generator = IE-component recipe ceiling + explicit IR lock;
both EnderIO tanks explicitly IR-locked). No Gilded/Atomic content introduced. The 4 seam deps
point INTO IR/metallurgy foundations (foundation-before-endgame direction), never later-tier.

### Byte discipline (per file, post-edit; Python byte count)
- g4_the_infinite_grid.snbt: CRLF 2663, bareLF 0, braces 519/519, brackets 244/244, 0 space-indent
- atomic_oritech_convergence.snbt: CRLF 1578, bareLF 0, braces 314/314, brackets 151/151, 0 space-indent
- ir_immersive_engineering_early_factory.snbt: CRLF 1855, bareLF 0, braces 317/317, brackets 166/166, 0 space-indent
- ir_create_industrial_addons.snbt: CRLF 2700, bareLF 0, braces 482/482, brackets 243/243, 0 space-indent
- ir_automation_safety_and_routing.snbt: CRLF 2109, bareLF 0, braces 382/382, brackets 191/191, 0 space-indent
Inserted nodes spot-checked with `cat -A`: tab-only indentation at correct depth, CRLF preserved.

### id uniqueness (anchored pack-wide)
`4954071000000103`, `49540A1000000039`, `49540A100000003A` each = 1 quest-id occurrence pack-wide.

### Crossing statement
- **g4 / atomic / IE (sub-tasks 1-3):** ADD-DEP only; every added dep targets a node in a
  DIFFERENT chapter, so it renders as a cross-chapter edge, not an in-chapter dependency line.
  ZERO new in-chapter edges -> ZERO new crossings in these three chapters.
- **ir_create_industrial_addons (sub-task 4):** segment-intersection computer over all resolvable
  in-chapter edges = 4 total crossings (identical to pre-edit baseline of 4); crossings involving
  my new node `4954071000000103` = **0**. gas_generator@(7.0,-1.0) off pumpjack was chosen
  specifically because 3 candidate placements off flarestack each ADDED a crossing (4->5/6);
  the pumpjack anchor adds none.
- **ir_automation_safety_and_routing (sub-task 5):** total crossings = 18 (identical to pre-edit
  baseline of 18); crossings involving my new nodes `49540A1000000039`/`...03A` = **0**. The tank
  pair sits in the empty x>=7 band at y-8.0, clear of the vat's existing edges.
- Net: my edits introduce 0 new crossings in any chapter. (Pre-existing baseline crossings in the
  two node-added chapters are unchanged and out of scope for this seam/fill wave.)

## Concerns
1. **Plan §E defect corrected (informational).** PLAN_02c section E asserts
   `immersivepetroleum:gas_generator` "DOES NOT EXIST in the IP jar" and DROPPED it. Direct jar
   inspection proves it DOES exist (block "Portable Generator", full recipe/model/loot/advancement)
   AND is explicitly AStages IR-locked (01_item_restrictions.js:675). My dispatch prompt's "jar-
   verified to exist" was correct; the plan's verification agent produced a false negative. Node
   authored as instructed. No downstream impact — it is a clean IR-legal leaf node.
2. All node prose is deferred to Opus via `phase0/stubs/I2_stubs.txt` (3 stubs). Sub-tasks 1-3
   touched no prose (pure structural dep adds on existing nodes).
