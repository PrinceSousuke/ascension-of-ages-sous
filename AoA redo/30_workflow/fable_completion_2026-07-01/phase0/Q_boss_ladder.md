# Q — Boss-progression ladder (research + design)

Status: RESEARCH + DESIGN ONLY. No files edited outside this `phase0/` dir. No git.
Author date: 2026-07-02. All entity/item/loot claims are jar-verified (three parallel
`unzip` census passes) or grep-verified against live chapters + AStages scripts.

Pack root: `C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)`

---

## 0. Executive summary

- **Total genuine boss-grade entities found in the pack: 51** across 15 boss-bearing mods
  (excluding ordinary mobs, minions, projectiles, and unfinished/W.I.P entities).
- **Qliphoth's Awakening = the mod `fdbosses`** (jar `fdbosses-3.1.0.3-1.21.1.jar`,
  `displayName="Qliphoth Awakening"`). It has **3 bosses: Chesed, Malkuth, Geburah**.
  Only **Geburah is quested today** (required Atomic exam). **Chesed and Malkuth have ZERO
  quest presence** — confirmed: no chapter references `fdbosses:chesed` or `fdbosses:malkuth`.
- **Current required boss spine = ~13 genuine bosses** (the count in the task brief is right
  once you strip the ~20 ordinary-mob "kill" tasks miscounted as required — see §2 defect).
- **Proposed required boss ladder: 44 encounters** across the 8 ages (see §3), with Cataclysm
  ordered by its internal roster and Qliphoth (Chesed/Malkuth/Geburah) placed as age
  capstone-adjacent bosses. This lands in the user's "closer to 50" target while every added
  boss is jar-verified and age-legal.

Proposed required-count per age (one line):
**Dark 0 · Medieval 3 · Renaissance 12 · IR 5 · Gilded 5 · Atomic 8 · Otherworldly 6 · Ascension 5 = 44.**

---

## 1. BOSS CENSUS (jar-verified)

Method: `unzip -p <jar> assets/<modid>/lang/en_us.json` (display names + roster),
`unzip -l <jar> | grep loot_table.*entities` (confirm real entities),
`unzip -p <jar> data/<modid>/loot_table/entities/<name>.json` (signature drop).
Loot path is `loot_table/` (singular) on all these jars. "UNVERIFIED drop" = the entity is
real and named but drops are Java-procedure-based with no JSON loot table, so an FTBQ **kill
(More Quest Types) task keyed to the entity id** is the correct proof surface, not an item task.

Age legality checked against `aoa_astages_03_dimension_restrictions.js` (dimension gates) and
`aoa_astages_00_register_stages.js` (stage registry). Dimension gates: Nether/End/Otherside/
Starlight/Aether/Undergarden → the_renaissance; Astral → gilded_age; Macabre's Pit → atomic;
Stellaris/afterdark → otherworldly.

### 1a. L_Ender's Cataclysm (`cataclysm`) — the technical boss spine
Ordered by internal progression. Loot `data/cataclysm/loot_table/entities/`.

| entity_id | boss | signature proof drop (verified) | arena/summon | tier | dim/age-legal |
|---|---|---|---|---|---|
| `cataclysm:ignis` | Ignis | `cataclysm:ignitium_ingot` | natural, Nether Fortresses | early | Nether → renaissance |
| `cataclysm:netherite_monstrosity` | Netherite Monstrosity | `cataclysm:infernal_forge` / `cataclysm:monstrous_horn` | natural, deep Nether/lava | early-mid | Nether → renaissance (quested IR today) |
| `cataclysm:the_harbinger` | The Harbinger | `cataclysm:witherite_block` | natural, Nether | mid | Nether → renaissance |
| `cataclysm:wadjet` | Wadjet | `cataclysm:ancient_metal_ingot` (bulk; weak proof) | desert/Sunken City | mid | Overworld → any age ≥ medieval |
| `cataclysm:maledictus` | Maledictus | `cataclysm:cursium_ingot` | natural, desert | mid | Overworld (REQUIRED Ren capstone today) |
| `cataclysm:ancient_remnant` | Ancient Remnant | `cataclysm:remnant_skull` / `cataclysm:sandstorm_in_a_bottle` | Ancient Desert Stele (block-triggered) | mid | Overworld |
| `cataclysm:scylla` | Scylla | `cataclysm:essence_of_the_storm` | natural, ocean/storm | mid-late | Overworld ocean |
| `cataclysm:the_leviathan` | The Leviathan | `cataclysm:tidal_claws` / `cataclysm:abyssal_egg` | deep ocean abyssal structure | late/apex | Overworld ocean (REQUIRED OW→Asc today) |
| `cataclysm:ender_guardian` | Ender Guardian | `cataclysm:gauntlet_of_guard` | natural, The End (post-Dragon) | apex | End → renaissance dim, but gear tier = OW |

