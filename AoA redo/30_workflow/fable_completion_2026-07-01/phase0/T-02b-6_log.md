# T-02b-6 log — apothic_enchanting controlled line

**Task:** P3 apothic_enchanting controlled line (6 nodes, UNGATED) in
`config/ftbquests/quests/chapters/ren_observation_experimentation.snbt`.
**Status:** DONE.
**File set (contract):** edited `ren_observation_experimentation.snbt` only; created this log
and `phase0/stubs/T-02b-6_stubs.txt`. No lang/en_us.snbt edit, no KubeJS, no gate work
(gating closed per plan §5 / Policy 1).

## Nodes created (6)

| # | quest id | reward id | task id | task | x | y | flags |
|---|---|---|---|---|---|---|---|
| AE1 | 0B03108000000120 | 0B033080000001A0 | 0B03208000000120 | item `apothic_enchanting:hellshelf` | -3.0 | -6.0 | entry; hide_until_deps_complete; icon hellshelf |
| AE2 | 0B03108000000121 | 0B033080000001A1 | 0B03208000000121 | item `apothic_enchanting:infused_hellshelf` | -4.5 | -6.0 | hide_until_deps_visible |
| AE3 | 0B03108000000122 | 0B033080000001A2 | 0B03208000000122 | smart_filter seashelf/deepshelf/endshelf | -6.0 | -6.0 | hide_until_deps_visible; icon endshelf |
| AE4 | 0B03108000000123 | 0B033080000001A3 | 0B03208000000123 | item `apothic_enchanting:library` | -7.5 | -6.0 | hide_until_deps_visible |
| AE5 | 0B03108000000124 | 0B033080000001A4 | 0B03208000000124 | smart_filter 12 `*_tome` | -7.5 | -4.5 | optional:true; hide_until_deps_visible; icon weapon_tome |
| AE6 | 0B03108000000125 | 0B033080000001A5 | 0B03208000000125 | item `apothic_enchanting:ender_library` | -9.0 | -6.0 | optional:true; shape diamond; hide_until_deps_visible |

## Dependency wiring (new edges, all in-file)
- 0B03108000000001 (chapter root, x0 y-7.5) -> AE1  (entry gets its >=1 dep from the chapter root)
- AE1 -> AE2 -> AE3 -> AE4  (linear spine)
- AE4 -> AE5 (optional tomes)
- AE4 -> AE6 (optional Library of Alexandria capstone)

No rootless nodes: AE1 deps the chapter root; every other node deps a prior AE node.
No re-wires of existing nodes (old->new): none. This is an additive line only.

## Layout / crossing
Line placed in the empty negative-x band at y=-6.0/-4.5. The chapter root is the only
occupant with y<-3; all 57 pre-existing content nodes sit at y>=-3.0 and every existing
dependency edge runs from the root (0,-7.5) toward x>=0. My line runs the opposite way
(x from -3 to -9), so no existing edge enters my region.

**Crossing computation** (segment-intersection over all 61 edges, `phase0`-style):
- NEW-involving crossings: **0** (my 6 edges cross nothing).
- 8 total crossings reported are ALL pre-existing (between old nodes in this dense chapter);
  I added none and re-laid nothing existing, per contract rule 9 ("do not add crossings to
  dense chapters").

## Verify-first (item IDs)
All 6 task items + all filter members jar-verified in
`mods/ApothicEnchanting-1.21.1-1.5.3.jar`:
```
unzip -l mods/ApothicEnchanting-1.21.1-1.5.3.jar | grep models/item/
  -> hellshelf, infused_hellshelf, seashelf, deepshelf, endshelf, library, ender_library,
     weapon_tome, pickaxe_tome, helmet_tome, chestplate_tome, leggings_tome, boots_tome,
     bow_tome, fishing_tome, extraction_tome, scrap_tome, improved_scrap_tome, other_tome
```
All ids match the plan §5 table + Verification Log §9. `ftbfiltersystem:smart_filter` filter
shape copied from live examples (at5_threshold_of_war `root(or(item(...),...))`, stone_water).
No new/unlisted ids used.

## Age discipline
AStages scan: `grep -rn apothic_enchanting kubejs/server_scripts/aoa_astages_*.js` -> NO item
gates (only a loot-bypass restriction in `09`). Ungated -> Renaissance-legal (matches plan
Policy 1, gating closed). tier_audit reports all 6 nodes **OK** ("no lock; family legal
at/before chapter", the_renaissance).

## Duplicate scans
- Anchored pack-wide id scan `^\s+id: "0B03108000000{120..125}"` -> exactly 1 hit each, all in
  target file. Reward ids `0B033080000001A0..A5` and task ids `0B03208000000120..125`: 0 prior hits.
- Duplicate item task pack-wide: `grep -rn apothic_enchanting: config/.../chapters/` before edit
  -> **No matches** (apothic_enchanting was tasked nowhere). No dep-reference needed.
- Variant discipline: biome shelves (AE3) and tomes (AE5) each a single smart_filter node, not
  per-variant. `draconic_endshelf`/`pearl_endshelf`/`treasure_shelf` deliberately NOT featured.

## Byte discipline
- Pre-edit: CRLF 1904 / LF-only 0. Post-edit: CRLF 2108 / LF-only 0. Pure CRLF preserved.
- Insertion done via Python (bytes) to guarantee CRLF on all new lines; tab-indent preserved.
- SkillsLevel + PlayerSpells blocks copied verbatim from sibling nodes (check:0b), not stripped,
  not hand-typed differently.
- Brace balance { } = 387/387; bracket balance [ ] = 255/255. No in-file duplicate ids.

## Audit outputs
- `tier_audit.py`: 0 SOFTLOCK involving my nodes; all 6 apothic nodes = OK. (2 total SOFTLOCK in
  regenerated table are pre-existing, unrelated.)
- `ef_audit.py`: DUP ids {} ; EM/EN dash 0 ; NON-ARRAY quest_desc 0 ; BACKWARD-age deps 0.
  1 dangling (`4D4E0120002400A1`) + 1 orphan (`stone_water...`) are PRE-EXISTING and unrelated
  to this task (different files/ids; I added no dangling dep and no orphan — AE1 deps the root).
- No KubeJS touched -> no `node --check` needed.

## Concerns
None. Line is additive, ungated, self-contained, crossing-free for its own edges.
Prose stubs handed to Opus via sidecar.
