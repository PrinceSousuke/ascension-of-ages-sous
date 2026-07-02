# Tech-Mod Coverage Verification — Census Correction (2026-07-02)

12 independent Opus verification passes over the IR/Gilded/OW/endgame tech-mod
families: jar truth (lang + recipes) + online mod docs + LIVE chapter grep +
AStages gate cross-check. Supersedes the tech-mod rows of
`mod_quest_coverage_census_2026-07-02.md`, whose methodology had four defects:

1. Counted quest NODES per chapter, not distinct item refs (Oritech "54" is
   really 115 distinct items; AE2 "14" is really ~193 family refs).
2. Missed `block_item` tasks and FTB Filter `smart_filter` tag refs entirely
   (RS "7 refs" is really ~48 family refs across 5 chapters).
3. Used raw model counts as scope (Electrodynamics "2116 models" counts
   blockstate multiparts; real item surface is 715. chemicalscience "909" is
   mostly per-planet ore + element decor).
4. Predates the 04 OW buildout (Draconic base/wyvern, QIO, advanced_ae,
   evolvedmek/mekmm quantum+multiversal, antimatter are now quested).

## Verdict table

| Family | Verdict | Real remaining gaps (bundled; details in per-mod file) |
|---|---|---|
| Immersive Engineering + IP + createaddition/new_age/diesel/oreexcavation | **CLOSED — no gaps** | none (census line void) |
| Mekanism core + generators + tools + additions | **ADEQUATE** | IR "personal kit" gear node; optional automation trio; 5x-loop prose beat; fusion logic_adapter fold-in |
| Mekanism addons (evolvedmek/mekmm/lasers/turrets/appmek) | **ADEQUATE** | at4: alloyer/chemixer/thermalizer + hypercharged→exoversal alloy chain (2 nodes); ow4: APT device + exotic QIO drives (2 nodes); mekmm CNC line (1-2 nodes) |
| PneumaticCraft (+appliedpneumatics) | **ADEQUATE** | the programmable-drone career (puzzles, roles, amadron, logistics frames) as 1-2 Gilded nodes; armor completion |
| Refined Storage family | **ADEQUATE** | extendedterminal (0 refs, full ladder) 1 Atomic node; small RS fabric bundle; 16384k disk |
| EnderIO + ProjectRed + Integrated* + morered | **ADEQUATE** | integratedtunnels import/export/interface node (the mod's core, unquested); ID on-ramp beat; place gated part_terminal_storage |
| Electrodynamics + nuclearscience + ballistix + voltaic + assemblyline | **ADEQUATE** | Electrodynamics endgame GEAR (~4 Atomic nodes: composite/combat armor, railguns, drill/chainsaw, hydraulic/servo, seismic); optional ballistix point-defense |
| Oritech (+things, compat) | **ADEQUATE + 1 defect** | fission reactor multiblock: 12 build parts unquested AND ungated = **bypass defect** (quest at Atomic + Atomic locks — bypass fix, not coverage gating); target_designator fold-in; optional exosuit |
| Modern Industrialization + EI + IO + HNI | **REAL GAPS (payoff layer)** | UU-matter/replicator fuel loop (OW); handheld ladder (steam→diesel→titanium drills, chainsaw, diesel jetpack); EI nano/nyano gear + nano_saber (Atomic→OW); gravichestplate (OW, superconductor-gated); IO vajra + terminal; quantum_circuit/robot_arm teach node |
| AE2 + extendedae + advanced_ae + megacells | **REAL GAP (entry chain)** | IR onboarding: certus/meteorite → inscriber + 4 presses → processors (3-4 nodes); network fabric (buses/interface/planes/P2P, ~3 bundles); cell ladder 4k-256k scale node — all in ir_digital_storage_foundations |
| chemicalscience / actuallyadditions / productivemetalworks / mifa / soph-storage / create_sa / immersive_machinery | **LEAVE / ACKNOWLEDGE** | only optional QoL beats (soph-storage upgrade cards; create_sa mobility stays ungated per flight policy) |
| Draconic awakened+chaotic / Draconic Additions / Re:Avaritia / Extended Crafting | **MAJOR GAPS → feeds 05 Ascension** | Avaritia neutron→singularity→infinity_catalyst spine + 9x9 extreme_crafting_table + catalyst input bundle; EC 5x5 advanced tier + alloy ladders (black_iron/luminessence/crystaltine/the_ultimate) + ultimate_singularity; DE reactor rotor parts, awakened/chaotic ladders, chaos-island economy, draconic/chaotic gear + staff; DA chaos processing loop. NOTE: singularities are ONE data-driven item id each (task the generic id, never per-metal). Infinity gear/necklaces/potato armor → reward tables, not quests |

## Standing facts for future passes
- Voltaic is a library+upgrades mod (0 blocks); its one g6 node is complete coverage.
- createoritechcompat adds zero items (recipe bridge only) — never a quest target.
- Mekanism fission (at3) vs createnuclear (at1) is intentional dual coverage.
- Oredictionificator/scuba/free_runners are deliberately ungated at IR.
- appmek chemical cells ride AE2 gating (at3), not the 01b addon file.
