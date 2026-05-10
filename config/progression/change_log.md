# Change Log

## 2026-04-02 - Mechanical Reward Pilot Rollout

### Added

- Added concrete reward payload templates for live FTB injection:
  - [`reward_payload_library.json`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/reward_payload_library.json)
- Added the targeted pilot assignment map:
  - [`reward_pilot_mechanical_assignments.json`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/reward_pilot_mechanical_assignments.json)

### Changed

- Extended [`reward_registry_ids.json`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/reward_registry_ids.json) with:
  - `mechanical_readiness_t1_bundle`
  - `mechanical_workshop_cache_t2`
- Applied live pilot rewards to two Mechanical chapters without changing gates, dependencies, or stage logic:
  - [`mechanical_workshop_logistics_and_storage.snbt`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/mechanical_workshop_logistics_and_storage.snbt)
  - [`mechanical_dungeon_readiness.snbt`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/mechanical_dungeon_readiness.snbt)

### Why

- This is the first live application pass for the reward framework: small, progression-safe, and chapter-targeted.
- The rollout focuses on workshop relief and readiness support without bypassing Mechanical progression or flooding trivial crafts with oversized payouts.

## 2026-04-02 - Reward Registry Framework Implementation Pass

### Added

- Added the reusable reward framework design doc:
  - [`reward_registry_framework.md`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/reward_registry_framework.md)
- Added the structured reward id library:
  - [`reward_registry_ids.json`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/reward_registry_ids.json)

### Changed

- Updated [`quest_chapter_plan.json`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/quest_chapter_plan.json) metadata to:
  - sync authored live count to `538`
  - register the new reward-framework/registry policy surface
- Updated [`quest_production_roadmap.md`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/quest_production_roadmap.md) with reward-framework authority ordering and placement-light rollout rules.
- Updated [`quest_source_audit.md`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/quest_source_audit.md) with reward registry source anchors tied to live installed mod ecosystems.

### Why

- AoA now has enough live chapter identity that rewards need a reusable framework instead of ad hoc per-quest item selection.
- This pass establishes stable ids, tier policy, quest-type mapping, and crate-pool behavior while keeping placement intentionally light and progression-safe.

## 2026-03-31 - Expedition Nether Phase Deepening

### Changed

- Added a real Expedition Nether chapter group instead of leaving Nether progression as a thin blaze checkpoint:
  - `expedition_nether_entry_and_route_survival.snbt`
  - `expedition_betternether_materials_and_adaptation.snbt`
  - `expedition_fortresses_and_hellish_trials.snbt`
- Built the Nether opener around truthful survival and route-planning beats:
  - first Nether entry
  - piglin-safe gold boots
  - glowstone return stock
  - magma cream as the first fire-resistance planning payoff
  - strider routing through `Warped Fungus on a Stick`
- Integrated `BetterNether` into Expedition as a real local material branch:
  - `Nether Reed`
  - `Cincinnasite`
  - `Cincinnasite Ingot`
  - `Cincinnasite Boots`
  - `Forged Cincinnasite`
  - `Cincinnasite Forge`
  - `Nether Ruby`
  - `Nether Ruby Sword`
- Integrated `Hellish Trials` and better fortress routing as the first real Nether combat-pressure branch:
  - `Nether Wart`
  - `Trial Key`
  - `Rib Trim`
- Kept the Expedition -> Automation handoff blaze-based because no deterministic Nether boss kill is truthful yet, but strengthened `blaze_breakthrough.snbt` so it now sits behind:
  - AE2 baseline
  - Ars apparatus
  - enchanting follow-up
  - workshop prep
  - BetterNether material payoff
  - Nether Trial combat proof
- Added one immediate post-blaze return-home payoff:
  - `Nether Brewing Stand`
- Synced the planning layer so Expedition now explicitly owns a real Nether phase, while `EternalNether` and `Luminous Nether` remain deferred until their payoff and power curve are clearer.

## 2026-03-31 - Expedition RPG Boss-Linked Unlock Surface

### Changed

- Extended `expedition_rpg_first_contacts.snbt` with the first real boss-linked unlock surface for the bounded Expedition RPG branch:
  - `Journey Key`
  - `Sapphire Shield`
  - `Rupee Helmet`
- Used the `Rockite Smasher` boss crystal reward from JITL as the first safe combat-proof gate for the branch instead of forcing later Nether or dimension bosses.
- Kept the rollout bounded:
  - no DivineRPG portal ownership
  - no JITL realm ladders
  - no over-tier boss trophies
- Updated the Expedition planning layer so the RPG branch now explicitly has a first boss-linked unlock surface while later boss ladders and full dimension ownership remain deferred.

## 2026-03-31 - Expedition Route Support + Portal Readiness

### Changed

- Extended `expedition_small_ships_and_water_routes.snbt` with a second truthful route-support step:
  - `Oak Drakkar`
  - `Oak Galley`
- Extended `expedition_rpg_first_contacts.snbt` with the next bounded readiness layer:
  - `Realmite Block`
  - `Rupee Block`
  - `Frozen Portal Frame`
- Kept the RPG branch below dishonest portal ownership:
  - DivineRPG now stops at stockpile readiness because its real portal surfaces still lean on later materials and boss-linked items.
  - JITL now reaches frozen portal-frame prep, but still stops before Euca portal gems, boss drops, and full realm ladders.
- Updated the Expedition planning layer so Small Ships second-step route support and DivineRPG/JITL bounded portal-readiness are reflected in the roadmap, tracker, coverage matrix, and deepening plan.

## 2026-03-31 - Expedition RPG + Water Routes Follow-Up

### Changed

- Added a new live Expedition branch chapter: `expedition_rpg_first_contacts.snbt`.
- Integrated the first truthful DivineRPG + JITL contact layer around overworld materials and guidebook setup instead of portal spam:
  - `Divine Sapling`
  - `Divine Guide`
  - `Raw Realmite`
  - `Realmite Ingot`
  - `Realmite Shield`
  - `Raw Rupee`
  - `Rupee Ingot`
  - `Rupee Rapier`
  - `Flame Coin`
  - `JITL Recipe Book`
  - `Sapphire`
  - `Sapphire Pickaxe`
  - `Raw Shadium`
- Extended `expedition_undergarden_and_deeper_frontiers.snbt` one narrow step beyond first contact:
  - `Goo Ball`
  - `Undergarden Leads`
- Added a new live Expedition travel-tech chapter: `expedition_small_ships_and_water_routes.snbt`.
- Built the Small Ships line around truthful route utility instead of generic tech clutter:
  - `Sail`
  - `Chest Boat`
  - `Oak Cog`
  - `Oak Brigg`
- Cross-linked the better ship payoff to the Undergarden lead utility so the dark-frontier branch now feeds real travel infrastructure.
- Updated the Expedition planning layer so `Journey Into The Light` is treated as installed and live in the first-contact RPG branch instead of remaining a planning-only assumption.

### Why

- Expedition needed one more breadth step that players will actually notice without destabilizing the current handoff into Automation.
- DivineRPG and JITL were ready for a controlled first-contact rollout through guidebooks, overworld ores, and compact gear payoffs, but not for portals or full realm ladders yet.
- Small Ships is the right travel-tech fit for Expedition because it changes route planning and cargo movement instead of adding more workshop machinery.

## 2026-03-31 - Nautec Second-Step Utility Follow-Up

### Changed

- Extended `expedition_nautec_underwater_first_contact.snbt` without rewriting the existing branch.
- Added a narrow second-step utility follow-up after `Aquatic Catalyst`:
  - `Damaged Aquatic Chip`
  - `Aquatic Chip`
  - `Aquarine Steel Ingot`
  - `Prism Monocle`
- Kept the branch focused on salvage repair and underwater utility instead of widening into laser chemistry, augmentation, or later Nautec machines.
- Corrected the Expedition deepening plan so the live Nautec branch references `Ancient Valve` instead of the older stale `Oil Barrel` note.
- Synced live Expedition counts and tracker notes to the current questbook state.

### Why

- Nautec was ready for one more truthful Expedition step that players would notice.
- Salvaged chips and a first monocle utility payoff fit the ocean-exploration identity better than jumping straight into full Nautec machinery.
- This keeps the current Expedition -> Automation handoff stable while making the underwater branch feel less like a stub.

## 2026-03-31 - Expedition Nautec + Undergarden First-Contact Pass

### Changed

- Added a new live Expedition branch chapter: `expedition_nautec_underwater_first_contact.snbt`.
- Built the Nautec branch around the first honest underwater loop:
  - `Salt Water`
  - `Ancient Valve`
  - `Cast Iron Stock`
  - `Nautec Guide`
  - `Diving Helmet`
  - `Brown Polymer`
  - `Diving Chestplate`
  - `Pressurized Air Bottle`
  - `Aquatic Catalyst`
- Added the first live bounded Undergarden chapter by implementing `expedition_undergarden_and_deeper_frontiers.snbt` as `Undergarden First Contact`.
- Kept that chapter intentionally first-contact only:
  - `Undergarden Catalyst`
  - `Twistytwig`
  - `Slingshot`
  - `Raw Cloggrum`
  - `Cloggrum Ingot`
  - `Utheric Shard`
  - `Shard Torch`
- Wired both new chapters off the existing Expedition travel-prep branch instead of the basic opener alone, so they read as connected route-expansion content rather than detached side islands.
- Updated the Expedition planning artifacts so Nautec is now formally placed as an underwater exploration branch and Undergarden is now live as the bounded dark-frontier first-contact branch.
- Kept `blaze_breakthrough` and all current Expedition -> Automation gate logic unchanged.

### Why

- Expedition needed one more live breadth step that players would actually notice.
- Nautec fits that role when treated as ocean exploration, diving preparation, and underwater salvage instead of generic machine clutter.
- Undergarden was the safest next dark-frontier expansion, but only at first-contact scale. This pass keeps it there and avoids prematurely widening into later horror or boss content.

## 2026-03-30 - Mechanical + Expedition Deepening Batch C Planning

### Changed

- Updated `mechanical_expedition_deepening_plan.md` with the Expedition placement-planning pass for the next breadth wave.
- Added concrete placement ledgers for:
  - `Gaze`
  - `Malum`
  - `DivineRPG`
  - `Journey Into The Light`
  - `The Undergarden`
  - `Deeper and Darker`
  - `Macabre`
  - `The Afterdark`
- Recorded first-appearance, main-age, and culmination-age ownership for those clusters instead of leaving them as loose “installed means future quests” placeholders.
- Marked `Undergarden` as the only dark-frontier branch currently safe for Expedition first-contact planning.
- Kept `Gaze` subordinate to `Malum` ritual placement instead of treating it as a standalone Expedition utility lane.
- Kept `DivineRPG` and `Journey Into The Light` out of current live Expedition breadth and placed them in the later RPG escalation family.
- Added an Expedition-forward unlock sequencing plan that keeps:
  - `diamonds_and_branch_unlocks` as the breadth opener
  - bounded realm / magic / storage branches as the current live prep layer
  - `blaze_breakthrough` as the truthful Expedition -> Automation handoff
- Explicitly recorded that this pass requires no live quest edits.

### Why

- Expedition is now broad enough that the next widening step needs controlled placement, not ad hoc chapter sprawl.
- This pass fixes that by deciding which clusters are safe for first contact, which should stay signposted only, and which are too late to touch yet.
- The result is a clearer next-wave map for dark-frontier, ritual, and RPG content without disturbing the current live questbook.

## 2026-03-29 - Age-Domain Boss Architecture Pass

### Added

