# FTB Ocean Mobs Audit

## Status

Jar: `mods/ftboceanmobs-21.1.4.jar`

Namespace: `ftboceanmobs`

Current AoA coverage: no live FTBQ/KubeJS quest coverage found for `ftboceanmobs:`.

Source: https://www.curseforge.com/minecraft/mc-mods/ftb-ocean-mobs

## Static Jar Findings

Visible lang/static surface:

- Blocks: `ftboceanmobs:abyssal_water`, `ftboceanmobs:energy_geyser`, `ftboceanmobs:sludge_block`.
- Item/material: `ftboceanmobs:sludge_ball`, `ftboceanmobs:abyssal_water_bucket`.
- Entities: `abyssal_sludge`, `abyssal_winged`, `corrosive_craig`, `mossback_goliath`, `rift_demon`, `rift_minotaur`, `rift_weaver`, `riftling_observer`, `shadow_beast`, `sludgeling`, `tentacled_horror`.
- Recipes: none found.
- Biome modifiers: none found.
- Loot tables: only `blocks/sludge_block` in the simple scan.
- Config: `config/ftboceanmobs-common.toml` only exposes `rift_weaver_arena_size = 48`.

Subagent bytecode scan also noted `rift_disruptor` and `drowning_shadows`, but these should not be authored as quest targets until runtime registry proof exists.

## Recommendation

Disable/remove or defer the jar for now.

Reasoning:

- It is not an ocean ecology layer.
- Hybrid Aquatic already fills the ocean ecosystem role better.
- Static evidence does not show natural spawn wiring, recipes, or pack quest ownership.
- Live config is minimal.
- Existing plan docs already recommended removing it, while the live jar remains.

If retained, make it a deliberate late optional rift/boss lane.

## If Kept: Quest Shape

| Quest | Target | Age | Notes |
|---|---|---|---|
| Abyssal Residue | `ftboceanmobs:sludge_ball` or `sludge_block` | Atomic/Otherworldly optional | Only if acquisition is proven. |
| Rift Disturbance | Manual/checkmark | Atomic/Otherworldly | Explain that this is not normal ocean wildlife. |
| Rift Weaver Arena | `ftboceanmobs:rift_weaver` proof or manual | Otherworldly | Needs runtime summon/spawn proof. |
| Rift Cleanup | boss drop or sludge proof | Otherworldly | Only after drop table is confirmed. |

## Cross-Weave Candidates

- Hybrid Aquatic: deep-sea threat escalation after Karkinos.
- Neo Vitae or Occultism: rift/abyss flavor, if a boss-lane exists.
- Otherworldly: ocean rift as a dimensional instability side boss.

## Do Not Quest

- Spawn eggs.
- Ambient rift mobs without an intentional spawn/summon path.
- The mod as early ocean content.

## Verify Flags

- `[VERIFY]` runtime spawn/summon path for Rift Weaver and rift mobs.
- `[VERIFY]` whether FTB Rift Helper or equivalent behavior is needed. `ftb-rift-helper` was not found installed during the ocean thread.
- `[VERIFY]` any residue in Apotheosis, Too Many Entities, sound config, or default configs before removal.

