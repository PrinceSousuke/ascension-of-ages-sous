# Quest Production Roadmap

## Purpose

This file turns the current quest cleanup work into a scalable production framework.

It answers three questions:

1. how the authored quest target reaches `2444` without filler
2. which ages and chapter classes carry that total
3. what the next `500-800` quests should actually be built around

## Budget Authority

Use this order when production numbers disagree:

1. `quest_design_bible.md`
2. `quest_chapter_plan.json` `group_targets`
3. `quest_production_tracker.csv`
4. per-chapter `quest_target` values
5. live SNBT file counts

## Architecture Authority

Age progression is now governed by:

1. `age_domain_boss_architecture.md`
2. `late_game_redesign_structure.md`
3. `quest_design_bible.md`
4. `quest_chapter_plan.json`
5. `quest_production_tracker.csv`

Use the boss-spine architecture when deciding:

- what each age must contain
- which boss chapter owns progression
- what unlocks a branch chapter
- whether a cluster is truly integrated

Important:

- the age-group budget is authoritative
- chapter targets are allowed to rebalance later
- do not solve local chapter ambitions by silently inflating the global authored total above `2444`

## Reward Framework Authority

Use this reward-framework order when reward planning files disagree:

1. `quest_design_bible.md` reward policy
2. `quest_ui_style.md` reward presentation rules
3. `reward_registry_framework.md`
4. `reward_registry_ids.json`
5. chapter-level implementation notes in `change_log.md`

Rules for upcoming reward assignment passes:

- use registry ids, not ad hoc one-off reward piles
- keep placement targeted per chapter pass (no silent whole-book assignment)
- use proof-symbolic rewards on progression gates and boss validators
- enforce age identity boundaries before applying any `T2+` cache

## Density Model

Use these chapter classes as the default production model:

| class | target size | use |
| --- | --- | --- |
| major arc | `20-40` quests | core survival, major tech, major magic, factory arcs |
| support / utility | `6-15` quests | bounded logistics, prep, synergy, convenience, support infrastructure |
| micro beat | `1-4` quests | utility mods or small support steps inside an existing chapter |
| gate | `3-8` quests | age transitions and threshold validation |
| boss / validator | `8-20` quests | readiness proof, challenge loops, age capstones |

If a chapter wants to exceed `40`, split it or explicitly phase it.

## Authored Quest Budget By Age

These are the authoritative authored quest budgets from the current plan:

| age | authored quest budget | share of total | role |
| --- | --- | --- | --- |
| Stone Age | `345` | `14.1%` | survival pressure, early routes, first iron threshold |
| Mechanical Age | `350` | `14.3%` | first real labor relief, workshop systems, pre-diamond maturity |
| Expedition Age | `385` | `15.8%` | tech-prep expansion, nether-fed logistics, selective exploration |
| Automation Age | `144` | `5.9%` | first real machine automation, routing literacy, and Oritech backbone |
| Industrial Age | `300` | `12.3%` | factory-campus maturity, metallurgy, petroleum, and serious scale-up |
| Nuclear Age | `260` | `10.6%` | hazardous power, reactors, containment, military tech, and chemical logistics |
| Space Age | `240` | `9.8%` | launch infrastructure, off-world logistics, advanced networks, and draconic escalation |
| Ascension | `220` | `9.0%` | prestige crafting and capstone progression |
| Annexes | `200` | `8.2%` | optional side systems and bridge content |
| Total | `2444` | `100%` | authored minimum target |

## Current Production Snapshot

Current live authored count is `538` quests across bounded scaffolds.

Current live backlog by age:

| age | budget | live authored now | remaining |
| --- | --- | --- | --- |
| Stone Age | `345` | `31` | `314` |
| Mechanical Age | `350` | `114` | `236` |
| Expedition Age | `385` | `148` | `237` |
| Automation Age | `144` | `69` | `75` |
| Industrial Age | `300` | `115` | `185` |
| Nuclear Age | `260` | `58` | `202` |
| Space Age | `240` | `0` | `240` |
| Ascension | `220` | `0` | `220` |
| Annexes | `200` | `3` | `197` |

Notes:

- `Stone`, `Mechanical`, and `Expedition` are structurally healthier than the later ages, but still far below their authored budget.
- Stone onboarding now uses one denser survival-basics chapter instead of splitting water and shelter into two shallow early files.
- Mechanical farm cleanup merged standalone tree-farming into the core farm-handling chapter to reduce shallow fragmentation.
- Mechanical kitchen and workshop cleanup now track real support systems: stove + sink + fridge for food relief, and storage barrel + backpack utility for workshop storage.
- Mechanical farming support now includes the real knife -> straw -> safety-net/canvas chain for Create Integrated Farming, and the tree line now teaches first automatic wood processing through a Mechanical Saw.
- `entering_the_iron_era` and `diamond_threshold` now use pre-tier readiness proofs instead of leaking raw iron or raw diamonds before the age boundary.
- Mechanical now has real live utility/readiness coverage through `mechanical_early_utility_machines`, `mechanical_dungeon_readiness`, and `mechanical_age_boss_hunts` in addition to the existing ironwork/farm/storage lanes.
- `mechanical_engineers_handwork` remains the bounded early Immersive Engineering support lane, giving Mechanical a truthful Coke Oven -> treated wood -> wiring workshop arc.
- `expedition_workshop_and_industrial_prep` is now a formal Expedition planning chapter and should be treated as the bounded tech-prep owner for the Nether return loop.
- Expedition now has a real Nether chapter group instead of a thin blaze checkpoint: `expedition_nether_entry_and_route_survival`, `expedition_betternether_materials_and_adaptation`, `expedition_fortresses_and_hellish_trials`, and `expedition_luminous_nether_climax` now turn the Nether into a full late-Expedition phase.
- `blaze_breakthrough` no longer owns the final move-on gate. Blaze now acts as a mandatory Nether branch proof, Luminous Nether provides the late hunt branch, and BOMD's Nether Gauntlet is the real final Expedition capstone that grants Automation.
- `expedition_aether_twilight_first_destinations` now has real first-contact utility from Aether, Deep Aether, and Twilight instead of reading like a travel stub.
- `expedition_storage_uplift`, `expedition_ae2_entry`, `expedition_ars_nouveau`, and `expedition_enchanting_and_apotheosis_followup` now have the first honest support pieces that make their branches feel usable instead of symbolic.
- `expedition_nautec_underwater_first_contact` is now live as the underwater Expedition branch, using salt water, ocean salvage, diving gear, air bottles, Aquatic Catalyst, repaired chips, and a first monocle utility step instead of treating Nautec like generic factory tech.
- `expedition_undergarden_and_deeper_frontiers` is now live as a bounded Undergarden first-contact chapter, now extended with goo-ball and lead utility while still stopping before infuser growth, deeper frontiers, and boss escalation.
- `expedition_rpg_first_contacts` is now live as a tightly controlled DivineRPG + JITL branch, now extended through bounded second-step readiness and its first real boss-linked unlock surface via the Rockite Smasher's Journey Key, while full realm ladders still stay deferred.
- `expedition_small_ships_and_water_routes` is now live as the first Expedition travel-tech branch, now extended with drakkar and galley follow-through so route support feels like real ship choice instead of decorative boat padding.
- `industrial_modern_industrialization` is now live as the first true Industrial Age arc, using the honest MI steam path instead of leaving Industrial empty after the Automation split.
- `industrial_create_process_infrastructure` is now live as the first dense Create-side Industrial support arc, pushing the base into mechanical crafting, fluid handling, energising, heat distribution, and electric Create machinery instead of isolated workshop blocks.
- `industrial_petroleum_and_extraction` is now live as the shared oil and anchored-extraction support arc, using TFMG pumpjacks and distillation plus Create Ore Excavation and Railways fuel handling to widen the factory footprint before PneumaticCraft opens.
- `industrial_industrial_foregoing` is now live as the first Industrial support arc attached to MI, using the honest latex -> plastic -> dissolution -> farm-loop path.
- `industrial_hostile_neural_networks` is now live as a bounded starter support arc attached to IF, stopping at the first prediction loop instead of pretending full loot fabrication is already online.
- `industrial_pneumaticcraft` is now live as the remaining major Industrial specialization branch, and it follows the real recipe path: explosion-forged compressed iron, safe pressure control, refinery-fed LPG, plastic output, a built pressure chamber, and one bounded Applied Pneumatics crossover. It consumes the shared petroleum backbone instead of opening a rival oil tree.
- `industrial_integrated_dynamics` is now live as the Industrial control-and-policy specialization, using the real Menril -> resin -> crystal -> variable -> reader/writer -> tunnels -> bounded crafting/terminal path instead of collapsing the stack into one cable craft or pretending it replaces AE2.
- pre-publish release fixes now block MineColonies from leaking obsidian or diamond rewards before `expedition_age`, remove the invalid Hydra trophy step from the first-destinations chapter, and hide the empty Ascension placeholder file.
- late-game targets now rise because `Nuclear Age` is a real inserted bridge, not a silent redistribution inside the old Space bucket.

