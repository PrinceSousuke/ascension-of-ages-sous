# Arcane Lanterns Audit

## Status

Jar: `mods/ArcaneLanterns-v21.1.0-1.21.1-NeoForge.jar`

Namespace: `arcanelanterns`

Current AoA coverage: no `arcanelanterns:` references found in FTBQ, KubeJS, docs, config, or generated defaults during this pass.

Source: https://www.curseforge.com/minecraft/mc-mods/arcane-lanterns

## Verified Content Surface

The mod is compact and quest-friendly: one crafting station plus ten functional lanterns. The hanging block variants are variants, not separate quest targets.

| Target | Function from jar lang | Placement |
|---|---|---|
| `arcanelanterns:lantern_maker` | Required station for imbuing lanterns. | Early Renaissance or Nether threshold. |
| `arcanelanterns:life_lantern` | Speeds crop growth nearby. | Medieval farming side or early Renaissance. |
| `arcanelanterns:feral_lantern` | Spawns temporary sparks over a large area. | Renaissance Nether/exploration. |
| `arcanelanterns:cloud_lantern` | Applies slow fall nearby. | Renaissance exploration/safety. |
| `arcanelanterns:warding_lantern` | Pushes living entities except players away. | Renaissance base safety. |
| `arcanelanterns:containing_lantern` | Confines living entities except players to an area. | Renaissance/Industrial mob handling. |
| `arcanelanterns:boreal_lantern` | Slows entities and extinguishes burning mobs. | Optional cold/hazard side quest. |
| `arcanelanterns:love_lantern` | Makes nearby mobs breed. | Optional husbandry automation. |
| `arcanelanterns:wailing_lantern` | Nausea/trap effect. | Defer. |
| `arcanelanterns:withering_lantern` | Wither area effect. | Defer to hazard lab if used. |
| `arcanelanterns:brilliant_lantern` | Converts nearby animals into XP. | Defer or gate carefully. |

## Suggested Quest Mini-Chain

| Quest | Target type | Target | Why |
|---|---|---|---|
| Build the Lantern Maker | Item | `arcanelanterns:lantern_maker` | Teaches the station. Recipe uses polished basalt and diamond. |
| Living Fields | Item | `arcanelanterns:life_lantern` | Direct farming QoL without being a hard gate. |
| Feral Survey Light | Item | `arcanelanterns:feral_lantern` | Makes base/exploration lighting feel magical and useful. |
| Cloud Lantern Safety | Item | `arcanelanterns:cloud_lantern` | Good tower/cave/fall-safety quest. |
| Warding Perimeter | Item | `arcanelanterns:warding_lantern` | Teaches base perimeter utility. |
| Containment Workshop | Item | `arcanelanterns:containing_lantern` | Pairs naturally with mob farms, cages, and testing rooms. |

## Cross-Weave Candidates

- Farming: Life Lantern near crop pressure quests.
- Exploration: Cloud Lantern near Aether, towers, caves, or fall-damage risk.
- Base safety: Warding/Containing Lantern near mob containment or Hostile Neural Networks onboarding.
- Arcane hazard lab: Withering/Boreal/Wailing only as optional "use responsibly" content.

## Do Not Quest

- Hanging variants separately.
- Every lantern as a required chain.
- Brilliant Lantern as required progression until animal-to-XP behavior is balance-tested.

## Verify Flags

- `[VERIFY]` Feral spark density and cleanup behavior in an AoA base.
- `[VERIFY]` Brilliant Lantern XP conversion balance.
- `[VERIFY]` generated config availability after launch; no live config was found.

