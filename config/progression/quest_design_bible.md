# Quest Design Bible

## Purpose

This file is the authoritative design contract for the `Ascension of Ages (test5)` questbook.

It exists to keep quest implementation readable, scalable, and progression-safe while supporting a very large authored book.

This file governs quest structure, density, tone, visibility, and reward behavior. It must be treated as the first source of truth before any large SNBT authoring pass.

## Authority Order

When files disagree, use this order:

1. `quest_design_bible.md`
2. `quest_ui_style.md`
3. `quest_chapter_plan.json`
4. `quest_source_audit.md`
5. `change_log.md`
6. quest SNBT implementation files

## Non-Negotiables

1. The questbook must keep the corrected age backbone:
   - `Stone Age`
   - `Mechanical Age`
   - `Expedition Age`
   - `Automation Age`
   - `Industrial Age`
   - `Nuclear Age`
   - `Space Age`
   - `Ascension`
2. Future age groups remain hidden until their unlock gate is reached.
3. Boss progression is represented inside each age, not as a global boss codex.
4. Existing imported questline-heavy content can remain, but it does not count toward the authored quest target.
5. The authored quest target is `2444` new quests minimum.
6. No manual-check or empty confirmation quests are allowed.
7. Every quest must use a real milestone task:
   - item acquisition
   - crafted component
   - built workstation or machine
   - boss kill
   - advancement
   - dimension or structure milestone
   - stage-dependent prerequisite
8. Quest copy must stay minimal. The book should teach mostly through doing, not through large blocks of explanation.

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

- Minimum authored quest target: `2444`
- Existing imported content is additional surface area and may sit above that target

## Chapter Group Model

Each top-level age is a `chapter_group`.

Required groups:

1. `Stone Age`
2. `Mechanical Age`
3. `Expedition Age`
4. `Automation Age`
5. `Industrial Age`
6. `Nuclear Age`
7. `Space Age`
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

The 2444-authored-quest target must be reached through disciplined chapter classes, not filler.

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
- do not silently increase the total authored target above `2444` just because chapter sums drift high

If an age starts over-allocating:

1. reduce or split oversized chapter targets
2. move optional content into later ages or annexes
3. preserve spine density before expanding side content

## 2444 Distribution Model

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

### Stone Age

The player is vulnerable, cold, thirsty, badly equipped, and forced to build real survival habits.

Required chapter themes:

- primitive materials
- safe water
- heat and shelter
- wounds and recovery
- food stability
- early travel planning
- low-tier treasure and controlled fights

### Mechanical Age

The player gains first true work relief through iron, Create, and manual-to-mechanical workshop upgrades.

Required chapter themes:

- ironwork
- workstations
- first machines
- workshop organization
- early logistics
- first dependable dungeon readiness

### Expedition Age

The player widens their world through diamonds, first major magic, dimensions, stronger storage, and better treasure routes.

Required chapter themes:

- diamond threshold
- major magic branch
- first serious storage branch
- dimension access
- stronger adventure prep
- better locks, routes, and structures

### Automation Age

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

### Nuclear Age

The player graduates from large industry into hazardous processing, reactor discipline, and hardened facility logic.

Required chapter themes:

- containment and hazard discipline
- hazardous chemical processing
- reactors and isotope infrastructure
- hardened grids and power campuses
- strategic defense and facility warfare

### Space Age

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

- `Stone Age -> Mechanical Age`
- `Mechanical Age -> Expedition Age`
- `Expedition Age -> Automation Age`
- `Automation Age -> Industrial Age`
- `Industrial Age -> Nuclear Age`
- `Nuclear Age -> Space Age`
- `Space Age -> Ascension`

Gate chapters must feel like structural thresholds, not random side tasks.

## Boss Chapter Rules

Stone Age is the exception. Every age from `Mechanical Age` onward has a dedicated boss chapter.

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
- `Ars Nouveau + survival systems`
- `manual storage -> smart storage -> digital networks`
- `Oritech + Modern Industrialization + Mekanism`
- `Industrial Foregoing + Hostile Neural Networks`
- `Mystical Agriculture + late-game tech`
- `adventure + waystones + treasure clues + lock tiers`

Synergy chapters must teach useful combinations without making the combined systems overpowered ahead of schedule.

## Source Usage Rules

Use reference packs as research input only.

Primary research sources:

- `Age of Fate (1)`
- `All the Mods 10`

Use AOF mainly for:

- Create
- Ars Nouveau
- Apotheosis
- Industrial Foregoing
- Hostile Neural Networks
- Ice and Fire
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

- authored quest count exceeds `2444`
- every age has a main gate chapter
- every age has a boss chapter
- every major chapter uses real milestone tasks
- future age groups stay hidden until unlocked
- annexes are isolated and do not replace the mainline
- rewards respect stage identity
- cross-mod relief and synergy lines are present in every major age
