# Age-Domain Boss Architecture

## Purpose

This file defines the source-of-truth progression architecture for:

- age-based boss spines
- cluster-based progression placement
- chapter unlock surfaces
- minimum age-domain quotas
- future implementation order
- late-game age boundaries from `Industrial` onward

Use this file when deciding where a chapter belongs, what unlocks it, and whether a mod cluster is truly integrated.

For late-game chapter ownership and the `Nuclear Age` insertion, pair this file with `late_game_redesign_structure.md`.

## Core Boss-Spine Rule

Every major age group from `Mechanical` onward must have one dedicated boss chapter.

Stone Age is the explicit exception.

Stone should use:

- survival-readiness validation
- exploration or structure proof
- dangerous encounter proof
- pre-boss combat preparation

Stone should not require a true boss kill to leave the age, and it should not have an age main boss that gates Mechanical.

That boss chapter follows one loop:

1. boss step unlocks sequentially
2. boss kill unlocks branch chapters elsewhere
3. required branch chapters must be completed
4. the next boss step unlocks
5. the age main boss unlocks last
6. the age main boss defeat opens the next progression threshold and its chapter-group visibility

This means:

- bosses are not isolated trophies
- branches are not loose side content
- age completion is not just chronological chapter cleanup
- Stone remains a survival-stabilization age rather than a true boss-gated age

## Boss Classification Model

| class | meaning | unlock behavior | requirement level |
| --- | --- | --- | --- |
| mandatory spine boss | required boss in the age boss chapter that advances the main sequence | unlocks mandatory branch packages and the next boss node | always required |
| mandatory branch boss | required boss inside a branch family that must be cleared before the age main boss opens | unlocks branch-completion credit, later branch packages, or the age main boss | required when assigned to the age architecture |
| optional prestige boss | boss with strong rewards, trophies, or side progression but no mainline lock ownership | unlocks prestige/loot/mastery content only | optional |

## Chapter Unlock Surface Model

Use these unlock surfaces deliberately. Do not leave major chapters on loose chronological visibility alone.

| unlock surface | use | what it should open |
| --- | --- | --- |
| boss kill | primary age progression driver | next boss node, mandatory branch chapters, next-age prep chapters |
| branch completion | proves the player actually used a system | next boss node, gate surface, capstone branch |
| dimension access | opens prep and survival chapters for that realm | entry/setup/support chapters, not full deep branch completion by itself |
| tech readiness | opens infrastructure-heavy chapters | machine/process/logistics branches |
| magic readiness | opens ritual, enchanting, and arcane branches | magic branches or mixed magic-tech bridges |
| structure or exploration proof | opens route, treasure, and expedition support | treasure, mapping, route-planning, boss prep |
| main boss defeat | age completion surface | next age group, next gate surface, next-wave branch families |

## Age Quota Model

Each age must force a broad experience. These are minimum domain quotas, not optional aspirations.

| age | tech / infrastructure | magic / ritual | dimension / exploration | boss progression | logistics / readiness | survival / pressure |
| --- | --- | --- | --- | --- | --- | --- |
| Stone | `2` core survival-tech chapters | `0-1` teaser branch | `1` travel/structure route branch | `0` mandatory boss spine, `0-1` optional prep/validator chapter | `1` route/readiness branch | `2` core chapters required |
| Mechanical | `3` workshop/process chapters | `1` light magic or relic-combat branch | `1` structured exploration branch | `1` sequential boss chapter | `1-2` storage/logistics branches | `1` readiness/supply branch |
| Expedition | `2` tech-prep chapters | `2` mandatory magic branches | `2` dimension/exploration branches | `1` sequential boss chapter | `1` storage/logistics branch | `1` pressure/readiness branch |
| Automation | `2` major spines plus `1-2` support branches | `1` support or gated teaser branch | `1` combat/exploration pressure branch | `1` sequential boss chapter | `2` logistics/power branches | `0-1` environment pressure beat |
| Industrial | `3` major factory spines plus `3-4` support branches | `0-1` bounded ritual or relic branch | `1-2` conquest / structure branches | `1` sequential boss chapter | `2-3` logistics/process branches | `1` hostile-pressure branch |
| Nuclear | `3` hazardous-tech spines plus `2-3` support branches | `0-1` bounded ritual or anomaly branch | `1` hostile-world / structure branch | `1` sequential boss chapter | `2` containment / hazardous-logistics branches | `1-2` hazard-pressure branches |
| Space | `2-3` off-world tech spines plus `2-3` support branches | `1` cosmic or draconic branch | `2` off-world or cosmic branches | `1` sequential boss chapter | `2` network/logistics branches | `1` hostile-environment branch |
| Ascension | `2-3` prestige tech/crafting arcs | `1` prestige ritual branch | `1` final-dimension/prestige branch | `1` final boss chapter | `1` final-network/logistics branch | optional only |