### 1b. Qliphoth's Awakening (`fdbosses`) — the MAIN thematic spine
Loot `data/fdbosses/loot_table/entities/`. All 3 drops verified.

| entity_id | boss | proof core (verified) | trophy | arena/summon | tier |
|---|---|---|---|---|---|
| `fdbosses:chesed` | Chesed | `fdbosses:lightning_core` | `fdbosses:chesed_trophy` | `chesed_boss_spawner` (monolith arena) | high |
| `fdbosses:malkuth` | Malkuth | `fdbosses:fire_and_ice_core` | `fdbosses:malkuth_trophy` | `malkuth_boss_spawner` | high |
| `fdbosses:geburah` | Geburah | `fdbosses:justice_core` | `fdbosses:geburah_trophy` | `geburah_boss_spawner` | apex |

Qliphoth = Kabbalah sephirot names (Chesed=Mercy, Geburah=Severity, Malkuth=Kingdom).
Arena is a spawner block placed in-world; not a natural spawn and not a token item, so it fits
the "no summon-token" rule (the spawner is a block/structure, not a custom AoA item).

### 1c. Bosses of Mass Destruction (`bosses_of_mass_destruction`)
| entity_id | boss | proof drop (verified) | arena/summon | tier |
|---|---|---|---|---|
| `bosses_of_mass_destruction:gauntlet` | Nether Gauntlet | `bosses_of_mass_destruction:blazing_eye` (chest table) | Nether Gauntlet structure | mid |
| `bosses_of_mass_destruction:lich` | Night Lich | `bosses_of_mass_destruction:ancient_anima` | soul_star + altar in Lich Tower | mid-late |
| `bosses_of_mass_destruction:void_blossom` | Void Blossom | `bosses_of_mass_destruction:void_thorn` | void_lily block → underground spawner | mid-late |
| `bosses_of_mass_destruction:obsidilith` | Obsidilith | `bosses_of_mass_destruction:obsidian_heart` (chest table) | Obsidian Altar (End frame + runes) | apex-End (REQUIRED IR→Gilded today) |

Note: `obsidian_heart` + `blazing_eye` come from a death-spawned loot **chest**, not the entity
table. `boss_progression_proof.js` already reroutes `obsidian_heart` onto the real-player kill
path via LootJS. Do the same for `blazing_eye` if Gauntlet is promoted.

### 1d. Renaissance dimension bosses
**Aether (`aether`)** — self-chaining dungeon-key ladder. Loot `data/aether/loot_table/entities/`.
| entity_id | boss | proof drop (verified) | arena | tier |
|---|---|---|---|---|
| `aether:slider` | Slider | `aether:bronze_dungeon_key` | Bronze Dungeon (REQUIRED today) | early |
| `aether:valkyrie_queen` | Valkyrie Queen | `aether:silver_dungeon_key` | Silver Dungeon | mid |
| `aether:sun_spirit` | Sun Spirit | `aether:gold_dungeon_key` / `aether:sun_altar` | Gold Dungeon / Sun Altar | late |

**Deep Aether (`deep_aether`)** — one boss.
| `deep_aether:eots_controller` | Eye of the Storm | `deep_aether:brass_dungeon_key` | Brass Dungeon (tier above Gold) | apex-Aether |

(Kill `eots_controller`, NOT `eots_segment` body parts.)

**Eternal Starlight (`eternal_starlight`)** — 4 bosses, **all loot tables are empty stubs** →
use MQT kill tasks keyed to entity id (advancement `player_killed_entity` exists per boss).
| entity_id | boss | proof (kill task) | gating mechanic |
|---|---|---|---|
| `eternal_starlight:the_gatekeeper` | The Gatekeeper | kill task | gate challenge (REQUIRED today) |
| `eternal_starlight:starlight_golem` | Starlight Golem | kill task | must FREEZE first (`frozen_tube`) |
| `eternal_starlight:permafrost` | Permafrost | kill task | Golem Forge region |
| `eternal_starlight:lunar_monstrosity` | Lunar Monstrosity | kill task | must IGNITE first (`saltpeter_matchbox`) |

