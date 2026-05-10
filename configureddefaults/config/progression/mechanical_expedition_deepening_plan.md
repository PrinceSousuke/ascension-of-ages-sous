# Mechanical + Expedition Deepening Plan

## Scope
- Freeze rule: preserve live/authored quests unless a gate, dependency, stage reference, or dead-end correction is required.
- This pass deepens Mechanical first, then prepares Expedition follow-through.
- Non-targets stay frozen: Stone structure, Iron gate philosophy, Industrial widening, Space/Ascension, broad boss-spine implementation.

## Current Live Coverage Recount

### Mechanical live clusters
- `mechanical_ironwork_and_workstations.snbt`: merged live backbone for iron workshop, starter Create literacy, and early IE handwork
- `mechanical_workshop_logistics_and_storage.snbt`: live workshop relief lane for Iron Chests, barrels, and backpack utility
- `mechanical_food_and_farm_handling.snbt`: live farm + tree + kitchen support lane

### Expedition live clusters
- `diamonds_and_branch_unlocks.snbt`: Expedition opener and branch release surface
- `expedition_storage_uplift.snbt`: bounded chest upgrade line
- `expedition_ae2_entry.snbt`: AE2 starter network baseline
- `expedition_refined_storage_entry.snbt`: optional RS line
- `expedition_enchanting_and_apotheosis_entry.snbt`: bounded enchanting entry
- `expedition_enchanting_and_apotheosis_followup.snbt`: bounded gem-cutting follow-up
- `expedition_ars_nouveau.snbt`: bounded apparatus entry
- `expedition_aether_twilight_first_destinations.snbt`: first realm-contact support
- `expedition_rpg_first_contacts.snbt`: bounded DivineRPG + JITL first-contact branch
- `expedition_small_ships_and_water_routes.snbt`: bounded water-route travel-tech branch
- `expedition_undergarden_and_deeper_frontiers.snbt`: bounded dark-frontier contact with one utility follow-up
- `expedition_nether_entry_and_route_survival.snbt`: Nether entry, survival adaptation, and route-planning opener
- `expedition_betternether_materials_and_adaptation.snbt`: BetterNether material and local-tool payoff branch
- `expedition_fortresses_and_hellish_trials.snbt`: Nether structure-combat proof branch
- `expedition_workshop_and_industrial_prep.snbt`: Nether-fed workshop prep and Automation handoff support

## Live Structure Correction Note
- Mechanical live content is currently consolidated into three chapter files.
- Tracker/plan rows such as `mechanical_create_foundations`, `mechanical_rotational_power_and_first_logistics`, `mechanical_create_food_relief`, and `mechanical_engineers_handwork` still describe logical sub-arcs, but their live quests now physically live inside the merged Mechanical files above.
- Future deepening should continue to build around the live files unless a later re-split becomes necessary for readability.

## Jar / Mod Mapping Ledger

### Mechanical cluster ledger

#### Create workshop cluster
- Jar file: `create-1.21.1-6.0.9.jar`
- Mod id: `create`
- Primary domain: tech / process infrastructure
- Secondary domain: workshop logistics
- Age first appears: Mechanical
- Age main arc lives in: Mechanical
- First honest payoff: first repeatable pressing, milling, power transfer, and simple moving-item work
- Support prerequisites: andesite alloy, shafts, cogwheels, water wheel, basin, millstone, press, belts, funnel/chute pieces
- Must-quest objects now: andesite alloy, shaft, cogwheel, water wheel, millstone, basin, press, depot, large cogwheel, gearbox, belt connector, funnel, chute, mechanical plough, deployer, harvester, portable storage interface, mechanical saw
- Should-quest objects later in Mechanical: encased fan, wrench, mechanical drill, weighted ejector
- Optional / defer: vaults, stock links, advanced train/process parts
- Chapter destination: `mechanical_ironwork_and_workstations`, `mechanical_food_and_farm_handling`
- Later dependency: `expedition_workshop_and_industrial_prep`, Automation Create support
- Gating surface: Mechanical Age readiness, Create chain already live
- Coverage classification: real arc already exists

#### Create Integrated Farming + Farmer's Delight + Cooking for Blockheads kitchen support
- Jar files:
  - `create-integrated-farming-1.2.1.jar`
  - `FarmersDelight-1.21.1-1.2.10.jar`
  - `cookingforblockheads-neoforge-1.21.1-21.1.18.jar`
- Mod ids:
  - `create_integrated_farming`
  - `farmersdelight`
  - `cookingforblockheads`
- Primary domain: farming / food / survival support
- Secondary domain: workshop relief
- Age first appears: Mechanical
- Age main arc lives in: Mechanical
- First honest payoff: repeatable food prep and utility kitchen support
- Support prerequisites: deployer/harvester line, cutting board, knife, straw, safety net, canvas, slicer, cooking pot, sink, stove
- Must-quest objects now: fishing net, roost, cutting board, iron knife, straw, safety net, canvas, slicer, cooking pot, stove, sink, fridge, counter, recipe book
- Should-quest objects: toaster, milk jar, fruit basket, rich soil, organic compost
- Optional / defer: decorative kitchen pieces, higher-end food transformations
- Chapter destination: `mechanical_food_and_farm_handling`
- Later dependency: travel food quality, Expedition branch stability, later kitchen throughput
- Gating surface: Mechanical farming line and workshop heat
- Coverage classification: icon-only / incomplete before this pass, meaningful support after this pass

#### Sophisticated workshop relief cluster
- Jar files:
  - `sophisticatedstorage-1.21.1-1.5.31.1549.jar`
  - `sophisticatedbackpacks-1.21.1-3.25.34.1604.jar`
  - `ironchest-neoforge-1.21.1-16.0.9.jar`
- Mod ids:
  - `sophisticatedstorage`
  - `sophisticatedbackpacks`
  - `ironchest`