## Cluster Family Map

Use clusters, not isolated mods, when deciding placement.

| cluster family | primary domain | secondary domain | earliest truthful age | main age | late extension age | first honest payoff | mid payoff | capstone payoff | boss / dimension ties | later unlocks | required role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Survival Pressure Cluster (`Legendary Survival Overhaul`, `Serene Seasons`) | atmosphere / survival pressure / horror | resource economy | Stone | Stone | Mechanical | safe water, shelter heat, injuries, seasonal awareness | stable food and route discipline | survival no longer dominates every decision | Overworld ruins and early travel | Iron readiness, first exploration branching | mandatory spine content |
| Workshop Backbone (`Create`, `Immersive Engineering`, workshop storage cluster) | tech / process infrastructure | logistics / storage | Mechanical | Mechanical | Expedition | first labor relief and truthful workstation upgrades | chained processing, logistics, treated wood, wiring | mature workshop ready for Expedition/Automation | Mechanical boss spine and dimension prep | Expedition prep, Automation on-ramp | mandatory spine content |
| Arcane Utility Cluster (`Ars Nouveau`, `Apotheosis`, `Apothic Enchanting`, `Gaze`, `Iron's Spellbooks`) | magic / ritual / arcane | boss / combat gate | Expedition | Expedition | Industrial | practical enchanting, first spell tooling, route-safe utility | deeper ritual power, affixes, spell combat | combat and infrastructure magic that feeds late progression | Expedition boss spine, dimension prep | Automation/Industrial branch unlocks | mandatory branch content |
| Soul Ritual Cluster (`Malum`, `Gaze`) | magic / ritual / arcane | atmosphere / survival pressure / horror | Expedition | Industrial | Space | first soul or ritual crafting payoff | ritual-powered combat or utility lines | ritual capstones that support late prestige or dark content | dark branches and branch bosses | Industrial magic branch, Space ritual branch | mandatory branch content |
| Celestial Magic Cluster (`Eternal Starlight`, `Pastel`) | magic / ritual / arcane | dimension / exploration | Industrial | Space | Ascension | first celestial materials or entry rituals | dimension-specific crafting and progression | cosmic-grade ritual or tool payoff | Space boss spine and cosmic dimensions | Ascension branch unlocks | mandatory branch content |
| Adventure Realms Cluster (`Aether`, `Deep Aether`, `Twilight Forest`) | dimension / exploration | boss / combat gate | Mechanical | Expedition | Industrial | first alternate realm travel and structure loot | sequential realm boss kills and resources | deep-realm branch completion and later payoff | Mechanical and Expedition boss spines; Stone may only use prep or non-mandatory encounter proofs | Expedition magic/storage/treasure branches | mandatory branch content |
| Dark Frontiers Cluster (`The Undergarden`, `Deeper and Darker`, `Macabre`, `The Afterdark`) | dimension / exploration | atmosphere / survival pressure / horror | Expedition | Industrial | Space | first dark-dimension survival and route payoff | hostile materials, deeper boss branches, horror escalation | full dark-frontier completion and later synthesis or ritual hooks | Expedition and Industrial boss spines | Automation/Industrial unlock surfaces, horror branches | mandatory branch content |
| RPG Escalation Cluster (`DivineRPG`, `Journey Into The Light`) | dimension / exploration | boss / combat gate | Expedition | later Expedition / Industrial | Space / Ascension | first guidebook contact, overworld material contact, and compact Expedition-safe gear payoff | controlled portal setup, chained dimension progression, realm gating, and gear advancement | high-tier multi-realm boss chain | later Expedition / Industrial and Space boss spines | late prestige and dimension unlocks | mandatory branch content |
| Industrial Factory Cluster (`Oritech`, `Modern Industrialization`, `Create Industrial`, `TFMG`, `Industrial Foregoing`, `PneumaticCraft`, `Integrated Dynamics`, `Hostile Neural Networks`) | tech / process infrastructure | logistics / storage / automation support | Automation | Industrial | Nuclear | first powered automation and first industrial process lines | shared petroleum, plastic, synthetic resources, advanced routing, and serious machine campuses | full industrial campus and the bridge into hazardous escalation | Automation and Industrial boss spines | Nuclear containment, synthesis, and launch-prep lines | mandatory spine plus mandatory branch content |
| Hazardous Power and Strategic Tech Cluster (`Mekanism`, `Mekanism Generators`, `Ballistix`, `Nuclear Science`, `Dynamic Electricity`, `Electrodynamics`, `Extreme Reactors`, `Generator Galore`, `Applied Mekanistics`, `Mekanism Turrets`, `Mekanism Lasers`, `Modular Force Fields`) | tech / process infrastructure | boss / combat gate | Industrial | Nuclear | Space | first hazardous-processing and containment payoff | reactors, isotopes, hardened grids, strategic force, and chemical logistics | launch-authority and pre-space facility mastery | Nuclear and Space boss spines | Space launch, antimatter, and cosmic-network lines | mandatory spine plus mandatory branch content |
| Cataclysmic Threat Cluster (`L_Ender's Cataclysm`, `Alex's Caves`, `Ice and Fire`, `Bosses of Mass Destruction`, `fdbosses`) | boss / combat gate | dimension / exploration | Industrial | Industrial / Nuclear | Space | first truly punishing boss-gated route or resource payoff | chained branch bosses feeding dragonfall, launch authority, and late unlocks | late hostile-world mastery and post-launch scale | Industrial, Nuclear, and Space boss spines | Space progression and prestige boss surfaces | mandatory spine and mandatory branch content |
| Cosmic Infrastructure Cluster (`Stellaris`, advanced `AE2` family, `Ender IO`, `Solar Flux Reborn`, late `Mekanism`) | tech / process infrastructure | logistics / storage / automation support | Nuclear | Space | Ascension | first launch, oxygen, and off-world routing payoff | advanced storage, remote logistics, antimatter-grade processing, and remote power | true off-world infrastructure and cosmic-scale industry | Space boss spine | Ascension thresholds and prestige crafting | mandatory spine plus support content |
| Prestige Cluster (`ProjectE`, `Dyson Cube Project`, `Re-Avaritia`, `Extended Crafting`, `Modular Machinery Reborn`, final boss mods) | boss / combat gate | tech / process infrastructure | Space | Ascension | Ascension | first prestige-crafting shift | exchange, mega-crafting, and capstone assembly | final completion loop | Ascension boss spine | pack completion and postgame mastery | mandatory spine and optional prestige content |

