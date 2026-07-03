# Late Tech Core Audit

Scope: Chemical Science, Nuclear Science, Electrodynamics, Voltaic, Dynamic Electricity, and Create Nuclear.

Sources:

- Chemical Science: https://www.curseforge.com/minecraft/mc-mods/chemicalscience
- Nuclear Science wiki: https://wiki.aurilis.dev/nuclear-science/
- Electrodynamics: https://www.curseforge.com/minecraft/mc-mods/electrodynamics
- Mekanism reactor references for comparable multiblock pacing: https://wiki.aidancbrady.com/wiki/Fission_Reactor and https://wiki.aidancbrady.com/wiki/Fusion_Reactor

## Coverage Snapshot

Live FTBQ/KubeJS already covers the core Atomic tech spine:

- Chemical Science appears in `g2_the_refinery`, `at1_nuclear_dawn`, `at2_the_periodic_table`, and `at5_threshold_of_war`.
- Nuclear Science appears heavily in `at3_chain_reaction`.
- Electrodynamics appears in Industrial power, Gilded circuits, and Atomic nuclear chapters.
- Dynamic Electricity is mostly convergence support, not a standalone questline.
- Voltaic is mostly upgrades/support.
- Create Nuclear has some reactor coverage, but decor/autunite variants should stay out.

## Chemical Science

Static jar scan found 904 recipes and 31 recipe types. Live coverage already includes major refinery and Fume Hood/chemical-bench concepts.

Good missing or undercalled targets:

- `chemicalscience:fuelcell`
- `chemicalscience:niobiumtitaniumcoil`
- `chemicalscience:radiationshielding_advancedglass`
- `chemicalscience:vanadium_catalyst`
- `chemicalscience:chromotographycardmethane`
- `chemicalscience:block_element_po`
- `chemicalscience:block_element_pm`
- `chemicalscience:dust_promethium`

Quest rule: do not quest the periodic table as a checklist. Quest only elements/cards that unlock a real gate.

Suggested shape:

| Quest | Target | Age | Why |
|---|---|---|---|
| Advanced Shielding | `chemicalscience:radiationshielding_advancedglass` | Atomic | Safety and reactor lab literacy. |
| Vanadium Catalyst | `chemicalscience:vanadium_catalyst` | Atomic | Crosses into process chemistry. |
| Methane Card | `chemicalscience:chromotographycardmethane` | Atomic optional | Good if gas separation matters. |
| Promethium Proof | `chemicalscience:dust_promethium` or `block_element_pm` | Otherworldly optional | FOMO if late nuclear chemistry matters. |

## Nuclear Science

Live coverage is strong for:

- Fission.
- Molten Salt Reactor.
- Fusion.
- Nuclear boiler/steam handling.
- Atomic assembler.
- Particle injector.
- Teleporter.
- Radioisotope generator.
- Hazmat gear.

Useful missing or undercalled targets:

- `nuclearscience:geigercounter`
- `nuclearscience:yellowcake`
- `nuclearscience:cellheavywater`
- `nuclearscience:frequencycard`
- `nuclearscience:logisticscablebase`
- `nuclearscience:moltensaltpipevanadiumsteelceramic`
- `nuclearscience:fuelplutonium`
- `nuclearscience:plutonium239`
- `nuclearscience:polonium210`
- `nuclearscience:cellantimattersmall`
- `nuclearscience:cellantimatterlarge`
- `nuclearscience:cellantimatterverylarge`
- `nuclearscience:celldarkmatter`

Suggested shape:

| Quest | Target | Age | Why |
|---|---|---|---|
| Geiger Discipline | `nuclearscience:geigercounter` | Atomic early | Safety literacy. |
| Heavy Water Cell | `nuclearscience:cellheavywater` | Atomic | Reactor setup bridge. |
| Reactor Logistics | `nuclearscience:logisticscablebase` | Atomic | Multiblock operation. |
| Plutonium Fuel | `nuclearscience:fuelplutonium` | Atomic optional | Alternate fuel proof. |
| Exotic Cells | antimatter/dark matter cells | Otherworldly | Only after acquisition path is verified. |

## Electrodynamics

Static jar scan found a very large machine, pipe, tank, wire, transformer, and chemistry surface. Many locked items are not directly quested.

Good missing/undercalled groups:

- Battery and battery boxes.
- Upgrade/downgrade transformers.
- `electrodynamics:decompressor`
- `electrodynamics:electricpump`
- Fluid/gas valves, vents, filters, pumps.
- Gas/Fluid tanks.
- `electrodynamics:logisticalmanager`
- `electrodynamics:relay`
- `electrodynamics:seismicrelay`
- `electrodynamics:wiremilldouble`
- `electrodynamics:mineralgrinderdouble`
- `electrodynamics:pressuregauge`

Suggested shape:

| Quest | Target | Age | Why |
|---|---|---|---|
| Transformer Yard | upgrade/downgrade transformer | Gilded/Atomic | Teaches voltage management. |
| Reserve Power | battery box | Gilded/Atomic | Prevents reactor/factory brownout surprise. |
| Pressure And Gas | pressure gauge plus gas tank/valve | Atomic | Explains chemical handling. |
| Pipe Logic | logistical manager/filter | Atomic optional | Only if players need ED logistics. |

## Voltaic

Mostly support/upgrades.

Do not quest every upgrade. If used, choose:

- `voltaic:upgradebasiccapacity`
- `voltaic:upgradebasicspeed`
- `voltaic:upgradeadvancedcapacity`
- `voltaic:upgradeadvancedspeed`
- `voltaic:upgradeimprovedsolarcell`

`voltaic:upgradeiteminput` needs runtime/JEI check because the static recipe looked self-referential.

## Dynamic Electricity

Best use: ingredient/weave support, not a standalone questline.

Potential weave targets:

- `dynamicelectricity:alternator`
- `dynamicelectricity:stator`
- `dynamicelectricity:motorachv`
- `dynamicelectricity:motordchv`

## Create Nuclear

Existing reactor coverage is enough for basic teaching.

Good targets only if needed:

- `createnuclear:reactor_controller`
- `createnuclear:reactor_core`
- `createnuclear:reactor_cooler`
- `createnuclear:reactor_blueprint_item`
- `createnuclear:graphite_rod`

Do not quest autunite decorative variants.

## Late-Core Repair Items

- `g2_the_refinery` has live `ftbquests:missing_item` residues for Industrial Foregoing black-hole storage placeholders.
- `at4_machine_soul` has live `ftbquests:missing_item` residues involving IF/IFEU hydroponic simulation and black-hole unit/tank placeholders.
- `at7_chaos_convergence` has `spectrum:deeper_down_portal` missing-item residue.

Repair these before expanding late tech questlines.

