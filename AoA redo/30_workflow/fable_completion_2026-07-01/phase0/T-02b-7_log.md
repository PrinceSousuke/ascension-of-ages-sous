# T-02b-7 log — mahoutsukai optional chapter `ren_mahou_tsukai`

Task: create NEW explicitly-optional Renaissance chapter (6 nodes, ALL `optional: true`,
never a capstone dependency). File set: CREATE
`config/ftbquests/quests/chapters/ren_mahou_tsukai.snbt` + this log + stub sidecar.

## Chapter header
- filename `ren_mahou_tsukai`, group `0B038EB15EBBFD95` (the_renaissance).
- id `4D41487500000000` (fresh; verified unique pack-wide).
- order_index `12` (no other chapter in the pack uses order_index 12; Second Mill=10,
  ren_spectrum_academy planned=11, this=12 per plan sec.6).
- icon `mahoutsukai:mahoujin_projector`.
- `hide_quest_until_deps_complete: true` (matches all sibling Renaissance chapters).

## ID PREFIX CHANGE (plan IDs were unusable — collision)
The plan sec.6 proposed node ids `0B03106000000001`..`0B03106000000006`. Anchored scan
proved `0B03106000000001` (and the entire `0B03106*` space) is ALREADY IN USE by
`ren_deeper_darker_otherside.snbt` (37 nodes). The plan's chapter-id note (`0B03107*`)
also collides with `ren_archive_recordkeeping.snbt`. Per contract rule 5 (fresh 16-hex ids
proven unique), I assigned a fresh coherent prefix `4D414875` ("MAHU" ASCII) for this
task. All ids proven unique via anchored scan (`^\s+id: "<16hex>"`) across all chapters.

## Nodes created (all `optional: true`; single root, fan right; no crossings)
| # | id | x | y | deps | task | icon | flags |
|---|---|---|---|---|---|---|---|
| MT1 | 4D41487500000001 | 0.0 | 0.0 | `6D7E8F901A2B1054` (Ren gateway) | item `mahoutsukai:guidebook` | guidebook | entry; hide_until_deps_complete; size 1.5; optional |
| MT2 | 4D41487500000002 | 1.5 | 0.0 | MT1 | item `mahoutsukai:attuner` | attuner | optional |
| MT3 | 4D41487500000003 | 3.0 | 0.0 | MT2 | item `mahoutsukai:mahoujin_projector` | mahoujin_projector | optional |
| MT4 | 4D41487500000004 | 4.5 | 0.0 | MT3 | item `mahoutsukai:mystic_code` | mystic_code | optional |
| MT5 | 4D41487500000005 | 6.0 | -1.5 | MT4 | smart_filter (scroll_familiars_garden OR scroll_gandr OR scroll_fay_sight) | scroll_familiars_garden | optional |
| MT6 | 4D41487500000006 | 6.0 | 1.5 | MT4 | item `mahoutsukai:mystic_staff` | mystic_staff | optional; shape diamond; size 1.5 |

Reward ids `4D4148753000000{1..6}`, task ids `4D4148752000000{1..6}` (all unique by
construction under the fresh prefix; covered by the anchored id scan for the node ids and
distinct sub-namespaces for reward/task).

## Entry gating (reveal rule)
MT1 (entry) depends on `6D7E8F901A2B1054`, the Medieval->Renaissance gateway defined in
`what_waits_in_the_grove.snbt` L1314 (grants `the_renaissance` via command reward). This
is the exact entry pattern of sibling `ren_second_mill_steam_rail_logistics.snbt` (its
entry node `0B031B1000000001` deps `["6D7E8F901A2B1054"]`). So the tab is NOT rootless /
always-visible; it opens when the player enters the Renaissance. NO node in the age spine
or any capstone aggregator depends on any mahoutsukai node (chapter is a leaf).

## Optional-chapter compliance
Every one of the 6 quests carries `optional: true`. The chapter is a standalone optional
side tab (mahoutsukai = self-contained flavor spell-circle system), never on the main
progression spine and never an N-of-M requirement. Confirmed by leaf status above.

## Verification (VERIFY-FIRST protocol)
### Jar item existence (mahoutsukai-1.21.1-v1.36.27.jar, assets/mahoutsukai/models/item/)
All present (python zipfile scan):
`guidebook` OK, `attuner` OK, `mahoujin_projector` OK, `mystic_code` OK,
`scroll_familiars_garden` OK, `scroll_gandr` OK, `scroll_fay_sight` OK, `mystic_staff` OK.
AVOID items confirmed present-but-excluded: `staff_emrys` (reward-gear), `morgan` (OW-gated).

### AStages age-discipline (tier_audit.py regenerated A_tier_softlock_table.md)
All 8 ren_mahou_tsukai task rows report **OK** — `(none)` lock, family legal at/before
`the_renaissance`. 0 SOFTLOCK contributed by this task. (The 2 SOFTLOCK rows in the table
are pre-existing AE2/RS entries in `ir_digital_storage_foundations`, not in my file set.)

### Duplicate-id scan (anchored `^\s+id: "<16hex>"`, all chapters)
All 7 ids (chapter + 6 nodes) return exactly 1 hit, all in ren_mahou_tsukai.snbt. PASS.

### Duplicate item-task scan (pack-wide)
Each of the 8 task items grepped across chapters/: 0 pre-existing task uses. No dep-ref
needed; safe to author as fresh tasks. PASS.

### ef_audit.py
DUP ids {} (0). EM/EN dash 0. NON-ARRAY quest_desc 0. BACKWARD-age deps 0.
DANGLING = 1 (`4D4E0120002400A1`, pre-existing, not mine). ORPHANS = 1
(`3400000000009000` in stone_water, pre-existing, not mine). This task adds 0 dangling /
0 orphan / 0 backward-age.

### .snbt byte discipline
Pure CRLF: 234 CRLF, 0 bare LF. Tabs preserved. SkillsLevel + PlayerSpells blocks copied
verbatim from sibling `ren_second_mill_steam_rail_logistics.snbt` (never hand-typed,
never stripped). Brace/bracket/paren balance: {}=45/45, []=26/26, ()=5/5.

### smart_filter shape
MT5 uses the live NBT shape copied from `g4_the_infinite_grid.snbt` L1010:
`item: { components: { "ftbfiltersystem:filter": "root(or(item(...),item(...),item(...)))" }, count: 1, id: "ftbfiltersystem:smart_filter" }`.

## Crossing statement
ren_mahou_tsukai: linear spine MT1->MT2->MT3->MT4 along y=0.0 (x 0.0..4.5), then MT4
branches to MT5 (y=-1.5) and MT6 (y=+1.5) on opposite sides at x=6.0. No two dependency
segments share the plane in a way that intersects. ZERO crossings.

## STATUS: DONE