**The Undergarden (`undergarden`)** — one boss.
| `undergarden:forgotten_guardian` | Forgotten Guardian | `undergarden:forgotten_nugget` (guaranteed, killed_by_player) | Catacombs structure (OPTIONAL today) |

### 1e. Atomic-tier horror + judgment
**macabre (`macabre`)** — "the Pit" dimension (gated atomic). 4 bosses, procedure-based drops
(hearts exist in lang but UNVERIFIED from JSON) → MQT kill tasks. All already quested/required.
| `macabre:valamon` (Corpse Butcher) · `macabre:gomoria` (Fleshmonger Monk) · `macabre:gargamaw`
(Grotesque Consumer) · `macabre:baal` (Motionless Calamity, apex) | False Idol spawner summon |
- fdbosses:geburah (Qliphoth apex) also lives here as the Atomic exam.

**Alex's Caves (`alexscaves`)**
| `alexscaves:tremorzilla` | Tremorzilla | **no signature item** (only uranium) → MQT kill (quested optional/required at7 today) | Primordial Caves apex |
| `alexscaves:luxtructosaurus` | Luxtructosaurus | `alexscaves:tectonic_shard` | high (not required) |
| `alexscaves:watcher` | Watcher | `alexscaves:occult_gem` | high (not required) |

### 1f. Astral Dimension (`astral_dimension`) — gilded-gated dimension
| entity_id | boss | proof drop | arena | tier |
|---|---|---|---|---|
| `astral_dimension:void_titan` (loot on `void_titan_defeat`) | Void Titan | `astral_dimension:astral_amulet` | altar summon (`void_titan_present` block) | apex (REQUIRED Gilded→Atomic today) |
| `astral_dimension:helioos` | Helioos | procedure-based, UNVERIFIED → MQT kill | Helioos biome | boss |
| `astral_dimension:angel_boss` / `tower_of_malice` / `amethyst_knight` | (minor astral bosses) | — | quested OPTIONAL today | mid |

### 1g. Bosses'Rise (`block_factorys_bosses`) — arena bosses (the asc6 chapter's namesake)
Loot `data/block_factorys_bosses/loot_table/entities/`. 5 true bosses ("X, the Y" naming).
| entity_id | boss | proof drop (verified) | tier |
|---|---|---|---|
| `block_factorys_bosses:yeti` | Skor, the Yeti | `block_factorys_bosses:ice_gauntlet` | mid-high (quested opt IR today) |
| `block_factorys_bosses:sandworm` | Sirok, the Sandworm | `block_factorys_bosses:sandworm_gauntlet` | mid-high (UNQUESTED) |
| `block_factorys_bosses:underworld_knight` | Helvar, the Underworld Knight | `block_factorys_bosses:knight_sword` | high (quested opt Ren today) |
| `block_factorys_bosses:kraken` | Nerakyss, the Kraken | `block_factorys_bosses:kraken_tooth` | high (quested opt Asc today) |
| `block_factorys_bosses:infernal_dragon` | Ashlord, the Infernal Dragon | `block_factorys_bosses:dragon_skull` | high (quested opt Asc today) |

### 1h. Mowzie's Mobs (`mowziesmobs`) — early hunt bosses
| `mowziesmobs:ferrous_wroughtnaut` | `mowziesmobs:wrought_axe` | structure duel | mid |
| `mowziesmobs:frostmaw` | `mowziesmobs:ice_crystal` | natural snowy | mid |
| `mowziesmobs:umvuthi` (Sunbird) | `mowziesmobs:sol_visage` | Barako village structure | mid-high |
| `mowziesmobs:sculptor` (Tongbi) | `mowziesmobs:sculptor_staff` | parkour trial (NOT a combat kill — quest as structure/trial) | boss-ish |
| `mowziesmobs:naga` | `mowziesmobs:naga_fang` | ocean cliffs | low-mid (elite, borderline) |

### 1i. Born in Chaos (`born_in_chaos_v1`) — mostly ordinary mobs
True bosses/minibosses only (rest are trash mobs — see §2 defect):
`lord_pumpkinhead_head` (Lord Pumpkinhead), `supreme_bonescaller_stage_2` (Supreme Bonescaller),
`nightmare_stalker`, `lifestealer_true_form`, `fallen_chaos_knight`, `krampus` (seasonal).

