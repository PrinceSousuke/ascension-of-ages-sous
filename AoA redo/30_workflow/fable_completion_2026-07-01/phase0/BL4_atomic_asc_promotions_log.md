# BL4 — Atomic-8 + Ascension-5 final boss promotions

Stage 4 (final) of the signed-off boss-ladder redesign. Closes the two PARTIAL
verdicts from BL3 §7: Atomic 5/8 -> 8/8 and Ascension 1/5 -> 4/4 wired
(draconic_guardian is the untouched finale, so 4 required ancestors + the finale
kill = the Ascension apex set). Additive / minimal-churn (BL2/BL3 idiom).

No git. Working tree only. Per-file EOL preserved (at7 + asc6 pure CRLF; lang pure
LF; Python byte checks below). SkillsLevel never stripped. Crossing-free for all
new edges (statements in §5). The Medieval/grove gate restructure is NOT touched
(parked with the grove rework per task instruction).

Author date: 2026-07-02.

---

## 0. What was missing (BL3 §7 confirmation section)

- **Atomic 5/8**: macabre valamon/gomoria/gargamaw/baal + geburah were REQUIRED.
  `alexscaves:tremorzilla` was OPTIONAL in at7; the "2 more" Atomic bosses the Q
  report §3 named were unwired.
- **Ascension 1/5**: only `draconicevolution:draconic_guardian` (the finale) was
  REQUIRED. `block_factorys_bosses:infernal_dragon` + `kraken` were OPTIONAL and on
  a dangling y=0 string that did NOT feed the finale; `cataclysm:scylla` was absent
  from asc6 (only a Route-5 strip entry in boss_progression_proof.js).

---

## 1. Design call — the Atomic "2 more" bosses (substitution, flagged for coordinator)

The Q report §3 Atomic-8 table named the 2 extra bosses as `alexsmobs:void_worm` +
`alexscaves:watcher`. **`alexsmobs:void_worm` was already consumed by BL3 as the OW
required 9th boss** (ow6 node `42560000EE010000`, feeds the ascension grant). A boss
cannot be a required ancestor of two different age grants without double-counting.

**Decision:** keep `alexscaves:watcher` (unambiguous, Atomic-legal, unclaimed) and
substitute `alexscaves:luxtructosaurus` for void_worm. Luxtructosaurus is the other
Alex's Caves apex boss (Q report §1e / §3 Gilded row / §4b names it), it is
Atomic-reachable (no AStages lock; AC content is Atomic-tier), and it drops a
guaranteed item proof. This yields a clean Atomic-8 = macabre 4 + geburah +
tremorzilla + watcher + luxtructosaurus with no cross-gate conflict. The two AC
bosses form a thematic "Alex's Caves apex" lane rooted on the Geburah exam.
**Coordinator: confirm this substitution is acceptable (void_worm stays OW-only).**

---

## 2. Jar proofs (unzip on live /mods)

