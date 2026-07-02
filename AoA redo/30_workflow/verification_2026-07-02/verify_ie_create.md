# IE + Create-family coverage verification (2026-07-02, READ-ONLY)

All six mods confirmed present in `/mods`:
- ImmersiveEngineering-1.21.1-12.4.2-194.jar
- ImmersivePetroleum-1.21.1-4.4.1-37.jar
- createaddition-1.6.0.jar
- create-new-age-1.2.0+neoforge-mc1.21.1.jar
- createdieselgenerators-1.21.1-1.3.14.jar
- createoreexcavation-1.21-1.6.8.jar (SKIP-tier per standing ruling; still confirmed quested)

Related IE-family jars also present (not in scope, not audited): more-immersive-wires, immersivethunder, Immersive-Energistics, immersive_aircraft/machinery/furniture/paintings.

Census claimed "86 IE refs, deep lines likely open." Verdict: the deep IE spine is NOT open. It is one of the most thoroughly built systems in the pack.

---

## Per-mod verdict

### immersiveengineering — COMPLETE (medieval->IR->gilded spine, deeply built)
The census undercounted. IE is quested across THREE chapters forming the intended spine:
- **metallurgy** (Medieval): 25 IE refs. Owns coke oven (`main/mb_cokeoven` advancement + `coke`/`coal_coke`/`cokebrick`), IE crusher (`multiblocks/mb_crusher`), treated wood family, LV wire/connectors, hammer, hempcrete, concrete, fluid pipe/valve, small tank. This is the medieval IE entry.
- **ir_immersive_engineering_early_factory** (IR): 83 IE refs, 235 quest nodes. The deep chapter. Uses `mb_` advancement tasks for the multiblocks-with-no-item-recipe (per memory rule): mb_blastfurnace, mb_arcfurnace, mb_excavator, mb_lightningrod, mb_cokeoven + item-task multiblocks mb_metalpress, mb_mixer, mb_refinery, mb_fermenter, mb_squeezer, mb_silo, mb_tank, mb_crusher, mb_improvedblastfurnace. Covers assembler, auto_workbench, bottling, sawmill, cloche, dynamo/generator/thermoelectric, watermill/windmill, capacitors, charging station, blueprint/circuit_table, drill, toolbox, steel/faraday armor, biodiesel bucket.
- **g5_empire_of_iron** (Gilded): 17 IE refs, 522 nodes(!). Owns the late/heavy IE: excavator + bucket_wheel + core sample drill (advancement mb_excavator), arc furnace, advanced_blast_furnace, tesla_coil, lightning_rod, turret_gun, turret_chem, assembler-at-scale.
- Guns (**railgun, revolver, chemthrower**) + drill/skyhook/buzzsaw upgrades: in g5 and `ir_ir_side_gear_hidden_equipment` (hidden gear chapter).

### immersivepetroleum — COMPLETE
31 refs concentrated in `ir_create_industrial_addons` (IR entry: pumpjack, derrick, oiltank, distillation_tower, seismic_survey, crude/diesel/gasoline/lubricant buckets, bitumen, gas_generator) and `g5_empire_of_iron` (Gilded: coker_unit, hydrotreater, auto_lubricator). `gas_generator` was wired in the I2 seams commit (48720a2). Flarestack is gated (IR) and referenced; not a fresh quest "today."

### createaddition — COMPLETE for progression surface
18 of ~40 jar ids quested in `ir_power_motion_and_grid` (28 refs) + seams. Covers the whole electric spine: electric_motor, alternator, rolling_mill, redstone_relay, digital_adapter, connectors (all tiers), modular_accumulator, portable_energy_interface, capacitor, tesla_coil, electrum spools, liquid_blaze_burner, biomass, straw. Unquested remainder is cosmetic/variant (goblets, figurines, cakes, rods/wires/sheets in every metal) — correctly excluded as anti-bloat.

### create_new_age — COMPLETE + correctly split
IR electric tier (motors/energisers/magnets/heater/coils/wire) in `ir_create_industrial_addons`; **Atomic thorium reactor chain** (reactor_casing/rod/glass/heat_vent/fuel_acceptor, thorium_ore, radioactive_thorium, nuclear_fuel, heat_pump) in `at1_nuclear_dawn`, matching canon (electric->IR, nuclear->Atomic). Gates in aoa_astages_01g back this exactly.

