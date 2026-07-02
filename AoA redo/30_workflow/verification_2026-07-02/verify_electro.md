# Electrodynamics family coverage verification — 2026-07-02

READ-ONLY census. All IDs jar-verified from item models + lang in the live `/mods` jars.

## Install truth (jars present)
- electrodynamics-1.21.1-1.0.9.jar (715 item models; **not** 2116 — census counted blockstate/multipart variants, not distinct items)
- voltaic-1.21.1-1.0.8.jar (16 items)
- nuclearscience-1.21.1-0.8.3.jar (91 items)
- ballistix-1.21.1-1.0.5.jar (127 items)
- assemblyline-1.21.1-0.8.2.jar (12 items)
- powergrid-mc1.21.1-0.5.5.1.jar, createnuclear-1.3.2-beta.3 (memory: **leave alone**)

## Web / progression truth (sources at bottom)
- **electrodynamics** = core aurilisdev tech mod (ore processing, wiring tiers, transformers, batteries, generators, gas handling, jetpack, composite armor, railgun). It is the *shared substrate* under NuclearScience / Ballistix / MFFS (the Voltz revival). It has **no fission reactor of its own** — that belongs to nuclearscience. So the census "very thin" read is wrong: it is the single most-quested mod of the family already.
- **voltaic** = **library + upgrade mod only**. Its entire non-guidebook surface is machine upgrades (speed/capacity/fortune/silk/unbreaking/experience/void/range/stator/solarcell) + a wrench. Ballistix "is based upon Voltaic and requires this mod." **0 blocks, no generators.** A single upgrade node is the correct and complete quest footprint. The "0 refs" census panic is void — 4 voltaic upgrade refs now live in g6.
- **ballistix** = ICBM/missile-silo/turret weapon mod on top of voltaic (+ optional nuclearscience/electrodynamics for realism). 3 launcher tiers, ~30 warheads, radar/CIWS defenses.
- **nuclearscience** = fission/fusion/molten-salt reactors, particle accelerator (antimatter), radiation gear.

## Per-mod verdict
| Mod | Census claim | Reality | Verdict |
|-----|--------------|---------|---------|
| electrodynamics | 41 refs, thin vs 2116 | ~38 distinct machines quested across 6 chapters; 715 real items not 2116 | **WELL COVERED** — machine spine complete; only gear/gadget tail missing |
| voltaic | 0 refs | pure upgrade/library mod; 4 upgrade refs now in g6 (added today) | **DONE** — nothing more is quest-worthy |
| nuclearscience | partial | full reactor/turbine/logistics/hazmat spine quested in at1–at4 + ow4 antimatter | **WELL COVERED** — only fuel-chain intermediates + radiation-consumables gap |
| ballistix | partial | warheads + 3 launcher tiers + radar quested in at5 + ow4 antimatter | **COVERED** — grenade/minecart/turret-defense tail missing |
| assemblyline | n/a | 10/12 quested in IR routing chapter | **DONE** — only storage-crate variants unquested (anti-bloat) |

## Beats table (chapter → age → what it teaches)
| Chapter | Age | Family content |
|---------|-----|----------------|
| ir_power_motion_and_grid | IR | electrodynamics basic generators/furnaces/wiremill/transformers/batterybox |
| ir_automation_safety_and_routing | IR | assemblyline conveyor/sorter/breaker/placer/detector/farmer |
| g1_the_golden_workshop / g2_the_refinery | Gilded | electrodynamics crushers, chemical mixer/reactor, electrolytic separator, oxidation furnace |
| g6_circuits_and_current | Gilded | electrodynamics circuits/current + **voltaic upgrades** (electrodynamics home) |
| at1_nuclear_dawn / at2_the_periodic_table | Atomic | electrodynamics thorium/uranium ore-processing bridge into nuclearscience |
| at3_chain_reaction / at4_machine_soul | Atomic | nuclearscience fission/fusion/MS reactor cores, turbine, logistics, hazmat, atomic assembler |
| at5_threshold_of_war | Atomic | ballistix launcher tiers 1–3, warhead families, radar |
| ow4_the_dyson_project | Otherworldly | nuclearscience antimatter cells + ballistix antimatter/largeantimatter/darkmatter (added today) |

