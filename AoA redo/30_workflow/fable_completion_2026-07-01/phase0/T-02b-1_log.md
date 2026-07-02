# T-02b-1 log — P1 Spectrum new chapter `ren_spectrum_academy`

Task: create NEW chapter `config/ftbquests/quests/chapters/ren_spectrum_academy.snbt` (12 nodes),
Renaissance group `0B038EB15EBBFD95`, order_index 11. File set: new chapter + this log + stub sidecar.

## STATUS: DONE_WITH_CONCERNS

Two forced deviations from the plan (both to preserve hard invariants), plus one age-gate substitution.
None change scope; all documented below and flagged to the coordinator.

---

## Files touched (exclusive to this task)
- CREATE `config/ftbquests/quests/chapters/ren_spectrum_academy.snbt` (12 quests + chapter header)
- CREATE `AoA redo/30_workflow/fable_completion_2026-07-01/phase0/stubs/T-02b-1_stubs.txt` (lang stubs; 13 title keys + 12x subtitle/desc)
- CREATE this log

No other file edited. `en_us.snbt` NOT touched (per contract rule 3).

---

## DEVIATION 1 (CRITICAL — coordinator action needed): quest-id prefix remapped `0B03105*` -> `0B0310C*`

The plan reserved ids `0B03105000000001 .. 0B03105000000024`. Anchored pack-wide scan proved
the ENTIRE `0B03105*` block is ALREADY OWNED by `ren_undergarden_descent.snbt`
(id `0B03105000000001`, `...0010`, `...0011`, `...0012`, `...0020`, `...0021`, `...0022` all exist there).
Shipping the plan ids verbatim would create 7+ hard id collisions (uniqueness is a hard FTBQ invariant).
The plan's sec-8 uniqueness proof was wrong for this prefix.

Resolution: allocated the next free block `0B0310C*` (verified fully unused; Second Mill is `0B0310B*`).
Chapter id = `0B0310C000000000`. Node ids `0B0310C000000001 .. ...0024` (same low-order suffixes as the plan).

**IMPACT ON T-02b-2 (the parallel IR-reveal wire):** the plan told T-02b-2 to add dep
`0B03105000000022` (plan N10) onto IR node `49540B100000000C`. That target id does NOT exist here.
The real N10 (Spirit Instiller convergence) id is now **`0B0310C000000022`**.
**T-02b-2 must reference `0B0310C000000022`, not `0B03105000000022`.**

Suffix map (plan -> shipped): all `0B03105xxxxxxxxx` -> `0B0310Cxxxxxxxxx` (identical last 6 hex).

## DEVIATION 2 (age-discipline): N9 fusion shrine `basalt` -> `calcite`

Plan N9 = `spectrum:fusion_shrine_basalt`. Live gate `aoa_astages_01m_magic.js` L72 gates
`fusion_shrine_basalt` to **industrial_revolution** (cross-age inversion in a Renaissance chapter).
L73 gates `fusion_shrine_calcite` to **the_renaissance**. Substituted to `spectrum:fusion_shrine_calcite`
(model + gate verified). Same mechanic (Fusion Shrine), correct age. tier_audit confirms OK@the_renaissance.

## DEVIATION 3 (no-dupe): N10 item task -> advancement task

Plan N10 = item `spectrum:spirit_instiller`. Pack-wide grep found `spectrum:spirit_instiller` is
ALREADY an item task in `g7_chartered_arcana.snbt` (quest `4341011000000004`, task `4341011020040001`;
it gates `g_magic_authorization_complete`). Re-tasking the item = duplicate (contract rule 8). The item
is Renaissance-gated so this chapter IS its correct age home, but I may only touch my own file and cannot
dep-reference a *later* Gilded node from a Renaissance node (backward-age/reveal leak).
Resolution: N10 tasks the ADVANCEMENT `spectrum:midgame/build_spirit_instiller_structure`
(jar-verified: `data/spectrum/advancement/midgame/build_spirit_instiller_structure.json`), icon still
`spectrum:spirit_instiller`. This teaches "build the Spirit Instiller apparatus" without an item-task dup.
Note: the same advancement is also tasked (optional) in `ir_magic_feedstock_and_spectrum_network.snbt`
(`49540B200000E000`); advancement-task reuse is not the forbidden item-task dup, and it is a distinct
chapter/age reading. Flagged for coordinator judgment if a hard single-source of the advancement is wanted.

Also note: the plan's N12 advancement `spectrum:milestones/build_spirit_instiller` does NOT exist
(only `midgame/build_spirit_instiller_structure` and `unlocks/blocks/spirit_instiller`). N12 used the
plan's named fallback: item `spectrum:ink_assortment` (verified, ungated Renaissance-legal).

---

## Node table (as shipped)

