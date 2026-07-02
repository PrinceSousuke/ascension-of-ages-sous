# T-02b-3 log — P2 IE repair in `metallurgy.snbt`

**Task:** 3-node IE repair per PLAN_02b_ren_earlier.md sec.2 — wire the dead-end
`mb_tank` leaf onward and add a forward pointer toward the IR multiblock fleet.
**File edited (exclusive):** `config/ftbquests/quests/chapters/metallurgy.snbt`
**Sidecar:** `phase0/stubs/T-02b-3_stubs.txt`
**Status:** DONE_WITH_CONCERNS (M1 item substituted; optional M3 dropped — both forced
by verification, both authorized by the plan's VERIFY-AT-AUTHOR / substitute clause).

---

## Nodes created (2)

| node | quest id | x | y | deps | task | icon | shape/flags |
|---|---|---|---|---|---|---|---|
| M1 | `2902E58DB70F9450` | 8.0 | -4.0 | `2902E58DB70F9441` (mb_tank) | item `immersiveengineering:pipe_valve` | (task item) | rsquare, hide_until_deps_complete, xp 25 |
| M2 | `2902E58DB70F9451` | 8.0 | -5.5 | `2902E58DB70F9450` (M1) | advancement `immersiveengineering:multiblocks/mb_crusher` | `immersiveengineering:crusher` | rsquare, hide_until_deps_complete, xp 25 |

Reward xp ids: M1 `2902E58DB70F9150`, M2 `2902E58DB70F9151`.
Task ids: M1 `2902E58DB70F9050`, M2 `2902E58DB70F9051`.
No old→new re-wires (pure additive; mb_tank kept its own dep on fluid_pipe `2902E58DB70F9440`).

## Deviations from plan (both forced by age-discipline + duplicate rules)

1. **M1 item substituted `fluid_pump` → `pipe_valve`.** The plan's M1 item
   `immersiveengineering:fluid_pump` carries an explicit AStages **item lock to
   industrial_revolution** (`aoa_astages_01_item_restrictions.js` L347:
   `["industrial_revolution", "immersiveengineering:fluid_pump", "item"]`). This chapter
   is `medieval_times`. Placing it would be a real cross-age softlock (the tier_audit would
   have flagged it SOFTLOCK, not CANON). The plan sec.9 explicitly authorizes: "confirm
   before use or substitute a verified IE fluid/tool item." Substituted
   `immersiveengineering:pipe_valve` — a fluid-pipe control component (regulates flow
   into/out of the IE tank), verified item model present, **no AStages lock anywhere**
   (grep of all `aoa_astages_*.js` — only fluid_sorter/sorter/fluid_placer/fluid_pump are
   IR-gated; pipe_valve/wooden_barrel/metal_barrel are ungated, same "ruled exception"
   class as the existing bootstrap-lane items fluid_pipe/hempcrete/concrete). Preserves the
   plan's stated intent ("wires the tank leaf onward, fluid handling").
2. **Optional M3 dropped.** The plan's M3 item `immersiveengineering:blueprint` is
   **already a live item task pack-wide** in `ir_immersive_engineering_early_factory.snbt`
   (quest `4954011000000011`, task `4954012000011000`). Contract rule 8 forbids duplicate
   item tasks. No Medieval-legal substitute preserves M3's stated "treated-wood → IR bridge"
   intent without becoming filler (that bridge role is already served by M2's mb_crusher
   forward pointer). M3 was the optional node ("2-3 (M1,M2,+opt M3)"), so dropping it keeps
   the required repair (dead-end wire + fleet pointer) fully intact. Net new nodes = 2.

## Verification IDs / jar proofs (this pass)

- `immersiveengineering:pipe_valve` model:
  `unzip -l ImmersiveEngineering-1.21.1-12.4.2-194.jar | grep models/item/pipe_valve` →
  `assets/immersiveengineering/models/item/pipe_valve.json` EXISTS.
- `immersiveengineering:crusher` model (M2 icon): `...models/item/crusher.json` EXISTS.
- `immersiveengineering:multiblocks/mb_crusher` advancement:
  `data/immersiveengineering/advancement/multiblocks/mb_crusher.json` EXISTS.
- AStages age proof: pipe_valve = **no lock** (Medieval-legal by IE-bootstrap exception,
  same as every other item in this lane). fluid_pump = IR (rejected).

## Audit outputs

- `tier_audit.py` → regenerated `A_tier_softlock_table.md`: **0 SOFTLOCK rows.** New node
  `2902E58DB70F9450` (pipe_valve) classified **CANON** — identical to the existing IE
  bootstrap lane siblings (stick_treated, fluid_pipe, hempcrete, connector_lv, …). No
  SOFTLOCK row mentions pipe_valve or either new id.
- `ef_audit.py`: **DUP ids: {} ; DANGLING deps: 0 ; BACKWARD-age deps: 0 ;** NON-ARRAY
  quest_desc 0. Orphans: 1 = pre-existing `3400000000009000` in
  `stone_water_weather_and_wounds` (not mine; both my nodes have ≥1 dep).
- Duplicate-id scan (pack-wide, anchored `id: "<id>"`): each of the 6 new ids (quest
  9450/9451, task 9050/9051, reward 9150/9151) → exactly 1 occurrence.
- Duplicate item-task scan: `immersiveengineering:pipe_valve` → 0 prior task uses pack-wide
  (safe). (blueprint → already tasked → M3 dropped, see deviation 2.)

## Byte discipline

- Line endings: pure **CRLF**, 0 bare LF, before (1652 CRLF) and after (1724 CRLF).
- Bytes 32185 → 33598.
- Tab structure matches siblings exactly (2-tab quest object, 3-tab fields, 4/5-tab nested
  PlayerSpells/SkillsLevel). SkillsLevel + PlayerSpells blocks copied verbatim from the
  sibling nodes — never stripped, never hand-typed values changed.
- Braces balanced 298/298; brackets balanced 192/192.
- Insertion done via a byte-level Python write (Edit tool would not match on the mixed-depth
  array-close tail); verified anchor uniqueness before write.

## Crossing statement

`metallurgy.snbt`: full pairwise segment-intersection check over all 48 nodes' dependency
edges → **0 crossings total** (0 involving the new nodes). M1 continues the existing
horizontal tank spur at y=-4.0 (x 6.5→8.0, stopping left of the 940F→9434 vertical at
x≈9.0); M2 drops vertically at x=8.0 (y -4.0→-5.5) into clear space. The original plan's
M2 at (9.5,-4.0) WOULD have crossed the 940F(9.05,-3.0)→9434(9.0,-4.25) line; re-laid M2 to
(8.0,-5.5) to keep the layout crossing-free.

## Handoff (for LEDGER / 02c)

- **02c:** the IR IE multiblock chapter entry should depend on M2 `2902E58DB70F9451`
  (mb_crusher pointer) for foundation→fleet continuity. Not authored here (cross-file).
- **Ledger note:** M1 substitution (fluid_pump→pipe_valve, age-discipline) and M3 drop
  (blueprint duplicate) should be recorded so 02c does not re-raise them. metallurgy node
  count 46 → 48 (+2, not +3).