- Added `age_domain_boss_architecture.md` as the source-of-truth architecture doc for:
  - age boss spines
  - boss classification
  - chapter unlock surfaces
  - age-domain quotas
  - cluster family placement

### Changed

- Updated `quest_production_roadmap.md` to make the boss-spine architecture authoritative for future implementation and to call out current structural gaps.
- Updated `quest_source_audit.md` and `age_domain_boss_architecture.md` to treat `Journey Into The Light` as an installed RPG escalation branch alongside `DivineRPG`.
- Updated `quest_chapter_plan.json` metadata with the new architecture policy and authority docs.
- Updated `quest_production_tracker.csv` notes for the age boss chapters and related gate surfaces so future batches keep treating them as real boss spines rather than loose validator buckets.
- Corrected the architecture so Stone Age is explicitly exempt from mandatory boss-gated age completion; Mechanical is now the first age expected to use a real boss spine.

## 2026-03-29 - Industrial Petroleum And Extraction Batch

### Added

- Added live Industrial support chapter `industrial_petroleum_and_extraction` with 15 quests covering:
  - TFMG oil surveying with `Vein Atlas`, `Surface Scanner`, and `Oil Hammer`
  - real TFMG support pieces including `Steel Mechanism`, `Heavy Machinery Casing`, `Machine Input`, `Industrial Pipe`, and `Steel Fluid Tank`
  - the honest pumpjack structure path with `Pumpjack Base`, `Pumpjack Hammer Holder`, and `Pumpjack Crank`
  - distillation setup through `Steel Distillation Controller`, `Steel Distillation Output`, and `Firebox`
  - Create Ore Excavation starter infrastructure with `Sample Drill`, `Drilling Machine`, and `Extractor`
  - Railways fuel-transfer support with `Fuel Tank` and `Portable Fuel Interface`

### Changed

- Reordered Industrial support chapter flow so `industrial_petroleum_and_extraction` sits between `industrial_create_process_infrastructure` and `industrial_industrial_foregoing`.
- Updated Industrial planning docs so `industrial_pneumaticcraft` depends on `industrial_petroleum_and_extraction` in addition to `industrial_power_grids`.
- Documented the shared-oil rule: TFMG/Create now owns the early petroleum chain and later PneumaticCraft should consume the shared tagged oil products instead of teaching a parallel oil-production ladder.

## 2026-03-29 - Industrial Create Process Infrastructure Pass

### Added

- Added a new live Industrial support chapter: `industrial_create_process_infrastructure.snbt`.
- Added `17` authored quests covering the first dense Create-side factory-expansion lane:
  - `Mechanical Crafter`
  - `Fluid Tank`
  - `Mechanical Pump`
  - `Spout`
  - `Basic Energiser`
  - `Electrical Connector`
  - `Overcharged Iron`
  - `Heat Pipe`
  - `Heater`
  - `Stirling Engine`
  - `Molten Brass`
  - `Rolling Mill`
  - `Capacitor`
  - `Wire Setup`
  - `Electric Motor`
  - `Alternator`
  - `Process Line Ready`

### Changed

- Reordered Industrial chapter indexes so the new Create process chapter sits directly after `Modern Industrialization`.
- Updated authored quest count from `263` to `280`.
- Updated tracker, roadmap, chapter plan, and source audit so the Create-side Industrial support arc is now live and active instead of implied by scattered addon presence.

### Why

- Base Create already had a real early backbone, but Industrial was still underusing the Create-side addons that can deliberately force larger, denser factory layouts.
- This pass turns that missing ecosystem into one honest support arc built around mechanical crafting, fluid infrastructure, powered heat, energising, rolling, and electric rotation instead of novelty one-off blocks.

## 2026-03-27 - Stone Survival Onboarding Cleanup Pass

### Changed

- Merged the old `Shelter, Heat, and Sleep` live chapter into the first Stone survival chapter.
- Rebuilt the opening Stone survival lane around the actual onboarding loop:
  - campfire
  - furnace
  - bottles
  - purified water
  - bandages
  - bed
  - chest
  - torches
  - weather gear
  - survival reserve
- Removed duplicate early survival asks that repeated the same lesson:
  - second purified-water stock quest
  - second bandage stock quest
  - duplicate hoe check in farming
  - farming water/temperature reminder quests that belonged in the opener
- Moved Stone travel to start after the new survival-reserve capstone instead of after a mid-shelter quest.
- Simplified the Iron gate so it now depends on the real survival-onboarding capstone, food stabilization, and the travel endpoint.

### Why

- The early Stone path was fragmented into thin chapters and repeated the same survival items without teaching new ideas.
- New players need one clear survival-onboarding arc before farming, travel, and Iron readiness start branching.
- This pass keeps the Stone opening focused on real survival problems: thirst, injury, warmth, shelter, lighting, and supply prep.

## 2026-03-26 - Immersive Engineering Support Cluster Pass

### Added

- Added a new live Mechanical support chapter: `mechanical_engineers_handwork.snbt`.
- Added `13` authored quests for the first bounded Immersive Engineering workshop lane:
  - `Coke Bricks`
  - `First Coke`
  - `Treated Wood`
  - `Engineer's Crafting Table`
  - `Engineer's Workbench`
  - `Copper Plates`
  - `Copper Wire`
  - `Wire Coils`
  - `Low Voltage Connectors`
  - `Breaker Switch`
  - `Conveyor Belt`
  - `Basic Engineering`
  - `Workshop Stock`

### Changed

- Reordered Mechanical chapter indexes so `Engineer's Handwork` now sits directly after `Ironwork and Workstations`.
- Wired `Workshop and Industrial Prep` to the new Mechanical IE capstone so Expedition industrial prep now follows a real starter IE workshop baseline.
- Bumped `implemented_authored_quest_count` from `213` to `226`.
- Updated the tracker, roadmap, and chapter plan so `mechanical_engineers_handwork` is now live and active instead of scaffold-only.

### Why

- The next clean live cluster was early `Immersive Engineering` support, not a new competing spine.
- Mechanical needed a truthful workshop arc that teaches real IE objects and setup milestones instead of jumping from hand tools straight to later industry prep.
- This pass closes the hidden copper-plate prerequisite for early wiring and keeps the IE lane aligned with live Expedition and Industrial chapters.

## 2026-03-25 - Quest Design Pass 1

### Added

- Created the authoritative quest design files under [`config/progression`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20%28test5%29_/config/progression).
- Locked the authored quest target at `2200` new quests minimum.
- Formalized the seven-group questbook structure:
  - Stone Age
  - Mechanical Age
  - Expedition Age
  - Industrial Age
  - Space Age
  - Ascension
  - Annexes
- Defined chapter ordering, density policy, reward policy, and no-checkmark quest rule.
- Mapped live `test5` systems to AOF and ATM10 source chapters.
- Produced a machine-readable chapter registry with per-group and per-chapter quest targets.
- Added a regression checklist under [`tests/progression`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20%28test5%29_/tests/progression).

### Locked Decisions

- Existing imported quest content does not count toward the authored target.
- `Minecolonies` and `When Dungeons Arise` stay as annexes.
- Future age groups remain hidden until unlocked.
- Boss progress lives inside each age.
- `Advent of Ascension` remains excluded because it is not in the live modpack.
- Quest text is minimal by default: titles and one-line subtitles are preferred, body descriptions are usually omitted.

### Why

- The current `test5` questbook is a scaffold, not a finished progression surface.
- A very large authored questbook needs authoritative planning files or the eventual SNBT pass will become inconsistent and unmaintainable.
- The live pack has enough branch systems, dimensions, bosses, survival mechanics, and automation overlap to justify a dense questbook without resorting to fake filler.

### Intent for Next Pass

- Scaffold chapter groups and new chapter files against the registry.
- Expand Stone and Mechanical age chapters first.
- Keep annex connectors separate from imported annex content.

## 2026-03-25 - Quest Scaffolding Pass 2

### Added

- Added the `Annexes` chapter group to the live FTB Quests group list.
- Added `51` new authored scaffold quests across:
  - `Water, Weather, and Wounds`
  - `Shelter, Heat, and Sleep`
  - `Travel, Routes, and Waystones`
  - `First Structures and Controlled Combat`
  - `Ironwork and Workstations`
  - `Create Foundations`
  - `Create Food Relief`
  - `Workshop Logistics and Storage`
  - `Annexes Index and Signposting`
- Added minimal-title localization for the new scaffold quest nodes.

### Changed

- Moved `Minecolonies` and `When Dungeons Arise` into the new `Annexes` group.
- Reordered early Stone and Mechanical chapter flow so the new scaffolding sits between the existing primitives and the existing gate chapters.
- Renamed the placeholder `First Tools` chapter display to `Diamond Threshold`.
- Replaced the placeholder quest title `test` with `Metal Stockpile`.
- Corrected the `Diamonds` stage reward from `end_age` to `automation_age` so the live questbook no longer skips a full age.

### Why

- The questbook needed real structure before large-scale quest authoring could continue safely.
- Annex content had to be separated now so the main age spine stays readable as the book grows.
- Early quest flow now teaches by build order and dependency instead of relying on descriptive text.

## 2026-03-25 - Cleanup and Reconciliation Pass 3

### Renamed

- Renamed legacy chapter files to match the quest plan:
  - `age0_awakening.snbt` -> `stone_awakening_and_salvage.snbt`
  - `age1_kitchen_garden.snbt` -> `stone_food_forage_and_nutrition.snbt`
  - `stone_travel_routes_and_readiness.snbt` -> `stone_travel_routes_and_waystones.snbt`
  - `first_tools.snbt` -> `diamond_threshold.snbt`
  - `diamonds.snbt` -> `blaze_breakthrough.snbt`
  - `enter_nirvana.snbt` -> `ascension_entry_and_scale_shift.snbt`

### Changed

- Normalized live chapter titles to match the design files:
  - `Awakening and Salvage`
  - `Food, Forage, and Nutrition`
  - `Travel, Routes, and Waystones`
  - `Annexes Index and Signposting`
  - `Entering the Iron Era`
  - `Entry and Scale Shift`
- Reassigned the old Expedition gate placeholder from a diamond task to a blaze-rod task so the live `automation_age` grant still belongs to `Blaze Breakthrough`.
- Left existing chapter and quest IDs stable so rename cleanup would not break live FTB Quests dependencies.

### Why

- The live book had drifted into a mix of placeholder-era names, plan names, and misowned gate chapters.
- This pass reconciles filenames, chapter titles, and gate intent without adding new authored chapter lines.
- At this point in the timeline, `Diamonds and Branch Unlocks` was still planned-only and not yet scaffolded as a live chapter.

## 2026-03-25 - Expedition Opener Scaffold Pass 4

### Added

- Added a new live Expedition scaffold chapter: `diamonds_and_branch_unlocks.snbt`.
- Added `3` minimum-viable opener/signpost quests in that chapter:
  - diamond confirmation
  - enchanting entry
  - branch compass signpost

### Changed

- Updated `blaze_breakthrough.snbt` to depend on `diamonds_and_branch_unlocks` so Expedition flow now goes:
  - `diamond_threshold` -> `diamonds_and_branch_unlocks` -> `blaze_breakthrough`
- Bumped `implemented_authored_quest_count` from `51` to `54`.
- Added the new scaffold chapter ID to `implemented_scaffold_chapters`.
- Added chapter and quest localization entries for the new opener.
- Updated source audit text to reflect that `Diamonds and Branch Unlocks` is now live scaffold, not planned-only.

### Why

