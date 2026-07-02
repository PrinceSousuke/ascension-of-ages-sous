# MI-family Coverage Verification — Ascension of Ages

Read-only census. JAR truth (v2.5.0 + addons), live gates, live FTBQ state as of 2026-07-02.
Registry bar: `modern_industrialization` + `extended_industrialization` get **"thorough endgame
treatment / deep complete coverage (tentpole endgame trees)"** (AOA_QUEST_SCOPE_REGISTRY §3).

## Verdicts

| Mod | modId | Verdict |
|---|---|---|
| Modern Industrialization 2.5.0 | `modern_industrialization` | **REAL GAPS** — machine/multiblock/tier ladder is thorough; portable tools, wearable gear, and the UU-matter/singularity/replication capstone loop are entirely UNTASKED |
| Extended Industrialization 1.15.43 | `extended_industrialization` | **REAL GAPS** — machines/tesla/solar well covered; the nano/nyano armor + nano_saber gear ladder is UNTASKED |
| Industrialization Overdrive 1.11.2 | `industrialization_overdrive` | **REAL GAPS** — pyrolyse_oven + multi_processing_array tasked; the two flagship tools (Vajra, Multiblock Builder terminal) UNTASKED |
| Hostile Neural Industrialization 1.0.15 | `hostile_neural_industrialization` | **ADEQUATE** — all 5 blocks (both simulation chambers, both loot fabricators, prediction casing) tasked in at4 |

The 118-ref "PARTIAL" census is right that MI isn't done, but wrong about where. The **machine
voltage ladder is essentially complete** across IR→OW. What's missing is the **player-facing
payoff layer**: drills/chainsaws/jetpack, the quantum/gravi/nano armor sets, and the
singularity→UU-matter→replicator endgame — the exact content the MI wiki calls "The Endgame."

## Tier-by-tier evidence (machines/multiblocks — the covered spine)

| Tier / Age (per gates) | Signature content (jar) | Quested? (chapter) | Gap |
|---|---|---|---|
| LV Bronze/Steel — **IR** | forge_hammer, bronze+steel macerator/compressor/mixer/cutting/furnace, coke_oven, steam_blast_furnace, EBF, assembler, large_steam_boiler, large_tank, steam_quarry, lv_steam_turbine, lv_diesel_gen | YES — `ir_modern_industrialization_steam_industry` (74 refs) | none (machines) |
| MV/HV Alu/Stainless — **Gilded** | distillation_tower, vacuum_freezer, distillery, heat_exchanger, pressurizer, centrifuge, chemical_reactor, electrolyzer, oil_drilling_rig, large_steam_turbine, mv/hv turbines+diesel, coils/transformers, pyrolyse_oven | YES — `g5_empire_of_iron` (77 refs) + tesla/solar/processing_array in `g6_circuits_and_current` | none (machines) |
| EV Titanium — **Atomic** | implosion_compressor, nuclear_reactor + nuclear casings/hatches, large_diesel_generator, EV hatches/transformer, highly_advanced hull/casing | YES — `at3_chain_reaction`, `at4_machine_soul` | none (machines) |
| Superconductor/Fusion/Plasma — **Otherworldly** | fusion_reactor, fusion_chamber, plasma_turbine, replicator (block), superconductor coil/hatches/storage, quantum machine casing/hull/tank/barrel | YES — `ow4_the_dyson_project`, `ow6_beyond_the_veil` | none (machines) |

## Tier-by-tier evidence (tools / gear / capstone loop — the gaps)

| Content family | Signature ids (jar-verified, recipes confirmed) | Age (per recipe inputs/gates) | Quested? | Gap |
|---|---|---|---|---|
| Portable steam/diesel tools | `steam_mining_drill`, `diesel_mining_drill`, `diesel_chainsaw` | IR→Gilded | **NO** | REAL — the "handheld power tool" beat MI is known for |
| Electric drills (tier ladder) | `stainless_steel_drill`, `titanium_drill` (+ aluminum/steel drill) | Gilded/Atomic | **NO** | REAL — mirrors the voltage ladder in the player's hand |
| Diesel jetpack | `diesel_jetpack` (recipe `armor/diesel_jetpack.json`) | Gilded (diesel/petrochem) | **NO** | REAL — early flight/mobility payoff |
| Quantum circuit / robot arm | `quantum_circuit`, `quantum_circuit_board`, `robot_arm` | Atomic (EV component tier) | **NO** | REAL — core crafting components, deserve a node, not just silent ingredients |
| GraviChestPlate | `gravichestplate` (needs superconductor_plate + coil + highly_advanced_upgrade) | **Otherworldly** (superconductor) | **NO** | REAL — flagship endgame chestplate; currently at5 only tasks quantum armor |
| Singularity → UU-matter → Replicator loop | `singularity` (implosion), `uu_matter_bucket` (electrolyzer), replicator *use* | Gilded→OW capstone | **NO** | **MAJOR** — the canonical MI endgame ("E=mc²"); replicator block is tasked but the loop that makes it work is not |
| EI nano/nyano armor + saber | `nano_helmet/chestplate/leggings/boots`, `nano_saber`, `nano_gravichestplate`, `nano_quantum_*`, `nyano_(quantum_)helmet` | Atomic→OW | **NO** | REAL — EI's entire wearable-gear ladder is untasked |
| EI electric chainsaw | `electric_chainsaw` | Gilded/Atomic | **NO** | minor (bundle with tools) |
| IO Vajra | `industrialization_overdrive:vajra` (assembler recipe) | Otherworldly (endgame AOE miner w/ silk-touch toggle) | **NO** | REAL — IO's headline tool |
| IO Multiblock Builder | `industrialization_overdrive:terminal` (auto-builds MI multiblocks, ME-linkable) | Gilded/Atomic | **NO** | REAL — huge QoL, thematically the "you've earned automation" reward |