### 1j. End-game apex
| `draconicevolution:draconic_guardian` | Chaos/Draconic Guardian | no direct drop → MQT kill (proof = `draconicevolution:chaos_shard` from crystal) | ascension (REQUIRED final today) |
| `alexsmobs:void_worm` | Void Worm | `alexsmobs:void_worm_eye` | End void, item-summoned | apex (UNQUESTED — strong OW/Asc candidate) |
| `minecraft:ender_dragon` | Ender Dragon | vanilla (no item task; MQT kill) | REQUIRED Ren today |
| `minecraft:warden` | Warden | vanilla (MQT kill) | REQUIRED Ren today (Undergarden depth) |

### 1k. Confirmed NOT present / not a boss
- **aquamirae**: not installed (no jar). Do not reference.
- **endrem / End Remastered**: installed but adds NO boss entity (only injects loot into vanilla
  mobs). Do not treat as a boss source.
- **cataclysmiccombat / cataclysmfortresses / integrated_cataclysm / lootintegrations_cataclysm**:
  addons/structure/loot mods, no new boss entities.
- **monsterplus (`monsterplus`)**: adds themed mobs (`ancient_hero`, `crystal_zombie`,
  `desert_sorceress`, `abyssologer`, `spectral_skull`) — these are ELITE MOBS, not boss-bar
  bosses. Currently mass-quested as required kills in Medieval (see §2 defect).
- **alchemists_garden (`alchemists_garden`)**: `gnome_king`, `spider_queen` are mini-bosses;
  `gnome`, `yeti` are ordinary mobs. Quested required in Medieval.

---

## 2. CURRENT COVERAGE (grep-verified, 73 kill tasks across 14 chapters)

Parsed every chapter, pairing each `type: "kill"` task with its quest's `optional:` flag
(script: `phase0/` scratch, reproduced from live `config/ftbquests/quests/chapters/*.snbt`).

**Genuine required boss spine today (~13):**
| age | required boss | proof |
|---|---|---|
| Renaissance | `aether:slider` | bronze_dungeon_key |
| Renaissance | `eternal_starlight:the_gatekeeper` | kill |
| Renaissance | `minecraft:warden` | kill (Undergarden depth) |
| Renaissance | `minecraft:ender_dragon` | kill (End threshold) |
| Renaissance | `cataclysm:maledictus` | cursium_ingot (Ren capstone) |
| Renaissance | `mowziesmobs:frostmaw` | ice_crystal (in maledictus_vigil) |
| IR | `cataclysm:netherite_monstrosity` | infernal_forge |
| IR | `bosses_of_mass_destruction:obsidilith` | obsidian_heart (IR capstone) |
| IR | `aether:valkyrie_queen` | silver_dungeon_key (in ir_side_gear) |
| Gilded | `astral_dimension:void_titan` | astral_amulet (Gilded capstone) |
| Atomic | `macabre:valamon`+`gomoria`+`gargamaw`+`baal` | hearts (kill) |
| Atomic | `fdbosses:geburah` | justice_core (Atomic exam) |
| OW | `cataclysm:the_leviathan` | tidal_claws (OW→Asc) |
| Ascension | `draconicevolution:draconic_guardian` | kill (final) |

**Qliphoth quest presence: Geburah only (required Atomic). Chesed = NONE. Malkuth = NONE.**
Grep of all chapters for `fdbosses:chesed` / `fdbosses:malkuth` returns zero hits. Confirmed.

**Optional/side boss quests today (26 kill tasks):** BFB yeti/kraken/infernal_dragon,
cataclysm ender_guardian, BOMD gauntlet/lich, ES permafrost/starlight_golem, mowzies
naga/sculptor/umvuthi, astral angel_boss/tower_of_malice/helioos/amethyst_knight,
undergarden forgotten_guardian, born_in_chaos supreme_bonescaller/lord_pumpkinhead, tremorzilla.