- The design files already required a distinct Expedition opener chapter, but live quest files only had the later `Blaze Breakthrough` gate.
- This pass inserts the missing opener with minimal scope so future Expedition branch authoring can attach cleanly without changing gate ownership.

## 2026-03-26 - Industrial Power Grids Support Pass

### Added

- Added a new Industrial support chapter file: `industrial_power_grids.snbt`.
- Added `12` bounded quests covering first-wave generation, buffering, distribution, and machine-support power links.

### Changed

- Kept storage ownership consistent with the AE2-required model:
  - no RS requirements were added in Industrial chapters
  - AE2 support tie-in was added through power input tasks (`Energy Acceptor`, `Energy Cell`, `Vibration Chamber`)
- Kept Oritech as the primary Industrial spine and anchored `industrial_power_grids` from `industrial_factory_logistics` capstone (`3400000000004239`).
- Updated chapter localization and new quest title/subtitle entries for IDs `3400000000004310` through `3400000000004336`.
- Updated planning/control docs:
  - `quest_chapter_plan.json`
  - `quest_production_tracker.csv`
  - `quest_production_roadmap.md`
- Updated authored quest count from `201` to `213`.
- Reclassified `industrial_power_grids` as support in tracker/roadmap alignment and marked it active at `12` live quests.

### Why

- Automation needed a dedicated power support lane to reinforce factory structure without competing with the Oritech processing spine.
- This pass closes the next missing support lane while preserving stabilized gate logic and the AE2-required / RS-optional storage model.

## 2026-03-25 - Expedition Opener Signpost Pass 5

### Changed

- Expanded `diamonds_and_branch_unlocks.snbt` from a bare opener into a bounded signpost chapter.
- Added two lightweight progression checks in the opener:
  - early enchanting fuel prep (`lapis_lazuli`)
  - first power-prep materials (`redstone`)
- Kept `Blaze Breakthrough` as the Expedition -> Industrial gate and left all stage grant logic unchanged.
- Added concise subtitle guidance in localization to clarify:
  - first Expedition branch destinations
  - first recommended power targets
  - what remains locked until `Blaze Breakthrough`
- Bumped `implemented_authored_quest_count` from `54` to `56`.

### Why

- The player needed immediate direction after entering Expedition without authoring full branch chapter lines yet.
- This pass keeps guidance bounded and practical while preserving existing chapter/gate architecture for later expansion.

## 2026-03-25 - Expedition Storage Starter Pass 6

### Added

- Added one bounded Expedition starter branch chapter: `expedition_storage_uplift.snbt`.
- Added `5` item-driven quests for chest-tier progression:
  - base chest
  - iron chest
  - gold chest
  - diamond chest
  - netherite-later marker

### Changed

- Wired the new chapter to start from the Expedition opener signpost quest (`3400000000002416`) so branch entry is gated by the opener flow.
- Kept gate ownership and stage grants unchanged:
  - `diamond_threshold` remains Mechanical gate ownership
  - `blaze_breakthrough` remains Expedition -> Industrial gate
- Marked the netherite tier quest with `progressivestages_required_stage: "automation_age"` so post-diamond storage tiering is deferred until the next age starts.
- Added chapter and quest localization entries for the new storage starter chapter.
- Bumped `implemented_authored_quest_count` from `56` to `61`.
- Added `expedition_storage_uplift` to `implemented_scaffold_chapters`.

### Why

- Expedition needed one high-value, practical starter branch immediately after opener routing.
- A chest-tier chain is intuitive, item-driven, and naturally teaches the early storage progression ceiling without requiring manual checkpoints.

## 2026-03-25 - Refined Storage Entry Pass 7

### Added

- Added one bounded Expedition follow-up chapter: `expedition_refined_storage_entry.snbt`.
- Added `5` item-driven entry/signpost quests:
  - quartz reserve
  - redstone reserve
  - first RS cable batch
  - first disk drive
  - portable access marker for later progression

### Changed

- Kept gate ownership and stage grants unchanged.
- Anchored the new chapter cleanly after `expedition_storage_uplift` using the accessible diamond-tier completion point.
- Deferred portable digital access by stage-checking the final marker quest with `progressivestages_required_stage: "automation_age"`.
- Added localization for the new chapter and quest titles/subtitles.
- Bumped `implemented_authored_quest_count` from `61` to `66`.
- Added `expedition_refined_storage_entry` to `implemented_scaffold_chapters`.

### Why

- Expedition needed a digital storage on-ramp that teaches value and prep without expanding into a full Refined Storage tree.
- This pass creates a bounded, practical entry lane and leaves deeper storage networks and AE2 parallel implementation for later chapters.

## 2026-03-25 - Enchanting Starter Pass 8

### Added

- Added one bounded Expedition starter chapter: `expedition_enchanting_and_apotheosis_entry.snbt`.
- Added `5` item-driven starter quests:
  - enchanting table confirmation
  - lapis supply
  - bookshelf prep
  - first practical enchanted-book milestone
  - Apotheosis growth marker

### Changed

- Kept gate ownership and existing stage grants unchanged.
- Anchored this chapter to the Expedition opener completion route (`diamonds_and_branch_unlocks` path).
- Added chapter/quest localization entries aligned with current naming style.
- Bumped `implemented_authored_quest_count` from `66` to `71`.
- Added `expedition_enchanting_and_apotheosis_entry` to `implemented_scaffold_chapters`.

### Why

- Expedition needed a practical enchant starter lane that activates real enchanting behavior without immediately expanding into a full optimization tree.
- This pass establishes the base enchanting loop and marks Apotheosis as the next growth direction while keeping scope bounded.

## 2026-03-25 - Aether/Twilight Starter Pass 9

### Added

- Added one bounded Expedition adventure starter chapter: `expedition_aether_twilight_first_destinations.snbt`.
- Added `5` item-driven starter quests:
  - entry kit prep
  - first Aether destination confirmation
  - first Twilight destination confirmation
  - first practical drop benchmarks from both routes
  - later boss-relic marker

### Changed

- Kept gate ownership and existing stage grants unchanged.
- Anchored this chapter to the Expedition opener route (`diamonds_and_branch_unlocks` path) so it sits alongside existing starter branches.
- Deferred deeper boss-relic completion by stage-checking the final marker quest with `progressivestages_required_stage: "automation_age"`.
- Added chapter/quest localization entries for the new bounded adventure starter.
- Bumped `implemented_authored_quest_count` from `71` to `76`.
- Added `expedition_aether_twilight_first_destinations` to `implemented_scaffold_chapters`.

### Why

- Expedition needed a first-destination adventure lane that teaches where to go and what to carry before a full dimension tree exists.
- This pass creates a practical entry route while leaving deeper rewards and hard encounters for later chapter work.

## 2026-03-25 - Enchanting Follow-Up Pass 10

### Added

- Added one bounded Expedition second-layer chapter: `expedition_enchanting_and_apotheosis_followup.snbt`.
- Added `5` item-driven follow-up quests:
  - practical enchant consistency target
  - Apotheosis cutting table setup
  - first gem integration
  - combat/exploration readiness handoff
  - later mythic marker

### Changed

- Kept gate ownership and existing stage grants unchanged.
- Chained the follow-up chapter after `expedition_enchanting_and_apotheosis_entry`.
- Deferred mythic-tier progression by stage-checking the final marker quest with `progressivestages_required_stage: "automation_age"`.
- Added chapter/quest localization entries for the follow-up chapter.
- Bumped `implemented_authored_quest_count` from `76` to `81`.
- Added `expedition_enchanting_and_apotheosis_followup` to `implemented_scaffold_chapters`.

### Why

- Expedition enchanting needed one practical second layer before the full Apotheosis branch expansion.
- This pass increases useful enchant reliability and introduces first meaningful Apotheosis integration while keeping scope bounded.

## 2026-03-25 - Mechanical Rotational Logistics Starter Pass 11

### Added

- Added one bounded Mechanical starter chapter: `mechanical_rotational_power_and_first_logistics.snbt`.
- Added `7` item-driven starter quests:
  - water wheel baseline
  - windmill bearing option
  - large cogwheel batch
  - gearbox routing
  - belt connector line
  - andesite funnel transfer
  - chute vertical transfer

### Changed

- Kept gate ownership and existing stage grants unchanged.
- Anchored this chapter after `mechanical_create_foundations` using the mechanical press milestone.
- Added chapter/quest localization entries aligned with existing naming/subtitle style.
- Bumped `implemented_authored_quest_count` from `81` to `88`.
- Added `mechanical_rotational_power_and_first_logistics` to `implemented_scaffold_chapters`.
- Normalized Mechanical ordering so this chapter sits cleanly between foundations and later Mechanical branches:
  - `mechanical_create_food_relief` `order_index` `2` -> `3`
  - `mechanical_workshop_logistics_and_storage` `order_index` `3` -> `4`
  - `diamond_threshold` `order_index` `4` -> `5`

### Why

- Mechanical Age needed a practical first machine-backbone chapter before expanding into broader branch depth.
- This pass establishes hands-on rotational power and first logistics flow without widening into industrial-scale automation.

## 2026-03-25 - Mechanical Food and Farm Handling Pass 12

### Added

- Added one bounded Mechanical follow-up chapter: `mechanical_food_and_farm_handling.snbt`.
- Added `6` item-driven starter quests:
  - mechanical plough setup
  - deployer planting step
  - mechanical harvester crop collection
  - portable storage interface offload
  - wheat flour processing target
  - dough throughput target

### Changed

- Kept gate ownership and existing stage grants unchanged.
- Anchored the chapter after `mechanical_rotational_power_and_first_logistics`.
- Positioned this chapter in Mechanical order flow between rotational backbone and broader food relief:
  - `mechanical_create_food_relief` `order_index` `3` -> `4`
  - `mechanical_workshop_logistics_and_storage` `order_index` `4` -> `5`
  - `diamond_threshold` `order_index` `5` -> `6`
- Added chapter/quest localization entries.
- Bumped `implemented_authored_quest_count` from `88` to `94`.
- Added `mechanical_food_and_farm_handling` to `implemented_scaffold_chapters`.

### Why

- Mechanical Age needed a Create-first food reliability lane that solves everyday survival and kitchen throughput pain before wider cross-mod food relief.
- This pass keeps scope practical and hands-on without expanding into industrial farming abstractions.

## 2026-03-25 - Mechanical Tree Farming and Wood Relief Pass 13

### Added

- Added one bounded Mechanical follow-up chapter: `mechanical_tree_farming_and_wood_relief.snbt`.
- Added `6` item-driven starter quests:
  - tree farm controller setup
  - structure block framing
  - input controller setup
  - first oak tree farm unit
  - repeatable log throughput target
  - plank conversion relief target

### Changed

- Kept gate ownership and existing stage grants unchanged.
- Anchored this chapter directly after `mechanical_rotational_power_and_first_logistics` as a sibling branch.
- Normalized Mechanical chapter order so the new wood lane sits before broader food/logistics chapters:
  - `mechanical_create_food_relief` `order_index` `4` -> `5`
  - `mechanical_workshop_logistics_and_storage` `order_index` `5` -> `6`
  - `diamond_threshold` `order_index` `6` -> `7`
- Added chapter/quest localization entries.
- Bumped `implemented_authored_quest_count` from `94` to `100`.
- Added `mechanical_tree_farming_and_wood_relief` to `implemented_scaffold_chapters`.

### Why

- Mechanical Age needed a non-industrial, repeatable wood-supply lane to reduce building and workshop expansion friction.
- This pass keeps wood progression centered on Multiblock Farming tree systems rather than Create-native factory identity.