### createdieselgenerators — COMPLETE
20 refs in ir_create_industrial_addons (bulk_fermenter, distillation controller/tank, large/huge diesel engine, biodiesel, full pumpjack assembly) + huge_diesel_engine in g5.

### createoreexcavation — COVERED (SKIP-tier confirmed)
13 refs in ir_create_industrial_addons: drilling_machine, sample_drill, vein_finder, vein_atlas, extractor. Has quest home; no further action per ruling.

---

## System | quested-where | gap table (IE)

| IE system | jar-verified | quested chapter | status |
|---|---|---|---|
| Coke oven / coal_coke | yes | metallurgy (mb_cokeoven adv) | DONE |
| Crusher | yes | metallurgy + IR (mb_crusher) | DONE |
| Blast furnace / improved | yes | IR (mb_blastfurnace, mb_improvedblastfurnace) | DONE |
| Arc furnace | yes | IR + g5 (mb_arcfurnace) | DONE |
| Metal press / mixer | yes | IR (mb_metalpress, mb_mixer) | DONE |
| Squeezer/fermenter/refinery (biodiesel) | yes | IR (mb_squeezer/fermenter/refinery) | DONE |
| Assembler / auto_workbench / bottling | yes | IR + g5 | DONE |
| Excavator + bucket_wheel + core sample drill | yes | g5 (mb_excavator adv) | DONE |
| Silo / tank | yes | IR (mb_silo, mb_tank) | DONE |
| Water/wind mill, dynamo, thermoelectric, generator | yes | IR | DONE |
| Lightning rod / tesla coil | yes | IR(rod)+g5, gated gilded | DONE |
| Turrets (gun/chem) | yes | g5, gated gilded | DONE |
| Railgun / revolver / chemthrower + upgrades | yes | g5 + hidden gear | DONE |
| Cloche | yes | IR, gated IR | DONE |
| Toolbox / manual / blueprint / circuit_table | yes | IR | DONE |
| Drill + heads / buzzsaw / skyhook | yes | IR + hidden gear | DONE |
| Charging station / capacitors / wires-connectors | yes | IR + metallurgy | DONE |
| Steel / faraday armor | yes | IR | DONE |
| Radio tower / radiator / furnace_heater / preheater | yes | IR, radio_tower gilded | DONE |
| Conveyor/wire VARIANTS, breaker switch, transformers, meters, balloon, electric_lantern | yes | not individually quested | INTENTIONAL (anti-bloat variants) |

## Gates (kubejs/server_scripts/aoa_astages_01d_immersive.js + 01g_create_family.js)
IE machines gated IR; radio_tower/lightning_rod/tesla_coil/turrets gated Gilded; IP seismic/flarestack IR, auto_lubricator Gilded; createaddition + create_new_age electric IR; create_new_age nuclear reactor + thorium Atomic; createdieselgenerators IR; COE sample_drill IR. Gates match placement. No mis-aged inversion found.

---

## Ranked jar-verified gap list

**No hard gaps. No softlocks. No cross-age inversions.** The census "deep IE lines likely open" is VOID — the deep lines are the most-built system audited.

Only optional/cosmetic residue, none quest-worthy per anti-bloat canon:
1. IE conveyor family + wire/relay/transformer/meter variants — VARIANTS, correctly excluded.
2. IE balloon, electric_lantern, breaker_switch/redstone_breaker, current_transformer — decor/utility, excluded.
3. createaddition metal rods/wires/sheets/goblets/figurines/cakes, barbed_wire, accumulator — cosmetic/variant, excluded.
4. IP motorboat/speedboat + hull upgrades, molotov/napalm, asphalt, paraffin/petcoke blocks — flavor/decor; speedboat could be an optional single node if ever desired (LOW, not required).

Recommendation: mark IE/Create-family census line CLOSED. If any single addition is entertained, it is one optional IP speedboat flavor node — not a "deep line."
