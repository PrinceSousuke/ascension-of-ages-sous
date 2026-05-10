# Quest Source Audit

## Purpose

This file maps planned AoA quest chapters to:

- live `test5` systems and mods
- reference chapters from `Age of Fate (1)`
- reference chapters from `All the Mods 10`
- explicit AoA-original authoring needs

This audit is written against the current live `test5` mod set and overrides older exports when they disagree with the instance.

## Live Pack Corrections

- `Advent of Ascension` is removed and must not receive quest chapters.
- `Oritech` is present and should be split across a major Automation backbone and a later Industrial escalation branch.
- `Modern Industrialization` is present and should be treated as a major Industrial Age branch.
- `Nuclear Age` is now the required bridge between `Industrial Age` and `Space Age`.
- `Mekanism` and related hazardous-power / strategic-tech content should no longer be treated as a generic Space bucket.
- `Stellaris` is installed and remains the current front-runner for Space ownership, but the future off-world owner should stay planning-flexible until the dedicated launch pass.
- Existing quest content for `Minecolonies` and `When Dungeons Arise` already exists and should be isolated under `Annexes`.
- `Journey Into The Light` is installed in the live pack and now shares a live Expedition first-contact branch with `DivineRPG`, while the fuller RPG escalation family still belongs later.

## Architecture Authority

Use `age_domain_boss_architecture.md` as the source-of-truth for:

- age boss-spine ownership
- boss classification
- chapter unlock surfaces
- age domain quotas
- cluster family placement
- late-game boss sequencing

Use `late_game_redesign_structure.md` as the source-of-truth for:

- Industrial -> Nuclear -> Space age boundaries
- late-game mod placement
- late-game chapter ownership
- late-game boss / capstone recommendations

This file stays focused on mapping live systems and reference sources into that architecture.

## Reward Registry Source Anchors

Reward framework files:

- [`reward_registry_framework.md`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/reward_registry_framework.md)
- [`reward_registry_ids.json`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/reward_registry_ids.json)

Reward ecosystem anchors should stay tied to live installed clusters rather than generic loot pools:

- Stone/Mechanical survival and workshop: Farmer's Delight, Aquaculture, Ocean's Delight, Create, Immersive Engineering, Sophisticated Storage/Backpacks
- Expedition outward support: Ars Nouveau, Apotheosis, Artifacts, Relics, AE2, Refined Storage (optional), NauTec, Small Ships, Nether expedition clusters
- Industrial specialization: Oritech, Modern Industrialization, Industrial Foregoing, Hostile Neural Networks, PneumaticCraft, Integrated Dynamics, TFMG
- Nuclear hazard campus: Mekanism, Nuclear Science, Ballistix, Electrodynamics, Dynamic Electricity, Applied Mekanistics
- Space/Ascension convergence: Stellaris (space-owner-flexible), ProjectE, Dyson Cube Project, Re-Avaritia

## Stone Age

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Awakening and Salvage | Minecraft, Legendary Survival Overhaul, Serene Seasons | AoA current scaffold only | AoA-original survival opener |
| Tools, Materials, and Binding | Minecraft, TreeChop, primitive survival loop | ATM10 `mainquestline_part_1` for dependency density | Rewrite completely for AoA |
| Water, Shelter, and Wounds | LSO, Serene Seasons, campfire/furnace loop, shelter lighting, injury care | AoA current scaffold only | AoA-original merged onboarding arc; Stone hydration, shelter heat, injuries, and reserve prep now teach one survival loop |
| Food and Seasonal Stability | manual crop loop, season awareness, early food reliability, backup food | AoA current `stone_food_and_farming_pressures`, AOF `basic_agriculture`, `farming`, `aquaculture` | Stone food/farming arc now focuses on stability after water/temperature lessons moved back into the opener |
| Travel and Controlled Combat | route prep, structure entry discipline, early combat readiness and recovery | AoA current `stone_travel_and_controlled_combat`, ATM10 `building_tips`, AOF `when_dungeons_arise` | Merged travel/combat arc with clearer progression bridge to iron readiness |
| Treasure and Lock Tiers | Clavis, loot/treasure plan, structure scouting | AoA current treasure text | AoA-original |
| Entering the Mechanical Age | Minecraft iron threshold, stage grant | AoA current `entering_the_iron_era` | Live gate now checks Stone survival-readiness capstones plus stable travel supplies, without leaking iron early |
| Stone Age Boss Hunts | early bosses and validators | boss export only | AoA-original |

