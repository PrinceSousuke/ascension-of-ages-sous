# Critters And Companions Audit

## Status

Jar: `mods/crittersandcompanions-neoforge-1.21.1-2.4.0.jar`

Namespace: `crittersandcompanions`

Current AoA coverage: no live FTBQ/KubeJS/config coverage found for `crittersandcompanions:`.

Source: https://modrinth.com/mod/critters-and-companions

## Meaningful Content

Best quest candidates:

- `crittersandcompanions:silk`
- `crittersandcompanions:silk_cocoon`
- `crittersandcompanions:grappling_hook`
- `crittersandcompanions:silk_lead`
- `crittersandcompanions:clam`
- `crittersandcompanions:pearl`
- `crittersandcompanions:pearl_necklace_1`
- `crittersandcompanions:pearl_necklace_2`
- `crittersandcompanions:pearl_necklace_3`
- `crittersandcompanions:sea_bunny_slime_bottle`
- `crittersandcompanions:sea_bunny_slime_block`
- `crittersandcompanions:snail_slime_bottle`
- `crittersandcompanions:koi_fish_bucket`
- Dragonfly armor, if dragonfly riding/armor behavior is confirmed.

Relevant mechanics:

- `grappling_hook` is a real traversal utility.
- Pearl chain can become End-adjacent value.
- Sea bunny slime gives slime alternative.
- Silk is a material route.
- Loot injections include clam/ocean content.
- Ferret digging may reach strong treasure and needs balance review.

## Suggested Quests

| Quest | Target | Age | Why |
|---|---|---|---|
| Silk Line Mobility | `crittersandcompanions:grappling_hook` | Medieval/Renaissance | Real traversal and FOMO target. |
| Silk Lead | `crittersandcompanions:silk_lead` | Medieval/Renaissance optional | Simple utility follow-up. |
| Koi in a Bucket | `crittersandcompanions:koi_fish_bucket` | Stone/Medieval side | Small wildlife onboarding. |
| Pearls and Necklace | `crittersandcompanions:pearl_necklace_1` or `_3` | Renaissance ocean/End-adjacent | Curios necklace and pearl chain. |
| Sea Bunny Slime | `crittersandcompanions:sea_bunny_slime_bottle` | Medieval/Renaissance | Useful slime route. |

## Cross-Weave Candidates

- Hybrid Aquatic: pearls, clams, sea bunny slime, and ocean discovery.
- Arcane Lanterns: Life/Love Lantern with companion/husbandry content.
- Create: grappling hook and silk can be optional mobility before larger factories.

## Do Not Quest

- Every creature.
- Spawn eggs.
- Leaf insect, stick bug, shima enaga, ladybug, red panda, otter, and ferret as item tasks unless custom/manual objectives are desired.
- Every bucket variant.

## Verify Flags

- `[VERIFY]` generated config after first launch.
- `[VERIFY]` ferret digging loot. Totem-level treasure would need balancing.
- `[VERIFY]` clam loot injection balance.
- `[VERIFY]` dragonfly armor/riding behavior before questing it.
