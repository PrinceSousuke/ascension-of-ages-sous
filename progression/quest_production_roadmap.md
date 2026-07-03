# Quest Production Roadmap

## Current 2026-05-13 Alignment

This document is active planning/reference material, but it is subordinate to the current Required Chapter Matrix, revised Mod Career Ledger, revised quest-density budget, live `mods/*.jar`, and the AStages/KubeJS restriction surface. Preserve useful architecture from this file, but rewrite stale specifics against:

- `audit_artifacts/AOA_REQUIRED_CHAPTER_MATRIX_2026-05-13.md`
- `audit_artifacts/AOA_MOD_CAREER_LEDGER_REVISED_2026-05-13.tsv`
- `audit_artifacts/AOA_REVISED_QUEST_DENSITY_BUDGET_2026-05-13.md`
- `kubejs/server_scripts/aoa_astages_00_register_stages.js`
- `kubejs/server_scripts/aoa_astages_*.js`



## Purpose

This file turns the current quest cleanup work into a scalable production framework.

It answers three questions:

1. how the authored quest target stays in the `3,225-3,975` range without filler
2. which ages and chapter classes carry that total
3. what the next implementation batches should actually be built around

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
- do not solve local chapter ambitions by inflating Dark Age/Medieval or drifting outside `3,225-3,975`

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

These are the current back-loaded quest-density targets from `audit_artifacts/AOA_REVISED_QUEST_DENSITY_BUDGET_2026-05-13.md`:

| age | total quest target | rough required target | role |
| --- | --- | --- | --- |
| Dark Age | `50-75` | `35-55` | survival prologue: pressure, shelter, food/water/sleep, primitive storage, first guide framing |
| Medieval | `125-175` | `95-130` | workshop/settlement prologue: handwork, early building, physical logistics, basic exploration |
| Renaissance | `400-475` | `300-355` | first true AoA curriculum age: magic literacy, realm literacy, archive/recordkeeping, F&A foundation |
| Industrial Revolution | `500-600` | `375-450` | first major systems-weaving age: IE, Oritech, PneumaticCraft, MI entry, storage/network discipline |
| Gilded Age | `500-600` | `375-450` | scaling and authorization: NauTec, Astral/Void Titan proof, advanced applied industry, computation/storage scale |
| Atomic | `700-850` | `525-640` | consequence and containment: nuclear, chemical, Macabre, MFF, Ballistix, hazardous systems |
| Otherworldly | `450-550` | `335-410` | operations beyond the world: launch, interdimensional infrastructure, high Oritech, cosmic systems |
| Ascension | `500-650` | `375-490` | final synthesis thesis: Draconic, Extended Crafting, Re:Avaritia, Archive of Ages convergence |
| Total | `3,225-3,975` | roughly `75%` required | optional depth remains inside chapters, as prestige/trophies/side bosses/cosmetics/challenges |

Dark Age and Medieval should not be inflated with catalog work. The real quest mass belongs from Renaissance onward, where the Mod Career Ledger shows the major cross-age systems coming online.

## Current Production Snapshot

The older live-count snapshot in this document is not current production authority. Re-count live SNBT before using any numeric backlog from this file.

Current planning stance:

- Dark Age and Medieval are intentionally lean onboarding eras.
- Do not resurrect old Expedition/RPG branches around removed mods.
- Oil/petroleum work should use the corrected CDG + Immersive Petroleum + Modern Industrialization stack unless live verification changes it.
- NauTec belongs in Gilded oceanic industry; Draconic belongs in Ascension/final convergence.

## Late-Game Redesign Override

Use the Required Chapter Matrix, revised Mod Career Ledger, and revised quest-density budget as authority for everything after Renaissance.

Corrected late-game ladder:

- `Industrial Revolution`
- `Gilded Age`
- `Atomic`
- `Otherworldly`
- `Ascension`

Ownership correction:

- `Industrial Revolution` owns the first major systems-weaving factory age: IE, Oritech, PneumaticCraft, MI entry, storage/network discipline, and corrected oil stack work.
- `Gilded Age` owns scaling and authorization: NauTec, Astral Dimension/Void Titan proof, advanced applied industry, computation/storage scale, and authorization proofs.
- `Atomic` owns containment and consequence: Mekanism/Nuclear Science/Ballistix/MFF/Macabre/hazardous systems.
- `Otherworldly` owns operations beyond the world: launch, interdimensional infrastructure, high Oritech/cosmic systems, and late network scale.
- `Ascension` owns final synthesis: Draconic, Extended Crafting, Re:Avaritia, F&A Tier 5 final-station use, and `aoa:archive_of_ages`-style convergence.

Late-game production should now follow this order:

1. repair stale chapter ownership and removed-mod references
2. integrate Industrial/Gilded oil, Oritech, MI, IE, PneumaticCraft, NauTec, and authorization proof chains
3. build Atomic containment/hazard systems around real proof outputs
4. build Otherworldly launch/cosmic operations as the canonical off-world spine

## Full-Pack Distribution

The current target is `3,225-3,975` total quests, not the old `2444` floor.

| bucket | target range | purpose |
| --- | --- | --- |
| required progression | roughly `75%` | required matrix chapters, process chains, proof recipes, capstones |
| optional depth | roughly `25%` | trophies, side bosses, prestige challenges, cosmetics, alternate routes inside chapters |
| annex/support | bounded only | support systems and references that should not become required catalog work |

This keeps the pack large while avoiding fake density in Dark Age, Medieval, decor, structures, ordinary mob mods, and removed systems.

## Chapter Budget By Age

Use this working production map:

| age | target total | production intent |
| --- | --- | --- |
| Dark Age | `50-75` | survival prologue only |
| Medieval | `125-175` | workshop and settlement prologue only |
| Renaissance | `400-475` | first true curriculum age |
| Industrial Revolution | `500-600` | first major systems-weaving age |
| Gilded Age | `500-600` | scaling and authorization age |
| Atomic | `700-850` | consequence and containment age |
| Otherworldly | `450-550` | operations beyond the world |
| Ascension | `500-650` | final synthesis thesis |

## Renaissance-And-Later Production Plan

The old Expedition/Automation/Space sections below this point were pruned because they carried removed-mod and old-age-model assumptions. Keep the useful production idea: build from lean prologue into increasingly dense system curricula.

Current batch order:

1. Dark Age: survival prologue only, `50-75` quests.
2. Medieval: workshop/settlement prologue only, `125-175` quests.
3. Renaissance: first real curriculum age, with magic literacy, realm literacy, recordkeeping, and F&A Tier 1 foundation.
4. Industrial Revolution: IE/Oritech/PneumaticCraft/MI entry, corrected oil stack, storage/network discipline.
5. Gilded Age: NauTec oceanic industry, Astral/Void Titan authorization, scaled computation/storage, advanced applied industry.
6. Atomic: containment, radiological materials, Macabre/MFF/Ballistix/Mekanism consequence systems.
7. Otherworldly: launch, interdimensional infrastructure, high Oritech/cosmic systems.
8. Ascension: Draconic, Extended Crafting, Re:Avaritia, completed F&A Tier 5 station, and final archive synthesis.

## Tracker Rules

When tracker rows disagree with the matrix/ledger, correct the row in place instead of deleting the entire tracker.

- `status=stale/remove_candidate` means keep only as cleanup evidence.
- Required rows must name a Required Chapter Matrix chapter or a current capstone/proof role.
- Optional rows must be inside chapters as side content, trophies, cosmetics, prestige, or Modonomicon-only support.
- Rows for decor, structures, ordinary mobs, QoL, and ambient content should stay support/watchlist unless explicitly promoted by the matrix.
- Rows with removed mods must not be used for implementation prompts.

## Boss-Spine Governance

Bosses provide boss-specific proofs only. They may feed capstone recipes or required chapter proofs, but they normally do not directly grant `industrial_revolution`, `gilded_age`, `atomic`, `otherworldly`, or `ascension`. Current exception: the Maledictus FTBQ kill quest directly grants `industrial_revolution` as legacy bridge debt; IR chapters now exist.

FTB Quest capstone rewards/AStages are the progression-proof authority. KubeJS must not read, grant, revoke, or mutate progression stages.