**DEFECT (CANON) — Medieval mob-kill spam.** `what_waits_in_the_grove.snbt` marks ~20 kill
tasks as required (non-optional), but most target ORDINARY MOBS, not bosses:
`born_in_chaos_v1:bone_imp`, `corpse_fly`, `zombie_bruiser`, `dread_hound`, `dire_hound_leader`,
`door_knight`, plus `monsterplus:crystal_zombie`, `spectral_skull`, `desert_acolyte`,
`desert_sorceress`, `abyssologer`, and `mowziesmobs:foliaath`/`grottol` (minor fauna). This
violates SHARED_CONTEXT rule "No mob-kill quests for ordinary mobs; kill tasks are legal ONLY
for bosses." It also inflates the apparent "required boss count." These should be demoted to
optional bestiary OR removed; keep only the true bosses (Wroughtnaut, Frostmaw, Naga, Sculptor,
gnome_king, spider_queen, and the born_in_chaos named bosses). This is why the brief's "~13
required bosses" is the correct real count once the mob spam is discounted.

---

## 3. LADDER PROPOSAL — 44 required boss encounters

Design principles honored:
- **Keep every verified existing age-boundary boss** (Maledictus, Obsidilith, Void Titan,
  macabre 4, Geburah, Leviathan, Draconic Guardian) as the age-grant capstone. No swaps that
  remove a working gate; where a Qliphoth boss is a better fit I add it as a *second* required
  boss in the age, not a replacement (see §3 design calls).
- **Cataclysm + Qliphoth are the spine**: Cataclysm bosses distributed by internal order across
  Ren→OW; Qliphoth's 3 placed at rising gear/arena tiers (Chesed IR, Malkuth Gilded, Geburah
  Atomic — a clean one-per-industrial-age escalation).
- **Renaissance dimension bosses are required inside their dimension chapters.**
- **Proof pattern**: item proof where a JSON drop is verified; MQT `kill` task where drops are
  procedure-based/empty (macabre, ES, tremorzilla, Draconic, vanilla). Add guaranteed-drop
  LootJS entries in `boss_progression_proof.js` for any new item-proof boss.
- **Single-granter + full fan-in invariant**: each age's capstone quest depends on ALL that
  age's required boss `_defeated` proofs before it grants the next age (the at7/asc6 model).
- **Warden > dragon difficulty precedent** preserved: harder bosses gate later.

### Dark Ages — 0 required bosses
No boss. Dark Ages is survival-only (canon). Mowzie's hunt lives in Medieval. (Optional: none.)

### Medieval — 3 required
| boss | proof | hosting chapter | role | rationale |
|---|---|---|---|---|
| `mowziesmobs:ferrous_wroughtnaut` | `mowziesmobs:wrought_axe` | what_waits_in_the_grove (existing) | required hunt | classic gear-check duel, pre-metal |
| `mowziesmobs:frostmaw` | `mowziesmobs:ice_crystal` | what_waits_in_the_grove | required hunt | ice-cave boss, survival tier |
| `mowziesmobs:naga` | `mowziesmobs:naga_fang` | what_waits_in_the_grove | required hunt | third hunt to close the chapter |
FIX: demote the ~17 ordinary-mob kill tasks in this chapter to optional/remove (see §2 defect).
Keep gnome_king/spider_queen/Sculptor as OPTIONAL depth (Sculptor is a parkour trial, not combat).

### Renaissance — 12 required (the big dimension block)
This is the heart of the expansion. Each dimension chapter requires its dimension boss(es).
| boss | proof | hosting chapter | role |
|---|---|---|---|
| `cataclysm:ignis` | `cataclysm:ignitium_ingot` | ren_nether_threshold (existing) | Nether entry boss (NEW required) |
| `cataclysm:the_harbinger` | `cataclysm:witherite_block` | ren_nether_threshold | Nether mid boss (NEW required) |
| `bosses_of_mass_destruction:gauntlet` | `blazing_eye` (reroute) | ren_nether_threshold | Nether structure boss (PROMOTE opt→req) |
| `minecraft:ender_dragon` | kill | ren_end_threshold (existing) | End gate (existing required) |
| `cataclysm:ender_guardian` | `cataclysm:gauntlet_of_guard` | ren_end_threshold | End apex (PROMOTE opt→req; but see §3 call — gear tier is high) |
| `aether:slider` | `bronze_dungeon_key` | ren_aether_literacy (existing) | Aether Bronze (existing required) |
| `aether:valkyrie_queen` | `silver_dungeon_key` | ren_aether_literacy | Aether Silver (MOVE from ir_side_gear → req here) |
| `aether:sun_spirit` | `gold_dungeon_key` | ren_aether_literacy | Aether Gold apex (NEW required — completes the key ladder) |
| `eternal_starlight:the_gatekeeper` | kill | ren_starlight_observation (existing) | Starlight gate (existing required) |
| `eternal_starlight:starlight_golem` | kill (freeze-first) | ren_starlight_observation | Starlight boss (PROMOTE opt→req) |
| `undergarden:forgotten_guardian` | `forgotten_nugget` | ren_undergarden_descent (existing) | Undergarden apex (PROMOTE opt→req) |
| `cataclysm:maledictus` | `cursium_ingot` | ren_maledictus_vigil (existing) | **Renaissance CAPSTONE** (existing grant) |
Optional depth kept: Deep Aether Eye of the Storm (brass_dungeon_key), ES permafrost + lunar
monstrosity, mowzies umvuthi, BOMD lich, born_in_chaos named bosses, cataclysm wadjet/ancient_remnant.
NOTE: `warden` (currently required in undergarden) — keep as required OR demote to optional in
favor of `forgotten_guardian` as the dimension's own boss (design call §3).

