# Phase 0 — Task I: FOMO Quest-Coverage Shortlist

**Audit only. No files edited outside phase0/. No git commands run.**
Date: 2026-07-02. Pack root: `C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)`.

## Method + proof commands

- **Coverage map**: parsed every `item:` / `id:` / `entity:` / `advancement:` / `block:` reference in
  `config/ftbquests/quests/chapters/*.snbt`, aggregated by namespace (strict `[a-z0-9_]+` namespace regex).
  Script: `phase0/scratch/diff.py` (mirrored in session scratchpad).
- **Installed mod ids**: parsed ONLY the `[[mods]]` table `modId` in each jar's `META-INF/neoforge.mods.toml`
  (546 jars; `[[dependencies]]` ignored). 401 declared mod ids.
- **Verdict floor**: content mod = adds items/blocks/mechanics a player experiences. Excluded libs, APIs,
  perf/client, map/UI, worldgen/structure-only, decor/furniture families, combat/rpg tweak systems, and
  ambient-mob-only mods. After exclusions: **100 content mods** classified.
- **Age assignment**: from live `kubejs/server_scripts/aoa_astages_*.js` locks where present (proof lines cited),
  else inferred from the preamble per-age legal-tech table.
- **Showpieces**: read each candidate jar's `assets/<modid>/lang/en_us.json` + recipe/model trees. All ids below
  are copied from jar lang, not guessed.

### Prior art
`docs/audits/quest_coverage/` referenced in memory **does not exist** on disk (checked
`docs/audits/` — no coverage matrix/report present). Built fresh.

### Two data-quality corrections found during the pass
1. **`hybrid_aquatic` is NOT a gap.** Its asset namespace is `hybrid-aquatic` (hyphen). A strict underscore
   regex reports 0, but loose grep shows it is covered across `m3_relics_and_burrows.snbt` (4 refs) and
   `g6_circuits_and_current.snbt` (18 refs) — diving suit, hooks, coral gear, crab pot, pearls. This is the
   ocean "Living Harvest" layer. **Verdict OK.** (Only hyphenated namespace in the pack.)
2. **`railways` (Create: Steam 'n' Rails) is a real gap even though a rail chapter exists.**
   `ren_second_mill_steam_rail_logistics.snbt` references only `createrailwaysnavigator:` (the display/navigator
   addon), never `railways:` — so trains, couplers, gauge track, and signals have no task despite the chapter.

---

## Coverage summary

| Bucket | Count |
|---|---|
| Content mods classified | 100 |
| ZERO coverage | 13 |
| UNDER (1–5 refs) | 19 |
| OK (>5 refs) | 68 |

Non-content ZERO/near-zero stragglers confirmed excluded via jar-lang inspection:
`advancement_portals` (2 items), `aether_emissivity` (0), `allthecompatibility` (0), `configured` (0),
`create_ultimate_factory` (recipe-only pack, registers **zero** items — never quest a `create_ultimate_factory:` id),
`the_afterdark` (only a teleport block + catalyst in this build; dimension gate at otherworldly but no gear/boss),
`variantsandventures` (4 ordinary biome mob variants only).

---

## FOMO shortlist — uncovered / under-covered content mods

Verdict key: **ZERO** = no task at all; **UNDER** = 1–5 refs, likely a stray reward not a real quest home.
"Age" = plausible chapter age from AStages lock (cited) or preamble table.