- Primary domain: workshop logistics / storage
- Secondary domain: exploration readiness
- Age first appears: Mechanical
- Age main arc lives in: Mechanical into Expedition
- First honest payoff: fewer return trips and less item chaos in a growing machine workshop
- Support prerequisites: iron chest, iron backpack, barrel, upgrade base, hopper, redstone, pistons, copper bulk
- Must-quest objects now: iron chest, iron backpack, barrel, upgrade base, deposit upgrade, packing tape, filter upgrade, pickup upgrade, stack upgrade starter tier, crafting upgrade
- Should-quest objects: controller, storage link, chest tier upgrades, restock upgrade
- Optional / defer: advanced upgrade families, netherite tiers, controller network scaling
- Chapter destination: `mechanical_workshop_logistics_and_storage` now, `expedition_storage_uplift` later
- Later dependency: AE2 bus integration, Expedition travel loadout, digital storage transition
- Gating surface: Mechanical Age workshop maturity now, comparator/ender-pearl storage network later
- Coverage classification: light support only before this pass, meaningful support after this pass

#### Iron workshop + early engineering support
- Jar files:
  - `ImmersiveEngineering-1.21.1-12.4.2-194.jar`
  - `ironfurnaces-neoforge-1.21.1-4.3.2.jar`
- Mod ids:
  - `immersiveengineering`
  - `ironfurnaces`
- Primary domain: tech / workshop maturity
- Secondary domain: process support
- Age first appears: Mechanical
- Age main arc lives in: Mechanical
- First honest payoff: faster smelting, first coke/treated wood, and first honest hand-built engineering parts
- Support prerequisites: iron furnace line, IE hammer, press support, coke bricks, treated wood, plates, wire, connectors
- Must-quest objects now: blast furnace, smithing table, anvil, iron furnace, IE hammer, wirecutter, coke bricks, coke, treated wood, engineer's crafting table, workbench, basic engineering, conveyor, copper plates, copper wire, wire coils, connectors, breaker switch
- Should-quest objects: low-voltage relay pieces, treated-wood crate, first capacitor once power support matters
- Optional / defer: heavy multiblocks, diesel, arc furnace line
- Chapter destination: `mechanical_ironwork_and_workstations`
- Later dependency: `expedition_workshop_and_industrial_prep`, Automation ore/logistics support
- Gating surface: Mechanical Age and Create press chain
- Coverage classification: light support only before consolidation, meaningful support now

#### Bounded utility / travel support placement
- Jar files:
  - `ars_nouveau-1.21.1-5.11.3.jar`
  - `Apotheosis-1.21.1-8.5.2.jar`
  - `waystones-neoforge-1.21.1-21.1.29.jar`
- Mod ids:
  - `ars_nouveau`
  - `apotheosis`
  - `waystones`
- Primary domain: utility magic / exploration support
- Secondary domain: readiness
- Age first appears: Mechanical as planning/signpost only
- Age main arc lives in: Expedition
- First honest payoff:
  - Ars: scribes table -> novice book -> apparatus literacy
  - Apotheosis: enchanting setup -> gem-cutting entry
  - Waystones: real fixed travel anchor once obsidian/warp stone are available
- Support prerequisites:
  - Ars: source gems, scribes table, novice book, arcane pedestal
  - Apotheosis: enchanting table, bookshelves, enchanted books, gem dust
  - Waystones: obsidian, warp stone, later scroll options
- Must-quest now: none added live in Mechanical
- Should-quest in Expedition: apparatus support pieces, gem-cutting table, return-to-realm travel support, waystone follow-through
- Optional / defer: Malum/Gaze overlap, late enchant reforging
- Chapter destination: Expedition branch chapters
- Later dependency: Automation gate prep, realm survival, later ritual placement
- Gating surface: Diamond threshold and Expedition branch unlocks
- Coverage classification: Expedition arcs exist, Mechanical planning only

### Expedition cluster ledger

#### Realm travel cluster
- Jar files:
  - `aether-1.21.1-1.5.10-neoforge.jar`
  - `deep_aether-1.21.1-1.1.5.1.jar`
  - `twilightforest-1.21.1-4.8.3345-universal.jar`
- Mod ids:
  - `aether`
  - `deep_aether`
  - `twilightforest`
- Primary domain: dimension / exploration
- Secondary domain: boss / danger preparation
- Age first appears: Expedition
- Age main arc lives in: Expedition
- First honest payoff: first realm materials, first useful Aether utility, first Twilight structure navigation, and first truthful Deep Aether contact without over-tier boss asks
- Support prerequisites: shield, backpack, waystone, safe food/water, basic enchant help, truthful portal access
- Must-quest objects for Batch B: skyroot planks, canopy planks, zanite gemstone, raven feather, skyroot chest, ambrosium torch, zanite ring, altar, raw clorite, magic map focus, magic map
- Should-quest objects: torchberries as a visible resource, ore magnet, Deep Aether compass tools, additional first-structure proof once combat envelope is clearer
- Optional / defer: Hydra and stronger realm boss trophies, late dungeon trophies
- Chapter destination: `expedition_aether_twilight_first_destinations`
- Later dependency: Expedition boss spine, dark-frontier placement, broader realm branches, travel route planning
- Gating surface: `diamonds_and_branch_unlocks`, travel readiness
- Coverage classification: light support only

#### Digital storage cluster
- Jar files:
  - `appliedenergistics2-19.2.17.jar`
  - `refinedstorage-neoforge-2.0.1.jar`
- Mod ids:
  - `ae2`
  - `refinedstorage`
- Primary domain: storage / logistics / automation support
- Secondary domain: workshop prep
- Age first appears: Expedition
- Age main arc lives in: Expedition
- First honest payoff: first powered ME network with real storage link support instead of a terminal-only preview
- Support prerequisites: quartz, charger, fluix, chest upgrades, cable, drives, cells, power input, starter storage controller/link utility
- Must-quest objects now: AE2 terminal, crafting terminal, chest, drive, 1k cells, storage bus, import/export bus, energy acceptor, controller, Sophisticated Storage controller, storage link
- Should-quest objects: quartz fiber, blank patterns, pattern provider, annihilation/formation planes later
- Optional / defer: advanced AE2 family, Mega Cells, later RS support cleanup
- Chapter destination: `expedition_storage_uplift`, `expedition_ae2_entry`
- Later dependency: Automation logistics and later Space networks
- Gating surface: `diamonds_and_branch_unlocks`, Nether quartz
- Coverage classification: AE2 real arc already exists, RS light support only

#### Expedition workshop + bounded magic cluster
- Jar files:
  - `ars_nouveau-1.21.1-5.11.3.jar`
  - `Apotheosis-1.21.1-8.5.2.jar`
  - `gaze-1.1.7.1.jar`
  - `malum-1.21.1-1.8.2.jar`
- Mod ids:
  - `ars_nouveau`
  - `apotheosis`
  - `gaze`
  - `malum`
