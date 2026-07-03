# Hybrid Aquatic Audit

## Status

Jar: `mods/[1.21.1-Neoforge] Hybrid Aquatic 1.5.5.jar`

Mod id: `hybrid_aquatic`

Resource/data namespace: `hybrid-aquatic`

Current AoA coverage: no live FTBQ/KubeJS references found for `hybrid-aquatic:` or `hybrid_aquatic:`.

Source: https://modrinth.com/project/HH4FjUqN

## Scale

Static jar findings:

- 109 entity IDs.
- 220 biome modifiers.
- 205 loot tables.
- 75 recipe JSONs.
- Many food drops, hooks, diving gear, shells, clams, pearls, crab tools, plants, and habitat blocks.

This is the real ocean ecosystem mod in the new set. It should not be represented as "collect every fish"; it needs a small number of representative mechanical quests.

## Best Quest Targets

High-value targets:

- `hybrid-aquatic:fishing_net`
- `hybrid-aquatic:crab_pot`
- `hybrid-aquatic:diving_helmet`
- `hybrid-aquatic:diving_suit`
- `hybrid-aquatic:diving_leggings`
- `hybrid-aquatic:diving_boots`
- `hybrid-aquatic:barbed_hook`
- `hybrid-aquatic:glowing_hook`
- `hybrid-aquatic:magnetic_hook`
- `hybrid-aquatic:ominous_hook`
- `hybrid-aquatic:giant_clam`
- `hybrid-aquatic:pearl`
- `hybrid-aquatic:black_pearl`
- `hybrid-aquatic:message_in_a_bottle`
- `hybrid-aquatic:sea_message_book`
- `hybrid-aquatic:hydrothermal_vent_shaft`
- `hybrid-aquatic:sulfur`
- `hybrid-aquatic:karkinos_claw`
- Crab claws as a collection family, if used to reach Ominous Hook/Karkinos.

Good representative encounters:

- One reef fish cluster.
- One jellyfish or venom hazard.
- One shark or predator warning.
- One crustacean/crab route.
- One deep-ocean rare route.

## Suggested Quest Shape

| Quest | Target | Age | Why |
|---|---|---|---|
| A Living Shoreline | Manual/checkmark | Medieval/Renaissance | Introduce that ocean biomes have new ecology. |
| Net, Not Checklist | `hybrid-aquatic:fishing_net` | Medieval/Renaissance | Teaches capture without asking for every species. |
| Crab Pot Supper | `hybrid-aquatic:crab_pot` | Medieval/Renaissance | Food and passive collection utility. |
| First Dive Kit | any full diving piece or set | Renaissance | Teaches practical underwater exploration. |
| Giant Clam | `hybrid-aquatic:giant_clam` | Renaissance/Gilded | Strong source of pearl/black pearl FOMO. |
| Black Pearl | `hybrid-aquatic:black_pearl` | Gilded | Good rare-ocean milestone. |
| Ominous Hook | `hybrid-aquatic:ominous_hook` | Gilded optional | Prepares Karkinos as deliberate encounter. |
| Karkinos Proof | `hybrid-aquatic:karkinos_claw` | Gilded/Atomic optional | Boss/rare encounter proof. |
| Thermal Vent | `hybrid-aquatic:hydrothermal_vent_shaft` or sulfur | Gilded | Links ocean ecology to materials. |

## Cross-Weave Candidates

- Create Aquatic Ambitions: black pearl/deep-ocean proof before craftable Heart of the Sea or trident.
- NauTec: diving gear and black pearl before Gilded ocean industry.
- Aquaculture/Ocean's Delight: representative seafood quests, not species spam.
- Arcane Lanterns: Cloud/Warding lantern as base camp safety for ocean expeditions.

## Do Not Quest

- Every fish species.
- Spawn eggs.
- Plushies.
- Wood/crate variants.
- Coral variants.
- Ordinary food variants unless one teaches a mechanic.

## Verify Flags

- `[VERIFY]` runtime spawn density/performance. The jar ships 220 biome modifiers.
- `[VERIFY]` generated Hybrid config behavior. No generated config file was present yet.
- `[VERIFY]` `hybrid-aquatic:shark_tooth` acquisition. It appears relevant to recipes, but static audit did not prove shark loot acquisition.
- `[VERIFY]` Karkinos summon and reward path in-game.