## Mechanical Age

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Ironwork and Workstations | Minecraft iron loop, iron tools, utility benches, bounded IE handwork prep | ATM10 `mainquestline_part_1` | AoA-original rewrite; includes early iron canteen utility handoff plus starter Immersive Engineering hand tools/parts |
| Create Foundations | Create | AOF `create`, ATM10 `create` | Strong reference chapter |
| Rotational Power and First Logistics | Create rotational entry, stress awareness, belt/funnel/chute transport backbone | AoA current `mechanical_rotational_power_and_first_logistics`, AOF `create` | Live bounded starter chapter between foundations and broader Mechanical branches |
| Mechanical Food and Farm Handling | Create crop loop starter, contraption offload, first grain processing, Multiblock Farming tree-lane prerequisites | AoA current `mechanical_food_and_farm_handling`, AOF `create` | Live merged farm + tree handling chapter now tracks real farm-crafter and upgrade prerequisites, with tree setup branching from portable storage and ending in first mechanical saw wood processing |
| Create Food Relief | Create, Create Integrated Farming, Slice and Dice, Farmer's Delight, Cooking for Blockheads | AOF `create`, AOF `farming`, ATM10 `food_and_farming` | Live kitchen synergy chapter now includes knife -> straw -> safety-net/canvas support before fishing nets, roosts, stove, sink, and fridge |
| Engineer's Handwork | Immersive Engineering, Create handwork overlap | AOF `immersive_engineering` | Live bounded workshop utility chapter; teaches the honest Coke Oven, treated wood, workbench, wire, connector, and starter conveyor path |
| Workshop Logistics and Storage | iron chests, sophisticated storage, sophisticated backpacks, hopper routing | AOF `storage`, ATM10 `storage` | Live pre-digital storage line now uses honest barrel + backpack-upgrade utility instead of minecart filler |
| Early Utility Machines | Create Additions connectors/spools/capacitors/rolling mill, Generator Galore starter generators/upgrades, Botany Pots compact crop support | AoA current `mechanical_early_utility_machines`, ATM10 `basic_power` | Live bounded utility chapter; keeps Mechanical focused on practical workshop relief rather than full industrial grids |
| Mechanical Dungeon Readiness | shield-first loadout, armor/rations fallback, Apotheosis affix contact, Artifacts find proof, Relics worktable contact | AoA current `mechanical_dungeon_readiness`, ATM10 `basic_armor`, AOF `adventurers_lodge` | Live bounded combat-prep branch tied to workshop maturity and travel-return safety |
| Expedition Threshold | Minecraft diamond threshold, stage grant | AoA current `diamond_threshold` | Mechanical gate chapter; now anchored to real Mechanical capstones and a stocked workshop, without leaking diamonds early |
| Mechanical Age Boss Hunts | Aether entry + bronze/silver dungeon progression, Twilight hunter + naga/lich progression, optional BOMD gauntlet follow-up | AoA current `mechanical_age_boss_hunts`, boss export, Twilight/Aether references | Live boss-validation branch now reads as prepared destination combat, not random trophy collection |
| Minecolonies Bridge | Minecolonies, Minecolonies Questline | existing AoA chapter plus imported content | Connector only, not mainline |