- Primary domain: magic / ritual / enchanting support
- Secondary domain: workshop prep
- Age first appears: Expedition
- Age main arc lives in: Expedition
- First honest payoff:
  - Ars: apparatus online
  - Apotheosis: gem cutting and starter enchanting support
  - Gaze: later Malum-adjacent utility and workbench placement
  - Malum: later soul ritual awareness
- Support prerequisites:
  - Ars literacy pieces already live
  - Enchanting and gem dust already live
  - Gaze depends on Malum ecosystem, so planning-first only now
  - Malum needs altar/crucible/totem infrastructure, so planning-first only now
- Must-quest now: worn notebook, source jar, agronomic sourcelink, salvaging table
- Should-quest Batch B: deepen Ars with source jar storage/use literacy; deepen Apotheosis with actual utility payoff instead of just one gem; keep Gaze/Malum as placement-only notes
- Optional / defer: Gaze/Malum live quests until proper branch placement is ready
- Chapter destination: existing Expedition magic chapters now, planning map for Batch C
- Later dependency: `blaze_breakthrough`, Automation handoff, future ritual branches
- Gating surface: Diamond threshold, enchanting readiness, branch completion
- Coverage classification: Ars and Apotheosis light support only; Gaze/Malum absent / planning only

#### Nautec underwater cluster
- Jar file: `nautec-1.21.1-NeoForge-0.3.2.jar`
- Mod id: `nautec`
- Primary domain: exploration / environmental adaptation
- Secondary domain: underwater utility and later tech support
- Age first appears: Expedition
- Age main arc lives in: Expedition
- First honest payoff: diving gear, the first Aquatic Catalyst, and repaired salvage utility like aquatic chips or a first monocle before later laser or chemistry systems appear
- Support prerequisites: route anchor, backpack support, safe ocean travel, prismarine access, dried kelp, copper, glass, salvage or cast iron, bubble columns for air bottles
- Must-quest Batch D: saltwater bucket, ancient valve salvage, cast iron stock, Nautec Guide, diving helmet, brown polymer, diving chestplate, air bottle, aquatic catalyst, damaged aquatic chip, aquatic chip, aquarine steel ingot, prism monocle
- Should-quest next: fishing station, prismarine sand, crowbar, early rust-removal support, first simple aquarine steel line
- Optional / defer: laser routing, chemistry line, bacteria line, augmentation, deep-sea drain, bio reactor, mutator, charger, advanced armor/tools
- Chapter destination: new bounded Expedition branch chapter
- Later dependency: later Nautec chemistry / laser branch, possible Automation-adjacent underwater utility support, ocean route planning
- Gating surface: existing Expedition travel prep from `expedition_aether_twilight_first_destinations`
- Coverage classification: meaningful bounded support after Batch D

#### RPG first-contact cluster
- Jar files:
  - `divinerpg-1.10.9.3.jar`
  - `JITL - 1.21.1 - 2.2.4.jar`
- Mod ids:
  - `divinerpg`
  - `jitl`
- Primary domain: dimension / combat escalation
- Secondary domain: exploration readiness
- Age first appears: Expedition
- Age main arc lives in: later Expedition / Industrial escalation into Space
- First honest payoff:
  - DivineRPG: guidebook setup, overworld realmite/rupee contact, compact defensive/combat payoff, truthful stockpile readiness, and one boss-linked follow-through defensive step
  - JITL: flame-coin setup, recipe-book contact, sapphire tool payoff, one extra overworld material hook, truthful portal-frame readiness, and the first boss-linked key unlock
- Support prerequisites: diamond access, shield/travel readiness, honest overworld ore access, and a stable Expedition loadout before later portals or bosses appear
- Must-quest now:
  - `divinerpg:divine_sapling`
  - `patchouli:guide_book` with the DivineRPG book id
  - `divinerpg:raw_realmite`
  - `divinerpg:realmite_ingot`
  - `divinerpg:realmite_shield`
  - `divinerpg:realmite_block`
  - `divinerpg:raw_rupee`
  - `divinerpg:rupee_ingot`
  - `divinerpg:rupee_rapier`
  - `divinerpg:rupee_block`
  - `jitl:flame_coin`
  - `jitl:recipe_book`
  - `jitl:sapphire`
  - `jitl:sapphire_pickaxe`
  - `jitl:raw_shadium`
  - `jitl:frozen_portal_frame`
  - `jitl:journey_key`
  - `jitl:sapphire_shield`
  - `divinerpg:rupee_helmet`
- Should-quest next: stronger realm-ready kit, later portal-piece awareness where bosses actually support it, and the next explicit boss-linked unlock surface once Expedition boss sequencing grows
- Optional / defer: Arcana portal frames, Euca portal gems and pieces, later realm ladders, full boss ladders, and all late-dimension asks
- Chapter destination: `expedition_rpg_first_contacts`
- Later dependency: future RPG escalation family and later boss-linked realm branches
- Gating surface: existing shield-and-travel readiness from `expedition_aether_twilight_first_destinations`
- Coverage classification: meaningful bounded support

#### Small Ships travel-tech cluster
- Jar file: `smallships-neoforge-1.21.1-2.0.0-b2.1.jar`
- Mod id: `smallships`
- Primary domain: exploration / travel utility
- Secondary domain: logistics / route planning
- Age first appears: Expedition
- Age main arc lives in: Expedition
- First honest payoff: the first cargo-capable ship line for rivers, coasts, and ocean approaches, followed by real route-role ship choices
- Support prerequisites: route anchor, expedition backpack, wool, logs, leads, chest boat support, and one truthful reason for better lead supply
- Must-quest now:
  - `smallships:sail`
  - `minecraft:oak_chest_boat`
  - `smallships:oak_cog`
  - `smallships:oak_brigg`
  - `smallships:oak_drakkar`
  - `smallships:oak_galley`
- Should-quest next: stronger ocean-route support, route supply beats, and alternate hulls only when more destinations justify them
- Optional / defer: warship flavor, cannons, and any line that stops being Expedition travel utility
- Chapter destination: `expedition_small_ships_and_water_routes`
- Later dependency: ocean-route planning, Nautec synergy, and later destination support
- Gating surface: existing route anchor + expedition pack, with the better cargo ship fed by bounded Undergarden lead utility
- Coverage classification: partial live introduction justified