## Boss-Spine Model By Age

This is the target chapter behavior. Existing chapter ids can remain, but their logic should evolve toward this structure.

| age | boss chapter | sequential spine steps | branch packages unlocked between steps | main boss unlock rule | main boss result | current structural problem |
| --- | --- | --- | --- | --- | --- | --- |
| Stone | `stone_age_boss_hunts` only if kept as an optional prep chapter | non-mandatory dangerous encounter proofs, structure-entry discipline, and pre-boss combat preparation | can unlock optional travel, treasure, or early realm-prep side packages | no mandatory age main boss; `entering_the_iron_era` remains a non-boss readiness gate | unlock Mechanical through survival, travel, supply, and security readiness instead of boss defeat | current Stone structure should stay focused on survival stabilization; any boss chapter here must remain optional or preparatory |
| Mechanical | `mechanical_age_boss_hunts` | `Step 1`: first structured realm boss. `Step 2`: second realm or dungeon boss. `Main Boss`: age-capstone boss proving workshop maturity and combat readiness. | unlock `mechanical_dungeon_readiness`, deepen storage/logistics, and open Expedition prep branches | required Mechanical workshop, logistics, and dungeon-readiness branches complete | unlock Expedition Age group and `diamonds_and_branch_unlocks` | current boss chapter is scaffolded and Diamond/Expedition progression is still more gate-driven than boss-driven |
| Expedition | `expedition_boss_hunts` | `Step 1`: first Expedition branch boss from Aether/Twilight cluster. `Step 2`: dark-frontier boss from Undergarden/Deeper and Darker/horror cluster. `Main Boss`: Expedition gate boss that sits above branch completion. | unlock `expedition_ars_nouveau`, enchanting/apotheosis, storage uplift, AE2 starter, workshop prep, and dark-frontier branches in staged packages | required Expedition magic, storage, workshop, and frontier branches complete | unlock Automation Age group and `industrial_nether_logistics_and_ore_escalation` | current Expedition gate is still centered on `blaze_breakthrough`, which is a truthful readiness surface but not yet a real boss-spine main boss |
| Automation | `automation_age_boss_hunts` | `Step 1`: first machine-age combat validator. `Step 2`: second industrial-pressure validator tied to the first real factory campus. `Main Boss`: Automation capstone boss. | unlock `industrial_oritech`, `industrial_factory_logistics`, `industrial_power_grids`, and later Industrial prep branches in sequence | required Automation spines and support branches complete | unlock Industrial Age group and `industrial_modern_industrialization` | live short spine now exists through Obsidilith, Ancient Factory routing, Ender Golem, and Ender Guardian |
| Industrial | `industrial_boss_hunts` plus `dragonfall_and_end_access` as the age main-boss gate surface | `Step 1`: Cataclysmic siege pressure through the Burning Arena and Netherite Monstrosity. `Step 2`: deep-anomaly and dragon-scale pressure through the Forsaken and an Ice and Fire dragon kill. `Main Boss`: Dragonfall / End-access boss. | unlock Create industrial support, petroleum/extraction, IF, PneumaticCraft, Integrated Dynamics, HNN, and late Oritech escalation in waves | required Industrial scale-up and threat-response branches complete | unlock Nuclear Age group and `nuclear_entry_and_containment_protocols` | live branch-boss package now exists: mature Industrial branches lead into Cataclysm, Alex's Caves, and Ice and Fire conquest proofs before End access, dragon kill, outer-End proof, Ancient Factory routing, and The Harbinger finish the age |
| Nuclear | `nuclear_boss_hunts` plus `space_launch_threshold` as the age main-boss gate surface | `Step 1`: first hazardous-world or war-machine validator. `Step 2`: second high-threat branch boss tied to strategic force or toxic-world pressure. `Main Boss`: launch-authority boss that proves the player can survive the world while operating dangerous systems. | unlock hazardous Mekanism processing, reactor/isotope infrastructure, hardened grids, defense systems, and chemical logistics in staged packages | required Nuclear hazard, power, defense, and logistics branches complete | unlock Space Age group and the future off-world owner mainline | the age is now live as a real bridge: containment, hazardous chemistry, reactors, hardened grids, strategic force, digital chemical routing, and the first Nuclear boss spine all exist before the future Space gate |
| Space | `space_boss_hunts` plus `ascension_threshold` as the age main-boss gate surface | `Step 1`: off-world or cosmic validator. `Step 2`: draconic or synthesis-linked boss. `Main Boss`: Space capstone boss. | unlock off-world launch lines, advanced storage, Ender IO, antimatter refinement, late agriculture/synthesis, and Draconic branches | required Space launch, network, synthesis, and dimension branches complete | unlock Ascension group and `ascension_entry_and_scale_shift` | Space should now own off-world mastery instead of every advanced terrestrial tech system |
| Ascension | `ascension_boss_hunts` | `Step 1`: prestige validator. `Step 2`: branch-capstone prestige validator. `Main Boss`: final completion boss. | unlock prestige crafting, ProjectE, Dyson Cube, and Avaritia capstones in sequence | required prestige branches complete | unlock final completion state and optional postgame prestige bosses | current Ascension structure has arcs but still needs its full boss-gated final spine |

