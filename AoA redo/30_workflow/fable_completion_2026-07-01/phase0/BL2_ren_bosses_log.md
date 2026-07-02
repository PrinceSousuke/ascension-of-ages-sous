# BL2 — Renaissance required boss ladder (9 dimension/exploration bosses)

Stage 2 of the signed-off boss-ladder redesign. Makes the 9 Renaissance dimension/
exploration bosses REQUIRED (the Q report's Renaissance set MINUS Ender Guardian, Sun
Spirit, and the Deep Aether boss, which move to Otherworldly in stage 3). Additive /
minimal-churn: each boss proof feeds its own dimension chapter's proof-grant quest, which
already fans into the Renaissance age grant `0B0310A0000000F0`.

No git. Working tree only. Per-file EOL preserved (chapters CRLF, lang bare-LF; byte
checks). SkillsLevel never stripped. Crossing-free (per-chapter statements below).

Author date: 2026-07-02.

---

## 1. The 9 required Renaissance bosses (all jar-verified)

| # | boss (entity id) | proof | proof kind | hosting chapter | node ids | promoted / new |
|---|---|---|---|---|---|---|
| 1 | `cataclysm:ignis` | `cataclysm:ignitium_ingot` | item (guaranteed drop) | ren_nether_threshold | `0B03102000000100` (kill+item) | **NEW** |
| 2 | `cataclysm:the_harbinger` | `cataclysm:witherite_block` | item (guaranteed drop) | ren_nether_threshold | `0B03102000000101` (kill+item) | **NEW** |
| 3 | `bosses_of_mass_destruction:gauntlet` | `bosses_of_mass_destruction:blazing_eye` | item (chest reroute) | ren_nether_threshold | `0B03102000000102` (locate arena), `0B03102000000103` (kill+item) | **NEW** |
| 4 | `minecraft:ender_dragon` | kill | kill (vanilla) | ren_end_threshold | `0B03109000000023` (pre-existing kill node) | pre-existing (see §6 gap) |
| 5 | `aether:slider` | `aether:bronze_dungeon_key` | item (existing) | ren_aether_literacy | `0B03103000000031` (existing grant/kill) | existing required |
| 6 | `aether:valkyrie_queen` | `aether:silver_dungeon_key` | item (guaranteed drop) | ren_aether_literacy | `0B03103000000100` (locate silver dungeon), `0B03103000000101` (kill+item, carries moved grant) | **NEW** (moved from ir_side_gear intent) |
| 7 | `eternal_starlight:the_gatekeeper` | kill | kill (empty loot) | ren_starlight_observation | `0B03104000000050` (existing gatekeeper node) | existing required |
| 8 | `eternal_starlight:starlight_golem` | kill | kill (empty loot) | ren_starlight_observation | `0B03104000000073` (existing optional -> promoted); `0B03104000000100` (new proof terminal, carries moved grant) | **PROMOTED** + new terminal |
| 9 | `undergarden:forgotten_guardian` | `undergarden:forgotten_nugget` | item (guaranteed drop) | ren_undergarden_descent | `0B03105000000041` (existing optional -> promoted); `0B03105000000100` (new proof terminal, carries moved grant) | **PROMOTED** + new terminal |

Plus `cataclysm:maledictus` remains the Renaissance CAPSTONE (`0B0310A000000014`, grants
`ren_maledictus_defeated` + `ren_maledictus_vigil_complete`); untouched, already required.

Removed from Renaissance scope per sign-off (move to OW in stage 3, NOT quested here):
`cataclysm:ender_guardian`, `aether:sun_spirit`, `deep_aether:eots_controller`.

---

## 2. Jar proofs (unzip on live /mods)

Method: `unzip -p <jar> data/<modid>/loot_table/entities/<name>.json`, entity/item lang
via `assets/<modid>/lang/en_us.json`, structures via `data/<modid>/worldgen/structure*`.

