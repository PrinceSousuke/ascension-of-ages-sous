# Mekanism Quest-Coverage Verification (READ-ONLY)

Pack: Ascension of Ages, NeoForge 1.21.1. Jars: `Mekanism-1.21.1-10.7.19.85` +
`MekanismGenerators` / `MekanismTools` / `MekanismAdditions` (same version). Evolved Mekanism
is also installed but out of scope for this census.

## Verdicts

| Mod | Census refs | Real verdict |
|---|---|---|
| **mekanism** (base) | 69 | **ADEQUATE with a few real gaps** — the machine tree is questbook-covered end to end (IR ore-works entry, at2 periodic table, ow4 QIO/teleport). Genuine holes are narrow: the 5x ore-processing *loop* isn't taught as a tier, and a small cluster of survival-QoL gear (jetpack/scuba/free-runners) has zero quest home. |
| **mekanismgenerators** | 26 | **ADEQUATE** — heat/bio/solar/wind (g6), gas-burning (at1), fission reactor + turbine (at3), fusion (ow6) are all quested. Only fuel-fluid intermediates are unquested, which is correct (fluids aren't task items). |
| **mekanismtools** | 25 | **ADEQUATE** — osmium (g1), steel/lapis (IR hidden gear), bronze/diamond paxels (g1), refined obsidian/glowstone armor + paxel (at5). Full tier ladder is represented. No action. |
| **mekanismadditions** | 0 | **CORRECTLY UNQUESTED** — 296 lang entries, ~290 are plastic decor / glow panels / balloons / walkie-talkies. Cosmetic. Do not quest (would be filler per CANON section 3/4). |

**Bottom line:** the census "69 vs a huge tree" framing is stale. Base Mekanism is
genuinely one of the most thoroughly quested mods in the pack — 245 raw ref-matches across
13 chapters. The remaining gaps are small and specific, not a coverage collapse.

## Where Mekanism is quested (live state, verified on disk)

| Chapter | Age | What it covers |
|---|---|---|
| `ir_mekanism_ore_works` | IR | 42 nodes. Core machine fleet: enrichment, crusher, energized smelter, osmium compressor, purification (3x), electrolytic separator, chemical injection (4x), chemical infuser, PRC, metallurgic infuser, thermal-evap controller, basic factory tier (smelt/enrich/crush). |
| `ir_ir_side_gear_hidden_equipment` | IR | steel + lapis armor, wood/stone paxel (hidden gear line). |
| `g1_the_golden_workshop` | Gilded | osmium armor set, bronze + diamond paxel. |
| `g6_circuits_and_current` | Gilded | heat/bio/solar/adv-solar/wind generators, solar panel, atomic disassembler. |
| `g_power_beyond_wires` | Gilded | atomic disassembler (weave). |
| `at1_nuclear_dawn` | Atomic | uranium ore→ingot chain, hazmat suit (4pc), gas-burning generator. **createnuclear** fission is the atomic entry here (26 refs). |
| `at2_the_periodic_table` | Atomic | 5x-tier machines (dissolution/washer/crystallizer/oxidizer), isotopic centrifuge, solar neutron activator, digital miner, dimensional stabilizer, quantum entangloporter, induction matrix (casing/port/cell/provider), bin/tank/energy-cube tiers (adv→ultimate), elite/ultimate control circuits, universal cable tiers. |
| `at3_chain_reaction` | Atomic | **Mek fission reactor** (casing/port/fuel-assembly/control-rod/logic-adapter), **industrial turbine** (casing/rotor/blade/vent/valve/complex/condenser/coil), boiler (casing/valve), SPS (casing/port/supercharged coil), polonium + antimatter pellets. |
| `at4_machine_soul` | Atomic | factory upper tiers (adv/elite/ultimate smelting) + advanced tier installer. |
| `at5_threshold_of_war` | Atomic | MekaSuit (4pc) + MekaTool, modification station, 3 modules (attack/jetpack/radiation-shield), laser fleet (laser/amplifier/tractor-beam), flamethrower, refined obsidian + glowstone armor/paxel. |
| `ow4_the_dyson_project` | OW | full QIO suite (dashboard/drive-array/4 drive tiers/importer/exporter/redstone-adapter/portable dashboard), teleporter + frame + portable teleporter, antiprotonic nucleosynthesizer. |
| `ow6_beyond_the_veil` | OW | **fusion reactor** (controller/frame/port/logic-adapter), laser focus matrix, hohlraum. |
| `journey_to_ascension` | (mirror) | atomic disassembler, fission casing, hohlraum mirrors. |

## Gate reality (from `kubejs/server_scripts/aoa_astages_*.js`)

Verified stages for placement discipline:
- **IR:** all base machines incl. purification/injection chambers, rotary condensentrator,
  precision sawmill, combiner, all *basic* factories, formulaic assemblicator, security desk,
  jetpack, resistive heater, electric pump, dynamic tank.
- **Atomic:** chemical dissolution chamber, digital miner, solar neutron activator, uranium
  chain, advanced/elite/ultimate factory tiers.
- **Otherworldly:** QIO, teleporter, fusion, antiprotonic nucleosynthesizer.
- **UNGATED (free at IR by recipe):** `oredictionificator`, `scuba_mask`, `scuba_tank`,
  `free_runners`. Placement of any new quest for these = IR/Gilded.

## Ranked, jar-verified gap list (real, non-filler)

Noise excluded from "gaps": fluids (brine/chlorine/steam/oxygen/hydrogen/sulfuric acid/
heavy water/lithium/sodium/ethene), upgrade items, cardboard box, configurator/dictionary/
network reader, universal-cable/pipe/tube/transporter families, dye/pigment machines,
seismic reader/vibrator, painting machine, robit, salt/fluorite/substrate intermediates —
these are support items, not chapter-worthy standalone quests.

### Rank 1 — 5x ore-processing loop is placed but never TAUGHT as a tier (base) [ATOMIC]
The at2 chapter drops `chemical_dissolution_chamber`, `chemical_washer`,
`chemical_crystallizer`, `chemical_oxidizer`, `rotary_condensentrator` as isolated
single-item nodes. The 2x/3x/4x ladder is taught coherently in `ir_mekanism_ore_works`,
but the crowning 5x quintupling loop (slurry → clean slurry → crystal → shard → 5 ingots)
is not explained anywhere. Wiki-canonical order: dissolution → washer → crystallizer feeds
back into the 4x injection line.
- **Fix:** one bundled at2 quest "Quintupled Ore" wiring dissolution+washer+crystallizer+
  rotary as a taught loop (or a short prose beat on an existing node). Machines already
  exist as tasks; this is prose/bundling, not new item tasks. Low effort, high payoff.
- IDs (already present): `mekanism:chemical_dissolution_chamber`, `:chemical_washer`,
  `:chemical_crystallizer`, `:rotary_condensentrator`, `:chemical_oxidizer`.

### Rank 2 — Survival-QoL gear cluster has NO quest home (base) [IR / Gilded]
Genuinely unquested, useful, real gear items:
- `mekanism:jetpack` (IR-gated) + `mekanism:jetpack_armored` (IR)
- `mekanism:scuba_mask` + `mekanism:scuba_tank` (UNGATED → IR)
- `mekanism:free_runners` (UNGATED → IR) + `mekanism:free_runners_armored`
- `mekanism:canteen` + `mekanism:nutritional_liquifier` + `:nutritional_paste` (IR)
- **Fix:** one small IR "Personal Kit" node bundling jetpack + free-runners + scuba set
  (thematic: early mobility/dive gear before MekaSuit at atomic). 3–4 item tasks max, not
  a chapter. Bundles sensibly with the existing IR hidden-gear line.

### Rank 3 — Storage & sorting utility trio (base) [IR]
`mekanism:logistical_sorter`, `mekanism:oredictionificator` (ungated),
`mekanism:formulaic_assemblicator` (IR, gated but unquested), `mekanism:personal_chest`/
`:personal_barrel`. These are the automation-glue players actually build. Optional single
bundled IR node "Automation Desk" (sorter + oredictionificator + assemblicator). Skip if
density is a concern — borderline support-tier.

### Rank 4 — Fusion fuel prep chain intermediates (generators) [OW]
`mekanismgenerators:deuterium`, `:tritium`, `:fusion_fuel`, `:bioethanol` are fluids/buckets
and the `fusion_reactor_logic_adapter` block is unquested. The logic adapter is the only
real non-fluid miss. Minor — fold into the existing ow6 fusion node as one extra task.
Fluids stay unquested (correct).

### Explicitly NOT gaps (do not author)
- All `mekanismadditions` plastic/decor/balloon/walkie content — cosmetic, filler if quested.
- `mekanismtools` — full tier ladder already covered; no holes.
- Fluids, upgrades, pipes/cables/tubes, robit, seismic, pigment/dye/painting machines,
  cardboard box, dosimeter/geiger (support instruments; geiger fits at1 prose if desired but
  not a standalone need).
- fission vs createnuclear: **both intentionally quested** — createnuclear is the at1 atomic
  *entry* reactor, mek fission is the at3 *mainline*. Not a conflict, not a duplicate.

## Sources
- Official Mekanism Wiki, Ore Processing: https://wiki.aidancbrady.com/wiki/Ore_Processing
- Purification Chamber: https://wiki.aidancbrady.com/wiki/Purification_Chamber
- Chemical Dissolution Chamber: https://wiki.aidancbrady.com/wiki/Chemical_Dissolution_Chamber
- Advanced Ore Processing Setup: https://wiki.aidancbrady.com/wiki/Tutorials/Advanced_Ore_Processing_Setup
- Jar truth: `mods/Mekanism-1.21.1-10.7.19.85.jar` (+Generators/Tools/Additions) lang json, extracted 2026-07-02.
- Live gates: `kubejs/server_scripts/aoa_astages_01_item_restrictions.js`, `01b_mekanism_addon_machines.js`, `01j_storage.js`, `01p_gap_closure.js`.