#### Nether expedition cluster
- Jar files:
  - `BetterNether-21.0.19.jar`
  - `HellishTrials-neoforge-1.0.5.jar`
  - `YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar`
  - `EternalNether-v21.1.3-1.21.1-NeoForge.jar`
  - `Luminous Nether V1.3.2 - NeoForge 1.3.2.jar`
  - `BOMD-NeoForge-1.21-1.3.2.jar`
- Mod ids:
  - `betternether`
  - `hellish_trials`
  - `betterfortresses`
  - `eternalnether`
  - `luminous_nether`
  - `bosses_of_mass_destruction`
- Primary domain: dimension / exploration / survival adaptation
- Secondary domain: combat escalation and return-home utility
- Age first appears: Expedition
- Age main arc lives in: late Expedition
- First honest payoff:
  - base Nether cluster: entry, glowstone, magma cream, wart routes, and strider travel so Nether trips become repeatable
  - BetterNether: Cincinnasite and Nether Ruby leading into a local workstation and one real local weapon payoff
  - Hellish Trials: the Nether Trial Key as the first real structure-combat proof
  - EternalNether: warped ender pearl and withered bone as natural combat proof, plus Catacomb contact as structure pressure
  - Luminous Nether: Ash Forest contact into Piglin Executioner and Basalt Executioner as the late-Nether hunt branch
  - BOMD: Gauntlet arena contact, Nether Gauntlet defeat, and Blazing Eye as the cleanest final Nether conquest payoff
- Support prerequisites: Diamond-threshold Expedition opener, stable shield and storage baseline, workshop prep, and enough travel discipline to survive repeated Nether runs
- Must-quest now:
  - `minecraft:golden_boots`
  - `minecraft:glowstone_dust`
  - `minecraft:magma_cream`
  - `minecraft:warped_fungus_on_a_stick`
  - `betternether:nether_reed_stem`
  - `betternether:cincinnasite`
  - `betternether:cincinnasite_ingot`
  - `betternether:cincinnasite_boots`
  - `betternether:cincinnasite_forged`
  - `betternether:cincinnasite_forge`
  - `betternether:nether_ruby`
  - `betternether:nether_ruby_sword`
  - `minecraft:nether_wart`
  - `minecraft:trial_key`
  - `minecraft:rib_armor_trim_smithing_template`
  - `eternalnether:warped_ender_pearl`
  - `eternalnether:withered_bone`
  - `eternalnether:catacomb` advancement
  - `luminous_nether:ash_forest_advancement`
  - `luminous_nether:kill_piglin_executioner`
  - `luminous_nether:kill_basalt_executioner`
  - `bosses_of_mass_destruction:gauntlet_blackstone`
  - `bosses_of_mass_destruction:nether/gauntlet_defeat`
  - `bosses_of_mass_destruction:blazing_eye`
- Should-quest next:
  - `betternether:nether_ruby` armor expansion
  - `betternether:obsidian_glass`
  - more fortress-route support once later structure loops matter
  - bounded EternalNether citadel contact
- Optional / defer:
  - EternalNether citadel loot ownership
  - Luminous Nether furnace / soul furnace / ritual content
  - BOMD brimstone-nectar reset utility
  - flaming ruby and later BetterNether smithing-template escalation
  - ominous trial escalation as a gate surface
- Chapter destination:
  - `expedition_nether_entry_and_route_survival`
  - `expedition_betternether_materials_and_adaptation`
  - `expedition_fortresses_and_hellish_trials`
  - `blaze_breakthrough`
  - `expedition_luminous_nether_climax`
  - `expedition_bomd_nether_gauntlet`
- Later dependency:
  - `expedition_bomd_nether_gauntlet`
  - `industrial_nether_logistics_and_ore_escalation`
- Gating surface: Diamond-threshold Expedition opener into a real Nether conquest chain; Hellish Trials and EternalNether act as mandatory branch combat proofs, blaze remains a required branch token, Luminous Nether provides the late hunt branch, and BOMD's Nether Gauntlet is the final Automation capstone
- Coverage classification: meaningful late-Expedition Nether phase after the capstone pass

## Object Inventory Summary By Cluster

### Mechanical must-quest objects in this pass
- `ironfurnaces:iron_furnace`
- `sophisticatedstorage:packing_tape`
- `sophisticatedbackpacks:filter_upgrade`
- `sophisticatedbackpacks:pickup_upgrade`
- `sophisticatedbackpacks:stack_upgrade_starter_tier`
- `sophisticatedbackpacks:crafting_upgrade`
- `cookingforblockheads:counter`
- `cookingforblockheads:recipe_book`

### Mechanical should-quest soon
- `sophisticatedstorage:controller`
- `sophisticatedstorage:storage_link`
- `sophisticatedstorage:gold_chest`
- `sophisticatedbackpacks:restock_upgrade`
- `cookingforblockheads:toaster`
- `cookingforblockheads:milk_jar`
- `ars_nouveau:source_jar`
- `ars_nouveau:agronomic_sourcelink`
- `apotheosis:salvaging_table` or equivalent utility payoff if truthful

### Mechanical defer
- higher Sophisticated tiers
- late kitchen novelty blocks
- full Ars branch
- full Apotheosis utility branch
- late Create utility machine sprawl

### Expedition must-quest for next batch
- `minecraft:chest` from `aether:skyroot_planks`
- `aether:ambrosium_torch`
- `aether:zanite_ring`
- `aether:altar`
- `deep_aether:raw_clorite`
- `twilightforest:magic_map_focus`
- `twilightforest:magic_map`
- `sophisticatedstorage:controller`
- `sophisticatedstorage:storage_link`
- `ae2:energy_acceptor`
- `ae2:controller`
- `ars_nouveau:worn_notebook`
- `ars_nouveau:source_jar`
- `ars_nouveau:agronomic_sourcelink`
- `apotheosis:salvaging_table`

