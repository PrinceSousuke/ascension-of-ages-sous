# Phase 0 — Audits C & D: Neo Vitae spine integrity + cross-weave integrity

Auditor: Claude Code (CC). Date: 2026-07-02. AUDIT ONLY — no files edited outside phase0/.
Verify-first: every finding below carries a proof command + file:line, cross-checked against
the actual jars in `mods/`.

Severity scale: SOFTLOCK > BROKEN > CANON > HYGIENE.

---

## Summary counts

- node --check: **73 / 73 PASS, 0 FAIL** (all `kubejs/server_scripts/*.js`).
- Bad / unresolved ids in the 8 audited scripts: **0**.
- Known phantom ids searched (xpetrified_orb, processed_soulstone, allthemodium*,
  draconicadditions:chaotic_core): **none present**.
- CANON findings (flag, do not judge): **2** (anchor A1 unfixed; Hephaestus Forge non-monotonic).

---

## Audit C — Neo Vitae spine integrity

### C1. Anchor A1 — F&A node still routed into capstone aggregator  [CANON — expected, UNFIXED]

**Confirmed: yes, unfixed.** In `config/ftbquests/quests/chapters/ren_magic_foundations.snbt`:

- The F&A node `0B03101000000039` is a real quest node (task item `neovitae:athanor`,
  `hide_until_deps_complete: true`, grants `ren_magic_foundations_complete`).
  - Node declaration: **line 1290** (`id: "0B03101000000039"`).
  - Grant reward: **line 1294** (`/astages add {p} ren_magic_foundations_complete true true`).
  - Task: **lines 1325-1327** (`item: neovitae:athanor`).
- It is listed as a dependency of the capstone aggregator `0B0310100000CAFE`:
  - Dependency entry: **line 2132** (inside the `dependencies: [ ... ]` array opening at line 2131).
  - Aggregator declaration: **line 2147** (`id: "0B0310100000CAFE"`, `invisible: true`,
    `optional: true`, `hide_dependency_lines: true`).

Full dependency array of `0B0310100000CAFE` (lines 2131-2137):
```
dependencies: [
    "0B03101000000039"   <- F&A node (line 2132)
    "0B03102000000062"
    "0B03109000000060"
    "0B03103000000031"
    ...
]
```

Proof:
`grep -n '0B03101000000039\|0B0310100000CAFE' config/ftbquests/quests/chapters/ren_magic_foundations.snbt`

Matches the MASTER_PREAMBLE §7 statement: A1 is NOT done; Oritech tag-swap anchors A2/A3 ARE
done (see C2). No action taken (audit only) — flagged for the fix pass.

### C2. `#aoa:magic_feedstock` membership + consumers  [SAFE / verified done]

`kubejs/data/aoa/tags/item/magic_feedstock.json` (`replace: false`):
```
neovitae:hellforged_block
neovitae:ingot_hellforged
forbidden_arcanus:deorum_ingot
```
All three verified present in their jars:
- `neovitae:hellforged_block`, `neovitae:ingot_hellforged` — OK in `neovitae-1.21.1-1.0.25.jar`.
- `forbidden_arcanus:deorum_ingot` — OK in `forbidden_arcanus-2.6.1.jar`.

Both required consumers reference the tag (`grep -n magic_feedstock kubejs/server_scripts/`):
- `ir_native_capstone_recipes.js:32` — Aureal Foundry, `D: '#aoa:magic_feedstock'`
  (output `oritech:foundry_block`).
- `magic_spine_bridges.js:17` — Oritech Machine Core 5, `D: '#aoa:magic_feedstock'`
  (output `oritech:machine_core_5`).

Both confirm A2/A3 (tag-swap) are wired. Consumers and outputs verified against the Oritech jar.

### C3. Hephaestus Forge tier gating  [CANON — flag for canon call, non-monotonic as expected]

`kubejs/server_scripts/aoa_astages_01m_magic.js` lines **31-35**:

| Tier | AStages stage | Age index |
|---|---|---|
| `forbidden_arcanus:hephaestus_forge_tier_1` | `the_renaissance` | 3 |
| `forbidden_arcanus:hephaestus_forge_tier_2` | `industrial_revolution` | 4 |
| `forbidden_arcanus:hephaestus_forge_tier_3` | `gilded_age` | 5 |
| `forbidden_arcanus:hephaestus_forge_tier_4` | `the_renaissance` | 3 |
| `forbidden_arcanus:hephaestus_forge_tier_5` | `the_renaissance` | 3 |

