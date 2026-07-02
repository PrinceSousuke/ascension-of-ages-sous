# T-02b-4 log — Malum soulstone-harvest completion in `ren_magic_foundations.snbt`

**Task:** PLAN_02b sec.3 (P2 Malum). Add the soulstone/spirit-harvest completion (3 nodes) to the
Renaissance Malum lane. File set: `config/ftbquests/quests/chapters/ren_magic_foundations.snbt`
(+ this log + `phase0/stubs/T-02b-4_stubs.txt`). No git, working-tree only.

## Nodes created (Malum lane, extends the spirit_jar column)

| id | task | icon | x,y | deps | flags |
|---|---|---|---|---|---|
| `0B0310100000000B` (MA1) | item `malum:crude_scythe` | crude_scythe | -9.0, 12.0 | `0B0310100000000A` (spirit_jar) | hide_until_deps_visible |
| `0B0310100000000C` (MA2) | item `ftbfiltersystem:smart_filter` (9 spirits) | (filter; renders spirit) | -9.0, 13.5 | `0B0310100000000B` | hide_until_deps_visible |
| `0B0310100000000D` (MA3) | item `malum:soul_stained_steel_scythe` | soul_stained_steel_scythe | -9.0, 15.0 | `0B0310100000000C` | optional:true, shape diamond, hide_until_deps_visible |

Reward ids `0B0330100000000B/C/D` (xp 15/20/30); task ids `0B0320100000000B/C/D`. All copy the sibling
Malum-node structure (PlayerSpells + SkillsLevel blocks copied verbatim from node `0B0310100000000A`,
never hand-typed/stripped).

MA2 smart-filter payload (exact NBT, copied shape from the live `49540B2000003000` filter in
`ir_magic_feedstock_and_spectrum_network.snbt`), extended to all 9 spirits:
`root(or(item(malum:sacred_spirit),item(malum:wicked_spirit),item(malum:arcane_spirit),item(malum:eldritch_spirit),item(malum:aerial_spirit),item(malum:aqueous_spirit),item(malum:earthen_spirit),item(malum:infernal_spirit),item(malum:umbral_spirit)))`

## Design deviation from the plan (documented, contract rule 9 mandate)

The plan (sec.3) proposed MA1 = `malum:soulstone`/`refined_soulstone` at x=-12.0. **Two author-time
corrections, both flagged VERIFY-AT-AUTHOR in the plan sec.9:**

1. **MA1 item changed soulstone -> `crude_scythe`.** `malum:refined_soulstone` is ALREADY a task item in
   this same chapter (node `0B03101000000004`, x=-7.5, y=0.0, line 140). Re-using it would be a
   pack-wide duplicate item task (forbidden). The plan's stated Renaissance gap is "nothing teaches the
   harvest that fills the jar." The harvest TOOL is `malum:crude_scythe` (jar-verified, ungated) — the
   honest missing rung. MA3 = `malum:soul_stained_steel_scythe` (the altar-infused upgrade) is the lane
   capstone. This is a tighter, non-duplicate teach of exactly the loop the plan named.
2. **Coordinates changed x=-12 column -> vertical extension of the spirit_jar column at x=-9.0
   (y=12.0/13.5/15.0).** The plan's x=-12,y=10.5 MA1 edge (from spirit_jar at -9.0,10.5) crosses the
   pre-existing pedestal edge `0B03101000000009`(-9.0,9.0) -> `0B0310100000003A`(-10.5,12.0) at
   (-9.75,10.5). Re-laid as a straight downward column below spirit_jar to satisfy the crossing-free
   hard constraint (verified below).

## Verification (outputs)

**Line endings:** pure CRLF preserved. Before: CRLF 2092 / bare-LF 0. After: CRLF 2190 / bare-LF 0.
**Structure:** braces balanced (0), brackets balanced (0). SkillsLevel blocks present in all 65 quests
(none stripped). Quest count 62 -> 65 (+3), matches plan sec.9 target (61->64 per plan text; the on-disk
baseline was 62 quests -> 65).

**Duplicate-id scan (anchored, pack-wide chapters):**
- `^\s+id: "0B0310100000000(B|C|D)"` -> No matches before insert (unique).
- reward ids `0B033010000000(0B|0C|0D)` and task ids `0B032010000000(0B|0C|0D)` -> No matches (free).

