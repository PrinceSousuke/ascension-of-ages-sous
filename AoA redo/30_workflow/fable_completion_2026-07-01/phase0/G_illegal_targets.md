# Phase 0 — G: Illegal quest-target scan

Scope: all 56 `config/ftbquests/quests/chapters/*.snbt`. Parser (brace-matched task
objects) at `scratchpad/extract.py`; per-class analysis at `scratchpad/analyze.py` /
`analyze2.py`. Task-object totals: item 2340, kill 73 (66 distinct entity refs), plus
xp/loot/random/etc. No `kill_entity` / `find_entity` / `tame_entity` string variants
exist in any chapter (verified: `grep -rn 'type: "kill_entity"'` = 0 hits; all entity
kills use the MQT `type: "kill"` string).

Severity legend: SOFTLOCK > BROKEN > CANON > HYGIENE. Every finding carries a proof
command. AUDIT ONLY — no chapter/config/kubejs edits were made.

---

## Class 1 — KILL / ENTITY TASKS

Legal bosses confirmed (NO action): the full capstone chain
(`cataclysm:maledictus`, `bosses_of_mass_destruction:obsidilith`+`gauntlet`+`lich`,
`astral_dimension:void_titan`, `macabre:valamon/gomoria/gargamaw/baal`,
`fdbosses:geburah`, `cataclysm:the_leviathan`, `draconicevolution:draconic_guardian`),
plus verified side/mini-bosses: `cataclysm:netherite_monstrosity`,
`cataclysm:ender_guardian`, `alexscaves:tremorzilla`, `aether:valkyrie_queen`,
`aether:slider`, `mowziesmobs:ferrous_wroughtnaut/frostmaw/naga/sculptor/umvuthi`,
`eternal_starlight:the_gatekeeper/permafrost/starlight_golem`,
`undergarden:forgotten_guardian`, `minecraft:warden`, `minecraft:ender_dragon`,
`deeperdarker`-line, all `block_factorys_bosses:*` (mod is a boss pack — jar has
`data/.../BossesRise*`), all `astral_dimension:*_boss/tower_of_malice/helioos/
amethyst_knight` (jar has `AngelBossEntity`, `FinalBossArenaBlock`),
`alchemists_garden:gnome_king/spider_queen`, `born_in_chaos_v1:supreme_bonescaller/
nightmare_stalker/lord_pumpkinhead` (elite variants). Vanilla ender_dragon/warden as
kill *entities* are fine (the vanilla ban is on task ITEMS, not boss kills).

ILLEGAL ordinary-mob kills:

| chapter | quest id | task | class | severity | suggested fix |
|---|---|---|---|---|---|
| what_waits_in_the_grove | 6D7E8F901A2B1019 "Elokosa Howler" | kill `mowziesmobs:elokosa_howler` | ordinary-mob kill | CANON | retarget to the paw-item craft it already gates, or delete node |
| what_waits_in_the_grove | 6D7E8F901A2B1051 "The Great Hunt: Foliaath" | kill `mowziesmobs:foliaath` | ordinary-mob kill | CANON | delete (Foliaath is a passive biting plant, not a boss) |
| what_waits_in_the_grove | 6D7E8F901A2B1053 "The Great Hunt: Grottol" | kill `mowziesmobs:grottol` | ordinary-mob kill | CANON | delete (Grottol is a fleeing diamond mole) |
| what_waits_in_the_grove | 6D7E8F901A2B3001 "Bonescaller" | kill `born_in_chaos_v1:bonescaller` | ordinary-mob kill | CANON | delete/retarget to a drop item |
| what_waits_in_the_grove | 6D7E8F901A2B3003 "Dread Hound" | kill `born_in_chaos_v1:dread_hound` x5 | ordinary-mob hunt (count 5) | CANON | delete |
| what_waits_in_the_grove | 6D7E8F901A2B3004 "Dire Hound Leader" | kill `born_in_chaos_v1:dire_hound_leader` | ordinary-mob kill | CANON | delete |
| what_waits_in_the_grove | 6D7E8F901A2B3005 "Sir Pumpkinhead" | kill `born_in_chaos_v1:sir_pumpkinhead` | ordinary-mob kill | CANON | delete (sir_ = common; lord_ is the boss) |
| what_waits_in_the_grove | 6D7E8F901A2B3006 | kill `born_in_chaos_v1:door_knight` x3 + `fallen_chaos_knight` x3 | ordinary-mob hunt | CANON | delete |
| what_waits_in_the_grove | 6D7E8F901A2B3007 "Lifestealer" | kill `born_in_chaos_v1:lifestealer` | ordinary-mob kill | CANON | delete |
| what_waits_in_the_grove | 6D7E8F901A2B3008 | kill `born_in_chaos_v1:zombie_bruiser` + `bone_imp` | ordinary-mob hunt | CANON | delete |
| what_waits_in_the_grove | 6D7E8F901A2B3009 | kill `born_in_chaos_v1:corpse_fly` + `mr_pumpkin` | ordinary-mob hunt | CANON | delete |
| what_waits_in_the_grove | 6D7E8F901A2B300A | kill `monsterplus:crystal_zombie` + `spectral_skull` | ordinary-mob hunt | CANON | delete |
| what_waits_in_the_grove | 7B26069EC5CF71D4 | kill `monsterplus:desert_sorceress` + `desert_acolyte` | ordinary-mob hunt | CANON | delete |
| what_waits_in_the_grove | 442C27F2E00B325C "Hermit Abysswalker" | kill `monsterplus:abyssologer` | ordinary-mob kill | CANON | delete/verify boss status (no boss marker found in jar) |
| what_waits_in_the_grove | 5468102A19D28104 "Corrupted Ancient Hero" | kill `monsterplus:ancient_hero` | ordinary-mob kill (unconfirmed boss) | CANON | NEEDS_VERIFICATION — monsterplus jar exposes only `BloodySlashEntity` class; ancient_hero not confirmed a boss. If not a boss, delete |

