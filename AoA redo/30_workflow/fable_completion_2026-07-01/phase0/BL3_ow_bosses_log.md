# BL3 — Otherworldly required boss ladder (9 bosses) + ender_dragon wiring + Med/Atomic/Asc confirmations

Stage 3 (final) of the signed-off boss-ladder redesign. Makes 9 Otherworldly bosses
REQUIRED, wires the leftover BL2 ender_dragon gap, and audits the Medieval / Atomic /
Ascension required-boss claims. Additive / minimal-churn (BL2 idiom): each OW boss proof
node feeds its own OW chapter grant node, which already fans into the OW capstone /
ascension grant `4256010000010006`.

No git. Working tree only. Per-file EOL preserved (4 OW chapters + ren_end_threshold pure
CRLF; lang pure LF; byte checks below). SkillsLevel never stripped. Crossing-free for all
new edges (per-chapter statements in §6).

Author date: 2026-07-02.

---

## 0. The 9 Otherworldly required bosses — count resolution

Signed-off design: "OW carries 9 = the Q report's OW set PLUS the three rebalance moves
from Renaissance." The literal union is:

- Q report §3 OW set (6): `eots_controller`, `permafrost`, `lunar_monstrosity`, `sandworm`,
  `underworld_knight`, `the_leviathan`.
- The 3 Renaissance moves (BL2 §1): `cataclysm:ender_guardian`, `aether:sun_spirit`,
  `deep_aether:eots_controller`.

`eots_controller` appears in BOTH lists, so the naive union is 8 distinct. To land exactly
9 distinct required bosses, the 9th is `alexsmobs:void_worm` — the Q report §1j explicitly
names it a "strong OW/Asc candidate (UNQUESTED)" and §3 Atomic offered it as a lane boss;
it is End-void / item-summoned and OW-tier, so it is the natural additive 9th. This is the
only interpretation that yields a clean 9 without double-counting `eots_controller`. Flagged
for the coordinator in case a different 9th was intended.

| # | boss (entity id) | proof | proof kind | hosting OW chapter | node id | new/promoted |
|---|---|---|---|---|---|---|
| 1 | `cataclysm:the_leviathan` | `cataclysm:tidal_claws` | item (guaranteed) | ow6_beyond_the_veil | `4256010000010004` (pre-existing) | already required (verified, not duplicated) |
| 2 | `aether:sun_spirit` | `aether:gold_dungeon_key` | item (guaranteed) | ow2_strange_dimension_operations | `4C580000EE010000` | NEW |
| 3 | `deep_aether:eots_controller` | `deep_aether:brass_dungeon_key` | item (guaranteed) | ow2_strange_dimension_operations | `4C580000EE020000` | NEW |
| 4 | `cataclysm:ender_guardian` | `cataclysm:gauntlet_of_guard` | item (guaranteed) | ow3_dragon_technology | `44540000EE010000` | NEW (move from Ren) |
| 5 | `block_factorys_bosses:underworld_knight` | `block_factorys_bosses:knight_sword` | item (guaranteed) | ow3_dragon_technology | `44540000EE020000` | NEW |
| 6 | `eternal_starlight:permafrost` | kill | kill-only (empty loot) | ow5_the_digital_cosmos | `44430000EE000000` | NEW |
| 7 | `eternal_starlight:lunar_monstrosity` | kill | kill-only (empty loot) | ow5_the_digital_cosmos | `44430000EE010000` | NEW |
| 8 | `block_factorys_bosses:sandworm` | `block_factorys_bosses:sandworm_gauntlet` | item (guaranteed) | ow6_beyond_the_veil | `42560000EE000000` | NEW |
| 9 | `alexsmobs:void_worm` | `alexsmobs:void_worm_eye` | item (guaranteed) | ow6_beyond_the_veil | `42560000EE010000` | NEW |

Plus two locate/prep nodes (item-light, keep the thin OW spine completable now):
`4C580000EE000000` (aether:the_aether dimension task, feeds Sun Spirit) and
`44540000EE000000` (minecraft:the_end dimension task, feeds Ender Guardian). 10 new nodes total.

