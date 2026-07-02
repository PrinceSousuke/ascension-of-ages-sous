# Oritech coverage verification — READ-ONLY

Date: 2026-07-02. Verifier: Claude Code (Opus). Scope: `oritech` + `createoritechcompat` + `oritechthings`.

## Jars on disk (verified)
- `oritech-neoforge-1.21.1-1.2.8.jar` — 331 distinct block/item lang keys.
- `oritechthings-0.0.44.jar` — addon: 8 upgrade-block families ×8 tiers (tiers 2-9), accelerator field/sensor, advanced_target_designator, frame_placer.
- `createoritechcompat-1.20.1-1.0.jar` — **recipe bridge only** (Create crushing/mixing/blasting/smelting for oritech ores). No new items → **nothing to quest here.** Verified as functional on 1.21.1 per memory.

## VERDICT
The census's "54 refs with real gaps" **overstates the problem in one direction and understates it in another.** Oritech is broadly well-covered: **115 distinct oritech/oritechthings items are quest-referenced** across 9 chapters, and the AStages gate file (`aoa_astages_01e_oritech.js` + `01_item_restrictions.js` + `01p_gap_closure.js`) is thorough (IR/Gilded/Atomic/OW/Ascension tiers all locked, oritechthings tiers 2-9 all Atomic-locked). The "54 refs" figure appears to be a count of quest *task nodes*, not distinct items, and does not by itself indicate gaps.

**One genuine, high-value gap exists: the entire Oritech nuclear reactor multiblock is unquested AND ungated.** Everything else the census may have flagged is either (a) already quested, (b) a decorative/pipe/staple item correctly excluded per the "skip ubiquitous staples" rule, or (c) gated-but-not-quest-taught (acceptable — a gate does not require a quest node).

## Tier table (quested / gated status)

| Tier / system | Items | Gate age | Quested? | Chapter |
|---|---|---|---|---|
| Machine cores 1-3, frame, foundry, pulverizer, powered furnace, refinery, steam engine, basic gen | many | IR | YES | `ir_oritech_foundry` |
| Machine core 4, assembler, centrifuge, placer, fertilizer, reactor_controller, fuel gen, silicon chain, enderic_lens, processing_unit | many | Gilded | YES | `g6_circuits_and_current` |
| Machine core 5/6/7, atomic_forge, fragment_forge, machine_extender, particle_collector, duratium | many | Atomic | YES | `at4_machine_soul` + `atomic_oritech_convergence` |
| Particle accelerator (controller/motor/ring/sensor) + oritechthings accel field/sensor | 6 | Atomic | YES | `atomic_oritech_convergence` |
| Augment stations (simple→arcane→advanced), augment_application, enchanter | 5 | IR→Atomic | YES | `atomic_oritech_convergence` + oritech_weaves |
| Enderic laser (laser_arm) + **target_designator** | 2 | Atomic | laser_arm YES, **designator NO** | `atomic_oritech_convergence` |
| oritechthings addon tiers 2-9 (6 families) | 48 | Atomic | YES (as-a-set) | `atomic_oritech_convergence` |
| black_hole_block, unstable_container | 2 | Ascension | YES | `asc4_singularity` |
| Exosuit (helm/chest/legs/boots/jetpack), jetpack variants | 8 | OW/Asc | gated, **not quest-taught** | (gap_closure gate only) |
| **Nuclear reactor multiblock** (rod/wall/vent/heat_pipe/reflector/condenser/ports/double+quad rod/absorber) | ~12 | **NONE** | **NO** | **— GAP —** |
| Deep drill, quarry addon, drone port, destroyer, treefeller, pump | ~6 | IR/Gilded/Atomic | mixed (some quested in convergence) | partial |
| Tools: chainsaw, hand_drill, promethium pick/axe, portable_laser, electric_mace, wrench | 6 | ungated | NO | (staples — see note) |
| Decor/pipes/paints/plating/resource_nodes/dusts/molten fluids | ~140 | n/a | NO (correctly) | — |

## Ranked jar-verified gap list

### GAP 1 — Oritech Nuclear Reactor multiblock (HIGH, real, bundle into one node)
- **Ungated AND unquested.** Only `oritech:reactor_controller` is locked (Gilded) and quest-referenced. The 12 build components are free-craftable at any age:
  `oritech:reactor_rod`, `reactor_wall`, `reactor_vent`, `reactor_heat_pipe`, `reactor_reflector`, `reactor_condenser`, `reactor_double_rod`, `reactor_quad_rod`, `reactor_energy_port`, `reactor_fuel_port`, `reactor_absorber_port`, `reactor_redstone_port` (fuel: `uranium_pellet`/`plutonium_pellet`, already Atomic-locked via duratium/pellet chain).
- Oritech's reactor is a genuine fission-power multiblock (uranium/plutonium pellets, heat pipes, vents, condensers). Age = **Atomic** (nuclear power is the Atomic age's domain). Recommend: **one bundled multiblock quest** in `at4_machine_soul` or `atomic_oritech_convergence` requiring reactor_controller + rod + wall + vent + a fuel/energy port. **Also flag to gate authority**: the rod/wall/port components should get an Atomic AStages lock in `aoa_astages_01e_oritech.js` to close the bypass (currently a player could hand-craft the whole reactor pre-Atomic). This is a gate gap, not just a quest gap.

### GAP 2 — Enderic laser targeting workflow incomplete (LOW, bundle into existing node)
- `oritech:laser_arm_block` is quested (atomic_oritech_convergence) but its **required companion** `oritech:target_designator` is neither quested nor gated. The laser arm is useless without the designator to assign a target. Recommend: add `target_designator` as a second task on the existing enderic-laser node. Not a softlock (designator is cheap), just an incomplete teaching beat.

### GAP 3 — Exosuit not quest-taught (LOW/optional, reward-gear class)
- `exo_helmet/chestplate/leggings/boots/jetpack` + `jetpack_exo_elytra` are **gated** (OW/Ascension, `01p_gap_closure.js`) but have **no quest node**. Per the reward-gear pattern these can live as an optional OW/Ascension gear node. Optional, not required — do not force.

## NON-gaps (do NOT author — verified excluded/covered)
- **createoritechcompat**: recipe bridge, zero new items. Nothing to quest.
- **Tools** (chainsaw, hand_drill, promethium pick/axe, portable_laser, electric_mace, wrench): ubiquitous low-signal staples. Per memory rule "skip ubiquitous Oritech staples." Leave unquested.
- **oritechthings addon tiers 2-9**: already referenced as a set in atomic_oritech_convergence and fully gated Atomic. The 48 individual tier-blocks do NOT each need a node — bundling is correct.
- **Decor/pipes/plating/paints/resource_nodes/dusts/molten-fluid buckets** (~140 keys): correctly excluded, no quest warranted.
- **Particle accelerator + black hole**: fully quested (atomic convergence + asc4_singularity) and gated (Atomic / Ascension). The memory note "asc3 impossible machine may hold accelerator" is STALE — verified: accelerator is Atomic (`atomic_oritech_convergence`), black_hole is `asc4_singularity`. No asc3 involvement.

## Bottom line
Oritech coverage is strong. **The only quest-worthy real gap is the nuclear reactor multiblock (GAP 1)** — and it doubles as a genuine **bypass/gate defect** (uranium-fueled reactor craftable pre-Atomic). GAP 2 and GAP 3 are minor polish. The "54 refs / real gaps" census framing is misleading: it counts nodes, and the vast majority of the 331 jar items are correctly-excluded decor/staples.