Note: `what_waits_in_the_grove` is Medieval (group 508B59840C508057) and holds **29 kill
tasks**; the entire `6D7E8F901A2B30xx` + monsterplus block is a bestiary "Great Hunt"
hunt-list — the single largest ordinary-mob-kill cluster in the pack. The Mowzie's
mini-bosses in the same chapter (wroughtnaut/naga/sculptor at 1..C/1010/1013 — dropping
wrought/naga/sculptor gear) are legitimate side-boss encounters and stay.

`monsterplus:ancient_hero` also killed at asc6 4252010000010008 and `abyssologer`
elsewhere — same NEEDS_VERIFICATION caveat; asc6 is a boss-rise chapter so a boss there is
plausible, but confirm the monsterplus boss list before trusting it.

Proof: `grep -n 'type: "kill"' config/ftbquests/quests/chapters/what_waits_in_the_grove.snbt`
(29 hits); entity/count map in `scratchpad/` run log. Jar rosters:
`unzip -l "mods/born_in_chaos_[Neoforge]_1.21.1_1.7.6.jar" | grep Entity.class`,
`unzip -l "mods/alchemists_garden_regrowth-v9.2.jar" | grep Entity.class`,
`unzip -l "mods/MonsterPlus-Neoforge1.21.1-v1.2.0.0.jar" | grep Entity.class`.

`m3_relics_and_burrows` kills `alchemists_garden:gnome` (7A25EF63FE8D9081) and `yeti`
(1EFA694CE92B2B72) — these are the **ordinary** gnome/yeti (jar has separate
`GnomeKingEntity`/`SpiderQueenEntity` bosses; plain `GnomeEntity`/`YetiEntity` are mobs).
Two more ordinary-mob kills, CANON severity — retarget to their drop items or delete.

---

## Class 2 — DECOR / VARIANT ITEM TASKS

### 2a. Color/material VARIANT that should use one smart_filter task

| chapter | quest id | task | class | severity | suggested fix |
|---|---|---|---|---|---|
| metallurgy | 43EB13F2C3D91789 | item `productivemetalworks:black_foundry_controller` | color variant | CANON | smart_filter accepting any color |
| metallurgy | 2902E58DB70F9409 | item `productivemetalworks:black_foundry_drain` | color variant | CANON | smart_filter any color |
| metallurgy | 2902E58DB70F940A | item `productivemetalworks:black_foundry_tank` | color variant | CANON | smart_filter any color |
| metallurgy | 2902E58DB70F940B | item `productivemetalworks:black_foundry_window` | color variant | CANON | smart_filter any color |
| metallurgy | 2902E58DB70F9414 | item `productivemetalworks:black_foundry_capacitor` | color variant | CANON | smart_filter any color |

Verified: productivemetalworks ships all 16 dye colors of every foundry block
(`unzip -p ... | strings | grep foundry_controller` → black_/blue_/brown_/cyan_/… ) with
free `_from_dye` recolor recipes, so the foundry multiblock works in any color. Forcing
`black_` is a variant-lock. Sanctioned fix, e.g. for the controller:
`root(or(item(productivemetalworks:black_foundry_controller),item(productivemetalworks:blue_foundry_controller), … all 16 …))`
— or, cleaner, use a tag if productivemetalworks ships a `#…:foundry_controller` tag
(verify first). Example live syntax pattern (at1_nuclear_dawn 4E4401100000010A):
`components: { "ftbfiltersystem:filter": "root(or(item(a),item(b)))" }, id: "ftbfiltersystem:smart_filter"`.