### Expedition must-quest for the current branch wave
- `nautec:saltwater_bucket`
- `nautec:ancient_valve`
- `nautec:cast_iron_ingot`
- `nautec:nautec_guide`
- `nautec:diving_helmet`
- `nautec:brown_polymer`
- `nautec:diving_chestplate`
- `nautec:air_bottle`
- `nautec:aquatic_catalyst`
- `nautec:damaged_aquatic_chip`
- `nautec:aquatic_chip`
- `nautec:aquarine_steel_ingot`
- `nautec:prism_monocle`
- `undergarden:catalyst`
- `undergarden:twistytwig`
- `undergarden:slingshot`
- `undergarden:raw_cloggrum`
- `undergarden:cloggrum_ingot`
- `undergarden:utheric_shard`
- `undergarden:shard_torch`
- `undergarden:goo_ball`
- `minecraft:lead`
- `divinerpg:divine_sapling`
- `patchouli:guide_book` with the DivineRPG book id
- `divinerpg:raw_realmite`
- `divinerpg:realmite_ingot`
- `divinerpg:realmite_shield`
- `divinerpg:realmite_block`
- `divinerpg:raw_rupee`
- `divinerpg:rupee_ingot`
- `divinerpg:rupee_rapier`
- `divinerpg:rupee_block`
- `jitl:flame_coin`
- `jitl:recipe_book`
- `jitl:sapphire`
- `jitl:sapphire_pickaxe`
- `jitl:raw_shadium`
- `jitl:frozen_portal_frame`
- `jitl:journey_key`
- `jitl:sapphire_shield`
- `divinerpg:rupee_helmet`
- `smallships:sail`
- `minecraft:oak_chest_boat`
- `smallships:oak_cog`
- `smallships:oak_brigg`
- `smallships:oak_drakkar`
- `smallships:oak_galley`

### Expedition should-quest soon
- `twilightforest:ore_magnet`
- `ars_nouveau:ritual_brazier`
- `nautec:fishing_station`
- `nautec:crowbar`
- `nautec:gear`
- `nautec:aquarine_steel_compound`
- `undergarden:stoneborn` trade proof
- `undergarden:infuser` after first-contact ownership intentionally widens
- first Gaze signpost once Malum placement is mapped
- later DivineRPG and JITL portal-piece awareness once stronger boss and dimension routing exists
- alternate Small Ships hulls once more destinations justify them
- additional AE2 pattern support once Automation ownership is clearer

### Expedition defer
- Nautec laser chemistry and augmentation
- Nautec bacteria and reactor systems
- late horror fronts
- over-tier boss asks
- DivineRPG and JITL portal builds, realm ladders, and boss asks
- Malum/Gaze live implementation before proper placement
- Deep Aether compass tools and broader addon rollout
- late Aether and Twilight trophies

## Chapter Placement Plan

### Batch A — Mechanical completion and integrity
- Extend `mechanical_ironwork_and_workstations`
  - add one stronger smelting/workshop payoff
- Extend `mechanical_workshop_logistics_and_storage`
  - add backpack sorting, pickup, crafting, and packing relief
- Extend `mechanical_food_and_farm_handling`
  - add the missing kitchen companion pieces that make the existing kitchen line easier to use

### Batch B — Expedition branch deepening
- Extend `expedition_aether_twilight_first_destinations`
- Extend `expedition_enchanting_and_apotheosis_entry`
- Extend `expedition_enchanting_and_apotheosis_followup`
- Possibly extend `expedition_ars_nouveau`
- Preserve `blaze_breakthrough` and the current Automation handoff

Batch B final live set:
- `expedition_aether_twilight_first_destinations`
  - `minecraft:chest` from skyroot
  - `aether:ambrosium_torch`
  - `aether:zanite_ring`
  - `aether:altar`
  - `deep_aether:raw_clorite`
  - `twilightforest:magic_map_focus`
  - `twilightforest:magic_map`
- `expedition_storage_uplift`
  - `sophisticatedstorage:controller`
  - `sophisticatedstorage:storage_link`
- `expedition_ae2_entry`
  - `ae2:energy_acceptor`
  - `ae2:controller`
- `expedition_ars_nouveau`
  - `ars_nouveau:worn_notebook`
  - `ars_nouveau:source_jar`
  - `ars_nouveau:agronomic_sourcelink`
- `expedition_enchanting_and_apotheosis_followup`
  - `apotheosis:salvaging_table`

### Batch C — Expedition placement planning
- place `gaze` and `malum`
- place `divinerpg` and `jitl`
- place dark-frontier first-contact gates
- map which boss or branch surfaces should open them later

#### Batch C coverage recount
- `gaze`: planning-only; not safe as a standalone Expedition live lane
- `malum`: first-contact safe only as a future ritual awareness branch
- `divinerpg`: first-contact safe as a bounded overworld-material branch
- `jitl`: first-contact safe alongside `divinerpg`
- `undergarden`: first-contact safe for Expedition planning and later bounded utility follow-up
- `deeperdarker`: planning-only until Ancient City / Warden readiness is a real branch gate
- `macabre`: defer; too late and too horror-dense for Expedition rollout
- `the_afterdark`: planning-only; dimension exists, but current first-contact path is too opaque for live Expedition

#### Batch C jar / mod placement ledger

##### Gaze preliminary placement
- Jar file: `gaze-1.1.7.1.jar`
- Mod id: `gaze`
- Primary domain: magic / ritual / arcane
- Secondary domain: utility support
- Age first appears: Expedition as planning-only awareness
- Age main arc lives in: Industrial
- Age culmination / late extension: Space
- First honest payoff: `gaze:enchantment_workbench` and `gaze:spirit_channel_pouch`, but they depend on Malum-style rune and spirit-infusion infrastructure rather than a self-contained Expedition utility lane
- Support prerequisites: Malum soulstone access, ritual progression, spirit infusion, rune progression
- Must-place-now elements: none live
- Should-signpost-now elements: planning note only that Gaze should open after the first truthful Malum ritual foothold, not before
- Defer elements: live Gaze quests, rune rollout, pouch utility, enchantment workbench rollout
- Future chapter destination: later shared ritual chapter, not a standalone Expedition microchapter
- Later dependency: Industrial ritual branch, later dark-frontier and utility-magic bridges
- Gating surface: future magic readiness plus Malum branch completion
- Coverage classification: planning-only

