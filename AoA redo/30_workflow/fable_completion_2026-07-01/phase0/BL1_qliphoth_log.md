# BL1 — Qliphoth additive co-required exams (Chesed IR + Malkuth Gilded)

Stage 1 of the signed-off boss-ladder redesign. ADDITIVE co-required Qliphoth exams:
Chesed becomes a REQUIRED Industrial Revolution boss, Malkuth a REQUIRED Gilded boss.
Obsidilith and Void Titan KEEP their stage grants (unchanged). Geburah untouched (Atomic exam).
No git. Working tree only. Per-file EOL preserved. SkillsLevel never stripped.

Author date: 2026-07-02.

---

## 1. Jar research — fdbosses-3.1.0.3-1.21.1.jar

Method: `unzip -p <jar> ...` on the live jar in `/mods`.

### Fight entry (how each boss is found/summoned)
- **Arenas generate naturally in the Overworld** via structure sets (random_spread):
  - `data/fdbosses/worldgen/structure_set/chesed_arena.json` -> structure `fdbosses:chesed_arena` (spacing 100, sep 50)
  - `data/fdbosses/worldgen/structure_set/malkuth_arena.json` -> structure `fdbosses:malkuth_arena` (spacing 100, sep 80)
- **The "eye" item is an Eye-of-Ender-style LOCATOR** for the arena. Verified by:
  - recipe `data/fdbosses/recipe/eye_of_chesed.json` = 4x `minecraft:sculk` + 1x `minecraft:ender_eye` (plus shape)
  - recipe `data/fdbosses/recipe/eye_of_malkuth.json` = `minecraft:ice` + `minecraft:magma_block` + `minecraft:ender_eye` (shaped)
  - structure-tag files `data/fdbosses/tags/worldgen/structure/eye_of_chesed_located.json` / `eye_of_malkuth_located.json`
  - lang string `fdbosses.word.cant_find_arena` = "Cannot find the structure in this dimension"
  - NOTE: eyes are craftable from cheap vanilla items, so they MUST be AStages-gated or the boss is reachable in Dark Ages. This is why the down-tier (not a new lock) was required — the eyes/entities were already locked to `atomic`.
- **Kill advancements** exist: `data/fdbosses/advancement/qliphoth_awakening/chesed.json` and `malkuth.json`
  (trigger `fdbosses:boss_killed`, boss_entity_type match). Used as the thematic arc; quest proof uses item task.

### Signature drops (verified loot tables — Geburah precedent)
`data/fdbosses/loot_table/entities/` — all single-roll (rolls 1.0), guaranteed:
- `chesed.json`  -> `fdbosses:lightning_core` (+ `phase_sphere`, `chesed_trophy`)
- `malkuth.json` -> `fdbosses:fire_and_ice_core` (+ `malkuth_fist` = "Emberfrost Gauntlet", `malkuth_trophy`)
- `geburah.json` (precedent) -> `fdbosses:justice_core` (+ divine_gear, geburah_trophy, polished_justicestone)

Because each core is a guaranteed drop, **item-task proof is used** (preferred over kill-only per brief),
mirroring the existing Geburah node `4358010000010002` in `at7_chaos_convergence.snbt`
(kill task + item task, grants `geburah_defeated`).

### Verified item/entity/structure IDs used
| id | proof |
|---|---|
| `fdbosses:eye_of_chesed` | recipe json + lang `item.fdbosses.eye_of_chesed` |
| `fdbosses:eye_of_malkuth` | recipe json + lang `item.fdbosses.eye_of_malkuth` |
| `fdbosses:chesed_arena` | `worldgen/structure/chesed_arena.json` + structure_set |
| `fdbosses:malkuth_arena` | `worldgen/structure/malkuth_arena.json` + structure_set |
| `fdbosses:chesed` (entity) | loot_table + advancement + lang `entity.fdbosses.chesed` |
| `fdbosses:malkuth` (entity) | loot_table + advancement + lang `entity.fdbosses.malkuth` |
| `fdbosses:lightning_core` | loot_table chesed.json + lang |
| `fdbosses:fire_and_ice_core` | loot_table malkuth.json + lang |
| `fdbosses:chesed_trophy` / `fdbosses:malkuth_trophy` | lang `block.fdbosses.*_trophy` (icons) |

---

## 2. Quest nodes created (all ids anchored-grep unique across all chapters; 7197 ids parsed, 0 collisions)

### Chesed line — host `ir_netherite_citadel_obsidilith.snbt` (IR boss chapter)
Root: `49540C1000000006` (obsidian_heart / obsidilith proof) — same idiom as at7 Geburah prep
rooting on a sibling proof; adds no new gate because the IR aggregator already requires obsidilith.

