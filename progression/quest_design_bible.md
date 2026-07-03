# Quest Design Bible

## Current 2026-05-13 Alignment

This document is active planning/reference material, but it is subordinate to the live FTB Quests SNBT, live lang files, live `mods/*.jar`, and the current AStages/KubeJS restriction surface. Preserve useful architecture from this file, but rewrite stale specifics against current implementation first, then evidence docs, then planning docs:

- `config/ftbquests/quests/**/*.snbt`
- `config/modpack_defaults/config/ftbquests/quests/**/*.snbt`
- `kubejs/server_scripts/aoa_astages_00_register_stages.js`
- `kubejs/server_scripts/aoa_astages_*.js`
- `kubejs/assets/**/lang/*.json`
- `docs/Evidence/Current/*.md`
- `audit_artifacts/AOA_REQUIRED_CHAPTER_MATRIX_2026-05-13.md`
- `audit_artifacts/AOA_MOD_CAREER_LEDGER_REVISED_2026-05-13.tsv`
- `audit_artifacts/AOA_REVISED_QUEST_DENSITY_BUDGET_2026-05-13.md`



## Purpose

This file is an active design reference for the `Ascension of Ages (codex and cc)` questbook. It is subordinate to live FTB Quests/KubeJS implementation and current evidence docs.

It exists to keep quest implementation readable, scalable, and progression-safe while supporting a very large authored book.

This file governs quest structure, density, tone, visibility, and reward behavior. It must be checked against live quest/KubeJS files before any large SNBT authoring pass.

## Authority Order

When files disagree, use this order:

1. live quest SNBT, lang, KubeJS recipe/restriction/stage files, and installed `mods/*.jar`
2. `docs/Evidence/Current/*.md`
3. `audit_artifacts/AOA_REQUIRED_CHAPTER_MATRIX_2026-05-13.md`
4. `audit_artifacts/AOA_MOD_CAREER_LEDGER_REVISED_2026-05-13.tsv`
5. `audit_artifacts/AOA_REVISED_QUEST_DENSITY_BUDGET_2026-05-13.md`
6. this design bible and `quest_ui_style.md`
7. `quest_chapter_plan.json` and `quest_production_tracker.csv`

## Non-Negotiables

1. The questbook must keep the current age backbone: Dark Age, Medieval, Renaissance, Industrial Revolution, Gilded Age, Atomic, Otherworldly, Ascension.
2. Every required chapter in the Required Chapter Matrix is required; optionality belongs inside chapters.
3. Dark Age and Medieval are lean prologues. Do not inflate them with fake catalog quests.
4. Future age groups remain hidden until their unlock gate is reached.
5. Bosses provide boss-specific proof only. Major age stages are awarded by FTB Quest capstone rewards/AStages, never by KubeJS stage mutation.
6. The authored questbook target is roughly 3,225-3,975 total quests, with about 75% required progression and 25% optional prestige/depth.
7. No manual-check or empty confirmation quests are allowed.
8. Every quest must use a real milestone task: item acquisition, crafted component, built workstation or machine, boss proof, advancement, dimension/structure milestone, or verified stage-dependent prerequisite.
9. Quest copy must stay minimal. The book should teach mostly through doing, not through large blocks of explanation.

## Authored Quest Count Policy

### Counted

- All newly written AoA quests created for this pass
- New connector chapters
- New annex bridge chapters
- New stage-gate chapters
- New boss hunt chapters

### Not Counted

- Existing `minecolonies` quests already present in the pack
- Existing `when_dungeons_arise` quests already present in the pack
- Any other preexisting imported questline content left intact

### Target

- Total authored quest target: `3,225-3,975`
- Rough required share: `75%`
- Rough optional/prestige/depth share: `25%`
- Existing imported content is additional surface area and may sit above that target

## Chapter Group Model

Each top-level age is a `chapter_group`.

Required groups:

1. `Dark Age`
2. `Medieval`
3. `Renaissance`
4. `Industrial Revolution`
5. `Gilded Age`
6. `Atomic`
7. `Otherworldly`
8. `Ascension`
9. `Annexes`

### Group Purpose

- Age groups carry main progression, system teaching, and boss readiness.
- `Annexes` contains large optional systems or imported questlines that are tied into the mainline through custom bridge chapters.

## Chapter Ordering Rules

Inside an age group, order chapters like this:

1. `main gate / threshold`
2. `core survival or system foundation`
3. `major branches`
4. `synergy and relief chapters`
5. `adventure / dimension / structure chapters`
6. `boss hunt / validator chapter`
7. `connector / handoff chapter` if needed

## Density Rules

This questbook is intentionally dense.

Quest count is not treated as something to minimize. Density is created by splitting meaningful gameplay into concrete, readable steps rather than padding with empty confirmations.

### Required pattern