**No duplicate item task (pack-wide chapters):**
- `id: "malum:crude_scythe"` -> 1 hit (my MA1 only).
- `id: "malum:soul_stained_steel_scythe"` -> 1 hit (my MA3 only).
- `malum:refined_soulstone` -> pre-existing task at node `0B03101000000004`; NOT reused (see deviation 1).
- 9 spirits: appear in MA2's smart_filter (a `ftbfiltersystem:smart_filter` item, not an individual
  item task) and in the IR chapter's own filter/`arcane_spirit` item task; MA2 is the Renaissance FIRST
  harvest (distinct mechanic surface from the IR feedstock node). No literal duplicate item-task id.

**tier_audit.py:** ran; regenerated `A_tier_softlock_table.md` has **0 SOFTLOCK**. My 3 nodes all report
`the_renaissance | OK | no lock; family legal at/before chapter` (all 9 spirits + crude_scythe +
soul_stained_steel_scythe each OK).

**ef_audit.py:** DUP ids {} (0). DANGLING dep sources 0 / dangling edges 0. BACKWARD-age deps 0.
EM/EN dash 0. ORPHANS 1 = `3400000000009000` in `stone_water_weather_and_wounds` (PRE-EXISTING, not
mine; my MA1 deps on spirit_jar so my chain is rooted). My 3 nodes correctly flagged missing_desc
(stubs live in the sidecar for Opus — expected).

**Era check:** all task items = the_renaissance-legal.
- `malum:crude_scythe` — no AStages lock (grep of `aoa_astages_*.js` returns only spirit_crucible/
  catalyzer @ IR and spirit_altar @ the_renaissance; scythe/spirits/refined_soulstone ungated).
- 9 spirits — ungated (`#malum:spirits` = `#malum:aspected_spirits` [8] + umbral_spirit [1], jar-verified
  from `data/malum/tags/item/spirits.json` + `aspected_spirits.json`).
- `malum:soul_stained_steel_scythe` — no lock. Crafted via `malum:spirit_infusion`
  (`data/malum/recipe/spirit_infusion/soul_stained_steel_scythe.json`) from crude_scythe +
  soul_stained_steel_ingot + refined_soulstone + hex_ash + earthen/wicked/arcane spirits, all
  Renaissance-legal at the spirit_altar. No EnderIO or Gilded machine on the path. Verified NOT a
  cross-age inversion (the `01l` comment gating EnderIO ensouled/soul_stained_steel *machines* to Gilded
  does not touch malum's own spirit-infusion ingot/scythe).

**Jar proofs (malum-1.21.1-1.8.2.jar item models):** `crude_scythe.json`, `soul_stained_steel_scythe.json`,
`refined_soulstone.json`, and all 9 `*_spirit.json` present. No `malum:hex` / `cracked_soul_container`
item (plan's MA3 alt icon candidates) — irrelevant, MA3 uses the verified scythe.

**Crossing statement (`ren_magic_foundations.snbt`):** segment-intersection computed over all dependency
edges post-edit. TOTAL proper crossings = 4, all PRE-EXISTING and unrelated to this task:
`(030->031 vs 001->051)`, `(030->031 vs 001->060)`, `(030->031 vs 001->071)` (root fan-out) and
`(036->03D vs 039->CAFE)` (capstone aggregator region). **CROSSINGS INVOLVING NEW NODES = 0.** This task
added zero crossings. The 4 pre-existing crossings are outside this task's file-set mandate (they involve
the root `0B03101000000001` fan and the `0B0310100000CAFE` aggregator, not the Malum lane) — flagged here
for the coordinator, not fixed.

## Files touched
- `config/ftbquests/quests/chapters/ren_magic_foundations.snbt` (+3 nodes, +98 lines)
- `AoA redo/30_workflow/fable_completion_2026-07-01/phase0/stubs/T-02b-4_stubs.txt` (created; 9 stub keys)
- `AoA redo/30_workflow/fable_completion_2026-07-01/phase0/T-02b-4_log.md` (this file)

No KubeJS files touched (no `node --check` needed). No lang/en_us.snbt edit (stubs -> sidecar per contract).