| node id | role | task(s) | icon | x,y | reward ids |
|---|---|---|---|---|---|
| `49540C100000002D` | locate: craft Eye of Chesed | item `fdbosses:eye_of_chesed` | eye_of_chesed | 13.0, 0.0 | xp `49540C3000002D00`, loot `49540C3000002D01` |
| `49540C100000002E` | enter arena | structure `fdbosses:chesed_arena` | chesed_trophy | 14.0, -1.5 | xp `49540C3000002E00`, loot `49540C3000002E01` |
| `49540C100000002F` | defeat + proof | kill `fdbosses:chesed` (`49540C2000002F01`) + item `fdbosses:lightning_core` (`49540C2000002F02`) | lightning_core | 13.0, -3.0 | cmd grant `chesed_defeated` `49540C3000002F00`, xp `49540C3000002F01` |

Task ids: `49540C2000002D01`, `49540C2000002E01`, `49540C2000002F01`, `49540C2000002F02`.

### Malkuth line — host `g_power_beyond_wires.snbt` (Gilded boss chapter; hosts void_titan + Gilded aggregator)
Chosen per Q report §3 Gilded table ("g_power_beyond_wires" — the chapter owning the Gilded boss lane
and the Void Titan capstone/aggregator). Root: `5057011000000001` (astral entry) — Gilded-legal, early in chapter.

| node id | role | task(s) | icon | x,y | reward ids |
|---|---|---|---|---|---|
| `505701100000000A` | locate: craft Eye of Malkuth | item `fdbosses:eye_of_malkuth` | eye_of_malkuth | 3.0, -6.0 | xp `50570110300A0000`, random `50570110300A0001` |
| `505701100000000B` | enter arena | structure `fdbosses:malkuth_arena` | malkuth_trophy | 4.5, -6.0 | xp `50570110300B0000`, random `50570110300B0001` |
| `505701100000000C` | defeat + proof | kill `fdbosses:malkuth` (`50570110200C0001`) + item `fdbosses:fire_and_ice_core` (`50570110200C0002`) | fire_and_ice_core | 7.5, -7.5 | cmd grant `malkuth_defeated` `50570110300C0000`, xp `50570110300C0001` |

Task ids: `50570110200A0001`, `50570110200B0001`, `50570110200C0001`, `50570110200C0002`.

Task types used are all proven-in-pack: `item`, `structure`, `kill`. Reward types: `xp`, `loot`, `random`, `command` (all in live use). Shapes `rsquare`/`hexagon` both already in use.

---

## 3. Fan-in wiring (verified aggregator ids on disk first)

Aggregator ids confirmed by grepping their `/astages add` grant commands:
- IR aggregator **`4954631000000000`** defined in `ir_netherite_citadel_obsidilith.snbt:474`, grants `gilded_age`.
- Gilded aggregator **`5057011000000004`** defined in `g_power_beyond_wires.snbt`, grants `atomic`.

Diffs (dependencies only; NO reward block touched, NO new stage grant created):

IR aggregator `4954631000000000` deps:
```
old: ["4954021000000016","49540A100000000F","49540B1000000015","49540C1000000006","4954051000000011","495406100000001D"]
new: [ ...same six... , "49540C100000002F" ]   <- Chesed proof added
```

Gilded aggregator `5057011000000004` deps:
```
old: ["4D50011000000003","5246011000000007","5057011000000003","4D4E011000000006","4D4F011000000005","4F47011000000002","4341011000000004"]
new: [ ...same seven... , "505701100000000C" ]   <- Malkuth proof added
```

Confirmed post-edit: IR aggregator still grants `gilded_age` + `ir_capstone_complete`; Gilded aggregator reward block untouched (still grants `atomic`). Obsidilith node `49540C1000000006` still grants `obsidilith_defeated`; Void Titan node `5057011000000003` still grants `void_titan_defeated`. Both original granters intact per the additive design.

---

## 4. Stage gates / AStages (down-tier, not new locks)