Possible variant-multiplication (lower confidence, verify intent):
- m3_relics_and_burrows quest at ~line 1420 requires BOTH
  `alchemists_garden:brown_shroom_staff` AND `red_shroom_staff` as two separate item
  tasks (ids 0FB18AD9604E5469 + 7E8FDF5F6C518F28). If the two staffs are functionally
  identical color variants, collapse to one smart_filter task. HYGIENE. (If they have
  distinct effects, leave — verify in jar.)

### 2b. Purely decorative blocks as tasks

| chapter | quest id | task | class | severity | suggested fix |
|---|---|---|---|---|---|
| ir_create_industrial_addons | 4954081000000036 | item `create_furnitures:brass_chair` | pure decor | CANON | retarget to a Create-addon machine/mechanic item; a chair teaches nothing |
| ren_archive_recordkeeping | 0B03107000000067 | item `betterarcheology:cracked_mud_bricks` | decor block | HYGIENE | retarget to archeology mechanic item (brush/table already gated) |
| ren_archive_recordkeeping | 0B03107000000075 | item `betterarcheology:loot_vase` | decor block | HYGIENE | retarget or drop |
| ren_deeper_darker_otherside | 0B0310600000008A | item `deeperdarker:grime_brick` | decor block | HYGIENE | retarget to Otherside mechanic item |
| metallurgy | 2902E58DB70F9405 | item `productivemetalworks:fire_brick` | borderline | HYGIENE | fire_brick IS a functional foundry-casing component, likely load-bearing — LOW confidence, probably keep |

NOT decor (functional crafting stations / machines — my first-pass regex false-positived
on "table/brick/lantern/panel"; do NOT touch): extendedcrafting `*_table`/`advanced_auto_table`,
`immersiveengineering:circuit_table`, `powergrid:circuit_design_table`,
`overgeared:drafting_table`, `chemicalscience:fractionating_column`, all `*_solar_panel`,
`ifeu:precision/fluid_crafting_table`, `extendedae:assembler_matrix_wall`,
`botanypots:*_botany_pot`, `farmersdelight:cooking_pot`, `hybrid-aquatic:crab_pot`,
`crafting_on_a_stick:*`, `betterarcheology:archeology_table`, `arcanelanterns:life_lantern`
(functional light-source mechanic), `projectred_illumination:red_lantern` (redstone lamp),
`immersiveengineering:electric_lantern`, `create:track_signal` (rail-logistics mechanic).

---

## Class 3 — VANILLA `minecraft:` ITEM TASKS (forbidden, ever)

**90 vanilla-item tasks** across 4 chapters. Per SHARED_CONTEXT the ban is absolute, so all
90 are technically violations. BUT note the Dark-Age chapters are survival-only by pack
canon (Dark Age minimalism), where vanilla items may be a deliberate exception — flag for a
canon call rather than mass-deleting. `minecolonies` is an Annex chapter (age-agnostic
colony-onboarding) and is the worst offender.

Distribution (`Counter` over parsed rows):
- `minecolonies.snbt` — **56** vanilla tasks (BROKEN): iron armor sets (helmet/chestplate/
  leggings/boots), leather armor sets, beds (white_bed, red_bed), 6 vanilla dyes
  (52453550206EC770), book/paper, iron_ore x3, iron_ingot, obsidian, diamond, bow, shield,
  iron_sword, shears, bucket, fishing_rod, carrot/apple/bread, wheat_seeds, flower_pot,
  lily_of_the_valley, enchanted_book, etc.
- `stone_food_and_farming_pressures.snbt` — **14** (CANON, Dark-Age survival): wheat_seeds,
  stone_hoe, potato, carrot, bone_meal, wheat, sweet_berries, bread, composter, cooked_cod,
  fishing_rod, smoker.
- `entering_the_iron_era.snbt` — **11** (CANON, Dark-Age per SHARED_CONTEXT filename-lies
  note): stick, flint, charcoal, bread, stone_pickaxe, coal, raw_copper, copper_ingot x2,
  grindstone, paper.
- `stone_water_weather_and_wounds.snbt` — **9** (CANON, Dark-Age survival): furnace, chest,
  torch, leather + leather armor set, campfire.