## Gate audit (aoa_astages_01k_nuclear_power.js) — tiered, clean
- electrodynamics: basic furnaces/generators/wiremill/transformers/battery = **IR**; crushers/chemical/electrolytic/oxidation/advanced = **Gilded**; quarry/lathe/alloyer/motorcomplex/mineralwasher/HV charger = **Atomic**. No softlock (age ≥ recipe ceiling).
- nuclearscience: all reactor/turbine/logistics = **Atomic**.
- ballistix: all warheads/launchers/radar = **Atomic**; antimatter/largeantimatter/darkmatter/thermobaric = **Otherworldly**.
- assemblyline: all = **IR** (01l_tech_stragglers + 01_item_restrictions).
- voltaic: correctly ungated (library, no blocks).
Verdict: gates comprehensive and age-consistent; no missing locks on quest-relevant items.

## Ranked, jar-verified remaining gaps (bundled, anti-bloat applied)

### RANK 1 — electrodynamics endgame gear (real gap, one node each, Atomic-tier)
Currently only baton/jetpack/nightvision quested. Missing high-value combat/tool gear:
- **Combat + Composite armor** (`combatarmor{helmet,chestplate,leggings,boots}`, `compositearmor{helmet,chestplate,leggings,boots}` + `compositeplating`) — bundle as ONE "protective plating" node. Atomic.
- **Railgun** (`railgunkinetic`, `railgunplasma`) — one node, the mod's signature weapon. Atomic (plasma OW-adjacent — verify recipe ceiling before placing).
- **Powered tools**: `electricdrill`, `electricchainsaw`, `hydraulicboots`, `servoleggings` — one "powered outfit/tools" node. Gilded/Atomic.
- **Seismic prospecting**: `seismicscanner` + `seismicmarker` + `seismicrelay` — one ore-survey node (pairs with the quarry). Atomic.

### RANK 2 — ballistix defensive layer (optional depth, at5)
- Turret/CIWS defenses: `ciwsturret`, `samturret`, `laserturret`, `railgunturret`, `radargun`, `scanner`, `defuser`, `laserdesignator` — bundle as ONE "point-defense" node beside the existing radar. Atomic.
- Higher missile tiers: `missiletier2`, `missiletier3`, `missilecluster`, `aamissile(mk2)` — one "escalation" node (tier1 already quested). Atomic.
- **Skip** (anti-bloat): ~46 `minecart*` warhead variants, `grenade*` variants, `tracker_00..31` (internal), `bullet`, `landmine` — variant spam, not quest-worthy.

### RANK 3 — nuclearscience fuel-chain + radiation kit (optional, at2/at3)
- Fuel/isotope chain: `yellowcake`, `uranium235`, `uranium238`, `plutonium239`, `fuelplutonium`, `fissiledust`, `fissilesalt`, `polonium210`, `actinium225`, `flinak` — most are recipe intermediates; a single "enrichment chain" node if at3 wants it (verify yellowcake bridge, already flagged in memory).
- Radiation consumables/gear: `geigercounter`, `iodinetablet`, `antidote`, `radiationshielding{glass,door,trapdoor,base}` — one "radiation safety" node. Atomic.

### RANK 4 — assemblyline storage (skip)
- `crate`, `cratemedium`, `cratelarge` — decorative storage variants, anti-bloat, not quest-worthy.

## Bottom line
No softlocks, no gate holes, no age inversions. The census figures are misleading (2116 = variant count; 0 voltaic = a library mod now correctly touched). The only *real* content gap worth authoring is **electrodynamics endgame gear (Rank 1)** — a handful of bundled Atomic-tier nodes for armor/railgun/powered-tools/seismic. Everything else is optional depth or deliberate anti-bloat exclusion.

## Sources
- https://www.curseforge.com/minecraft/mc-mods/electrodynamics
- https://wiki.aurilis.dev/electrodynamics/
- https://github.com/aurilisdev/Electrodynamics
- https://www.curseforge.com/minecraft/mc-mods/ballistix
- https://wiki.aurilis.dev/ballistix/missile-silos/
- Jars: electrodynamics-1.0.9, voltaic-1.0.8, nuclearscience-0.8.3, ballistix-1.0.5, assemblyline-0.8.2 (item models + en_us.json)
- Gate: kubejs/server_scripts/aoa_astages_01k_nuclear_power.js, 01l_tech_stragglers.js, 01_item_restrictions.js