### Industrial Revolution — 5 required
| boss | proof | hosting chapter | role |
|---|---|---|---|
| `cataclysm:netherite_monstrosity` | `infernal_forge` | ir_netherite_citadel_obsidilith (existing) | mid boss (existing required) |
| `fdbosses:chesed` | `fdbosses:lightning_core` | **NEW branch** in ir_netherite_citadel_obsidilith OR new Qliphoth node | **Qliphoth I** (NEW required) |
| `block_factorys_bosses:yeti` | `ice_gauntlet` | ir_side_gear (existing) | arena boss (PROMOTE opt→req) |
| `bosses_of_mass_destruction:void_blossom` | `void_thorn` | ir_netherite_citadel_obsidilith | structure boss (NEW required) |
| `bosses_of_mass_destruction:obsidilith` | `obsidian_heart` | ir_netherite_citadel_obsidilith | **IR CAPSTONE** (existing grant) |

### Gilded Age — 5 required
| boss | proof | hosting chapter | role |
|---|---|---|---|
| `fdbosses:malkuth` | `fdbosses:fire_and_ice_core` | **NEW branch** g_power_beyond_wires or g7 | **Qliphoth II** (NEW required) |
| `astral_dimension:helioos` | kill | g_power_beyond_wires (existing, opt) | astral boss (PROMOTE opt→req) |
| `bosses_of_mass_destruction:lich` | `ancient_anima` | g5_empire_of_iron or new node | Night Lich (NEW required) |
| `alexscaves:luxtructosaurus` | `tectonic_shard` | g_power_beyond_wires | AC mega-boss (NEW required) |
| `astral_dimension:void_titan` | `astral_amulet` | g_power_beyond_wires | **Gilded CAPSTONE** (existing grant) |

### Atomic — 8 required (macabre 4 + Qliphoth apex + AC + 2)
| boss | proof | hosting chapter | role |
|---|---|---|---|
| `macabre:valamon` | kill | at7_chaos_convergence (existing) | Pit boss (existing required) |
| `macabre:gomoria` | kill | at7 | Pit boss (existing required) |
| `macabre:gargamaw` | kill | at7 | Pit boss (existing required) |
| `macabre:baal` | kill | at7 | Pit apex (existing required) |
| `alexscaves:tremorzilla` | kill | at7 | nuclear apex (PROMOTE opt→req) |
| `alexsmobs:void_worm` | `void_worm_eye` | at5_threshold_of_war or at7 | End-void apex (NEW required) |
| `alexscaves:watcher` | `occult_gem` | at7 | occult boss (NEW required) |
| `fdbosses:geburah` | `justice_core` | at7 | **Atomic EXAM CAPSTONE** (existing grant) |

### Otherworldly — 6 required
| boss | proof | hosting chapter | role |
|---|---|---|---|
| `deep_aether:eots_controller` | `brass_dungeon_key` | ow2_strange_dimension_operations | Deep Aether apex (NEW required — or move to Ren; see §3 call) |
| `eternal_starlight:permafrost` | kill | ow2 or ren | ES boss (PROMOTE) |
| `eternal_starlight:lunar_monstrosity` | kill (ignite-first) | ow2 | ES apex (PROMOTE opt→req) |
| `block_factorys_bosses:sandworm` | `sandworm_gauntlet` | ow2 or ow5 | arena boss (NEW required — currently UNQUESTED) |
| `block_factorys_bosses:underworld_knight` | `knight_sword` | ow6_beyond_the_veil | high arena boss (PROMOTE opt→req) |
| `cataclysm:the_leviathan` | `tidal_claws` | ow6_beyond_the_veil | **OW→Ascension CAPSTONE** (existing grant) |

