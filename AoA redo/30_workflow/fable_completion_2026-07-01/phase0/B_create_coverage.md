# Audit B — Create machine coverage reconciliation

Audit only. No files edited outside phase0/. No git. All findings carry a proof command + file.
Date: 2026-07-02. Pack root relative paths.

## Method / proof commands

- Installed jars: `ls mods/ | grep -iE 'create'` plus mod-id extraction from
  `META-INF/neoforge.mods.toml` for ambiguously-named jars.
- Quest coverage: Python pass over `config/ftbquests/quests/chapters/*.snbt` counting
  `item: { ... id: "<ns>:..." }` in TASK context and `type: "advancement"` blocks,
  bucketed per namespace per chapter (script run inline; see counts below).
- Gating: `grep -rnE '"<ns>:...", *"(item|block_item)"'` over
  `kubejs/server_scripts/aoa_astages_*.js`.
- Docs: `AoA redo/40_create_addons/*.md` (21 per-mod docs + INDEX.md), which are
  jar-verified but PREDATE the Phase 1/2/4 quest rollout.

---

## 1. Installed Create-family jars (verified in `mods/`)

Player-content add-ons (26 jars):

| Jar | Namespace | Role (doc) |
|---|---|---|
| create-1.21.1-6.0.10.jar | `create` | spine |
| createaddition-1.6.0.jar | `createaddition` | support |
| createdieselgenerators-1.21.1-1.3.14.jar | `createdieselgenerators` | spine (IR) |
| create-stuff-additions1.21.1_v2.1.4a.jar | `create_sa` | support |
| create-aeronautics-bundled-1.21.1-1.3.0.jar | `aeronautics`(+`simulated`/`offroad`) | world/flight |
| create-integrated-farming-1.2.6.jar | `create_integrated_farming` | compat |
| create-new-age-1.2.0+neoforge.jar | `create_new_age` | support |
| createpropulsion-1.1.4.jar | `createpropulsion` | support (flight) |
| create_furnitures-1.1.2.jar | `create_furnitures` | flavor/decor |
| createrailwaysnavigator-...-0.9.1.jar | `createrailwaysnavigator` | utility |
| powergrid... (bundled/data) | `powergrid` | support |
| create-confectionery1.21.1_v1.1.3b.jar | `create_confectionery` | flavor |
| create_cold_sweat-1.1.2.jar | `create_cold_sweat` | compat (0 items) |
| sliceanddice... | `sliceanddice` | support |
| createmetalwork-2.0.0.jar | `createmetalwork` | support |
| createnuclear-1.3.2-beta.3.jar | `createnuclear` | spine (Atomic) |
| alloyed-3.0.6... | `alloyed` | support |
| create_ultimate_factory-2.2.4.jar | `create_ultimate_factory` | support (data-only, no items) |
| createoreexcavation-1.21-1.6.8.jar | `createoreexcavation` | support |
| create_aquatic_ambitions-1.21.1-2.0.2.jar | `create_aquatic_ambitions` | support |

Out-of-scope Create-family jars (decor/perf/compat/tooling, NOT player-progression;
mod ids confirmed via toml): `create_dragons_plus` (CreateDragonsPlus), `createdeco`,
`createframed`, `createbetterfps`, `kubejs-create`, `emi_create_schematics`,
`createoritechcompat`, `createaddoncompatibility`, `create_otbwg_compat`. These
correctly have zero quest coverage and need none.

---

## 2. CURRENT quest coverage vs docs (the delta)

Task-item id counts per namespace per chapter (current on-disk state):