## 2026-03-25 - Stone Farming Pressure + Mechanical Handoff Cleanup Pass 14

### Added

- Added one bounded Stone Age chapter: `stone_farming_seasons_and_survival_pressures.snbt`.
- Added `8` practical quests for:
  - first manual farm setup
  - crop planting with season awareness
  - weather check habit
  - hydration reminder
  - temperature gear prep
  - manual harvest workload
  - food reserve setup
  - clear signpost to later Mechanical farming tools

### Changed

- Kept gate ownership and existing stage grants unchanged.
- Positioned the new Stone chapter after `stone_food_forage_and_nutrition` in visible order:
  - `stone_travel_routes_and_waystones` `order_index` `4` -> `5`
  - `stone_structures_and_controlled_combat` `order_index` `5` -> `6`
  - `entering_the_iron_era` `order_index` `6` -> `7`
- Updated Mechanical handoff clarity with minimal changes:
  - `mechanical_create_food_relief` opener now depends on both `stone_food_forage_and_nutrition` and `mechanical_rotational_power_and_first_logistics` completion (`3400000000002342`), so timing follows the rotational backbone.
  - Replaced the duplicated `create:mechanical_harvester` milestone in `mechanical_create_food_relief` with `farmersdelight:cooking_pot` to sharpen branch identity.
- Updated localization for the new Stone chapter using the requested short title/subtitle set (including `supply` in quest 7 wording).
- Bumped `implemented_authored_quest_count` from `100` to `108`.
- Added `stone_farming_seasons_and_survival_pressures` to `implemented_scaffold_chapters`.

### Why

- Stone now teaches farming pressure by doing: season checks, hydration, weather prep, and manual harvest effort.
- Mechanical remains the place where labor relief starts, and the cleanup keeps the handoff from Stone into Mechanical food branches clearer.

## 2026-03-26 - Stone/Mechanical Validity Cleanup Pass 15

### Changed

- Kept all gate grants and gate ownership unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Fixed Stone hydration progression validity:
  - Replaced Stone canteen requirements with Stone-safe purified-water milestones in:
    - `stone_water_weather_and_wounds`
    - `stone_farming_seasons_and_survival_pressures`
  - Replaced Stone `first_aid_supplies` requirement with a stronger bandage reserve milestone.
  - Updated chapter icon from canteen to purified water bottle for consistency.
- Reintroduced canteen at early iron utility timing:
  - Added `Make a Canteen` quest to `mechanical_ironwork_and_workstations`.
- Kept the prior Mechanical food-branch distinction and overlap cleanup:
  - `mechanical_food_and_farm_handling` remains base Create starter.
  - `mechanical_create_food_relief` remains broader cross-mod relief.
- Added/updated localization keys for the adjusted Stone and Mechanical quests.
- Bumped `implemented_authored_quest_count` from `108` to `109`.

### Why

- Canteen is iron-gated by live recipe and is not valid as a Stone requirement.
- This pass preserves progression philosophy: Stone teaches survival pressure, while early iron/Mechanical introduces the first practical relief utility.

## 2026-03-26 - Stone Consolidation and Arc Deepening Pass 16

### Changed

- Consolidated Stone chapters into denser arcs with quest IDs preserved:
  - merged `stone_food_forage_and_nutrition` + `stone_farming_seasons_and_survival_pressures` into `stone_food_and_farming_pressures`
  - merged `stone_travel_routes_and_waystones` + `stone_structures_and_controlled_combat` into `stone_travel_and_controlled_combat`
- Removed the two superseded chapter files after migrating their quest nodes.
- Re-sequenced merged Stone chapter order:
  - `stone_water_weather_and_wounds` (`0`)
  - `stone_shelter_heat_and_sleep` (`1`)
  - `stone_food_and_farming_pressures` (`2`)
  - `stone_travel_and_controlled_combat` (`3`)
  - `entering_the_iron_era` (`4`)
- Strengthened Stone gate validity and pacing:
  - `entering_the_iron_era` now depends on completion points from all four merged Stone arcs (`101C`, `111F`, `03D1`, `131F`) before granting `iron_age`.
- Updated chapter localization and progression/support files to match merged structure.

### Why

- Stone had too many shallow top-level chapters with overlapping lessons.
- This pass keeps total useful depth while reducing fragmentation, making Stone feel more authored and progression-coherent.

## 2026-03-26 - Mechanical Tightening and Gate Clarity Pass 17

### Changed

- Preserved non-negotiable gate grants unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Fixed hard Mechanical dependency breakage caused by drifted quest IDs:
  - restored first quest IDs in:
    - `mechanical_rotational_power_and_first_logistics` (`3400000000002330`)
    - `mechanical_food_and_farm_handling` (`3400000000002350`)
    - `mechanical_tree_farming_and_wood_relief` (`3400000000002370`)
- Tightened food-branch sequencing without merging chapters:
  - `mechanical_create_food_relief` now opens after `mechanical_food_and_farm_handling` completion (`340000000000235F`).
  - Mid-branch tasks now depend on the slicer step (`3400000000002213`) to prevent bypassing branch setup.
- Resolved unresolved item placeholder:
  - Replaced `ftbquests:missing_item` fridge task with direct `cookingforblockheads:fridge`.
- Hardened Mechanical gate visibility pacing:
  - `diamond_threshold` first quest now depends on core Mechanical spine completion markers (`201F`, `2122`, `2342`) in addition to iron gate completion.

### Why

- Mechanical chapters were mostly healthy, but remaining sequencing drift and one placeholder item weakened authored feel.
- This pass improves chapter identity boundaries and gate clarity with minimal structural change and no chapter sprawl.

## 2026-03-26 - Gate Transition Integrity Pass 18

### Changed

- Preserved non-negotiable gate grants unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Tightened `blaze_breakthrough` dependency targets to explicit Expedition branch capstones:
  - `3400000000002619` (`expedition_refined_storage_entry` pre-automation endpoint)
  - `3400000000002819` (`expedition_aether_twilight_first_destinations` pre-automation endpoint)
  - `3400000000002919` (`expedition_enchanting_and_apotheosis_followup` pre-automation endpoint)
- Removed prior weak dependency on `3400000000002400` (chapter-level `diamonds_and_branch_unlocks` ID) to avoid gate unlock drift.

### Why

- Gate chapters should key off meaningful arc capstones, not a nearby chapter ID.
- This keeps `blaze_breakthrough` earned through the implemented pre-automation Expedition spine while avoiding a broad restructure.

## 2026-03-26 - Mod Coverage Control Pass 19

### Changed

- Added a dedicated coverage tracker:
  - `config/progression/mod_coverage_matrix.md`
  - includes tiering (`Tier A/B/C`), coverage levels (`none/incidental/partial/meaningful/full/core`), ownership, and cross-mod linkage tracking.
- Added one bounded cross-mod storage refinement without changing gate logic:
  - `expedition_refined_storage_entry` now includes an automation-gated AE2 prep handoff quest:
    - quest id `340000000000261F`
    - tasks:
      - `3400000000002620` (`ae2:certus_quartz_crystal` x32)
      - `3400000000002621` (`ae2:fluix_crystal` x16)
  - This quest depends on RS disk-drive capstone `3400000000002619`.
- Added localization for the new handoff quest in `en_us.snbt`:
  - title: `AE2 Material Stash`
  - subtitle: `Start stockpiling Certus and Fluix for your future AE2 network line.`

### Why

- Coverage needed an operational control surface, not one-off audits.
- The AE2 prep handoff strengthens RS-to-future-digital cross-mod continuity with a minimal, low-risk edit and no chapter sprawl.

## 2026-03-26 - Current-Age Coverage Integration Pass 20

### Changed

- Preserved non-negotiable gate ownership and grant commands unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Added bounded RSRequestify live integration inside current Expedition storage flow:
  - `expedition_refined_storage_entry.snbt` new quest `3400000000002623`
  - tasks:
    - `3400000000002624` (`rsrequestify:requester`)
    - `3400000000002625` (`rsrequestify:crafting_emitter`)
  - dependency anchored to RS capstone `3400000000002619`
  - kept full AE2 branch deferred (existing AE2 prep remains automation-gated).
- Added bounded Ars Nouveau bridge in Expedition opener:
  - `diamonds_and_branch_unlocks.snbt` new quest `3400000000002420`
  - tasks:
    - `3400000000002421` (`ars_nouveau:source_gem` x4)
    - `3400000000002422` (`ars_nouveau:scribes_table`)
  - dependency anchored to branch signpost completion `3400000000002416`
  - no full Ars chapter rollout in this pass.
- Added localization keys:
  - `quest.3400000000002623.*` (`Request and Stock`)
  - `quest.3400000000002420.*` (`Ars Setup Supplies`)
- Updated coverage/control docs:
  - `mod_coverage_matrix.md` now marks RSRequestify as live/meaningful and Ars Nouveau as live/partial bridge coverage
  - `quest_chapter_plan.json` updated `expedition_refined_storage_entry` source mods to include `RSRequestify`
  - `quest_source_audit.md` updated Expedition rows to reflect new RSRequestify and Ars bridge integration

### Why

- RS + RSRequestify is the intended Diamond/Expedition storage solution and needed explicit live representation.
- Ars Nouveau is planned for Expedition and required at least a real bridge beat now, without forcing premature full-arc sprawl.

## 2026-03-26 - Expedition Refinement Pass 21 (Ars Nouveau)

### Changed

- Preserved stable gate logic and grant ownership unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Added a bounded live Ars Nouveau Expedition starter chapter:
  - `expedition_ars_nouveau.snbt` (`3400000000002A00`)
  - sequence:
    - `3400000000002A10` Source Gem stock
    - `3400000000002A13` Scribe's Table
    - `3400000000002A16` Novice Spellbook
    - `3400000000002A19` Arcane Pedestal
    - `3400000000002A1C` Enchanting Apparatus
  - chapter opener depends on both:
    - `3400000000002420` (Expedition opener Ars bridge)
    - `3400000000002710` (Enchanting entry)
- Added localization:
  - chapter title `chapter.3400000000002A00.title`
  - quest titles/subtitles for `2A10`, `2A13`, `2A16`, `2A19`, `2A1C`
- Updated progression control docs:
  - `quest_chapter_plan.json` implemented scaffold list now includes `expedition_ars_nouveau`
  - `mod_coverage_matrix.md` promotes Ars Nouveau from bridge-only partial to meaningful live coverage
  - `quest_source_audit.md` updated Ars Nouveau status to bounded live starter

### Why

- Ars Nouveau was the highest-value remaining current-age gap with strong plan alignment and clear integration points.
- This pass promotes Ars from token bridge coverage into a real Expedition beat without gate churn or chapter sprawl.

## 2026-03-26 - Expedition Support Utility Pass 22 (Waystones + Backpacks)

### Changed

- Preserved stable gate logic and grant ownership unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Added tightly scoped Expedition support integration inside `expedition_aether_twilight_first_destinations`:
  - new `Route Anchor` quest `3400000000002820` requiring `waystones:waystone`
  - new `Expedition Pack` quest `3400000000002823` requiring `sophisticatedbackpacks:gold_backpack`
- Wired support utility into branch progression (no new chapter):
  - Aether and Twilight branch-entry quests (`2813`, `2816`) now require both support beats in addition to shield prep
  - keeps travel routing and inventory logistics as explicit Expedition readiness requirements
- Added localization keys:
  - `quest.3400000000002820.*`
  - `quest.3400000000002823.*`