Nothing broken/unobtainable found — every gap item above has a live recipe in its jar.
`quantum armor` (helmet/chest/legs/boots/sword) IS tasked (at5_threshold_of_war), so the quantum
*set* is half-covered; gravichestplate and the nano sets complete it.

## Ranked quest-worthy gaps (bundled, no filler)

1. **[MAJOR] Singularity → UU-Matter → Replication capstone.** ids: `modern_industrialization:singularity`, `uu_matter_bucket`, replicator-use.
   Age: **Otherworldly** (bundle into `ow6_beyond_the_veil` or a short capstone node in ow4).
   Rationale: THE defined MI endgame; replicator block is already tasked but its fuel loop isn't — closing this makes the tentpole tree actually land.
2. **[REAL] GraviChestPlate + nano/nyano armor ladder.** ids: `modern_industrialization:gravichestplate`; `extended_industrialization:nano_chestplate`/`nano_saber`/`nano_gravichestplate`/`nano_quantum_chestplate`/`nyano_quantum_helmet`.
   Age: gravi = **Otherworldly** (superconductor_plate); nano base = **Atomic**, nano-quantum/nyano = **OW**. Bundle into a "Powered Suits" node in at5 (nano) + ow (gravi/nyano).
   Rationale: completes the wearable-gear payoff; quantum set is already tasked so this is the natural finisher.
3. **[REAL] MI portable tool ladder.** ids: `steam_mining_drill`, `diesel_mining_drill`, `diesel_chainsaw`, `stainless_steel_drill`, `titanium_drill`, `diesel_jetpack` (+ EI `electric_chainsaw`).
   Age: steam=IR, diesel/stainless=Gilded, titanium=Atomic. Bundle 1–2 nodes across `ir_..._steam_industry` (steam drill) and `g5_empire_of_iron`/g6 (diesel+stainless+jetpack), titanium_drill in at.
   Rationale: iconic MI handheld power; mirrors the voltage ladder the player already builds.
4. **[REAL] IO flagship tools.** ids: `industrialization_overdrive:vajra`, `industrialization_overdrive:terminal` (Multiblock Builder).
   Age: terminal = **Gilded/Atomic** (once multiblocks matter), vajra = **Otherworldly**. Bundle into at4/ow near the existing IO multi_processing_array node.
   Rationale: IO's only two non-machine headline items; terminal is major QoL, vajra is the endgame miner.
5. **[REAL] Quantum circuit + robot arm as explicit nodes.** ids: `quantum_circuit`, `quantum_circuit_board`, `robot_arm`.
   Age: **Atomic** (EV component tier). Add one component node in at4_machine_soul.
   Rationale: they are load-bearing craft components silently consumed today; a "thorough" tree should teach them.

## Notes / risks
- Gravichestplate recipe requires `superconductor_plate` → it is **OW-gated by ingredient**, do NOT place it in Atomic even though quantum armor lives at at5.
- Replicator *block* is tasked in `ow6_beyond_the_veil`; only the singularity/UU fuel loop is missing — scope the new node as the loop, not the block.
- HNI is complete; do not re-raise it. `hostileneuralnetworks` (base HNN) is a separate mod, out of MI scope.
- All placements respect existing gates (IR bronze/steel, Gilded alu/stainless/petrochem, Atomic titanium/nuclear/quantum, OW superconductor/fusion/plasma) — no new gates proposed (Policy 1).

## Web sources
- https://unofficial-modern-industrialization.fandom.com/wiki/The_Endgame
- https://unofficial-modern-industrialization.fandom.com/wiki/E_%3D_mc%5E2_(Guide_Book_Entry)
- https://unofficial-modern-industrialization.fandom.com/wiki/Quantum_Tier_(Guide_Book_Entry)
- https://unofficial-modern-industrialization.fandom.com/wiki/Modern_Industrialization_Guide_Book