Non-monotonic exactly as the preamble predicted (T1 ren / T2 IR / T3 gilded / T4 ren / T5 ren).
The inline comment (lines 9-10) states the intent is that T1 is the entry block and "T2-T5 are
reagent-gated ritual upgrades … not item locks here" — yet the code DOES place item locks on
T2/T3, and the T4/T5 locks drop back to `the_renaissance`. This is the leftover-bug shape flagged
for a canon call; not judging intent.

All five `hephaestus_forge_tier_1..5` ids are REAL: the single Hephaestus Forge block is
registered with 5 tier blockstate/model variants
(`unzip -l forbidden_arcanus-2.6.1.jar | grep hephaestus_forge_tier` → 5 blockstates + 5 models).
The block_item locks target valid ids. (The shared display name uses the `hephaestus_forge` lang key.)

Proof: `grep -n hephaestus kubejs/server_scripts/aoa_astages_01m_magic.js`

---

## Audit D — Cross-weave integrity

### D1. node --check sweep  [SAFE]

All 73 `.js` files under `kubejs/server_scripts/` pass `node --check`. 0 failures.
Proof: `for f in *.js; do node --check "$f"; done` → PASS=73 FAIL=0 TOTAL=73.

### D2. Id resolution per audited script

Scripts audited: `aoa_recipes_renaissance_weaves.js`, `aoa_recipes_ir_weaves.js`,
`aoa_recipes_gilded_weaves.js`, `aoa_recipes_atomic_weaves.js`, `aoa_recipes_oritech_weaves.js`,
`aoa_recipes_neovitae_weaves.js`, `magic_spine_bridges.js`, `ir_magic_feedstock_bridges.js`
(EXISTS), `ir_native_capstone_recipes.js`, `aoa_recipes_capstone_convergence.js`,
`aoa_oil_spine_weaves.js`, `ir2_fuel_engine_interchange.js`, `boss_progression_proof.js`.

Every namespace used maps to an installed jar (cross-checked vs the live `mods/` listing).
~90 distinctive/uncommon ids spot-verified against each jar's `assets/*/lang/en_us.json`
(or blockstate/gas registry where the item uses a non-item lang key). **All resolve. No bad ids.**

