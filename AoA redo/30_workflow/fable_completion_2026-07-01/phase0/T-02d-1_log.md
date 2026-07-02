# T-02d-1 log — Neo Vitae blood-orb ladder (g7_chartered_arcana)

**Status:** DONE
**Date:** 2026-07-02
**File touched:** `config/ftbquests/quests/chapters/g7_chartered_arcana.snbt` (+ sidecar
`phase0/stubs/T-02d-1_stubs.txt` + this log). No other file edited. No git.

## Nodes created (4: 3 required + 1 optional)

| node id | task item | type | deps | optional | icon | grid (x,y) | task id | reward id |
|---|---|---|---|---|---|---|---|---|
| `43410110000001A0` | `neovitae:blood_orb_magician` | item | `["0B03101000000034"]` (Ren apprentice-orb node, ren_magic_foundations) | no | `neovitae:blood_orb_magician` | (-8.0, 3.0) | `43410110201A0001` | `43410110301A0000` (xp 200) |
| `43410110000001A1` | `neovitae:blood_orb_master` | item | `["43410110000001A0"]` | no | `neovitae:blood_orb_master` | (-8.0, 5.0) | `43410110201A1001` | `43410110301A1000` (xp 300) |
| `43410110000001A2` | `neovitae:blood_orb_archmage` | item | `["43410110000001A1"]` | no | `neovitae:blood_orb_archmage` | (-8.0, 7.0) | `43410110201A2001` | `43410110301A2000` (xp 400) |
| `43410110000001A3` | `neovitae:rune_2_capacity_augmented` | item | `["43410110000001A1"]` | **yes** | `neovitae:rune_2_capacity_augmented` | (-6.0, 5.0) | `43410110201A3001` | `43410110301A3000` (xp 150) |

Ladder shape: A0 -> A1 -> A2 (linear spine); A1 -> A3 (optional side branch).
No `/astages` reward on any node (spine content, not a gate — per plan §2).
`PlayerSpells` + `SkillsLevel` inert blocks copied verbatim from sibling g7 nodes (not stripped, not hand-typed).

## Re-wires (old -> new)
None. The three orb ids were first-placed here (0 prior tasks anywhere), so no existing quest
re-pointing was needed. No ow6 / g4 / g2 / g5 edits (per plan §3-§7 decisions: sentient tools /
hi-gems stay in ow6, no dupe, no cross-ref dep added).

## Era check (age-tier discipline) — PASS
Chapter age = gilded_age (group `5E42E6B4A7C91D30`). Every task item legal at/before Gilded:
- `neovitae:blood_orb_magician` — `gilded_age` (aoa_astages_01m_magic.js:141) — exact.
- `neovitae:blood_orb_master` — `gilded_age` (:142) — exact.
- `neovitae:blood_orb_archmage` — `gilded_age` (:143) — exact.
- `neovitae:rune_2_capacity_augmented` — no AStages lock anywhere (grep of kubejs/server_scripts
  astages returned nothing); ungated block, family legal. Craftable at Gilded (recipe ingredients
  hellforged_parts=IR :147, netherite_scrap=vanilla, rune_capacity_augmented/rune_capacity=ungated).
Transcendent orb (Atomic) deliberately NOT tasked — ladder ends at archmage.

## Verify-first proofs (all ids proven on disk)
Jar: `mods/neovitae-1.21.1-1.0.25.jar`.
- `unzip -p … assets/neovitae/lang/en_us.json | grep -iE "blood_orb_(magician|master|archmage)|rune_2_capacity_augmented"`:
  - `item.neovitae.blood_orb_magician` = "Veneficus Orb of Vitae"
  - `item.neovitae.blood_orb_master` = "Magus Orb of Vitae"
  - `item.neovitae.blood_orb_archmage` = "Dominus Orb of Vitae"
  - `block.neovitae.rune_2_capacity_augmented` = "Reinforced Augmented Capacity Rune"
- Rune recipe proven craftable: `data/neovitae/recipe/rune_2_capacity_augmented.json` = shaped craft
  (hellforged_parts + netherite_scrap + rune_capacity_augmented + #minecraft:stone_crafting_materials).
- Dep node `0B03101000000034` verified in `ren_magic_foundations.snbt:765` tasking
  `neovitae:blood_orb_apprentice` (correct Ren apprentice-orb node).
- Softlock guard: `kubejs/data/neovitae/tags/block/altar/pillars.json` still non-empty
  (bloodstone_brick + forbidden_arcanus:arcane_polished_darkstone_pillar + malum:tainted_rock_column
  + spectrum:onyx_pillar) -> T2/T3/T4 Ara Vitae buildable at Gilded. Not edited (read-only confirm).

## No-dupe scan
`grep -rl "blood_orb_magician\|blood_orb_master\|blood_orb_archmage" config/ftbquests/quests/chapters/`
-> only `g7_chartered_arcana.snbt`. g7 owns the three orb ids. No pack-wide dupe.

## Anchored id uniqueness
Chosen node/task/reward ids scanned across ALL chapters before authoring (ripgrep, anchored
`^\s+id: "…"`) -> 0 pre-existing matches. Post-edit full-file anchored dup scan: 32 ids, 0 dups.

## Byte discipline (Python ground truth, post-edit)
- EOL: CRLF 461 / LF-total 461 / bare-LF 0 -> pure CRLF preserved (file was 320/320 pre-edit).
- Braces { } 87/87 balanced. Brackets [ ] 42/42 balanced.
- Indentation: 0 lines with leading space (all tabs).

## Crossing-free statement — PASS
The four new nodes are an isolated left-hand column (x = -8 for A0/A1/A2, x = -6 for A3). Existing
g7 graph occupies x in [-4, +4]; the new column is entirely left of it with no shared x-band.
Internal edges: A0->A1 (vertical, x=-8), A1->A2 (vertical, x=-8), A1->A3 (short horizontal at y=5).
None of these cross. The single external edge A0->`0B03101000000034` targets a node in a DIFFERENT
chapter (ren_magic_foundations), so it draws off-canvas and cannot cross any g7 edge. No new
crossings introduced in g7.

## Audit outputs
- `tier_audit.py`: regenerated `A_tier_softlock_table.md` has SOFTLOCK count = 2, both PRE-EXISTING
  and unrelated (ir_digital_storage_foundations: ae2:pattern_provider, refinedstorage:autocrafter).
  All 4 of my new g7 rows report **OK** (A0/A1/A2 = gilded/gilded; A3 = (none)/gilded). 0 new softlock.
- `ef_audit.py`: DUP ids {} ; BACKWARD-age deps 0 ; EM/EN dash 0. 1 dangling edge + 1 orphan reported,
  both PRE-EXISTING and unrelated to this task (dangling `4D4E0120002400A1`->`5054012000060001` is a
  sibling task's stub state; orphan `3400000000009000` in stone_water). My A0 cross-chapter dep
  resolved cleanly (0 backward-age, no new dangling referencing my ids).
- `node --check`: N/A (no KubeJS touched).

## Concerns
None. Ladder is spine content with no gate; grants nothing. Optional rune (A3) kept — its recipe is
confirmed Gilded-craftable, so no reason to drop it per plan §2.
