# T-02c-3 log — IE core multiblocks (EXTEND `ir_immersive_engineering_early_factory`)

Date: 2026-07-02. Owner lane: Fable (structure). File set: chapter above (+ this log +
`stubs/T-02c-3_stubs.txt`). No git run. Changes left in working tree.

## Key finding that reshaped the task (plan deviation, logged)

The plan's T-02c-3 node table proposed authoring blast furnace / crusher / mixer / silo as new
`mb_*` advancement nodes. A duplicate-task scan of the chapter proved these advancements are
**ALREADY TASKED here** (disguised behind item-icon nodes):

| existing node | icon | advancement task already present | coords |
|---|---|---|---|
| `4954011000000004` | ingot_steel | `immersiveengineering:main/mb_blastfurnace` | (5.5, 0.0) |
| `4954011000000007` | dust_iron | `immersiveengineering:multiblocks/mb_crusher` | (4.0, -2.5) |
| `495401100000000B` | concrete | `immersiveengineering:multiblocks/mb_mixer` | (7.0, -1.5) |
| `495401100000000F` | sheetmetal_iron | `immersiveengineering:multiblocks/mb_silo` | (4.0, -4.0) |
| `4954011000000003` | coal_coke | `immersiveengineering:main/mb_cokeoven` | (2.0, 2.5) |
| `4954011000000009` | plate_iron | `immersiveengineering:multiblocks/mb_metalpress` | (5.5, -1.5) |
| `4954011000000030` | refinery | `immersiveengineering:multiblocks/mb_refinery` | (14.0, 0.0) |
| `4954011000000031` | fermenter | `immersiveengineering:multiblocks/mb_fermenter` | (8.5, -8.5) |

Re-authoring those four advancements would create duplicate advancement tasks (defect;
contract rule 8 + preamble §6 "no duplicate quests"). Therefore only the genuinely-NEW content
was authored, preserving the plan's dependency INTENT by rooting each new node on the existing
equivalent node instead of a re-created one. `mb_silo`/`mb_metalpress` needed no new companion.

## Nodes created (6)

All in chapter `4954010000000000` (group `3F77A31B7D30C0AA`, industrial_revolution). Task shape
copied byte-exact from siblings: advancement nodes from the refinery node `4954011000000030`
(xp:25 + loot table `8430738502437568513L`); item nodes from the root node `4954011000000001`.
`PlayerSpells`/`SkillsLevel` blocks copied verbatim, not hand-typed or stripped. Both
`hide_until_deps_complete: true` and `hide_until_deps_visible: true` set (matches root node).

| new node id | task | type | parent (dep) | x | y |
|---|---|---|---|---|---|
| 4954011000000102 | adv `immersiveengineering:multiblocks/mb_improvedblastfurnace` | advancement | 4954011000000004 (existing Crude Blast Furnace) | 4.5 | 4.0 |
| 4954011000000104 | item `immersiveengineering:alloy_smelter` | item | 4954011000000102 | 3.0 | 5.5 |
| 4954011000000106 | adv `immersiveengineering:multiblocks/mb_squeezer` | advancement | 4954011000000007 (existing Crusher) | 2.5 | -4.0 |
| 4954011000000107 | item `immersiveengineering:bottling_machine` | item | 4954011000000106 | 1.0 | -5.0 |
| 4954011000000108 | item `immersiveengineering:sawmill` | item | 495401100000000B (existing Mixer) | 6.0 | -3.5 |
| 4954011000000109 | item `immersiveengineering:auto_workbench` | item | 4954011000000108 | 6.0 | -5.0 |

Icons: adv nodes use the formed-block item (`advanced_blast_furnace` for improved BF; `squeezer`);
item nodes use their task item. Reward ids: `4954013000010N00`/`...01` per node (all proven free).
Task ids: `495401200000010N`. No old->new re-wires needed (pure additive leaves off existing nodes).

## F.4 adjudication honored