- Updated progression control docs:
  - `quest_chapter_plan.json` `expedition_aether_twilight_first_destinations` source mods now include `Waystones` and `Sophisticated Backpacks`
  - `quest_source_audit.md` notes new waystone/backpack support integration in this chapter
  - `mod_coverage_matrix.md` promotes Waystones and Sophisticated Backpacks support coverage to meaningful live status

### Why

- Waystones and Sophisticated Backpacks were still underrepresented despite strong current-age utility value.
- Integrating both in a single existing Expedition adventure starter chapter gives high player-facing value with minimal structural risk and no chapter sprawl.

## 2026-03-26 - Utility Scope Correction Pass 23 (Waystones + Backpacks)

### Changed

- Preserved stable gate logic and grant ownership unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Kept Waystones and Sophisticated Backpacks in the existing Expedition destination chapter as utility support only:
  - retained `Route Anchor` quest `3400000000002820` as a single minor optional travel beat
  - expanded backpacks into a short optional two-step utility beat:
    - new `Trail Pack` quest `3400000000002826` (`sophisticatedbackpacks:backpack`)
    - existing `Expedition Pack` quest `3400000000002823` now depends on `3400000000002826`
- Removed utility mods from branch-critical progression requirements:
  - `3400000000002813` and `3400000000002816` now depend only on `3400000000002810` again
  - Waystones/Backpacks no longer gate destination branch continuation
- Added localization keys:
  - `quest.3400000000002826.*`
  - updated subtitle for `quest.3400000000002823`
- Updated support control docs for utility-scoped representation:
  - `quest_source_audit.md` now marks waystone/backpack support beats as optional utility prep
  - `mod_coverage_matrix.md` reclassifies routefinding Expedition waystone handling to utility-level partial coverage and records backpacks as a bounded utility beat (not a branch)

### Why

- Utility/support mods should relieve pain points without becoming major progression walls.
- This correction keeps the live utility value while restoring clearer branch identity and avoiding coverage inflation.

## 2026-03-26 - Tech-First Nether/Expedition Recenter Pass 24

### Changed

- Preserved non-negotiable gate grant ownership unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Recentered `blaze_breakthrough` feeder dependencies toward tech-first Expedition progress:
  - replaced RS disk-drive capstone dependency `3400000000002619` with RSRequestify capstone `3400000000002623`
  - replaced Aether/Twilight capstone dependency `3400000000002819` with Ars capstone `3400000000002A1C`
  - retained enchanting/apotheosis follow-up capstone `3400000000002919`
- Added a bounded early Immersive Engineering utility beat to Mechanical:
  - `mechanical_ironwork_and_workstations.snbt`
  - new `Engineer's Hammer` quest `3400000000002025` (`immersiveengineering:hammer`)
  - new `Wires and Plates` quest `3400000000002028` (`immersiveengineering:wirecutter` + `immersiveengineering:plate_iron` x4)
- Tightened Mechanical -> Diamond transition readiness:
  - `diamond_threshold` preparation quest `5D89181DA25D6E1B` now also depends on IE handwork capstone `3400000000002028`
- Added localization:
  - `quest.3400000000002025.*`
  - `quest.3400000000002028.*`
- Updated support/control docs to reflect tech-first weighting:
  - `quest_source_audit.md` now marks Aether/Twilight as optional support and records IE handwork presence
  - `mod_coverage_matrix.md` adds IE early-handwork row and updates Blaze feeder, RSRequestify, and Aether/Twilight status text

### Why

- This pack’s current phase should prioritize base maturity, Nether-fed digital storage, and future-industry preparation over early mandatory dimension branching.
- Aether/Twilight remains live, but automation entry now depends on systems that materially feed future tech progression.

## 2026-03-26 - Production Framework Pass 25

### Changed

- Locked the production scaling model into the design contract:
  - `quest_design_bible.md` now defines default chapter density classes
  - added budget authority rules so age-group budgets outrank drifting per-chapter targets
  - added a full-pack `2200` distribution model for spine/support/optional/mastery content
- Added a dedicated authored-quest production roadmap:
  - `quest_production_roadmap.md`
  - includes authoritative age budgets, current backlog by age, chapter-budget model, Expedition completion plan, and Automation-age scaffold order
- Added a dedicated chapter-level production tracker:
  - `quest_production_tracker.csv`
  - fields include chapter owner, mod cluster, branch type, target quest count, current live count, coverage level, status, links, and notes
  - includes the live but unplanned `expedition_workshop_and_industrial_prep` drift explicitly so it is no longer invisible
- Synced plan metadata with the current live authored count:
  - `quest_chapter_plan.json` `implemented_authored_quest_count` `109` -> `135`
  - added `expedition_workshop_and_industrial_prep` to `implemented_scaffold_chapters`

### Why

- The next bottleneck is no longer local cleanup. It is production control.
- The pack now needs a roadmap and tracker that can scale to `2200` authored quests without frontloading the early game or letting mid/late progression stay hand-wavy.

## 2026-03-26 - Roadmap Production Pass 26

### Changed

- Added quest-writing rules to the design contract:
  - plain, functional titles
  - descriptions only when they materially improve clarity
  - no lore or flavor padding
- Normalized the live Expedition prep chapter into the formal plan:
  - added `expedition_workshop_and_industrial_prep` to the Expedition chapter list in `quest_chapter_plan.json`
  - target `20` quests
  - owner cluster: `Minecraft + Create + Immersive Engineering`
- Rebalanced Expedition planning targets so the age budget is no longer over-allocated:
  - `expedition_apotheosis_and_enchanting` `46` -> `40`
  - `expedition_aether_and_deep_aether` `44` -> `28`
  - `expedition_twilight_forest` `42` -> `28`
  - `expedition_undergarden_and_deeper_frontiers` `40` -> `24`
  - `expedition_treasure_routes_and_clavis_ii` `32` -> `20`
  - `expedition_boss_hunts` `31` -> `19`
  - `annex_wda_bridge` `20` -> `12`
  - Expedition chapter sum now matches the authoritative `385`-quest age budget
- Tightened the first Automation scaffold definition:
  - `industrial_nether_logistics_and_ore_escalation` now carries `assembly` and `synergy` families
  - source ownership expanded to `Minecraft + AllTheOres + Create + Immersive Engineering`
- Updated production control docs:
  - `quest_production_roadmap.md` now treats Workshop/Industrial Prep as the bounded Nether return loop owner
  - `quest_production_tracker.csv` now reflects the normalized Expedition chapter, re-budgeted Expedition side content, and the clarified first Automation scaffold

### Why

- This pass uses the production framework instead of bypassing it.
- Expedition now has a clearer next tech-forward block, and Automation now has a concrete first scaffold instead of a vague future placeholder.

## 2026-03-26 - Nether Loop Build Pass 27

### Changed

- Preserved stable gate grants unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Expanded `expedition_workshop_and_industrial_prep.snbt` from `5` to `12` live quests by building the bounded Nether return loop:
  - retained existing Create / IE prep beats:
    - `Blaze Burner`
    - `Mechanical Mixer`
    - `Treated Wood`
    - `Coke Bricks`
    - `Iron Plates`
  - added Nether / RS / IE / factory-return beats:
    - `Quartz Run`
    - `Blaze Powder`
    - `Quartz-Enriched Iron`
    - `Machine Casing`
    - `Copper Coil`
    - `LV Connectors`
    - `Factory Crafter`
- Added the first live Automation scaffold chapter:
  - `industrial_nether_logistics_and_ore_escalation.snbt`
  - `6` bounded scaffold quests:
    - `Nether Stock`
    - `Quartz-Enriched Iron`
    - `Machine Casings`
    - `Copper Coils`
    - `LV Connectors`
    - `Factory Crafters`
  - opener depends on both:
    - live `blaze_breakthrough` gate quest
    - Expedition prep capstone `Factory Crafter`
- Added localization with plain titles and only two opener subtitles:
  - Expedition opener `Blaze Burner`
  - Industrial opener `Nether Stock`
- Synced the production framework:
  - `quest_chapter_plan.json` `implemented_authored_quest_count` `135` -> `148`
  - `industrial_nether_logistics_and_ore_escalation` added to `implemented_scaffold_chapters`
  - `quest_production_tracker.csv` now marks:
    - `expedition_workshop_and_industrial_prep` as `12` live quests / `active`
    - `industrial_nether_logistics_and_ore_escalation` as `6` live quests / `bounded`
  - `quest_production_roadmap.md` current live authored total `135` -> `148`

### Why

- This is the first roadmap-driven Nether-to-industry build pass.
- It keeps Expedition focused on returning with materials that directly strengthen storage, workshop maturity, and the first Automation on-ramp.

## 2026-03-26 - Industrial On-Ramp Deepening Pass 28

### Changed

- Kept scope bounded to `industrial_nether_logistics_and_ore_escalation` only.
- Expanded the chapter from `6` to `14` live quests to establish a clearer factory-transition identity:
  - ore and material escalation:
    - `Nickel Ingots`
    - `Platinum Ingots`
  - RS batching and machine-part wave:
    - `RS Controller`
  - IE and Create logistics wave:
    - `Coke Fuel`
    - `Belt Stock`
    - `Brass Funnels`
    - `Batch Hoppers`
  - handoff capstone:
    - `Factory Transition Stock`
- Preserved writing rules:
  - plain functional titles
  - no flavor/lore text
  - only one new subtitle, used for the final handoff signpost
- Synced production framework:
  - `quest_chapter_plan.json` `implemented_authored_quest_count` `148` -> `156`
  - `quest_production_tracker.csv` now marks Industrial on-ramp as `14` live quests, `meaningful`, `active`
  - `quest_production_roadmap.md` snapshot updated to live authored `156` and Industrial remaining `406`

### Why

- The chapter now reads as the first industrial material/logistics wave rather than only Expedition prep continuation.
- Oritech remains the next factory-processing spine and is referenced by handoff intent, not prematurely implemented here.

## 2026-03-26 - Oritech Starter Spine Pass 29

### Changed

- Preserved stable gate grants unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Added the first bounded live Oritech chapter:
  - `industrial_oritech.snbt` (`3400000000004100`)
  - `13` quests (`3400000000004110` through `3400000000004136`)
  - chapter opener depends on `Factory Transition Stock` (`3400000000004039`) from `industrial_nether_logistics_and_ore_escalation`
- Implemented starter Oritech arc scope:
  - first materials/components (`steel_ingot`, `electrum_ingot`, `raw_silicon`, machine cores, frames, coils, motors)
  - first machine identity (`basic_generator_block`, `powered_furnace_block`, `charger_block`)
  - first transport setup (`item_pipe`, `energy_pipe`, `wrench`)
  - bounded capstone stock for next Oritech processing depth
- Added localization for chapter and quest names/subtitles with plain titles and minimal descriptions.
- Synced production framework:
  - `quest_chapter_plan.json` `implemented_authored_quest_count` `156` -> `169`
  - added `industrial_oritech` to `implemented_scaffold_chapters`
  - aligned planned chapter dependency to `industrial_nether_logistics_and_ore_escalation`
  - `quest_production_tracker.csv` now marks `industrial_oritech` as live `13` quests, `partial`, `active`
  - `quest_production_roadmap.md` snapshot updated to live authored `169` and Industrial remaining `393`

### Why

- Industrial now has a concrete first Oritech spine chapter immediately after the Nether factory-transition chapter.
- This keeps scope bounded to starter processing identity and avoids widening into full Oritech ecosystem rollout too early.

## 2026-03-26 - Oritech Processing Deepening Pass 30

### Changed