Break major tasks into dependency-linked chains such as:

1. gather raw materials
2. craft the first intermediate part
3. build the relevant workstation or machine
4. perform one useful action with it
5. use that output to make life easier
6. connect that use case to another system

### Example

- Acquire logs
- Process wood into planks and sticks
- Make primitive binding or cutting tools
- Build campfire
- Cook safe food
- Prepare food for travel

This pattern is expected across survival, magic, tech, storage, boss prep, and logistics chapters.

## Production Density Classes

The 3,225-3,975 authored-quest target must be reached through disciplined chapter classes, not filler.

Use these defaults unless a chapter is explicitly promoted into a larger multi-phase arc:

- `major arc chapter`: `20-40` quests
- `support / utility chapter`: `6-15` quests
- `micro utility beat`: `1-4` quests inside an existing chapter
- `gate chapter`: `3-8` quests
- `boss / validator chapter`: `8-20` quests

Rules:

- If a chapter wants to exceed `40` quests, split it into two linked arcs or define internal phases before implementation grows further.
- Utility mods do not get major-arc treatment unless the plan explicitly promotes them.
- Small convenience mods should usually live as micro beats or short support beats inside existing chapters.
- Gate chapters stay short and dense. They should validate readiness, not become pseudo-branches.

## Budget Authority Rules

The questbook has two different planning layers:

- age-group quest budgets
- per-chapter quest targets

When those layers disagree, the age-group budget wins.

This means:

- `group_targets` / `new_authored_quest_target` is the authoritative budget by age
- chapter `quest_target` values are production targets that may need later rebalance
- do not silently inflate Dark Age or Medieval, and keep global totals inside the `3,225-3,975` target range unless the matrix is revised

If an age starts over-allocating:

1. reduce or split oversized chapter targets
2. move optional content into later ages or annexes
3. preserve spine density before expanding side content

## Revised Back-Loaded Distribution Model

The authored total does not need to be almost entirely mandatory spine progression.

Use this approximate full-pack distribution:

- `core spine + major tech/magic progression`: `1200-1300`
- `support / synergy / utility chapters`: `450-550`
- `optional dimensions / side systems / annex bridges`: `250-350`
- `gates / boss hunts / mastery validators / postgame cleanup`: `150-250`

This keeps the book large without turning it into a checklist of low-value tasks.

## Text Economy Rules

Quest text is not the primary teaching tool.

Use:

- concise chapter titles
- concise quest titles
- one-line subtitles when needed
- no more than one short line of body copy unless the task is genuinely unclear without it

Prefer:

- dependency flow
- concrete task ordering
- visual routing
- item and machine requirements

Avoid:

- long paragraphs
- lore-heavy explanation
- repeating the same teaching in subtitle and description
- explaining obvious actions the dependency chain already teaches

## Quest Naming And Description Rules

Use plain, functional quest titles.

Rules:

- do not use esoteric, poetic, cryptic, or dramatic naming
- titles should immediately tell the player what the quest is about
- most normal crafting and progression quests should have no description if the title and task are already clear
- descriptions must earn their existence

Descriptions are reserved for:

- chapter openers
- signpost or introduction quests
- confusing mechanics
- tasks where the practical purpose is not obvious from title plus task alone

Description limits:

- `0-2` sentences maximum
- explain practical purpose, not flavor or lore
- do not write lore paragraphs
- do not add descriptions only for style consistency
- when in doubt, leave the description blank

## Quest Family Model

Each meaningful chapter should include several of these families:

- `foundation`
  - raw materials, starter parts, first crafts
- `assembly`
  - workstation, ritual, machine, or infrastructure setup
- `usage`
  - use the system for one real result
- `relief`
  - show how the system removes labor, danger, or travel cost
- `synergy`
  - connect the system to another lane or mod
- `scale_up`
  - increase throughput, reliability, or reach
- `validation`
  - prove readiness through combat, adventure, or a higher build requirement

No major mod chapter should be a single short line with one or two quests.

## Mainline Age Identity

### Dark Age

The player is vulnerable, cold, thirsty, badly equipped, and forced to build real survival habits.

Required chapter themes:

- primitive materials
- safe water
- heat and shelter
- wounds and recovery
- food stability
- early travel planning
- low-tier treasure and controlled fights

### Medieval

The player gains first true work relief through iron, Create, and manual-to-mechanical workshop upgrades.

Required chapter themes:

- ironwork
- workstations
- first machines
- workshop organization
- early logistics
- first dependable dungeon readiness

### Renaissance

The player widens their world through diamonds, first major magic, dimensions, stronger storage, and better treasure routes.

Required chapter themes:

- diamond threshold
- major magic branch
- first serious storage branch
- dimension access
- stronger adventure prep
- better locks, routes, and structures

### Industrial Revolution

The player turns outward-expedition gains into repeatable machine lines, stable routing, and dependable powered production.