## Expedition Age

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Diamonds and Branch Unlocks | diamonds, enchant entry, better gear | AoA current `diamonds_and_branch_unlocks`, ATM10 early mainline | Live Expedition opener and branch signpost, separate from the Industrial gate; now includes an Ars setup-supplies bridge |
| Enchanting and Apotheosis Entry | enchanting table activation, shelf prep, first practical enchant, Apotheosis growth marker | AoA current `expedition_enchanting_and_apotheosis_entry`, AOF `apotheosis` | Live bounded starter chapter before the full Apotheosis branch |
| Enchanting and Apotheosis Follow-Up | practical enchant upgrades, first gem integration, readiness handoff | AoA current `expedition_enchanting_and_apotheosis_followup`, AOF `apotheosis` | Live bounded second layer; mythic and deeper optimization deferred for later progression |
| Ars Nouveau | Ars Nouveau | AOF `ars_nouveau`, ATM10 `ars_nouveau` | Live bounded Expedition starter chapter is now implemented; deeper Ars expansion remains planned |
| Apotheosis and Enchanting | Apotheosis, Apothic Enchanting, Apothic Attributes | AOF `apotheosis`, ATM10 `apotheosis_2`, `apothic_enchanting` | Expedition power branch |
| Storage Uplift | Sophisticated Storage tiering and practical storage discipline before digital networks | AoA current `expedition_storage_uplift`, AOF `storage`, ATM10 `storage` | Live starter scaffold focuses chest-tier progression to diamond; netherite deferred until Automation age |
| Refined Storage Entry | Refined Storage + RSRequestify optional convenience lane | AoA current `expedition_refined_storage_entry`, AOF `refined_storage` | Live optional chapter only; no gate ownership and no mainline dependency ownership |
| Aether and Twilight First Destinations | first destination routing, pre-entry prep, first benchmark drops | AoA current `expedition_aether_twilight_first_destinations`, AOF `the_aether`, AOF `the_twilight_forest` | Live bounded starter chapter is now optional support content in a tech-first flow; deeper boss rewards and harder encounters deferred to later progression |
| Nautec Underwater First Contact | ocean salvage, diving prep, air handling, first catalyst, repaired chip utility | AoA current `expedition_nautec_underwater_first_contact`, Nautec guidebook getting-started entries | Live bounded underwater branch; now extends into repaired salvage and first monocle utility while staying focused on Expedition exploration and adaptation rather than full chemistry or augmentation ownership |
| Nether Entry and Route Survival | Nether portal entry, piglin-safe footing, glowstone return stock, magma-cream fire planning, strider travel | AoA-original | Live Nether opener so first Nether trips feel like a route-planning and survival phase instead of one blaze errand |
| BetterNether Materials and Adaptation | BetterNether reeds, Cincinnasite shard/ingot/forge line, Nether Ruby, first local gear payoff | AoA-original | Live BetterNether branch now gives Expedition a real local-material payoff before Automation takes over larger Nether ore and factory loops |
| Fortresses and Hellish Trials | fortress wart routing, Hellish Trials combat proof, EternalNether warped-ender-pearl and withered-bone proof, Catacomb structure contact, rib-trim treasure proof | AoA-original | Live Nether structure-combat branch now folds in EternalNether as a real Expedition owner instead of deferring it out of the phase |
| Luminous Nether Hunts | Ash Forest contact, Piglin Executioner proof, Basalt Executioner late hunt | AoA-original | Live Luminous Nether branch now supplies late-Nether hunt pressure and one harder follow-through, but it no longer owns the final move-on gate |
| Nether Gauntlet Conquest | BOMD Gauntlet arena contact, Gauntlet defeat, Blazing Eye payoff | AoA-original | Live BOMD capstone chapter now provides the final Expedition move-on gate through a clearer and more findable Nether boss structure |
| DivineRPG and JITL First Contacts | DivineRPG + JITL guidebooks, overworld ores, first practical tools, bounded stockpile prep, first portal-frame readiness, and the first boss-linked unlock surface | AoA original Expedition RPG first-contact integration arc | Live bounded RPG branch now uses guidebook setup, overworld material contact, first Realmite/Rupee/Sapphire payoffs, DivineRPG stockpile blocks, JITL frozen portal frames, and the Rockite Smasher's Journey Key to open one controlled follow-through layer without opening full portals, late bosses, or full realm ladders |
| Aether and Deep Aether | Aether, Deep Aether | AOF `the_aether` | Dimension branch |
| Twilight Forest | Twilight Forest | AOF `the_twilight_forest`, ATM10 `twilight_forest` | Dimension branch |
| Undergarden First Contact | The Undergarden first-contact utility, first metal proof, and lead support | AoA current `expedition_undergarden_and_deeper_frontiers`, AOF `the_undergarden` | Live bounded dark-frontier contact chapter now includes goo-ball and lead utility; Deeper and Darker remains planning-only |
| Small Ships and Water Routes | Small Ships, chest boats, route-role hulls, and better water-route cargo travel | AoA original Expedition travel-tech branch | Live bounded Expedition travel-tech chapter; sail -> cog -> brigg -> drakkar/galley gives outward water routes a real utility payoff and uses Undergarden lead support instead of standing alone |
| Treasure Routes and Clavis II | Clavis, better treasure structures, loot routing | AOF `treasures_artifacts`, AOF `when_dungeons_arise` | AoA-original |
| Blaze Breakthrough | nether/blaze threshold and branch proof | AoA current `blaze_breakthrough`, progression exports, and AoA gate policy | Blaze now remains a mandatory Nether branch proof and workshop-enabler, while the Automation Age stage grant belongs to the Nether Gauntlet conquest surface |
| Expedition Boss Hunts | Aether, Twilight, Undergarden, Warden-tier validators | boss export | AoA-original |
| WDA Bridge | WDA questline content | existing AoA `when_dungeons_arise` | Connector only |

