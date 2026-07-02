# PLAN 02c — Industrial Revolution Foundations + Completion

**Role:** structural DESIGN only. This document is implementation-ready for dispatch to
implementer (Fable) agents. It authorizes NO edits by itself. Owner chain per age:
Fable (structure) -> Opus (prose) -> CC (age-discipline + merge). Prepend
`01_MASTER_PREAMBLE.md` to every implementer prompt.

**Scope authority:** `AOA_QUEST_SCOPE_REGISTRY.md` wins over everything. Gating is CLOSED
(Policy 1): this plan proposes ZERO new AStages gates. Every mod named here is ALREADY
IR-gated; the exact live lock line is cited per mod so implementers can confirm legality
without touching `aoa_astages_*.js`.

**Verification status:** every item/block/advancement id in this plan was jar-verified on
2026-07-02 (four verification agents; corrections folded in). The per-id proof path is in
the VERIFICATION LOG (section E). IDs that could not be verified were DROPPED, not invented
(notably `immersivepetroleum:gas_generator`, which does not exist in the jar).

---

## A. Design decisions (2-3 approaches weighed, one chosen)

### A1. AE2 + RS foundations -> ONE new IR chapter `ir_digital_storage_foundations` (CONFIRM default a)
- **Options.** (1) Pool AE2+RS into one new IR chapter, two crossing-free lanes. (2) Two
  separate new chapters. (3) Retro-fit the foundation rungs into g4 (Gilded).
- **Chosen: (1).** g4 `the_infinite_grid` is group `5E42E6B4A7C91D30` = **Gilded**, and its AE2
  content opens on `ae2:molecular_assembler` (`4D4E011000000001`) — a mid-network device, not a
  controller. AE2 and RS are both IR-gated (`aoa_astages_01i_ae2.js:34`,
  `aoa_astages_01j_storage.js:31`). The foundation therefore belongs at IR, before g4. One
  chapter with two parallel lanes (AE2 top, RS bottom) keeps them visually pooled, avoids two
  near-empty tabs, and gives a single clean re-wire seam into g4. Option 3 rejected: it would
  place IR-tier onboarding inside a Gilded tab (age-tab inversion, hides the foundation behind
  the Gilded gate — the exact defect this pass fixes).

### A2. Mekanism IR ore-processing spine -> NEW chapter `ir_mekanism_ore_works` (CONFIRM default b)
- **Options.** (1) New dedicated chapter. (2) Fold into `ir_modern_industrialization_steam_industry`.
  (3) Fold into `ir_power_motion_and_grid`.
- **Chosen: (1).** Mekanism's 5-stage factory chain + evaporation + factory tier is a signature
  multi-node system; it deserves its own home and resolves ledger row 11 (Mekanism has no IR
  chapter). Folding into MI or power/grid would bury it under an unrelated mod's spine and force
  crossings. All ids IR-locked in `aoa_astages_01_item_restrictions.js:287-328`.

### A3. IE multiblocks -> EXTEND existing `ir_immersive_engineering_early_factory` (CONFIRM default c)
- **Options.** (1) Extend the existing IE chapter. (2) New IE-multiblock chapter.
- **Chosen: (1).** The chapter already exists (id `4954010000000000`, group IR) and already uses
  `mb_*` advancement tasks (e.g. it neighbours the IP oil chain's `immersivepetroleum:main/mb_derrick`
  pattern). IE multiblocks have NO craftable item — the formed structure returns a block item but
  formation is best tracked via the `immersiveengineering:multiblocks/mb_*` advancements (precedent
  in-pack). A second IE chapter would split the mod pointlessly. Free space exists (see D3 sketch).