No boss already had an OW-chapter optional node to promote (the ir_side_gear ender_guardian
opt node, ren_maledictus_vigil underworld_knight opt node, and g1 sun_spirit/eots
item-gather nodes live in the WRONG age chapters). Per "host in the thematically matching
OW chapter," fresh OW nodes were authored rather than relocating distant nodes and breaking
those chapters' layouts. The stray optional nodes elsewhere are left untouched.

---

## 1. Jar proofs (unzip on live /mods)

| id | verification |
|---|---|
| `aether:sun_spirit` | `entity.aether.sun_spirit`; loot `sun_spirit.json` -> `aether:gold_dungeon_key` (guaranteed single roll) + `sun_altar`. Must be frozen before it takes damage. |
| `aether:gold_dungeon_key` | `item.aether.gold_dungeon_key` ("Gold Key"). |
| `deep_aether:eots_controller` | `entity.deep_aether.eots_controller` ("Eye of the Storm"); loot `eots_controller.json` -> `deep_aether:brass_dungeon_key` (guaranteed single roll). Kill controller, not `eots_segment`. Deep Aether has NO own dimension folder -> it is a sub-region of `aether:the_aether` (dimension gate already Renaissance). |
| `deep_aether:brass_dungeon_key` | `item.deep_aether.brass_dungeon_key` ("Brass Key"). |
| `cataclysm:ender_guardian` | `entity.cataclysm.ender_guardian`; loot `ender_guardian.json` -> `cataclysm:gauntlet_of_guard` (guaranteed single roll). Advancement `cataclysm:kill_ender_guardian`. Spawns natural in the End post-Dragon. |
| `cataclysm:gauntlet_of_guard` | `item.cataclysm.gauntlet_of_guard` ("Gauntlet of Guard"). |
| `block_factorys_bosses:underworld_knight` | `entity.block_factorys_bosses.underworld_knight` ("Helvar"); loot -> `block_factorys_bosses:knight_sword`. Advancement `kill_underworld_knight`. |
| `block_factorys_bosses:sandworm` | `entity.block_factorys_bosses.sandworm` ("Sirok"); loot -> `block_factorys_bosses:sandworm_gauntlet`. Advancement `kill_sandworm`. |
| `eternal_starlight:permafrost` | `entity.eternal_starlight.permafrost`; loot table = empty stub (random_sequence only) -> KILL-ONLY proof. Advancement `kill_permafrost`; Golem Forge region. |
| `eternal_starlight:lunar_monstrosity` | `entity.eternal_starlight.lunar_monstrosity`; loot table empty -> KILL-ONLY proof. Advancement `kill_lunar_monstrosity`; must IGNITE first. |
| `alexsmobs:void_worm` | `entity.alexsmobs.void_worm`; loot pool "eye" -> `alexsmobs:void_worm_eye` (+ `void_worm_mandible`). End-void, item-summoned. |
| `alexsmobs:void_worm_eye` | `item.alexsmobs.void_worm_eye` ("Void Worm Eye"). |
| `cataclysm:the_leviathan` | pre-existing ow6 node; `cataclysm:tidal_claws` (already guaranteed in boss_progression_proof.js). |

`node --check` PASS (only KubeJS script edited):
```
PASS kubejs/server_scripts/boss_progression_proof.js
```

---

## 2. Wiring — fan-in invariant preserved (each boss is a transitive ancestor of the ascension grant)

The OW capstone `4256010000010006` (in ow6, grants `ascension`) fans in each OW chapter's
grant node: ow1 `4C57010000010004`, ow2 `4C58010000010005`, ow3 `4454010000010005`,
ow4 `4C59010000010004`, ow5 `4443010000010006`, plus the Leviathan node `4256010000010004`
and the veil grant `4256010000010005`. Making a boss node a (transitive) dependency of one
of those fan-in nodes makes the boss required for the age grant.