##### Malum preliminary placement
- Jar file: `malum-1.21.1-1.8.2.jar`
- Mod id: `malum`
- Primary domain: magic / ritual / arcane
- Secondary domain: atmosphere / survival pressure / horror
- Age first appears: Expedition as signposted first-contact only
- Age main arc lives in: Industrial
- Age culmination / late extension: Space
- First honest payoff: `malum:encyclopedia_arcana`, then `malum:spirit_altar`
- Support prerequisites: `malum:refined_soulstone`, runewood access, gold, altar setup, later crucible/totem structure
- Must-place-now elements: no new live quests; place the branch in planning as a future Expedition-forward unlock family
- Should-signpost-now elements: first-contact documentation payoff through `encyclopedia_arcana`; altar as the first real branch opener once ritual readiness is intentionally unlocked
- Defer elements: `spirit_crucible`, totems, soul-binding, full spirit-infusion ownership, combat curios, Gaze crossover
- Future chapter destination: bounded Expedition signpost later, main ownership in an Industrial ritual chapter
- Later dependency: Gaze rollout, dark-frontier ritual crossover, later Space ritual ownership
- Gating surface: future branch completion from bounded Expedition magic plus later dark-frontier or boss-linked ritual unlock
- Coverage classification: first-contact safe

##### DivineRPG placement
- Jar file: `divinerpg-1.10.9.3.jar`
- Mod id: `divinerpg`
- Primary domain: dimension / exploration
- Secondary domain: boss / combat gate
- Age first appears: Expedition first contact
- Age main arc lives in: later Expedition / Industrial escalation
- Age culmination / late extension: Space / Ascension
- First honest payoff: guidebook setup, overworld realmite/rupee contact, and the first compact shield/weapon payoff before portal ownership exists
- Support prerequisites: shield and travel readiness, diamond access, honest overworld ore access, and stronger later boss sequencing before any real realm ladder begins
- Must-place-now elements: Divine sapling, guide book, realmite/rupee materials, and one bounded Realmite/Rupee gear payoff
- Should-signpost-now elements: later portal construction and stronger realm escalation stay locked behind later combat and boss readiness
- Defer elements: Arcana portal frames, realm resource loops, and boss asks
- Future chapter destination: future RPG escalation family, likely paired with `jitl`
- Later dependency: later RPG escalation family, future boss-linked realm unlocks, and post-Automation dimension breadth
- Gating surface: existing Expedition shield-and-travel readiness now; future boss kill plus dimension readiness later
- Coverage classification: first-contact safe and now partially live

##### Journey Into The Light placement note
- Jar file: `JITL - 1.21.1 - 2.2.4.jar`
- Mod id: `jitl`
- Primary domain: dimension / exploration
- Secondary domain: boss / combat gate
- Age first appears: Expedition first contact
- Age main arc lives in: later Expedition / Industrial escalation
- Age culmination / late extension: Space / Ascension
- First honest payoff: flame-coin setup, recipe-book contact, sapphire utility, and a second overworld material hook before portals exist
- Support prerequisites: the same Expedition travel readiness as DivineRPG first contact, then stronger boss/dimension ownership before portal pieces matter
- Must-place-now elements: flame coin, recipe book, sapphire, sapphire pickaxe, and raw shadium
- Should-signpost-now elements: later portal-piece routing beside DivineRPG, not separate dimension spam
- Defer elements: Euca portal gems, portal pieces, later dimensions, and boss asks
- Future chapter destination: future RPG escalation family
- Later dependency: same later RPG escalation family and boss-linked dimension routing as DivineRPG
- Gating surface: Expedition travel readiness now; future boss and dimension proof later
- Coverage classification: first-contact safe and now partially live

##### Undergarden first-contact placement
- Jar file: `The_Undergarden-1.21.1-0.9.5.jar`
- Mod id: `undergarden`
- Primary domain: dimension / exploration
- Secondary domain: atmosphere / survival pressure / horror
- Age first appears: Expedition
- Age main arc lives in: Industrial
- Age culmination / late extension: Space
- First honest payoff: `undergarden:catalyst` dimension access, then `undergarden:slingshot` as the first practical dimension-native utility/combat payoff
- Support prerequisites: ender pearls, copper, stone, safe Expedition travel kit, later dimension survival support, eventual `infuser` for deeper branch identity
- Must-place-now elements: place Undergarden in planning as the only dark-frontier branch that is truly safe for Expedition first contact
- Should-signpost-now elements: Catalyst entry, first slingshot utility, first cloggrum / shard-torch / structure-exploration support in a future bounded pass
- Defer elements: Forgotten Guardian branch, forgotten smithing progression, full infuser ownership, deeper ore/armor rollouts
- Future chapter destination: future `expedition_dark_frontier_entry` followed by a later Industrial dark-frontier chapter
- Later dependency: second Expedition boss-step planning, later Industrial dark-frontier scale-up
- Gating surface: future dimension access unlock after bounded Expedition branch completion, not the basic Expedition opener
- Coverage classification: first-contact safe

##### Deeper and Darker placement
- Jar file: `deeperdarker-neoforge-1.21.1-1.3.5.jar`
- Mod id: `deeperdarker`
- Primary domain: dimension / exploration
- Secondary domain: atmosphere / survival pressure / horror
- Age first appears: late Expedition planning only
- Age main arc lives in: Industrial
- Age culmination / late extension: Space
- First honest payoff: `deeperdarker:sculk_transmitter` and Otherside access, but both are tightly tied to Ancient City and Warden progression
- Support prerequisites: Ancient City discovery, Warden-adjacent readiness, stronger enchant/combat kit, controlled deep-dark routing
- Must-place-now elements: none live
- Should-signpost-now elements: planning note that this branch should open from exploration proof plus stronger combat readiness, not from generic dimension curiosity
- Defer elements: Otherside entry, sculk transmitter, sonorous staff, live Deeper and Darker chapter rollout
- Future chapter destination: future dark-frontier second-wave chapter
- Later dependency: second Expedition boss-step planning, Industrial horror branch progression
- Gating surface: structure or exploration proof plus later boss/danger proof
- Coverage classification: planning-only

##### Macabre placement
- Jar file: `macabre-0.7.3-neoforge-1.21.1.jar`
- Mod id: `macabre`
- Primary domain: atmosphere / survival pressure / horror
- Secondary domain: boss / combat gate
- Age first appears: Industrial planning only
- Age main arc lives in: Industrial
- Age culmination / late extension: Space
- First honest payoff: not Expedition-safe; the visible branch identity is already wrapped around `Valamon` and heavy body-horror combat
- Support prerequisites: late dark-frontier ownership, explicit horror-branch intent, stronger gear/combat envelope
- Must-place-now elements: none
- Should-signpost-now elements: none live; planning note only that Macabre belongs after the first dark-frontier foothold, not as an Expedition opener
- Defer elements: all live implementation
- Future chapter destination: late Industrial horror branch
- Later dependency: Industrial boss branches, later ritual or prestige horror tie-ins
- Gating surface: future boss kill plus horror-branch completion
- Coverage classification: defer

