# Mekanism-Addon Coverage Verification (jar-truth, live re-count)

Date: 2026-07-02. READ-ONLY verifier. Sources: mod jars (lang), live chapters, AStages gate 01b, scope registry, web.

## TL;DR
The census (evolvedmek 6 / mekmm 10 / lasers 6 / turrets 4 / appmek 2, "all thin") is **stale and undercounts**. Live re-count shows these are the SECOND-most-quested addon family in the pack after core Mekanism. The middle atomic tiers (overclocked/dense) are NOT "gated atomic and quested nowhere" — a representative slice is already built in at4 + a full quantum/multiversal tree in **ow4** (there is no ow5; the prompt's "ow5" = **ow4 The Dyson Project**). The genuine remaining gaps are narrow and specific: the standalone alloy machines, the top alloy chain, the 4 QIO drives, and the APT capstone device.

---

## Gate map (from aoa_astages_01b, header + entries) — AUTHORITATIVE
Tier ladder is `basic → advanced → elite → ultimate → overclocked → dense → quantum → multiversal → creative` (Evolved Mek's own 5 new tiers are overclocked/quantum/dense/multiversal/creative; note overclocked and dense come BEFORE quantum in the mod's power order but are both era-floored the same).

| Tier band | AStages age | Notes |
|---|---|---|
| basic / advanced / elite / ultimate / **overclocked** / **dense** | **atomic** | soft item-lock (hidden JEI, no place) |
| **quantum** / **multiversal** | **otherworldly** | soft item-lock |
| creative | (not addon-locked; excluded) | main-file / creative excluded |

So there is NO "middle tier gated atomic quested nowhere" band — overclocked+dense ARE the atomic band, and at4 already builds representative overclocked/dense/solidification machines. quantum+multiversal are the OW band, fully covered in ow4.

---

## Per-mod verdict

### evolvedmekanism — VERDICT: well-covered; small real gap (alloy machines + alloy chain + QIO + APT)
Jar tier evidence: factories in {combining, compressing, crushing, enriching, infusing, injecting, purifying, sawing, smelting, alloying, chemixing} × 9 tiers; storage {bin, chemical_tank, fluid_tank, induction_cell, induction_provider, energy_cube}; transmitters {logistical_transporter, mechanical_pipe, pressurized_tube, universal_cable, thermodynamic_conductor}; solar {advanced..multiversal solar_generator + solar_panel items}; standalone machines **alloyer / chemixer / thermalizer / solidification_chamber**; alloy chain **infused → reinforced → atomic (vanilla Mek) → hypercharged → subatomic → singular → exoversal → creative**; circuits overclocked/quantum/dense/multiversal/creative; tier installers overclocked/quantum/dense/multiversal/max/creative; QIO drives **boosted / singularity / hypra_solidified / black_hole / creative**; APT device = casing + port + **supercharging_element** (up to 25 for speed, per CurseForge); metals better_gold / plaslitherite / refined_redstone; molds; radioactive+solar upgrades.

Quested live: dense_enriching, overclocked_enriching, solidification_chamber, apt_casing, ultimate_personal_chest, ultimate_solar_generator (+ solar filter advanced/elite/dense/overclocked/ultimate) in **at4**; quantum + multiversal {alloying, enriching, smelting, crushing, bin, fluid_tank, chemical_tank, universal_cable, induction_cell, induction_provider} in **ow4**.

### mekmm — VERDICT: well-covered; gap = the CNC/replicator machine identities
Jar machine TYPES (each × 9 tiers as `*_factory` + a base station): oxidizing, chemical_infusing, dissolving, washing, crystallizing, pressurised_reacting, centrifuging, liquifying, recycling (base `recycler`), planting (base `planting_station`), stamping (base `cnc_stamper`), lathing (base `cnc_lathe`), rolling_mill (base `cnc_rolling_mill`), replicating (base `replicator` + `fluid_replicator` + `chemical_replicator`). Standalone: ambient_gas_collector, wireless_charging_station, wireless_transmission_station, large_* {rotary_condensentrator, chemical_infuser, electrolytic_separator, solar_neutron_activator, heat_generator, gas_burning_generator}, mid/max chemical tanks × 4 tiers. Items: scrap, scrap_box, empty_crystal, uu_matter, connector, advanced_electrolysis_core. Chemicals: nutritional_paste, nutrient_solution, uu_matter, unstable_dimensional_gas.

Quested live: ultimate_max_chemical_tank + tank filter (8 tiers) in at2; large_gas_burning_generator + large_heat_generator in at3; basic_oxidizing, planting_station, recycler, large_chemical_infuser, large_rotary_condensentrator, wireless_charging_station, wireless_transmission_station in at4; quantum/multiversal {centrifuging, crystallizing, pressurised_reacting} in ow4.

### mekanism_lasers — VERDICT: covered for its distinctive blocks; nothing meaningful missing
Jar: lasers basic/advanced/elite/ultimate/creative (+ toggleable variants), laser_stopper, laser_splitter, energy_transformer, energy_storage {casing, port, cell} multiblock, **ore_generator** (ODECM — light→ore duplication), interface_block, remote_control, energized_fence.
Quested live (at2): elite_laser, laser filter (all 8), laser_splitter, laser_stopper, energy_storage_casing, energy_storage_cell, ore_generator. Only energy_transformer / interface_block+remote_control / energized_fence unbuilt — low-signal control glue, correctly skipped.

### mekanism_turrets — VERDICT: fully covered
Jar: laser_turret basic/advanced/elite/ultimate + electric_fence. NO ammo item (energy-per-shot only). Quested live: all 4 turret tiers built individually in at5. electric_fence is the only omission (redundant with lasers' energized_fence). Done.

### appmek — VERDICT: covered enough; one optional gap
Jar: chemical_cell_housing; chemical_storage_cell 1k/4k/16k/64k/256k; portable_chemical_cell ×5; **chemical_p2p_tunnel**. (No "chemical interface / pattern provider" exists — those are AE2's; the "pattern" chapter hits are AE2, not appmek.) Memory note "appmek cells ATOMIC-gated" — cells are NOT in 01b; they ride AE2's own gating in at3.
Quested live: chemical_cell_housing + chemical_storage_cell_64k + 5-tier cell filter in at3; portable_chemical_cell filter (5) in at4. Missing: **chemical_p2p_tunnel** only.

---

## Ranked jar-verified GAP LIST (bundled; no one-quest-per-machine)

**G1 — Evolved Mek standalone alloy line + alloy chain (ATOMIC).** HIGH value: this is the actual crafting substrate the tier ladder rides on, and it's entirely absent.
- Machines: `evolvedmekanism:alloyer`, `evolvedmekanism:chemixer`, `evolvedmekanism:thermalizer` (thermalizer/solidification pair; solidification already quested).
- Alloy chain items: `evolvedmekanism:alloy_hypercharged`, `alloy_subatomic`, `alloy_singular`, `alloy_exoversal`.
- Suggested home: **at4 Machine Soul** (new bundled node "The Alloy Line" — 1 machine-cluster quest + 1 alloy-progression quest). Age: atomic. Bundled = 2 nodes.

**G2 — APT capstone device (OTHERWORLDLY-adjacent / atomic-late).** HIGH flavor value: the APT is the 7th-tier crafting core (makes exoversal/multiversal circuits). apt_casing is quested but the device itself is not.
- Items: assemble via `evolvedmekanism:apt_casing` (built) + `apt_port` + `supercharging_element`; product tier installers `quantum_tier_installer` / `dense_tier_installer` / `multiversal_tier_installer` / `max_tier_installer`, `multiversal_control_circuit`.
- Suggested home: **ow4 The Dyson Project** (single "Antimatter Transmutator" node feeding the existing quantum/multiversal tree). Age: otherworldly. Bundled = 1 node (2 tasks: build APT, use it for one multiversal circuit/installer).

**G3 — QIO drive ladder (OTHERWORLDLY).** MEDIUM: distinctive Evolved-Mek storage endgame; qio_drive already appears in ow4 (Mekanism base QIO) so this is a natural extension, not a new area.
- Items: `evolvedmekanism:qio_drive_boosted`, `qio_drive_singularity`, `qio_drive_hypra_solidified`, `qio_drive_black_hole`.
- Suggested home: **ow4** existing QIO cluster (one bundled "Boosted QIO Drives" node, filter-style over the 4 drives). Age: otherworldly. Bundled = 1 node.

**G4 — mekmm CNC/replicator machine identities (ATOMIC).** MEDIUM: five distinctive base stations with unique mechanics (mold stamping, lathe, rolling mill, UU-matter replication) currently unbuilt at their base tier; only oxidizing/planting/recycler represent mekmm processing in at4.
- Items: `mekmm:cnc_stamper`, `cnc_lathe`, `cnc_rolling_mill`, `replicator` (+ `fluid_replicator`, `chemical_replicator`), `ambient_gas_collector`; support `uu_matter`, `empty_crystal`, `scrap_box`.
- Suggested home: **at4 Machine Soul** (one bundled "CNC & Replication" node: 1 CNC-cluster task + 1 replicator task). Age: atomic. Bundled = 1–2 nodes.

**G5 — Multiversal solar + dense/multiversal transmitters (OTHERWORLDLY).** LOW: completeness only; solar filter stops at ultimate, quantum/multiversal solar unbuilt.
- Items: `evolvedmekanism:multiversal_solar_generator` (+ quantum), quantum/multiversal `mechanical_pipe`/`pressurized_tube`/`logistical_transporter` if a node wants breadth.
- Suggested home: fold into **ow4** solar/logistics node as filter variants. Age: otherworldly. Bundled = 0–1 node (extend existing filter).

**G6 — appmek chemical P2P tunnel (ATOMIC, with AE2).** LOW/optional.
- Item: `appmek:chemical_p2p_tunnel`.
- Suggested home: **at3** appmek cell node as an extra task, OR skip (P2P is niche). Bundled = 0 (add as task, not a node).

### Explicitly NOT gaps (do not author)
- Per-tier factory quests for every processing type × 9 tiers (padding; filters already cover breadth).
- mekmm dolls (author_doll/modeler_doll — decoration), connector, is_blocking glue.
- lasers energy_transformer/interface/remote/energized_fence, turrets electric_fence (low-signal control blocks).
- Molten-fluid buckets (100+ cosmetic fluids), molds beyond one representative, ore variants (depthrock/end/holystone/etc. are worldgen, ride Mek ore gating).

---

## Corrections to standing notes
- **Census is void** for "thin" — replace with: evolvedmek ~26 live refs, mekmm ~14, lasers ~10 (incl. 8-way filter), turrets 4, appmek ~11 (incl. 2 filters). All ATOMIC/OW placements match gate 01b; no cross-age inversion.
- **"ow5 expanded today"** = **ow4 The Dyson Project** (no ow5 file exists). Quantum/multiversal bundles confirmed present there.
- **Memory "appmek cells ATOMIC-gated"**: cells are NOT in 01b; they are placed in at3 riding AE2 gating. Harmless but note the gate source.

Sources: mod jars (lang/en_us.json for all 5); `kubejs/server_scripts/aoa_astages_01b_mekanism_addon_machines.js`; live `config/ftbquests/quests/chapters/{at2,at3,at4,at5,ow4}`; `AOA_QUEST_SCOPE_REGISTRY.md`; [Evolved Mekanism CurseForge](https://www.curseforge.com/minecraft/mc-mods/evolved-mekanism); [Mekanism Antimatter wiki](https://wiki.aidancbrady.com/wiki/Antimatter).
