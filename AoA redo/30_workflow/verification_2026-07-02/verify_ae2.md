# AE2-family quest coverage verification

READ-ONLY audit. Date 2026-07-02. Instance: Ascension of Ages (codex and cc).

## Installed AE2-family jars (verified in /mods)

| Jar | Namespace | Role |
|---|---|---|
| appliedenergistics2-19.2.17.jar | `ae2` | Core ME storage/autocrafting spine |
| ExtendedAE-1.21-2.2.33-neoforge.jar | `extendedae` | Assembler matrix, ex_ machines, circuit cutter, caner |
| AdvancedAE-1.6.11-1.21.1.jar | `advanced_ae` | Quantum crafter/computer, adv pattern providers, reaction chamber |
| megacells-4.11.0.jar | `megacells` | Mega cells/crafting, bulk/portable cell ladder |
| ae2wtlib-19.5.0.jar | (ae2 wireless terminals lib) | Wireless terminal support (content surfaces under ae2) |
| Applied-Mekanistics-1.6.3.jar | (appmek) | Chemical cells bridge (registry-excluded per prior canon) |
| appliedpneumatics-1.21.1-neoforge-1.0.8.jar | (appliedpneumatics) | AE2 pneumatic addon |

NOT installed: megacells is present (verified); `expatternprovider` is NOT a
separate namespace here (ExtendedAE ships under `extendedae`); `aeinfinitybooster`
NOT present. `advancedae`/`aeadditions` namespaces do not appear.

## VERDICT: the "14 refs" census figure is FALSE / undercounted

Actual namespace token counts across `config/ftbquests/quests/chapters/`:

- `ae2:` = 55
- `extendedae:` = 31
- `advanced_ae:` = 29
- `megacells:` = 78
- Total AE2-family item tokens = ~193, across 5 chapters.

The census almost certainly counted only `ae2:` *distinct nodes in one chapter*
(the IR chapter has exactly 14 distinct AE2-family task ids). The pack has broad
AE2 coverage. **The real problem is not volume — it is a missing entry chain.**

### Chapter map

| Chapter | Age | AE2-family content |
|---|---|---|
| `ir_digital_storage_foundations` | IR | 14 nodes: controller, drive, chest, io_port, energy acceptor/cell, crafting_unit/accelerator, 1k crafting storage, item_storage_cell_1k, cell_workbench, terminal, crafting/pattern-encoding terminal, cable pattern provider |
| `g4_the_infinite_grid` | Gilded | molecular_assembler, pattern_provider(s), wireless access point/terminal/booster/receiver, extendedae crystal_assembler + machine_frame, advanced_ae reaction_chamber, full megacells 1M-256M item/fluid/chemical cell + mega-crafting ladder |
| `at3_chain_reaction` | Atomic | megacells:radioactive_cell_component (single seam) |
| `at4_machine_soul` | Atomic | spatial IO (pylon/port/anchor), full extendedae ex_ suite + assembler matrix + caner/circuit_cutter/crystal_fixer, advanced_ae adv pattern providers, megacells 256M + portable cell ladder |
| `ow4_the_dyson_project` | OW | quantum bridge (link/ring/singularity/QES/matter_ball), advanced_ae quantum crafter/computer/multithreader/storage, extendedae wireless hub/connect |

## Beats-vs-quested table (canonical AE2 progression)

Source: guide.appliedenergistics.org. Legend: T = taught by a quest task, — = absent.

| Progression beat (jar-verified id) | Taught where | Gap |
|---|---|---|
| Meteorite / sky_stone_block / meteorite compass | — | **GAP — entry point never introduced** |
| Certus quartz crystal / charged certus (`ae2:certus_quartz_crystal`, `ae2:charged_certus_quartz_crystal`) | — | **GAP** |
| Budding certus + growth accelerator (`ae2:growth_accelerator`) | — | **GAP — core early-game farm never taught** |
| Charger (`ae2:charger`) → charged certus / fluix | — | **GAP** |
| Fluix crystal (`ae2:fluix_crystal`) | — | **GAP** |
| Inscriber (`ae2:inscriber`) | — | **GAP — the single most important AE2 machine** |
| 4 presses (`ae2:silicon_press`, `logic_processor_press`, `calculation_processor_press`, `engineering_processor_press`) | — | **GAP — meteorite reward never claimed by quest** |
| Printed silicon + printed processors (`ae2:printed_silicon`, `printed_*_processor`) | — | **GAP** |
| Processors (`ae2:logic_processor`, `calculation_processor`, `engineering_processor`) | — | **GAP — every ME block depends on these** |
| Energy acceptor / cell (`ae2:energy_acceptor`, `ae2:energy_cell`) | IR | T |
| Controller (`ae2:controller`) | IR | T |
| ME drive + 1k cell (`ae2:drive`, `ae2:item_storage_cell_1k`, `ae2:1k_crafting_storage`) | IR | T (but only 1k; 4k/16k/64k/256k gated, not quest-taught) |
| Terminals (`ae2:terminal`, `crafting_terminal`, `pattern_encoding_terminal`) | IR | T |
| Cell workbench (`ae2:cell_workbench`) | IR | T |
| IO port (`ae2:io_port`) | IR | T |
| ME cables / quartz fiber (`ae2:*_glass_cable`, `ae2:quartz_fiber`) | — | **GAP — network wiring never taught** |
| Interface (`ae2:interface`) | — | **GAP** |
| Import/Export/Storage bus (`ae2:import_bus`, `export_bus`, `storage_bus`) | — | **GAP — automation I/O never taught** |
| Annihilation / formation plane (`ae2:annihilation_plane`, `ae2:formation_plane`) | — | **GAP** |
| Level emitter (`ae2:level_emitter`, `energy_level_emitter`) | — | **GAP** |
| P2P tunnels (`ae2:me_p2p_tunnel` + fe/item/fluid/redstone variants) | — | **GAP — whole P2P subsystem absent** |
| Matter condenser / singularity (`ae2:condenser`, `ae2:singularity`, `matter_ball`) | condenser —, singularity/matter_ball OW | condenser GAP |
| Molecular assembler + pattern provider (autocrafting) | Gilded (g4) | T |
| Crafting CPU: unit/accelerator/monitor/storage tiers | IR (unit/accel), Gilded (mega) | partial T |
| Wireless terminal + access point + booster | Gilded (g4) | T |
| Spatial IO (pylon/port/anchor) | Atomic (at4) | T |
| Quantum bridge (link/ring/QES) | OW (ow4) | T |
| Security terminal (`ae2:security_station`) | — | minor GAP (optional) |
| Color applicator / cable colors | — | intentionally ungated decor; skip |