### ow2 (strange dimension operations) — Aether-family boss line
- Chain: `4C580000EE000000` (locate aether:the_aether) -> `4C580000EE010000` (Sun Spirit
  kill + gold_dungeon_key) -> `4C580000EE020000` (Eye of the Storm kill + brass_dungeon_key).
- Grant `4C58010000010005` dep **added**: `["4C58010000010004"]` ->
  `["4C58010000010004", "4C580000EE020000"]`. Both Aether bosses now required upstream of
  the grant.

### ow3 (dragon technology) — End apex + arena knight line
- Chain: `44540000EE000000` (re-enter minecraft:the_end) -> `44540000EE010000` (Ender
  Guardian kill + gauntlet_of_guard) -> `44540000EE020000` (Underworld Knight kill + knight_sword).
- Grant `4454010000010005` dep **added**: `["4454010000010004"]` ->
  `["4454010000010004", "44540000EE020000"]`.

### ow5 (digital cosmos) — Eternal Starlight kill-only line
- Chain: `44430000EE000000` (Permafrost kill) -> `44430000EE010000` (Lunar Monstrosity kill).
- Grant `4443010000010006` dep **added**: `["4443010000010005"]` ->
  `["4443010000010005", "44430000EE010000"]`.

### ow6 (beyond the veil) — apex line
- Chain: `42560000EE000000` (Sandworm kill + gauntlet) -> `42560000EE010000` (Void Worm kill
  + eye). Rooted on the existing Leviathan node `4256010000010004`.
- Capstone `4256010000010006` dep array **added** `"42560000EE010000"` (after the existing
  `"4256010000010005"` line). Void Worm (and via the chain, Sandworm) now required for the
  ascension grant.

Transitive-closure trace of the ascension grant `4256010000010006` after edits confirms all
9 bosses REQUIRED (§6).

---

## 3. Ender Dragon wiring (BL2 §7 leftover gap) — ren_end_threshold.snbt

BL2 left `minecraft:ender_dragon` (`0B03109000000023`) as a non-optional dead-end leaf: it
depended on the End-dimension node `0B03109000000022` but nothing depended on it, so it was
NOT a transitive ancestor of the End grant. The required End spine ran
`...000022 -> 000080 (exotic_eye) -> 000060 (ren_end_threshold_complete grant)`, bypassing
the dragon.

Coordinate-safe fix (threads the dragon INTO the required chain, no new node):
- `0B03109000000080` (exotic_eye) dependency **swapped** `0B03109000000022` ->
  `0B03109000000023` (the dragon). Chain is now
  `...000022 -> 000023 (dragon) -> 000080 -> 000060 (grant)`.
- Dragon node `0B03109000000023` moved (coordinate-only) from `(-5, 1.5)` to `(0, 3.0)` so
  the new outgoing edge routes cleanly under the spine.

Verified: dragon `0B03109000000023` is now in the transitive closure of the
`ren_end_threshold_complete` grant `0B03109000000060` AND of the Renaissance age grant
`0B0310A0000000F0` (grants `industrial_revolution`). The dragon is genuinely required now.

Crossing impact: ren_end_threshold is an inherently dense chapter with **15 pre-existing
edge crossings** (long optional betterend/endrem/unusualend gallery branches sweeping across
the map). The dragon edit is crossing-NEUTRAL: it removed 2 crossings (the old
`000022->000080` edge) and added 2 at the same location (the new `000023->000080` edge),
against the same two pre-existing optional edges (`000060->000097`, `000060->00009F`). Net
15 -> 15, **zero new crossings introduced**. A full crossing-free relayout of the optional
End galleries is out of scope for a required-dep fix; recommend it as a separate End-chapter
layout pass (§7).

---

## 4. AStages — NO edits needed (all 9 bosses already OW-legal)

All 9 OW bosses were already locked at or before `otherworldly`, so no down-tier and no new
lock was required (verified in `aoa_astages_08_mob_boss_restrictions.js` +
`aoa_astages_01_item_restrictions.js`):

