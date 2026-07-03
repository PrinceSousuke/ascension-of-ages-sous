# AoA Mob & Ocean Overhaul — Execution Plan

Date: 2026-06-28 (Revision 2)
Platform: NeoForge 1.21.1, CurseForge
Status: ready to execute. One open decision flagged in Section 6.

## Revision 2 note

This revision is driven by a real constraint: the pack has heavy mob-hunt content (verified: 73 FTB Quests kill-tasks plus 40 questlog hunt-tasks) and prior player feedback that mobs were too sparse to find and caves posed no real danger. That changes the whole density direction. Specifically:

- The Born in Chaos cut list dropped from 13 to 10. Three of the proposed cuts (`dread_hound`, `corpse_fly`, `mr_pumpkin`) are live targets in the grove-hunt chain (`what_waits_in_the_grove`) and are now protected.
- The In Control! density reduction in the old Section 5C is reversed. Lowering the caps would make caves emptier and hunt mobs harder to find, which is the opposite of what the pack needs.
- Cave danger and "harder" now come from difficulty (Section 6), not from cutting counts. That makes the Section 6 pick load-bearing, not optional.
- The Alex's Mobs trims (catfish, lobster, terrapin) were verified clean: none are quest targets.

## Goal

Deepen the ocean into a real system, add ambient life to a world heavy on hostiles, and add one monster mod for variety, while keeping hostiles plentiful and findable for the pack's hunt quests and making caves genuinely dangerous through difficulty rather than raw volume. Only redundant filler gets trimmed. Every item below was verified against the live mods folder, config files, and quest files, or against CurseForge. Nothing here is guessed.

Net entity count rises with these adds. That is acceptable: the pack's measured lag is chunk generation during exploration (a separate budget), not entity tick load, and the difficulty-first approach makes caves dangerous without flooding them with entities.

## 1. Add

| Mod | Role | Build / notes | Drop-in status |
|---|---|---|---|
| Hybrid Aquatic | Ocean creatures (30+ fish, 10 sharks, crabs, diving gear) | 1.21.1 NeoForge 1.5.5 | Needs Curios (verify present). Prune species in Section 5E. |
| Create: Aquatic Ambitions | Create ocean/prismarine/coral/copper automation | 1.21.1 NeoForge 2.0.2, needs Create 6.0.6+ | Create 6.0.10 installed. Clean. |
| Critters & Companions | Ambient fauna (otters, ferrets, red pandas, koi, octopus) | 1.21.1 NeoForge 2.4.0 | Clean. |
| Creatures & Beasts: Continued | Ambient fauna (swamp, nether, End niches) | 1.21.1 NeoForge 1.7.17 | Clean. |
| Mobs of Mythology | New monster variety (Automaton, Chupacabra, Drake, Kobold, Basilisk) | Use 2.2.2 (proven), NOT 3.0.0 (10 days old) | All 7 deps already in pack. Clean. |
| Boids (optional) | Flocking AI for fish, no new entities | 1.21.1 NeoForge 1.0.3 | Near-zero cost. |

## 2. Trim / remove

| Mod | Action | Reason |
|---|---|---|
| FTB Ocean Mobs | Remove the jar | Inert (no default spawns, zero quest/script/datapack wiring). Hybrid Aquatic supersedes its role. |
| Born in Chaos | Keep, cut 10 redundant filler spawners (Section 5A) | Lower nighttime clutter while keeping every miniboss, boss, AND every quest-target mob. |
| Alex's Mobs | Keep, fix catfish + coastal crowd (Section 5B) | Removes the catfish never-despawn bug and over-tuned coastal spawns. Verified not quest targets. |

## 3. Decided against (do not add)

- Mekanism Mobs. Dropped by choice.
- Cave Dweller / single-stalker horror. Dropped (one repeated mob gets old).
- Bosses of Mass Destruction. Already installed.
- Champions, Infernal Mobs. Redundant with Apotheosis.
- DarkMobs. Conditional only, see Section 6.

## 4. Difficulty + density model

The pack needs hostiles to stay plentiful and findable (70+ hunt quests) and caves to feel dangerous. The model:

- Keep density: do NOT cut natural spawn caps. Leave In Control! as is (Section 5C explains why).
- Remove only redundant filler: the 10 Born in Chaos generic zombies/skeletons that duplicate Variants & Ventures and MonsterPlus (Section 5A), plus the buggy/over-tuned Alex's coastal mobs (Section 5B). This trims clutter without thinning the hunt pool.
- Make encounters dangerous through difficulty, not volume:
  - Apotheosis invading affix-bosses, made more frequent (Section 5D), give caves and the surface periodic hard, varied threats.
  - A baseline difficulty layer (Section 6) makes ordinary cave mobs hit harder so caves are threatening without needing more of them.