Required chapter themes:

- first powered factory backbone
- stable routing and buffering
- dependable grid support
- machine-campus discipline
- structured handoff into Industrial Age

### Industrial Age

The player industrializes production and turns systems into repeatable infrastructure.

Required chapter themes:

- factory planning
- power infrastructure
- industrial machine chains
- advanced logistics
- gated synthetic resource loops
- stronger combat readiness

### Atomic

The player graduates from large industry into hazardous processing, reactor discipline, and hardened facility logic.

Required chapter themes:

- containment and hazard discipline
- hazardous chemical processing
- reactors and isotope infrastructure
- hardened grids and power campuses
- strategic defense and facility warfare

### Otherworldly

The player launches off-world, sustains remote operations, and scales true post-launch logistics and cosmic-grade systems.

Required chapter themes:

- launch infrastructure
- orbital or off-world survival
- large-scale digital networks
- late synthesis and antimatter-grade follow-through
- cosmic combat and draconic escalation

### Ascension

The player enters final prestige scale and true capstone progression.

Required chapter themes:

- prestige crafting
- absurd-scale automation
- exchange or conversion ethics
- capstone combat and project validation

## Gate Chapter Rules

Each age requires one clearly labeled gate or threshold chapter.

Required thresholds:

- `Dark Age -> Medieval`
- `Medieval -> Renaissance`
- `Renaissance -> Industrial Revolution`
- `Industrial Revolution -> Industrial Age`
- `Industrial Age -> Atomic`
- `Atomic -> Otherworldly`
- `Otherworldly -> Ascension`

Gate chapters must feel like structural thresholds, not random side tasks.

## Boss Chapter Rules

Dark Age and Medieval are lean prologues. Boss content before Renaissance should be bounded preparation, not the primary age-transition mechanism.

Rules:

- Stone exits through readiness and survival validation, not a mandatory boss kill
- bosses live inside the age they validate
- optional bosses may exist beside validators
- bosses should prove readiness, not replace the age's main system development
- rewards from boss chapters must not bypass the age they belong to

## Annex Policy

`Annexes` is where imported or unusually large optional questlines live.

Rules:

- annex content must not define the mainline
- annex chapters are connected to the mainline through custom AoA bridge chapters
- annexes do not count toward the authored quest target
- annex rewards must respect AoA stage pacing

Initial annex targets:

- `Minecolonies`
- `When Dungeons Arise`

## Reward Policy

Reward style is `Tutorial Boosts`.

Allowed:

- food
- bandages and basic medical supplies
- purified water and travel consumables
- low-volume machine starter parts
- books, notes, and routing aids
- sample catalysts that do not skip the core loop

Disallowed:

- rewards that collapse a lane's intended progression
- big resource dumps that trivialize age identity
- late-game items appearing early as quest freebies

## Cross-Mod Synergy Rules

Every major system chapter must include at least one practical cross-mod synergy family.

Required synergy areas:

- `Create + Create Integrated Farming + Slice and Dice`
- `Create + Farmer's Delight / Ocean's Delight / Aquaculture`
- `Create + Immersive Engineering`
- installed magic/ritual systems + survival or tech catalysts
- `manual storage -> smart storage -> digital networks`
- `Oritech + Modern Industrialization + Mekanism`
- `Industrial Foregoing + Hostile Neural Networks`
- late HNN/IF/Solar Flux synthesis only where matrix-approved
- `adventure + waystones + treasure clues + lock tiers`

Synergy chapters must teach useful combinations without making the combined systems overpowered ahead of schedule.

## Source Usage Rules

Use reference packs as research input only.

Primary research sources:

- `Age of Fate (1)`
- `All the Mods 10`

Use AOF mainly for:

- Create
- Apotheosis
- Industrial Foregoing
- Hostile Neural Networks
- Immersive Engineering
- Refined Storage
- Undergarden

Use ATM10 mainly for:

- Oritech
- Modern Industrialization
- Mekanism
- Integrated Dynamics
- PneumaticCraft
- Twilight Forest
- Draconic Evolution
- late digital/storage progression

Never import removed content such as `Advent of Ascension`.

## Implementation Order

1. maintain these design files
2. scaffold chapter groups and chapter registry
3. author Stone and Mechanical ages first
4. author Expedition and Automation ages
5. author Industrial and Nuclear ages
6. author Space and Ascension
7. wire annex connectors
8. run regression checklist

## Definition of Done

The questbook pass is not complete until all of the following are true:

- authored quest count exceeds `3,225-3,975`
- every age has a main gate chapter
- every age has a boss chapter
- every major chapter uses real milestone tasks
- future age groups stay hidden until unlocked
- annexes are isolated and do not replace the mainline
- rewards respect stage identity
- cross-mod relief and synergy lines are present in every major age