| id | verification |
|---|---|
| `cataclysm:ignis` | entity lang `entity.cataclysm.ignis`; loot `ignis.json` -> `ignitium_ingot` (+ music_disc). Spawns natural (Nether Fortresses). |
| `cataclysm:ignitium_ingot` | `item.cataclysm.ignitium_ingot`; single-roll entity drop. |
| `cataclysm:the_harbinger` | `entity.cataclysm.the_harbinger`; loot `the_harbinger.json` -> `witherite_block`; structure `data/cataclysm/structure/the_harbinger.nbt` (ancient factory pool). |
| `cataclysm:witherite_block` | `block.cataclysm.witherite_block`; single-roll drop. |
| `bosses_of_mass_destruction:gauntlet` | `entity.bosses_of_mass_destruction.gauntlet`; **entity loot table absent** -> proof `blazing_eye` from `loot_table/chests/gauntlet.json` (death-chest). Arena `worldgen/structure/gauntlet_arena.json` + structure_set (natural). |
| `bosses_of_mass_destruction:blazing_eye` | `item.bosses_of_mass_destruction.blazing_eye`; sole roll of chest table. |
| `bosses_of_mass_destruction:gauntlet_arena` | structure_set confirms `bosses_of_mass_destruction:gauntlet_arena`. |
| `aether:valkyrie_queen` | `entity.aether.valkyrie_queen`; loot `valkyrie_queen.json` -> `silver_dungeon_key` (+ golden_sword). |
| `aether:silver_dungeon_key` / `aether:silver_dungeon` | `item.aether.silver_dungeon_key` ("Silver Key"); structure `worldgen/structure/silver_dungeon.json`. |
| `eternal_starlight:starlight_golem` | `entity.eternal_starlight.starlight_golem`; loot table = empty stub (random_sequence only) -> **kill-task proof** (user-approved). |
| `eternal_starlight:the_gatekeeper` | `entity.eternal_starlight.the_gatekeeper`; empty loot -> existing kill-task proof. |
| `undergarden:forgotten_guardian` | `entity.undergarden.forgotten_guardian`; loot `forgotten_guardian.json` -> `forgotten_nugget` (guaranteed, killed_by_player). |
| `undergarden:forgotten_nugget` / `..._spawn_egg` | `item.undergarden.forgotten_nugget`, `item.undergarden.forgotten_guardian_spawn_egg`. |

`node --check` PASS (all three edited KubeJS scripts):
```
PASS aoa_astages_01_item_restrictions.js
PASS aoa_astages_08_mob_boss_restrictions.js
PASS boss_progression_proof.js
```

---

## 3. Wiring (old -> new) — fan-in invariant preserved

Renaissance age grant = `0B0310A0000000F0` (in `ren_maledictus_vigil.snbt`, grants
`industrial_revolution`). It fans in each chapter's proof-grant node. Each boss proof is
now a (transitive) dependency of its chapter grant, so the boss is required for the age
grant. NO net dependency was added to the age grant (two 1-for-1 swaps only, see below).

Verified: transitive closure of `0B0310A0000000F0` deps now contains ALL of
`ignis / harbinger / gauntlet / slider / valkyrie / gatekeeper / starlight_golem /
forgotten_guardian / maledictus` proof nodes (ender_dragon exception in §6).

### Nether (ren_nether_threshold)
- Boss line rooted on the blaze-burner node `0B03102000000061`:
  `ignis 100 -> harbinger 101 -> gauntlet_locate 102 -> gauntlet_defeat 103`.
- Grant `0B03102000000062` (grants `ren_nether_threshold_complete`) deps:
  `["0B03102000000061"]` -> `["0B03102000000061","0B03102000000103"]` (Gauntlet terminal
  added; chain makes all three Nether bosses required upstream of the grant).

### Aether (ren_aether_literacy)
- The existing grant node `0B03103000000031` IS the slider kill (Bronze Dungeon). Valkyrie
  (Silver Dungeon) is strictly harder/later, so it must come AFTER slider — it cannot be a
  dependency OF the slider node without a backward-difficulty inversion.
- Added `silver_dungeon locate 100 -> valkyrie kill+key 101` after the slider node.
- **Moved** the `ren_aether_literacy_complete` command reward (id `0B03303000000070`) from
  the slider node `0B03103000000031` onto the valkyrie terminal `0B03103000000101`.
- Age-grant fan-in dep **swapped 1-for-1**: `0B03103000000031` -> `0B03103000000101`
  (in `ren_maledictus_vigil.snbt`). Slider stays required transitively (valkyrie deps on
  the silver-locate node, which deps on the slider node). Net age-grant dep count unchanged.

### Starlight (ren_starlight_observation)
- Promoted the existing OPTIONAL `starlight_golem` node `0B03104000000073` (removed
  `optional: true`). It already deps on the gatekeeper grant node `0B03104000000050`.