## Late-Game Redesign Override

Use `late_game_redesign_structure.md` as the authority for everything after `Automation Age`.

Corrected late-game ladder:

- `Automation Age`
- `Industrial Age`
- `Nuclear Age`
- `Space Age`
- `Ascension`

Ownership correction:

- `Industrial` owns factory-campus maturity: MI, Create industrial support, petroleum, IF, PneumaticCraft, Integrated Dynamics, and bounded HNN.
- `Nuclear` owns hazardous escalation: Mekanism processing, reactors, isotopes, hardened grids, strategic force, and chemical logistics.
- `Space` owns launch and off-world infrastructure: the eventual off-world owner, advanced digital scale, Ender IO utility, antimatter-grade follow-through, late synthesis, and Draconic escalation.
- `Ascension` owns prestige convergence: Extended Crafting, Modular Machinery Reborn, ProjectE, Dyson Cube Project, and Re-Avaritia.

Late-game production should now follow this order:

1. deepen the live Industrial foundation without rewriting it
2. author the Nuclear age entry and its three required pillars
3. build the future off-world opener only after the Nuclear stack is complete and the final Space-owner decision is ready
4. hold ProjectE and full prestige convergence until Ascension

## Full-Pack Distribution

The `2444` total should be distributed like this:

| bucket | target range | purpose |
| --- | --- | --- |
| core spine | `1200-1300` | major progression, gates, main tech and magic arcs |
| support / synergy | `450-550` | storage, logistics, QoL, bounded support systems |
| optional side / dimension / annex | `250-350` | branches that deepen the pack without blocking the spine |
| boss / mastery / validator | `150-250` | capstones, challenge beats, post-branch proof |

This keeps the pack large without turning every mod into mandatory progression.

## Chapter Budget By Age

Use this chapter mix as the working production map:

| age | chapter budget model | production intent |
| --- | --- | --- |
| Stone Age | `5-6` dense core chapters, `2-3` side/support chapters, `1` gate, `1` boss | finish the missing opener/material/treasure arcs without re-fragmenting Stone |
| Mechanical Age | `5-6` major workshop/system arcs, `4-5` support branches, `1` gate, `1` boss, `1` annex bridge | deepen Create/IE/workshop maturity before diamond |
| Expedition Age | `5-6` major tech-prep arcs, `4-6` support/side chapters, `1` gate, `1` boss, `1-2` connectors | keep the age centered on nether-fed storage, prep, and industry setup |
| Automation Age | `2-3` major automation arcs, `2-3` support branches, `1` connector/gate | bridge expeditionary prep into first serious machine automation |
| Industrial Age | `4` major factory arcs, `4-5` support/specialization branches, `1` gate, `1` boss | factory-campus maturity, petroleum, metallurgy, control, and dragonfall pressure |
| Nuclear Age | `3` hazardous-tech pillars, `3-4` support/combat branches, `1` gate, `1` boss | reactors, containment, strategic force, hardened grids, and chemical logistics |
| Space Age | `3-4` major off-world arcs, `3-4` support branches, `1` gate, `1` boss | launch, orbital logistics, advanced networks, synthesis, draconic escalation |
| Ascension | `4` prestige arcs, `1` entry, `1` boss | short, dense, capstone-focused |
| Annexes | `5-6` connectors plus `1` index | optional but meaningful bridge content only |

## Expedition Completion Plan

Expedition is the immediate production target. It should become a medium-size tech-prep age, not an early exploration showcase.

Build order:

1. Deepen `expedition_workshop_and_industrial_prep`
   - target `18-24` quests
   - owner: `Minecraft + Create + Immersive Engineering`
   - role: blaze burner, mixer, treated wood, coke brick, quartz return, and first industrial materials handoff