- Preserved stable gate grants unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Deepened `industrial_oritech.snbt` from `13` to `23` quests with a bounded second wave focused on repeatable processing:
  - new machine chain nodes:
    - `Pulverizer` (`340000000000413A`)
    - `Foundry` (`340000000000413D`)
    - `Steam Engine` (`3400000000004149`)
  - new repeatable production stock nodes:
    - `Quartz Dust Batch` (`3400000000004140`)
    - `Coal Dust Batch` (`3400000000004143`)
    - `Foundry Steel Batch` (`3400000000004146`)
  - new throughput/routing upgrade nodes:
    - `Machine Plating Batch` (`340000000000414C`)
    - `Framed Energy Pipe` (`340000000000414F`)
    - `Framed Item Pipe` (`3400000000004152`)
  - new capstone:
    - `Oritech Throughput Stock` (`3400000000004155`)
- Added plain localization entries for the new Oritech quest IDs with minimal subtitles only on process-signpost and capstone nodes.
- Synced production framework:
  - `quest_chapter_plan.json` `implemented_authored_quest_count` `169` -> `179`
  - `quest_production_tracker.csv` now marks `industrial_oritech` as `23` live quests, `meaningful`, `active`
  - `quest_production_roadmap.md` snapshot updated to live authored `179` and Industrial remaining `383`

### Why

- Oritech now reads as a real first factory-processing lane instead of a starter setup checklist.
- The chapter now demonstrates machine chaining and repeatable throughput while staying bounded and avoiding side-lane expansion.

## 2026-03-26 - Factory Logistics Support Pass 31

### Changed

- Preserved stable gate grants unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Added the first bounded Industrial support chapter:
  - `industrial_factory_logistics.snbt` (`3400000000004200`)
  - `14` quests (`3400000000004210` through `3400000000004239`)
  - chapter opener depends on Oritech throughput capstone `3400000000004155`
- Implemented support-lane scope around Oritech:
  - routing and line structure (`brass_funnel`, `brass_tunnel`, `smart_chute`, `mechanical_arm`)
  - buffering and staging (`item_vault`, `depot`, Sophisticated Storage chest/input/output)
  - flow control and signaling (`stockpile_switch`, `content_observer`, `redstone_link`)
  - capstone `Factory Bus Ready` as handoff marker toward `industrial_power_grids`
- Added localization for chapter and quest titles with minimal subtitles only on opener and capstone.
- Synced production framework:
  - `quest_chapter_plan.json` `implemented_authored_quest_count` `179` -> `193`
  - added `industrial_factory_logistics` to `implemented_scaffold_chapters`
  - aligned planned chapter dependency to `industrial_oritech`
  - `quest_production_tracker.csv` now marks `industrial_factory_logistics` as support, live `14` quests, `partial`, `active`
  - `quest_production_roadmap.md` snapshot updated to live authored `193` and Industrial remaining `369`

### Why

- Industrial needed an organization layer around the Oritech spine so Automation reads as a factory age instead of isolated machine placements.
- This pass adds that structure without expanding into side branches or competing with the Oritech spine.

## 2026-03-26 - Storage Ownership Refactor Pass 32

### Changed

- Preserved gate grant commands unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Switched Expedition digital-storage ownership to AE2:
  - added `expedition_ae2_entry.snbt` (`3400000000002650`) with `8` starter quests
  - AE2 starter includes:
    - quartz/fluix material stock
    - first terminal and crafting terminal
    - first ME chest, drive, and 1k cells
    - first storage bus link to practical storage
    - first import/export bus baseline capstone
- Updated gate dependency ownership:
  - `blaze_breakthrough` now depends on AE2 capstone quest `3400000000002666` instead of RSRequestify quest `3400000000002623`
- Demoted RS to optional:
  - chapter display shifted to `Refined Storage Optional`
  - RS chapter remains available but is no longer gate-critical
- Removed RS requirements from mandatory mainline prep/on-ramp chapters:
  - `expedition_workshop_and_industrial_prep`:
    - `refinedstorage:quartz_enriched_iron` -> `ae2:fluix_glass_cable`
    - `refinedstorage:machine_casing` -> `ae2:drive`
  - `industrial_nether_logistics_and_ore_escalation`:
    - `refinedstorage:quartz_enriched_iron` -> `ae2:fluix_glass_cable`
    - `refinedstorage:machine_casing` -> `ae2:drive`
    - `refinedstorage:controller` -> `ae2:chest`
- Added/updated localization for:
  - new AE2 chapter + quest titles
  - RS optional chapter naming and optional-branch subtitles
  - updated title keys for converted AE2 prep quests in Expedition/Industrial chapters
- Synced planning/control docs:
  - `quest_chapter_plan.json` `implemented_authored_quest_count` `193` -> `201`
  - added `expedition_ae2_entry` to implemented scaffold chapter list
  - updated Expedition chapter registry to include required AE2 starter chapter
  - `blaze_breakthrough` plan dependency now points to `expedition_ae2_entry`
  - `quest_production_tracker.csv` now includes `expedition_ae2_entry` as spine and marks RS as optional support
  - `quest_production_roadmap.md` storage policy text now reflects AE2-required / RS-optional ownership and updated live counts

### Why

- AE2 is now the required digital storage language for this technology-first pack.
- RS remains available as an optional convenience branch without owning progression gates.

## 2026-03-26 - Logic Integrity Cleanup Pass 33

### Changed

- Preserved gate grant commands unchanged:
  - `entering_the_iron_era` -> `iron_age`
  - `diamond_threshold` -> `diamond_age`
  - `blaze_breakthrough` -> `automation_age`
- Fixed invalid placeholder task target in Mechanical food relief:
  - replaced `ftbquests:missing_item` wrapper with direct `cookingforblockheads:fridge` item task in quest `340000000000221F`
- Corrected wrong-abstraction tree farming path:
  - merged `mechanical_tree_farming_and_wood_relief` into `mechanical_food_and_farm_handling`
  - removed standalone chapter file `mechanical_tree_farming_and_wood_relief.snbt`
  - replaced fake direct tree-controller progression with real prerequisite chain:
    - `mm_farming:block_crafter_farm`
    - `mm_farming:item_fertilizer_world`
    - `mm_farming:item_upgrade_speed_world`
    - structure/input parts
    - wood-output validation
- Tightened AE2 prerequisite truth in Expedition workshop prep:
  - added dependency on AE2 material baseline quest `3400000000002651` before `Fluix Cable Batch` quest `3400000000002B23`
- Added plain localization titles for touched Mechanical farm/tree and Create food relief quests.

### Framework Sync

- `quest_chapter_plan.json`
  - removed `mechanical_tree_farming_and_wood_relief` from implemented live scaffold list
  - removed standalone Mechanical tree chapter entry from Mechanical group
  - expanded `mechanical_food_and_farm_handling` scope/target/mod coverage for merged tree-lane ownership
- `quest_production_tracker.csv`
  - removed standalone tree-farming row
  - updated `mechanical_food_and_farm_handling` as merged, denser active chapter (`12` live quests)
  - added note for fixed fridge target in `mechanical_create_food_relief`
- `quest_source_audit.md` and `mod_coverage_matrix.md`
  - updated Mechanical farming ownership and AE2/RS storage ownership language to match live logic
- `quest_production_roadmap.md`
  - added note documenting the Mechanical farm/tree consolidation cleanup

### Why

- Cleanup priority was correctness: quest what players can really craft, place, configure, and verify.
- This pass removes invalid abstraction targets, reduces shallow chapter fragmentation, and tightens prerequisite truth without widening progression scope.

## 2026-03-29 - Mechanical Integrity Cleanup Pass 34

### Changed

- Re-anchored Mechanical tree farming so it branches from `Portable Storage Interface` instead of late dough processing:
  - `mechanical_food_and_farm_handling` quest `0FDF8FDB10226330` now depends on `3400000000002359`
- Expanded `mechanical_create_food_relief` into a truthful first kitchen system:
  - added `Kitchen Stove` (`3400000000002222`) for `farmersdelight:stove`
  - added `Kitchen Sink` (`3400000000002225`) for `cookingforblockheads:sink`
  - `Kitchen Fridge` (`340000000000221F`) now depends on the real kitchen support path instead of skipping straight from generic Create food beats
- Cleaned up `mechanical_workshop_logistics_and_storage` so it tracks real workshop utility instead of filler:
  - replaced vanilla barrel with `sophisticatedstorage:barrel`
  - replaced minecart/chest minecart beats with `sophisticatedbackpacks:upgrade_base` and `sophisticatedbackpacks:deposit_upgrade`
- Hardened Stone-to-Mechanical gate logic:
  - `entering_the_iron_era` now requires `8` `minecraft:iron_ingot` instead of a trivial `minecraft:stone_pickaxe`
- Hardened Mechanical-to-Diamond gate logic:
  - `diamond_threshold` now depends on real Mechanical capstones:
    - `3400000000002342`
    - `340000000000237F`
    - `3400000000002077`
    - `340000000000231F`
  - replaced placeholder `minecraft:spruce_pressure_plate` requirement with `4` `minecraft:diamond`
- Added plain one-line quest explanations across the touched Mechanical chapters and both gate quests for better beginner clarity.

### Framework Sync

- `quest_chapter_plan.json`
  - `implemented_authored_quest_count` `221` -> `223`
  - added `Cooking for Blockheads` to `mechanical_create_food_relief` source mods
  - corrected `mechanical_workshop_logistics_and_storage` source mods to match live backpack/storage ownership
  - updated `diamond_threshold` planned dependencies to reflect real live Mechanical capstones
- `quest_production_tracker.csv`
  - `mechanical_create_food_relief` `6` -> `8`, now `meaningful` and `active`
  - updated notes for `mechanical_food_and_farm_handling`, `mechanical_workshop_logistics_and_storage`, `entering_the_iron_era`, and `diamond_threshold`
- `quest_production_roadmap.md`
  - live authored total `221` -> `223`
  - Mechanical live total `62` -> `64`
- `quest_source_audit.md`
  - updated Mechanical food, kitchen, workshop, and gate notes to reflect the cleanup

### Why

- Mechanical was still carrying weak filler, hidden prerequisite drift, and a few misleading single-block mod representations.
- This pass keeps the chapter set smaller and cleaner while making the touched systems more truthful and teachable for a new player.

## 2026-03-29 - Farming Ecosystem Batch Pass 35

### Changed

- Deepened `mechanical_food_and_farm_handling` so the tree lane ends in real wood processing:
  - added `Mechanical Saw` (`3400000000002382`) after `Tree Farm Log Output`
  - `Wood Supply Online` now depends on the saw instead of jumping straight from raw logs to planks
- Deepened `mechanical_create_food_relief` so Create Integrated Farming has its real support chain:
  - added `Iron Knife` (`3400000000002228`)
  - added `Straw Stock` (`340000000000222B`)
  - added `Safety Net` (`340000000000222E`)
  - added `Canvas` (`3400000000002231`)
  - `Fishing Net` now waits on `Safety Net`
  - `Roost` now waits on `Canvas`
- Added plain one-line quest explanations for the new farming support and wood-processing beats.

### Framework Sync

- `quest_chapter_plan.json`
  - `implemented_authored_quest_count` `223` -> `228`
- `quest_production_tracker.csv`
  - `mechanical_food_and_farm_handling` `12` -> `13`
  - `mechanical_create_food_relief` `8` -> `12`
  - updated notes so the tracker reflects the honest support chain and saw payoff
- `quest_production_roadmap.md`
  - live authored total `223` -> `228`
  - Mechanical live total `64` -> `69`
- `quest_source_audit.md`
  - updated Mechanical farming and kitchen notes to reflect the new support chain

