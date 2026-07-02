# T-02c-5 log — IP seismic/flarestack EXTEND ir_create_industrial_addons

Task: EXTEND `config/ftbquests/quests/chapters/ir_create_industrial_addons.snbt` — add
`immersivepetroleum:seismic_survey` + `immersivepetroleum:flarestack` off the existing IP
projector/pumpjack lane. `gas_generator` NOT added (designer drop — see CONCERN below).

File set (contract): `ir_create_industrial_addons.snbt` + this log + `stubs/T-02c-5_stubs.txt`.
No other file edited. NO git run.

## Nodes created

| node id | item | task type | icon | x | y | dep | dep rationale |
|---|---|---|---|---|---|---|---|
| 4954071000000101 | `immersivepetroleum:seismic_survey` | item | seismic_survey | 1.5d | -4.0d | `4954071000000001` (projector) | survey-then-drill loop, sequenced right off the Engineer's Projector |
| 4954071000000102 | `immersivepetroleum:flarestack` | item | flarestack | 4.5d | -2.0d | `4954071000000003` (pumpjack) | vents a working well; hangs off the Pumpjack multiblock node |

- Reward ids: seismic xp `4954073000101000` / loot `4954073000101001`; flarestack xp
  `4954073000102000` / loot `4954073000102001`. Loot table `8430738502437568513L` (the IP
  item-node table used by every existing IP item node in this chapter).
- Task ids: `4954072000101000`, `4954072000102000`.
- Both nodes copied the `SkillsLevel`/`PlayerSpells` inert blocks byte-for-byte from the
  sibling IP item node (projector). `hide_until_deps_visible: true` matches the existing IP
  chain nodes (derrick/pumpjack/oiltank all use `hide_until_deps_visible`). No rootless node
  (each has exactly one dependency).
- No re-wire of old nodes needed (pure additive leaves; no existing node depends on them).

## Chapter node count

- Before: 57 quest nodes. After: 59 (+2). (File `id: "4954080000000000"`, order_index 4 —
  note the plan text calls it `4954070000000000`; the actual on-disk chapter id is
  `4954080000000000`; IP node scheme inside it is `4954071000000NNN`, which is what the plan's
  node table uses, so the suffix assignments are correct.)

## Verification (outputs)

- **Line endings:** pure CRLF preserved. Before: 2568 CRLF / 0 bare LF. After: 2656 CRLF / 0
  bare LF. Tabs preserved (nodes generated at the file's real tab depth: `\t\t{`, `\t\t\t`
  fields, `\t\t\t\t`+ nested).
- **Brace/bracket balance:** `{ } 474/474 BAL`; `[ ] 239/239 BAL`.
- **Anchored id-dup scan** (`^\s+id: "..."`): `4954071000000101` -> 1 (only this chapter);
  `4954071000000102` -> 1. All reward/task ids each appear exactly once pack-wide.
- **Duplicate-item scan:** `immersivepetroleum:seismic_survey` and `:flarestack` appear in ZERO
  other chapters before this edit — no duplicate task, no dep-reference substitution needed.
- **Item existence (jar):** `mods/ImmersivePetroleum-1.21.1-4.4.1-37.jar`,
  `assets/immersivepetroleum/lang/en_us.json`: `block.immersivepetroleum.seismic_survey =>
  "Seismic Survey Tool"`, `block.immersivepetroleum.flarestack => "Flarestack"`. Item models
  present (`models/item/seismic_survey.json`, `models/item/flarestack.json`).
- **AStages legality (gating CLOSED, cited only to confirm IR-legal):**
  `kubejs/server_scripts/aoa_astages_01d_immersive.js:61` seismic_survey @ industrial_revolution;
  line 63 flarestack @ industrial_revolution. Chapter age = IR. No later-tier item.
- **tier_audit.py:** ran; regenerated `A_tier_softlock_table.md` lists both my nodes as **OK**
  (item lock IR == chapter IR). The 2 SOFTLOCK rows in the table belong to
  `ir_digital_storage_foundations` (sibling task T-02c-1), NOT my file. My chapter = 0 softlock.
- **ef_audit.py:** DUP ids {}; DANGLING 0; BACKWARD-age 0; EM/EN dash 0. Sole ORPHAN is
  `3400000000009000` in `stone_water_weather_and_wounds` (pre-existing, not mine).
- **Era check:** IP is IR-tier tech; both items IR-legal. No later-tier tech introduced.

## Crossing statement — ZERO crossings

New edges: seismic (1.5,-4.0) -> projector (0.0,-2.5); flarestack (4.5,-2.0) -> pumpjack
(5.5,0.0). Ran a proper-segment-intersection check against all nearby existing IP/oil edges
(derrick->projector, pumpjack->derrick, crudeoil->pumpjack, oiltank->pumpjack, plastic->refinery)
and new-vs-new: **NONE**. No existing node lies on either new edge; no coordinate clash. The
flarestack edge shares its parent endpoint with the oiltank vertical (both off pumpjack) and
diverges without crossing.

## CONCERN — designer's gas_generator drop is factually wrong for THIS jar

Followed the task instruction and did NOT add `immersivepetroleum:gas_generator`. However, the
plan's stated reason ("id does not exist in the IP jar", PLAN section E) is CONTRADICTED by the
installed jar. In `ImmersivePetroleum-1.21.1-4.4.1-37.jar` the item is fully real and craftable:
- `block.immersivepetroleum.gas_generator => (lang present)`
- `assets/immersivepetroleum/models/item/gas_generator.json`
- `assets/immersivepetroleum/blockstates/gas_generator.json`
- `data/immersivepetroleum/recipe/gas_generator.json` (a craftable recipe)
- `data/immersivepetroleum/loot_table/blocks/gas_generator.json`

So the drop rationale is stale/incorrect for the live jar; the item exists and has a recipe. I
left it OUT per the explicit task instruction ("gas_generator was dropped by the designer... do
not add it"), but flag for CC: if the drop was based on the "does not exist" claim, that premise
is false and a gas_generator node (IR-tier IP gas-burning generator, would slot off the
distillation/coker gas outputs) could legitimately be authored. Requesting a canon call rather
than authoring it blind, since it is a scope reversal, not a fix within my file set.