## Chapter Unlock Governance

Use these rules when implementing or revising chapters:

- boss chapters own sequential major-age combat progression from `Mechanical` onward
- gate chapters validate readiness but should not replace the age boss spine
- Stone gate chapters should stay non-boss and readiness-based
- dimension access opens prep chapters, not full branch completion by itself
- mandatory branch chapters must have a later dependency or they are not truly integrated
- optional prestige chapters should never own mainline age progression
- chapter visibility should follow real unlock surfaces, not just age chronology

## Existing Structural Weak Points

- boss chapters are mostly treated as validator buckets instead of sequential spines
- Stone still needs to stay outside mandatory boss-gated age completion
- branch chapters are still often unlocked by broad chronology or thresholds instead of boss kills and branch completion
- `Automation Age` now has a live dedicated boss chapter, but the earlier ages still need the same boss-spine treatment
- `industrial_boss_hunts` is now live, but the late-game staircase still needs the future Space bridge after Nuclear completion
- the later `Space` launch gate is still scaffolded even though the Nuclear bridge itself is now live
- dark, horror, and RPG clusters are present in the pack but not yet mapped into one coherent age-domain sequence
- magic clusters beyond Expedition are still under-positioned, especially `Malum`, `Gaze`, `Eternal Starlight`, and `Pastel`
- `DivineRPG` + `Journey Into The Light` now have a bounded Expedition first-contact layer, but their portal and boss ladders still need later boss-surface ownership
- `Space Age` still needs to stop acting like a generic holder for all advanced tech; the eventual off-world owner and off-world logistics should become its identity