### A4. Oritech -> NEW chapter `ir_oritech_foundry` (per 02c, default d)
- No IR Oritech home exists (backlog confirmed). All IR-tier machine blocks are locked at IR in
  `aoa_astages_01e_oritech.js:37-63`. `machine_core_1` ("Primitive Machine Core") is the ONLY core
  NOT locked — it is the free entry tier; `machine_core_2/3` are IR-locked, `_4` Gilded. **Critical
  Oritech fact** (from that file's header comment, lines 3-5): *Oritech machines do NOT craft from
  machine_core; each machine uses explicit intermediates.* The chapter therefore teaches the machine
  BLOCKS directly (pulverizer/powered_furnace/foundry/refinery) with cores as progression markers,
  not as literal build prereqs.

### A5. P2 list -> hosted in existing IR chapters by theme (default e), with drops
- **extendedcrafting basic_table** -> new `ir_oritech_foundry` is wrong theme; host in the
  existing `ir_modern_industrialization_steam_industry`? No — extendedcrafting is a standalone
  crafting-tier tree. **Chosen host: a small 3-node lane appended to `ir_mekanism_ore_works`** (T2's
  new chapter) is also wrong theme. Cleaner: give extendedcrafting its own 3-node lane inside the
  new `ir_digital_storage_foundations` chapter is off-theme too. **Final: append the 3-node
  extendedcrafting lane to `ir_oritech_foundry`** (both are "bench/machine fabrication" theme, both
  new, keeps the edit in one new file). basic_table + prereqs IR-locked
  (`aoa_astages_01n_ascension.js:145-149`).
- **cabletiers elite (5 ids)** -> host in `ir_digital_storage_foundations` RS lane (they ARE RS
  devices; elite tier IR-locked `aoa_astages_01j_storage.js:57-61`).
- **immersivepetroleum seismic_survey + flarestack** -> host in existing
  `ir_create_industrial_addons` (id `4954070000000000`), sequenced off the existing
  `immersivepetroleum:projector` node (`4954071000000001`) so the CDG-diesel -> IP handoff is
  visible. **`gas_generator` DROPPED — it does not exist in the IP jar** (verification agent
  confirmed no such id; IP has no fuel-burning generator, that role is IE's diesel generator).
  Both surviving ids IR-locked (`aoa_astages_01d_immersive.js:61,63`).
- **neovitae IR segment** -> host in existing `ir_magic_feedstock_and_spectrum_network`
  (id `49540B0000000000`). All ids IR-locked (`aoa_astages_01m_magic.js:128-138`).
- **electrodynamics base mineralgrinder line** -> host in existing `ir_power_motion_and_grid`
  (id `4954050000000000`), beside the existing electrodynamics "triple" cluster. Base
  `mineralgrinder`/`electricfurnace` IR-locked (`aoa_astages_01k_nuclear_power.js:106`).
- **psi** -> NOT authored. Registry Policy 3 = optional-only; 02c says "only after the scope call".
  No scope call has been made, so psi is OUT of this plan.

### A6. Ledger row 8 — Deeper & Darker IR gear tail MOVE (Neo Vitae precedent)
- Move `warden_upgrade_smithing_template` (`0B0310600000008F`) + `resonarium_upgrade_smithing_template`
  (`0B0310600000008D`) + the DUPLICATE `sonorous_staff` node (`0B03106000000091`) out of
  `ren_deeper_darker_otherside` and into `ir_netherite_citadel_obsidilith` (host per row 8).
- **`warden_carapace` (`0B0310600000008E`) STAYS in Ren.** Extraction proved it depends on
  `reinforced_echo_shard` (`0B03106000000033`), which is a LOAD-BEARING hub in the Ren chapter
  (3 dependents incl. the resonarium sub-tree). Moving carapace would either orphan the template
  or force a cross-chapter dependency on a Renaissance node. **Deviation from the prompt's "8E" —
  see section F.** The two smithing templates and the duplicate staff are pure leaves; they move
  cleanly. The FIRST `sonorous_staff` (`0B03106000000045`) stays in Ren (it is gated behind an
  external Ren node `0B031070000000A9`); only the redundant duplicate `0B03106000000091` moves,
  which also de-dupes the pack.

---

## B. Task list (dispatchable, STRICTLY DISJOINT file sets)

Each task = one implementer agent. File sets do not overlap, so T-02c-1..8 can run in parallel.
Lang stubs for every task go to its own sidecar `phase0/stubs/<task-id>_stubs.txt` (one
`quest.<id>.key: value` line each) — NEVER to `en_us.snbt` (Opus owns that later).

| Task | Deliverable | Files touched (disjoint) |
|---|---|---|
| **T-02c-1** | AE2+RS+cabletiers foundation — NEW chapter `ir_digital_storage_foundations` | `config/ftbquests/quests/chapters/ir_digital_storage_foundations.snbt` (new); `phase0/stubs/T-02c-1_stubs.txt` |
| **T-02c-2** | Mekanism ore-works — NEW chapter `ir_mekanism_ore_works` | `config/ftbquests/quests/chapters/ir_mekanism_ore_works.snbt` (new); `phase0/stubs/T-02c-2_stubs.txt` |
| **T-02c-3** | IE core multiblocks — EXTEND `ir_immersive_engineering_early_factory` | `config/ftbquests/quests/chapters/ir_immersive_engineering_early_factory.snbt`; `phase0/stubs/T-02c-3_stubs.txt` |
| **T-02c-4** | Oritech foundry + extendedcrafting lane — NEW chapter `ir_oritech_foundry` | `config/ftbquests/quests/chapters/ir_oritech_foundry.snbt` (new); `phase0/stubs/T-02c-4_stubs.txt` |
| **T-02c-5** | IP seismic/flarestack — EXTEND `ir_create_industrial_addons` | `config/ftbquests/quests/chapters/ir_create_industrial_addons.snbt`; `phase0/stubs/T-02c-5_stubs.txt` |
| **T-02c-6** | Neo Vitae IR segment — EXTEND `ir_magic_feedstock_and_spectrum_network` | `config/ftbquests/quests/chapters/ir_magic_feedstock_and_spectrum_network.snbt`; `phase0/stubs/T-02c-6_stubs.txt` |
| **T-02c-7** | Electrodynamics base grinder line — EXTEND `ir_power_motion_and_grid` | `config/ftbquests/quests/chapters/ir_power_motion_and_grid.snbt`; `phase0/stubs/T-02c-7_stubs.txt` |
| **T-02c-8** | Deeper&Darker gear-tail MOVE — EXTEND `ir_netherite_citadel_obsidilith` + edit `ren_deeper_darker_otherside` | `config/ftbquests/quests/chapters/ir_netherite_citadel_obsidilith.snbt` + `config/ftbquests/quests/chapters/ren_deeper_darker_otherside.snbt`; `phase0/stubs/T-02c-8_stubs.txt` |

**Re-wire seams (RUN AFTER the foundation tasks that own the source chapter — these edit the
ENDGAME chapters, so they are grouped as a serialized follow-up wave `T-02c-9` to keep file sets
disjoint from the foundation authors):**

| Task | Deliverable | Files touched (disjoint from T1-8) |
|---|---|---|
| **T-02c-9a** | Re-wire g4 AE2/RS nodes onto the new IR foundation capstone | `config/ftbquests/quests/chapters/g4_the_infinite_grid.snbt` |
| **T-02c-9b** | Re-wire atomic Oritech convergence root onto the new IR Oritech capstone | `config/ftbquests/quests/chapters/atomic_oritech_convergence.snbt` |

> **Parallelism rule.** T-02c-1..8 are mutually disjoint and parallel-safe. T-02c-9a depends on
> T-02c-1 (needs the new AE2/RS capstone id). T-02c-9b depends on T-02c-4 (needs the new Oritech
> capstone id). 9a/9b touch g4 and atomic_oritech_convergence respectively — neither is touched by
> any T1-8 — so 9a and 9b are parallel with each other and with any still-running T1-8 EXCEPT their
> own upstream. Dispatch order: wave 1 = T1..T8; wave 2 = T9a (after T1), T9b (after T4).

**ID-block convention (avoid collisions).** New chapters get a fresh chapter id and all nodes use
that prefix. Assigned chapter ids (all outside existing prefixes — implementer must `grep` to
confirm unused before writing):
- `ir_digital_storage_foundations` chapter id `4954100000000000`; nodes `495410 1 000000NN`.
- `ir_mekanism_ore_works` chapter id `4954110000000000`; nodes `495411 1 000000NN`.
- `ir_oritech_foundry` chapter id `4954120000000000`; nodes `495412 1 000000NN`.
Appended nodes in existing chapters continue that chapter's own id scheme with fresh unused
suffixes (see per-task tables). **All chapter `group:` = `3F77A31B7D30C0AA` (industrial_revolution)
for the three new chapters.** Set `order_index` after the existing IR chapters (they run 0..8;
use 9/10/11).

---

## C. Per-task node + re-wire tables

Legend: task type `item` unless noted. Icon = the task item unless noted. Every new node carries
`hide_until_deps_complete: true` + the inert `SkillsLevel`/`PlayerSpells` blocks copied byte-for-byte
from a sibling node in the same chapter (do NOT hand-type them; do NOT strip them). Coords on 0.5 grid.

### T-02c-1 — `ir_digital_storage_foundations` (NEW). Two crossing-free lanes.

**Lane AE2 (top band, y = 0 .. +3). Left-to-right dependency flow.**

| node id | item id | teaching purpose (Opus brief) | x | y | deps |
|---|---|---|---|---|---|
| 4954101000000001 | `ae2:controller` | The network core: every ME device talks to a controller; power in, channels out. | 0.0 | 0.0 | [] (chapter root A) |
| 4954101000000002 | `ae2:energy_acceptor` | Convert FE/other power into AE energy the network can store. | 2.5 | 0.0 | ["4954101000000001"] |
| 4954101000000003 | `ae2:energy_cell` | Buffer AE energy so the grid rides through demand spikes. | 4.0 | 1.0 | ["4954101000000002"] |
| 4954101000000004 | `ae2:drive` | The disk bay: houses storage cells so items live in the grid. | 5.5 | 0.0 | ["4954101000000002"] |
| 4954101000000005 | `ae2:item_storage_cell_1k` | First storage cell. 1k holds bulk items; format it in a cell workbench. | 7.0 | 1.0 | ["4954101000000004"] |
| 4954101000000006 | `ae2:cell_workbench` | Pre-partition cells so a cell only accepts the items you assign. | 8.5 | 1.0 | ["4954101000000005"] |
| 4954101000000007 | `ae2:chest` | Single-cell access without a full drive; the cheapest way to read a cell. | 7.0 | -1.0 | ["4954101000000004"] |
| 4954101000000008 | `ae2:io_port` | Bulk import/export between cells and inventories in one action. | 10.0 | 0.0 | ["4954101000000006"] |
| 4954101000000009 | `ae2:terminal` | The window into the grid: view and pull stored items. | 11.5 | 1.0 | ["4954101000000008"] |
| 495410100000000A | `ae2:crafting_terminal` | A terminal with a crafting grid so you craft straight from network stock. | 13.0 | 1.0 | ["4954101000000009"] |
| 495410100000000B | `ae2:crafting_unit` | The blank block of a crafting CPU; combine with storage + accelerators. | 13.0 | -0.5 | ["495410100000000A"] |
| 495410100000000C | `ae2:1k_crafting_storage` | Crafting CPU memory: how many parallel autocraft jobs the CPU can hold. | 14.5 | -0.5 | ["495410100000000B"] |
| 495410100000000D | `ae2:crafting_accelerator` | Speeds a crafting CPU; more accelerators = faster autocraft. | 14.5 | 0.5 | ["495410100000000B"] |
| 495410100000000E | `ae2:pattern_encoding_terminal` | Encode crafting patterns; the recipe list an autocraft CPU follows. | 16.0 | 0.0 | ["495410100000000C","495410100000000D"] | 
| **495410100000000F** | `ae2:pattern_provider` | **AE2 lane capstone.** Feed encoded patterns to assemblers to run first autocraft. | 17.5 | 0.0 | ["495410100000000E"] |

**Lane RS (bottom band, y = -4 .. -7). Left-to-right.**

| node id | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 4954101000000020 | `refinedstorage:controller` | RS network core: supplies energy and identity to every connected device. | 0.0 | -4.0 | [] (chapter root B) |
| 4954101000000021 | `refinedstorage:cable` | Wire the network; devices only work when cabled to the controller. | 2.0 | -4.0 | ["4954101000000020"] |
| 4954101000000022 | `refinedstorage:disk_drive` | Holds storage disks; the grid's item capacity lives here. | 4.0 | -4.0 | ["4954101000000021"] |
| 4954101000000023 | `refinedstorage:1k_storage_disk` | First RS disk. Bulk item storage, no pre-format needed. | 5.5 | -3.0 | ["4954101000000022"] |
| 4954101000000024 | `refinedstorage:grid` | The RS access window: search, sort, extract stored items. | 7.0 | -4.0 | ["4954101000000022"] |
| 4954101000000025 | `refinedstorage:crafting_grid` | A grid that crafts from network stock and remembers recipes. | 8.5 | -3.0 | ["4954101000000024"] |
| 4954101000000026 | `refinedstorage:detector` | Emit redstone on stock thresholds; the trigger for auto-restock. | 8.5 | -5.0 | ["4954101000000024"] |
| 4954101000000027 | `refinedstorage:storage_monitor` | Wall display of one item's count; instant stock-at-a-glance. | 10.0 | -5.0 | ["4954101000000024"] |
| 4954101000000028 | `refinedstorage:security_manager` | Lock the network per player: who may insert, extract, autocraft. | 11.5 | -5.0 | ["4954101000000024"] |
| 4954101000000029 | `refinedstorage:portable_grid` | Handheld access to a disk in the field, off-network. | 10.0 | -3.0 | ["4954101000000025"] |
| **495410100000002A** | `refinedstorage:autocrafter` | **RS lane capstone.** Autocrafting: encode patterns and let the network build. | 13.0 | -4.0 | ["4954101000000025"] |

**Lane cabletiers (elite RS devices, tucked below RS lane, y = -7 .. -8; deps into RS capstone).**

| node id | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 4954101000000030 | `cabletiers:elite_importer` | Higher-throughput RS import than the base importer; one cable, many stacks/tick. | 13.0 | -6.5 | ["495410100000002A"] |
| 4954101000000031 | `cabletiers:elite_exporter` | Elite export cable: push stacks into machines at speed. | 14.5 | -6.5 | ["4954101000000030"] |
| 4954101000000032 | `cabletiers:elite_constructor` | Elite constructor: place blocks from the network fast. | 14.5 | -7.5 | ["4954101000000030"] |
| 4954101000000033 | `cabletiers:elite_destructor` | Elite destructor: break + ingest blocks into the network fast. | 16.0 | -6.5 | ["4954101000000030"] |
| 4954101000000034 | `cabletiers:elite_disk_interface` | Elite disk interface: bulk disk-to-network transfer. | 16.0 | -7.5 | ["4954101000000030"] |

- Icons: all task items. Chapter icon: `ae2:controller`.
- **Crossing statement.** AE2 lane occupies y>=-0.5, RS lane y<=-3, cabletiers y<=-6.5; the three
  bands never share a row and each lane flows strictly left-to-right from its own root, so no
  dependency line crosses. Two roots (AE2 controller, RS controller) are both at x0 in separate
  bands. VERIFY with the crossing computer at author time.

**RE-WIRE (owned by T-02c-9a, edits `g4_the_infinite_grid.snbt`):**

| existing g4 node | current deps | ADD dep on | rationale |
|---|---|---|---|
| `4D4E011000000001` (`ae2:molecular_assembler`) | ["4D4D011000000003"] | **495410100000000F** (AE2 capstone) | Molecular assembler is post-pattern-provider; a player must have built the network first. |
| `4D4E011000000006` (`refinedstorage:autocrafter`) — NOTE this DUPLICATES the new RS capstone item | ["4D4E011000000005"] | see F | This g4 node tasks the SAME item as new RS capstone `495410100000002A`. Dedup: convert the g4 node to a `check_quest` on `495410100000002A`, OR delete it and point its child (`4D4E01100000000A` megacells) at the new capstone. Decision in F. |
| `4D4E011000000108` (`ae2:pattern_provider`) — DUPLICATES new AE2 capstone item | ["4D4E011000000001"] | see F | Same item as `495410100000000F`. Dedup per F. |

### T-02c-2 — `ir_mekanism_ore_works` (NEW). Single main spine + factory-tier side lane.

**Main spine (the 5-stage doubling chain, left-to-right, y=0):**

| node id | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 4954111000000001 | `mekanism:enrichment_chamber` | Stage-1 ore doubling: dust from ore. Mekanism's entry processing machine. | 0.0 | 0.0 | [] (root) |
| 4954111000000002 | `mekanism:crusher` | Turns ingots back to dust; pairs with enrichment for the 2x tier. | 2.0 | 0.0 | ["4954111000000001"] |
| 4954111000000003 | `mekanism:energized_smelter` | Powered smelting; the electric furnace of the Mek line. | 3.5 | 1.0 | ["4954111000000002"] |
| 4954111000000004 | `mekanism:osmium_compressor` | Compress osmium onto dust for enriched alloys; 3x-tier feeder. | 3.5 | -1.0 | ["4954111000000002"] |
| 4954111000000005 | `mekanism:purification_chamber` | Stage-3 (gas): ore -> clumps with oxygen. Needs the oxygen loop. | 5.5 | 0.0 | ["4954111000000004"] |
| 4954111000000006 | `mekanism:electrolytic_separator` | Split water into hydrogen + oxygen; the gas supply for purification/injection. | 5.5 | -1.5 | ["4954111000000004"] |
| 4954111000000007 | `mekanism:chemical_injection_chamber` | Stage-4: ore -> shards with hydrogen chloride. The 4x tier. | 7.5 | 0.0 | ["4954111000000005","4954111000000006"] |
| 4954111000000008 | `mekanism:chemical_infuser` | Combine gases (e.g. HCl) to feed the injection chamber. | 7.5 | -1.5 | ["4954111000000006"] |
| 4954111000000009 | `mekanism:pressurized_reaction_chamber` | Item+fluid+gas reactions (substrate, etc.); the versatile PRC. | 9.5 | 0.0 | ["4954111000000007"] |
| 495411100000000A | `mekanism:metallurgic_infuser` | Infuse dusts (carbon/redstone/diamond) to make alloys and steel dust. | 3.5 | 2.0 | ["4954111000000001"] |
| **495411100000000B** | `mekanism:thermal_evaporation_controller` | **Spine capstone (multiblock).** Brine -> lithium and 5x-tier salt; bundle the block+valve here. | 11.0 | 0.0 | ["4954111000000009"] |

- Bundle the thermal-evaporation multiblock into ONE node `...000B`: its task is
  `mekanism:thermal_evaporation_controller` (icon), and its prose instructs building the tower from
  `mekanism:thermal_evaporation_block` + `mekanism:thermal_evaporation_valve` (do NOT create
  separate block/valve item nodes — those are bare multiblock parts).

**Factory-tier side lane (basic tier only; y=+3, deps off the matching base machine):**

| node id | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 4954111000000010 | `mekanism:basic_smelting_factory` | Factory = parallel machines in one block; smelting tier. Bump throughput. | 2.0 | 3.0 | ["4954111000000003"] |
| 4954111000000011 | `mekanism:basic_enriching_factory` | Enriching factory: parallel ore-doubling. | 3.5 | 3.5 | ["4954111000000010"] |
| 4954111000000012 | `mekanism:basic_crushing_factory` | Crushing factory: parallel crushing for the return leg. | 5.0 | 3.0 | ["4954111000000011"] |

- Bundle steel intermediates into prose, not nodes. `mekanism:ingot_steel`/`ingot_bronze`/
  `ingot_osmium` and `steel_casing`/`basic_control_circuit` are bare-material feeders — reference
  them in the enrichment/infuser prose, do NOT task them (bare-ingot rule).
- **Do NOT re-task** the Atomic uranium/Mekasuit content; those live elsewhere and already depend
  on the base machines by recipe. No structural re-wire needed for Mekanism — the Atomic factory
  tiers (`aoa_astages_01_item_restrictions.js:588+`) are gated a full age later and reachable only
  after this IR chapter by progression. (If an Atomic Mek node is later found to be reachable
  before this chapter, add a dep on `495411100000000B`; none found in extraction.)
- **Crossing statement.** Main spine y in [-1.5, 0], infuser branch at y=2, factory lane at y>=3.
  All flow left-to-right from the single root. Two short vertical stubs (oxygen loop 6->7, 6->8)
  stay within one column-gap and do not cross the horizontal spine. VERIFY at author time.

### T-02c-3 — EXTEND `ir_immersive_engineering_early_factory` (id `4954010000000000`).

The existing chapter roots on `4954011000000001` (task `immersiveengineering:craftingtable`,
dep external `0B0310A0000000F0`) and spans x[0,15.5], y[-12,+5.5]. Free band: **left-lower region
x[-4,-1] and the y[+2.5,+6] top strip** are sparse. Place the multiblock line as a new lane
rooted on the existing crafting-table node. Use fresh suffixes in the `495401 1 0000010N` range
(implementer must grep to confirm unused).

**IE multiblock lane (advancement tasks where a formation advancement exists; item task for
single-block machines that have none):**

| node id | task | task type | teaching purpose | x | y | deps |
|---|---|---|---|---|---|---|
| 4954011000000101 | adv `immersiveengineering:main/mb_blastfurnace` | advancement | Crude Blast Furnace: brick multiblock that makes steel from iron + coal coke. Icon `immersiveengineering:blast_furnace`. | -3.0 | 3.0 | ["4954011000000001"] |
| 4954011000000102 | adv `immersiveengineering:multiblocks/mb_improvedblastfurnace` | advancement | Improved Blast Furnace: faster, adds slag; the real steel workhorse. Icon `immersiveengineering:advanced_blast_furnace`. | -1.5 | 3.0 | ["4954011000000101"] |
| 4954011000000103 | adv `immersiveengineering:multiblocks/mb_crusher` | advancement | Crusher multiblock: ore doubling via grinding. Icon `immersiveengineering:crusher`. | 0.0 | 4.0 | ["4954011000000102"] |
| 4954011000000104 | item `immersiveengineering:alloy_smelter` | item | Alloy Smelter (single block, no formation adv): combine metals into alloys. | 0.0 | 5.5 | ["4954011000000102"] |
| 4954011000000105 | adv `immersiveengineering:multiblocks/mb_mixer` | advancement | Mixer multiblock: fluid mixing (concrete, alloys). Icon `immersiveengineering:mixer`. | 1.5 | 4.0 | ["4954011000000103"] |
| 4954011000000106 | adv `immersiveengineering:multiblocks/mb_squeezer` | advancement | Squeezer multiblock: press seeds/plants to oil and plantoil. Icon `immersiveengineering:squeezer`. | 1.5 | 5.5 | ["4954011000000103"] |
| 4954011000000107 | item `immersiveengineering:bottling_machine` | item | Bottling Machine (single block): fill containers from a fluid feed. | 3.0 | 5.5 | ["4954011000000106"] |
| 4954011000000108 | item `immersiveengineering:sawmill` | item | Sawmill (single block): logs -> planks + sawdust at scale. | 3.0 | 4.0 | ["4954011000000105"] |
| 4954011000000109 | item `immersiveengineering:auto_workbench` | item | Auto Workbench (single block): blueprint-driven crafting from feed. | 4.5 | 4.0 | ["4954011000000108"] |
| 495401100000010A | adv `immersiveengineering:multiblocks/mb_silo` | advancement | Silo multiblock: bulk single-item storage. Icon `immersiveengineering:silo`. | 4.5 | 5.5 | ["4954011000000107"] |

- The Medieval `coke_oven` (`immersiveengineering:main/mb_cokeoven`) is authored in 02b (Medieval
  IE onboarding) — do NOT author it here; the blast furnace prose references coke as its input.
  If 02b has not landed, note `NEEDS 02b coke_oven` and still root the blast furnace on the existing
  IE crafting-table node.
- **Crossing statement.** New lane lives entirely in y>=+3 (top strip), the existing chapter's dense
  content is y<=+2.5. The lane flows left-to-right from the existing root at (0,0) up into the free
  strip; the single edge from (0,0) to (-3,3) runs into empty left space. VERIFY at author time.

### T-02c-4 — `ir_oritech_foundry` (NEW) + extendedcrafting lane.

**Oritech spine (machine blocks; cores are markers, machines craft from explicit intermediates —
do NOT imply core-as-ingredient in prose). Left-to-right, y=0.**

| node id | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 4954121000000001 | `oritech:machine_core_1` | Primitive Machine Core: the shared processing-tier marker. Craft the machines below directly. | 0.0 | 0.0 | [] (root) |
| 4954121000000002 | `oritech:basic_generator_block` | Basic Generator: burns fuel for RF; the power source every Oritech machine needs. | 2.0 | 1.0 | ["4954121000000001"] |
| 4954121000000003 | `oritech:pulverizer_block` | Pulverizer: ore -> dust doubling. Oritech's entry ore processor. | 2.0 | -1.0 | ["4954121000000001"] |
| 4954121000000004 | `oritech:powered_furnace_block` | Powered Furnace: electric smelting for the pulverized output. | 4.0 | -1.0 | ["4954121000000003"] |
| 4954121000000005 | `oritech:machine_core_2` | Basic Machine Core: the second processing tier; unlocks the foundry/refinery. | 4.0 | 0.5 | ["4954121000000004"] |
| 4954121000000006 | `oritech:foundry_block` | Foundry: multi-input alloying (bronze, steel, machine plating). | 6.0 | -1.0 | ["4954121000000005"] |
| 4954121000000007 | `oritech:refinery_block` | Refinery: fluid refining; feed with the refinery module for outputs. | 6.0 | 1.0 | ["4954121000000005"] |
| 4954121000000008 | `oritech:machine_frame_block` | Machine Frame: shared chassis the higher-tier machines assemble on. | 8.0 | 0.0 | ["4954121000000006","4954121000000007"] |
| **4954121000000009** | `oritech:machine_core_3` | **Chapter capstone.** Improved Machine Core: the IR ceiling; Gilded core_4 builds on this. | 10.0 | 0.0 | ["4954121000000008"] |

- Optional depth (side stubs off the spine, NOT required): `oritech:small_storage_block` (battery)
  off basic_generator; `oritech:steam_engine_block` off basic_generator as an alt power. Keep to
  1-2 optional nodes; do not pad. Mark optional nodes `optional: true`.
- Do NOT task `machine_plating_block` alone (bare material) — reference in foundry prose.

**extendedcrafting lane (3 nodes, appended below, y=+3; standalone tree, deps only within itself):**

| node id | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 4954121000000020 | `extendedcrafting:frame` | Machine Frame: the shell for the Basic Crafting Table. Made from black iron. | 6.0 | 3.0 | ["4954121000000005"] |
| 4954121000000021 | `extendedcrafting:basic_table` | Basic Crafting Table: a 5x5 grid for oversized recipes many mods use later. | 8.0 | 3.0 | ["4954121000000020"] |
| 4954121000000022 | `extendedcrafting:handheld_table` | Handheld Crafting Table: portable 3x3 access; QoL companion to the big table. | 10.0 | 3.0 | ["4954121000000021"] |

- `extendedcrafting:material_black_iron` (Black Iron Ingot) is the frame's feedstock — reference in
  frame prose, do NOT task (bare ingot). basic_table + frame + handheld_table all IR-locked
  (`aoa_astages_01n_ascension.js:145-149`).
- Chapter icon: `oritech:foundry_block`.
- **Crossing statement.** Oritech spine y in [-1,1] flowing left-to-right; extendedcrafting lane at
  y=3 with a single vertical entry edge from core_2 (`...0005`, at y0.5) down to frame (y3) at x6 —
  this edge runs in the gap between the spine and the ec lane with no node in column x6 between
  y1 and y3, so no crossing. VERIFY at author time.

**RE-WIRE (owned by T-02c-9b, edits `atomic_oritech_convergence.snbt`):**

| existing node | current deps | ADD dep on | rationale |
|---|---|---|---|
| `4F43010000010000` (`oritech:machine_processing_addon`, in-chapter root, 8 children) | ["4D53010000010003"] (external chapter-entry) | **4954121000000009** (new IR Oritech capstone) | This is the atomic Oritech graph root. Adding the IR foundry capstone as a second dependency forces a player through the IR machine line before the atomic addon tier. Keep the existing external dep too (AND-combines). |

### T-02c-5 — EXTEND `ir_create_industrial_addons` (id `4954070000000000`).

Existing IP oil chain: `projector` (`4954071000000001`, x0 y-2.5) -> `derrick`
(`4954071000000002`) -> `pumpjack` (`4954071000000003`) ... Sequence the two surviving IP items
off the projector/pumpjack so the CDG-diesel -> IP handoff reads. Fresh suffixes `495407 1 0000010N`.

| node id | item id | task type | teaching purpose | x | y | deps |
|---|---|---|---|---|---|---|
| 4954071000000101 | `immersivepetroleum:seismic_survey` | item | Seismic Survey Tool: scan a chunk for oil reservoirs before you drill. Sequenced right after the Engineer's Projector so the survey-then-drill loop is explicit. | 1.5 | -4.0 | ["4954071000000001"] |
| 4954071000000102 | `immersivepetroleum:flarestack` | item | Flarestack: safely burn off excess gas/pressure from the oil rig; vents the pumpjack. | 4.5 | -2.0 | ["4954071000000003"] |

- **`immersivepetroleum:gas_generator` DROPPED — id does not exist in the IP jar** (verified). Do
  NOT invent a substitute; if a gas-burning generator beat is later wanted, it is IE's diesel
  generator, already covered elsewhere.
- Icons: task items. **Crossing statement.** Both new nodes hang directly off existing nodes in the
  existing left region; seismic at (1.5,-4) below projector (0,-2.5) — edge runs down-right into a
  gap; flarestack at (4.5,-2) off pumpjack — verify pumpjack coords at author time and nudge to
  avoid the derrick->pumpjack edge. Compute crossings; re-lay if the flarestack edge clips.

### T-02c-6 — EXTEND `ir_magic_feedstock_and_spectrum_network` (id `49540B0000000000`).

Neo Vitae IR segment (Hellfire Forge era). Node scheme `49540B1000000NNN`; use fresh suffixes in
the `49540B10000001NN` range (grep to confirm unused). Root the segment on the chapter's existing
Neo Vitae entry (implementer: grep the chapter for the highest-tier existing `neovitae:` node —
likely the `hellfire_forge` node — and root on it; if none, root on the chapter's spine entry).

| node id | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 49540B1000000101 | `neovitae:vas_maleficum` | Vas Maleficum: the demon-will collection vessel; stores tartaric essence for the infernal tier. | (place) | (place) | [root] |
| 49540B1000000102 | `neovitae:spira_infernalis` | Spira Infernalis: routes/pumps demon will between vessels; the infernal network's plumbing. | (place) | (place) | ["49540B1000000101"] |
| 49540B1000000103 | `neovitae:crystallarium_maleficum` | Crystallarium Maleficum: grows will-infused crystals; the demon-will crafting feedstock. | (place) | (place) | ["49540B1000000102"] |
| 49540B1000000104 | `neovitae:teleposer` | Teleposer: block/entity teleport pad; program it with a Teleposition Focus (`neovitae:focus`). | (place) | (place) | ["49540B1000000101"] |
| 49540B1000000105 | `neovitae:tabula_robur` | Tabula Robur: the strength living-armor upgrade tablet; applied at the Hellfire Forge. | (place) | (place) | ["49540B1000000103"] |
| 49540B1000000106 | `neovitae:tabula_animata` | Tabula Animata: the animation/attack living-armor tablet. | (place) | (place) | ["49540B1000000105"] |

- CORRECTIONS folded: NO `crystallarium` (only `_maleficum`); focus item is `neovitae:focus`
  (reference in teleposer prose, do not task — it is a small component); tabula line is
  `tabula_robur`/`tabula_animata` (NO `tabula_rasa`/`tabula_maleficum`; `tabula_vitae` is the
  Renaissance one, already staged Ren — do NOT task here).
- All six IR-locked (`aoa_astages_01m_magic.js:129-138`).
- **Coords:** implementer computes from the chapter's free space (read the existing node coord
  range first). Lay as one crossing-free lane branching off the Neo Vitae hub: vessel->plumbing->
  crystallarium->tabulas as the main chain, teleposer as a side stub off the vessel.
- **Crossing statement.** One linear chain + one stub = inherently crossing-free if laid on a fresh
  row band. VERIFY against the existing chapter layout at author time (this chapter is shared with
  Spectrum/Malum content — pick a row band the existing nodes do not occupy).

### T-02c-7 — EXTEND `ir_power_motion_and_grid` (id `4954050000000000`).

Base electrodynamics processing tier (the "triple" tiers are already tasked here; the base tier is
not). Node scheme `495405 1 00000NNN`; existing electrodynamics cluster sits around x[12.5,14],
y[-9]. Add the base tier just LEFT of / above the triple cluster and make the triple node depend on
the base (progression: base -> triple). Fresh suffixes `495405 1 0000003N`.

| node id | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 4954051000000031 | `electrodynamics:mineralgrinder` | Mineral Grinder: base ore-grinding machine; the electrodynamics processing entry. | 10.5 | -9.0 | [existing electrodynamics entry — grep for it] |
| 4954051000000032 | `electrodynamics:electricfurnace` | Electric Furnace: base powered smelting for ground output. | 10.5 | -10.5 | ["4954051000000031"] |

- **RE-WIRE within this chapter (same task, no separate seam):** the existing
  `electrodynamics:mineralgrindertriple` node (`495405100000002D`, deps `["495405100000002B"]`) should
  gain a dep on the new base `4954051000000031` so base precedes triple. Confirm `495405100000002B`
  is the electrodynamics sub-root; if the triple tier already chains off a base-adjacent node,
  insert the base node into that chain instead of adding a parallel edge (avoid a crossing).
- **DEDUP:** `electrodynamics:coalgenerator` is ALREADY tasked in this chapter
  (`ir_power_motion_and_grid.snbt:2242`) — do NOT re-task; the base grinder can reference it as its
  power source in prose. `mineralcrusher`/`mineralcrushertriple` already tasked in g6 — do NOT task
  here.
- **Crossing statement.** Two new nodes in a short vertical stub at x10.5, left of the existing
  triple cluster (x12.5+). The single re-wire edge from base (10.5,-9) to triple (14,-9) runs along
  the y=-9 row; confirm no existing node sits on that row between x10.5 and x14 (the arc-furnace
  triple is at 12.5,-9 — SO IT WILL CLIP). **Re-lay:** put the base grinder at (10.5,-11) and route
  the edge below the existing cluster, OR insert base as the parent of `495405100000002B` (cleaner).
  Implementer computes crossings and picks the non-clipping option. FLAG for CC.

### T-02c-8 — Deeper & Darker gear-tail MOVE (ledger row 8).

**Move OUT of `ren_deeper_darker_otherside` and INTO `ir_netherite_citadel_obsidilith`
(id `49540C0000000000`, group IR). Neo Vitae precedent: ids travel, source re-wired, proof intact.**

Nodes to MOVE (all leaves in Ren; safe):

| source node (Ren) | item id | Ren deps | dependents in Ren | action |
|---|---|---|---|---|
| `0B0310600000008F` | `deeperdarker:warden_upgrade_smithing_template` | ["0B0310600000008E" warden_carapace] | none (leaf) | MOVE to citadel; re-parent (see below) |
| `0B0310600000008D` | `deeperdarker:resonarium_upgrade_smithing_template` | ["0B03106000000034" resonarium] | none (leaf) | MOVE to citadel; re-parent |
| `0B03106000000091` | `deeperdarker:sonorous_staff` (DUPLICATE) | ["0B03106000000034" resonarium] | none (leaf) | MOVE to citadel (de-dupes: the other sonorous_staff `0B03106000000045` stays in Ren) |

**New home in citadel** (reuse the existing Deeper Darker presence: the chapter already has
`deeperdarker:resonarium_helmet` at `49540C1000000029`, x-1.5 y-3, in the left gear-tail cluster
rooted on `49540C1000000001`). Place the three moved nodes as a small DD sub-lane off that helmet
node. Assign fresh citadel-scheme ids `49540C10000000NN` (grep to confirm unused; `...002A..002F`
are taken, use `...0030+`):

| new citadel node | item id | teaching purpose | x | y | deps |
|---|---|---|---|---|---|
| 49540C1000000030 | `deeperdarker:warden_upgrade_smithing_template` | Warden smithing template: upgrade netherite-tier gear with warden materials for the citadel's deep-dark set. | -1.5 | -4.5 | ["49540C1000000029"] |
| 49540C1000000031 | `deeperdarker:resonarium_upgrade_smithing_template` | Resonarium smithing template: the resonarium armor upgrade path. | 0.0 | -4.5 | ["49540C1000000029"] |
| 49540C1000000032 | `deeperdarker:sonorous_staff` | Sonorous Staff: sculk-charged utility weapon; the deep-dark capstone toy. | 1.5 | -4.5 | ["49540C1000000029"] |

- **Source re-wire (in `ren_deeper_darker_otherside`):** DELETE the three moved nodes
  (`0B0310600000008F`, `0B0310600000008D`, `0B03106000000091`). Since all three are LEAVES (no Ren
  node depends on them), deletion breaks nothing in Ren. `warden_carapace` (`0B0310600000008E`),
  `resonarium` (`0B03106000000034`), `reinforced_echo_shard` (`0B03106000000033`), and the surviving
  `sonorous_staff` (`0B03106000000045`) all STAY — they are load-bearing Ren hubs.
- **Proof-stage intact:** neither the Ren chapter capstone nor the `ren_deeper_darker_otherside_complete`
  grant depends on any of the three moved leaves (verify the chapter capstone's dep list at author
  time; extraction shows the moved nodes have zero dependents). The move does not alter any AStages
  grant. DD gear stays legal: it is atomic-context deep-dark gear placed in an IR citadel chapter
  that ALREADY hosts betterend/undergarden/deeperdarker post-Ren gear as a reward tail — consistent
  with the chapter's established role.
- **Lang:** move the three quests' existing `quest.<id>.*` lang keys is NOT needed — the quest IDs
  change (new citadel ids), so the OLD keys (`quest.0B0310600000008F.*` etc.) become orphaned and
  the NEW ids need stubs. Add stub keys for `49540C1000000030/31/32` to
  `phase0/stubs/T-02c-8_stubs.txt`; Opus writes fresh prose. Leave the orphaned Ren keys for the
  Codex normalization sweep to prune (do NOT hand-delete lang in this task).
- **Crossing statement.** Three new nodes in a single row (y-4.5) under the existing resonarium_helmet
  (x-1.5,y-3), each a direct child — three short parallel down-edges, no crossing. VERIFY.

### T-02c-9a / T-02c-9b — see re-wire tables under T-02c-1 and T-02c-4.

---

## D. Lane sketches (per new/extended chapter)

- **`ir_digital_storage_foundations`** (T1): 3 horizontal bands.
  - Row band +0..+3 = AE2 lane (controller root at x0 -> pattern_provider capstone at x17.5).
  - Row band -4..-3 = RS lane (controller root at x0 -> autocrafter capstone at x13).
  - Row band -6.5..-7.5 = cabletiers elite (5 nodes hanging off the RS capstone).
  - Two roots at x0 (top + bottom band). No inter-lane edges except cabletiers->RS-capstone (stays
    in the bottom two bands). Crossing-free.
- **`ir_mekanism_ore_works`** (T2): single left-to-right spine y[-1.5,0], infuser stub at y2,
  factory lane at y3. One root. Crossing-free.
- **`ir_immersive_engineering_early_factory`** (T3, extend): new IE multiblock lane in the y>=+3
  top strip, x[-3,4.5]; existing content stays y<=+2.5. One entry edge from existing root into the
  strip. Crossing-free within the strip.
- **`ir_oritech_foundry`** (T4): spine y[-1,1] x[0,10]; extendedcrafting lane y3 x[6,10] with a
  single vertical entry edge at x6. Crossing-free.
- **`ir_create_industrial_addons`** (T5, extend): 2 nodes appended to the existing IP oil sub-tree
  (left region). Verify against existing derrick/pumpjack edges; nudge to avoid clip.
- **`ir_magic_feedstock_and_spectrum_network`** (T6, extend): one linear chain + teleposer stub in a
  fresh row band the Spectrum/Malum content does not occupy. Implementer picks the band.
- **`ir_power_motion_and_grid`** (T7, extend): 2-node vertical stub left of the electrodynamics
  triple cluster; re-lay to avoid the y=-9 arc-furnace-triple clip (see T7 note).
- **`ir_netherite_citadel_obsidilith`** (T8, extend): 3-node DD row at y-4.5 under resonarium_helmet.
  Crossing-free.

---

## E. VERIFICATION LOG (every id proven; agents 2026-07-02)

**AStages IR-gate lines (legality proof — gating is CLOSED, cited only to confirm legal-at-IR):**
- AE2: `kubejs/server_scripts/aoa_astages_01i_ae2.js:34-42` — controller/drive/energy_cell/
  energy_acceptor @ industrial_revolution.
- RS: `aoa_astages_01j_storage.js:31-38` — controller/grid/crafting_grid/disk_drive/detector/
  security_manager/storage_monitor/portable_grid @ IR.
- cabletiers elite: `aoa_astages_01j_storage.js:57-61` — elite_exporter/constructor/destructor/
  interface/disk_interface @ IR.
- Mekanism: `aoa_astages_01_item_restrictions.js:287-328` — all base machines + basic_*_factory +
  thermal_evaporation_* @ IR (advanced/elite/ultimate factories @ atomic, lines 588+).
- IE: `aoa_astages_01d_immersive.js:34-53` — IE machines @ IR (multiblocks have no item lock; they
  are structural — the mb_* advancement is the completion signal).
- Oritech: `aoa_astages_01e_oritech.js:37-63` — machine_core_2/3, pulverizer/powered_furnace/
  foundry/refinery/basic_generator/steam_engine @ IR; machine_core_1 UNLOCKED (free entry);
  machine_core_4 @ gilded (line 65). Header lines 3-5: machines do NOT craft from cores.
- extendedcrafting: `aoa_astages_01n_ascension.js:145-149` — basic_table/basic_auto_table/
  handheld_table/frame/pedestal @ IR.
- immersivepetroleum: `aoa_astages_01d_immersive.js:61,63` — seismic_survey, flarestack @ IR.
- neovitae: `aoa_astages_01m_magic.js:129-138` — vas_maleficum/spira_infernalis/
  crystallarium_maleficum/teleposer/tabula_robur/tabula_animata @ IR.
- electrodynamics: `aoa_astages_01k_nuclear_power.js:106` — electricfurnace @ IR; base processing @
  IR per file header (line 8).

**Item-id proofs (jar lang/model, verified; corrections in bold):**
- AE2: controller, energy_acceptor, energy_cell, drive, cell_workbench, io_port, crafting_unit,
  crafting_accelerator, crafting_terminal, terminal, pattern_encoding_terminal, pattern_provider,
  molecular_assembler, wireless_access_point — CONFIRMED (lang `block.ae2.*`/`item.ae2.*`, models).
  **`item_storage_cell_1k`** (not `1k_storage_cell`), **`1k_crafting_storage`** (not
  `crafting_storage_1k`), **`chest`** (not `me_chest`). Jar `appliedenergistics2-19.2.17.jar`.
- RS: controller, grid, crafting_grid, disk_drive, 1k_storage_disk, detector, security_manager,
  storage_monitor, portable_grid, cable — CONFIRMED. **`autocrafter`** (not `crafter`); no
  `disk_manipulator` (nearest `disk_interface`). Jar `refinedstorage-neoforge-2.0.9.jar`.
- cabletiers: **entry tier = elite** (no basic/advanced). elite_importer/exporter/constructor/
  destructor/disk_interface CONFIRMED (`item.cabletiers.*`). Jar `cabletiers-...-0.6.12.jar`.
- Mekanism: enrichment_chamber, crusher, purification_chamber, chemical_injection_chamber,
  chemical_infuser, osmium_compressor, electrolytic_separator, pressurized_reaction_chamber,
  thermal_evaporation_controller/block/valve, energized_smelter, metallurgic_infuser,
  basic_smelting/enriching/crushing_factory — CONFIRMED (`block.mekanism.*`). **NO `combining_factory`
  bare — use `basic_combining_factory`.** Ingots are **`ingot_steel`/`ingot_bronze`/`ingot_osmium`**
  (not `*_ingot`). heat_generator is **`mekanismgenerators:`** namespace (not used in plan). Jar
  `Mekanism-1.21.1-10.7.19.85.jar`.
- IE: block items blast_furnace, advanced_blast_furnace, crusher, alloy_smelter, mixer, squeezer,
  bottling_machine, sawmill, auto_workbench, silo — CONFIRMED. Advancements:
  `main/mb_blastfurnace`, `multiblocks/mb_improvedblastfurnace`, `multiblocks/mb_crusher`,
  `multiblocks/mb_mixer`, `multiblocks/mb_squeezer`, `multiblocks/mb_silo` — CONFIRMED (advancement
  ids do NOT match block ids). alloy_smelter/bottling_machine/sawmill/auto_workbench have **NO mb_
  advancement** -> task on block item. IE steel = **`ingot_steel`**. Jar
  `ImmersiveEngineering-1.21.1-12.4.2-194.jar`.
- Oritech: machine_core_1 ("Primitive"), _2, _3, pulverizer_block, powered_furnace_block,
  foundry_block, refinery_block, basic_generator_block, steam_engine_block, small_storage_block —
  CONFIRMED. **`machine_frame_block`** (not `machine_frame`), **`machine_plating_block`** (not
  `machine_plating`). No `bioreactor_block` (it is `bio_generator_block`). Jar
  `oritech-neoforge-1.21.1-1.2.8.jar`.
- extendedcrafting: basic_table ("Basic Crafting Table"), frame ("Machine Frame"), handheld_table,
  crafting_core — CONFIRMED. Black iron feedstock = **`material_black_iron`** (not `black_iron_frame`/
  `black_iron_ingot`). Jar `ExtendedCrafting-1.21.1-7.0.8.jar`.
- immersivepetroleum: seismic_survey ("Seismic Survey Tool", ITEM), flarestack ("Flarestack",
  BLOCK), projector, pumpjack (multiblock) — CONFIRMED. **`gas_generator` DOES NOT EXIST — DROPPED.**
  Jar `ImmersivePetroleum-1.21.1-4.4.1-37.jar`.
- neovitae: vas_maleficum, spira_infernalis, crystallarium_maleficum, teleposer, tabula_robur,
  tabula_animata — CONFIRMED. **No `crystallarium`/`teleposer_focus`/`tabula_rasa`/`tabula_maleficum`;
  focus item = `focus`.** Jar `neovitae-1.21.1-1.0.25.jar`.
- electrodynamics: **`mineralgrinder`** (no underscore), electricfurnace, coalgenerator — CONFIRMED.
  Jar `electrodynamics-1.21.1-1.0.9.jar`.
- deeperdarker: warden_carapace, warden_upgrade_smithing_template, resonarium_upgrade_smithing_template,
  sonorous_staff, reinforced_echo_shard — CONFIRMED (`item.deeperdarker.*`, jar
  `deeperdarker-neoforge-1.21.1-1.4.1.jar`). `soul_elytra` exists as an item but is NOT tasked in
  `ren_deeper_darker_otherside` — DROPPED from the move (nothing to move).

**Existing-structure proofs (extraction agent, 2026-07-02):**
- g4 `5E42E6B4A7C91D30` (Gilded): AE2 nodes `4D4E011000000001` (molecular_assembler),
  `4D4E011000000108` (pattern_provider), `4D4E011000000002` (wireless_access_point),
  `4D4E011000000006` (refinedstorage:autocrafter). No spatial/quantum node exists.
- atomic_oritech_convergence `7D28E4AEBC440F10` (Atomic): in-chapter root `4F43010000010000`
  (machine_processing_addon), 8 children.
- ir_netherite_citadel_obsidilith `3F77A31B7D30C0AA` (IR): root `49540C1000000001`; obsidilith kill
  `49540C1000000005`; capstone `4954631000000000` (7 deps); existing DD node
  `deeperdarker:resonarium_helmet` `49540C1000000029`. `...002A..002F` taken.
- ren_deeper_darker_otherside `0B038EB15EBBFD95` (Ren): moved leaves `0B0310600000008F`,
  `0B0310600000008D`, `0B03106000000091` (all zero dependents). Load-bearing (stay):
  `0B03106000000033` reinforced_echo_shard, `0B03106000000034` resonarium, `0B0310600000008E`
  warden_carapace, `0B03106000000045` sonorous_staff (external-gated).

---

## F. Open decisions for CC / canon call (do NOT author blind)

1. **g4 duplicate-item dedup (T-02c-9a).** g4 nodes `4D4E011000000108` (`ae2:pattern_provider`) and
   `4D4E011000000006` (`refinedstorage:autocrafter`) task the SAME items as the new AE2/RS capstones
   `495410100000000F` / `495410100000002A`. The pack-wide no-duplicate-item-task rule requires a
   choice: (a) DELETE the g4 duplicates and re-point their children onto the new IR capstones
   (cleanest, removes 2 g4 nodes); or (b) convert the g4 duplicates to `check_quest` tasks pointing
   at the new IR capstone ids (keeps g4 node count, no item re-task). **Recommend (a).** CC to
   confirm before T-02c-9a runs; the g4 children affected are `4D4E011000000005`
   (`expandedae:exp_crafting_unit`) and the megacells ladder root `4D4E01100000000A` — re-parent
   them onto the surviving new capstone.
2. **Row-8 `warden_carapace` (8E) deviation.** The prompt named `warden_carapace 8E` among the moved
   ids. Extraction proved `warden_carapace` (`0B0310600000008E`) is NOT a leaf: it depends on
   `reinforced_echo_shard` (`0B03106000000033`, a load-bearing Ren hub with 3 dependents) and it is
   the PARENT of the `warden_upgrade_smithing_template`. Moving carapace would either (i) drag the
   reinforced_echo_shard hub and orphan the resonarium sub-tree, or (ii) create a citadel node with
   a cross-chapter dependency on a Renaissance node (age-inversion of a dependency edge). **Chosen:
   leave `warden_carapace` in Ren; move only the two smithing templates + the duplicate staff (all
   true leaves), and re-parent the moved warden template onto the existing citadel
   `resonarium_helmet` node instead of onto carapace.** This preserves the "gear tail in citadel"
   intent (templates + staff land in the citadel) without breaking Ren or inverting a dependency.
   If CC wants carapace itself in the citadel, that is a larger move (also relocate
   reinforced_echo_shard, re-wire the resonarium sub-tree) — flag as a separate task, not folded
   here.
3. **T-02c-7 electrodynamics edge clip.** The base->triple re-wire edge clips the existing
   arc-furnace-triple node at (12.5,-9). Two safe fixes offered in T7; implementer picks the
   non-crossing one and CC confirms. Prefer inserting the base grinder as the PARENT of the
   electrodynamics sub-root `495405100000002B` (no new long edge).
4. **IE coke_oven dependency (T-02c-3).** Blast furnace prose references coke from the Medieval
   `coke_oven` (02b deliverable). If 02b has not landed, the IE blast-furnace node still roots on the
   existing IR crafting-table node (no hard dep on a non-existent coke node) — note it and proceed.

---

## G. Verification steps (every task; per 02c "Method")

Each implementer task, before hand-off:
1. **tier_audit** — run the reveal/tier audit (`.aoa_reveal_audit/` toolchain) confirming every new
   node's task item is legal at IR (or earlier) per the AStages line cited in E. No node may task an
   item gated later than industrial_revolution.
2. **ef_audit (era-flavor)** — confirm no node introduces a mod/mechanic outside IR's legal tech
   (section 3 of the preamble). Mekanism advanced/elite/ultimate factories, Oritech core_4+,
   AE2 spatial/quantum, RS INFINITE tier = OUT (they are Gilded/Atomic/OW) and must NOT appear.
3. **crossing statement** — run the dependency-crossing computer on the edited chapter; paste the
   result. ZERO crossings required (hard constraint). Re-lay coordinates until zero.
4. **duplicate-item scan** — `grep` the ENTIRE `config/ftbquests/quests/chapters/` for each new task
   item id BEFORE adding it; if it already appears, reference the existing quest as a dependency
   instead of re-tasking (this plan already did this scan; re-run to catch anything landed since).
5. **anchored id-dup scan** — `grep -P '^\s+id: "'` (or the locale-safe Grep-tool equivalent) to
   confirm no quest-id collision with the assigned prefix.
6. **byte discipline** — CRLF/tab preserved; `SkillsLevel`/`PlayerSpells` blocks copied from a
   sibling, never stripped or hand-typed.
7. **stubs** — every new node's three lang keys written to `phase0/stubs/<task-id>_stubs.txt` (one
   line each, `[STUB]`/`[BRIEF]` encoding the teaching purpose from the node table). NONE to
   `en_us.snbt`.
8. **before/after counts** — record to `LEDGER.md` (chapter node counts pre/post).

Final CC gate (after all tasks): confirm, per foundation mod, that a fresh player can path
foundation -> endgame by quest dependencies alone: AE2 controller -> ... -> new capstone -> g4
molecular_assembler; RS controller -> ... -> new capstone -> (g4 re-wire); Oritech core_1 -> ... ->
core_3 capstone -> atomic machine_processing_addon; Mekanism/IE reachable-before-endgame confirmed.
