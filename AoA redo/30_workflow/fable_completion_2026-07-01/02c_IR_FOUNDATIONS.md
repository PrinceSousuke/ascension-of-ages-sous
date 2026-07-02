# 02c — INDUSTRIAL REVOLUTION: FOUNDATIONS + COMPLETION (the biggest pass)

**Owner:** Fable (structure) → Opus (prose) → CC (age-discipline + merge). **Prepend:**
`01_MASTER_PREAMBLE`. **Target list:** the "Industrial Revolution" section of `02a`.
**Depends on:** `LEDGER.md` signed.

IR looks finished (411 quests) but that's a mirage: the flashy endgame of every big tech mod
is taught while the **onboarding is missing**. Hand-verified, all at 0 quests: AE2 controller/
drive/cells, RS controller/grid/disk-drive, Mekanism enrichment/purification/injection spine,
Oritech machine cores, IE blast furnace/crusher/squeezer. This pass fixes the pattern. It is
the highest-ROI work in the whole program.

## The doctrine for this pass: teach the network from node zero
For each foundation mod, the deliverable is the **start-the-system arc**, then a re-wire so the
existing endgame chapter depends on it. A player must be able to reach the taught endgame by
following quests alone.

### P1 — AE2 [SPINE][FOUND]  (single largest gap in the pack)
In `g4_the_infinite_grid` (or a new `ir_applied_energistics_network` chapter if g4 is Gilded-
tier — check its group; AE2 is IR-gated so the foundation belongs at IR): author the network
arc — `controller` → `energy_acceptor`/`energy_cell` → `drive` + storage cells (1k/4k) →
`me_chest` → `cell_workbench` → `io_port` → grid/terminal → crafting CPU trio → first
autocraft. Then make the existing `molecular_assembler`/pattern/wireless/spatial quests depend
on this arc. Verify every id against the ae2 jar.

### P1 — Refined Storage [SPINE][FOUND]
Same shape: `controller` → `grid` → `disk_drive` + disks → `crafting_grid` → `detector`/
`storage_monitor`/`security_manager` → `portable_grid` → autocrafter. Re-point the existing
`autocrafter`/wireless quests to depend on it.

### P1 — Mekanism [SPINE][FOUND]
Author the IR ore-processing spine (currently 0): the 5-stage factory chain
`enrichment_chamber` → `crusher` → `purification_chamber` → `chemical_injection_chamber` →
`chemical_infuser`, plus `osmium_compressor`, `electrolytic_separator`,
`pressurized_reaction_chamber`, thermal evaporation tower, and the basic factory tier (0/9
taught). This is Mekanism's signature mid-game — it deserves a real multi-node line, bundled
sensibly (multiblocks as single nodes). The Atomic uranium/Mekasuit content already exists;
wire it to depend on this.

### P1 — Immersive Engineering [FOUND]
Author the core multiblocks (0 quests): `blast_furnace` (after the Medieval `coke_oven` from
`02b`), `crusher`, `alloy_smelter`, `mixer`, `squeezer`, `bottling_machine`, `sawmill`,
`auto_workbench`, `silo`. These are what IE is famous for. Existing IE gear/generator/Gilded
quests wire on top.

### P1 — Oritech [FOUND]  (needs a NEW chapter)
No IR home chapter exists. Create `ir_oritech_foundry` (verify the g-series/at naming): author
`machine_core_1/2/3` (everything later builds from these) → `pulverizer_block` →
`powered_furnace_block` → `foundry_block` → `refinery_block` → basic generator/power → addon
tier 1. The existing `atomic_oritech_convergence` (78 refs) then depends on this IR base.

### P2 — the rest of the IR list
- **extendedcrafting**: `basic_table` + prereqs (its own gate entry, 0 quests).
- **cabletiers**: the elite/IR tier (5 ids) — pack currently has no IR RS-cable quest at all.
- **immersivepetroleum**: `seismic_survey` (sequence it right after a CDG `oil_scanner` quest
  so the intended Create-Diesel→IP handoff is visible), `gas_generator`, `flarestack`.
- **neovitae** [SPINE]: IR segment — `vas_maleficum`, `spira_infernalis`,
  `crystallarium_maleficum`, `teleposer`, `tabula_*` line (0 despite gate).
- **electrodynamics** [P3]: base `mineralgrinder` line.
- **psi** [CANON, P3]: optional IR side-chapter only after the scope call; verify ids first.

## Method
Same five steps as `02b`. Emphasis here on the **re-wire**: after authoring each foundation,
update the dependency edges of the existing endgame quests so nothing is reachable before its
prerequisite. CC must confirm, per mod, that a fresh player can path from the foundation to the
old endgame with no gap. Crossing-free (this is a dense age — compute crossings, re-lay as
needed). Any re-source needed → `06` weaves.

## Deliverables
New/edited IR chapters (incl. `ir_oritech_foundry`), full VERIFICATION LOG, stub briefs,
before/after counts to `LEDGER.md`, dependency-flow sketch per foundation mod for CC audit.