## Recommended Future Implementation Order

1. Convert the planned boss chapters in `quest_chapter_plan.json` into explicit boss-spine packages with step-by-step branch unlock ownership from `Mechanical` onward.
2. Keep `Stone Age` exit logic centered on survival, travel, and readiness gates; if `stone_age_boss_hunts` is implemented, keep it optional or preparatory instead of using it as the age-transition mechanism.
3. Rebuild `mechanical_age_boss_hunts` and `expedition_boss_hunts` around sequential mandatory spine bosses before widening more optional side branches.
4. Build on the live `automation_age_boss_hunts` spine so Industrial and later boss chapters inherit the same sequential validator logic.
5. Build on the live `Nuclear Age` bridge from containment into hazardous power, strategic force, chemical routing, and launch-authority ownership.
6. Build `space_launch_threshold` as the next boss-gated bridge from hazardous terrestrial mastery into true off-world progression.
7. Place the dark-frontier cluster (`Undergarden`, `Deeper and Darker`, `Macabre`, `The Afterdark`) into Expedition -> Industrial branch packages with explicit boss-step unlocks.
8. Place the celestial and ritual clusters (`Eternal Starlight`, `Pastel`, `Malum`, `Gaze`) into Industrial -> Space planning with real gate/payoff/dependency ownership.
9. Expand the combined `DivineRPG` + `Journey Into The Light` RPG escalation family from its new Expedition first-contact layer into a later boss-surfaced branch family with Industrial/Space ownership.
10. After the architecture surfaces are in place, author quests in boss-step batches instead of mod-by-mod batches.