- `cataclysm:ender_guardian` = `the_renaissance` (line 30) — legal in OW.
- `aether:sun_spirit` = `gilded_age` (line 77); item `aether:gold_dungeon_key` = `gilded_age`.
- `deep_aether:eots_controller` = `gilded_age` (line 78); item `deep_aether:brass_dungeon_key` = `gilded_age`.
- `block_factorys_bosses:underworld_knight` = `the_renaissance` (line 69).
- `block_factorys_bosses:sandworm` = `the_renaissance` (line 70).
- `eternal_starlight:permafrost` / `lunar_monstrosity` — no mob lock (reachable via the
  Starlight dimension gate, `the_renaissance`).
- `alexsmobs:void_worm` — no lock; End-void, item-summoned. Left unlocked (no age-inversion
  for an OW requirement; adding a lock would be scope creep). Flagged as an optional hygiene
  lock the coordinator may add later.

**NEW STAGES CREATED: NONE.** As in BL2, the fan-in runs entirely through FTBQ quest
dependencies into the existing OW chapter grants, which already fan into the OW capstone /
ascension grant. No `_defeated` stage was registered, so **no register_stages edit and no
J2A ripple** for this stage. (`ender_guardian_defeated` already exists in the registry but is
not awarded by these nodes and is not needed for the fan-in.)

### boss_progression_proof.js additions (guaranteed-drop pattern, BL2/Geburah idiom)
Added a REQUIRED OW section with `guaranteeProofDrop: true` + non-player-kill strip for the
6 item-proof OW bosses: `cataclysm:ender_guardian` (gauntlet_of_guard),
`block_factorys_bosses:underworld_knight` (knight_sword), `aether:sun_spirit`
(gold_dungeon_key), `deep_aether:eots_controller` (brass_dungeon_key),
`block_factorys_bosses:sandworm` (sandworm_gauntlet), `alexsmobs:void_worm` (void_worm_eye).
Each proof is a guaranteed single-roll entity drop, so the LootJS `addEntityModifier` loop
guarantees it on real-player kills and the EntityEvents.drops loop strips it on non-player
kills — the fan-in is not bypassable by a captured/farmed kill.
`eternal_starlight:permafrost` and `lunar_monstrosity` keep their existing Route-5
(`guaranteeProofDrop: false`) entries: empty loot tables mean the MQT kill task IS the proof
(no LootJS possible). `cataclysm:the_leviathan` is already guaranteed above.

---

## 5. Lang stubs (config/ftbquests/quests/lang/en_us.snbt, bare-LF preserved)

30 keys added (10 new nodes x title/quest_subtitle/quest_desc), `[STUB]`/`[BRIEF]` form per
preamble §5 with the teaching brief + jar facts for Opus (entity ids, proof drops, kill-vs-
item, which chapter grant each feeds, freeze/ignite mechanics). New nodes:
`4C580000EE000000/010000/020000` (ow2), `44540000EE000000/010000/020000` (ow3),
`44430000EE000000/010000` (ow5), `42560000EE000000/010000` (ow6). None appear in ef_audit's
MISSING quest_desc list (all 10 have desc).

---

## 6. Verification outputs

- **tier_audit.py**: `=== SOFTLOCK + ILLEGAL rows ===` **EMPTY** (0 SOFTLOCK, 0 ILLEGAL).
  CANON 21 unchanged (pre-existing metallurgy IE-family + MI bronze advisories, unrelated).
  OK 2634 -> 2640 (+6 new item tasks). No new cross-age inversion.
- **ef_audit.py**: `DUP ids {}`; `EM DASH 0` / `EN DASH 0`; `DANGLING dep sources 0 / total
  dangling edges 0`; `BACKWARD-age deps 0`; `ORPHANS 1` (pre-existing
  `stone_water_weather_and_wounds:3400000000009000`, not ours); `MISSING quest_desc 59`
  (unchanged — all 10 new nodes have desc); total quest ids 1945 -> 1955 (+10).
