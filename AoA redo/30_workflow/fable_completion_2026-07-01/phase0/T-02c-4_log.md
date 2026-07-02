# T-02c-4 log — `ir_oritech_foundry` (NEW chapter) + Extended Crafting lane

Owner: Fable (structure). Date: 2026-07-02. STATUS: DONE_WITH_CONCERNS (2 dedup deviations, both resolved in-file; see Concerns).

## File set (contract-disjoint)
- CREATED `config/ftbquests/quests/chapters/ir_oritech_foundry.snbt` (new chapter).
- CREATED `AoA redo/30_workflow/fable_completion_2026-07-01/phase0/stubs/T-02c-4_stubs.txt` (lang stubs).
- This log.
- NOTHING else touched. Did NOT touch `atomic_oritech_convergence.snbt` (that is T-02c-9b). Did NOT touch `en_us.snbt`.

## Chapter shell
- filename `ir_oritech_foundry`; chapter id `4954120000000000`; group `3F77A31B7D30C0AA` (industrial_revolution); order_index `9` (existing IR chapters run 0..8); icon `oritech:foundry_block`; `hide_quest_until_deps_complete: true`. Modeled byte-for-byte on sibling `ir_immersive_engineering_early_factory.snbt` header.

## Nodes created (14)
Oritech spine (root -> capstone):
- `4954121000000001` machine_core_1 (ROOT; dep `0B0310A0000000F0` = Renaissance->IR gateway; `hide_until_deps_complete`+`hide_until_deps_visible`, item task) x0 y0
- `4954121000000002` basic_generator_block (dep 0001) x2 y1 — **check_quest -> 4954051000000007** (dedup, see Concerns)
- `4954121000000003` pulverizer_block (dep 0001, item) x2 y-1
- `4954121000000004` powered_furnace_block (dep 0003, item) x4 y-1
- `4954121000000005` machine_core_2 (dep 0004, item) x4 y0.5
- `4954121000000006` foundry_block (dep 0005) x6 y-1 — **check_quest -> 49540B1000000005** (dedup, see Concerns)
- `4954121000000007` refinery_block (dep 0005, item) x6 y1
- `4954121000000008` machine_frame_block (deps 0006+0007 converge, item) x8 y0
- `4954121000000009` machine_core_3 (dep 0008, item, CAPSTONE, loot 515, xp 75) x10 y0
- `495412100000000A` small_storage_block (dep 0002, item, `optional:true`) x2 y2.5
- `495412100000000B` steam_engine_block (dep 0002, item, `optional:true`) x0.5 y2
Extended Crafting lane (standalone, entry off machine_core_2):
- `4954121000000020` extendedcrafting:frame (dep 0005, item) x6 y3
- `4954121000000021` extendedcrafting:basic_table (dep 0020, item) x8 y3
- `4954121000000022` extendedcrafting:handheld_table (dep 0021, item) x10 y3

All non-root nodes carry `hide_until_deps_complete: true`. Inert `PlayerSpells`/`SkillsLevel` blocks copied byte-for-byte from the IE sibling root node onto every item-task node (check_quest nodes follow the pack check_quest shape from `ir_power_motion_and_grid.snbt:480-486`, which carries no Skills block).

## Re-wires (old->new)
- None in this file set. The Atomic convergence re-wire (add dep on capstone `4954121000000009`) is T-02c-9b's job on `atomic_oritech_convergence.snbt` — NOT touched here, per contract.

## Verification outputs

### tier_audit.py
Ran `python "AoA redo/30_workflow/fable_completion_2026-07-01/phase0/tier_audit.py"`. All 12 `ir_oritech_foundry` item rows = **OK** (IR item locked at IR):
- machine_core_1 (01_item_restrictions.js:366), machine_core_2 (01e:37), machine_core_3 (01e:38), pulverizer_block (01e:39), powered_furnace_block (01e:40), refinery_block (01e:48), machine_frame_block (01_item:365), small_storage_block (01e:46), steam_engine_block (01e:54), extendedcrafting:frame (01n:148), basic_table (01n:145), handheld_table (01n:147).
- ZERO SOFTLOCK / ILLEGAL rows for this chapter (`grep ir_oritech_foundry A_tier_softlock_table.md | grep SOFTLOCK|ILLEGAL` = NONE).
- The 2 SOFTLOCK rows in the audit summary belong to `ir_digital_storage_foundations` (T-02c-1), not this task.
- (check_quest nodes 0002/0006 carry no item task, so tier_audit correctly evaluates nothing for them; the underlying items basic_generator_block/foundry_block are IR-locked per plan §E.)

