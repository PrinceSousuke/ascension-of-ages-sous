# Create Aquatic Ambitions Audit

## Status

Jar: `mods/create_aquatic_ambitions-1.21.1-2.0.2.jar`

Namespace: `create_aquatic_ambitions`

Current AoA coverage: no direct FTBQ or KubeJS references found for `create_aquatic_ambitions:`.

Sources:

- https://www.curseforge.com/minecraft/mc-mods/create-aquatic-ambitions
- https://modrinth.com/mod/create-aquatic-ambitions/versions

## Verified Meaningful Targets

Strong targets:

- `create_aquatic_ambitions:mechanical_conduit`
- `create_aquatic_ambitions:prismarine_alloy`
- `create_aquatic_ambitions:prismarine_alloy_rod`
- `create_aquatic_ambitions:prismarine_alloy_block`
- `create_aquatic_ambitions:calcium_rich_powder`
- `create_aquatic_ambitions:suspicious_rock`
- `create_aquatic_ambitions:spiky_shell`
- Crafted `minecraft:trident` using the mod recipe.
- Channeling path to `minecraft:heart_of_the_sea`.

Reverify before authoring:

- `create_aquatic_ambitions:nautilus_shard` appeared in lang/static extraction but should be runtime-registry verified before quest use.

Do not author from static model-only evidence:

- `prismarine_rod`
- `flint_shard`
- `polished_quartz_tine`

## Mechanics

The mod is not a broad ocean content mod. It is a Create automation bridge for ocean resources:

- Prismarine alloy and rods.
- Conduit Cage / mechanical conduit.
- Channeling recipes for ocean-resource automation.
- Coral revival.
- Wet sponge revival.
- Prismarine shard/crystal automation.
- Copper weathering/deweathering automation.
- Craftable trident.
- Heart of the Sea route.

## Placement

Best fit: late Renaissance or Gilded.

Reasoning:

- It can make powerful vanilla ocean loot such as trident and Heart of the Sea craftable or automatable.
- It naturally bridges Create to NauTec, which is already live-covered in Gilded.
- Early placement would flatten exploration and drowned/trident rarity too much.

## Suggested Quests

| Quest | Target | Placement | Notes |
|---|---|---|---|
| Alloy From the Reef | `create_aquatic_ambitions:prismarine_alloy` | Late Renaissance/Gilded | First material proof. |
| Conduit Cage | `create_aquatic_ambitions:mechanical_conduit` | Gilded ocean industry | Main machine/block target. |
| Channeling Lab | Manual/checkmark or recipe target | Gilded | Explain that channeling recipes unlock renewable ocean resources. |
| Suspicious Rock Wash | `create_aquatic_ambitions:suspicious_rock` | Gilded | Good bridge into processing loops. |
| Spiky Shell | `create_aquatic_ambitions:spiky_shell` | Gilded | Trident prerequisite. |
| Forged Trident | `minecraft:trident` | Gilded optional | Use only after deciding that craftable tridents are intended. |
| Manufactured Heart | `minecraft:heart_of_the_sea` | Gilded/Atomic optional | Strong FOMO callout, not mainline unless NauTec needs it. |

## Cross-Weave Candidates

- NauTec: require prismarine alloy or mechanical conduit near `aquatic_catalyst` or `deep_sea_drain`.
- Hybrid Aquatic: combine `spiky_shell`, black pearl, or deep-ocean exploration before the trident/Heart path.
- Create: use deployer/mixer/washer literacy for coral and prismarine loops.

## Do Not Quest

- Coral variants individually.
- Copper weathering variants individually.
- Every channeling output.

## Verify Flags

- `[VERIFY]` runtime registry for `nautilus_shard`.
- `[VERIFY]` JEI visibility and actual acquisition of `spiky_shell`.
- `[VERIFY]` whether craftable Heart of the Sea and trident are acceptable at the selected age.