### Why

- The farming cluster was still too close to “iconic block coverage” instead of a real usable system.
- This pass keeps the chapter structure stable while making the farming/food/tree path more honest and easier for a beginner player to follow.
## 2026-03-29 - Automation Age Architecture And Gate Truthfulness Pass 36

### Changed

- Inserted a real `Automation Age` into the live questbook group structure instead of compressing first-line automation into `Industrial Age`.
  - repurposed the current live factory chapter group to display as `Automation Age`
  - added a new empty `Industrial Age` group for later true scale-up content
- Reclassified the live first-factory chapters into Automation ownership in the planning/tracker layer:
  - `industrial_nether_logistics_and_ore_escalation`
  - `industrial_oritech`
  - `industrial_factory_logistics`
  - `industrial_power_grids`
- Split `Oritech` planning into:
  - live Automation starter backbone in `industrial_oritech`
  - new planned Industrial follow-up in `industrial_oritech_escalation`
- Repaired circular tier gates without leaking next-tier raw materials early:
  - `entering_the_iron_era` now gates on stable pre-Iron survival supplies instead of iron itself
  - `diamond_threshold` now gates on stocked Mechanical readiness instead of raw diamonds
  - raw iron and raw diamond locks were restored so the age boundary stays strong
- Reworked the Stone travel capstone away from impossible pre-Iron asks:
  - removed pre-Iron `compass`, `shield`, and `water_bucket` requirements
  - replaced them with real pre-Iron scouting, first-aid, and travel-water milestones

### Framework Sync

- `quest_chapter_plan.json`
  - inserted `automation_age`
  - split former Industrial budget into `automation_age` `144` and `industrial_age` `276`
  - added `industrial_oritech_escalation`
  - corrected age display order after the new insertion
- `quest_production_tracker.csv`
  - moved live first-factory chapters into `Automation Age`
  - added scaffold row for `industrial_oritech_escalation`
  - updated gate notes so Iron and Diamond gates are described as materially obtainable
- `quest_production_roadmap.md`
  - updated the authored budget tables and live backlog by age
  - replaced the vague Automation/Industrial blur with an explicit Automation -> Industrial split
- `quest_source_audit.md`
  - split the old Industrial section into `Automation Age` and `Industrial Age`
  - updated Oritech ownership notes

### Why

- The questbook stage structure had been compressing first automation literacy and later industrial scale-up into one age, which makes Oritech, power, and logistics teach the wrong lesson at the wrong time.
- The Iron and Diamond gates were also materially impossible because the required tier materials were still locked by stage config.
- This pass fixes both problems directly: Automation is now a real age in the questbook/planning layer, and the main early tier gates are now truthful in the live pack state.

## 2026-03-29 - Pre-Publish Live Readiness Fix Pass

- Added `iron_age` stage gating to the Annexes compass signpost so the live book no longer asks for an impossible early iron utility item.
- Added `diamond_age` stage gating to the MineColonies nether-worker and mystical-site diamond reward steps so the annex cannot leak Nether access or raw diamonds before the intended age boundary.
- Removed the `twilightforest:hydra_trophy` quest from `expedition_aether_twilight_first_destinations`; it was too late for a first-destinations chapter and referenced the nonexistent `expedition_age` stage.
- Marked the empty `ascension_entry_and_scale_shift` placeholder chapter as always invisible so it does not appear as a blank late-game page in tonight's publish.
- Synced live authored totals from `295` to `294` after removing the invalid Hydra step.

## 2026-03-29 - Automation Gate Tightening Follow-Up

### Changed

- Tightened `blaze_breakthrough` so it now depends on the real Expedition capstones instead of a mid-workshop checkpoint:
  - `AE2 Starter Network`
  - `Apparatus Online`
  - `Workshop Stock`
  - pre-Automation enchanting follow-up readiness
- Kept the `blaze_rod` task as the final danger-proof token, since blaze loot is still an Expedition-earned threshold material rather than an Automation-tier identity leak.

### Why

- The stricter gate standard should apply here too: a gate should mean the age lessons are complete, not just that one material was found.
- Blaze loot still works as a final proof item, but only after the actual Expedition prep arcs are finished.

## 2026-03-29 - Industrial MI Starter Batch

### Changed

- Added the first live `industrial_modern_industrialization` chapter as a real Industrial Age spine.
- Built the chapter around the truthful MI steam path:
  - `Forge Hammer`
  - `Iron Hammer`
  - `First Bronze`
  - `Fire Clay Bricks`
  - `Bronze Machine Casing`
  - `Bronze Tank`
  - `Bronze Boiler`
  - `Bronze Compressor`
  - `Bronze Mixer`
  - `Bronze Macerator`
  - `Bronze Water Pump`
  - `MI Wrench`
  - `Fluid Pipe`
  - `Item Pipe`
  - `Steam Blast Furnace`
  - `First Steel Batch`
- Added one-line practical explanations for the machine and pipe introduction quests.
- Synced the plan, tracker, roadmap, and source audit so `Modern Industrialization` is no longer counted as absent.

### Why

- The live book still felt shallow because Industrial had planning rows but no real spine chapter.
- `Modern Industrialization` was the strongest missing Tier 1 system: it is planned as a major Industrial branch, it has a clear early steam ecosystem, and it gives Industrial its own identity instead of borrowing more work from Automation.

## 2026-03-29 - Industrial IF + HNN Support Batch

### Changed

- Added the first live `industrial_industrial_foregoing` chapter as an attached Industrial support arc.
- Built the IF chapter around the real early-use loop:
  - `Pity Machine Frame`
  - `Fluid Extractor`
  - `Latex Processing Unit`
  - `Dry Rubber Batch`
  - `Plastic Batch`
  - `Pitiful Generator`
  - `Dissolution Chamber`
  - `Simple Machine Frame`
  - `Plant Sower`
  - `Plant Gatherer`
  - `Biofuel Generator`
  - `Mob Imprisonment Tool`
  - `Factory Farm Ready`
- Added the first live `industrial_hostile_neural_networks` chapter as a bounded follow-on support arc.
- Built the HNN starter chapter around the first honest simulation payoff:
  - `Model Framework`
  - `Deep Learner`
  - `Prediction Matrix Batch`
  - `Simulation Chamber`
  - `Overworld Predictions`
  - `Nether Predictions`
  - `Simulation Stock`
- Added one-line explanations for the machine and system-introduction quests.
- Synced the plan, tracker, roadmap, and audit files so IF and HNN are no longer counted as absent.

### Why

- Industrial still felt thin because only the MI starter spine existed live.
- `Industrial Foregoing` is the next most useful support cluster after MI because it creates a real material and farm-support loop instead of a single-machine cameo.
- `Hostile Neural Networks` belongs immediately after that support layer, but only as a starter simulation arc. Full loot fabrication would have overreached past the current Industrial prerequisites.

## 2026-03-30 - Mechanical + Expedition Deepening Batch A

### Changed

- Added `mechanical_expedition_deepening_plan.md` as the source-of-truth planning artifact for the next Mechanical -> Expedition deepening wave.
- Audited the live Mechanical and Expedition chapter set against the installed jars and documented:
  - jar filenames
  - mod ids
  - first honest payoffs
  - support prerequisites
  - must-quest / should-quest / defer objects
  - chapter destinations
  - later dependencies
- Deepened `mechanical_ironwork_and_workstations` with `Iron Furnace` so faster smelting has a real workshop payoff in Mechanical instead of staying only implied by the tracker.
- Deepened `mechanical_workshop_logistics_and_storage` with the first honest Sophisticated utility chain:
  - `Packing Tape`
  - `Filter Upgrade`
  - `Pickup Upgrade`
  - `Stack Upgrade`
  - `Crafting Upgrade`
- Deepened `mechanical_food_and_farm_handling` with the missing Cooking for Blockheads support pieces:
  - `Kitchen Counter`
  - `Recipe Book`
- Added one-line practical explanations for the new workshop and kitchen utility quests.
- Updated `quest_chapter_plan.json` so the authored live total reflects this pass and the new planning file is part of the authority-doc set.

### Why

- Mechanical already had a real backbone, but it still felt narrower than the installed ecosystem because several support mods were present only as first-touch icons.
- This batch keeps the existing live quests intact and broadens the age by making the workshop easier to run, easier to organize, and easier to cook out of.
- The result is a more complete Mechanical age now, plus a cleaner planning handoff into the next Expedition deepening batch.

## 2026-03-30 - Mechanical + Expedition Deepening Batch B

### Changed

- Updated `mechanical_expedition_deepening_plan.md` Expedition coverage so Batch B now has:
  - jar / mod mapping
  - first honest payoffs
  - support prerequisites
  - must-quest / should-quest / defer lists
  - chapter placement and later-dependency notes
- Deepened `expedition_aether_twilight_first_destinations` without rewriting the live starter flow:
  - `Skyroot Chest`
  - `Ambrosium Torch`
  - `Zanite Ring`
  - `Aether Altar`
  - `Raw Clorite`
  - `Magic Map Focus`
  - `Magic Map`
- Deepened `expedition_storage_uplift` with the first real Sophisticated Storage network pieces:
  - `Storage Controller`
  - `Storage Link`
- Deepened `expedition_ae2_entry` with honest powered-network support:
  - `Energy Acceptor`
  - `ME Controller`
- Deepened `expedition_ars_nouveau` with bounded utility continuation:
  - `Worn Notebook`
  - `Source Jar`
  - `Agronomic Sourcelink`
- Deepened `expedition_enchanting_and_apotheosis_followup` with the first real Apotheosis utility payoff:
  - `Salvaging Table`
- Preserved all existing live Expedition gate ownership and capstone logic:
  - `blaze_breakthrough` unchanged
  - no stage grants changed
  - no over-tier realm boss asks added

### Why

- Expedition needed to feel like the first breadth age instead of a narrow “get blaze rods” corridor.
- This pass makes the age feel more outward-facing and more useful by adding truthful realm utility, storage-network support, bounded magical infrastructure, and a clearer pre-Automation support layer without loosening the current progression gates.
## 2026-03-31 - Nether Combat Capstone Replacement
- Re-audited Nether-facing combat content and promoted EternalNether + Luminous Nether into the live Expedition Nether phase instead of leaving them as pure defer entries.
- Extended `expedition_fortresses_and_hellish_trials` with EternalNether warped ender pearl, withered bone, and Catacomb contact so naturally available Nether combat and structures matter before the final move-on gate.
- Added `expedition_luminous_nether_climax` and originally moved the `/stage grant automation_age` reward off `blaze_breakthrough`, later superseded by the BOMD Nether Gauntlet capstone correction in the same release cycle.
- Reframed `blaze_breakthrough` as a mandatory Nether branch proof instead of the final Expedition -> Automation gate, and synced the planning/tracker layer to the new Nether conquest structure.
## 2026-03-31 - Nether Gauntlet Capstone Correction
- Re-audited BOMD and replaced Basalt Executioner as the final Expedition -> Automation gate with the Nether Gauntlet from Bosses of Mass Destruction.
- Added `expedition_bomd_nether_gauntlet` for Gauntlet arena contact, Nether Gauntlet kill, and Blazing Eye payoff.
- Kept the Luminous Nether chain live, but downgraded it from final gate ownership to a late-Nether hunt branch so the final capstone is clearer and more findable.
- Strengthened Nether signposting text so players can read the Nether as a campaign: entry and route survival, BetterNether materials, Hellish Trials, EternalNether pressure, blaze proof, Luminous hunts, then Nether Gauntlet.

