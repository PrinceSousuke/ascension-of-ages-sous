# Create Tutorial & Motivating Questline — Design

Date: 2026-07-01
Branch: quest-prose-cc1-cc2
Pack: NeoForge 1.21.1, CurseForge. Quest layer: FTB Quests.
Status: DESIGN ONLY. No quest files edited by this document. This is the
implementation brief for a later authoring pass.

Every item id in this document was jar-verified on 2026-07-01 against the mods in
`mods/` (see the verification appendix). The research this design rests on lives
in `AoA redo/40_create_addons/` (`INDEX.md` + one doc per add-on); read the
specific add-on doc before authoring its nodes.

---

## 0. Goal and scope

A brand-new Create player starts at zero and is carried, age by age, from raw
rotation to advanced systems. Every mechanic is taught before it is needed. Every
add-on enters only where it is legal on the 8-age ladder, and only after its
prerequisite base-Create mechanic is taught. Accuracy is paramount because this
drives player-facing quest text, and Create/CAA quest prose must be mechanically
correct.

The 8 ordered ages (exact ids): `dark_ages`, `medieval_times`, `the_renaissance`,
`industrial_revolution`, `gilded_age`, `atomic`, `otherworldly`, `ascension`. No
Create content is legal in `dark_ages` (survival-only). Base Create hands off to
non-Create spines by `otherworldly`/`ascension`; do not stretch a Create add-on
into those ages for coverage's sake.

**Coordination.** The ocean "Living Harvest" branch, including its two Create:
Aquatic Ambitions g6 nodes, is being implemented separately per
`docs/superpowers/specs/2026-07-01-ocean-living-harvest-design.md`. This design
does NOT re-plan or duplicate Aquatic Ambitions. It references it and focuses
elsewhere. Where a fluid/oil or ocean touchpoint overlaps, this doc defers to the
ocean spec as the owner.

**The one rule that recurs.** Create processing (milling, crushing, splashing,
blasting, smelting) and most add-on recipes OUTPUT vanilla `minecraft:` items
(nuggets, dust, ingots, flint, egg, bucket, experience_bottle, enchanted_golden_
apple, trident, iron_nugget, netherite_ingot, planks, sticks, dyes, end_stone…).
A `minecraft:` item can NEVER be a quest task item. Quest the machine, or a
mod-namespaced intermediate. Every task in this doc is a mod-namespaced id, and
each add-on section calls out its specific vanilla-output trap.

---

## 1. Fundamentals ladder (base Create)

This is the teaching spine. Each rung is a prerequisite for the next AND for the
add-ons that hook off it. The Medieval portion mostly EXISTS in
`chapters/m1_first_mill.snbt` (id group `508B59840C508057`, "The First Mill",
`medieval_times`), which already covers the base kinetics and andesite processing
well. The Renaissance tail is the biggest gap in the whole pack.

Teaching order (rungs 1–8 Medieval, 9–12 Renaissance):

1. **Rotation + Stress/SU.** First SU source (Water Wheel / Windmill Bearing +
   sails / Hand Crank). Teach that power has speed (RPM) AND stress (SU), and both
   are network-wide: over-consume SU and the whole network stops. Hand out
   `create:goggles` and `create:stressometer` (and `create:speedometer`).
2. **Rotation grammar.** `create:shaft`, `create:cogwheel`,
   `create:large_cogwheel` (ratio change), `create:gearbox` (90°),
   `create:gearshift` (reverse on redstone), `create:clutch` (cut on redstone),
   `create:encased_chain_drive` / `create:adjustable_chain_gearshift`,
   `create:rotation_speed_controller`. Point to Ponder (press W) per block rather
   than re-explaining every one.
3. **Processing.** Andesite Alloy via `create:mechanical_mixer` + `create:basin`
   (the gateway item); then `create:millstone` (cheap, single input) ->
   `create:crushing_wheel` (pair, ore doubling) -> `create:mechanical_press` +
   basin (sheets/compacting). Then the **Encased Fan** and its FOUR catalysts,
   which is the biggest new-player "aha" and failure point: `create:encased_fan`
   over lava = blasting, over fire = smoking, over flowing water = splashing, over
   soul fire = haunting. Teach that fan SPEED sets RANGE, not throughput, and that
   the fan needs the RIGHT block behind it — a fan alone smelts nothing.
4. **Logistics.** `create:belt` (via `create:belt_connector`), `create:chute`,
   `create:andesite_funnel` / `create:brass_funnel`, `create:depot`,
   `create:brass_tunnel`, `create:filter`; then `create:deployer` and
   `create:mechanical_crafter` as the automation payoff.
5. **Fluids.** `create:mechanical_pump` + `create:fluid_pipe` + `create:fluid_tank`
   + `create:spout` (filling) + `create:item_drain` (emptying).
6. **Contraptions.** `create:super_glue` / `create:linear_chassis` /
   `create:mechanical_piston` / `create:mechanical_bearing` / `create:rope_pulley`
   / `create:cart_assembler`.
7. **Sequenced Assembly.** `create:sequenced_assembly` -> `create:precision_
   mechanism` as the Medieval capstone (deploy/press/spout loop on a belt).
8. **Schematics (optional polish).** `create:schematic_and_quill` ->
   `create:schematicannon` end-to-end. The quill is quested; the full capture ->
   cannon -> auto-build workflow is not taught as a line. Optional depth, not spine.

### What already exists vs what to add (Medieval)

`m1_first_mill` already quests, in order: `water_wheel` -> `andesite_alloy` ->
`shaft` -> `wrench` -> `hand_crank` -> `windmill_bearing` + sails ->
`cogwheel`/`large_cogwheel` -> `gearbox`/`gearshift`/`clutch` -> chain drives ->
`goggles`/`speedometer`/`rotation_speed_controller` -> `millstone` ->
`mechanical_press`+`basin` -> `encased_fan` -> belts/chute/depot/funnel/filter ->
`portable_storage_interface` -> fluid pipe/tank/pump -> super glue/chassis/piston/
bearing/rope pulley/cart assembler -> harvester/saw/plough -> schematic_and_quill
-> brass_casing/deployer/brass_funnel/brass_tunnel/mechanical_crafter/sequenced_
gearshift/crushing_wheel/flywheel/electron_tube/rose_quartz/mechanical_arm/
clockwork_bearing.

The base ladder is therefore **already well authored through rung 7.** The
Medieval work is polish, not new chapters:

- **Add explicit stress teaching** if not already present: a short prose beat on
  the existing goggles/stressometer node that over-stress stops the whole network,
  and that fan speed = range not throughput. Verify against the live node text
  before adding; do not duplicate.
- **Encased Fan four-catalyst node**: confirm the existing `encased_fan` node
  teaches all four catalysts (lava/fire/water/soul fire). If it only mentions one,
  extend the prose. This is the single highest-value teaching correction in
  Medieval. Do NOT split it into four nodes; one node, four catalysts, point to
  Ponder.

No new Medieval base-Create chapter is needed. Medieval add-on hooks (§3) attach
to `m1_first_mill` or adjacent Medieval chapters.

---

## 2. The Renaissance tail (the biggest gap)