- Added a proof terminal `0B03104000000100` (item `orb_of_prophecy`) depending on the golem.
- **Moved** the `ren_starlight_observation_complete` command reward (id `0B03304000000050`)
  from `0B03104000000050` onto the terminal `0B03104000000100`.
- Age-grant fan-in dep **swapped 1-for-1**: `0B03104000000050` -> `0B03104000000100`.
  Gatekeeper + golem both required transitively.

### Undergarden (ren_undergarden_descent)
- Promoted the existing OPTIONAL `forgotten_guardian` node `0B03105000000041` (removed
  `optional: true`).
- Added a proof terminal `0B03105000000100` (item `forgotten_nugget`) depending on the
  guardian; placed at (20,5) beside the guardian to keep the edge clean (the far-left grant
  `0B03105000000050` cannot be fed from the right-side guardian without crossing the
  `0B03105000000031 -> 0B03105000000040` barrier).
- **Moved** the `ren_undergarden_descent_complete` command reward (id `0B03305000000060`)
  from the return-to-overworld grant node `0B03105000000050` onto the terminal
  `0B03105000000100`.
- Age-grant fan-in dep **swapped 1-for-1**: `0B03105000000050` -> `0B03105000000100`.
  Guardian required; the guardian's optional side branch (`0B03105000000042` etc.) is
  untouched.

Grant integrity confirmed post-edit: each of the four `ren_*_complete` grant commands now
appears exactly once, on the correct (boss-gated) node. Maledictus capstone untouched.

---

## 4. AStages (down-tier, not new locks)

The Nether/Aether cataclysm+BOMD bosses and the Silver Key were locked LATER than
Renaissance and had to be down-tiered so the required bosses are age-legal. Single lock per
id (grep-verified), so most-restrictive-wins yields the intended age. NO new stages, NO new
dimension gates (all arenas are natural Overworld/Nether/dimension spawns already gated by
the Renaissance dimension gates in `aoa_astages_03_dimension_restrictions.js`).

`aoa_astages_08_mob_boss_restrictions.js`:
- `cataclysm:the_harbinger` gilded_age -> `the_renaissance`
- `cataclysm:ignis` gilded_age -> `the_renaissance` (flame attack-message preserved)
- `bosses_of_mass_destruction:gauntlet` industrial_revolution -> `the_renaissance`
- `aether:valkyrie_queen` industrial_revolution -> `the_renaissance`
- (`undergarden:forgotten_guardian` was already `the_renaissance`; `starlight_golem`/
  `the_gatekeeper` have no mob lock — reachable via the Starlight dimension gate.)

`aoa_astages_01_item_restrictions.js`:
- `aether:silver_dungeon_key` industrial_revolution -> `the_renaissance`
- (proof items `ignitium_ingot`, `witherite_block`, `blazing_eye`, `forgotten_nugget` have
  no item lock — obtained only by killing the boss.)

`boss_progression_proof.js` — added a REQUIRED Renaissance section (mirrors the Geburah /
Obsidilith idiom) so a non-player kill cannot bypass the fan-in:
- guaranteeProofDrop true + strip proof/utility on non-player kill for `cataclysm:ignis`
  (`ignitium_ingot`), `cataclysm:the_harbinger` (`witherite_block`),
  `bosses_of_mass_destruction:gauntlet` (`blazing_eye`), `aether:valkyrie_queen`
  (`silver_dungeon_key`), `undergarden:forgotten_guardian` (`forgotten_nugget`).
- Gauntlet's native `blazing_eye` is a death-chest drop -> added
  `addTableModifier('bosses_of_mass_destruction:chests/gauntlet').removeLoot('...blazing_eye')`
  next to the existing obsidilith reroute, moving it onto the real-player kill path.
- Starlight Golem + Gatekeeper stay kill-task proofs (empty loot tables; user-approved), so
  no LootJS entry is needed for them.

**NEW STAGES CREATED: NONE.** The task said create a `<boss>_defeated` stage only if the Q
report explicitly requires it. It does not: the fan-in here runs entirely through FTBQ
quest dependencies into the existing `ren_<chapter>_complete` proofs, which already fan into
the age grant. No stage registry edit, so **no J2A ripple** (the coordinator does not need
to regenerate J2A for this stage). BL1's `chesed_defeated`/`malkuth_defeated` were needed
because those fed a stage-granting AGGREGATOR; here we feed chapter proofs, which is
sufficient and lower-churn.

---

## 5. Lang stubs (config/ftbquests/quests/lang/en_us.snbt, bare-LF preserved)