## Automation Age

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Nether Logistics and Ore Escalation | blaze, nether prep, ore throughput | ATM10 `basic_logistics`, AOF `the_nether` | First Automation bridge chapter |
| Oritech | first powered processing, machine chaining, starter throughput | ATM10 `oritech` | Live Automation backbone |
| Factory Logistics | conveyors, transport, drawers, logistics blocks | ATM10 `basic_logistics`, `storage` | Automation support branch |
| Power Grids | starter industrial power, wiring, buffers | ATM10 `basic_power`, AOF `extreme_reactors` | Automation support branch only; fuller reactor-scale ownership now belongs in the new Nuclear bridge |
| Automation Age Boss Hunts | machine-age combat validators and Industrial-opening capstone | boss exports + age-domain architecture | Live Automation boss spine. It now turns End-ready factory ownership into the real Industrial Age gate through Obsidilith, Ancient Factory routing, Ender Golem, and Ender Guardian |

## Industrial Age

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Oritech Escalation | later Oritech throughput, denser machine payoff | ATM10 `oritech` | Industrial split branch after the Automation starter chapter |
| Modern Industrialization | Modern Industrialization, Extended Industrialization, Modern Dynamics, MI Sound Addon | ATM10 `mi_steam`, `mi_electric`, `mi_digital`, `mi_endgame` | Core Industrial pillar. Live starter arc already covers forge hammer, bronze, boiler, first steam machines, pipe support, and first steel; later electric and digital MI remain planned inside this age |
| Create Process Infrastructure | Create, Create Additions, Create New Age, Create Metalwork, Create Oritech Compat, Assembly Line | AoA-original industrial Create support arc | Industrial physical-infrastructure bush: mechanical crafting, fluid tanks/pumps, spouts, energising, heat pipes, powered heaters, rolling mills, and electric-bridge support |
| Petroleum and Extraction | TFMG, Create Ore Excavation, Railways, Create | AoA-original industrial petroleum and extraction integration arc | Shared oil and extraction backbone for PneumaticCraft and later hazardous tech; this stays in Industrial instead of being duplicated later |
| Industrial Foregoing | Industrial Foregoing, Industrial Foregoing Souls | AOF `industrial_foregoing`, ATM10 `industrial_foregoing` | Applied-automation pillar for latex, plastic, dissolution, farm utility, and the later handoff into HNN and synthesis |
| PneumaticCraft | PneumaticCraft, Applied Pneumatics | ATM10 `pneumaticcraft`, live recipe audit against `pneumaticcraft-repressurized-8.2.19+mc1.21.1` and `appliedpneumatics-1.0.8` | Live Industrial specialization branch. Uses explosion-crafted compressed iron as the real opener, then safe pressure control, refinery -> LPG -> plastic, pressure-chamber structure, and one bounded ME Pressure Interface payoff. Deeper PCB/assembly and later Applied Pneumatics temperature/storage tools stay deferred. |
| Integrated Dynamics | Integrated Dynamics, Integrated Tunnels, Integrated Crafting, Integrated Terminals | ATM10 `integrated_dynamics`, live recipe audit against `integrateddynamics-1.32.3`, `integratedtunnels-1.9.4`, `integratedcrafting-1.4.5`, and `integratedterminals-1.6.28` | Live Industrial control-and-policy branch. Starts with Menril processing, then variables/cables/battery/transformers, then readers/writers and tunnels, then one bounded crafting + portable-terminal payoff. Attuned crafting and deeper terminal expansion stay deferred. |
| Hostile Neural Networks | Hostile Neural Networks, Hostile Neural Industrialization | AOF `hostile_neural_networks`, ATM10 `hostile_neural_networks` | Industrial starter arc only. First prediction loops belong here, but later synthesis ownership belongs in Space |
| Dragonfall and End Access | industrial readiness proof, End access, Dragonfall, outer-End follow-through, Ancient Factory routing, The Harbinger | progression exports + Cataclysm advancement chain | Live Industrial -> Nuclear gate. Mature factory branches now feed a real conquest bridge that grants `nuclear_age` only after post-dragon scale and The Harbinger are defeated |
| Industrial Boss Hunts | Cataclysm, Alex's Caves, Ice and Fire | AOF `cataclysm`, ATM10 `cataclysm`, boss export | Live Industrial branch-boss spine. Burning Arena -> Netherite Monstrosity, Forlorn Hollows -> Forsaken, and one dragon-scale hunt now prove factory-backed conquest after Create process, petroleum, Industrial Foregoing, Hostile Neural Networks, PneumaticCraft, and Integrated Dynamics have all matured the campus |