Base Create's Renaissance-locked content — steam, trains, and the Create 6.0
factory logistics system — is nearly untaught. Grep confirms: the ONLY
Renaissance `create:` node touching steam is a single isolated OPTIONAL
`create:steam_engine` item task buried in `ren_observation_experimentation.snbt`
(id `0B031080000000D2`), gated on a magic skill level, not a steam bridge. There
is ZERO trains content and ZERO factory-logistics content anywhere in the book
(verified: no `create:track`, `track_station`, `packager`, `stock_ticker`,
`factory_gauge`, `frogport`, bogey references in any chapter). This is Create 6's
flagship system and it is invisible.

Proposal: **one new Renaissance chapter, "The Second Mill: Steam, Rail & Logistics"**
(working title), containing three tight branches off a shared steam-bridge root.
All items are Renaissance-legal (the whole train + factory-logistics family is
`the_renaissance`-locked in `aoa_astages_01g_create_family.js`; steam_engine and
the track family are Renaissance-locked in `aoa_astages_01_item_restrictions.js`).

Chapter age: `the_renaissance`. Reveal on the Renaissance entry gate like the
other Renaissance chapters (see §5). Required-vs-optional split below.

### 2A. Steam-engine bridge (root, required)

Teaches the jump off water wheels to real SU. Bundle the boiler concept into one
node, then the engine.

- Node **S1 — "Fire the Boiler"** (required). `create:blaze_burner` is already
  item-tasked in `ren_nether_threshold` (and is Medieval-legal), so S1 MUST NOT be a
  second `create:blaze_burner` item task. **Directive, not a suggestion:** author S1
  as a `check_quest` mirror keyed to the existing blaze-burner node, or as a
  prose-only teaching node that depends on it. Same discipline applied to the stray
  steam_engine node and the Rolling Mill dupe. Prose: a `create:fluid_tank` filled
  with water and heated by blaze burners becomes a boiler; the more burners and the
  taller the tank, the more steam power. Confirm against `ren_nether_threshold`
  (which quests `create:blaze_burner`/`empty_blaze_burner`/`blaze_cake`) before
  authoring so the check_quest points at the right existing node.
- Node **S2 — "Steam Power"** (required, chapter root proper). Task:
  `create:steam_engine`. Prose: a Steam Engine mounted on the boiler tank outputs
  far more SU than a water wheel, freeing large factories from sprawling wheels.
  Optional add: `create:steam_whistle` as a flavor sibling node (optional).
  NOTE: relocate/deprecate the stray magic-gated steam_engine node in
  `ren_observation_experimentation` OR leave it (first-placement-wins is this
  chapter). Recommend converting that stray node to a `check_quest` mirror so the
  same block is not double-item-tasked across two chapters. Flag for the authoring
  pass; do not silently delete an existing node.

S2 is the dependency root for both 2B and 2C.

### 2B. Trains chapter branch (required core, optional depth)

Teach the Renaissance "connect the colony" line. Track -> station -> bogeys ->
assemble -> signalling.

- Node **T1 — "Lay the Track"** (required). Task: `create:track`. Prose: place
  Train Track and pave curves; Create trains ride Create track, not vanilla rails.
- Node **T2 — "Build a Station"** (required). Task: `create:track_station`.
  Prose: a Station assembles and disassembles trains and issues schedules.
- Node **T3 — "Wheels on the Rail"** (required). Task: `create:small_bogey`
  (bundle `create:large_bogey` into the same node as a second required item, or a
  sibling optional). Prose: bogeys are the train's wheels; place them on track
  under your carriage, then assemble at the station.
- Node **T4 — "Drive and Schedule"** (required). Task: `create:controls` (Train
  Controls seat) with `create:schedule` (Train Schedule item) bundled in the same
  node. Prose: sit in the Controls to drive manually, or write a Schedule to
  automate the route.
- Node **T5 — "Block Signalling"** (optional depth). Task: `create:track_signal`
  (bundle `create:track_observer`). Prose: signals stop trains from colliding on
  shared track; observers detect passing trains. Optional because a single-train
  line does not strictly need it.

Rule-trap safety: every train id above is a real `create:` block/item, jar-
verified. No vanilla-output trap in this branch (trains produce no items).

**Scope note (Steam'n'Rails / `railways`).** Steam'n'Rails IS installed
(`railways-0.3.0-alpha.2+neoforge-mc1.21.1.jar`) and its content is already
Renaissance-gated in `aoa_astages_01g_create_family.js` (`semaphore`, `handcar`,
`link_and_pin`, `portable_fuel_interface`, lines 120-123), plus a
`train_station_clock` item lock. This design teaches BASE-Create trains only and
deliberately leaves the `railways:` overlay out of scope for this pass, parallel to
how Aquatic Ambitions is deferred to the ocean spec. To avoid a second uncoordinated
rail authoring pass, either (a) hold `railways:` for a dedicated follow-up, or (b)
fold a single optional node, `railways:handcar` (jar-verified), into the bottom of
the Trains column so the two rail mods are coordinated rather than colliding later.
Do NOT open a separate Steam'n'Rails chapter.

### 2C. Factory Logistics chapter branch (Create 6.0 flagship, required core)

Teach AFTER belts/funnels (Medieval) so the player appreciates the abstraction.
The recommended teaching order matches Create 6's own dependency chain:
packager -> stock link + stock ticker -> factory gauge -> frogport.

- Node **L1 — "Package It"** (required). Task: `create:packager`. Prose: a
  Packager wraps a stack into a shippable Package entity — the atom of the
  Logistics Network. Optional sibling: `create:repackager` (optional).
- Node **L2 — "Request from the Network"** (required). Task: `create:stock_link`
  with `create:stock_ticker` bundled in one node. Prose: link inventories with a
  Stock Link, then request items from the whole network through a Stock Ticker's
  shopping list. This is the "order from anywhere" beat.
- Node **L3 — "Auto-Restock"** (required, the flagship payoff). Task:
  `create:factory_gauge`. Prose: a Factory Gauge watches a linked inventory and
  keeps it stocked at a target level, dispatching crafting orders through the
  network automatically. This is the automation backbone of Create 6 — the "why
  this system exists" node.
- Node **L4 — "Deliver by Air"** (optional depth). Task: `create:package_frogport`
  (bundle `create:redstone_requester` as optional). Prose: Frogports launch and
  receive Packages between distant network nodes; a Redstone Requester triggers an
  order on a signal. Optional because L1–L3 already close the loop.

Rule-trap safety: all factory-logistics ids are real `create:` blocks, jar-
verified. Packages are entities, not items — task the machines, never a "package."

### 2D. QoL polish (optional, small)

`create:elevator_pulley` (Renaissance-locked contraption elevators),
`create:gantry_shaft`/`create:gantry_carriage` (programmable positioning),
`create:display_board`/`create:display_link`/`create:nixie_tube` (signage). Keep
to at most 1–2 optional nodes total; do not enumerate. Recommended: one optional
"Display Board" node (`create:display_board`) that also seats the Railways
Navigator tail (§3, Renaissance flavor). Do not build a signage sub-chapter.

---

## 3. Add-on hooks mapped to the age ladder

Each add-on enters only where its prerequisite base-Create mechanic is taught and
where AStages makes it legal. Task ids below are all jar-verified. Each entry
names the vanilla-output trap to avoid.

### Medieval Times (`medieval_times`)