## Gate truth (`kubejs/server_scripts/aoa_astages_01i_ae2.js`)

Tier→age map is thorough: core ME network at `industrial_revolution`; spatial +
extendedae ex_ suite + assembler matrix at `atomic`; advanced_ae quantum +
extendedae crystal_assembler/machine_frame + megacells mega ladder at
`gilded_age`/`otherworldly`. The script's own header comment states: *"AE2 starts
in Industrial Revolution. inscriber + fluix produce the processors there."*

**The gate says the inscriber/press/processor chain belongs to IR — but the IR
chapter teaches none of it.** Certus/fluix/growth/inscriber/press are left
ungated (correctly, they are the entry funnel), yet no quest introduces them.
Result: a player reading only the questbook is told to build a Controller and ME
Drive with no quest ever explaining where processors, presses, or certus come
from. Not a hardlock (recipes are open), but a real teaching gap on the pack's
storage spine.

## Ranked jar-verified gap list (no filler)

All ids verified present in the respective jar lang. All are at/below their
proposed chapter's age per the live gate.

### P0 — IR entry chain (belongs in `ir_digital_storage_foundations`, age=industrial_revolution)
Bundle into ~3-4 new upstream nodes feeding the existing Controller node:

1. **Meteorite + certus + growth farm** — `ae2:certus_quartz_crystal`,
   `ae2:charged_certus_quartz_crystal`, `ae2:growth_accelerator`, `ae2:charger`.
   (sky_stone_block/meteorite compass optional flavor.) One node.
2. **Inscriber + 4 presses** — `ae2:inscriber` +
   `ae2:silicon_press`, `ae2:logic_processor_press`,
   `ae2:calculation_processor_press`, `ae2:engineering_processor_press`. One node.
3. **Processors** — `ae2:logic_processor`, `ae2:calculation_processor`,
   `ae2:engineering_processor` (fold `printed_silicon`/`fluix_crystal` into text).
   One node. This is the prerequisite the current chapter silently assumes.

### P1 — IR network fabric (same chapter, one node each or bundled pair)
4. **Buses** — `ae2:import_bus`, `ae2:export_bus`, `ae2:storage_bus` (bundle 3).
5. **Interface + planes** — `ae2:interface`, `ae2:annihilation_plane`,
   `ae2:formation_plane` (bundle 3).
6. **Level emitter + P2P** — `ae2:level_emitter`, `ae2:me_p2p_tunnel` (bundle;
   fe/item/fluid P2P variants as text). Automation logic beat.
7. **Cell ladder** — `ae2:item_storage_cell_4k/16k/64k/256k` +
   `ae2:4k/16k/64k/256k_crafting_storage` (bundle into one "scale the drive" node;
   all IR-gated, currently only 1k taught).

### P2 — minor / optional
8. `ae2:condenser` (matter condenser → singularity feeder) — IR/Gilded, one seam.
9. `ae2:security_station` — optional network-security beat, IR.

### Non-gaps (do NOT author)
- Decorative quartz/fluix/sky_stone building blocks, cable color variants — ungated by design.
- appmek chemical bridge, cell color variants — registry-excluded / housing-is-the-gate.
- Gilded/Atomic/OW surfaces (g4/at3/at4/ow4) are already well covered.

## Bottom line
Volume is fine (~193 tokens, 5 chapters). The census "14" is the IR chapter's
distinct-node count, not total coverage. The genuine defect is a **missing IR
entry chain**: certus → growth → charger → inscriber → 4 presses → processors,
plus the **network fabric** (buses, planes, interface, level emitter, P2P) — all
jar-verified, all IR-legal per the gate, all absent from every chapter. The
questbook currently starts AE2 at the Controller, skipping everything a new
player needs to reach it.

## Sources
- guide.appliedenergistics.org/development/getting-started (1.21.1 canonical beats)
- guide.appliedenergistics.org/1.20.1/getting-started
- allthemods.github.io/alltheguides/mods/ae2/introduction/
- JAR lang: appliedenergistics2-19.2.17.jar, ExtendedAE-1.21-2.2.33, AdvancedAE-1.6.11, megacells-4.11.0
- Live: config/ftbquests/quests/chapters/{ir_digital_storage_foundations,g4_the_infinite_grid,at3_chain_reaction,at4_machine_soul,ow4_the_dyson_project}.snbt
- Gate: kubejs/server_scripts/aoa_astages_01i_ae2.js
