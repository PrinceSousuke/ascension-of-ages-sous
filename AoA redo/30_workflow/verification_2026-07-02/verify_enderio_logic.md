# EnderIO + Integrated + ProjectRed/MoreRed coverage verify (2026-07-02)

READ-ONLY. Jars in `/mods`, chapters in `config/ftbquests/quests/chapters`, gates in
`kubejs/server_scripts/aoa_astages_01_item_restrictions.js` (+01l stragglers).

## Jars confirmed installed
- `enderio-8.2.11-beta.jar` (NeoForge 1.21.1 port — well past EnderIO 7; this is a MATURE build, not partial)
- `integrateddynamics-1.21.1-neoforge-1.33.3.jar`
- `integratedtunnels-1.21.1-neoforge-1.9.4.jar`
- `integratedterminals-1.21.1-neoforge-1.7.0.jar`
- `morered-1.21.1-6.0.0.3.jar`
- ProjectRed `4.22.0` x6: core, expansion, exploration, illumination, integration, transmission

Census that opened this ticket (enderio 38 "deep tree open", ID 9, terminals 0, tunnels 1,
morered 0, projectred_transmission 1) was miscounted / shallow. True live refs = **131 across 9 files**.

---

## Per-mod verdict

### enderio — WELL COVERED (no real gap)
Jar surface (verified in lang): alloy_smelter, sag_mill, slice_and_splice, soul_binder, vat,
wired_charger, impulse_hopper, painting_machine, enchanter, drain, crafter, farming_station,
powered_spawner, vacuum_chest, xp_vacuum, fluid_tank/pressurized, capacitor banks (basic→vibrant)
+ capacitors (basic/double/octadic/loot), photovoltaics (energetic/pulsating/vibrant), soul_vial/
void_vial, obelisks (attractor/aversion/inhibitor/relocator/weather/xp), soul_engine, wireless_charger,
travel_anchor + staff_of_travelling/levity, conduits + facades/binder, all alloys (redstone/energetic/
conductive/pulsating/vibrant/dark_steel/end_steel/soularium), grains_of_infinity, dark_steel gear.
- **IR chapter** `ir_automation_safety_and_routing` carries ~22 distinct enderio machines/tiers.
- **Gilded** `g5_empire_of_iron` carries the soul tier (soul_engine, slice_and_splice, soul_binder,
  farming_station, powered_spawner, 6 obelisks, wireless_charger).
- **Atomic** `at1_nuclear_dawn` carries photovoltaics + advanced/vibrant capacitor banks.
- VERDICT: machines/mechanics all quested at correct ages. Only unquested items are decorative
  (painted blocks, clear_glass/fused_quartz color variants, silent pressure plates) and grinding
  balls — correctly excluded per anti-bloat. NO GAP.

### integrateddynamics — COVERED, one worthwhile add
Jar: menril tree → squeezer/drying_basin (+ mechanical variants) → variable/cable/proxy/delay/
materializer/variablestore → logic_programmer (+portable) + logic_director, coal_generator, labeller.
- IR chapter has: logic_programmer, materializer, proxy, mechanical_squeezer, drying_basin,
  coal_generator, cable, variable. `ir_magic_feedstock` uses logic_director; journey mirror uses materializer.
- GAP (minor): **squeezer** (base, non-mechanical) + **menril seed/sapling entry beat** and the
  **variable_transformer** (in/out) are unquested. The base squeezer + menril intro is the true ID
  on-ramp; right now the chapter jumps to mechanical_squeezer. Worth ONE bundled entry node.

### integratedtunnels — UNDER-COVERED (real gap)
Jar: importer/exporter (item/fluid/energy) parts, interface (item/fluid/energy), player_simulator.
- Live: only `part_player_simulator` (gated atomic, used in at4). The **import/export/interface parts**
  — the actual point of the mod, the ID↔storage bridge — are UNQUESTED.
- GAP (moderate): one IR/Gilded node bundling `part_importer`/`part_exporter`/`part_interface` (item+fluid).
  This is the ID network payoff and currently has no quest home.

### integratedterminals — MECHANICALLY COVERED
Jar: storage terminal part + portable storage terminal + cosmetic glass.
- `part_terminal_storage` is GATED (IR, line 680) but NOT placed as a quest task anywhere.
- GAP (minor): the storage terminal is the ID "player-facing GUI" capstone. One IR node would close it.
  Low priority — ID network already has quest presence.