- **node --check**: PASS on `boss_progression_proof.js` (only KubeJS file edited).
- **Global id uniqueness**: 0 duplicate ids across ALL chapters over quest+task+reward+table
  ids (anchored parse; 7256 -> 7291 quest ids, +35 including task/reward). The 40 candidate
  ids were pre-cleared clash-free; 36 emitted, 4 item-task ids reserved-but-unused (kill-only
  / locate-only nodes have no item task).
- **Brace/bracket balance**: all 5 edited chapters braceDelta=0, bracketDelta=0.
- **EOL purity**: 4 OW chapters + ren_end_threshold pure CRLF (0 bare LF); lang pure LF
  (0 CRLF, 7770 -> 7800 lines). Preserved.
- **SkillsLevel**: intact in every new task; no block stripped.
- **Crossing statements (baseline-vs-current, proper segment-intersection check):**
  - **ow2**: 8 edges, **0 crossings**.
  - **ow3**: 8 edges, **0 crossings**.
  - **ow5**: 9 edges, **0 crossings**.
  - **ow6**: 16 edges, **0 crossings** (baseline 0, current 0 — new apex line + capstone dep
    added cleanly in the lower band).
  - **ren_end_threshold**: 15 pre-existing crossings, current 15 — **crossing-neutral**, 0 new
    (dragon edit removed 2 old + added 2 at same location vs the same pre-existing optional edges).

### Fan-in trace (transitive closure of ascension grant 4256010000010006)
All 9 OW bosses REQUIRED (in-closure via a non-optional node):
```
cataclysm:the_leviathan               REQUIRED  4256010000010004 (ow6, opt=False)
aether:sun_spirit                     REQUIRED  4C580000EE010000 (ow2, opt=False)
deep_aether:eots_controller           REQUIRED  4C580000EE020000 (ow2, opt=False)
cataclysm:ender_guardian              REQUIRED  44540000EE010000 (ow3, opt=False)
block_factorys_bosses:underworld_knight REQUIRED 44540000EE020000 (ow3, opt=False)
eternal_starlight:permafrost          REQUIRED  44430000EE000000 (ow5, opt=False)
eternal_starlight:lunar_monstrosity   REQUIRED  44430000EE010000 (ow5, opt=False)
block_factorys_bosses:sandworm        REQUIRED  42560000EE000000 (ow6, opt=False)
alexsmobs:void_worm                   REQUIRED  42560000EE010000 (ow6, opt=False)
minecraft:ender_dragon                REQUIRED  0B03109000000023 (ren_end, opt=False)  [BL2 gap now closed]
```

---

## 7. Med / Atomic / Ascension confirmations (audit + tiny-fix mandate)

Transitive-closure trace against each age's grant node (`trace_closure.py`, in this dir).

| age | required bosses claimed | grant node traced | verdict |
|---|---|---|---|
| Medieval (3) | ferrous_wroughtnaut, frostmaw, naga | `6D7E8F901A2B1054` (grants the_renaissance) | **PARTIAL / follow-up** |
| Atomic (8) | macabre valamon/gomoria/gargamaw/baal + geburah + tremorzilla + (2 more) | `4358010000010003` (grants otherworldly) | **PARTIAL (5/8 confirmed)** |
| Ascension (5) | infernal_dragon, kraken, scylla, sandworm, draconic_guardian | `4153010000010002` (grants aoa_complete) | **PARTIAL (1/5 confirmed)** |