| # | id | x | y | deps (in-chapter) | task | icon | flags |
|---|---|---|---|---|---|---|---|
| N1 | 0B0310C000000001 | 0.0 | 0.0 | gateway 6D7E8F901A2B1054 | item spectrum:pigment_palette | pigment_palette | entry, size 1.5, hide_until_deps_complete |
| N2 | 0B0310C000000002 | 1.5 | 0.0 | N1 | item spectrum:color_picker | (task item) | hide_until_deps_visible |
| N3 | 0B0310C000000003 | 3.0 | 0.0 | N2 | item spectrum:titration_barrel | (task item) | " |
| N4 | 0B0310C000000010 | 1.5 | -1.5 | N1 | item spectrum:pedestal_all_basic | (task item) | " |
| N5 | 0B0310C000000011 | 3.0 | -3.0 | N4 | smart_filter: pedestal_basic_amethyst/citrine/topaz | pedestal_basic_topaz | " |
| N6 | 0B0310C000000012 | 4.5 | -1.5 | N5 | item spectrum:pedestal_moonstone | (task item) | " |
| N7 | 0B0310C000000013 | 6.0 | -1.5 | N6 | item spectrum:pedestal_onyx | (task item) | shape diamond |
| N8 | 0B0310C000000020 | 4.5 | 1.5 | N3 | smart_filter: 5 Pastel Network nodes | provider_node | hide_until_deps_visible |
| N9 | 0B0310C000000021 | 6.0 | 1.5 | N8 | item spectrum:fusion_shrine_calcite (SUB) | (task item) | shape hexagon |
| N10 | 0B0310C000000022 | 7.5 | 0.0 | N7, N9 | advancement spectrum:midgame/build_spirit_instiller_structure (SUB) | spirit_instiller | shape gear |
| N11 | 0B0310C000000023 | 9.0 | -1.5 | N10 | item spectrum:particle_spawner | (task item) | optional |
| N12 | 0B0310C000000024 | 9.0 | 1.5 | N10 | item spectrum:ink_assortment | (task item) | optional |

Reward ids `0B0310C030000001..024` (xp), task ids `0B0310C020000001..024`. All unique (share the file's unique prefix).

---

## Verification outputs

### Byte discipline (Python)
`ren_spectrum_academy.snbt`: bytes 8727, CRLF 418, LF-only 0, brace balance 0, bracket balance 0.
Matches sibling convention (Second Mill = CRLF 609/0). SkillsLevel + PlayerSpells blocks copied verbatim
from sibling nodes on every item/filter/advancement task (never hand-typed, never stripped).

### Entry-gating pattern (contract rule 6)
Replicated from siblings `ren_second_mill_steam_rail_logistics.snbt` (entry quest deps `["6D7E8F901A2B1054"]`,
`hide_until_deps_complete: true`) and `ren_starlight_observation.snbt`. Chapter header copies the sibling
structure (group `0B038EB15EBBFD95`, `hide_quest_until_deps_complete: true`, `order_index: 11` after
Second Mill's 10). Entry node N1 has 1 dep (the Renaissance gateway) so the tab is NOT rootless/always-visible.

### Duplicate-id scan (anchored, pack-wide) — ripgrep (bash grep -P fails on this locale)
`^\s+id: "(all 13 new ids)"` over `config/ftbquests/quests/chapters` = 13 hits, all in `ren_spectrum_academy.snbt`, one each. 0 collisions.

### Duplicate item-task scan (pack-wide)
Every task item grepped over chapters dir. All 0 pre-existing EXCEPT `spectrum:spirit_instiller` (3 hits:
g7 item task + IR icon/advancement + journey icon) — resolved via DEVIATION 3 (advancement, not item).
No new item-task duplicates introduced.

### tier_audit.py -> A_tier_softlock_table.md
Regenerated. **0 SOFTLOCK** total. All 17 `ren_spectrum_academy` rows = **OK** @ the_renaissance
(pigment_palette L730, pedestals L731-736, color_picker/titration_barrel/particle_spawner/fusion_shrine_calcite
via 01m_magic.js, 5 network nodes L485-489, ink_assortment ungated-legal). N10 advancement has no item row (correct).

### ef_audit.py
`TOTAL quest ids parsed: 2062; DUP ids: {}; DANGLING dep sources: 0; total dangling edges: 0; BACKWARD-age deps: 0;
EM DASH 0; EN DASH 0.` ORPHANS: 1 = pre-existing `3400000000009000` in `stone_water_weather_and_wounds` (NOT mine).

### Era check
No item later-tier than the_renaissance. Basalt->calcite substitution (DEV2) removed the only inversion the
plan would have introduced. No AVOID-list items placed.

### Crossing statement
`ren_spectrum_academy`: 12 nodes, 12 in-chapter dependency edges. Segment-intersection test over all edge
pairs (proper crossings, shared endpoints excluded) = **0 CROSSINGS**. Three lanes fan right from the N1 entry
(color/tool lane y=0; pedestal lane y=-1.5..-3; network+shrine lane y=1.5), converging cleanly at N10 (7.5,0).

### node --check
No KubeJS file touched. N/A.

---

## Handoffs / concerns for coordinator
1. **T-02b-2 target id changed**: use `0B0310C000000022` (not the plan's `0B03105000000022`) for the IR-reveal dep onto `49540B100000000C`. (DEVIATION 1.)
2. N9 shipped as `fusion_shrine_calcite` (Renaissance-legal), not `basalt` (IR-gated). (DEVIATION 2.)
3. N10 shipped as advancement `spectrum:midgame/build_spirit_instiller_structure` (avoids g7 item-task dup); if a single-source of that advancement is desired, decide whether the IR optional node `49540B200000E000` should be re-pointed. (DEVIATION 3.)
4. Ledger before/after: new `ren_spectrum_academy` = 12 nodes (matches plan sec.9 expected count).
