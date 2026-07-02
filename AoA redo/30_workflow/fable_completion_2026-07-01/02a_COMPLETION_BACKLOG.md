# 02a — THE COMPLETION BACKLOG (verified, whole-roster, by age)

_Built from the full census (`AoA redo/30_workflow/mod_quest_coverage_census_2026-07-02.md`,
546 jars / 303 content mods) + a depth audit of the major mods, both verified on disk
2026-07-02. Spot-checked by hand: AE2/RS/Mekanism/Oritech/IE foundations confirmed at 0
quests; Avaritia tables at 0; Spectrum pedestals at 0._

## The headline
**216 of 303 content mods (71%) are not fully quested.** 87 DONE, 56 PARTIAL, 160 ZERO.
139 of the not-done mods are **ungated** (no AStages entry) — some intentional (Quark decor),
most not. The dominant pattern is a **foundations gap**: the big tech mods have dense
*endgame* chapters but their *mid-game onboarding is missing* — a player following quests
never learns to place an AE2 controller, a Mekanism enrichment chamber, or an Oritech machine
core. Closing that pattern is the highest-value work in the pack.

Legend: **[SPINE]** = required critical path (canon main/side spine). **[FOUND]** = foundation
gap (endgame taught, onboarding missing) — highest ROI. **[CANON]** = needs your decision,
not just authoring (see 08). **[EXCLUDED]** = user ruling: do not quest. Priority P1 (do first) → P3 (polish).

> **2026-07-02 B0 reconciliation note.** Whole-roster coverage re-verified against a 15% random
> sample (27 of 178 enumerable PARTIAL/ZERO verdicts) by hand-grepping `config/ftbquests/quests/chapters/*.snbt`.
> **Verdict agreement: 27/27 (100%).** One count drift: `unusualend` is 28 unique refs on disk, census
> said 23 (still PARTIAL — a slight undercount, not a wrong verdict). `artifacts` re-confirmed ZERO
> (the lone "artifacts:" hit is `reliquified_artifacts:mimi_dust`, a different mod). All 8 foundation
> gaps re-confirmed at **0 across all chapters, including smart_filter/ftbfiltersystem NBT bodies**:
> `ae2:controller`, `ae2:drive`, `refinedstorage:controller`, `mekanism:enrichment_chamber`,
> `oritech:machine_core_1`, `immersiveengineering:blast_furnace`, `spectrum:pedestal_moonstone`
> (and every `spectrum:pedestal*` variant), `avaritia:extreme_crafting_table`. Full proof in
> `phase0/M_b0_reconciliation.md`. **User coverage rulings (2026-07-02) applied below**, marked `[RULING 07-02]`.

### User coverage rulings applied 2026-07-02 (standing decisions)
- **zoniex / relics / artifacts** — **[EXCLUDED]** do not quest. Remove from scope.
- **railways** (Steam 'n' Rails) — **minimal only**, a couple quests max. Not a chapter.
- **psi** — **optional-only, never required.** May exist as an optional side beat; never on any spine.
- **avaritia / stellaris / modern_industrialization / extendedcrafting** — **thorough endgame treatment.** These get deep coverage.
- **flight** (create aeronautics / createpropulsion) — **stays unquested.** Intentionally free/ungated (many players installed the pack for it). Do not gate, do not chapter.
- **createnuclear / oreexcavation / powergrid** — **leave alone** (already placed; no rework).
- **ftboceanmobs** — **being dropped** from the pack; do not author coverage for it.

---

## Renaissance and earlier  → run with `02b`
- **spectrum** [SPINE][FOUND] P1 — pedestal crafting (the mod's entire front door:
  `pedestal_all_basic`, `pedestal_basic_*`, `pedestal_moonstone`, `pedestal_onyx`) + all 5
  network nodes + `color_picker`/`titration_barrel` hue tools: **0 quests** despite Renaissance
  gate. Highest-priority magic gap in the pack. Apparatus + Deeper Down ladder already good.