Discovery: all fdbosses eyes + entities were ALREADY locked to `atomic` (Geburah's age). Since Chesed
must be legal at IR and Malkuth at Gilded, this was a **down-tier of existing locks**, not new entries.
No double-locks exist (grep-verified one lock per id), so most-restrictive-wins yields the intended age.

Edits (each `node --check` PASS):
- `aoa_astages_01_item_restrictions.js`: `eye_of_chesed` atomic->`industrial_revolution`; `eye_of_malkuth` atomic->`gilded_age`; `eye_of_geburah` stays `atomic`.
- `aoa_astages_04_mob_restrictions.js`: `fdbosses:chesed` atomic->`industrial_revolution`; `fdbosses:malkuth` + `fire_malkuth_warrior` + `ice_malkuth_warrior` (arena minions) atomic->`gilded_age`; `fdbosses:geburah` stays `atomic`.
- `aoa_astages_08_mob_boss_restrictions.js`: `fdbosses:malkuth` atomic->`gilded_age`; `fdbosses:chesed` atomic->`industrial_revolution` (also removed the pre-existing em dash in Chesed's flavor message); `fdbosses:geburah` stays `atomic`.
- `aoa_astages_00_register_stages.js`: registered new stages `chesed_defeated` (IR proofs block) and `malkuth_defeated` (Gilded proofs block).
- `boss_progression_proof.js`: added `fdbosses:chesed` (proof `lightning_core`) and `fdbosses:malkuth` (proof `fire_and_ice_core`), `guaranteeProofDrop:true`, strip trophy/utility drops on non-player kills — mirrors the Geburah entry so the required fan-in cannot be bypassed by a non-player kill.

`node --check` PASS lines:
```
PASS aoa_astages_00_register_stages.js
PASS aoa_astages_01_item_restrictions.js
PASS aoa_astages_04_mob_restrictions.js
PASS aoa_astages_08_mob_boss_restrictions.js
PASS boss_progression_proof.js
```

No new dimension gate needed: both arenas are Overworld structures.

---

## 5. Lang stubs (appended to `config/ftbquests/quests/lang/en_us.snbt`, bare-LF preserved)

18 keys added (6 nodes x title/quest_subtitle/quest_desc). Titles/subtitles = `[STUB] ...`;
descs = `["[BRIEF] ..."]` array form with the teaching brief + recipe/mechanic facts for Opus.
Covers: eye recipes, arena-locator behavior, the crystal/reflector (Chesed) and cannon/fire-ice-weakness
(Malkuth) combat mechanics, the guaranteed core drops, the stage grant + which aggregator each feeds.

---

## 6. Verification outputs

- **tier_audit.py**: `SOFTLOCK 0`, `ILLEGAL 0`. (Chesed@IR / Malkuth@Gilded legal; no new cross-age inversion.)
- **ef_audit.py**: `TOTAL quest ids 1935` (+6 nodes vs 1929 baseline); `DUP ids {}`; `DANGLING dep sources 0 / total dangling edges 0` (both new fan-ins resolve); `MISSING quest_desc 57` (returned to baseline — all 6 new nodes have lang); `EM DASH 0`, `EN DASH 0`; `BACKWARD-age deps 0`; `ORPHANS 1` (pre-existing, unchanged).
- **Brace/bracket balance**: ir chapter 421/421 braces, 195/195 brackets; g chapter 456/456 braces, 197/197 brackets; lang 1/1 braces, 1954/1954 brackets. All balanced.
- **EOL purity**: ir chapter + g chapter pure CRLF (0 bare LF); lang pure LF (0 CRLF). Preserved.
- **SkillsLevel**: intact in every new task (IR chapter now 58 SkillsLevel blocks = 52 old + 6 new). None stripped.
- **Em dashes**: 0 across all edited files (also removed one pre-existing em dash in the AStages 08 Chesed message).

### Manual crossing check (dependency lines must not cross)
Computed every new edge's min distance to every node (existing + new) with a point-to-segment routine.

IR Chesed (all cells free; all edges clear, no node within 0.6u of any edge):
- `49540C1000000006`(11,0) -> `...2D`(13,0)  [horizontal, clear]
- `...2D`(13,0) -> `...2E`(14,-1.5)  [clear]
- `...2E`(14,-1.5) -> `...2F`(13,-3)  [clear]
- `...2F`(13,-3) -> aggregator `4954631000000000`(9.5,-2.5)  [clear; stays below the earthdive/levitation optionals at y-1.5]

Gilded Malkuth (all cells free; all edges clear, no node within 0.65u of any edge):
- `5057011000000001`(0,0) -> `...0A`(3,-6)  [clear; runs through open lower-left]
- `...0A`(3,-6) -> `...0B`(4.5,-6)  [horizontal, clear]
- `...0B`(4.5,-6) -> `...0C`(7.5,-7.5)  [clear]
- `...0C`(7.5,-7.5) -> aggregator `5057011000000004`(9.5,-8)  [clear; approaches from lower-left, below the void_titan optional cluster]

Both chapters remain crossing-free.

---

## 7. Notes / non-actions
- Live path `config/ftbquests/quests/` edited only. `config/modpack_defaults/...` copies are copy-if-absent
  DEFAULTS (not a live sync target) and were intentionally NOT edited in this stage. `.codex_backups/*`
  are stale and ignored.
- Malkuth `random` rewards chosen to match g_power_beyond_wires' existing reward style (that chapter uses
  xp/random/item, no loot tables). Chesed uses the IR chapter's loot table `8430738502437568515L` to match
  its siblings.
- Strip lists include `chesed_spawn_egg`/`malkuth_spawn_egg` (no such bare ids in the jar — the real ids are
  the warrior spawn eggs); harmless no-ops, and the `_spawn_egg` suffix rule in proof.js catches the real ones.
