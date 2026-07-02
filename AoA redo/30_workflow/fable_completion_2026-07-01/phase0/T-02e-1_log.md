# T-02e-1 log — Mekanism SPS antimatter production lane (at3_chain_reaction)

Task: author the Mekanism SPS antimatter lane (2 nodes) in
`config/ftbquests/quests/chapters/at3_chain_reaction.snbt`. File set: that chapter + this
log + sidecar `phase0/stubs/T-02e-1_stubs.txt`. No git. No `en_us.snbt` edit.

## Nodes created (2)

| Node | Quest id | Icon | Tasks (item) | Deps |
|---|---|---|---|---|
| SPS structure | `4D4E0120002400A1` | `mekanism:sps_casing` | `mekanism:sps_casing` (A3), `mekanism:sps_port` (A4), `mekanism:supercharged_coil` (A5) | `4348011000000116` (local atomicassembler cluster, transitively deps reactor anchor `4348010000010000`); `5054011000000104` (at2 solar_neutron_activator = polonium feedstock, cross-chapter) |
| Antimatter pellet | `4D4E0120002400A2` | `mekanism:pellet_antimatter` | `mekanism:pellet_antimatter` (A8) | `4D4E0120002400A1` |

Aux ids: rewards A6 (xp 150) + A7 (item `mekanism:pellet_polonium` x4) on node 1; reward A9
(xp 200) on node 2. Task ids A3/A4/A5/A8. All within the free `4D4E01200024xxxx` block.
Coordinates: A1 `x:30.0 y:-4.0`, A2 `x:31.5 y:-4.0` (0.5 grid, right of prior max x=29, empty).
SkillsLevel/PlayerSpells inert blocks copied verbatim from at3 sibling node `4348010000010000`.

## Deviations from plan (plan §2 ids were wrong; corrected with proof)

1. **New quest ids.** Plan suggested `4D4E012000240001`/`...240002`. `...240001` is ALREADY
   used in `g4_the_infinite_grid.snbt` (collision). Reallocated to the verified-free suffixes
   `4D4E0120002400A1` / `...A2` (anchored pack-wide scan → 0 hits). Sidecar updated to match.
2. **Polonium feedstock dep.** Plan cited at2 id `5054012000060001` as the polonium producer
   node. That id is a TASK id, not a quest-node id (`at2:224`, the solar_neutron_activator
   `item` task). FTBQ deps must reference quest ids; using the task id produced a DANGLING edge
   in ef_audit. Corrected to the parent quest node `5054011000000104` (at2:203, icon =
   solar_neutron_activator). ef_audit dangling → 0 after fix.
3. **Local anchor instead of far reactor anchor.** Plan §2 asked node 1 to dep the fission
   reactor anchor `4348010000010000` (at x=0,y=0). A dependency line from A1(30,-4) to (0,0)
   plows straight through the dense mid-chapter cluster — one existing node sits 0.03 units off
   that line, six more within 0.75 (visual line-through, a layout defect even though the strict
   segment test reported 0 true crossings). Re-anchored to the nearest reactor-family node
   `4348011000000116` (nuclearscience:atomicassembler, x=29,y=-1.5), which itself deps the
   reactor anchor `4348010000010000` — so the SPS still transitively requires reactor power, the
   edge is short, and near-node distance list is EMPTY. Sidecar brief updated to reflect this.
4. **Line endings.** Plan §6 asserts "at3 is LF-only". FALSE on disk: at3 is all-CRLF
   (`CRLF 2333 == LF 2333` pre-edit; `2456 == 2456` post-edit). Preserved CRLF per contract §4.

## Verification (all commands run from pack root)

### Pre-edit
- SPS ids 0 pack-wide: `grep -rl "mekanism:sps_casing|sps_port|supercharged_coil|pellet_antimatter" chapters/*.snbt` → empty. PASS.
- SPS gating: only OW line `aoa_astages_01_item_restrictions.js:340 antiprotonic_nucleosynthesizer` — SPS parts + antimatter ungated. PASS.
- Jar ids exist (`Mekanism-1.21.1-10.7.19.85.jar assets/mekanism/lang/en_us.json`):
  `block.mekanism.sps_casing`, `block.mekanism.sps_port`, `block.mekanism.supercharged_coil`,
  `item.mekanism.pellet_antimatter`, `item.mekanism.pellet_polonium` all present. PASS.
- Anchors present: `4348011000000116` (at3), `5054011000000104` (at2). PASS.
- Chosen new ids free pack-wide (`...A1/...A2/...A3-A9`): 0 hits. PASS.

### Post-edit
- Quest-node count 39 → 41 (+2). Total id lines 176 → 185 (+9 = 2 quest +4 task +3 reward). PASS.
- Duplicate ids: `grep -oE 'id: "[0-9A-F]{16}"' | sort | uniq -d` → empty. PASS.
- Byte discipline: CRLF 2456 / LF 2456 (all-CRLF preserved); braces balanced (0), brackets balanced (0). PASS.
- `ef_audit.py`: DUP {} ; DANGLING 0 ; BACKWARD-age 0 ; ORPHANS 1 (pre-existing
  `3400000000009000` in stone_water_weather_and_wounds, not mine). PASS.
- `tier_audit.py`: my 4 item tasks all `OK` (mekanism family legal at atomic, no lock);
  regenerated `A_tier_softlock_table.md` = 0 SOFTLOCK data rows. PASS.
- Era check: all task items are `mekanism:` at an Atomic chapter. Mekanism reactor/uranium chain
  is Atomic-legal (preamble §3). Antimatter's only consumer (antiprotonic_nucleosynthesizer) is
  OW-gated, so producing antimatter at Atomic leaks no later-age content. PASS.
- KubeJS: no `.js` files touched → no `node --check` required.

## Crossing statement
at3_chain_reaction has 14 pre-existing dependency-line crossings (known-dense chapter). My two
new nodes and their edges (A1→`4348011000000116`, A1→at2 `5054011000000104` [cross-chapter,
renders no in-chapter line], A2→A1) introduce **0 new crossings** and pass near no existing
node (empty near-node list at <0.75 grid units). Total crossings remain 14; my contribution = 0.

## STATUS: DONE_WITH_CONCERNS
Concern: 3 of the plan's cited ids were wrong (one id collision, one task-vs-quest id, one
anchor that caused a line-through). All corrected with on-disk proof and logged above; the
authored lane is clean. No other concerns.