### ef_audit.py
Ran `python "...phase0/ef_audit.py"`: DUP ids `{}`; BACKWARD-age deps `0`. Global dangling (1) + orphan (1) are PRE-EXISTING and unrelated (`4D4E0120002400A1`->`5054012000060001`; orphan `3400000000009000` in stone_water). Confirmed no `495412` id appears in dangling/orphan set. This chapter contributes 0 dup / 0 dangling / 0 orphan / 0 backward-age.

### Era check (preamble §3)
No Gilded/Atomic Oritech content present. `machine_core_4`, `assembler`, `atomic_forge`, core_5-7, duratium = ABSENT. Extended Crafting advanced/ender/elite/ultimate = ABSENT (only basic_table/frame/handheld_table, all IR). Clean.

### Byte discipline
`python` byte count on the new file: 11583 bytes, **crlf 613, lone_lf 0** (pure CRLF, matches sibling). Tabs preserved. Braces `{`108 = `}`108; brackets `[`58 = `]`58 (balanced). 14 quest node ids parsed.

### id uniqueness (anchored, Python `^\t+id: "<16hex>"`)
All 14 quest ids unique across all 60 chapter files; chapter id `4954120000000000` count = 1; no `495412*` id (quest/task/reward) appears more than once.

### Duplicate-item scan (pack-wide, post-write)
Each of my 12 item-task items resolves ONLY to `ir_oritech_foundry.snbt`. The two items that were already tasked elsewhere (`oritech:basic_generator_block` @ `ir_power_motion_and_grid`, `oritech:foundry_block` @ `ir_magic_feedstock_and_spectrum_network`) are present in my file ONLY as node icons (no `item:` task) plus one check_quest target each. No duplicate item task introduced.

### Crossing statement
Ran a segment-intersection computer over all 14 in-chapter dependency edges: **0 crossings**. Oritech spine occupies y in [-1, 1] flowing left-to-right (x0->x10); optional stubs at y2/y2.5 hang off basic_generator; Extended Crafting lane at y3 (x6->x10) enters via a single edge from machine_core_2 (x4,y0.5 -> x6,y3) that runs through empty space (no node between). External root dep (`0B0310A0000000F0`) lives in another chapter and is excluded from in-chapter crossing (standard). CROSSING-FREE (hard constraint satisfied).

## Concerns (for CC / Opus)
1. **DEDUP DEVIATION (2 nodes converted to check_quest).** The plan §C T-02c-4 table specifies `oritech:basic_generator_block` and `oritech:foundry_block` as item tasks. Both items are ALREADY tasked in other IR chapters (`4954051000000007` in ir_power_motion_and_grid; `49540B1000000005` in ir_magic_feedstock_and_spectrum_network). Contract rule 8 forbids duplicate item tasks pack-wide. My file set does not permit editing those other chapters to re-point them here, so I resolved in-file by making my two spine nodes `check_quest` tasks targeting the existing owner quests (established pack pattern, cf. `ir_power_motion_and_grid.snbt:480`). Icons remain the machine blocks. Effect: the foundry spine node (load-bearing: core_2 -> foundry+refinery -> frame -> core_3 capstone) completes when the player completes the existing Foundry quest; basic_generator (side branch feeding only optional nodes) likewise. Spine integrity + reachability preserved; no item re-tasked. **CC: confirm check_quest dedup is the preferred resolution vs. a cross-task re-point of the other chapters' nodes onto this new foundation (which would need those files in scope).**
2. **machine_core_1 legality note.** Plan §A4/§E says machine_core_1 is the UNLOCKED free-entry tier. tier_audit maps it to the oritech family floor and reports it OK at industrial_revolution/industrial_revolution (still legal at IR). No action needed; flagged for transparency.
3. **Optional depth.** Added exactly the two optional nodes the plan authorized (small_storage_block, steam_engine_block), both `optional:true`, no padding. `machine_plating_block` NOT tasked (bare material, referenced in foundry prose brief). `material_black_iron` NOT tasked (bare ingot, referenced in frame prose brief).
4. **Re-wire seam ready.** Capstone `4954121000000009` (machine_core_3) is the id T-02c-9b must add as a dep on `atomic_oritech_convergence` root `4F43010000010000`.