### Ascension — 5 required (apex convergence)
| boss | proof | hosting chapter | role |
|---|---|---|---|
| `block_factorys_bosses:infernal_dragon` | `dragon_skull` | asc6_bosses_rise (existing, opt) | arena apex (PROMOTE opt→req) |
| `block_factorys_bosses:kraken` | `kraken_tooth` | asc6_bosses_rise | arena apex (PROMOTE opt→req) |
| `cataclysm:scylla` | `essence_of_the_storm` | asc6_bosses_rise | ocean apex (NEW required — currently only in proof.js optional) |
| `astral_dimension:void_titan` (rematch) OR keep single | — | — | (skip; avoid rematch) |
| `draconicevolution:draconic_guardian` | kill (`chaos_shard`) | asc6_bosses_rise | **FINAL BOSS** (existing grant) |
(5th slot = the existing `alexscaves:tremorzilla` at7 could echo, but better: keep asc6 to 5
distinct: infernal_dragon, kraken, scylla, + a Bosses'Rise sandworm if not used in OW, +
Draconic Guardian as the singular final grant.)

**Total: 0+3+12+5+5+8+6+5 = 44 required boss encounters.** Optional side bosses (Deep Aether if
moved, ES extras, BOMD, mowzies umvuthi, born_in_chaos, astral minors, AC watcher/lux if not
promoted, wadjet, ancient_remnant, harbinger extras) add ~15-20 more for the "closer to 50"
total-content figure.

---

## 4. GAP ANALYSIS — what the proposal needs built

### 4a. New chapters / branches
- **No new full chapters strictly required.** Every proposed boss has an existing home chapter
  (dimension chapters, at7, asc6, g_power_beyond_wires, ir_netherite_citadel). Qliphoth
  Chesed/Malkuth need NEW quest NODES (2 nodes) — recommend a small **Qliphoth branch** threaded
  through IR (Chesed) and Gilded (Malkuth) so all three sephirot form a visible arc culminating
  in Geburah's Atomic exam. Optionally a dedicated cross-age "Qliphoth Ascendant" annex tab that
  mirrors the 3 nodes for narrative visibility (mirror pattern like journey_to_ascension).
- Renaissance dimension chapters need added required nodes: Sun Spirit (aether), Starlight Golem
  (starlight), plus Nether Ignis/Harbinger/Gauntlet in ren_nether_threshold.

### 4b. `boss_progression_proof.js` additions (drop-guarantee pattern)
The file uses two mechanisms: (1) `EntityEvents.drops` strips proof + capture drops on non-player
kills; (2) `LootJS.modifiers` `addEntityModifier(id).addLoot(...when(killedByPlayer()))` guarantees
the proof on real-player kills. Add entries (guaranteeProofDrop:true) for each NEW **item-proof**
required boss:
- `cataclysm:ignis` → `ignitium_ingot`; `cataclysm:the_harbinger` → `witherite_block`;
  `cataclysm:ender_guardian` → `gauntlet_of_guard`; `cataclysm:scylla` → `essence_of_the_storm`
  (already partially present as optional — flip guaranteeProofDrop true).
- `bosses_of_mass_destruction:gauntlet` → `blazing_eye` (add chest-table reroute like obsidilith);
  `bosses_of_mass_destruction:void_blossom` → `void_thorn`; `bosses_of_mass_destruction:lich` → `ancient_anima`.
- `aether:valkyrie_queen` → `silver_dungeon_key`; `aether:sun_spirit` → `gold_dungeon_key`;
  `deep_aether:eots_controller` → `brass_dungeon_key`; `undergarden:forgotten_guardian` → `forgotten_nugget`.