##### The Afterdark placement
- Jar file: `the_afterdark-1.21.1-neoforge-1.0.3.1.jar`
- Mod id: `the_afterdark`
- Primary domain: dimension / exploration
- Secondary domain: atmosphere / survival pressure / horror
- Age first appears: Industrial planning only
- Age main arc lives in: Industrial
- Age culmination / late extension: Space
- First honest payoff: teleport-altar discovery and `the_afterdark:teleport_catalyst`, but the practical entry path is still too opaque for a safe Expedition rollout
- Support prerequisites: structure discovery, catalyst logic, clearer branch ownership, later dark-frontier readiness
- Must-place-now elements: none
- Should-signpost-now elements: planning note only; no live signpost until the first dark-frontier branch is already established
- Defer elements: all live implementation
- Future chapter destination: later Industrial dark-frontier branch
- Later dependency: horror-branch escalation after Undergarden and Deeper and Darker placement are already stable
- Gating surface: future structure proof plus dark-frontier branch completion
- Coverage classification: planning-only

#### Batch C first-appearance / main-age / culmination-age placement table

| cluster | first appearance | main age | culmination / late extension | placement call |
| --- | --- | --- | --- | --- |
| Gaze | Expedition awareness only | Industrial | Space | planning-only until Malum has a real ritual foothold |
| Malum | Expedition first-contact signpost | Industrial | Space | first-contact safe, but not a live full branch yet |
| DivineRPG | Expedition first contact | later Expedition / Industrial | Space / Ascension | bounded live contact now; portals and bosses later |
| JITL | Expedition first contact | later Expedition / Industrial | Space / Ascension | bounded live contact now; portals and bosses later |
| Undergarden | Expedition first-contact | Industrial | Space | safest dark-frontier early placement; bounded utility follow-up is also safe |
| Deeper and Darker | late Expedition planning only | Industrial | Space | too Warden-tied for current live Expedition |
| Macabre | Industrial planning only | Industrial | Space | too horror-heavy and combat-late for Expedition |
| The Afterdark | Industrial planning only | Industrial | Space | not transparent enough for safe Expedition rollout yet |

#### Batch C must-place-now / signpost-now / defer

##### Must-place-now
- `malum` as a future Expedition-forward ritual family with first-contact only
- `undergarden` as the dark-frontier branch with the safest Expedition first-contact fit
- `divinerpg` + `jitl` as a paired RPG escalation family whose first-contact layer can safely begin in Expedition
- `deeperdarker`, `macabre`, and `the_afterdark` as dark-frontier layers that need stronger gates than the current Expedition opener

##### Should-signpost-now
- Malum first honest foothold:
  - `malum:encyclopedia_arcana`
  - `malum:spirit_altar`
- Undergarden first honest foothold:
  - `undergarden:catalyst`
  - `undergarden:slingshot`
- DivineRPG / JITL first honest footholds:
  - guidebooks
  - overworld material contact
  - first compact Expedition-safe gear payoffs
- Deeper and Darker planning note:
  - Ancient City / Warden readiness before Otherside access

##### Defer
- all live `gaze` quests
- all live `deeperdarker` quests
- all live `macabre` quests
- all live `the_afterdark` quests
- full live `malum` rollout until ritual ownership is intentionally unlocked
- full live `undergarden` rollout until Expedition first-contact sequencing is authored

#### Expedition-forward unlock sequencing plan

##### Current live-safe unlock surfaces
- `diamonds_and_branch_unlocks`
  - owns first Expedition breadth visibility
- existing realm first-contact completion
  - owns bounded realm utility and exploration support
- existing Expedition magic/storage/workshop branches
  - own the current truthful prep into `blaze_breakthrough`

##### Future Expedition-forward sequencing
1. `diamonds_and_branch_unlocks`
   - opens realm-contact, storage, enchanting, Ars, and workshop-prep branches
2. first bounded Expedition branch completion
   - should later unlock `undergarden` first-contact, not Deeper and Darker or late horror content
3. bounded Expedition magic completion
   - can later unlock Malum awareness or first ritual-contact signposting
4. first Expedition branch boss or equivalent danger proof
   - should later unlock the next dark-frontier planning surface
5. stronger structure/exploration proof
   - should later unlock Deeper and Darker planning surfaces
6. `blaze_breakthrough`
   - remains the current Expedition -> Automation gate and should stay above sightseeing or teaser-only branches

##### Over-tier asks to avoid
- no Hydra-tier or equivalent realm trophies in first-contact chapters
- no Ancient City / Warden / Otherside progression in the early Expedition opener
- no DivineRPG realm portals in current Expedition breadth
- no Macabre or Afterdark live asks before a real dark-frontier branch exists

#### Batch C gating / dependency validation checklist
- do not add live Malum or Gaze tasks before ritual support exists
- keep live DivineRPG and JITL tasks limited to guidebooks, overworld materials, and compact tools until later combat/dimension architecture exists
- if Undergarden goes live later, require bounded Expedition branch completion before Catalyst entry
- if Deeper and Darker goes live later, require Ancient City / Warden readiness instead of generic curiosity
- keep `blaze_breakthrough` as the only live Expedition -> Automation handoff
- do not expose late horror branches as current-use content in the Expedition opener
- every future branch must have a later dependency:
  - Malum -> Gaze / ritual branch growth
  - Undergarden -> later dark-frontier and boss sequencing
  - DivineRPG / JITL -> later RPG escalation family
  - Deeper and Darker / Macabre / Afterdark -> later Industrial horror ownership

#### Batch C recommended minimal live changes
- none required in this pass
- existing live Expedition quests remain truthful enough for release and for the current breadth layer
- the next safe live widening after this planning pass is a bounded `Undergarden` first-contact pass, not full dark-frontier rollout

#### Batch C validation notes
- no live quest edits are required for this planning pass
- no false stage references are introduced
- no new gate surfaces are invented
- late horror content stays out of current live Expedition
- DivineRPG is placed without turning Expedition into chaotic RPG sprawl
- Gaze remains subordinate to Malum instead of being placed as a fake standalone utility branch
- Undergarden is the only dark-frontier cluster currently marked as Expedition first-contact safe
- `blaze_breakthrough` remains the truthful Automation handoff above the current Expedition support set