### morered — NOT QUESTED (defensible exclusion, but one bridge worth it)
Jar: red_alloy_wire, logic gates (and/or/not/nand/nor/xor/xnor + bitwise + latch/diode/multiplexer/
pulse), network cables (16 colors), soldering_table, red_alloy_ingot, redwire/bundled spools.
- Live quests: **0**. Only `morered:bundled_network_cable` is gated (IR, line 684).
- VERDICT: per-color cables & duplicate gate variants are anti-bloat NON-targets. MoreRed overlaps
  ProjectRed integration/transmission which IS quested (ren_observation_experimentation). Reasonable
  to leave morered as free/ungated flavor. OPTIONAL: one node on `soldering_table` + `red_alloy_ingot`
  if a distinct MoreRed beat is wanted, but not required.

### projectred — WELL COVERED
- **Renaissance** `ren_observation_experimentation`: red_ingot, plate, anode, cathode, conductive_plate,
  red_alloy_wire, not_gate, timer_gate, red_lantern — the logic-primitives on-ramp.
- **IR** `ir_automation_safety_and_routing`: expansion machines (auto_crafter, deployer, transposer,
  block_breaker, frame_motor, battery_box, pneumatic_tube), integration state_cell_gate, core silicon chain.
- Gates: silicon chain + expansion machines IR; red_ingot/plate/red_alloy_wire/frame_actuator Renaissance.
- VERDICT: gates + beats align. Per-color wires/lamps/backpacks/illumar correctly excluded. NO GAP.

---

## Beats table

| Mod | Renaissance | Industrial Rev | Gilded | Atomic |
|---|---|---|---|---|
| enderio | — | 22 machines (ir_automation) | soul tier x14 (g5) | photovoltaics + capacitor banks (at1) |
| integrateddynamics | — | squeezer/basin/logic/proxy/materializer/cable | — | (materializer mirror in JTA) |
| integratedtunnels | — | **(none)** | — | player_simulator (at4) |
| integratedterminals | — | gated-not-placed | — | — |
| morered | — | **(none — only gated)** | — | — |
| projectred | logic primitives (ren_obs_exp) | expansion machines + silicon (ir_auto) | — | — |

## Gates (all clean, most-restrictive-wins respected)
- enderio: IR machines + basic_capacitor_bank (lines 31–45); soul tier + obelisks → gilded_age (46–55). Correct.
- ID: cable/basin/logic_programmer/mechanical_basin → IR (676–679). Correct.
- tunnels: part_player_simulator → atomic (650). Correct.
- terminals: part_terminal_storage → IR (680) — gated but unplaced.
- morered: bundled_network_cable → IR (684). ProjectRed silicon/expansion IR, red primitives Renaissance.
- soularium recipe reroute in `ender_io_soul.js`; comment header confirms design intent
  (void_chassis→IR, ensouled/soul_stained→Gilded).

---

## Ranked jar-verified gap list (bundled, ids + age + chapter)

1. **[MODERATE] integratedtunnels import/export/interface** — one node, IR or Gilded,
   `ir_automation_safety_and_routing` (or a Gilded logistics chapter).
   Items: `integratedtunnels:part_importer`, `part_exporter`, `part_interface` (verify exact part ids
   from jar — lang exposes them as `part_*`). This is the ID↔storage bridge and the mod's whole point.
2. **[MINOR] integrateddynamics base on-ramp** — extend the existing IR node.
   Items: `integrateddynamics:squeezer` + `menril_sapling`/`menril_berries` (menril intro) +
   `variable_transformer_input/output`. Fills the jump from menril→mechanical_squeezer.
3. **[MINOR] integratedterminals storage terminal** — place the already-gated part as a task.
   Item: `integratedterminals:part_terminal_storage`, IR, `ir_automation_safety_and_routing`.
4. **[OPTIONAL] morered distinct beat** — only if a MoreRed identity node is wanted.
   Items: `morered:soldering_table` + `morered:red_alloy_ingot`, IR. Otherwise leave as free flavor.

Anti-bloat NON-gaps (do NOT author): per-color wires/cables/lamps/insulated wires (projectred/morered),
illumar dyes, backpacks, enderio painted/glass/quartz decor + grinding balls, silent pressure plates.

## Sources
- Jar lang inspection (ground truth): all six mods' `assets/*/lang/en_us.json` in `/mods`.
- EnderIO 1.21.1 port active/mature: https://github.com/Team-EnderIO/EnderIO/releases ,
  https://github.com/Team-EnderIO/EnderIO/tree/1.21.1/docs , https://modrinth.com/mod/enderio/changelog