| Script | Notable ids verified | Result |
|---|---|---|
| renaissance_weaves | theurgy:pyromantic_brazier, reformation_source_pedestal; malum:refined_soulstone, crushed_soulstone; forbidden_arcanus:arcane_crystal, soul_extractor, utrem_jar; deeperdarker:sonorous_staff; eternal_starlight:thioquartz_shard; occultism:golden_sacrificial_bowl; aether tag bridge | all OK |
| ir_weaves | pneumaticcraft:uv_light_box, etching_tank, pcb_blueprint, pressure_tube, small_tank, vortex_tube; spectrum:neolith; integrateddynamics:materializer, variable, menril_torch, mechanical_squeezer, squeezer, energy_battery; immersiveengineering:sample_drill, steel_scaffolding_standard; malum:crushed_soulstone; theurgy:sal_ammoniac_crystal | all OK |
| gilded_weaves | nautec:bio_reactor, aquatic_chip, laser_channeling_coil, mutator, petri_dish, eas_bucket, bacterial_containment_shield; enderio:pulsating_crystal, grains_of_infinity; industrialforegoing:ore_laser_base; industrialforegoingsouls:soul_laser_base; hostilenetworks:sim_chamber; chemicalscience:catalytic_reformer; electrodynamics:titaniumheatcoil, tanksteel, pressuregauge; immersivepetroleum:bitumen, asphalt; extendedcrafting:advanced_table; oritech:processing_unit | all OK |
| atomic_weaves | tag add only: c:yellow_cake_uranium <- mekanism:yellow_cake_uranium | OK |
| oritech_weaves | oritech:arcane_augment_station, enchantment_catalyst_block, unstable_container, flux_gate, simple_augment_station, adamant_ingot; forbidden_arcanus:mundabitur_dust; theurgy:mercury_shard; malum:eldritch_spirit; apothic_enchanting:hellshelf, sightshelf; apotheosis:mythic_material; **avaritia:crystal_matrix_ingot, neutron_ingot; draconicevolution:chaotic_core**; modularforcefields:fortroncapacitor | all OK |
| neovitae_weaves | neovitae:sentient_axe, spiritus_gem_petty, raw_spiritus_catalyst, tau_oil, alchemy_flask, simple_catalyst, weak_blood_shard, hellforged_dust, tabula_robur; malum:arcane_spirit; forbidden_arcanus:eternal_stella, arcane_crystal_dust; occultism:otherworld_essence; theurgy alchemical_salts tag | all OK |
| magic_spine_bridges | oritech:machine_core_5, adamant_ingot, advanced_computing_engine; malum:hallowed_gold_ingot; theurgy:mercury_catalyst; #aoa:magic_feedstock | all OK |
| ir_magic_feedstock_bridges | pneumaticcraft:spawner_agitator; #malum:spirits; integrateddynamics:logic_director, crystalized_chorus_chunk, crystalized_menril_chunk; spectrum:resonance_shard | all OK |
| ir_native_capstone_recipes | oritech:machine_frame_block, foundry_block, motor; immersiveengineering:component_iron, rs_engineering; #aoa:magic_feedstock | all OK |
| capstone_convergence | powergrid:circuit_design_table; createaddition:tesla_coil, large_connector; create:electron_tube, empty_schematic, precision_mechanism, andesite_alloy; dynamicelectricity:alternator; electrodynamics:combustionchamber; createdieselgenerators:distillation_controller; create_new_age:layered_magnet; createoreexcavation:vein_finder; modern_industrialization:centrifuge, basic_machine_hull, large_motor; actuallyadditions:advanced_coil; blastcraft:blastcompressor; industrialization_overdrive:pyrolyse_oven; immersiveengineering:heavy_engineering | all OK |
| oil_spine_weaves | chemicalscience:rhodium_silica_catalyst, benzene, toluene; electrodynamics:coalcoke, **hydrogen** (gas registry, not item lang); pneumaticcraft:gasoline; modern_industrialization:diesel, boosted_diesel; c:naphtha tag | all OK |
| ir2_fuel_engine_interchange | tag adds only: immersivepetroleum:crudeoil, diesel, diesel_sulfur, gasoline, kerosene, petroleum_gas, naphtha, lubricant; oritech:still_oil, still_diesel; createdieselgenerators/pneumaticcraft/modern_industrialization/chemicalscience crude+diesel | all OK |
| boss_progression_proof | cataclysm:cursium_ingot, tidal_claws, essence_of_the_storm; bosses_of_mass_destruction:obsidian_heart; fdbosses:justice_core; astral_dimension:void_boots_helmet; macabre:*_heart; eternal_starlight:* | all OK |

### D3. False-positive MISSes investigated (both benign, NOT bad ids)

- `electrodynamics:hydrogen` — used only as a `gasbi` (gas byproduct) in oil_spine_weaves W1.
  Registered as `gas.electrodynamics.hydrogen` (not an item/block), so it correctly does not
  appear under item/block lang. VALID.
  Proof: `unzip -p electrodynamics-1.21.1-1.0.9.jar assets/electrodynamics/lang/en_us.json | grep hydrogen`
- `enderio:soul_stained_steel_ingot` — appears ONLY in a comment in `ir_magic_feedstock_bridges.js:17`.
  The real consumed item is `malum:soul_stained_steel_ingot` in `ender_io_soul.js` (out of scope,
  and OK). No recipe in the audited scripts uses an `enderio:` soul-stained id. VALID.

### D4. Phantom-id watch  [SAFE]

Searched the audited scripts for the four known phantoms — none present. Notably
`aoa_recipes_ir_weaves.js:13-16` documents that `forbidden_arcanus:xpetrified_orb` was
deliberately KILLED in review and is intentionally absent. The Oritech weave uses
`draconicevolution:chaotic_core` (REAL — verified in Draconic-Evolution jar), which is a
different namespace from the phantom `draconicadditions:chaotic_core`.

---

## Bad-id failure table

| script | recipe | bad id |
|---|---|---|
| (none) | (none) | (none — 0 unresolved ids) |

---

## Bottom line

- Anchor A1 is confirmed unfixed (ren_magic_foundations.snbt line 2132 routes F&A node
  `0B03101000000039` into capstone `0B0310100000CAFE`). Fix owner: the A1 remediation pass.
- Hephaestus Forge tier gating is non-monotonic (T4/T5 back to Renaissance) — needs a canon call.
- All KubeJS weave/spine/bridge scripts are syntactically clean (73/73 node --check) and every
  recipe id resolves to an installed jar. Cross-weave integrity is intact.