2. Deepen `expedition_storage_uplift` and `expedition_ae2_entry`
   - make `AE2` the required current-age digital storage baseline
   - keep `Refined Storage + RSRequestify` as optional convenience support
3. Use the Workshop/Industrial Prep chapter as the bounded Nether logistics/material loop
   - quartz, blaze, soul-sand-adjacent routing, stockpiling, base return loops
   - this should explain why the Nether matters to a tech-first pack
4. Expand bounded IE setup in Expedition
   - treated wood, coke, wires, connectors, early workshop infra
   - still support-scale, not a full IE branch yet
5. Deepen magic only where it supports readiness or infrastructure
   - Ars and enchant/apotheosis can grow
   - keep text concise and task-driven
6. Keep exploration selective
   - `Aether/Twilight First Destinations` stays as a light support branch
   - `Undergarden` is now live only at first-contact scale
   - `Deep Aether`, `Twilight Forest`, and later dark-frontier expansion stay deferred until their outputs materially feed future progression

Expedition chapters that should stay central now:

- `diamonds_and_branch_unlocks`
- `expedition_storage_uplift`
- `expedition_ae2_entry`
- `expedition_ars_nouveau`
- `expedition_enchanting_and_apotheosis_entry`
- `expedition_enchanting_and_apotheosis_followup`
- `expedition_nautec_underwater_first_contact`
- `expedition_nether_entry_and_route_survival`
- `expedition_betternether_materials_and_adaptation`
- `expedition_fortresses_and_hellish_trials`
- `expedition_workshop_and_industrial_prep`

Expedition chapters that should stay lighter for now:

- `expedition_aether_twilight_first_destinations`
- `expedition_rpg_first_contacts`
- `expedition_small_ships_and_water_routes`
- `expedition_undergarden_and_deeper_frontiers`
- `expedition_treasure_routes_and_clavis_ii`
- `expedition_refined_storage_entry` (optional convenience)

Expedition chapters that should move later unless tech payoff is defined:

- `expedition_aether_and_deep_aether`
- `expedition_twilight_forest`
- `expedition_boss_hunts`

## Automation To Space Ladder

Automation is now a distinct age, not a vague early-Industrial blob. Expedition should feed into it directly, and the late-game ladder should continue through `Industrial -> Nuclear -> Space` instead of jumping straight from `Industrial` into a generic advanced-tech bucket.

Automation spine and support:

1. `industrial_nether_logistics_and_ore_escalation` `28`
2. `industrial_oritech` `32`
3. `industrial_factory_logistics` `44`
4. `industrial_power_grids` `40`

Industrial scale-up and specialization:

1. `industrial_oritech_escalation` `24`
2. `industrial_modern_industrialization` `52`
3. `industrial_create_process_infrastructure` `38`
4. `industrial_petroleum_and_extraction` `34`
5. `industrial_industrial_foregoing` `38`
6. `industrial_pneumaticcraft` `30`
7. `industrial_integrated_dynamics` `28`
8. `industrial_hostile_neural_networks` `24`
9. `industrial_boss_hunts` `16`

Nuclear hazardous bridge:

1. `nuclear_entry_and_containment_protocols` `24`
2. `nuclear_mekanism_processing_and_chemicals` `56`
3. `nuclear_reactors_isotopes_and_hazardous_power` `48`
4. `nuclear_strategic_power_and_hardened_grids` `32`
5. `nuclear_defense_systems_and_strategic_force` `34`
6. `nuclear_chemical_storage_and_digital_bridges` `26`
7. `nuclear_boss_hunts` `24`
8. `space_launch_threshold` `16`

Space launch and off-world mastery:

1. `space_launch_infrastructure_and_stellaris` `34`
2. `space_orbital_life_support_and_logistics` `24`
3. `space_advanced_storage_and_digital_networks` `36`
4. `space_ender_io_networks` `24`
5. `space_antimatter_and_cosmic_refinement` `30`
6. `space_late_game_agriculture_and_synthesis` `30`
7. `space_draconic_evolution` `26`
8. `space_boss_hunts` `20`
9. `ascension_threshold` `16`

Boundary rules:

- `Immersive Engineering` expands from Expedition prep into Automation support infrastructure, not into a competing first-factory spine.
- `industrial_nether_logistics_and_ore_escalation` owns the conversion from Nether return loot into repeatable factory materials and ore throughput.
- `industrial_oritech` is the first clear machine-processing and throughput spine.
- `industrial_factory_logistics` and `industrial_power_grids` are enabling support for first-line automation, not the whole late-game power story.
- `industrial_oritech_escalation` is the later Oritech branch after first automation literacy is already established.
- `industrial_create_process_infrastructure` should force larger mechanical-crafting layouts, fluid buffers, powered heat lines, and Create-side electric rotation before later industrial specializations spread wider.
- `industrial_petroleum_and_extraction` should own early crude-oil surveying, pumpjack structure, distillation, anchored extraction, and rail fuel handoff so later PneumaticCraft consumes one shared petroleum backbone instead of building a parallel oil ladder.
- `Modern Industrialization`, `Industrial Foregoing`, `PneumaticCraft`, `Integrated Dynamics`, and `HNN` belong to Industrial scale-up and specialization, not to the first automation tutorial.
- `Mekanism`, `Ballistix`, `Nuclear Science`, `Dynamic Electricity`, and strategic-defense tooling belong to `Nuclear Age`, not to Industrial and not to Space as a catch-all.
- the eventual off-world owner should own the actual Space opener, life-support loop, and first off-world logistics.
- advanced `AE2` scale, `Ender IO`, late Mekanism antimatter-grade follow-through, late synthesis, and `Draconic Evolution` belong after launch, not before it.
- `industrial_modern_industrialization` should start with forge hammer, bronze, steam machines, Modern Dynamics routing, and first steel before later electric or digital MI escalation.
- `industrial_industrial_foregoing` should open with latex, dry rubber, plastic, simple frames, and plant/biofuel utility before mob or pink-slime escalation.
- `industrial_pneumaticcraft` should open after the shared TFMG/Create petroleum line is online, using tagged crude-oil and LPG inputs instead of teaching a second oil-production identity.
- `industrial_hostile_neural_networks` should start with model setup and the first simulation loop; full loot fabrication and deeper synthesis should stay later.
- `blaze_breakthrough` should validate Expedition capstones first and use blaze loot as a required Nether branch proof, not as a substitute for missing branch completion or as the final move-on gate.

## Next 500-800 Quest Production Order

Use this order instead of more isolated cleanup passes:

1. finish Expedition tech-prep backlog
2. deepen AE2 starter flow and bounded IE prep, keep RS optional
3. expand truthful IE/Create support where it feeds the industrial on-ramp
4. deepen the Automation spine first, then build Industrial scale-up on top of it
5. only then widen optional dimension content again

## Tracker Rules

Use `quest_production_tracker.csv` after every bounded authoring pass.

Each pass must update:

- current live quest count
- target quest count
- status
- inbound links
- outbound links
- notes when a live chapter drifts outside the formal plan

The tracker is not optional. It is the control surface for preventing:

- underbuilt major mods
- overbuilt utility mods
- frontloaded early game count
- vague midgame and endgame plans

## Boss-Spine Governance

Future implementation must follow the boss-spine model in `age_domain_boss_architecture.md`.

Minimum policy:

- Stone is the exception: it should not use a mandatory boss-gated age completion surface
- every age from `Mechanical` onward gets one dedicated boss chapter
- boss nodes unlock sequentially
- each boss node unlocks branch packages elsewhere
- required branches must complete before the next boss or age main boss opens
- the age main boss defeat opens the next age group and its branch surfaces

Current architecture gaps that future passes must close:

- `stone_age_boss_hunts` should be repositioned as optional or preparatory content if it stays at all; Stone exit logic should remain non-boss and readiness-based
- `mechanical_age_boss_hunts` is now live as a bounded sequential validation spine; `expedition_boss_hunts` remains the next boss-spine conversion gap
- `automation_age_boss_hunts` is now live as the Automation -> Industrial gate, `dragonfall_and_end_access` is now live as the Industrial -> Nuclear Harbinger gate, and seven Nuclear bridge chapters are now live as the post-Industrial hazardous ramp
- `industrial_boss_hunts` is now live as the branch-boss package feeding Dragonfall, so the next late-game structural gap after Nuclear completion is still `space_launch_threshold`
- dark, ritual, celestial, and RPG cluster placement must follow the cluster map in `age_domain_boss_architecture.md` instead of ad hoc chapter expansion