### Medieval — NOT a clean 3-boss gate (follow-up, NOT a simple missing-dep)
The Ren-grant `6D7E8F901A2B1054` uses a 3-of-4 OR gate (`min_required_dependencies: 3`) over
`1050` (wroughtnaut kill), `1051` (foliaath kill), `1052` (frostmaw kill), `1053` (grottol
kill). Two of the four (`foliaath`, `grottol`) are ORDINARY MOBS, not bosses — the exact
Medieval mob-kill defect the Q report §2 flagged. Because it is 3-of-4, neither wroughtnaut
nor frostmaw is strictly forced, and `mowziesmobs:naga` (node `6D7E8F901A2B1013`,
non-optional) is a dangling leaf NOT wired into the grant at all. So the "Medieval 3 required
bosses" claim is **not met**: it is a mixed 3-of-4 real-boss/ordinary-mob gate with naga
unwired. Fixing this properly = restructure the hunt gate to force the 3 real bosses
(wroughtnaut, frostmaw, naga) and demote foliaath/grottol, which exceeds the tiny-fix
mandate. **Follow-up recommended:** rebuild the `...1054` gate to depend on the 3 boss kill
nodes (`1050` wroughtnaut, `1052` frostmaw, and a wired naga kill) with min_required = 3,
demoting foliaath/grottol to optional bestiary.

### Atomic — 5 of 8 confirmed required
Confirmed REQUIRED (in closure, non-optional): `macabre:valamon` (`4646010000010000`),
`macabre:gomoria` (`...0001`), `macabre:gargamaw` (`...0002`), `macabre:baal` (`...0003`),
`fdbosses:geburah` (`4358010000010002`). The macabre-4 + Geburah exam spine is solid.
`alexscaves:tremorzilla` is present but OPTIONAL in both at7 (`4358010000010001`) and asc6
(`4252010000010007`) — NOT in the OW-grant closure. The Q report's proposed 8th boss set
(promote tremorzilla + add void_worm + watcher) was a stage-2 proposal, not wired today.
**Follow-up recommended:** if Atomic-8 is signed off, promote tremorzilla (remove
`optional: true` on the at7 node and add it to the atomic-grant fan-in) and add the 2
remaining Atomic bosses; this is a reclassify + fan-in, larger than a missing-dep.

### Ascension — 1 of 5 confirmed required
Confirmed REQUIRED: `draconicevolution:draconic_guardian` (`425201000001000B`, the final
boss, non-optional, grants `draconic_guardian_defeated` + `asc_final_boss_convergence_complete`).
`block_factorys_bosses:infernal_dragon` and `kraken` are OPTIONAL in asc6; `cataclysm:scylla`
is absent from asc6 (only in proof.js as an optional strip). `block_factorys_bosses:sandworm`
is now OW-required (this stage) — it should NOT also be an Ascension boss. The Q report's
Ascension-5 (promote infernal_dragon + kraken + scylla) was a proposal, not wired today.
**Follow-up recommended:** if Ascension-5 is signed off, promote infernal_dragon + kraken and
author a scylla node in asc6, wiring them into the final convergence — larger than a
missing-dep, so logged rather than done.

---

## 8. Notes / non-actions
- Live path `config/ftbquests/quests/` and `kubejs/server_scripts/` edited only;
  `config/modpack_defaults/...` copies are copy-if-absent defaults, intentionally NOT touched.
- Reward types used: `xp` (existing in live use). Task types: `kill`, `item`, `dimension`
  (all proven-in-pack). Shapes `diamond`/`hexagon` already in use. Icons are verified proof
  items / boss drop items (jar-checked).
- **Coordinator J2A note:** NO stage-registry edit was made (no new `_defeated` stage), so
  `.aoa_reveal_audit/gen_j2a.py` does NOT need regeneration for BL3. (Not edited here per
  task instruction.)
- Files touched: 4 OW chapters (ow2_strange_dimension_operations, ow3_dragon_technology,
  ow5_the_digital_cosmos, ow6_beyond_the_veil), ren_end_threshold, lang en_us.snbt, and 1
  KubeJS (boss_progression_proof.js).
- Follow-ups flagged (not shipped): (1) Medieval hunt-gate rebuild to force 3 real bosses +
  wire naga; (2) Atomic tremorzilla + 2 boss promotions if Atomic-8 confirmed; (3) Ascension
  infernal_dragon/kraken/scylla promotions if Asc-5 confirmed; (4) ren_end_threshold optional-
  gallery crossing cleanup (15 pre-existing crossings); (5) optional `alexsmobs:void_worm`
  AStages OW lock for hygiene.