## Nuclear Age

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Containment Protocols | hazard discipline, shielding mindset, sealed-facility setup | `late_game_redesign_structure.md` | Live Nuclear opener now correctly sits behind `nuclear_age` and uses hazmat gear, shielding, scrubbers, waste handling, and the first Nuclear Science extraction/separation tools |
| Mekanism Processing and Chemicals | Mekanism, Additions, Tools, MoreMachine, compat | ATM10 `mekanism` | Live hazardous-processing pillar. Rehomes the main Mekanism bridge out of Space and starts the real gas/slurry/chemical campus |
| Reactors, Isotopes, and Hazardous Power | Mekanism Generators, Nuclear Science, Extreme Reactors, Create New Age reactor support | ATM10 `mekanism_reactors`, AOF `extreme_reactors` | Live reactor-campus pillar for hazardous power and isotope infrastructure, now with fission, reactor logic, Nuclear Science heat handling, and first turbine proofs |
| Strategic Power and Hardened Grids | Electrodynamics, Dynamic Electricity, Generator Galore, Create New Age, Nuclear Science support | `late_game_redesign_structure.md` | Live hardened-grid branch for dangerous facilities. Now covers transformer control, monitored substations, reserve buffering, backup generation, power conversion, reactor-service gas support, and quantum-capacitor campus relays before strategic-force escalation |
| Defense Systems and Strategic Force | Ballistix, Mekanism Turrets, Mekanism Lasers, Modular Force Fields, Evolved Mekanism | `late_game_redesign_structure.md` | Live military / defense pillar. It now covers hardened-grid stock, radar, perimeter turrets, laser hardware, tier-one launch systems, force-field geometry, and dense-energy backing |
| Chemical Storage and Digital Bridges | Applied Mekanistics, RS Mekanism Integration, Mekanism Covers, AE2, RS | `late_game_redesign_structure.md` | Live hazardous logistics bridge so gases and chemical inventories are taught before Space-scale networking through AE2 chemical cells, entangloporters, covered routing, and bounded RS chemical storage |
| Space Launch Threshold | final Nuclear gate | progression exports + `late_game_redesign_structure.md` | Planned Space connector. It should consume the now-live reactor, hardened-grid, strategic-force, hazardous-logistics, and boss-hunt proofs without hard-binding the final off-world owner in this pass |
| Nuclear Boss Hunts | Alex's Caves and Cataclysm hazardous-world / war-machine threats | boss export + `late_game_redesign_structure.md` | Live Nuclear boss spine. A prepared strike kit now leads into Nucleeper, Magnetron, and Netherite Monstrosity as the first hazardous validator chain before launch authority |

