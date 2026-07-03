# New Mod And Late-Age Quest Audit Master Roadmap

Date: 2026-06-28
Mode: read-only audit and planning. No quest, KubeJS, config, staging, commit, or push changes were made.

## Evidence Base

This pass combined:

- Live installed jars under `mods/`.
- Live FTBQ chapters under `config/ftbquests/quests/chapters/`.
- Live KubeJS AStages, recipe weave, tag, data map, and Modonomicon files.
- Current tracker/planning docs under `progression/` and `docs/Evidence/Current/`.
- Parallel background threads for ocean, late tech, creature/QoL, and Neo Vitae.
- Parallel subagents for ocean jar audit, ambient jar audit, late quest coverage, late jar registry audit, and Neo Vitae verification.
- Current web/source checks where local jar evidence did not explain mechanics.

Important source links used:

- Create Aquatic Ambitions: https://www.curseforge.com/minecraft/mc-mods/create-aquatic-ambitions
- Hybrid Aquatic: https://modrinth.com/project/HH4FjUqN
- FTB Ocean Mobs: https://www.curseforge.com/minecraft/mc-mods/ftb-ocean-mobs
- Arcane Lanterns: https://www.curseforge.com/minecraft/mc-mods/arcane-lanterns
- Critters and Companions: https://modrinth.com/mod/critters-and-companions
- Creatures and Beasts Continued: https://www.curseforge.com/minecraft/mc-mods/creatures-and-beasts-continued
- Mekanism Fission Reactor: https://wiki.aidancbrady.com/wiki/Fission_Reactor
- Mekanism Fusion Reactor: https://wiki.aidancbrady.com/wiki/Fusion_Reactor
- Mekanism SPS: https://wiki.aidancbrady.com/wiki/Supercritical_Phase_Shifter
- Nuclear Science wiki: https://wiki.aurilis.dev/nuclear-science/
- Oritech docs: https://moddedmc.wiki/hu/project/oritech/latest/docs
- Chemical Science: https://www.curseforge.com/minecraft/mc-mods/chemicalscience
- Electrodynamics: https://www.curseforge.com/minecraft/mc-mods/electrodynamics

## Bottom Line

The new ocean and ambient mods are almost completely unquested by namespace. Neo Vitae is the opposite: the older planning docs are stale because the live checkout already has Neo Vitae locks, quests, tags, data maps, and cross-weaves. Late Gilded and Atomic have meaningful live coverage, but Otherworldly and Ascension remain skeletal compared with the amount of gated late-game surface.

## Recommended Authoring Order

1. Fix Neo Vitae risk before expanding it.
   - Highest risk: `ren_magic_foundations` appears to require `neovitae:athanor`, while its jar recipe requires `neovitae:tabula_animata` and tier-2 orb access that live AStages place later. Reverify in-game/JEI before adding more Neo quests.
   - Smoke Ara Vitae tier validation with the KubeJS pillar tags and `hellfire_forge_upgrade` behavior.

2. Decide FTB Ocean Mobs before any ocean quest writing.
   - Current recommendation: disable/remove or defer it.
   - If kept, design it as a deliberate late rift/boss lane, not ambient ecology.

3. Add compact QoL side quests.
   - Arcane Lanterns is a good functional base-utility mini-chain.
   - Critters and Companions and CNB should get only mechanic-bearing fauna quests.

4. Build the ocean ecosystem.
   - Create Aquatic Ambitions should bridge Create automation to prismarine/coral/conduit automation.
   - Hybrid Aquatic should introduce ocean ecology, diving, fishing tools, clams/pearls, crab pots, Karkinos, and deep-ocean hazards without asking for every fish.

5. Repair late-age residues and then expand.
   - Fix live `ftbquests:missing_item` residues in Gilded/Atomic.
   - Add Otherworldly and Ascension spines after jar-verifying each target.

## Placement Summary

