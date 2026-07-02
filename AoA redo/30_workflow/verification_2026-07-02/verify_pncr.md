# PneumaticCraft: Repressurized — Coverage Verification (READ-ONLY)

Date: 2026-07-02. Mods verified in `/mods`:
- `pneumaticcraft-repressurized-8.2.20+mc1.21.1.jar` (PneumaticCraft: Repressurized)
- `appliedpneumatics-1.21.1-neoforge-1.0.8.jar` (Applied Pneumatics — AE2 bridge addon)

## VERDICT

**ADEQUATE, essentially complete for the machine/mechanic spine. Under-covered only on the endgame *career* surface (drones, pneumatic armor, tools).**

The census "63 refs / just under adequate" undercounts quality. The IR chapter
`ir_pneumaticcraft_pressure_plastic.snbt` is one of the densest single-mod chapters in
the pack: ~48 distinct pneumaticcraft item-tasks walking the full pressure ladder from
compressed iron through the assembly line. The pressure/PCB/refinery/plastic **spine is
fully quested and correctly aged**. What genuinely remains unquested is the *tail*:
programmed drones, the pneumatic armor set, and the utility tools — and most of that tail
is small, optional-flavor, or deliberately out of scope. There is **no gating gap** and
**no softlock**: the AStages gate (`aoa_astages_01c_pneumaticcraft.js`) already locks the
full IR machine set + Gilded drone-programming set, including items that are locked but not
quested (elevator, spawners, kerosene_lamp).

Recommendation: one small Gilded **drone-career** quest cluster is the only genuinely
quest-worthy gap. Everything else is anti-bloat skip or already covered.

## PROGRESSION SURFACE (jar-verified) vs LIVE COVERAGE

| Beat | Canonical mechanic | Quested? | Where |
|------|--------------------|----------|-------|
| Entry | compressed_iron (TNT/explosion route) → compressed_iron_block | YES | IR chap (compressed_iron_block task) |
| Air 1.5 bar | air_compressor (manual/solar/flux) + air_canister + charging_station + pressure_gauge | YES | IR chap (manual/solar/flux_compressor, air_compressor, air_canister, charging_station, pressure_gauge) |
| Pressure vessel | pressure_chamber (walls/valve/interface) + pressure_tube + tube safety | YES | IR chap (pressure_chamber_valve/interface, pressure_tube, reinforced_pressure_tube, tube_junction, pressure_gauge_module) |
| Higher tiers | advanced/thermal/electrostatic compressor (→4.5/10/20 bar) | YES | IR chap (advanced_air/liquid, thermal, electrostatic compressors) |
| PCB chain | uv_light_box → empty_pcb → etching (acid/tank) → unassembled_pcb → printed_circuit_board (+transistor, capacitor) | YES | IR chap (uv_light_box, empty_pcb, etching_acid_bucket, etching_tank, unassembled_pcb, printed_circuit_board, transistor, capacitor) |
| Assembly line | assembly_controller + platform + drill + laser + io_units + drone (component) | YES | IR chap (all 5 assembly blocks + drone item) |
| Processing/refinery | thermopneumatic_processing_plant; refinery → diesel/kerosene/gasoline/LPG | YES | IR chap (thermo plant ×3); **refinery in `ir_create_industrial_addons`** (oil chapter, 20-level gate) |
| Plastic | plastic (from oil chain, 1.21) | YES | IR chap + ir_create_industrial_addons |
| Heat mgmt | heat_sink, heat_pipe, thermal_lagging, vortex_tube | YES | IR chap (all four) |
| Power | pneumatic_dynamo (air→FE), pneumatic_generator | YES (dynamo) | IR chap (pneumatic_dynamo) |
| Fluid logistics | tanks (huge_tank), liquid/omnidirectional_hopper, gas_lift, vacuum_pump | YES | IR chap |
| Utility blocks | aerial_interface, air_cannon, air_grate_module | YES | IR chap |
| Endgame IR block | electrostatic_compressor, aerial_interface | YES | IR chap |
| **Drones (career)** | collector/harvesting/logistics/guard drone + programming_puzzle + amadron_tablet + logistics network | **NO** (drone *item* only) | GAP — Gilded |
| **Drone programming** | programmer, programmable_controller, drone_interface, universal_sensor | YES (blocks) | `g4_the_infinite_grid` (Gilded) |
| **Pneumatic armor** | pneumatic_helmet/chestplate/leggings/boots + upgrade matrix | PARTIAL (chestplate only) | `ir_ir_side_gear_hidden_equipment` |
| **Tools** | jackhammer, minigun, drill bits, pneumatic_wrench, gps_tool, manometer | PARTIAL (jackhammer, minigun) | `ir_ir_side_gear_hidden_equipment` |
| Spawner tech | spawner_extractor, pressurized_spawner, vacuum_trap, spawner_core | NO | locked, not quested (skip — niche) |
| Elevator | elevator_base/frame/caller | NO | locked, not quested (skip — QoL/decor) |
| Applied Pneumatics | me_amadron/temperature/pressure interface (AE2 bridge) | NO | locked Gilded, not quested (skip — deep AE2 tail) |