Base Create fundamentals live here. Three support add-ons are legal and currently
under- or un-taught. Attach as small branches to `m1_first_mill` or adjacent
Medieval chapters (`m3_relics_and_burrows` already hosts the CIF acquire tasks and
Farmer's Delight content).

- **Create: Alloyed (`alloyed`)** — Alloy Forge + Steel gear. Legal Medieval
  (Alloy Forge is iron+furnace+deepslate; Steel is iron+coal+fire charge). 1 early
  metallurgy beat: build the Forge, then a steel tool set.
  - Node: `alloyed:forge` (required-ish anchor). Prose: a fuel-burning GUI station
    (input/fuel/output slots), NOT a Create kinetic machine and NOT a furnace.
  - Node: `alloyed:steel_pickaxe` (or `steel_sword`/`steel_chestplate`). Genuine
    `alloyed:` items, safe task targets.
  - Optional flavor: `alloyed:bronze_bell` (wrench-tuned, Deployer-rung redstone
    instrument).
  - **Trap:** the Alloy Forge and Create mixing routes YIELD `alltheores:steel_
    ingot`/`bronze_ingot` (swapped by `ato_material_conflict_cleanup.js`). NEVER
    quest `alloyed:steel_ingot`/`bronze_ingot`/blocks/nuggets. Quest the Forge,
    the steel TOOLS/armor, sheets (`alloyed:steel_sheet`), or the bell. Bronze
    recipe with Create installed uses zinc nugget + `create:cinder_flour`, not
    iron nuggets — author prose accordingly.
  - The Create automation route (mixing/pressing) re-surfaces at IR as optional
    decoration/automation; do not force it into Medieval.
- **Create Slice & Dice (`sliceanddice`)** — Slicer (gated `medieval_times`). One
  clean legal item task, currently zero quested.
  - Node: `sliceanddice:slicer` (anchor). Prose: the mixer/press-family machine
    that automates Farmer's Delight cutting-board recipes; give it rotation and
    right-click a knife or axe into it.
  - Optional depth: `sliceanddice:fertilizer_bucket` + Sprinkler
    (`sliceanddice:sprinkler`) fluid loop (compost + water -> Liquid Fertilizer ->
    spray a farm or Fill `farmersdelight:rich_soil`).
  - **Trap:** the Slicer runs the whole FD cutting set, whose OUTPUTS are
    frequently `minecraft:` (planks, sticks, dyes, string). Never task "produce X
    with the Slicer" where X is vanilla. Task the Slicer block, the fertilizer
    bucket, or an FD-namespaced output (`farmersdelight:rich_soil`).
- **Create: Integrated Farming (`create_integrated_farming`)** — Roost + Fishing
  Net (both gated `medieval_times`). The 2 acquire tasks EXIST in
  `m3_relics_and_burrows` (`roost` id `4B2D3C5E8F7B000B`, `fishing_net` id
  `4B2D3C5E8F7B000A`); the automation MECHANICS are untaught. Add prose/loop, do
  not re-add the acquire tasks.
  - Extend the existing roost node prose: place the Roost, capture a chicken
    (right-click bird / Lead / spawner), then FEED it — seeds via a belt, or pipe
    `createaddition:seed_oil` into a Spout over it. Egg farm that runs itself.
  - Extend the existing fishing_net node prose: the Fishing Net ONLY fishes while
    MOVING as part of a Create contraption (gantry/cart/rotating). A static Net
    does nothing — teach this explicitly or it reads as broken.
  - **Trap:** the Chicken Roost's product is `minecraft:egg`. Never quest the egg.
    Quest the Roost block (already done) or a downstream automation goal. Do NOT
    quest the Lava Fishing Net (uncraftable here) or duck/goose roosts (dormant,
    loot emptied).
- **Create Crafts & Additions Rolling Mill (`createaddition:rolling_mill`)** —
  kinetic-only, already quested in `m1_first_mill` (id `7A1F050000000205`) and
  correctly LEFT UNGATED. This is the Medieval toe-hold that makes wires exist for
  IR. **Known duplicate:** the Rolling Mill is ALSO tasked in
  `ir_power_motion_and_grid.snbt`. First-placement-wins is Medieval. The IR
  duplicate should be reviewed/removed or converted to a `check_quest` mirror in
  the IR authoring pass (flag, not this doc's job).

### Industrial Revolution (`industrial_revolution`)

The electricity/power convergence age. Most of this is quested; the gaps are the
material/fuel/entry-rung micro-layers. IR already has dedicated chapters:
`ir_power_motion_and_grid` (Power Grid + CAA machines), `ir_create_industrial_
addons` (CAA electric + New Age electric + Diesel Generators + Ore Excavation).
Add missing entry rungs INTO those chapters; do not create new IR Create chapters.

- **Create Crafts & Additions (`createaddition`)** — the FE<->rotation bridge.
  Machine spine (~11 blocks) is quested in `ir_power_motion_and_grid` /
  `ir_create_industrial_addons`. ~75–80% of the material/fuel layer is unquested.
  The single biggest new-player confusion point is **low-vs-high current wire**,
  which deserves an explicit node.
  - Node (required, insert before the big-machine nodes): **"Low vs High Current."**
    Task: `createaddition:copper_spool` (bundle a `createaddition:connector`).
    Prose: a Copper Spool + small Connector = LOW current (up to 4 links); Gold or
    Electrum spool + Large Connector = HIGH current (up to 6). A big machine off
    copper gives "requires a high current wire." Wrench cycles Push/Pull/None.
  - Optional depth material line: `createaddition:electrum_ingot` /
    `createaddition:electrum_spool` (high-current path), `createaddition:capacitor`.
    Silver IS available at IR: `alltheores:silver_ingot` and the whole silver line
    are gated at `the_renaissance` in `aoa_astages_01_item_restrictions.js` (lines
    436-529), which is strictly before `industrial_revolution`, so `c:ingots/silver`
    resolves and the electrum/high-current path does NOT stall. Keep electrum as
    optional depth for PACING (copper low-current is enough to start), not because
    of a missing material.
  - Optional depth fuel loop: `createaddition:biomass` ->
    `createaddition:liquid_blaze_burner` + `createaddition:straw` (renewable Create
    fuel). Not spine.
  - Existing machine tasks to LEAVE ALONE: `alternator`, `electric_motor`,
    `connector`, `large_connector`, `modular_accumulator`, `tesla_coil`,
    `portable_energy_interface`, `digital_adapter`, `redstone_relay`,
    `small_light_connector` (already quested across the two IR chapters).
  - **Trap:** `charging/channeling` outputs `minecraft:enchanted_book`;
    `filling/cake` outputs `minecraft:cake`; deoxidize recipes output vanilla
    copper; electrify-gold touches vanilla gold. Never task those. Also never task
    `createaddition:creative_energy` (creative) or the deprecated single
    `createaddition:accumulator` (use `modular_accumulator`).
- **Create: New Age (`create_new_age`)** electric tier — ~2/3 quested in
  `ir_create_industrial_addons` (reinforced motor/energiser, netherite magnet,
  generator coil, carbon brushes, heat pipe/heater, connectors, magnets). The
  FOUNDATIONAL entry rung is under-taught: how you FIRST make electricity.
  - **Already item-tasked in `ir_create_industrial_addons` — do NOT re-task these
    (grep-confirmed 2026-07-01):** `generator_coil` (id `4954082000000014`),
    `carbon_brushes` (id `4954082000000015`), `redstone_magnet` (id
    `4954082000000018`), `electrical_connector` (id `495408200000001A`). First
    placement wins; a second item task on any of them is the exact duplicate defect
    this doc flags for the Rolling Mill. Teach these mechanics by depending on the
    EXISTING nodes, not by re-tasking.
  - **Genuinely un-quested at IR — safe to task (grep-confirmed 0 occurrences
    anywhere in the book):** `create_new_age:basic_motor`, `create_new_age:basic_
    energiser`, `create_new_age:copper_wire`. Build the entry rungs around these.
  - Node (required, insert as the electricity-entry rung BEFORE the reinforced-tier
    nodes): **"First Electricity."** This teaches generation but MUST NOT re-task
    `generator_coil`/`carbon_brushes`/`redstone_magnet`. Author it as a
    `check_quest` mirror keyed to the existing generator-coil node (id
    `4954082000000014`), or as a prose-teaching node that depends on that node.
    Prose (must be mechanically exact): a Generator Coil generates electricity ONLY
    when rotated by Create kinetics AND ringed by magnets; it EATS SU and does NOT
    spin anything. Carbon Brushes collect the electricity. Stronger magnets = more
    SU-to-electricity efficiency (redstone -> layered -> netherite) but higher SU
    draw.
  - Node (required, "Move the Power"): task `create_new_age:copper_wire` only
    (un-quested). Do NOT re-task `electrical_connector` — depend on its existing
    node (id `495408200000001A`) instead. Prose: Inert vs Pull mode, max wire
    length.
  - Node (required, "Use the Power"): `create_new_age:basic_motor` +
    `create_new_age:basic_energiser` (both un-quested, safe to bundle). Prose: motor
    turns electricity back to rotation (fixed SU, wrench speed); the Energiser +
    `create_new_age:energising` category makes overcharged materials. Mention (do
    NOT task) that a full energising line can even brew experience bottles and
    enchanted golden apples as the payoff.
  - **Trap:** `energising/experience_bottle` outputs `minecraft:experience_bottle`;
    the enchanted_golden_apple sequence outputs `minecraft:enchanted_golden_apple`.
    Teach in prose, never task. Do NOT reference `esl:` (internal library).
  - **Do NOT duplicate** the Atomic thorium reactor chain — it is fully quested in
    `at1_nuclear_dawn` (see §5).
- **Create: Power Grid (`powergrid`)** — has a FULL dedicated IR chapter
  (`ir_power_motion_and_grid`, ~23 ids). LEAVE THE SPINE ALONE. Only the
  electronics micro-layer (resistors/tubes/CRT/punch cards) is open, and it is
  correctly optional depth. Do not add required nodes. If any polish: one optional
  "analog electronics" note pointing at the Circuit Design Table. Prose must never
  say Power Grid "generates FE" — the internal grid is analog volts/amps; FE
  appears only at the Device Connector and Portable Battery.
- **Create: Diesel Generators (`createdieselgenerators`)** — IR spine quested in
  `ir_create_industrial_addons` (pumpjack parts, distillation, modular engine,
  biodiesel). Gap: an explicit fuel-tier teaching node and the burner/basin
  mechanic.
  - Node (optional depth, "Fuel Tiers"): teach ethanol/plant oil = weak, biodiesel
    (plantoil + ethanol) = renewable sweet spot, diesel (crude) = best. Task:
    `createdieselgenerators:biodiesel_bucket` (already quested — verify, and if so
    convert this to prose on the existing node rather than a duplicate).
  - Optional: `createdieselgenerators:burner` + basin heat mechanic.
  - **Trap:** basin-fermenting outputs `minecraft:golden_apple`/`golden_carrot`/
    `magma_cream`/`fermented_spider_eye`; do not quest those. Do NOT re-author
    `createdieselgenerators:distillation_controller` — its recipe is overridden in
    `aoa_recipes_capstone_convergence.js`. The oil spine is owned by the oil-single-
    source system; defer to it. `huge_diesel_engine` graduates to Gilded (already
    quested in `g5_empire_of_iron`).
- **Create: Metalwork (`createmetalwork`)** — crush/melt/compact yield loop
  entirely untaught, UNGATED, 0 quested. Add a SMALL efficiency sub-branch inside
  the IR Create processing chapter (`ir_create_industrial_addons`), not its own
  chapter. **Anti-bloat cap: 2 nodes, not 4.** Ore doubling itself is already taught
  via crushing wheels in Medieval, so this branch teaches only the ONE new mechanic
  Metalwork adds — molten buffering/pouring for higher yield — plus its one
  distinctive payoff (netherite pour). Do NOT author a node per molten metal.
  - Node (teach the loop): `createmetalwork:molten_iron_bucket`. Prose: crush raw
    material -> heat-mix in a Basin to a molten fluid (buffered, 111 mB/ingot,
    pipeable) -> pour/compact back to ingots, more metal per ore than a furnace.
    This one node carries the whole crush-melt-pour teaching; the `crushed_andesite`/
    `crushed_netherite_scrap` items are prose steps, not their own nodes.
  - Node (the distinctive payoff, IR->Gilded seam): `createmetalwork:molten_
    netherite_bucket` (4 crushed gold + 4 crushed scrap -> 2 netherite via pour).
  - **Trap:** every ingot-from-compacting recipe outputs a `minecraft:` ingot
    (iron/copper/gold/netherite). NEVER task those. Use the `createmetalwork:`
    crushed items and molten buckets. Tin/bronze/steel molten are INERT here
    (`create_ironworks` not installed) — do not reference them.
- **Create Ore Excavation (`createoreexcavation`)** — FULLY quested at IR
  (`ir_create_industrial_addons`, vein finder -> sample drill -> drilling machine).
  LEAVE ALONE.
- **Optional flavor tier (1–2 optional nodes each, never a chapter):**
  - **Create: Confectionery (`create_confectionery`)** — one optional IR food
    branch off the Create factory chapter. Node: `create_confectionery:cocoa_powder`
    (Press+Crush chain), optional `caramel_bucket` -> `bar_of_caramel` ->
    `chocolate_candy`. Namespace is `create_confectionery` (underscore); the hint
    `createconfectionery` is WRONG. **Trap:** emptying recipes output
    `minecraft:bucket`/`glass_bottle`; ruby chocolate needs `minecraft:dragon_
    breath` (End access, Renaissance+, fine at IR). Keep off the required path.
  - **Create: New Furnitures (`create_furnitures`)** — one optional "workshop
    dressing" node. Task: `create_furnitures:brass_chair` or `andesite_table`
    (clean-named). Namespace `create_furnitures` (single underscore); the
    double-underscore `create__furnitures` lang keys are MCreator artifacts and do
    not resolve. No vanilla-output trap (all outputs are `create_furnitures:`
    blocks). Do NOT enumerate the 75 blocks or quest the unlocalized pillar
    segments.
  - **Create: Cold Sweat (`create_cold_sweat`)** — PROSE ONLY. Zero items, nothing
    questable. Fold one or two temperature tips onto existing IR Create heat
    quests: a lit blaze burner and a boiler radiate real body-temperature heat
    (scales smouldering -> seething), and hot fluid in pipes/tanks warms a room
    (cold fluid cools it). Never author a task for it; it has no ids.

### Gilded Age (`gilded_age`)

Flight and advanced branches. This is where the big motivating payoff lives, and
it is almost entirely unquested. Propose **one new Gilded chapter, "Take to the
Skies"** (working title), a support/flavor transport chapter — NOT a spine gate
(nothing else in the pack depends on flight). One tight chapter beats a per-block
tour. `g5_empire_of_iron` already hosts `huge_diesel_engine` and the single
optional `createpropulsion:coral_generator` node; the flight chapter is new.

**Gating prerequisite (RELEASE-BLOCKING; must land BEFORE any node is authored).**
The entire Aeronautics/Simulated/Offroad system and most of Create Propulsion are
currently UNGATED. Verified: `create_family.js` has no simulated/aeronautics/offroad
locks, and the only createpropulsion lock is `coral_generator` at `gilded_age`.
Until the companion AStages pass lands, every "Gilded" flight item is craftable from
world start (effectively `dark_ages`-legal) — a live day-one bypass and an age-tier
inversion in practice. **Phase 3 is blocked until every lock below exists at
`gilded_age` and is verified.** Do not author a single flight node before then.

Gating checklist (all at `gilded_age`, verify each after adding):
- `simulated:physics_assembler`
- the Simulated portable engines (`simulated:red_portable_engine` and siblings)
- `aeronautics:levitite_blend_bucket`
- `aeronautics:propeller_bearing`
- `offroad:wheel_mount`
- the createpropulsion thruster line (`createpropulsion:thruster`,
  `createpropulsion:ion_thruster`), its fuels (`createpropulsion:turpentine_bucket`),
  and the platinum-metal line (platinum ore is already Renaissance-gated; the metal
  line and thrusters are not)

This is a required companion change, not optional. If the locks are not authored and
verified first, do NOT ship the flight chapter.

- **Create: Aeronautics (`aeronautics` / `simulated` / `offroad`)** — the flight
  questline. NAMESPACE TRAP: the Physics Assembler, engines, controls, sensors are
  `simulated:`; flight bags/props/levitite are `aeronautics:`; wheels are
  `offroad:`. Verify every id's namespace (all below are jar-verified).
  - Node **F1 — "The Physics Assembler"** (required root). Task:
    `simulated:physics_assembler`. Prose: glue a platform, touch it with the
    Assembler, pull the lever to lift it into a live physics body (a Simulated
    Contraption with real mass/thrust/drag/buoyancy). Reward:
    `simulated:contraption_diagram` (visualizes forces).
  - Node **F2 — "Motive Power"** (required). Task:
    `simulated:red_portable_engine` (bundle `simulated:steering_wheel` +
    `simulated:throttle_lever`). Prose: on-board rotational power vs a stationary
    Create network.
  - Node **F3 — "Wheels First"** (required, easiest payoff). Task:
    `offroad:wheel_mount` (bundle `offroad:tire`). Prose: mount + tire + engine +
    steering = a car; low-risk physics intro before flight.
  - Node **F4 — "Balloon Flight"** (required). Task: `aeronautics:white_envelope`
    (bundle `aeronautics:adjustable_burner`). Prose: hot air in the envelope
    generates lift; the Hot Air Burner needs a fuel source.
  - Node **F5 — "Powered Flight"** (optional depth). Task:
    `aeronautics:propeller_bearing` (bundle `aeronautics:wooden_propeller`;
    optional `aeronautics:smart_propeller` auto-pitch). Prose: a bearing spun by
    Create rotation drives propellers for thrust.
  - Node **F6 — "The Airship" (capstone)** (required chapter capstone). Teach the
    levitite fluid loop: crush end_stone -> `aeronautics:end_stone_powder` ->
    heat-mix into `aeronautics:levitite_blend` -> pour/crystallize into
    `aeronautics:levitite`. Task: `aeronautics:levitite_blend_bucket` (the fluid
    step; levitite itself forms by in-world crystallization, NOT a crafting
    recipe, so do not task `aeronautics:levitite` as a craft). Prose: levitite is
    always-on lift; combine with envelope + propeller + engine + sensors for a
    self-lifting airship.
  - **Traps:** the CUF end_stone compat outputs `minecraft:end_stone` (renewable
    but vanilla — task `aeronautics:end_stone_powder`, never end_stone).
    `simulated:white_symmetric_sail` crafts into `create:white_sail` (task the
    symmetric sail, not white_sail). NEVER quest `simulated:absorber` (a broken
    placeholder that says "DOES NOT WORK"). Levitite is a crystallization, not a
    recipe. Flag `sable` physics cost for the performance pass.
- **Create Propulsion (`createpropulsion`)** — Gilded DEPTH inside the flight
  chapter, not its own gate. Short thruster mini-line.
  - Node (optional, "Turpentine Fuel"): teach crush spruce -> Pine Resin -> mix
    with water -> Turpentine. Task: `createpropulsion:turpentine_bucket`.
  - Node (optional, "First Thruster"): `createpropulsion:thruster` (fluid thruster,
    redstone 0–15 throttle, requireFuel). Mount on a Sable/Aeronautics contraption
    for force-at-point thrust.
  - Node (optional, capstone flavor): Coral Generator (existing g5 optional node,
    `createpropulsion:coral_generator`) -> FE -> `createpropulsion:ion_thruster`.
    Coral hazard warning belongs in prose.
  - **Trap:** do NOT quest bare platinum ingots/nuggets/sheets — quest the machines
    and fuels. Platinum ore is already Renaissance-gated; the platinum metal line
    and thrusters/fuels are ungated (flag for the AStages pass above). The
    `sequenced_assembly` folder ships empty — no sequenced recipe exists.
- **Create: Aquatic Ambitions (`create_aquatic_ambitions`)** — OWNED BY THE OCEAN
  SPEC. Do not plan or duplicate its g6 conduit-channeling branch here. Reference
  `docs/superpowers/specs/2026-07-01-ocean-living-harvest-design.md`.
- **Create: Diesel Generators `huge_diesel_engine`** — already quested in
  `g5_empire_of_iron` as the heavy 16384-SU generator. LEAVE ALONE.
- **Optional flavor:** none new at Gilded beyond the above.

### Atomic (`atomic`)

- **Create: Nuclear (`createnuclear`)** — FULLY quested in `at1_nuclear_dawn`
  (uranium refine -> enriching-fire fan -> reactor multiblock). LEAVE ALONE. Do
  NOT duplicate. The steel-mixing bypass is deliberately removed
  (`createnuclear_steel_removal.js`) — do not re-add.
- **Create: New Age thorium reactor** — FULLY quested in `at1_nuclear_dawn`
  (thorium ore -> ingot -> radioactive thorium -> nuclear fuel -> reactor blocks ->
  heat pump). LEAVE ALONE. The teaching that IS worth a prose check: the
  enriching-fire fan mechanic and the two always-true rules — "always sink the heat
  or the reactor melts down" and "radiation needs leather armor or full casing."
  If the existing nodes lack that prose, ADD it to the existing nodes; do not add
  new item tasks.
- **Create Ore Excavation, Cold Sweat** — no new Atomic Create content.

### Otherworldly / Ascension

No Create add-on anchors these ages. Base Create has handed off to non-Create
spines. Do not stretch any Create add-on into them for coverage.

---

## 4. Task-item verification table (per proposed task)

Every proposed TASK item, mod-namespaced, jar-verified 2026-07-01. Vanilla outputs
are listed as the trap, never as tasks.

| Age | Node | Task item (verified) | Vanilla-output trap to avoid |
|---|---|---|---|
| Med | Encased Fan | `create:encased_fan` (exists) | fan outputs vanilla nuggets/dust/flint — task machine |
| Med | Alloy Forge | `alloyed:forge` | `alloyed:steel_ingot`/`bronze_ingot` swap to `alltheores:` — task Forge/tools |
| Med | Steel gear | `alloyed:steel_pickaxe` / `steel_sword` / `steel_chestplate` / `steel_sheet` | (tools/sheets are genuine `alloyed:`) |
| Med | Bronze Bell | `alloyed:bronze_bell` | — |
| Med | Slicer | `sliceanddice:slicer` | FD cuts output `minecraft:` planks/sticks/dyes — task block |
| Med | Fertilizer | `sliceanddice:fertilizer_bucket`, `sliceanddice:sprinkler` | Filling outputs `farmersdelight:rich_soil` (legal) |
| Med | Roost (prose) | existing `create_integrated_farming:roost` node | roost yields `minecraft:egg` — never task egg |
| Med | Fishing Net (prose) | existing `create_integrated_farming:fishing_net` node | net = vanilla fishing pool |
| Med | Rolling Mill | `createaddition:rolling_mill` (already quested Med) | — (dedupe IR copy) |
| IR | Low/High Current | `createaddition:copper_spool`, `createaddition:connector` | `enchanted_book`/`cake`/vanilla copper from charging — task spool |
| IR | Electrum line | `createaddition:electrum_ingot`, `electrum_spool`, `capacitor` | needs `c:ingots/silver` — RESOLVED: silver is Renaissance-gated, available at IR |
| IR | Bio-fuel | `createaddition:biomass`, `liquid_blaze_burner`, `straw` | — |
| IR | First Electricity | check_quest mirror on existing `generator_coil` node (id `4954082000000014`) | generator_coil/carbon_brushes/redstone_magnet already tasked — do NOT re-task |
| IR | Move Power | `create_new_age:copper_wire` (un-quested) | `electrical_connector` already tasked (id `495408200000001A`) — depend, do NOT re-task |
| IR | Use Power | `create_new_age:basic_motor`, `basic_energiser` (both un-quested) | `experience_bottle`/`enchanted_golden_apple` — prose only |
| IR | Metalwork loop (2 nodes max) | `createmetalwork:molten_iron_bucket` | ingot-compacting = `minecraft:` ingots; crushed items are prose steps not nodes |
| IR | Netherite pour | `createmetalwork:molten_netherite_bucket` | never `minecraft:netherite_ingot` |
| IR | Fuel tiers (prose) | existing `createdieselgenerators:biodiesel_bucket` | golden_apple/carrot/magma_cream basin outputs |
| IR | Burner | `createdieselgenerators:burner` | — |
| IR | Confectionery | `create_confectionery:cocoa_powder`, `caramel_bucket`, `bar_of_caramel` | `minecraft:bucket`/`glass_bottle` empties; dragon_breath ruby |
| IR | Furniture | `create_furnitures:brass_chair` / `andesite_table` | none (all `create_furnitures:` outputs) |
| IR | Cold Sweat | NONE (prose only) | mod has zero items |
| Ren | Steam bridge | S1 = check_quest on existing `create:blaze_burner` node (no re-task); S2 = `create:steam_engine` (+ `steam_whistle` opt) | blaze_burner already tasked in `ren_nether_threshold` — do NOT re-task |
| Ren | Trains | `create:track`, `track_station`, `small_bogey`, `large_bogey`, `controls`, `schedule`, `track_signal`, `track_observer` | trains produce no items |
| Ren | Factory logistics | `create:packager`, `stock_link`, `stock_ticker`, `factory_gauge`, `package_frogport`, `redstone_requester`, `repackager` | packages are entities — task machines |
| Ren | QoL/signage | `create:display_board` (opt), `create:elevator_pulley` (opt) | — |
| Ren | Railways Navigator | `createrailwaysnavigator:navigator`, `advanced_display` | none (all CRN outputs modded); `navigator_lectern` has NO recipe — do not task |
| Gild | Physics Assembler | `simulated:physics_assembler` | — |
| Gild | Motive power | `simulated:red_portable_engine`, `steering_wheel`, `throttle_lever` | — |
| Gild | Wheels | `offroad:wheel_mount`, `offroad:tire` | — |
| Gild | Balloon | `aeronautics:white_envelope`, `adjustable_burner` | — |
| Gild | Propellers | `aeronautics:propeller_bearing`, `wooden_propeller`, `smart_propeller` | `simulated:white_symmetric_sail` -> `create:white_sail` |
| Gild | Airship | `aeronautics:levitite_blend_bucket` | CUF outputs `minecraft:end_stone`; `simulated:absorber` broken; levitite = crystallization not recipe |
| Gild | Thrusters | `createpropulsion:turpentine_bucket`, `thruster`, `coral_generator` (existing), `ion_thruster` | never bare platinum ingots/nuggets/sheets |

### Renaissance flavor tail (Railways Navigator)

`createrailwaysnavigator` (`the_renaissance`, utility) — a short QoL tail on the
trains branch (§2B), NOT its own chapter. 2 real task nodes max plus 1 optional:
- `createrailwaysnavigator:advanced_display` ("Read the Departure Board").
- `createrailwaysnavigator:navigator` ("Plan Your Journey"; needs a Mechanical
  Crafter + precision mechanism, reinforcing the Create tier).
- `createrailwaysnavigator:train_station_clock` (optional flavor; already gated).
- Do NOT quest `navigator_lectern` (no shipped recipe — acquisition path
  unverified). Do NOT author one quest per display shape (cosmetic form factors).

---

## 5. Chapter strategy

### New chapters (2)

1. **"The Second Mill: Steam, Rail & Logistics"** — `the_renaissance`. Base
   Create's Renaissance tail (§2). Steam bridge (required root) -> Trains branch
   (required core T1–T4, optional T5) -> Factory Logistics branch (required core
   L1–L3, optional L4) -> optional QoL/signage + Railways Navigator tail. This is
   the single biggest content gap in the pack.
2. **"Take to the Skies"** — `gilded_age`. The flight questline (§3 Gilded).
   Physics Assembler root -> motive power -> wheels -> balloon -> propellers
   (optional) -> airship capstone -> Create Propulsion thruster depth (optional).
   Support/flavor transport chapter, NOT a spine gate.

### Extensions of existing chapters (no new chapter)

- `m1_first_mill` (`medieval_times`): stress + encased-fan four-catalyst prose
  polish; attach the `alloyed` Alloy Forge + Steel beat and the `sliceanddice`
  Slicer beat as small branches (or attach to adjacent Medieval chapters).
- `m3_relics_and_burrows` (`medieval_times`): extend the existing CIF roost/
  fishing-net nodes with the automation-loop prose (do not re-add acquire tasks).
- `ir_create_industrial_addons` (`industrial_revolution`): insert the New Age
  "First Electricity/Move/Use Power" entry rungs (First Electricity + electrical
  connector as check_quest/depend, not re-tasked; only `copper_wire`/`basic_motor`/
  `basic_energiser` are new item tasks); add the Metalwork 2-node yield sub-branch;
  add optional Confectionery + Furniture nodes (1-2 each, no more); fold Cold Sweat +
  Diesel fuel-tier prose onto existing nodes.
- `ir_power_motion_and_grid` (`industrial_revolution`): insert the CAA
  "Low vs High Current" node before the big-machine nodes; dedupe the Rolling Mill
  IR copy. Leave the Power Grid spine alone.

### Required vs optional

- **Required spine** per new chapter: Steam bridge S1–S2; Trains T1–T4; Factory
  Logistics L1–L3; Flight F1–F4 + F6 capstone. IR entry rungs (CAA current, New
  Age first-electricity) are required within their existing chapters.
- **Optional depth:** T5 signalling, L4 frogport, F5 propellers, all Propulsion
  nodes, QoL/signage, Railways Navigator, Confectionery, Furniture, Metalwork
  netherite capstone, Diesel fuel tiers.
- **Optional flavor must NOT grant or gate any AStages stage.** These chapters are
  Create tutorial/motivation; they teach and reward, they do not award progression
  stages. The pack's stage grants stay on the existing spine capstones.

**Anti-bloat guardrail (canon §4 — padding to hit a count is forbidden).** This is a
large surface (2 new chapters + inserts into 4 existing chapters + several optional
flavor tails), so apply the anti-bloat lens per node at authoring time:
- Every optional node must teach a DISTINCT mechanic that no other node teaches. If a
  node exists only to give an add-on a "home," cut it.
- The two NEW chapters (Second Mill, Take to the Skies) stay: each covers a genuinely
  zero-quested flagship system (Create 6 factory logistics; the flight family).
- The IR inserts are where creep is most likely — hold each flavor add-on
  (Confectionery, Furnitures) to the stated 1-2 optional nodes, and the Metalwork
  sub-branch to 2 nodes (molten buffering is the one new mechanic; ore doubling is
  already taught by crushing wheels — do not re-teach it).
- Prefer prose folds onto existing nodes over new item tasks whenever the item is
  already quested (First Electricity, S1 boiler, Diesel fuel tiers, Cold Sweat).

### Reveal model

Native FTBQ progressive reveal, matching the pack pattern
(`hide_quest_until_deps_complete` + a prior-age gate). A quest needs >=1 dependency
or it is rootless and always-visible (bytecode-verified). So:
- Each new chapter's ROOT quest depends on the prior age's capstone gateway (the
  Renaissance chapter root chains off the Renaissance entry gate; the Gilded flight
  chapter root chains off the Gilded entry gate) so the chapter tab opens at the
  right time.
- Every downstream node depends on its predecessor (crossing-free — see §6).
- Do NOT add stray rootless nodes.

### Leave-alone list (already-quested Create content)

- `createnuclear` — `at1_nuclear_dawn` (Atomic). Fully quested. Do not touch.
- `create_new_age` thorium reactor — `at1_nuclear_dawn` (Atomic). Do not touch.
- `createoreexcavation` — `ir_create_industrial_addons` (IR). Fully quested.
- `powergrid` — `ir_power_motion_and_grid` (IR), its own ~23-id chapter. Leave the
  required spine; electronics micro-layer stays optional depth.
- `create_aquatic_ambitions` — owned by the ocean spec. Do not duplicate.
- `huge_diesel_engine`, `coral_generator` (optional) — `g5_empire_of_iron`.
- `m1_first_mill` base kinetics through sequenced assembly — already thorough;
  polish prose only.

---

## 6. Layout constraint (crossing-free)

Hard constraint: dependency lines must not cross. Tight 0.5-grid spacing. Flow
direction is negotiable (vertical/backward allowed); crossings are not. Design
each new chapter as a spine with side-branches so bundled multi-item nodes keep
the graph planar:

- **Second Mill:** a vertical steam root (S1 top, S2 below), then the graph forks
  LEFT into the Trains column (T1->T2->T3->T4->T5 top-to-bottom) and RIGHT into the
  Factory Logistics column (L1->L2->L3->L4 top-to-bottom). The QoL/signage +
  Railways Navigator tail hangs off the bottom of the Trains column so CRN sits
  next to the track content it depends on. No line crosses because the two columns
  never share a dependency edge below the steam root.
- **Take to the Skies:** a vertical spine F1->F2, then F2 forks to F3 (wheels,
  left) and F4 (balloon, right); F4->F5 (propellers) -> F6 (airship capstone)
  converges on the right spine; F3 (wheels) is a leaf. Create Propulsion depth
  hangs as a short chain off F6 (or off F2's engine node) on the far side so its
  edges do not cross the flight spine.

Bundle multi-block steps into one node (e.g. clutch+housing+rotor for a generator,
or track_signal+track_observer) rather than scattering them, per canon.

---

## 7. Phased authoring roadmap

Build in this order (highest teaching-value gap first, dependencies respected):

1. **Phase 1 — Renaissance "Second Mill" chapter.** The single biggest gap; Create
   6's flagship factory-logistics system is nearly untaught. Author steam bridge +
   trains + factory logistics. Attach the Railways Navigator tail. This is the
   priority.
2. **Phase 2 — IR entry-rung inserts (existing chapters).** CAA "Low vs High
   Current"; New Age "First/Move/Use Electricity" (First Electricity is a
   check_quest mirror; `electrical_connector` is depended-on, not re-tasked; only
   `copper_wire`/`basic_motor`/`basic_energiser` are new item tasks); Metalwork
   2-node yield sub-branch. All are inserts into `ir_create_industrial_addons` /
   `ir_power_motion_and_grid`, lower risk than a new chapter. Dedupe the Rolling Mill
   IR copy here.
3. **Phase 3 — Gilded "Take to the Skies" chapter.** Requires the AStages gating
   companion change FIRST (lock Aeronautics/Simulated/Offroad + Propulsion at
   Gilded). Author flight spine + Propulsion depth after locks land.
4. **Phase 4 — Medieval add-on beats.** Alloy Forge + Steel (`alloyed`); Slicer
   (`sliceanddice`); CIF roost/net automation prose. Small, low-risk polish.
5. **Phase 5 — Optional flavor + prose folds.** Confectionery, Furnitures, Cold
   Sweat prose, Diesel fuel-tier prose, encased-fan/stress prose polish in
   `m1_first_mill`. Do last; smallest signal.

After each phase: run the FTBQ validation (crossing-free check, dependency
integrity, no rootless nodes, no duplicate `id:`-anchored item tasks, all task ids
resolve), and confirm no optional flavor node grants/gates an AStages stage.

---

## 8. Open questions needing a human call

1. **Silver source at IR — RESOLVED, no longer open.** The CAA high-current path
   (`createaddition:electrum_ingot`/`electrum_spool`) needs `c:ingots/silver`.
   Silver IS provided before IR: `aoa_astages_01_item_restrictions.js` gates the
   whole `alltheores:` silver line (`silver_ingot`, ores, dust, raw) at
   `the_renaissance` (lines 436-529), and the IE/occultism/projectred silver ores
   are disguised at Renaissance in `aoa_astages_06_ore_restrictions.js`. Renaissance
   is strictly before `industrial_revolution`, so silver is available at IR and the
   high-current path does NOT stall. Keep electrum as optional depth for pacing
   only. No human call needed.
2. **New chapters vs mega-chapter.** Two new chapters proposed (Renaissance Second
   Mill, Gilded Take to the Skies). Confirm the pack wants two discrete chapters
   vs folding steam/trains/logistics into an existing Renaissance chapter. Canon
   favors discrete chapters for coherent systems; confirm before authoring group
   ids.
3. **AStages gating for flight (blocking Phase 3).** Aeronautics/Simulated/Offroad
   and most of Create Propulsion are ungated (verified: no simulated/aeronautics/
   offroad locks in `create_family.js`; only `createpropulsion:coral_generator` is
   locked). The flight chapter is blocked until the full companion AStages pass
   lands — see the "Gating checklist" under §3 Gilded Age for the exact item list to
   lock at `gilded_age`. The only open human call here is scope/ownership: confirm
   this AStages pass is in scope for this initiative and who authors the locks. The
   requirement itself is settled — it is a prerequisite, not optional, and Phase 3
   does not start until every checklist lock is verified.
4. **Stray Renaissance steam_engine node.** `ren_observation_experimentation`
   node `0B031080000000D2` item-tasks `create:steam_engine` gated on a magic skill
   level. Confirm: relocate to the new Second Mill chapter, convert to a
   `check_quest` mirror, or leave as a magic-flavor duplicate? (Recommend convert
   to avoid a double-item task; needs a call.)
5. **Rolling Mill IR duplicate.** `createaddition:rolling_mill` is item-tasked in
   both `m1_first_mill` (Medieval, correct) and `ir_power_motion_and_grid` (IR).
   Confirm removal/conversion of the IR copy in the Phase 2 pass.
6. **Encased-fan / stress prose in `m1_first_mill`.** Needs a live-node read to
   confirm whether the four catalysts and network-wide stress are already taught
   before adding prose (avoid duplicating existing text). A verification read, not
   a design decision, but flag it as a pre-authoring step.
7. **Aquatic Ambitions seam.** The ocean spec §9 notes Aquatic Ambitions "may be
   absorbed" into this initiative. This design leaves it with the ocean spec.
   Confirm the ownership stays with the ocean spec so the g6 branch is authored
   once, not twice.
8. **Performance: Sable physics.** The flight chapter motivates many simultaneous
   Sable physics contraptions, a real server-tick cost. Flag for the performance
   pass before shipping a chapter that encourages fleets of airships.

---

## 9. Verification appendix

All task ids below were read from the actual mod jars in `mods/` on 2026-07-01
(`unzip -p <jar> assets/<ns>/lang/en_us.json`). No id in this design was invented.

- **Base Create** (`create-1.21.1-6.0.10.jar`): verified `packager`, `repackager`,
  `stock_link`, `stock_ticker`, `factory_gauge`, `redstone_requester`,
  `package_frogport`, `steam_engine`, `steam_whistle`, `track`, `track_station`,
  `track_signal`, `track_observer`, `small_bogey`, `large_bogey`, `controls`,
  `schedule`, `display_board`, `display_link`, `nixie_tube`, `elevator_pulley`,
  `precision_mechanism`, `electron_tube`, `brass_casing`, `deployer`,
  `mechanical_crafter`. (Fundamentals ids drawn from jar-verified `create_base.md`.)
- **createaddition** (`createaddition-1.6.0.jar`): `rolling_mill`, `alternator`,
  `electric_motor`, `connector`, `large_connector`, `modular_accumulator`,
  `tesla_coil`, `liquid_blaze_burner`, `copper_spool`, `gold_spool`,
  `electrum_spool`, `copper_wire`, `electrum_ingot`, `capacitor`, `biomass`,
  `straw`.
- **create_new_age** (`create-new-age-1.2.0+neoforge-mc1.21.1.jar`):
  `generator_coil`, `carbon_brushes`, `basic_motor`, `basic_energiser`,
  `electrical_connector`, `copper_wire`, `redstone_magnet`, `layered_magnet`.
- **createmetalwork** (`createmetalwork-2.0.0.jar`): `crushed_andesite`,
  `crushed_netherite_scrap`, `molten_iron_bucket`, `molten_brass_bucket`,
  `molten_netherite_bucket`.
- **createdieselgenerators** (`createdieselgenerators-1.21.1-1.3.14.jar`):
  `oil_scanner`, `pumpjack_crank`, `distillation_controller`, `diesel_engine`,
  `large_diesel_engine`, `huge_diesel_engine`, `biodiesel_bucket`,
  `bulk_fermenter`, `burner`.
- **alloyed** (`alloyed-3.0.6+1.21.1-neoforge.jar`): `forge`, `steel_pickaxe`,
  `steel_sword`, `steel_chestplate`, `steel_sheet`, `bronze_bell`. (Ingots/blocks
  swap to `alltheores:` — not tasked.)
- **sliceanddice** (`sliceanddice-forge-4.2.4.jar`): `slicer`, `sprinkler`,
  `fertilizer_bucket`.
- **create_integrated_farming** (`create-integrated-farming-1.2.6.jar`): `roost`,
  `chicken_roost`, `fishing_net`.
- **create_confectionery** (`create-confectionery1.21.1_v1.1.3b.jar`):
  `cocoa_powder`, `caramel_bucket`, `bar_of_caramel`. (Namespace underscore.)
- **create_furnitures** (`create_furnitures-1.1.2-neoforge-1.21.1.jar`):
  `brass_chair`, `andesite_table` (single-underscore namespace; from jar-verified
  doc).
- **createpropulsion** (`createpropulsion-1.1.4.jar`): `thruster`, `ion_thruster`,
  `coral_generator`, `turpentine_bucket`, `stirling_engine`.
- **Aeronautics bundle** (`create-aeronautics-bundled-1.21.1-1.3.0.jar`, nested
  jarjar): `simulated:physics_assembler`, `simulated:red_portable_engine`,
  `simulated:steering_wheel`, `simulated:throttle_lever`, `simulated:gimbal_sensor`,
  `simulated:contraption_diagram`, `aeronautics:white_envelope`,
  `aeronautics:adjustable_burner`, `aeronautics:propeller_bearing`,
  `aeronautics:wooden_propeller`, `aeronautics:smart_propeller`,
  `aeronautics:levitite`, `aeronautics:levitite_blend_bucket`,
  `offroad:wheel_mount`, `offroad:tire`.
- **createrailwaysnavigator** (`navigator`, `advanced_display`,
  `train_station_clock`; from jar-verified doc — `navigator_lectern` has no recipe,
  not tasked).
- **create_cold_sweat** — verified to register ZERO items; prose-only, never
  tasked.

### Could-not-verify / must-verify-before-authoring flags

- `c:ingots/silver` availability at IR — VERIFIED 2026-07-01: `alltheores:silver_
  ingot` and the full silver line are Renaissance-gated in
  `aoa_astages_01_item_restrictions.js` (lines 436-529), available at IR. Resolved.
- Exact live prose of the `m1_first_mill` encased-fan and stress nodes — needs a
  read before adding prose (open question 6).
- Whether the existing `createdieselgenerators:biodiesel_bucket` node is the right
  anchor for a fuel-tier prose fold vs a duplicate — read the live IR node first.
- `createrailwaysnavigator:navigator_lectern` acquisition path — unverified; do
  not task.
- Runtime Sable physics performance cost — flagged for the performance pass, not
  measured.