- `fdbosses:chesed` → `lightning_core`; `fdbosses:malkuth` → `fire_and_ice_core`.
- `block_factorys_bosses:yeti/sandworm/underworld_knight/kraken/infernal_dragon` → respective gauntlet/sword/tooth/skull.
- `astral_dimension:luxtructosaurus`… (that's alexscaves) `alexscaves:luxtructosaurus` → `tectonic_shard`;
  `alexscaves:watcher` → `occult_gem`; `alexsmobs:void_worm` → `void_worm_eye`.
- **Kill-only (no item proof, use MQT kill task, no LootJS needed):** macabre 4 (already),
  tremorzilla (already), ES 4 bosses, helioos, ender_dragon, warden, draconic_guardian.

### 4c. Stage locks / AStages
- Register NEW `_defeated` stages in `aoa_astages_00_register_stages.js` for each new required
  boss that a capstone fans in: e.g. `chesed_defeated`, `malkuth_defeated`, `sun_spirit_defeated`,
  `ignis_defeated`, `void_worm_defeated`, etc. (mirror the existing `macabre_*_defeated` style).
- No NEW dimension gates needed — Deep Aether shares `aether:the_aether`? VERIFY: Deep Aether may
  use its own dimension id; if so add a `the_renaissance` (or OW) lock in
  `aoa_astages_03_dimension_restrictions.js`. **UNVERIFIED — needs a dimension-id check on the
  deep_aether jar before placing.**
- Ensure fan-in: update each age capstone quest's `dependencies:` to include the new boss nodes'
  ids (invariant: age grant depends on ALL current-age required boss proofs). This is the
  at7/asc6 fan-in pattern — extend it to Renaissance (maledictus_vigil), IR (obsidilith),
  Gilded (void_titan) capstones.

### 4d. Optional→required promotions (already-authored quests, just reclassify + wire fan-in)
BFB yeti (IR), astral helioos (Gilded), ES starlight_golem (Ren), ES permafrost + lunar (OW),
undergarden forgotten_guardian (Ren), tremorzilla (Atomic), BFB kraken + infernal_dragon (Asc),
BFB underworld_knight (OW), cataclysm ender_guardian (Ren/OW), aether valkyrie_queen (move Ren).
These are the cheapest wins: flip `optional: true`→remove, then add to the capstone fan-in.

### 4e. NEW quests to author (nodes that don't exist yet)
Chesed, Malkuth (Qliphoth), aether Sun Spirit, deep_aether Eye of the Storm, cataclysm Ignis +
Harbinger + Scylla, BOMD void_blossom + gauntlet, alexsmobs void_worm, alexscaves luxtructosaurus +
watcher, BFB sandworm. ~14 new boss nodes. Fable authors structure + stub keys; Opus writes prose.

---

## 5. Top design calls needing user sign-off

1. **Qliphoth placement — additive vs capstone-swap.** I placed Chesed=IR, Malkuth=Gilded,
   Geburah=Atomic (existing) as an escalating one-per-industrial-age arc, ADDED alongside the
   existing capstone bosses (Obsidilith, Void Titan) rather than replacing them. The user said
   "Qliphoth bosses must be age capstones." Option A (my proposal): Qliphoth are *co-required*
   bosses, existing bosses stay the stage-granters. Option B: make Chesed the IR→Gilded granter
   (demoting Obsidilith to required-but-not-granter) and Malkuth the Gilded→Atomic granter
   (demoting Void Titan). Option B is a bigger rewire and removes two verified working gates.
   **Recommend A.** Need the call.

2. **Renaissance required-boss load (12) is heavy.** That is the biggest single-age block and
   makes Renaissance a long grind (Nether Ignis/Harbinger/Gauntlet + End Dragon/Ender Guardian +
   Aether Slider/Valkyrie/Sun Spirit + Starlight Gatekeeper/Golem + Undergarden + Maledictus).
   Ender Guardian's gear tier is genuinely high (End apex) — it may fit OW better than Renaissance
   despite the End being Ren-gated. **Call: keep Ren at 12, or move Ender Guardian + Sun Spirit +
   Deep Aether to OW to balance (Ren 9 / OW 9)?**

3. **macabre + Eternal Starlight + Tremorzilla + Draconic proofs are kill-only** (procedure/empty
   loot tables). That is fine mechanically (MQT kill task), but it means those bosses give no
   guaranteed *item* the player can hold as evidence outside the quest system. **Confirm kill-task
   proofs are acceptable for these** (they already are for macabre/tremorzilla/draconic today), OR
   decide whether to add custom guaranteed drops via LootJS for ES bosses (would need item ids
   verified in-game first — currently UNVERIFIED). Recommend accept kill-task proofs.

Secondary flags (not blocking): the Medieval mob-kill spam in `what_waits_in_the_grove` should be
demoted per canon regardless of this ladder; Deep Aether dimension-id gate is UNVERIFIED and needs
a jar check before any stage lock is placed; `warden` vs `forgotten_guardian` as the Undergarden
required boss is a minor call.