| Mod or family | Best placement | Why |
|---|---|---|
| Neo Vitae | Required Renaissance to Gilded, optional Atomic/Otherworldly | Live files already implement this shape, but the Atanor gate needs verification. |
| Arcane Lanterns | Medieval farming side or Renaissance utility | Functional light/control effects are useful but not central progression. |
| Create Aquatic Ambitions | Late Renaissance or Gilded ocean automation | Craftable trident/Heart of the Sea and conduit automation are too strong for early play. |
| Hybrid Aquatic | Medieval/Renaissance ecology, Gilded deep-ocean optional | Broad ecology starts early; black pearl, Karkinos, vents, and deep gear belong later. |
| FTB Ocean Mobs | Disabled/deferred, or late rift boss | No recipes, no built-in biome modifiers found, minimal config. |
| Critters and Companions | Medieval/Renaissance utility side | Grappling hook, silk, pearls, sea bunny slime, and dragonfly gear are useful. |
| CNB | Renaissance Nether/desert/cold side lanes | Cindershell, Cactem, Sporeling, and Yeti drops are the useful subset. |
| Chemical Science | Gilded refinery to Atomic radiochemistry | Live coverage exists; deep elements/cards should only be quested when they gate systems. |
| Nuclear Science | Atomic core, Otherworldly exotic continuation | Reactor spine is covered; antimatter/dark matter cells are the later gap. |
| Electrodynamics/Voltaic/Dynamic Electricity | Industrial/Gilded grid into Atomic support | Many locked support items are unquested; avoid wire/color variants. |
| Oritech/Oritech Things | Gilded/Atomic mastery, Ascension convergence | Live Oritech is strong; reactor/logistics/early cores are the main omissions. |
| Mekanism and addons | Atomic to Otherworldly/Ascension | SPS, antimatter, quantum/multiversal factories, QIO, and chemical storage need clearer routes. |

## Global Do-Not-Quest Rules

- Do not quest every fish, mob, colored cable, wood variant, coral variant, decor block, plushie, vase, window, sand, or ordinary material block.
- Do not quest every Mekanism factory/tank/cable tier. Quest tier breaks and systems.
- Do not quest every Oritech addon tier. Quest representative addon roles.
- Do not quest every Chemical Science element or chromatography card. Quest cards/elements only when they unlock a real recipe gate.
- Do not quest spawn eggs unless the pack deliberately gives them.

## Live Risk Register

| Risk | Evidence | Recommendation |
|---|---|---|
| Neo Vitae Atanor hardlock | `athanor` capstone in Renaissance, but jar recipe appears to require later-gated `tabula_animata` and tier-2 orb access. | Verify JEI/runtime. Patch gate or capstone before expanding Neo. |
| FTB Ocean Mobs inert or surprise-hostile | No recipes, no biome modifiers in jar, config only has Rift Weaver arena size. | Remove/defer unless a boss lane is designed. |
| Hybrid Aquatic spawn density | 109 entities and 220 biome modifiers. | Runtime/performance check before hard-gating quests. |
| Late missing-item residues | `g2`, `at4`, `at7` still have `ftbquests:missing_item`. | Repair before adding late quest content. |
| Otherworldly/Ascension thinness | OW chapters are 4 to 13 quests; Ascension chapters are 2 to 11 quests by top-level ID count. | Add full spines after target verification. |
| Tracker drift | Tracker still marks some rows 0 while live skeleton chapters exist. | Update tracker after authoring decisions. |

## Document Index

- `01_NEOVITAE_VERIFICATION.md`
- `02_ARCANE_LANTERNS.md`
- `03_CREATE_AQUATIC_AMBITIONS.md`
- `04_HYBRID_AQUATIC.md`
- `05_FTB_OCEAN_MOBS.md`
- `06_CRITTERS_AND_COMPANIONS.md`
- `07_CREATURES_AND_BEASTS_CNB.md`
- `08_LATE_TECH_CORE.md`
- `09_ORITECH_MEKANISM_ADDONS.md`
- `10_OTHERWORLDLY_ASCENSION_GAP_MAP.md`

