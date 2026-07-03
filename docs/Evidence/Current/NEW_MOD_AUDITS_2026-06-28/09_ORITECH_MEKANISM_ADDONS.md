# Oritech, Mekanism, And Addon Audit

Sources:

- Oritech docs: https://moddedmc.wiki/hu/project/oritech/latest/docs
- Mekanism SPS: https://wiki.aidancbrady.com/wiki/Supercritical_Phase_Shifter
- Mekanism Fission Reactor: https://wiki.aidancbrady.com/wiki/Fission_Reactor
- Mekanism Fusion Reactor: https://wiki.aidancbrady.com/wiki/Fusion_Reactor

## Oritech

Jar: `mods/oritech-neoforge-1.21.1-1.2.8.jar`

Live coverage is strong in `g6_circuits_and_current.snbt`, `atomic_oritech_convergence.snbt`, and KubeJS AStages/weaves.

Already covered or strong:

- Particle Accelerator parts.
- Quantum Research Station.
- Assembler.
- Atomic Forge.
- Generators.
- Centrifuge.
- Bedrock Extractor.
- Drone Port.
- Stabilized Enchanter.
- Foundry.
- Fragment Forge.
- Laser Arm / Enderic Laser.
- Reactor Controller.
- Spawner Controller.
- Major machine cores and addon capstones.

Useful missing or undercalled targets:

- `oritech:charger_block`
- `oritech:energy_pipe`
- `oritech:fluid_pipe`
- `oritech:item_pipe`
- `oritech:pipe_booster_block`
- `oritech:pulverizer_block`
- `oritech:pump_block`
- `oritech:machine_core_1`, `_2`, `_3`
- `oritech:machine_frame_block`
- `oritech:machine_speed_addon`
- `oritech:machine_efficiency_addon`
- `oritech:machine_fluid_addon`
- `oritech:steam_engine_block`
- `oritech:steam_boiler_addon`
- Reactor components: `reactor_fuel_port`, `reactor_energy_port`, `reactor_heat_pipe`, `reactor_vent`, `reactor_rod`, `reactor_double_rod`, `reactor_quad_rod`, `reactor_reflector`.

Suggested shape:

| Quest | Target | Age | Why |
|---|---|---|---|
| Early Oritech Utilities | `oritech:charger_block`, pipes, pump | Industrial/Gilded | Teaches infrastructure before late machines. |
| Machine Core Ladder | cores 1 to 3, then existing higher core branch | Gilded | Smooths current jump into advanced cores. |
| Addon Literacy | speed/efficiency/fluid addon | Gilded optional | Representative, not every addon. |
| Oritech Reactor Lab | reactor ports/vents/rods | Atomic optional | Current Oritech reactor parts are undercalled. |

## Oritech Things

Jar: `mods/oritechthings-0.0.44.jar`

Live coverage is strong for capacitor tiers and accelerator sensor.

Only clear missing target:

- `oritechthings:frame_placer`

Do not quest every capacitor tier separately beyond existing coverage.

## Mekanism Core And Generators

Live coverage is substantial but not complete.

High-value missing or undercalled endgame targets:

- `mekanism:sps_casing`
- `mekanism:sps_port`
- `mekanism:supercharged_coil`
- `mekanism:antiprotonic_nucleosynthesizer`
- `mekanism:qio_drive_time_dilating`
- Antimatter pellet and polonium/plutonium throughput proof.
- MekaSuit/Meka-Tool modules only as representative capstones.

Suggested shape:

| Quest | Target | Age | Why |
|---|---|---|---|
| SPS Structure | `mekanism:sps_casing` plus `sps_port` | Otherworldly | Official Mekanism endgame antimatter machine. |
| Supercharged Coil | `mekanism:supercharged_coil` | Otherworldly | Prevents SPS from being a mystery box. |
| Antimatter Pellet | pellet or nucleosynthesizer | Otherworldly | Major FOMO target. |
| QIO Breakthrough | high-tier QIO drive | Otherworldly optional | Storage route after AE/RS. |

## MekMM

Jar: `mods/mekmm-1.21.1-1.3.1.jar`

Live coverage covers many basic to dense factory variants, but misses the late breaks.

High-value targets:

- `mekmm:replicator`
- `mekmm:chemical_replicator`
- `mekmm:fluid_replicator`
- `mekmm:ambient_gas_collector`
- `mekmm:large_electrolytic_separator`
- `mekmm:large_solar_neutron_activator`
- Quantum factory tier as a representative break.
- Multiversal factory tier as a representative break.

Quest rule: one representative factory per new tier is enough unless a factory type unlocks a unique system.

## Evolved Mekanism

Jar: `mods/Evolved Mekanism-1.21.1-1.2.1-fix3.jar`

KubeJS already gates many quantum and multiversal items. Questing should explain tier breaks, not every item.

Good targets:

- `evolvedmekanism:quantum_alloying_factory`
- `evolvedmekanism:multiversal_alloying_factory`
- Quantum/multiversal induction cell/provider as one storage proof.
- Quantum/multiversal universal cable as one transmission proof.

Do not quest every ore/mold/molten material.

## Applied Mekanistics And RS Mekanism Integration

Applied Mekanistics covered:

- `appmek:chemical_cell_housing`
- `appmek:chemical_storage_cell_1k`
- `4k`
- `16k`
- `64k`
- `256k`

Missing but useful:

- `appmek:chemical_p2p_tunnel`
- One portable chemical cell as optional storage QoL.

RS Mekanism Integration appears adequately covered for its chemical storage disk/part tiers. Do not add every size unless a storage branch needs one representative tier.

## Mekanism Lasers And Turrets

Mekanism Turrets are already covered through ultimate turret.

Mekanism Lasers are mostly covered; missing useful parts:

- `mekanism_lasers:energy_storage_port`
- `mekanism_lasers:energy_transformer`

Only add if the laser branch needs structure-completion guidance.

## Cross-Weave Candidates

- SPS requires Nuclear Science polonium/plutonium proof or Chemical Science shielding proof.
- Antimatter unlocks MekMM/Evolved quantum tier.
- Oritech Black Hole/unstable container can remain Ascension convergence, not broad duplication.
- AE2/AppMek chemical storage should bridge Nuclear Science waste/chemicals.
- Dynamic Electricity HV motor can be woven as an ingredient, not standalone questline.

## Do Not Quest

- Every Mekanism factory, tank, cable, bin, transporter, pipe, and color tier.
- Every Evolved Mekanism molten material or mold.
- Every MekMM factory type at every tier.
- Every Oritech pipe/duct/framed pipe variant.

## Verify Flags

- `[VERIFY]` exact JEI recipes for SPS and antimatter in this modpack after all KubeJS overlays.
- `[VERIFY]` MekMM replicator economy before making it a required route.
- `[VERIFY]` Oritech reactor behavior and fuel path in-game.
- `[VERIFY]` any QIO/AE/RS bridge target against live storage progression.