- Let Me Despawn (installed) clears lingering modded mobs so the cleanup is automatic. No action.

## 5. Exact config edits

All paths relative to the instance root. Back up each file before editing. Mirror anything you want shipped as a default into `defaultconfigs/` and/or `config/modpack_defaults/`.

### 5A. Born in Chaos — cut 10 redundant filler spawners

File: `config/borninconfiguration-general.toml`

Set these 10 keys to `false` (currently `true`). This removes generic zombies/skeletons already covered elsewhere plus a couple of low-value swarm mobs, roughly a 37% cut to Born in Chaos added spawn weight, while keeping every miniboss, boss, and quest target.

```
ZOMBIE_FISHERMAN_SPAWNING_ENABLED  = false
DECAYING_ZOMBIE_SPAWNING_ENABLED   = false
ZOMBIE_LUMBERJACK_SPAWNING_ENABLED = false
ZOMBIE_BARREL_SPAWNING_ENABLED     = false
BABY_SKELETON_SPAWNING_ENABLED     = false
DECREPIT_SKELETON_SPAWNING_ENABLED = false
BABY_SPIDER_SPAWNING_ENABLED       = false
CORPSE_FISH_SPAWNING_ENABLED       = false
FIRELIGHT_SPAWNING_ENABLED         = false
PUMPKIN_DUNCE_SPAWNING_ENABLED     = false
```

PROTECTED, do NOT disable (grove-hunt quest targets in `what_waits_in_the_grove`):

```
DREAD_HOUND   (keep)   # hunt target, hounds-and-knights chain
CORPSE_FLY    (keep)   # hunt target
MR_PUMPKIN    (keep)   # hunt target
```

Config applies on world load (restart, not `/reload`).

Live in-world test alternative (gamerules, instant). Nine of the ten have gamerules; `PUMPKIN_DUNCE` is config-only.

```
/gamerule zombieFishermanSpawn false
/gamerule decayingZombieSpawn false
/gamerule zombieLumberjackSpawn false
/gamerule zombiesinaBarrelSpawn false
/gamerule babySkeletonSpawn false
/gamerule decrepitSkeletonSpawn false
/gamerule babySpiderSpawn false
/gamerule corpseFishSpawn false
/gamerule firelightSpawn false
```

Authority caveat: config-vs-gamerule precedence in this addon is unconfirmed. Test with a gamerule first; if a mob still spawns after a config-only disable, the gamerule is the fallback.

### 5B. Alex's Mobs — fix catfish + coastal crowding

File: `config/alexsmobs-common.toml`, section `[spawning]`. Verified not quest targets.

```
catfishSpawnWeight  = 0      # was 4. Kills the never-despawn pile-up bug.
lobsterSpawnWeight  = 3      # was 7. Coastal crowding.
terrapinSpawnWeight = 2      # was 4. Coastal crowding.
```

To keep catfish as flavor instead, leave a low weight and clear stacked ones once: `/kill @e[type=alexsmobs:catfish]`.

### 5C. In Control! — REVERSED, leave caps as they are

File: `config/incontrol/spawn.json`

The earlier plan lowered the per-chunk hostile caps (42/48/42). That is withdrawn. Reasons:

- Those caps are high ceilings that rarely trigger in normal play, so lowering them would START to bite and actively reduce cave density.
- With 70+ hunt quests and the "caves too safe / mobs hard to find" feedback, reducing density is the wrong direction.

Do not change the hostile cap amounts. Leave the boss-deny block, phantom, slime, and bat rules as they are too.

If you want caves to actually have MORE mobs (not just deadlier ones), that is a spawn-RATE change, not a cap change, and is tracked as an open question below. In Control! is better used here to PROTECT hunt-target spawns than to throttle them. If a specific hunt mob is ever hard to find, add an `"result": "allow"` rule for it in the relevant biome/dimension rather than touching caps.

### 5D. Apotheosis — more frequent elite invaders

File: `config/apotheosis/apotheosis.cfg`, section `bosses`

```
Boss Spawn Cooldown = 3600   ->  2400
```

Time in ticks between natural affix-boss spawns per dimension (3600 = 3 min, 2400 = 2 min). Lower it for more frequent hard, varied elite encounters in caves and on the surface. Leave `Boss Glowing On Spawn` and `Boss Announcement Range` so they stay readable.

### 5E. Hybrid Aquatic — control density (after first launch)

File: `config/hybrid-aquatic.json` (generated on first run). Per-species on/off booleans plus worldgen and loot toggles, no numeric weight sliders. If the ocean feels crowded, disable individual species. For finer control, override biome spawn entries via KubeJS (already in pack).