- **immersiveengineering** [FOUND] P2 — Medieval onboarding `coke_oven` + `tank`: 0 quests
  (the rest of IE is an IR gap, below).
- **malum** [SPINE] P2 — spirit_altar/soulstone intro is solid; 5 elemental Spirit types have
  no ladder + **no gate**; `ritual_plinth` barely touched. [CANON] Depths of Malum dimension:
  no gate, no quest — decide in/out.
- **neovitae** [SPINE] P2 — Renaissance altar/orb line is real; keep.
- **apothic_enchanting** [CANON] P3 — canon expects "late-Renaissance controlled," but it's
  **ungated + 0 quests**. Needs a gate AND content from scratch.
- **mahoutsukai** [CANON] P3 — optional-fun per canon; 0 quests. Needs a small optional
  Renaissance chapter. Verify circle/familiar item ids in the jar before authoring.

## Industrial Revolution  → run with `02c` (the big one)
- **ae2** [SPINE][FOUND] P1 — **the single largest gap in the pack.** ME network foundation
  (`controller`, `drive`, `me_chest`, `energy_cell`, `energy_acceptor`, `condenser`,
  `cell_workbench`, `io_port`, crafting CPU trio, 1k/4k storage) = 0 quests; `g4` opens on
  `molecular_assembler`. Quest the whole start-the-network arc at IR.
- **refinedstorage** [SPINE][FOUND] P1 — same defect: `controller`, `grid`, `crafting_grid`,
  `disk_drive`, `detector`, `security_manager`, `storage_monitor`, `portable_grid` = 0.
- **mekanism** [SPINE][FOUND] P1 — entire IR ore-processing spine = 0: `enrichment_chamber`,
  `osmium_compressor`, `purification_chamber`, `chemical_injection_chamber`, `chemical_infuser`,
  `electrolytic_separator`, `pressurized_reaction_chamber`, thermal evaporation, 8/9 basic
  factories. Mekanism's signature mid-game, untquested.
- **immersiveengineering** [FOUND] P1 — core multiblocks = 0: `blast_furnace`, `crusher`,
  `alloy_smelter`, `mixer`, `squeezer`, `bottling_machine`, `sawmill`, `auto_workbench`, `silo`.
- **oritech** [FOUND] P1 — entire IR tier = 0 and **no home chapter exists**: `machine_core_1/2/3`,
  `pulverizer_block`, `powered_furnace_block`, `foundry_block`, `refinery_block`, basic power,
  addon set. Needs a dedicated IR Oritech chapter. (Verified not a softlock — pure gap.)
- **extendedcrafting** [FOUND][RULING 07-02: thorough endgame] P2 — `basic_table` + prereqs (its own gate entry) = 0.
  Deep treatment through the elite/ultimate/crystaltine tiers (order confirmed under Ascension below).
- **modern_industrialization** [RULING 07-02: thorough endgame] — MI is the pack's biggest tech tree (census 118 refs
  against 1082 models = still partial). Give it deep, thorough coverage across its IR→Gilded→Atomic→OW span.
- **railways** [RULING 07-02: minimal] — Steam 'n' Rails: **a couple quests max**, not a chapter. Was ZERO in census.
- **relics** / **artifacts** / **zoniex** [RULING 07-02: EXCLUDED] — do not quest. Drop from all age scopes.
- **create aeronautics / createpropulsion (flight)** [RULING 07-02: stays unquested] — do not gate, do not chapter.
- **createnuclear / oreexcavation / powergrid** [RULING 07-02: leave alone] — already placed; no rework.
- **ftboceanmobs** [RULING 07-02: dropped] — being removed from the pack; author no coverage.
- **cabletiers** P2 — entry elite tier (5 ids) = 0 (pack has no IR-tier RS cable quest at all).
- **immersivepetroleum** P2 — `seismic_survey` (CDG→IP bridge), `gas_generator`, `flarestack`.
- **electrodynamics** P3 — base `mineralgrinder` line (Gilded successor is taught).
- **neovitae** [SPINE] P2 — IR segment: `vas_maleficum`, `spira_infernalis`,
  `crystallarium_maleficum`, `teleposer`, `tabula_*` line = 0 despite gate.