| Namespace | Task items | Chapters (count) | Doc verdict | Delta |
|---|---|---|---|---|
| `create` | 80 | m1_first_mill(54), ren_second_mill_steam_rail_logistics(17), ir_create_industrial_addons(3), ren_nether_threshold(3), ir_power_motion(1), metallurgy(1), ren_observation(1) | "trains + 6.0 factory thin" | **STALE — Second Mill chapter now covers steam/trains/factory logistics (17 ids incl. packager, stock_link, stock_ticker, factory_gauge, frogport, steam_engine, track/station/bogeys/signals)** |
| `createaddition` | 18 | ir_power_motion_and_grid(14), ir_create_industrial_addons(3), m1_first_mill(1) | "~75-80% open" | Partially closed — IR power/current rungs now present |
| `createdieselgenerators` | 8 | ir_create_industrial_addons(7), g5_empire_of_iron(1) | "fuel-tier gap" | Roughly matches doc |
| `create_new_age` | 22 | ir_create_industrial_addons(14), at1_nuclear_dawn(8) | "~2/3 quested; entry rung thin" | Matches doc |
| `powergrid` | 17 | ir_power_motion_and_grid(17) | "full IR chapter" | Matches |
| `createnuclear` | 14 | at1_nuclear_dawn(14) | "fully quested" | Matches |
| `create_aquatic_ambitions` | 7 | g6_circuits_and_current(7) | "4 optional g6 nodes" | Matches (shallow, intentional) |
| `createoreexcavation` | 5 | ir_create_industrial_addons(5) | "fully quested" | Matches |
| `alloyed` | 5 | m1_first_mill(5): forge, steel_pickaxe, steel_chestplate, steel_sheet, bronze_bell | "ZERO quested" | **STALE — Phase 4 landed Medieval beats** |
| `sliceanddice` | 3 | m3_relics_and_burrows(3): slicer, sprinkler, fertilizer_bucket | "ZERO quested" | **STALE — Phase 4 landed** |
| `create_integrated_farming` | 2 | m3_relics_and_burrows(2) | "2 item tasks" | Matches (mechanics still untaught) |
| `createmetalwork` | 2 | ir_create_industrial_addons(2) | "ZERO quested" | **STALE — 2 nodes now exist** |
| `createrailwaysnavigator` | 2 | ren_second_mill_steam_rail_logistics(2) | "ZERO quested" | **STALE — support tail on trains line** |
| `createpropulsion` | 1 | g5_empire_of_iron(1): coral_generator (optional) | "1 optional quested" | Matches |
| `create_furnitures` | 1 | ir_create_industrial_addons(1) | "ZERO quested" | Minor — 1 flavor node exists |
| `create_confectionery` | 1 | ir_create_industrial_addons(1) | "ZERO quested" | Minor — 1 flavor node exists |
| `create_sa` | **0** | — | "ZERO quested" | Still zero (see §3) |
| `aeronautics`/`simulated`/`offroad` | **0** | — | "ZERO quested" | Still zero — INTENTIONAL (see §4) |
| `create_cold_sweat` | 0 | — | "0 questable items" | Correct — nothing to quest |
| `create_ultimate_factory` | 0 | — | "no ownable items" | Correct — data-only, nothing to quest |

Net: several "0 quested" doc verdicts are now stale. The Phase 1/2/4 rollout is
confirmed on disk:
- **Phase 1 (Second Mill / Renaissance):** `ren_second_mill_steam_rail_logistics.snbt`
  carries the Create 6.0 factory-logistics + trains + steam content that the doc
  called "the single biggest content gap."
- **Phase 2 (IR entry rungs):** `createaddition` (14 in ir_power_motion) and
  `create_new_age` (14 in ir_create_industrial_addons) electricity rungs present.
- **Phase 4 (Medieval beats):** `alloyed` (5, m1) + `sliceanddice` (3, m3) landed as
  additive optional nodes.

---

## 3. create_sa (Create Stuff & Additions) — still zero-coverage, mostly ungated

- Chapters: `grep -rniE 'create_sa|createstuff' config/ftbquests/quests/chapters/` = **0**
  (all matches were `kubejs/data/create_sa/recipe/*` JSON, not quests; the "simulated"
  hydroponic false-match was excluded as instructed).
- Gating: exactly ONE item locked —
  `aoa_astages_01_item_restrictions.js:666  ["industrial_revolution", "create_sa:drone_controller", "item"]`.
  All power-gear left ungated by explicit design comment
  `aoa_astages_01g_create_family.js:14  // create_sa power-gear (wearables, different axis) left ungated.`
- Verdict: create_sa is a real GAP — a full engines/jetpack/exoskeleton questline
  (doc-recommended home = the_renaissance) does not exist. Copper tier is removed by
  `early_overgeared_progression_cleanup.js` (per doc), so any node must start at
  Andesite/Brass tier. This is the largest single unquested content island.

## 4. Aeronautics + Propulsion flight — intentionally ungated AND unquested

- `grep -rniE '"aeronautics:' kubejs/server_scripts/aoa_astages_*.js` = **0** locks.
  Only `createpropulsion:coral_generator` (gilded_age) and two propulsion ORE ids are
  gated; the flight physics fleet itself is free.
- Per stated user decision, free flight is a selling point of the pack. **Do NOT
  recommend gating or questing aeronautics/propulsion flight.** Excluded from all gap
  math below. The lone `createpropulsion:coral_generator` optional node in
  `g5_empire_of_iron.snbt` is the only intentional touchpoint and is fine as-is.