## Space Age

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Launch Infrastructure and Stellaris | rockets, oxygen, stations, first off-world travel | Stellaris guidebook and recipes | Provisional Space mainline scaffold. Stellaris is the current front-runner off-world owner, but the live Nuclear pass stays compatible with a later owner swap or hybrid launch model |
| Orbital Life Support and Logistics | oxygen distribution, remote base support, return routing | Stellaris guidebook and recipes | Support branch so off-world play feels operational instead of one rocket craft |
| Advanced Storage and Digital Networks | AE2, AdvancedAE, ExtendedAE, Mega Cells, RS | AOF `applied_energistics`, ATM10 `applied_energistics_2`, `extended__advanced_ae` | Late digital branch. Full network scaling now belongs after launch and Nuclear hazardous logistics |
| Ender IO Networks | Ender IO, Immersive Energistics | AOF `ender_io` | Space utility branch for conduit-scale remote infrastructure |
| Antimatter and Cosmic Refinement | late Mekanism and chemical/digital synergy | ATM10 `mekanism_reactors` | Space keeps late Mekanism follow-through such as antimatter-scale refinement, not the whole Mekanism ladder |
| Late-Game Agriculture and Synthesis | Mystical Agriculture, Agradditions, IF, HNN, Solar Flux | AOF `mystical_agriculture`, ATM10 `elmystical_agriculturerr` | Must stay late; Space owns off-world resource synthesis and photovoltaic scaling |
| Draconic Evolution | Draconic Evolution, Draconic Additions | AOF `draconic_evolution`, ATM10 `draconic_evolution` | Space-to-Ascension pillar with reactor, chaos, and draconic combat pressure |
| Ascension Threshold | prestige unlock routing | progression exports | Connector |
| Space Boss Hunts | Draconic, Cataclysm, BOMD, other post-launch validators | boss export | Space boss spine |

## Ascension

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Entry and Scale Shift | prestige transition | AoA-original | Sets final tone |
| Prestige Crafting | Extended Crafting, Modular Machinery Reborn, Modular Machinery Reborn Mekanism | AOF `extended_crafting`, ATM10 star-era patterns | Main fabrication backbone for the final age |
| ProjectE Exchange Ethics | ProjectE | progression exports only | Must remain late |
| Dyson Cube Project | Dyson Cube Project | progression exports only | Major capstone branch |
| Avaritia Capstones | Re-Avaritia / prestige components | progression exports only | Major capstone branch |
| Ascension Boss Hunts | Geburah path and alternate final validators | boss exports, progression design bible | AoA-original |

## Annexes

| AoA Chapter | Live Systems | Primary References | Notes |
| --- | --- | --- | --- |
| Annexes Index and Signposting | questbook routing | existing AoA book | New authored guide chapter |
| Minecolonies Prologue | Minecolonies | existing AoA `minecolonies` chapter | Bridge only |
| Minecolonies Supply Chain | Minecolonies + mainline resource loops | existing AoA `minecolonies` chapter | Bridge and redirection only |
| WDA Expedition Guide | WDA structures and routing | existing AoA `when_dungeons_arise` chapter | Bridge only |
| Structure Route Planner | WDA + treasure loops + waystones | AOF `when_dungeons_arise`, `treasures_artifacts` | New authored guidance |
| Side Systems and Optional Tracks | optional branches and off-mainline utility | ATM10 `tips_and_tricks`, AOF `random_but_useful_stuff2` | AoA-original |
| Retrospective and Redirects | reroute players back into the spine | AoA-original | Connector and cleanup chapter |

## Explicit Exclusions

- `Advent of Ascension`
- any source chapter for mods not present in live `test5`
- any source chapter whose reward style would bypass AoA stage identity without a rewrite

## Existing Quest Files Kept but Reclassified

- [`minecolonies.snbt`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20%28test5%29_/config/ftbquests/quests/chapters/minecolonies.snbt)
  - keep as annex content
- [`when_dungeons_arise.snbt`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20%28test5%29_/config/ftbquests/quests/chapters/when_dungeons_arise.snbt)
  - keep as annex content

These chapters remain outside the authored quest count budget.