24 keys added (8 new nodes x title/quest_subtitle/quest_desc), `[STUB]`/`[BRIEF]` form with
the teaching brief + jar facts for Opus (entity ids, proof drops, kill-vs-item task, the
moved grant, which chapter grant each feeds). New nodes: `0B03102000000100..103` (Nether),
`0B03103000000100/101` (Aether), `0B03104000000100` (Starlight terminal),
`0B03105000000100` (Undergarden terminal). Verified: none of the 8 appear in ef_audit's
MISSING quest_desc list.

Opus follow-up flagged in the Starlight terminal brief: the promoted golem node
`0B03104000000073` still reads "optional construct boss / not a required chapter gate" —
now FALSE; re-prose it.

---

## 6. Verification outputs

- **tier_audit.py**: `=== SOFTLOCK + ILLEGAL rows ===` **EMPTY** (0 SOFTLOCK, 0 ILLEGAL).
  Down-tiered bosses are now Renaissance-legal; no new cross-age inversion. (CANON rows are
  pre-existing metallurgy / MI family-floor advisories, unrelated.)
- **ef_audit.py**: `DUP ids {}`; `EM DASH 0` / `EN DASH 0`; `DANGLING dep sources 0 / total
  dangling edges 0`; `BACKWARD-age deps 0`; `ORPHANS 1` (pre-existing
  `stone_water_weather_and_wounds:3400000000009000`, not ours); `MISSING quest_desc 59`
  (none in ren_ chapters; all 8 new nodes have desc); total quest ids 1945.
- **node --check**: PASS on all three edited KubeJS scripts (see §2).
- **Brace/bracket balance**: all five edited chapters braceDelta=0, bracketDelta=0.
- **EOL purity**: five chapters pure CRLF (0 bare LF); lang pure LF (0 CRLF). Preserved.
- **SkillsLevel**: intact in every new task; no block stripped.
- **Duplicate ids**: 0 cross-file dup quest ids (7227 -> +8 new, all unique; anchored grep).
- **Global dep resolution**: 0 unresolved dependencies across all five edited chapters.
- **Fan-in trace**: all 9 boss proof nodes (+maledictus) are in the transitive dependency
  closure of the Renaissance age grant `0B0310A0000000F0`.

### Crossing statements (per chapter — only new/modified edges checked against ALL edges)
- **ren_nether_threshold**: boss chain `061->100->101->102->103` + `103->062(grant)` placed
  in the open upper-left band (y=0..1.5) feeding the grant from directly above. 0 crossings.
- **ren_aether_literacy**: `031->100->101` + age-grant edge to `101`. 0 crossings.
- **ren_starlight_observation**: `073->100`. 0 crossings.
- **ren_undergarden_descent**: `041->100`; guardian promoted in place, optional side branch
  untouched. 0 crossings. (Direct grant->guardian was abandoned because it crossed the
  `031->040` barrier; the age-grant-swap-to-terminal pattern is crossing-free instead.)

---

## 7. Known gap / non-action (flag, not silently shipped)

- **`minecraft:ender_dragon` (`0B03109000000023`) is NOT actually wired as required.** It is
  a LEAF side-node in `ren_end_threshold.snbt` (shares parent `0B03109000000022` with the
  grant chain but nothing depends on it). The Q report listed it as "existing required," but
  the live wiring shows it is a dead end, so it was already outside the 8 nodes authored
  here. Wiring it into the End grant crossing-free is a non-trivial rewire of a dense chapter
  (every candidate edge `023 -> 080`/`023 -> 060` crosses existing nodes/edges). Left as-is
  rather than shipping an unclean crossing. **Recommend a follow-up layout pass** for the End
  chapter to route the dragon into `ren_end_threshold_complete` (or a coordinator call on
  whether the End dimension-clear proof already implies the dragon).

## 8. Notes
- Live path `config/ftbquests/quests/` edited only; `config/modpack_defaults/...` copies are
  copy-if-absent defaults, intentionally NOT touched.
- Reward types used: `xp`, `command` (existing in live use). Task types: `kill`, `item`,
  `structure` (all proven-in-pack). Shapes `diamond`/`hexagon` already in use.
- Files touched: 5 chapters (ren_nether_threshold, ren_aether_literacy,
  ren_starlight_observation, ren_undergarden_descent, ren_maledictus_vigil), lang en_us.snbt,
  and 3 KubeJS (aoa_astages_01, aoa_astages_08, boss_progression_proof).