---

## 5. Machine / major-item classification

QUESTED (representative, current disk): base Create fundamentals + trains + factory
logistics (m1, ren_second_mill), createaddition IR power, powergrid chapter,
create_new_age electric + thorium, createnuclear reactor chain, createoreexcavation,
create_aquatic_ambitions g6, createdieselgenerators IR, alloyed forge/steel/bell,
sliceanddice slicer/sprinkler, create_integrated_farming roost/net.

INTENTIONALLY DEFERRED per doc / user call: aeronautics+propulsion flight (free,
ungated — user decision); create_cold_sweat (0 questable items); create_ultimate_factory
(data-only, no ownable namespace items); create_furnitures/create_confectionery beyond
1 flavor node each (flavor tier, keep to 1-2 optional nodes, never a chapter).

GAP (real, questable, currently uncovered):
1. **create_sa engines → jetpack/exoskeleton line** (0 quested; Renaissance home).
2. **createmetalwork crush→melt→compact molten yield loop** (mechanic untaught; only
   2 item stubs exist; the signature "12 mB pinch doubles andesite→andesite_alloy"
   trick and molten-pour alloying are the teachable payoff).
3. **createaddition wire/rod/sheet/spool chain + low-vs-high current distinction**
   (~partial; the low-vs-high current wire confusion is the #1 new-player trap, no
   explicit teaching node).
4. **create_new_age entry electricity rung** (generator coil eats SU without spinning —
   under-explained; overcharged-material subsystem open).
5. **create_integrated_farming automation MECHANICS** (roost feed loop + moving Fishing
   Net contraption untaught even though 2 item tasks exist).

---

## 6. FOMO lens — showpiece items with no quest (unique mechanics, not decor/variants/ingots)

All ids doc-verified against jars in `AoA redo/40_create_addons/`.

**create_sa (Renaissance):**
1. `create_sa:brass_jetpack_chestplate` — powered flight wearable (top functional tier).
2. `create_sa:brass_exoskeleton_chestplate` — stat-armor with energy drain (Haste+Strength).
3. `create_sa:steam_engine` / `create_sa:heat_engine` / `create_sa:hydraulic_engine` —
   sequenced-assembly engine gate items (the whole gear line hangs off these).
4. `create_sa:grapple` — swing/boost movement toy (unique traversal mechanic).
5. `create_sa:portable_drill` / `create_sa:flamethrower` — powered handheld tools.

**createmetalwork (IR):**
1. `createmetalwork:molten_iron_bucket` (or the molten fluid loop node) — the crush→melt→
   compact 2:1 yield loop, the entire point of the mod.
2. Molten-pour alloying (brass 4-ingot pour; andesite_alloy 12 mB doubling trick).

**create_new_age (IR/Atomic):**
1. `create_new_age:energiser` — overcharged-material subsystem showpiece.
2. Generator coil + magnet electricity entry (mechanic, not currently a discrete node).

**createaddition (IR):**
1. Low-current vs high-current wire/connector distinction — a teaching gap, not a decor item.

**createrailwaysnavigator (Renaissance):**
1. `createrailwaysnavigator` DB-Navigator route-search over live train network (2 nodes
   exist on the trains line; deeper display/route mechanics still a light FOMO item —
   support tail only, do NOT expand to a chapter).

NOTE (rule-trap, do not author as tasks): Metalwork/createaddition/new_age outputs are
frequently `minecraft:` vanilla items (ingots, experience_bottle, enchanted_golden_apple)
which can never be task items — quest the machine or the mod-namespaced intermediate.

---

## 7. Summary counts

- Create-family player-content namespaces installed: 20 (excl. 9 decor/perf/tooling).
- Namespaces with quest coverage: 16. With zero coverage: 4
  (`create_sa`, `aeronautics`, `create_cold_sweat`, `create_ultimate_factory`);
  of those, only `create_sa` is a REAL gap (aeronautics intentional; the other two
  have no questable items).
- Stale doc verdicts corrected: 6 (`create` trains/factory, `alloyed`, `sliceanddice`,
  `createmetalwork`, `createrailwaysnavigator`, plus `create_furnitures`/`create_confectionery`
  minor).
- Real questable GAPs (severity HYGIENE/CANON — coverage completeness, no softlocks):
  **5** (create_sa line; metalwork molten loop; createaddition current distinction;
  new_age entry rung; integrated_farming mechanics).
- Age-discipline: no cross-age inversions found in Create coverage; gates match doc
  baseline. No SOFTLOCK or BROKEN findings.