| Mod | Refs | Verdict | Age (proof) | Showpieces a player would regret missing |
|---|---|---|---|---|
| **relics** | 0 | ZERO | the_renaissance (`aoa_astages_01p_gap_closure.js:454` `["the_renaissance","relics:reflective_necklace","relics"]`, 26 locks) | Ring of the Seven Deadly Sins (endgame trinket); Mantle line (`midnight_mantle`/`ghostly_mantle`/`glitchy_mantle` — phase/decoy back-slot); `chorus_staff` (blink); `kinetic_belt` (speed→chain-lightning); `shield_of_retaliation` (reflect). Level-up trinket system — its own showcase. |
| **artifacts** | 0 | ZERO | the_renaissance (curios accessories; unstaged — set at Ren w/ Neo Vitae magic tier) | `cloud_in_a_bottle` (double-jump); `helium_flamingo` (air ascent); `vampiric_glove` (lifesteal); `power_glove`+`feral_claws` (melee dmg/speed); `antidote_vessel`; the `mimic` chest ambush mob. |
| **psi** | 4 | UNDER | industrial_revolution (`aoa_astages_01m_magic.js:110` `["industrial_revolution","psi:programmer","block_item"]`) | Spell Programmer + CAD Assembler (write spells as data-flow programs); the CAD wand progression (`cad_core_*` Basic→Radiative); `spell_bullet` delivery family; `psimetal_exosuit` auto-cast armor; psimetal tools. Deep, unmistakable — chapter-worthy. |
| **spell_engine** | 0 | ZERO (but framework) | medieval_times (`aoa_astages_01_item_restrictions.js:1280` `["medieval_times","spell_engine:spell_binding","block_item"]`) | Spell Binding Table + Spell Book (9-slot spell hotbar) + Spell Scroll. NOTE: it's the casting **runtime**; spells come from partner mods. Quest the table/book, not spells. |
| **railways** | 0 | ZERO | the_renaissance (`aoa_astages_01g_create_family.js:120` `["the_renaissance","railways:semaphore","block_item"]`) | Knuckle/Screwlink couplers (multi-carriage trains); narrow+wide gauge track/bogeys; Brass Track Switch + semaphore + conductor whistle (signaling); handcar. Fold into the existing Second Mill rail chapter. |
| **create_sa** | 0 | ZERO | Create tier (`aoa_astages_01g_create_family.js`, 1 lock) | Jetpack tiers (andesite→netherite) + Exoskeleton tiers; `flamethrower`; brass drone + `drone_controller`; `grapplin_whisk`; `portable_drill`. ⚠ Jetpacks/propellers hit the **CANCELLED flight-gating** decision (P3) — flight gear stays ungated; quest the drone/drill/flamethrower instead. Lang has junk tooltip strings ("poulet","gay"). |
| **create_dragons_plus** | 0 | ZERO | industrial_revolution (`aoa_astages_01_item_restrictions.js:665` `["industrial_revolution","create_dragons_plus:blaze_upgrade_smithing_template","item"]`); Aether/End content leans Renaissance | Bulk Enchanting (fan + Golden Aercloud auto-enchants/repairs); Bulk Ending (`fan_ending`, Dragon Head catalyst → End variants); Fragile Fluid Tanks (throwable explosive/lava/dragon-breath); `dragon_breath` fluid; Blaze Upgrade template. |
| **alexsmobs** | 2 | UNDER | mixed (unstaged; gear gated by mob drop — place per source biome/dimension) | `tarantula_hawk_elytra` (elytra alt); `dimensional_carver` (Void Worm apex teleport tool); armor sets (crocodile/rock-shell/froststalker/moose); `skelewag_sword`/`tendon_whip`/`hemolymph_blaster`; `echolocator`/`endolocator` locators; `transmutation_table`; `animal_dictionary`. Deep drop-gated gear — under-served at 2 refs. |
| **mm_farming** | 0 | ZERO | industrial_revolution (`aoa_astages_01_item_restrictions.js:680` `["industrial_revolution","mm_farming:block_controller_system","block_item"]`) | System/Input Controller multiblock; Plant/Tree/Garden Farm Controllers + Farm Crafter; tiered Speed/Fertilizer upgrades (World→Nether→Ender→Creative). Genuine compact auto-farm system, not decor. |
| **arcanelanterns** | 2 | UNDER | the_renaissance (magic tier; unstaged — 0 AStages locks, place with Ren magic) | Lantern Maker (fusing station); `life_lantern` (crop growth); `brilliant_lantern` (animals→XP); `containing`/`warding_lantern` (mob control); `withering`/`boreal_lantern` (area traps). Whole mod is functional effect-lanterns from one station. |
| **zoniex** | 0 | ZERO | the_renaissance (`aoa_astages_01p_gap_closure.js:483` `["the_renaissance","zoniex:deathly_heart","zoniex"]`, 11 locks) | Skin Crawler summon (centerpiece encounter w/ Block Shockwave); `staff_of_the_undying`; `whiplasher` whip; `deathly_heart` (totem/revive-tier drop); tameable Blood Eagle mount. Horror/gore combat set. |
| **sliceanddice** | 5 | UNDER | medieval_times (`aoa_astages_01_item_restrictions.js:685` `["medieval_times","sliceanddice:slicer","block_item"]`) | Slicer (Create-powered auto-harvest/replant); Sprinkler + Liquid Fertilizer trio. Already touched (P4 additive nodes) — near-covered. |
| **create_integrated_farming** | 2 | UNDER | medieval_times (`aoa_astages_01_item_restrictions.js:650` `["medieval_times","create_integrated_farming:fishing_net","block_item"]`) | Roost (passive breeding, chicken/duck/goose); Fishing Net; Lava Fishing Net (Nether-tier twist). Shallow — branch, not chapter. |
| **crittersandcompanions** | 2 | UNDER | ambient/early (unstaged) | `grappling_hook` (traversal — standout); tiered `dragonfly_armor` barding; `silk_lead` from farmed silk; pearl curio. Mostly food/decor otherwise; branch-sized. |
| **mekanismadditions** | 0 | ZERO (mostly decor) | industrial_revolution (Mekanism tier; unstaged) | Walkie-Talkie (comms); Obsidian TNT (obsidian-piercing); tethered lifting Balloons. Real payload is Plastic Blocks/Glow Panels = decor. Only 3 quest-worthy items — low FOMO. |
| **integratedterminals** | 0 | ZERO | industrial_revolution (Integrated Dynamics is covered at 20; IR tier) | Portable Storage Terminal + ID network terminals. Small; fold into the existing Integrated Dynamics/digital-logistics coverage. |
| **interdimensionalwirelesstransmitter** | 0 | ZERO | otherworldly (`aoa_astages_01_item_restrictions.js:689` `["otherworldly","interdimensionalwirelesstransmitter:black_interdimensional_wireless_transmitter","block_item"]`) | Single block: infinite-range + cross-dimensional wireless storage terminal. One high-tier convenience node, not a chapter. |
| **projectred_exploration** | 0 | ZERO (mostly variants) | industrial_revolution (ProjectRed covered at 16+15; IR tier) | Ruby/Sapphire/Peridot gem gear + Saws + colored Backpacks + silver/tin ores. Almost all variant gear/ore — low FOMO; ProjectRed already has a quest home. |
| **actually_division** | 0 | ZERO (variant gear) | industrial_revolution (Actually Additions tier) | Actually Additions crystal gear re-add: Palis/Restonia/Enori/Diamatine/Void/Emeradic crystal armor + AIOT tools. Almost pure variant gear — **skip per no-variant-quest rule**. |
| **create_ultimate_factory** | 0 | N/A (recipe-only) | — | No items. Adds Create recipes producing vanilla outputs. Never a task-item source. Leave. |

---

## Age-cluster read (where the gaps concentrate)
- **Renaissance** is the heaviest under-served band: `relics`, `artifacts`, `zoniex`, `arcanelanterns`,
  `create_dragons_plus` (Aether/End), and the `railways` train layer all land here. A Renaissance trinket/relic
  branch + folding trains into the Second Mill chapter would close most of it.
- **Industrial Revolution** has real automation gaps: `psi` (chapter-worthy), `mm_farming`, `integratedterminals`.
- **Otherworldly**: `interdimensionalwirelesstransmitter` (single convenience node).
- **Medieval**: `spell_engine` table/book, `create_integrated_farming`, `sliceanddice` (near-done).

## Respected user decisions (not flagged as gaps)
`createnuclear` / `createoreexcavation` / `powergrid` = leave alone. Flight (`immersive_aircraft`,
`immersive_machinery`, `createpropulsion`, and `create_sa` jetpacks) stays unquested/ungated. `ftboceanmobs`
being dropped. Removed mods (phantasm, luminous_nether, gardens_of_the_dead) not present. `hybrid_aquatic`
already covered (Living Harvest).