## 6. Decision needed: baseline mob difficulty (now load-bearing)

Verified: Apotheosis 8.5.4 makes occasional invading bosses harder but does NOT raise the baseline of ordinary mobs. Since we are no longer cutting density, the way to make caves dangerous and hunts meaningful is to make ordinary mobs hit harder. Pick one:

- Option A (recommended): Silent's Power Scale. Verified on 1.21.1 NeoForge. Scales mob power up with progression and distance from spawn, so caves and far-flung areas get genuinely dangerous on an RPG curve, without adding entities. Best fit for "caves should be scary" plus "fewer-but-harder" without hurting findability or lag.
- Option B: DarkMobs at half strength via its Easy Mode datapack. Flat stat buff to all mobs, server-side, cheap. Tune to about half so it does not compound on Apotheosis spikes. Uniform rather than curved.
- Option C: do nothing extra. Vanilla Hard plus more frequent Apotheosis elites. Caves get periodic danger but ordinary mobs stay vanilla-tough.

Recommendation: Option A. It is the cleanest solution to the exact complaint (caves not dangerous) and complements, rather than fights, the dense hunt pool.

## 7. Open question: do caves need MORE mobs, or just DEADLIER ones?

The feedback had two parts: hard to find hunt mobs, and caves not dangerous. Difficulty (Section 6) solves "not dangerous." If "hard to find" is still a problem after that, the fix is raising spawn RATE for the relevant mobs, which is separate work:

- For specific hunt-target mobs: add In Control! `allow`/boost rules, or raise their spawn weight via KubeJS/datapack, so they reliably appear where the quest sends players (the grove, specific biomes).
- For general cave density: investigate cave-spawn rates and lighting; vanilla 1.18+ cave spawning plus modpack light sources often makes caves sparse. This may want a dedicated spawn-rate pass.

Flagging this rather than guessing. Tell me if hunt-mob findability is still an active pain and I will scope a spawn-rate pass for the specific quest targets.

## 8. Execution order

1. Back up the world save and the `config/` folder.
2. Add jars: Hybrid Aquatic (+ Curios if missing), Create: Aquatic Ambitions, Critters & Companions, Creatures & Beasts: Continued, Mobs of Mythology 2.2.2, optional Boids. Plus the Section 6 pick.
3. Remove `ftboceanmobs-21.1.4.jar`.
4. Apply config edits 5A, 5B, 5D. Leave 5C unchanged. (5E after first launch.)
5. Launch a fresh test world. Confirm no missing-dependency or registry crash.
6. Apply 5E (Hybrid Aquatic species prune) once its config exists.
7. Run the grove-hunt quests in a test save to confirm `dread_hound`, `corpse_fly`, `mr_pumpkin`, bonescallers, and the other targets still spawn and the quests complete.
8. Spark profile at night and explore an ocean to confirm behavior.

## 9. Verification checklist

- [ ] Game loads with all new jars, no crash, no red errors.
- [ ] FTB Ocean Mobs gone, nothing references it (already confirmed inert).
- [ ] Born in Chaos: the 10 filler mobs no longer spawn; minibosses, bosses, AND the 3 protected hunt mobs still do.
- [ ] Grove-hunt chain (`what_waits_in_the_grove`) still completable: dread hound, corpse fly, mr pumpkin, bonescallers all findable.
- [ ] Alex's Mobs: catfish no longer accumulating.
- [ ] In Control! caps unchanged; hostiles still plentiful for hunts.
- [ ] Apotheosis affix-boss invasions appearing on the shorter cooldown.
- [ ] Caves feel dangerous after the Section 6 pick is in.
- [ ] Mobs of Mythology creatures spawning in their structures/biomes.
- [ ] Ocean populated but not laggy after the Hybrid Aquatic species prune.

## 10. Notes and sources

- Net entity count rises overall; that is fine since measured lag is chunk generation, not entity tick. The difficulty-first approach avoids adding entity load to make caves dangerous.
- Two diving-gear sets will coexist (NauTec suit, Hybrid Aquatic armor). Cosmetic overlap only.
- NauTec is standalone ocean-magitech (installed), not a Create addon. Pairs with Create: Aquatic Ambitions on different toolkits, no conflict.
- Quest-target verification was done against `config/ftbquests` and `questlog/` directly. 73 FTBQ kill-tasks + 40 questlog hunt-tasks present, so hunt density is a real constraint.

Sources: Hybrid Aquatic, Create: Aquatic Ambitions, Critters & Companions, Creatures & Beasts: Continued, Mobs of Mythology, Boids, In Control!, Silent's Power Scale, DarkMobs (all CurseForge, 1.21.1 NeoForge files verified). Config and quest values read directly from the live files in this instance.
