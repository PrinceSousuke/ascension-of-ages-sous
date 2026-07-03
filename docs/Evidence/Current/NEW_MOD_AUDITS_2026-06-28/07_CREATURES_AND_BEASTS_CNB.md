# Creatures And Beasts / CNB Audit

## Status

Jar: `mods/CNB-1.21.1-neoforge-1.7.17.jar`

Namespace: `cnb`

Current AoA coverage: no live FTBQ/KubeJS/config coverage found for `cnb:`. Existing Yeti hits are unrelated other-mod content.

Source: https://www.curseforge.com/minecraft/mc-mods/creatures-and-beasts-continued

## Meaningful Content

Best quest candidates:

- `cnb:cinder_furnace`
- `cnb:cinder_sword`
- `cnb:cindershell_shell_shard`
- `cnb:cactem_spear`
- `cnb:entity_net`
- `cnb:sporeling_backpack`
- `cnb:yeti_antler`
- `cnb:yeti_hide`
- `cnb:cindershell_bucket`
- `cnb:heal_spell_book_1`, `_2`, `_3` only if acquisition is verified.

Entities with possible quest value:

- `cnb:cactem`
- `cnb:cindershell`
- `cnb:sporeling`
- `cnb:yeti`
- `cnb:end_whale`

## Suggested Quests

| Quest | Target | Age | Notes |
|---|---|---|---|
| Cactem Spear | `cnb:cactem_spear` | Medieval/Renaissance desert side | Useful drop-backed combat proof. |
| Cindershell Furnace | `cnb:cinder_furnace` | Renaissance Nether | Real utility block from Cindershell chain. |
| Cinder Sword | `cnb:cinder_sword` | Renaissance Nether | Good optional weapon target. |
| Sporeling Pack | `cnb:sporeling_backpack` | Renaissance swamp/mushroom/lush cave | Companion utility. |
| CNB Yeti Proof | `cnb:yeti_antler` or `cnb:yeti_hide` | Industrial/cold side | Only with explicit disambiguation from existing Yeti content. |

## Defer

- `cnb:entity_net` until capture-bypass risk is tested.
- `cnb:end_whale` until traversal utility and proof target are clear.
- Heal spell books until acquisition path is verified.
- Lizard, Little Grebe, Minipad, Lilytad, waterlily/flower variants, and flower crowns unless a future wildlife chapter wants flavor.

## Cross-Weave Candidates

- Nether threshold: Cindershell to cinder furnace/sword.
- Cold biome/Industrial side gear: CNB Yeti drops with existing Yeti lines, but names must be clear.
- Expedition: End Whale only if it has a real player-facing use.
- Capture systems: entity net only after bypass testing.

## Do Not Quest

- Spawn eggs.
- Every creature.
- Decorative waterlily/minipad/flower variants.
- CNB Yeti without disambiguating from existing Yeti quests.

## Verify Flags

- `[VERIFY]` generated config after first launch.
- `[VERIFY]` `entity_net` capture bypass risk.
- `[VERIFY]` End Whale mechanics and spawn density.
- `[VERIFY]` heal spell book acquisition path.
- `[VERIFY]` CNB nether bridge loot modifier balance.