## 2026-04-01 - Late-Game Redesign Structure and Nuclear Age Insertion
- Added `late_game_redesign_structure.md` as the new source-of-truth planning artifact for the post-Automation redesign.
- Completed a late-game audit covering:
  - current pacing failures from Industrial onward
  - under-positioned installed mod clusters
  - the missing bridge between factory maturity and off-world play
  - late boss and capstone ownership
- Inserted `Nuclear Age` into the planning ladder between `Industrial Age` and `Space Age`.
- Reworked the planning layer so the late-age identities are now:
  - `Industrial`: factory-campus maturity
  - `Nuclear`: hazardous power, reactors, containment, strategic force, and chemical logistics
  - `Space`: launch infrastructure, off-world logistics, advanced networks, antimatter-grade follow-through, synthesis, and draconic escalation
  - `Ascension`: prestige convergence
- Updated `quest_chapter_plan.json` to:
  - raise the authored target floor to `2444`
  - add `nuclear_age`
  - rebalance Industrial / Nuclear / Space / Ascension targets
  - replace the old `space_mekanism_core` concept with a split Nuclear + Space structure
  - make `Stellaris` the true Space opener
- Updated `age_domain_boss_architecture.md` so the global architecture now recognizes `Nuclear Age`, its domain quotas, and its boss-spine role.
- Updated `quest_source_audit.md`, `mod_coverage_matrix.md`, `quest_production_roadmap.md`, and `quest_production_tracker.csv` so the active planning layer now agrees on:
  - `Mekanism` hazardous processing in `Nuclear Age`
  - `Stellaris` as the real Space owner
  - `Applied Mekanistics` / RS chemical bridges as Nuclear logistics
  - `Ballistix` / turrets / lasers / force fields as Nuclear strategic-force ownership
  - `ProjectE`, `Dyson Cube Project`, and `Re-Avaritia` staying in `Ascension`
- This pass was planning-only. No live authored quest SNBT files were rewritten or removed.
# 2026-04-01 - Canonical Stage Rename And Nuclear Scaffold Correction

- Normalized the canonical age/stage identities to `stone_age`, `mechanical_age`, `expedition_age`, `automation_age`, `industrial_age`, `nuclear_age`, `space_age`, and `ascension`.
- Renamed the ProgressiveStages files away from legacy `iron_age`, `diamond_age`, `end_age`, and `apex_age`.
- Updated live quest stage grants and stage-gated visibility surfaces so early progression now grants `mechanical_age` and `expedition_age` instead of legacy stage names.
- Removed the stale `automation_age` reward from the old duplicated `blaze_breakthrough` file and from the Basalt Executioner follow-up so the Nether Gauntlet remains the actual Expedition -> Automation gate.
- Added the missing `automation_age_boss_hunts` scaffold to the chapter plan and tracker so every age from Mechanical onward now has an explicit boss-spine planning surface.
- Synced the planning files and added a dedicated migration note for preserved legacy quest ids and the corrected age-gate mapping.

## 2026-04-01 - Automation Gate Execution And Early Nuclear Live Authoring

- Authored the first live `automation_age_boss_hunts` chapter in the Automation group.
- Added the real `industrial_age` stage grant to `Ender Guardian` inside `automation_age_boss_hunts`.
- Rewired the first Industrial entry quests so they now also depend on the Automation capstone instead of opening directly off the Automation support lanes alone.
- Added a real `Nuclear Age` chapter group to FTB Quests.
- Authored the first live Nuclear chapters:
  - `nuclear_entry_and_containment_protocols`
  - `nuclear_mekanism_processing_and_chemicals`
  - `nuclear_reactors_isotopes_and_hazardous_power`
- Updated localization, tracker, boss-architecture notes, and stage-migration notes so Automation -> Industrial is now a live gate and early Nuclear is no longer planning-only.

## 2026-04-01 - Dragonfall Bridge, Nuclear Severance, And Strategic Nuclear Live Pass

- Authored the real live `dragonfall_and_end_access` gate as the Industrial -> Nuclear bridge.
- Made the live gate require:
  - mature Industrial branch completion
  - End access
  - Ender Dragon defeat
  - post-dragon outer-End proof through an `elytra`
  - `cataclysm:find_ancient_factory`
  - `cataclysm:kill_harbinger`
- Added the real `/stage grant {p} nuclear_age` reward to `The Harbinger` inside `dragonfall_and_end_access`.
- Re-keyed the live Nuclear starter chapters from `industrial_age` to `nuclear_age` so they now sit behind the real gate instead of opening as a soft post-Industrial preview.
- Authored the missing live Nuclear branches:
  - `nuclear_defense_systems_and_strategic_force`
  - `nuclear_chemical_storage_and_digital_bridges`
  - `nuclear_boss_hunts`
- Braided the Nuclear identity across:
  - Mekanism hazardous chemistry and storage
  - Nuclear Science containment and reactor support
  - Ballistix launch hardware and targeting
  - Electrodynamics / Dynamic Electricity hardened facility support
  - Mekanism Turrets / Mekanism Lasers / Modular Force Fields defense systems
  - Applied Mekanistics and RS chemical storage bridges
- Added the first live Nuclear boss spine using:
  - `alexscaves:alexscaves/defeat_nucleeper`
  - `alexscaves:alexscaves/defeat_magnetron`
  - `cataclysm:kill_monstrosity`
- Added `severance_array_outline.md` as the first basic Ascension planning scaffold for the future off-world Severance Array prestige structure.
- Synced the tracker, chapter plan, stage-migration note, source audit, roadmap, mod coverage, and boss architecture files to the new live state.
## 2026-04-01 - Nuclear Hardened Grids Pass

- Authored the live [`nuclear_strategic_power_and_hardened_grids`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/nuclear_strategic_power_and_hardened_grids.snbt) chapter as the missing Nuclear infrastructure spine.
- The new chapter now covers ceramic insulation, advanced transformer control, monitored substations, reserve battery yards, backup generation, power conversion, reactor-service gas utilities, laser-power backing, and campus relay hardware.
- Tightened live Nuclear sequencing so [`nuclear_defense_systems_and_strategic_force`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/nuclear_defense_systems_and_strategic_force.snbt) and [`nuclear_boss_hunts`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/nuclear_boss_hunts.snbt) now sit downstream of the hardened-grid proof instead of floating beside it.
- Kept [`space_launch_threshold`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/quest_chapter_plan.json) planning-only, but updated the planning layer so the future launch-authority gate explicitly consumes hardened grids without hard-binding Space to one off-world owner in this pass.
- Added a tiny [`severance_array_outline.md`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/severance_array_outline.md) refinement so future Ascension severance control clearly descends from Nuclear hardened-grid and strategic-force mastery.

## 2026-04-01 - Industrial Boss Hunts Live Pass

- Authored the live [`industrial_boss_hunts`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/industrial_boss_hunts.snbt) chapter as the missing Industrial branch-boss package.
- Selected a coherent Industrial threat ladder: Burning Arena -> Netherite Monstrosity, Forlorn Hollows -> Forsaken, and one Ice and Fire dragon-scale hunt.
- Wired [`dragonfall_and_end_access`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/dragonfall_and_end_access.snbt) to consume the new Industrial conquest proof before End access and The Harbinger.
- Synced the tracker, roadmap, source audit, coverage matrix, and boss-architecture docs so Industrial combat pressure is now live and no longer scaffold-only.

## 2026-04-01 - Industrial PneumaticCraft Live Pass

- Authored the live [`industrial_pneumaticcraft`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/industrial_pneumaticcraft.snbt) chapter as the missing Industrial pressure-specialization branch.
- Used the real recipe path from the installed mod versions instead of the misleading manual-compressor intuition: explosion-crafted compressed iron first, then pressure tubes, reinforced stone, the air compressor, safe pressure modules, refinery-fed LPG, the thermopneumatic plant, plastic, a real pressure chamber, and one bounded Applied Pneumatics payoff.
- Kept PneumaticCraft tied to the shared petroleum backbone by making the branch consume refinery inputs and LPG from the live TFMG/Create oil line instead of opening a second oil identity.
- Wired [`industrial_boss_hunts`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/industrial_boss_hunts.snbt) to sit downstream of the new pressure-engineering proof so Industrial strike readiness now reflects one more real factory specialization before Dragonfall.
- Synced the tracker, roadmap, source audit, coverage matrix, and chapter plan so PneumaticCraft is now live and counted as part of Industrial campus maturity.

## 2026-04-01 - Industrial Integrated Dynamics Live Pass

- Authored the live [`industrial_integrated_dynamics`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/industrial_integrated_dynamics.snbt) chapter as the missing Industrial control-and-policy specialization.
- Used the real recipe chain from the installed Integrated stack instead of reducing the branch to random variables: Menril collection, resin handling, crystalized Menril, logic programmer + variables, cable bus, battery + transformers, machine/inventory control, tunnels, mechanical drying, bounded crafting policy, and a portable terminal payoff.
- Kept the branch complementary to Expedition AE2 and Industrial physical logistics by treating Integrated Dynamics as the programmable control layer for a mature factory campus rather than as a replacement storage network.
- Wired [`industrial_boss_hunts`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/industrial_boss_hunts.snbt) to sit downstream of the new `Factory Intelligence Ready` proof, so Industrial strike readiness now reflects programmable control as well as power, fuel, pressure, and synthetic materials.
- Synced the tracker, roadmap, source audit, coverage matrix, and chapter plan so Integrated Dynamics is now live and counted as part of Industrial campus maturity.

## 2026-04-01 - Industrial Presentation Coherence Pass

- Tightened the player-facing opener and capstone subtitles across the live Industrial group so each branch now states its role more clearly:
  - Modern Industrialization as the process backbone
  - Create as the physical plant
  - petroleum as the extraction/fuel backbone
  - Industrial Foregoing as applied automation
  - Hostile Neural Networks as synthetic-resource discipline
  - PneumaticCraft as pressure specialization
  - Integrated Dynamics as control-and-policy intelligence
  - boss hunts as conquest pressure
  - Dragonfall as the final Industrial threshold
- Kept the live Industrial order and dependency structure intact because the current chapter flow already reads coherently left-to-right without needing a structural rebalance.
- Preserved all gate logic, stage grants, and protected quest content while making the Industrial age feel more like one authored campus-growth arc in the quest UI.

## 2026-04-01 - Mechanical Deepening Protected Pass

- Added the missing live Mechanical chapters:
  - [`mechanical_early_utility_machines`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/mechanical_early_utility_machines.snbt)
  - [`mechanical_dungeon_readiness`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/mechanical_dungeon_readiness.snbt)
  - [`mechanical_age_boss_hunts`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/mechanical_age_boss_hunts.snbt)
- Deepened existing live Mechanical chapters additively without overwriting protected hand-authored content:
  - [`mechanical_ironwork_and_workstations`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/mechanical_ironwork_and_workstations.snbt): added hand-crank/wrench setup, first fluid routing (pipe/tank/pump), and item-vault support
  - [`mechanical_food_and_farm_handling`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/mechanical_food_and_farm_handling.snbt): added Aquaculture + Ocean's Delight route-support food beats
  - [`mechanical_workshop_logistics_and_storage`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/ftbquests/quests/chapters/mechanical_workshop_logistics_and_storage.snbt): added restock/magnet and storage I/O routing support
- Kept `diamond_threshold` gate logic and protected quest surfaces intact; no stage-id regressions or legacy stage names were introduced.
- Synced planning and tracking surfaces so Mechanical utility/readiness/boss coverage is now represented as live instead of scaffold-only.