- **psi** [RULING 07-02: optional-only, never required] P3 — only the 2 gateway items name-dropped;
  CAD assembly/spell-bullets untaught. If authored at all, an **optional** IR side-beat only — never
  place it on any spine. Verify component ids first.

## Gilded Age  → run with `02d`
- **neovitae** [SPINE] P1 — the missing blood_orb **magician/master/archmage** ladder = 0
  (structural hole between Renaissance apprentice and Atomic transcendent).
- **industrialforegoing** P2 — `sludge_refiner`, sewer/`sewage_composter`, `washing_factory`,
  `water_condensator`, `potion_brewer`, `stasis_chamber`, `spores_recreator`, `conveyor`,
  `infinity_charger` (all Gilded-gated, unquested).
- **extrastorage** P2 — `netherite_crafter`, `advanced_importer`.
- **appmek** P2 — remaining `chemical_storage_cell` tiers (1k/4k/16k/256k).
- **enderio** P3 — `fluid_tank`/`pressurized_fluid_tank`; [CANON] `powered_spawner` (ungated+unquested).
- **cabletiers** P3 — (mega tier is Atomic, below).
- **mekanismadditions** [CANON] P3 — zero gate, zero quests. Check jar contents before scoping.

## Atomic  → run with `02e`
- **draconicevolution** P2 — entire IO/relay/wireless crystal energy-network subsystem = 0
  at any tier; `particle_generator`, `grinder`, `disenchanter`, `celestial_manipulator`.
- **ballistix** P2 — `nuclear` + `thermobaric` warheads themselves = 0 (the softlock is fixed
  but unexploited); +representative subset of remaining warheads.
- **evolvedmekanism** P2 — one more factory family beyond enriching + dense personal storage.
- **mekmm** P2 — 2–3 more large-factory representatives beyond `basic_oxidizing_factory`.
- **extrastorage/cabletiers** P3 — `netherite_crafter` done above; cabletiers mega tier (7 ids).
- **nuclearscience** P3 — `radioisotopegenerator`; confirm full hazmat set beyond helmet.
- **appmek** P3 — remaining cell tiers if not done at Gilded.

## Otherworldly  → run with `04` (full buildout)
- **draconicevolution** P1 — wyvern-tier core content is the OW showpiece; deepen.
- **evolvedmekanism / mekmm** P2 — quantum/multiversal tiers gated here but **0 coverage** —
  at least one representative quest each to close the loop.
- **industrialforegoing** P2 — `supreme_black_hole_unit`/`tank`.
- **occultism** P3 — `book_of_binding_marid`, `iesnium_anvil`, short Marid capstone beat.
- **ballistix** P2 — entire antimatter/darkmatter tier = 0 (the mod's true endgame).
- Plus the OW-native set already in `04`: Stellaris [RULING 07-02: thorough endgame — confirm depth is adequate,
  not just "done"], advanced_ae quantum, MI fusion.

## Ascension  → run with `05` (full buildout)
- **avaritia** [FOUND][RULING 07-02: thorough endgame] P1 — the **compressed-crafting-table ladder itself is 0**
  (compressed→double→nether/end/sculk→`extreme_crafting_table`), i.e. the mod's whole reason to exist;
  +`extreme_smithing_table`, `tesseract`, neutron density ladder, representative infinity gear. Give it deep coverage.
- **draconicevolution** P1 — awakened/chaotic/reactor tier + chaos-tier crystal network.
- **extendedcrafting** P2 — elite/ultimate/crystaltine dense (done); confirm ladder order.

---

## How to use this
`02b`–`02e` + `04`/`05` are the per-age prompts; each takes its section above as the target
list. **Foundations-first within every age:** author the onboarding rungs of AE2/RS/Mekanism/
IE/Oritech BEFORE their capstone content, then wire the existing endgame chapters to depend on
them. Every [CANON] item goes to the decision queue in `08`, not authored blind.
