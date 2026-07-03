# Otherworldly And Ascension Gap Map

## Coverage Counts

Subagent top-level quest ID count snapshot:

Gilded:

- `g1_the_golden_workshop`: 36
- `g2_the_refinery`: 61
- `g4_the_infinite_grid`: 58
- `g5_empire_of_iron`: 87
- `g6_circuits_and_current`: 63
- `g7_chartered_arcana`: 6
- `g_power_beyond_wires`: 39

Atomic:

- `at1_nuclear_dawn`: 37
- `at2_the_periodic_table`: 35
- `at3_chain_reaction`: 39
- `at4_machine_soul`: 64
- `at5_threshold_of_war`: 37
- `at7_chaos_convergence`: 25
- `atomic_oritech_convergence`: 36

Otherworldly:

- `ow1_launch_window`: 4
- `ow2`: 5
- `ow3`: 5
- `ow4`: 5
- `ow5_the_digital_cosmos`: 7
- `ow6_beyond_the_veil`: 13

Ascension:

- `asc1`: 8
- `asc2`: 6
- `asc3`: 6
- `asc4`: 2
- `asc5`: 5
- `asc6`: 11
- `asc7`: 2

These are regex counts of top-level quest IDs, not a meaningful-quest classification. They still show the shape clearly: Gilded and Atomic have real bodies; Otherworldly and Ascension are skeletal.

## Gilded

Current recommendation: stabilize, do not massively expand.

Needed:

- Fix `g7_chartered_arcana` optionality/progression contradiction.
- Resolve `g2_the_refinery` `ftbquests:missing_item` residues.
- Add a small Oritech escalation branch only if the tracker row is still considered live.
- Keep NauTec in Gilded; it is already live-covered in `g6_circuits_and_current`.

## Atomic

Current recommendation: targeted gap filling.

Needed:

- Preserve the current rule that Oritech/Periodic Table depth is optional to Chaos Gate.
- Repair `at4_machine_soul` missing item residues.
- Repair `at7_chaos_convergence` `spectrum:deeper_down_portal`.
- Add safety/system proof around radiation, geiger, reactor logistics, and selected Chemical Science gates.
- Avoid expanding every Mekanism tier.

## Otherworldly

Needs three substantial lines:

1. Launch and orbital operations.
   - Launch prep.
   - Oxygen/life support.
   - Station/planet logistics.
   - Space-boss or planet proof.

2. Advanced digital/cosmic logistics.
   - AE2/Advanced AE/MEGA route.
   - QIO route.
   - Applied Mekanistics chemical storage.
   - Cross-dimensional power/storage.

3. Antimatter and cosmic refinement.
   - Mekanism SPS.
   - Antimatter pellet.
   - Nuclear Science exotic cells if verified.
   - Evolved/MekMM quantum factory tier.
   - Optional Draconic bootstrap.

## Ascension

Needs a final progression spine:

1. ExtendedCrafting/Avaritia prestige fabrication.
2. Draconic Evolution/Additions apex route.
3. Oritech unstable container and black-hole convergence.
4. Singularity convergence.
5. Final infinity proof.

Good existing model:

- The Oritech unstable container weave is a strong convergence concept. Reuse the idea conceptually, not by duplicating broad ingredients everywhere.

## Cross-Weave Candidates

| Candidate | Target age | Why |
|---|---|---|
| Advanced AE quantum parts gated by Mekanism SPS/antimatter or QIO proof | Otherworldly | Makes digital endgame depend on real energy/chemistry. |
| AppMek chemical storage tied to Nuclear Science/Mekanism waste | Otherworldly | Prevents chemical storage from appearing detached. |
| Draconic wyvern/energy core tied to Advanced AE quantum or post-fusion materials | Otherworldly/Ascension | Gives Draconic a pack-integrated entry. |
| Avaritia infinity catalyst tied to Draconic chaotic core, ExtendedCrafting ultimate catalyst, Oritech unstable container, and MFF/Fortron proof | Ascension | Clear final convergence. |
| MekMM/Evolved quantum/multiversal tiers tied to antimatter or singularity proof | Otherworldly/Ascension | Avoids raw tier spam. |

## Do Not Quest

- Every Mekanism factory/storage/pipe/cable tier.
- Every Oritech Things addon tier.
- Every AE/MEGA/Advanced AE cell size/type.
- Every Ballistix payload/turret variant.
- Every Draconic tool/armor/crystal variant.
- Every Avaritia tool/armor/trinket.
- Every Chemical Science element/card/polymer unless it is a real recipe gate.

## Verify Flags

- `[VERIFY]` jar registry for every new Otherworldly/Ascension quest target before authoring.
- `[VERIFY]` current host/in-game reload behavior after any late quest edits.
- `[VERIFY]` tracker rows before using target counts as current truth; tracker has drift.
- `[VERIFY]` missing-item replacement IDs from installed jars before repairs.