Severity: `minecolonies` = **BROKEN** (Annex, not survival-Dark-Age; vanilla armor/dye/bed
tasks have no survival-minimalism excuse and several are pure checkmark-equivalents).
The three stone_* / iron_era Dark-Age chapters = **CANON, canon-call** (survival-only age
may intentionally use vanilla; do not bulk-edit without user ruling).
Suggested fix: minecolonies → retarget to `minecolonies:` blocks/tools/build-tool items
or delete the checkmark-style armor/dye/bed nodes; Dark-Age chapters → hold for canon call.
Full 90-row list in scan output (`scratchpad/analyze.py` stdout).

Proof: `grep -rn 'id: "minecraft:' config/ftbquests/quests/chapters/*.snbt` inside item tasks.

---

## Class 4 — BARE MATERIALS (ingot/dust/plate/gem/shard/rod with no mechanic)

104 bare-material tasks matched. MOST are load-bearing: the FIRST signature metal/crystal
of a freshly-opened dimension or mod (cloggrum/froststeel, deepsilver/lunar_crystal,
draconium, desh/tharsite, cincinnasite, cursium (boss-proof), infinity_ingot (final),
uranium chain, aquarine/neptunium ocean metals, etc.). Those are intro/gateway items — keep.

Genuine filler / duplicate candidates:

| chapter | quest id | task | class | severity | suggested fix |
|---|---|---|---|---|---|
| at7_chaos_convergence | 4358011000EE0008 "Demonite Cache" | item `neovitae:demonite_trim_ingot` | bare ingot, DUPLICATE | HYGIENE | 4358011000EE0009 "The Foreman's Gate" tasks the SAME ingot; collapse the two nodes or retarget one to the downstream trim block |
| at7_chaos_convergence | 4358011000EE0009 "The Foreman's Gate" | item `neovitae:demonite_trim_ingot` | bare ingot, DUPLICATE | HYGIENE | see above |
| metallurgy | 2902E58DB70F… | item `alltheores:iron_dust` | bare dust | HYGIENE-LOW | intro chapter teaches ore-doubling; likely load-bearing, keep with prose |
| metallurgy | — | item `alltheores:brass_ingot` + `brass_plate` | bare ingot/plate | HYGIENE-LOW | foundry-alloy output of the chapter's mechanic; borderline, keep if prose teaches |
| ir_modern_industrialization_steam_industry | — | item `modern_industrialization:steel_dust` | bare dust | HYGIENE | mid-chapter dust; verify it isn't a checkmark before an ingot node |
| ren_observation_experimentation | — | item `modern_industrialization:bronze_plate` + `bronze_gear` | bare plate/gear | HYGIENE-LOW | bronze intro; keep if teaching the MI assembler, else fold |
| ir_power_motion_and_grid | — | item `createaddition:electrum_ingot` | bare ingot | HYGIENE-LOW | first electrum for wiring; likely load-bearing |

Confidence: all Class-4 flags are LOW/HYGIENE except the at7 exact-duplicate ingot
(clear). No SOFTLOCK/BROKEN here. Do NOT strip the dimension-intro ingots.

Proof: `scratchpad/analyze2.py` bare-material section; at7 dup via
`grep -n 'demonite_trim_ingot' config/ftbquests/quests/chapters/at7_chaos_convergence.snbt`.

---

## Create-family output trap check

Checked Create-related chapters (ren_second_mill, ir_create_industrial_addons,
m1_first_mill). No task targets a vanilla `minecraft:` item produced by a Create machine
(e.g. no `minecraft:iron_ingot` / crushed-ore vanilla drops as tasks in those chapters).
`create:andesite_alloy`, `create:experience_nugget`, `create:white_sail`,
`create:track_signal`, `alloyed:steel_sheet`, `createaddition:copper_wire` are all
real `create*`/`alloyed` namespace items, not vanilla passthrough. No trap hits.
(`create:white_sail` is a genuine single-recipe item, not a dye-variant lock.)

---

## Counts

- Class 1 (kill): 16 ILLEGAL ordinary-mob nodes (14 confirmed + 2 NEEDS_VERIFICATION),
  concentrated in what_waits_in_the_grove (14) and m3_relics_and_burrows (2). ~50 boss
  kills are legal.
- Class 2 (decor/variant): 5 confirmed color-variant nodes (metallurgy foundry set) +
  ~4 pure-decor nodes + 1 possible variant-multiplication (m3 shroom staffs).
- Class 3 (vanilla): 90 tasks (minecolonies 56 = BROKEN; 34 in Dark-Age survival chapters
  = CANON-call).
- Class 4 (bare material): 2 clear (at7 duplicate ingot) + ~6 low-confidence HYGIENE;
  ~96 bare-material tasks judged load-bearing (dimension/mod intro items) and left.
