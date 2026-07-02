# Phase 0 shared context (read before your audit task)

Pack root: `C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)`
All paths below are relative to the pack root.

## Hard rules for ALL Phase 0 agents
- AUDIT ONLY. Do NOT edit any file under `config/`, `kubejs/`, or `mods/`. You may only
  WRITE new files under `AoA redo/30_workflow/fable_completion_2026-07-01/phase0/`
  (your report + any scratch scripts).
- NO git commands of any kind. Not even `git status`. Leave the working tree alone.
- Verify, never assume: never cite an item id, mod, task type, or stage you did not
  confirm on disk (chapters, kubejs scripts, or the actual jar in `mods/`). Every finding
  must carry a proof command + file:line.
- The mount can misreport truncation; trust `wc -l` / `grep -c` / Python byte reads.
- Read `AoA redo/30_workflow/fable_completion_2026-07-01/01_MASTER_PREAMBLE.md` for the
  8-age ladder, per-age legal tech baseline, and capstone boss chain.

## The 8 ages (ordered, exact stage ids)
`dark_ages` → `medieval_times` → `the_renaissance` → `industrial_revolution`
→ `gilded_age` → `atomic` → `otherworldly` → `ascension`

## Chapter → age map (resolved via chapter `group:` field, VERIFIED 2026-07-02)
Group ids: 12B6640DF4C0DCFE=dark_ages, 508B59840C508057=medieval_times,
0B038EB15EBBFD95=the_renaissance, 3F77A31B7D30C0AA=industrial_revolution,
5E42E6B4A7C91D30=gilded_age, 7D28E4AEBC440F10=atomic, 080F7BA9FFB8FC07=otherworldly,
6A196D2B21EDE4C0=ascension, 5350010000000000=Journey (meta roadmap),
1A7F0E9D4C22B6F1=Annexes (age-agnostic).

- dark_ages: stone_food_and_farming_pressures, stone_water_weather_and_wounds,
  entering_the_iron_era (filename lies; it IS Dark Ages)
- medieval_times: m1_first_mill, m3_relics_and_burrows, metallurgy, what_waits_in_the_grove
- the_renaissance: ren_aether_literacy, ren_archive_recordkeeping,
  ren_deeper_darker_otherside, ren_end_threshold, ren_magic_foundations,
  ren_maledictus_vigil, ren_nether_threshold, ren_observation_experimentation,
  ren_second_mill_steam_rail_logistics, ren_starlight_observation, ren_undergarden_descent
- industrial_revolution: ir_automation_safety_and_routing, ir_create_industrial_addons,
  ir_immersive_engineering_early_factory, ir_ir_side_gear_hidden_equipment,
  ir_magic_feedstock_and_spectrum_network, ir_modern_industrialization_steam_industry,
  ir_netherite_citadel_obsidilith, ir_pneumaticcraft_pressure_plastic,
  ir_power_motion_and_grid
- gilded_age: g1_the_golden_workshop, g2_the_refinery, g4_the_infinite_grid,
  g5_empire_of_iron, g6_circuits_and_current, g7_chartered_arcana, g_power_beyond_wires
- atomic: at1_nuclear_dawn, at2_the_periodic_table, at3_chain_reaction, at4_machine_soul,
  at5_threshold_of_war, at7_chaos_convergence, atomic_oritech_convergence
- otherworldly: ow1_launch_window, ow2_strange_dimension_operations, ow3_dragon_technology,
  ow4_the_dyson_project, ow5_the_digital_cosmos, ow6_beyond_the_veil
- ascension: asc1_the_table_of_infinities, asc2_the_philosophers_dream,
  asc3_the_impossible_machine, asc4_singularity, asc5_the_draconic_heart, asc6_bosses_rise,
  asc7_ascension
- Journey: journey_to_ascension (56 mirror nodes, check_quest tasks; meta, not an age)
- Annexes: minecolonies

## Key file locations
- Chapters (structure only): `config/ftbquests/quests/chapters/*.snbt`
- All player prose: `config/ftbquests/quests/lang/en_us.snbt` (keys quest.<id>.title /
  .quest_subtitle / .quest_desc)
- Stage locks: `kubejs/server_scripts/aoa_astages_01*.js` (+ 02..09). AStages is
  most-restrictive-wins: an item locked in two files is gated at the LATER age.
  Effective gate = MAX across all restriction files.
- Stage registry: `kubejs/server_scripts/aoa_astages_00_register_stages.js`
- Line endings in .snbt are MIXED per file; if you edit nothing this doesn't matter,
  but never rely on grep alone for byte-level claims.
- Duplicate/quest id scans must be anchored: `grep -P '^\s+id: "'` (loose `id:` matches
  autofocus_id).
- FTB Filter System (`ftbfiltersystem`, installed 21.1.4) allows one item task to accept
  any variant via `ftbfiltersystem:smart_filter` — the pack's sanctioned way to handle
  color/wood/material variants.

## Quest legality rules (from pack canon; flag violations)
- No vanilla `minecraft:` items as task items, ever.
- No checkmark/bare-ingot/dust/plate/decor tasks.
- No mob-kill quests for ordinary mobs; kill tasks are legal ONLY for bosses
  (capstone or side bosses).
- No per-variant quests (white foundry / black foundry etc.) — one quest with a
  smart_filter should accept any variant.
- No em dashes in prose. No AI-isms.

## Report contract
Write your full report to the path given in your task prompt (markdown, tables where
useful, every finding with severity SOFTLOCK > BROKEN > CANON > HYGIENE and a proof
command). Your final message back must be ONLY: status line, counts per severity, and
the 3-5 most important findings in one line each. Do not paste the whole report back.