## RANKED GAP LIST (jar-verified ids; bundled; anti-bloat applied)

**G1 — Drone career cluster (Gilded) — the one genuinely quest-worthy gap.**
The drone *item* is a task in IR (as an assembly-line output), but the actual programmable-
drone gameplay — the mod's signature system — has no quest home. Bundle into 1–2 Gilded
nodes sitting under the existing `g4` programmer/drone_interface line:
- `pneumaticcraft:programming_puzzle` (the graphical-programming pieces — the core mechanic)
- one drone-role node: `pneumaticcraft:collector_drone`, `pneumaticcraft:harvesting_drone`,
  `pneumaticcraft:logistics_drone`, `pneumaticcraft:guard_drone` (pick 1 task, list rest in prose)
- `pneumaticcraft:amadron_tablet` (trading/ordering terminal — natural Gilded logistics beat)
- logistics network: `pneumaticcraft:logistics_frame_requester` / `_active_provider`
  (default_storage frame is already an IR task; the requester/provider complete the loop)
Age: **gilded_age** (matches the existing gate). Chapter: `g4_the_infinite_grid`.

**G2 — Pneumatic armor set completion (IR) — optional-flavor, low priority.**
`pneumatic_chestplate` is already a hidden-equipment task; the set is incomplete. If desired,
add one bundled node for `pneumatic_helmet` + `pneumatic_leggings` + `pneumatic_boots`
(the chestplate + a helmet gate the upgrade-matrix armor system). Age: **industrial_revolution**,
chapter `ir_ir_side_gear_hidden_equipment`. Anti-bloat: upgrades (`speed/volume/range/
night_vision/...`) are NOT individually quest-worthy — mention in prose only.

**G3 — heat_frame + tool tail (IR) — optional, low priority.**
`pneumaticcraft:heat_frame` (a genuinely useful cross-mod cooling/heating item) has no home;
could join a heat-management node with the already-quested heat_sink/vortex_tube. Tools
`drill_bit_diamond`/`_netherite`, `manometer`, `gps_tool`, `pneumatic_wrench` are QoL and
belong in prose, not as tasks.

**SKIP (verified out-of-scope / anti-bloat):**
- Spawner extraction (spawner_extractor, pressurized_spawner, vacuum_trap): locked, niche mob-
  farm tech; not a spine beat. Skip.
- Elevator (elevator_base/frame/caller), kerosene_lamp, pneumatic_door: decor/QoL. Locked, skip.
- All upgrades (`*_upgrade`), tube variants (safety/regulator/flow modules), plastic/wall_lamp
  decor variants: per anti-bloat rule, mechanics not variants. Skip.
- Applied Pneumatics (me_amadron/temperature interfaces): deep AE2-bridge tail, correctly gated
  Gilded; out of quest scope unless a dedicated AE2-bridge beat is wanted later.

## GATE STATUS (no action needed)

`kubejs/server_scripts/aoa_astages_01c_pneumaticcraft.js` is thorough: IR machines/vessels/
PCB/processing/generators/utility all locked at `industrial_revolution`; digital-logic +
drone-programming + smart_chest/security/sentry at `gilded_age`; Applied Pneumatics ME bridge
at `gilded_age`. It even locks items with no quest task (elevator, spawners, kerosene_lamp),
so the unquested tail cannot leak early. `reinforced_chest`/`tag_workbench` left ungated per
overscope policy. **No missing gate, no coverage-driven gate to add** (per QUEST_SCOPE_REGISTRY).

## SOURCES
- JAR lang truth: `assets/pneumaticcraft/lang/en_us.json` (8.2.20) and
  `assets/appliedpneumatics/lang/en_us.json` (1.0.8), extracted from the live jars.
- Live chapters: `config/ftbquests/quests/chapters/ir_pneumaticcraft_pressure_plastic.snbt`,
  `ir_create_industrial_addons.snbt`, `ir_ir_side_gear_hidden_equipment.snbt`,
  `g4_the_infinite_grid.snbt`.
- Gate: `kubejs/server_scripts/aoa_astages_01c_pneumaticcraft.js`; fuel tags
  `ir2_fuel_tag_unification.js`; oil weave `aoa_oil_spine_weaves.js`.
- Progression order: FTB Wiki https://ftb.fandom.com/wiki/PneumaticCraft ;
  desht changelog/gameplay https://gist.github.com/desht/b604bd670f7f718bb4e6f20ff53893e2 ;
  CurseForge https://www.curseforge.com/minecraft/mc-mods/pneumaticcraft-repressurized .
