# Stage Identity Migration Note

## Purpose

This file records the canonical age/stage correction pass that normalized the pack around:

- `stone_age`
- `mechanical_age`
- `expedition_age`
- `automation_age`
- `industrial_age`
- `nuclear_age`
- `space_age`
- `ascension`

It is the implementation note for preserved legacy quest ids, changed stage ids, and the corrected age-gate mapping.

## Old And Hybrid Names Found

Canonical naming drift found in the current planning or implementation layer:

- `Iron (Mechanical)`
- `Diamond (Expedition)`
- `End (Automation)`
- `iron_age`
- `diamond_age`
- `end_age`
- `apex_age`
- player-facing gate labels still using `Iron Era` or `Diamond Threshold`

## Renamed Surfaces

Player-facing labels normalized:

- `Entering the Iron Era` -> `Entering the Mechanical Age`
- `Enter the Iron Era` -> `Enter the Mechanical Age`
- `Diamond Threshold` -> `Expedition Threshold`

Stage ids normalized:

- `iron_age` -> `mechanical_age`
- `diamond_age` -> `expedition_age`
- `end_age` -> `industrial_age`
- `apex_age` -> `ascension`

New canonical stage files added:

- `nuclear_age`
- `space_age`

## Preserved Legacy Internal Ids

These internal ids were intentionally preserved to avoid unnecessary quest-graph migration risk:

- `entering_the_iron_era`
- `diamond_threshold`
- `dragonfall_and_end_access`
- `ascension_age` chapter-group id in planning files

These ids remain implementation-safe as long as their display labels, stage grants, and semantics follow the canonical age ladder.

## Stage Id Changes And Command Surfaces

Changed live or supporting stage surfaces:

- `entering_the_iron_era.snbt`
  - `/stage grant {p} iron_age` -> `/stage grant {p} mechanical_age`
- `diamond_threshold.snbt`
  - `progressivestages_required_stage: "iron_age"` -> `progressivestages_required_stage: "mechanical_age"`
  - `/stage grant {p} diamond_age` -> `/stage grant {p} expedition_age`
- duplicated FTB Quests subtree mirrors updated to the same canonical values
- `annexes_index_and_signposting.snbt`
  - `iron_age` requirement -> `mechanical_age`
- `minecolonies.snbt`
  - `iron_age` requirements -> `mechanical_age`
  - `diamond_age` requirements -> `expedition_age`
- `astages_loot_tiers.js`
  - moved AStages loot restrictions from `iron_age`/`diamond_age` to `mechanical_age`/`expedition_age`
  - restriction ids renamed to `requires_mechanical_age` and `requires_expedition_age*`

Corrective cleanup on live gate ownership:

- removed the stale `automation_age` reward from the duplicated legacy `blaze_breakthrough.snbt`
- removed the stale `automation_age` reward from `kill_basalt_executioner`
- retained the real Expedition -> Automation stage grant on the Nether Gauntlet defeat inside `expedition_fortresses_and_hellish_trials.snbt`

## Age Gate Mapping

| age transition | quest id(s) | display name(s) | granted stage | live status |
| --- | --- | --- | --- | --- |
| Stone -> Mechanical | `entering_the_iron_era` | `Entering the Mechanical Age` | `mechanical_age` | live |
| Mechanical -> Expedition | `diamond_threshold` | `Expedition Threshold` | `expedition_age` | live |
| Expedition -> Automation | `3400000000003613` in `expedition_fortresses_and_hellish_trials` | `Nether Gauntlet` | `automation_age` | live |
| Automation -> Industrial | `3400000000004392` in `automation_age_boss_hunts` | `Ender Guardian` | `industrial_age` | live |
| Industrial -> Nuclear | `3400000000004927` in `dragonfall_and_end_access` | `The Harbinger` | `nuclear_age` | live |
| Nuclear -> Space | `space_launch_threshold` | `Space Launch Threshold` | `space_age` | planned scaffold |
| Space -> Ascension | `ascension_threshold` | `Ascension Threshold` | `ascension` | planned scaffold |

## Boss-Spine Correction Summary

- Stone remains outside mandatory boss-gated age completion.
- `mechanical_age_boss_hunts`, `expedition_boss_hunts`, `automation_age_boss_hunts`, `industrial_boss_hunts`, `nuclear_boss_hunts`, `space_boss_hunts`, and `ascension_boss_hunts` are the canonical boss-spine planning surfaces.
- `automation_age_boss_hunts` is now live and owns the real `industrial_age` grant through the `Ender Guardian` capstone.
- `dragonfall_and_end_access` is now live and owns the real `nuclear_age` grant through the `Dragonfall -> Outer End Reach -> Ancient Factory -> The Harbinger` chain.
- the first seven live Nuclear chapter surfaces now require `nuclear_age`, not `industrial_age`.

## Validation Checklist

- JSON planning files parse cleanly after the rename pass.
- No planning authority file should still use `Iron (Mechanical)`, `Diamond (Expedition)`, or `End (Automation)` as canonical age names.
- No live quest grant should still award `iron_age`, `diamond_age`, or `end_age`.
- Early visibility and stage-required quest surfaces now reference `mechanical_age` and `expedition_age`.
- Existing authored quest content was preserved; only stage commands, stage requirements, labels, and planning scaffolds were corrected.