| id | verification |
|---|---|
| `alexscaves:watcher` | `entity.alexscaves.watcher` (alexscaves-2.0.10.jar); loot `watcher.json` pool `watcher_gem` -> `alexscaves:occult_gem` (set_count 0-1, so NOT natively guaranteed) + `dark_tatters`. Defeat advancement `defeat_watcher`. |
| `alexscaves:occult_gem` | `item.alexscaves.occult_gem` ("Occult Gem"). |
| `alexscaves:luxtructosaurus` | `entity.alexscaves.luxtructosaurus`; loot `luxtructosaurus.json` -> `alexscaves:tectonic_shard` (set_count 7-11, effectively guaranteed). Defeat advancement `defeat_luxtructosaurus`. Summoned via Amber Monolith. |
| `alexscaves:tectonic_shard` | `item.alexscaves.tectonic_shard` ("Tectonic Shard"). |
| `alexscaves:tremorzilla` | `entity.alexscaves.tremorzilla`; already quested at7 (kill + tremorzilla_egg item task). Kept as-is. |
| spawn eggs | Alex's Caves uses PREFIX form `alexscaves:spawn_egg_watcher` / `alexscaves:spawn_egg_luxtructosaurus` (NOT the `_spawn_egg` suffix), so the auto-`_spawn_egg` strip does NOT catch them — they are listed explicitly in each strip array. |
| `cataclysm:scylla` | `entity.cataclysm.scylla` (L_Ender's Cataclysm 1.21.1-3.31); loot `scylla.json` has a dedicated single-roll pool -> `cataclysm:essence_of_the_storm` (guaranteed). |
| `cataclysm:essence_of_the_storm` | `item.cataclysm.essence_of_the_storm` ("Essence of the Storm"). |
| `block_factorys_bosses:infernal_dragon` | loot `infernal_dragon.json` -> `dragon_skull` (+ dragon_bone). Node already existed (kill task). |
| `block_factorys_bosses:kraken` | loot `kraken.json` -> `kraken_tooth`. Node already existed (kill task). |

`node --check` PASS (only KubeJS file edited):
```
PASS kubejs/server_scripts/boss_progression_proof.js
```

---

## 3. ATOMIC — at7_chaos_convergence.snbt (Atomic 5/8 -> 8/8)

New required "Alex's Caves apex" lane, rooted on the Geburah exam, terminating into
the existing Atomic capstone grant:

```
geburah 4358010000010002  ->  luxtructosaurus 4358010000EE0F02  ->  watcher 4358010000EE0F01  ->  tremorzilla 4358010000010001  ->  atomic grant 4358010000010003
```

Edits:
- **tremorzilla** node `4358010000010001`: removed `optional: true`; dependency
  changed `4358010000010000` -> `4358010000EE0F01` (watcher); coordinate moved
  `(14,-2.5)` -> `(19,-2.5)` (coordinate-only, keeps the new incoming edge out of
  the geburah->grant corridor). Its `tremorzilla_defeated` command reward and its two
  optional child nodes (`...0102`, `...0103`) are untouched.
- **NEW luxtructosaurus** `4358010000EE0F02` at `(15,-2.5)`, dep geburah
  `4358010000010002`. Tasks: kill `alexscaves:luxtructosaurus` (`...EE0F21`) + item
  `alexscaves:tectonic_shard` (`...EE0F22`). Reward: xp 300 (`4358013000EE0F21`).
- **NEW watcher** `4358010000EE0F01` at `(17,-2.5)`, dep luxtructosaurus. Tasks:
  kill `alexscaves:watcher` (`...EE0F11`) + item `alexscaves:occult_gem` (`...EE0F12`).
  Reward: xp 300 (`4358013000EE0F11`).
- **atomic grant** `4358010000010003`: dependency array gained `4358010000010001`
  (tremorzilla), which pulls the whole AC lane into the fan-in.

No stage grant on the two new nodes (see §6). Icons are the proof items
(tectonic_shard, occult_gem) — jar-verified.

---

## 4. ASCENSION — asc6_bosses_rise.snbt (Ascension 1/5 -> 4 required + untouched finale)

Threaded the two BFB arena apex bosses and a new Scylla node INTO the final
convergence's dependency chain:

```
asc5 grant 4448010000010005 -> infernal_dragon 4252010000010009 -> kraken 425201000001000A -> scylla 4252010000EE0001 -> finale 425201000001000B (draconic_guardian, grants convergence)
```

Edits:
- **infernal_dragon** `4252010000010009`: removed `optional: true`; dependency
  re-rooted `4252010000010008` (monsterplus:ancient_hero, an ELITE MOB — must NOT
  become a required prerequisite) -> `4448010000010005` (asc5 grant, cross-chapter,
  no in-chapter edge). Coordinate unchanged `(16,0)`.
- **kraken** `425201000001000A`: removed `optional: true`. Dep (infernal_dragon)
  and coordinate `(18,0)` unchanged.
- **NEW scylla** `4252010000EE0001` at `(19,-2)`, dep kraken. Tasks: kill
  `cataclysm:scylla` (`4252012000EE0001`) + item `cataclysm:essence_of_the_storm`
  (`4252012000EE0002`). Reward xp 300 (`4252013000EE0001`). Shape `rsquare` to match
  the chapter's boss-node style.
- **finale** `425201000001000B` (draconic_guardian): dependency array changed from
  `["4448010000010005"]` to `["4448010000010005", "4252010000EE0001"]`. The finale
  node itself, its two grant rewards (`asc_final_boss_convergence_complete`,
  `draconic_guardian_defeated`), its kill task, shape and coordinate are otherwise
  UNTOUCHED — it stays the singular final exam.

The old optional y=0 string (leviathan -> macabre-4 -> geburah-copy -> tremorzilla-copy
-> ancient_hero) remains optional depth. ancient_hero `...010008`'s downstream link to
infernal_dragon was severed (infernal_dragon re-rooted), so no ordinary-mob kill is a
required prerequisite.

---

## 5. Crossing statements (proper segment-intersection, baseline vs current)

- **at7_chaos_convergence**: baseline 4 crossings -> current **2**. The tremorzilla
  relocation REMOVED the two pre-existing crossings that involved its optional
  children at the old `(14,-2.5)` position; the new AC-lane edges (geburah->lux,
  lux->watcher, watcher->tremorzilla, tremorzilla->grant) add **0** crossings. The 2
  remaining are pre-existing neovitae-chain crossings unrelated to this stage. **Zero
  new crossings.**
- **asc6_bosses_rise**: baseline 0 -> current **0**. The re-rooted infernal_dragon
  edge (cross-chapter, not drawn), kraken->scylla and scylla->finale edges add **0**
  crossings. **Zero new crossings.**

---

## 6. AStages / stages — NO edits, NO new stages, NO J2A ripple

Following the BL3 precedent, the fan-in runs entirely through FTBQ quest
dependencies into the existing age-grant nodes. **No new `_defeated` stage was
registered** (`tremorzilla_defeated` already exists and its grant reward is kept;
watcher/luxtructosaurus/scylla nodes carry only an xp reward, no stage grant). So
**`.aoa_reveal_audit/gen_j2a.py` does NOT need regeneration for BL4** (not edited per
task instruction).

All promoted bosses are already age-legal (verified in
`aoa_astages_08_mob_boss_restrictions.js` + `aoa_astages_01_item_restrictions.js`):
- `alexscaves:watcher`, `alexscaves:luxtructosaurus`, `alexscaves:tremorzilla` — no
  mob lock; AC content is Atomic-tier and reachable in the Atomic chapter.
- `cataclysm:scylla` = `otherworldly` mob lock (line 42) — legal in Ascension.
- `block_factorys_bosses:infernal_dragon` = `atomic` (line 71), `kraken` =
  `otherworldly` (line 73) — both legal in Ascension.
- No down-tier and no new lock required; no cross-age inversion introduced
  (tier_audit 0 SOFTLOCK / 0 ILLEGAL).

### boss_progression_proof.js additions (guaranteed-drop pattern, BL3 idiom)
- **Flipped** `cataclysm:scylla` `guaranteeProofDrop: false -> true` (its
  essence_of_the_storm is a guaranteed single-roll drop; the asc6 node uses an item
  task, so guarantee on real-player kill + strip on non-player kill = un-bypassable).
- **Added** `alexscaves:watcher` (occult_gem) and `alexscaves:luxtructosaurus`
  (tectonic_shard) with `guaranteeProofDrop: true`. Watcher's occult_gem is a 0-1
  roll so the LootJS `addLoot(killedByPlayer)` makes it reliable; luxtructosaurus's
  tectonic_shard is a bulk 7-11 drop (guaranteed either way, normalized for
  consistency). Spawn-egg strip ids use the correct PREFIX form
  (`spawn_egg_watcher`, `spawn_egg_luxtructosaurus`).
- Tremorzilla stays kill-only (no LootJS): its item task is the obtainable
  `tremorzilla_egg` summon item.

---

## 7. Lang stubs (config/ftbquests/quests/lang/en_us.snbt, bare-LF preserved)

9 keys added (3 new nodes x title/quest_subtitle/quest_desc) in `[STUB]`/`[BRIEF]`
form per preamble §5, encoding entity ids, proof drops, kill-vs-item, chapter, prior
node, and which grant each feeds for Opus:
`4358010000EE0F02` (luxtructosaurus), `4358010000EE0F01` (watcher),
`4252010000EE0001` (scylla). Lang 7800 -> 7809 lines, pure LF (0 CRLF).

---

## 8. Verification outputs

- **tier_audit.py**: SOFTLOCK **0**, ILLEGAL **0**. CANON 21 unchanged (pre-existing
  metallurgy IE-family advisories, unrelated). No new cross-age inversion.
- **ef_audit.py**: `DUP ids {}`; `EM DASH 0` / `EN DASH 0`; `DANGLING dep sources 0
  / total dangling edges 0`; `BACKWARD-age deps 0`; `ORPHANS 1` (pre-existing
  `stone_water_weather_and_wounds` orphan, not ours); `MISSING quest_desc 59`
  (back to the BL3 baseline; all 3 new nodes have desc); total quest ids 1955 ->
  1958 (+3).
- **node --check**: PASS on `boss_progression_proof.js` (only KubeJS file edited).
- **Global id uniqueness**: 0 duplicate 16-hex ids across ALL chapters over
  quest+task+reward ids (anchored parse; 7303 distinct / 7303 total). All 12 new ids
  present exactly once.
- **Brace/bracket balance**: at7 braceDelta=0 bracketDelta=0; asc6 braceDelta=0
  bracketDelta=0.
- **EOL purity**: at7 pure CRLF (1523 CRLF, 0 bare LF); asc6 pure CRLF (585 CRLF, 0
  bare LF); lang pure LF (0 CRLF, 7809 LF). Preserved.
- **SkillsLevel**: intact in every task (at7 41/41 SkillsLevel==PlayerSpells; asc6
  13/13). No block stripped; new tasks each carry the inert block.

### Fan-in trace (trace_closure.py)
Atomic grant `4358010000010003` closure — all 8 REQUIRED:
```
alexscaves:tremorzilla       REQUIRED  4358010000010001 (at7, opt=False)
alexscaves:watcher           REQUIRED  4358010000EE0F01 (at7, opt=False)
alexscaves:luxtructosaurus   REQUIRED  4358010000EE0F02 (at7, opt=False)
macabre:baal (+valamon/gomoria/gargamaw) REQUIRED 4646010000010003 (at7, opt=False)
fdbosses:geburah             REQUIRED  4358010000010002 (at7, opt=False)
```
Ascension finale `425201000001000B` closure — 3 required ancestors + finale kill:
```
block_factorys_bosses:infernal_dragon REQUIRED  4252010000010009 (asc6, opt=False)
block_factorys_bosses:kraken          REQUIRED  425201000001000A (asc6, opt=False)
cataclysm:scylla                      REQUIRED  4252010000EE0001 (asc6, opt=False)
draconicevolution:draconic_guardian   = the finale node itself (untouched, grants convergence)
```

---

## 9. Notes / non-actions / follow-ups

- Live path `config/ftbquests/quests/` + `kubejs/server_scripts/` edited only;
  `config/modpack_defaults/...` copies are copy-if-absent defaults, intentionally NOT
  touched.
- **Stale prose flag (Opus follow-up, NOT structural):** the existing lang for
  infernal_dragon `4252010000010009` and kraken `425201000001000A` still reads
  "optional boss-route check" — now inaccurate since both are required. Prose is
  Opus's lane; flagged for the prose pass, not edited here.
- **Coordinator sign-off wanted (§1):** the void_worm -> luxtructosaurus substitution
  for the Atomic 8th boss (void_worm is OW-only per BL3).
- Reward types used: `xp` (proven in live use). Task types: `kill`, `item` (proven).
  Shape `rsquare` (asc6 style) / default (at7). Icons are jar-verified proof items.
- **J2A:** no stage-registry edit, so no gen_j2a regeneration needed.