### Batch D — Nautec + Undergarden first contact
- add a bounded Nautec underwater branch
- keep Nautec focused on ocean salvage, diving prep, air handling, and Aquatic Catalyst first-contact
- implement a bounded Undergarden first-contact chapter only
- keep Deeper and Darker, Macabre, and Afterdark out of live Expedition
- preserve `blaze_breakthrough` and the current Automation handoff

### Batch D Follow-Up — Nautec second-step utility
- extend the live Nautec branch with repaired salvage and first utility-only Aquarine Steel use
- keep the follow-up on buried treasure repair and ocean geode salvage instead of widening into lasers, chemistry, or augmentation
- preserve Undergarden exactly as first-contact only

### Batch E - RPG first contacts + water routes
- add one bounded live chapter for DivineRPG + JITL first contact
- keep it on guidebooks, overworld materials, and first practical Expedition-safe gear
- do not open portals, boss trophies, or full dimension ladders
- extend Undergarden one narrow step with goo-ball and lead utility only
- add one bounded Small Ships travel-tech chapter so Expedition gets a real water-route branch
- preserve `blaze_breakthrough` and the current Automation handoff

### Batch F - route support + bounded portal readiness
- extend `expedition_small_ships_and_water_routes` with route-role hull follow-through
- use drakkar and galley as real ship-choice payoffs, not decorative padding
- extend `expedition_rpg_first_contacts` with the first honest second-step readiness surface
- keep DivineRPG on stockpile readiness only where real portal items are still too early
- allow JITL to reach frozen portal frames, but stop before Euca portal gems, bosses, or full realm ladders
- preserve `blaze_breakthrough` and the current Automation handoff

### Batch G - first boss-linked RPG unlock surface
- extend `expedition_rpg_first_contacts` with one truthful boss-linked proof instead of a fake teaser
- use the Rockite Smasher's `journey_key` as the first safe JITL boss-linked unlock surface
- let that key unlock one bounded next layer of defensive follow-through
- keep DivineRPG below real portal ownership and keep JITL below full realm ladders
- do not widen into Nether JITL bosses, DivineRPG Nether bosses, or full RPG boss chains
- preserve `blaze_breakthrough` and the current Automation handoff

## Gating / Dependency Map

### Mechanical
- `entering_the_iron_era` -> `mechanical_ironwork_and_workstations`
- iron workshop -> Create press / IE handwork -> workshop logistics -> food handling
- new workshop relief quests stay under existing live dependencies and do not add stage leaks
- no diamond, Nether, ender pearl, or late-dimension asks are added to Mechanical

### Expedition
- `diamond_threshold` -> `diamonds_and_branch_unlocks`
- Expedition breadth remains locked behind diamond progression
- `blaze_breakthrough` stays the Automation handoff and should continue to require Expedition capstones, not sightseeing
- new Expedition work should not ask for stronger boss trophies than the current age envelope supports
- realm utility additions should hang from existing first-contact proofs, not bypass them
- Nautec should hang from existing travel-readiness proof and stay underwater-exploration-first rather than becoming a generic tech chapter
- Undergarden should stay bounded: catalyst, first utility tools, first metal proof, anti-rotspawn light, and one narrow goo-ball -> lead utility follow-up only
- AE2/storage additions should clarify powered-network use and later bus integration, not pre-empt Automation autocrafting
- DivineRPG and JITL now reach a bounded second step through DivineRPG stockpile readiness, JITL frozen portal frames, and the Rockite Smasher's Journey Key, but full portal ownership and boss ladders still stay deferred
- Small Ships belongs here as travel-tech, not Industrial factory tech, and its second step should deepen route roles rather than decorative variants
- Gaze and Malum still stay planning-first unless a bounded first-contact payoff can be proven truthful

## Recommended Implementation Order
1. Batch A — Mechanical completion and integrity
2. Batch B — Expedition branch deepening
3. Batch C — Expedition cluster placement planning
4. Batch D — Nautec underwater first contact + bounded Undergarden first contact
5. Batch D follow-up — Nautec second-step utility

6. Batch E - RPG first contacts + water routes
7. Batch F - route support + bounded portal readiness
8. Batch G - first boss-linked RPG unlock surface

## Mechanical Deepening Follow-Up (2026-04-01)
- `mechanical_early_utility_machines` is now live with Create Additions, Generator Galore, and Botany Pots as one bounded utility lane.
- `mechanical_dungeon_readiness` is now live with shield/armor/rations plus first Apotheosis/Artifacts/Relics contact beats.
- `mechanical_age_boss_hunts` is now live as a bounded sequential validation route:
- `aether:enter_aether` -> `aether:bronze_dungeon` -> `aether:silver_dungeon`
- `twilightforest:twilight_hunter` -> `twilightforest:progress_naga` -> `twilightforest:progress_lich`
- `bosses_of_mass_destruction:nether/gauntlet_defeat` is present as an optional extra validator, not the Mechanical gate.
- Existing protected Mechanical chapters were deepened additively:
- `mechanical_ironwork_and_workstations`: hand crank, wrench, fluid pipe/tank/pump, and item vault support
- `mechanical_food_and_farm_handling`: Aquaculture + Ocean's Delight food-route follow-through
- `mechanical_workshop_logistics_and_storage`: restock/magnet and storage I/O routing beats

## Validation Checklist
- no existing live quest rewritten unless required for safety
- no false stage references introduced
- no Diamond/Nether/Automation leaks into Mechanical
- every new quest uses a real obtainable item
- support pieces are included before the payoff they enable
- new Mechanical content makes the workshop feel broader, not more fragmented
- Expedition planning identifies later gates and dependencies before widening live realm content
- no over-tier realm trophies or boss kills are introduced into early Expedition support chapters
- Expedition still ends on `blaze_breakthrough`, not on sightseeing or random branch clutter
- Nautec stays an underwater Expedition branch, not a detached tech island
- Undergarden stays bounded and stops before infuser expansion, forgotten-metal upgrades, or boss escalation
- DivineRPG stays below untruthful portal ownership and full boss asks; JITL stops at frozen portal frames plus the first boss-linked key surface rather than full realm ladders
- Small Ships stays a travel branch with route utility and ship-role choice rather than becoming generic workshop clutter