The Improved Blast Furnace node (`4954011000000102`) roots on the existing IR blast-furnace node
`4954011000000004` (which itself roots on the IR crafting-table root `4954011000000001` + external
`2902E58DB70F9422`). It carries NO dependency on the Medieval coke node `4954011000000003`
(`mb_cokeoven`). Metallurgy/coke is handled separately, as F.4 requires. Prose brief instructs Opus
to reference coke as an input in the Crude Blast Furnace prose, not to add a coke dependency edge.

## Verification (contract §Verification)

- **Item/advancement id proofs (jar `ImmersiveEngineering-1.21.1-12.4.2-194.jar`):**
  - `multiblocks/mb_improvedblastfurnace` -> `data/immersiveengineering/advancement/multiblocks/mb_improvedblastfurnace.json` PRESENT
  - `multiblocks/mb_squeezer` -> `data/immersiveengineering/advancement/multiblocks/mb_squeezer.json` PRESENT
  - `alloy_smelter`, `bottling_machine`, `sawmill`, `auto_workbench`, `advanced_blast_furnace` (icon)
    -> block models + `block.immersiveengineering.*` lang keys all PRESENT.
- **Legality (AStages, gating CLOSED - cited, not edited):** tier_audit rows show all four item
  nodes OK @ industrial_revolution: alloy_smelter `aoa_astages_01d_immersive.js:34`,
  bottling_machine `01d:35`, sawmill `aoa_astages_01_item_restrictions.js:764`, auto_workbench
  `...765`. IE family floor = industrial_revolution (chapter age).
- **tier_audit.py:** `=== SOFTLOCK + ILLEGAL rows ===` EMPTY. `A_tier_softlock_table.md` grep for
  SOFTLOCK/ILLEGAL = 0. My 4 item nodes listed **OK**.
- **ef_audit.py:** DUP ids `{}` (0); DANGLING 0; total dangling edges 0; BACKWARD-age deps 0;
  ORPHANS 1 (pre-existing `3400000000009000` in `stone_water_weather_and_wounds`, not mine — all
  my nodes have >=1 dep, no rootless leak); EM/EN dash 0.
- **Byte discipline:** file was pure CRLF (1580 CRLF / 0 bare LF before); after edit 1852 CRLF /
  0 bare LF. Tabs preserved. Brace balance {}=0, bracket balance []=0.
- **Id-dup scan (anchored `^\s+id: "…16hex"` across all chapters):** none of the 24 new
  node/task/reward ids collide pack-wide.
- **Duplicate item-task scan (whole chapters dir):** `alloy_smelter`/`bottling_machine`/`sawmill`/
  `auto_workbench` tasked nowhere else. `advanced_blast_furnace` used only as an ICON here (item
  task exists in g5_empire_of_iron `1490` - no collision, different task types).
- **node --check:** N/A (no KubeJS file touched).

## Crossing statement

ZERO crossings introduced by this task. Computed with a segment-intersection test over the full
current 41-node / 45-edge graph:
- WITH the 6 new nodes: 10 total geometric crossings.
- WITHOUT the 6 new nodes (pre-edit graph): 10 total geometric crossings — identical.
- Crossings involving any new node (0102/0104/0106/0107/0108/0109): **0**.

The 10 straight-line crossings are entirely PRE-EXISTING among old dense-chapter edges
(e.g. `4954011000000030`->`495401100000000B`, `4954011000000012`->`4954011000000006`,
`495401100000001B`->`4954011000000019`). They predate T-02c-3, are outside this task's file-set
mandate to re-lay, and FTBQ renders them fine. FLAG for CC: the chapter carries pre-existing
straight-line dependency crossings if a future layout pass wants them cleaned. My additions kept
each new edge short and in confirmed-empty local space (BF pair in the empty top-left strip
x[-3,6.5] y[3.5,7]; squeezer/bottling in empty y<0 left space; sawmill/auto_workbench in empty
space beside the mixer), each edge geometrically clean.

## Before/after counts

`ir_immersive_engineering_early_factory.snbt`: 35 nodes -> 41 nodes (+6). 1580 -> 1852 lines.
