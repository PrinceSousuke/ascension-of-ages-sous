# GROVE REWORK — Execution Plan

**Concept B: "Arm Yourself Against the Dark"** — rework of the Medieval capstone
chapter `what_waits_in_the_grove.snbt`.

- **Status:** PLAN ONLY. This document is the sole artifact of this pass. No
  `.snbt`, KubeJS, config, or lang edits are made here. No git.
- **Author lane:** this is a Fable/CC structural rework (nodes, deps, tasks,
  coords). Prose (`en_us.snbt` values) is written LATER by Opus from the
  `[STUB]`/`[BRIEF]` keys this plan schedules. See `01_MASTER_PREAMBLE.md §5`.
- **Age:** `medieval_times`. Chapter group `508B59840C508057`, chapter id
  `6D7E8F901A2B0501`, `order_index: 3`.
- **Subject file:** `config/ftbquests/quests/chapters/what_waits_in_the_grove.snbt`
  (2684 lines, **60 quest node objects**, all CRLF).
- **Prose file:** `config/ftbquests/quests/lang/en_us.snbt` (bare-LF; keys
  `quest.6D7E8F901A2B*.*`, plus the fresh-id nodes).

> Note on node count: the accepted brainstorm said "48 nodes." A byte-accurate
> brace-depth parse of the live file finds **60** quest objects (the brainstorm
> under-counted the mask/collector/curio leaf nodes and the born_in_chaos brew
> nodes). This plan is built on the verified 60-node inventory in §1.

---

## 0. THE OPEN CANON CALL (Born in Chaos boss status) — A/B TOGGLE

The user is unsure whether `supreme_bonescaller`, `sir_pumpkinhead`, and
`dire_hound_leader` count as "bosses" (keep `kill` tasks) or as ordinary mobs
(retarget to their signature drop items). This plan is **parameterized** on that
one decision. It affects **exactly three nodes** and nothing else in the graph.

- **VARIANT A — "bosses" (keep kills).** Nodes `...3002` / `...3005` / `...3004`
  survive as `kill` tasks on `supreme_bonescaller` / `sir_pumpkinhead` /
  `dire_hound_leader`. Total remaining kills after rework = 13 (see §2).
- **VARIANT B — "ordinary" (DEFAULT, SAFER).** Those three nodes are retargeted
  to `item` tasks on their jar-verified drops:
  - `supreme_bonescaller` → `born_in_chaos_v1:bonescaller_staff`
  - `dire_hound_leader` → `born_in_chaos_v1:fangofthe_hound_leader`
  - `sir_pumpkinhead` → `born_in_chaos_v1:lord_pumpkinheads_lamp`
    (fallback `born_in_chaos_v1:pumpkinhandgun`)
  Total remaining kills after rework = 10 (mowzies + alchemists_garden only).

**Default = VARIANT B.** It is the strictly "bosses only means true bosses"
reading, matches the go-forward zero-ordinary-mob-kill rule the user set, and
matches the Living Harvest item-based precedent. Every step below is written for
Variant B; the three Variant-A deltas are called out inline and collected in §5.

Item-id proofs for the three toggle drops (jar
`mods/born_in_chaos_[Neoforge]_1.21.1_1.7.6.jar`,
`assets/born_in_chaos_v1/lang/en_us.json`):
- `item.born_in_chaos_v1.bonescaller_staff` = "Bonescaller Staff" ✔
- `item.born_in_chaos_v1.fangofthe_hound_leader` = "Fang of the Hound Leader" ✔
- `item.born_in_chaos_v1.lord_pumpkinheads_lamp` = "Lord Pumpkinhead's Lamp" ✔
- `item.born_in_chaos_v1.pumpkinhandgun` = "Pumpkin Pistol" ✔ (fallback)

---

## 1. CURRENT-STATE INVENTORY (verified from disk, 2026-07-02)

### 1.1 Load-bearing / externally-referenced IDs — NEVER re-id or delete

Grep across `config/ftbquests/quests/**` (parser + literal search). The ONLY grove
node referenced by another CHAPTER is the capstone. Every other grove id appears
only inside the grove chapter and its own `en_us.snbt` lang keys.

| ID | Role | External references | Rule |
|---|---|---|---|
| `6D7E8F901A2B0501` | Chapter id | self + `chapter.6D7E8F901A2B0501.*` lang | Keep chapter id + chapter lang keys. |
| `6D7E8F901A2B1054` | Capstone "Master of the Grove" — **the pack's sole `the_renaissance` grant** | `ren_magic_foundations.snbt:15`, `ren_deeper_darker_otherside.snbt:15`, `ren_second_mill_steam_rail_logistics.snbt:15` (all `dependencies:[...1054]`); `journey_to_ascension.snbt:87` (`check_quest` mirror, `targets:["6D7E8F901A2B1054"]`); lang `quest.6D7E8F901A2B1054.*` | **NEVER touch id, deps set, or the 3 command rewards.** All Renaissance tabs open off this. |
| `6D7E8F901A2B1050/1051/1052/1053` | Great Hunt four beasts (feed capstone, `min_required_dependencies:2` each; capstone needs 3-of-4) | internal only, but ARE the capstone fan-in | Keep all four as the boss gate. |
| `097AED7C91033D5E` | Entry gate — **NOT in this file**; it is metallurgy's "Entering the Iron Era" (`metallurgy.snbt:915`) | most grove roots dep on it; also `journey_to_ascension.snbt:65` | External gate. Keep every new lane root depending on it. |
| `2902E58DB70F9442` | **NOT in this file**; a metallurgy node (`metallurgy.snbt:1451`). The current Monster Plus lane root (`7B26069EC5CF71D4`) deps on it. | grove Monster Plus lane roots off it | If the Monster Plus lane is rebuilt with fresh ids, its new root must still dep on `2902E58DB70F9442` (or on `097AED7C91033D5E`) — do not orphan the lane. See §2 decision. |

The capstone's own dependency set is `["...1050","...1051","...1052","...1053"]`
with `min_required_dependencies: 3`. The Great Hunt nodes each currently dep on
`{...3004 (dire_hound_leader kill), ...3002 (supreme_bonescaller kill), ...102C
(elokosa_paw_gibbous item), 5468102A19D28104 (ancient_hero kill)}` with
`min_required_dependencies: 2`. **This fan-in is the correct boss-anchored gate
and its SHAPE is preserved** (the four leaf deps may be re-pointed in Variant B —
see §3 — but the 2-of-4 → 3-of-4 structure and the four beast kills do not change).

### 1.2 Full node inventory (60 nodes)

Format: `node_id | deps | task(s) → target | x,y | flags`. `opt` = `optional:true`.
`sf` = smart_filter task. Kill targets are the offending checklist unless noted.

**Mowzies lane (left, x≈1–6, y 0–16) — the marquee, gear-first:**

| id | deps | task → target | x,y | note |
|---|---|---|---|---|
| `6D7E8F901A2B100C` | `097AED7C91033D5E` | kill `mowziesmobs:ferrous_wroughtnaut` | 3.0,0.0 | BOSS kill — KEEP |
| `6D7E8F901A2B100D` | `...100C` | item `mowziesmobs:wrought_helmet` | 5.5,0.0 | gear |
| `6D7E8F901A2B2101` | `...100C` | item `mowziesmobs:wrought_axe` (`consume:false`) | 5.5,2.0 | gear |
| `6D7E8F901A2B1010` | `097AED7C91033D5E` | kill `mowziesmobs:sculptor` | 3.0,4.0 | BOSS kill — KEEP |
| `6D7E8F901A2B1011` | `...1010` | item `mowziesmobs:sculptor_staff` | 5.5,6.0 | gear |
| `6D7E8F901A2B2102` | `...1010` | item×4 `geomancer_beads/robe/belt/sandals` | 4.5,7.0 | 4-piece set |
| `6D7E8F901A2B1013` | `097AED7C91033D5E` | kill `mowziesmobs:naga` | 3.0,6.0 | BOSS kill — KEEP |
| `6D7E8F901A2B1014` | `...1013` | item `mowziesmobs:naga_fang` | 3.5,8.0 | gear |
| `6D7E8F901A2B1016` | `097AED7C91033D5E` | item `mowziesmobs:spear` | 5.0,11.0 | curio |
| `6D7E8F901A2B1018` | `097AED7C91033D5E` | item `mowziesmobs:bluff_rod` | 5.5,12.0 | curio |
| `6D7E8F901A2B1019` | `097AED7C91033D5E` | item+kill `mowziesmobs:elokosa_howler` | 3.0,14.0 | miniboss (KEEP kill) |
| `6D7E8F901A2B101A` | `...1019` | item `mowziesmobs:elokosa_paw_full` | 5.5,14.0 | gear |
| `6D7E8F901A2B101D` | `097AED7C91033D5E` | item `mowziesmobs:elokosa_paw_crescent` | 10.0,11.5 | gear |
| `6D7E8F901A2B101B` | `097AED7C91033D5E`,`42BFA7916F2CD4FC` | sf item `umvuthana_mask_fury` OR `umvuthana_mask_faith` | 3.0,16.0 | mask |
| `42BFA7916F2CD4FC` | `097AED7C91033D5E` | item `mowziesmobs:umvuthana_mask_fury` | 1.1,9.5 | diamond mask node |
| `6D7E8F901A2B2103` | `...101A` | item `mowziesmobs:glowing_jelly` | 8.0,14.0 | curio |

**Born in Chaos cluster (middle, x≈8–22):**

| id | deps | task → target | x,y | note |
|---|---|---|---|---|
| `4F1787685B57BB4A` | `097AED7C91033D5E` | item `born_in_chaos_v1:pieceofdarkmetal` | 8.25,8.25 | diamond, dark-metal intro |
| `6D7E8F901A2B101F` | `097AED7C91033D5E` | item×2 `dark_metal_ingot`+`dark_metal_block` | 12.0,8.0 | **crafting spine anchor** |
| `6D7E8F901A2B1020` | `...101F` | item `orbofthe_summoner` | 11.0,9.0 | brew |
| `6D7E8F901A2B1021` | `...101D` | item `death_totem` | 12.0,12.5 | brew |
| `6D7E8F901A2B1022` | `...101D` | item×2 `monster_skin`(+?) | 9.5,10.0 | `opt` |
| `6D7E8F901A2B1023` | `...101F` | item×2 `seedof_chaos`(+?) | 14.0,10.5 | brew |
| `6D7E8F901A2B1024` | `...101F` | item `staff_of_magic_arrows` | 12.5,10.5 | weapon |
| `6D7E8F901A2B1025` | `...101D` | item `spiritual_dust` | 12.0,14.0 | brew |
| `6D7E8F901A2B1026` | `...101F` | **kill `nightmare_stalker`** | 11.5,10.0 | OFFENDING kill |
| `6D7E8F901A2B1027` | `...2103` | item `elixirof_wither_resistance` | 10.0,14.0 | elixir |
| `6D7E8F901A2B1028` | `...102C` | item `tombstone_the_gentleman_frog` | 16.5,12.5 | curio (block-lang, resolves as item) |
| `6D7E8F901A2B1029` | `...101F` | item `transmuting_elixir` | 14.5,9.5 | elixir |
| `6D7E8F901A2B102A` | `...102C` | item `elixir_of_vampirism` | 17.0,13.5 | elixir |
| `6D7E8F901A2B102C` | `...1024`,`...1029` | item `mowziesmobs:elokosa_paw_gibbous` | 18.0,10.5 | **feeds Great Hunt + gnome/spider + collector** |
| `6D7E8F901A2B3001` | `...101F` | **kill `bonescaller`** | 15.5,8.0 | OFFENDING kill |
| `6D7E8F901A2B3002` | `...3001` | **kill `supreme_bonescaller`** | 14.95,5.2 | TOGGLE node (feeds Great Hunt) |
| `6D7E8F901A2B3003` | `...3002` | **kill `dread_hound`** | 18.5,7.0 | OFFENDING kill |
| `6D7E8F901A2B3004` | `...3003` | **kill `dire_hound_leader`** | 22.1,5.85 | TOGGLE node (feeds Great Hunt) |
| `6D7E8F901A2B3005` | `31F70E7481C6CE82` | **kill `sir_pumpkinhead`** | 13.0,1.95 | TOGGLE node |
| `6D7E8F901A2B3006` | `...102C` | **kill×2 `door_knight`+`fallen_chaos_knight`** | 18.0,14.0 | OFFENDING kill |
| `6D7E8F901A2B3007` | `29DE51ABF8B5D7FA` | **kill `lifestealer`** | 18.0,16.0 | OFFENDING kill |
| `6D7E8F901A2B3008` | `280E76D5A93E6B6C` | **kill×2 `zombie_bruiser`+`bone_imp`** | 22.5,10.5 | OFFENDING kill |
| `6D7E8F901A2B3009` | `29DE51ABF8B5D7FA` | **kill×2 `corpse_fly`+`mr_pumpkin`** | 20.0,16.0 | OFFENDING kill, `opt` |

**Monster Plus cluster (top, x≈8–14, y negative):**

| id | deps | task → target | x,y | note |
|---|---|---|---|---|
| `7B26069EC5CF71D4` | `2902E58DB70F9442` (metallurgy) | **kill×2 `desert_sorceress`+`desert_acolyte`** | 8.0,-4.0 | OFFENDING kill (lane root) |
| `6D7E8F901A2B300A` | `7B26069EC5CF71D4` | **kill×2 `crystal_zombie`+`spectral_skull`** | 8.0,-2.0 | OFFENDING kill |
| `442C27F2E00B325C` | `...300A` | kill `abyssologer` | 9.75,-1.3 | miniboss (borderline; rsquare) |
| `1F215CC13B2A1F81` | `442C27F2E00B325C`,`7B26069EC5CF71D4` (minreq 1) | item `ancient_scroll` | 12.0,-2.0 | relic |
| `6D7E8F901A2B300E` | `442C27F2E00B325C`,`7B26069EC5CF71D4` (minreq 1) | item×2 `crystal_shard`(+?) | 12.0,-4.0 | relic |
| `6D7E8F901A2B300F` | `442C27F2E00B325C`,`7B26069EC5CF71D4` (minreq 1) | item×2 `dark_chestplate`(+?) | 10.0,-4.0 | gear |
| `55E3541DEC3D3BE4` | `...300F`,`...300E` | item `dark_helmet` | 14.0,-6.0 | gear |
| `5468102A19D28104` | `097AED7C91033D5E` | kill `ancient_hero` | 18.85,-0.65 | miniboss (rsquare; feeds Great Hunt) |
| `31F70E7481C6CE82` | `5468102A19D28104` | item `ancient_broken_sword` | 14.0,3.0 | relic |

**Great Hunt convergence + capstone:**

| id | deps | task → target | x,y | note |
|---|---|---|---|---|
| `6D7E8F901A2B1050` | `...3004`,`...3002`,`...102C`,`5468102A19D28104` (minreq 2) | kill `ferrous_wroughtnaut` | 17.0,3.0 | Great Hunt |
| `6D7E8F901A2B1051` | same 4 (minreq 2) | kill `foliaath` | 19.5,2.5 | Great Hunt |
| `6D7E8F901A2B1052` | same 4 (minreq 2) | kill `frostmaw` | 20.5,3.0 | Great Hunt |
| `6D7E8F901A2B1053` | same 4 (minreq 2) | kill `grottol` | 18.5,2.5 | Great Hunt |
| `6D7E8F901A2B1054` | `...1050/1051/1052/1053` (minreq 3) | timer + 3 command grants | 18.75,5.25 | **CAPSTONE — the_renaissance grant** |

**Alchemist's Garden side bosses:**

| id | deps | task → target | x,y | note |
|---|---|---|---|---|
| `280E76D5A93E6B6C` | `...102C` | item+kill `alchemists_garden:gnome_king` | 21.0,12.0 | real side boss, loot bag |
| `09B42DE5A859BA0D` | `280E76D5A93E6B6C` | item `kings_shovel` | 23.0,12.0 | reward |
| `29DE51ABF8B5D7FA` | `...102C` | item+kill `alchemists_garden:spider_queen` | 21.0,14.0 | real side boss, loot bag |
| `0ABD97C61DE42DCF` | `29DE51ABF8B5D7FA` | loot+item `queens_fang` (loot table `8849093687305634787`) | 23.0,14.0 | reward |

**Collector + Crittersandcompanions tail:**

| id | deps | task → target | x,y | note |
|---|---|---|---|---|
| `0713486EDCE7D787` | `...102C` | sf item AND(`elokosa_paw_crescent`+`full`+`gibbous`) | 22.0,8.0 | square collector |
| `E101BB0D29F60954` | `...100C` | item `crittersandcompanions:grappling_hook` | 0.0,19.0 | `opt` ambient |
| `92614B6AD7E19E44` | `E101BB0D29F60954` | item `crittersandcompanions:silk_lead` | 2.5,19.0 | `opt` ambient |

### 1.3 Rewards (current)

Almost all `xp` (25 typical; 50 on the paw collector; 75 on the two diamond
nodes `42BFA7916F2CD4FC` / `4F1787685B57BB4A`). Real item/loot rewards only on:
`280E76D5A93E6B6C` (gnome_king_loot_bag), `29DE51ABF8B5D7FA`
(spider_queen_loot_bag), `0ABD97C61DE42DCF` (loot table `8849093687305634787`).
Capstone `...1054` = `timer` task + 3 command rewards, no item reward.

### 1.4 Byte / format facts (MUST preserve)

- **Grove chapter is 100% CRLF** (2684/2684 line endings are `\r\n`, 0 bare LF).
  Any edit tool must write CRLF back. Verify post-edit with a Python byte count
  (`raw.count(b'\r\n')` vs `raw.count(b'\n')`) — grep/`file`/`cat` lie about this.
- **`en_us.snbt` is 100% bare LF** (0 CRLF, 7702 LF). New lang keys must be bare
  LF. Do NOT mix. This is a per-file difference, not an age split.
- Every task carries the inert `PlayerSpells` + `SkillsLevel` blocks (More Quest
  Types mixin, `check:0b`). **Do NOT strip them** — they regenerate on save and
  removing them only churns the file.
- `quest_desc` values in `en_us.snbt` are the array-of-strings form. Any new
  key's `.quest_desc` must be an array (`[ "..." ]`), matching pack standard.

---

## 2. TARGET DESIGN — "Arm Yourself Against the Dark"

Three parallel vertical equip-lanes hanging off the metallurgy gate, converging
on the unchanged Great Hunt column on the right. Lanes never interleave →
crossing-free by construction.

Narrative frame (for Opus, not authored here): metallurgy gave you iron; the
grove is where iron is not enough. Each of the three dark powers yields a weapon
or armor line; mastering the four great beasts seals the Medieval era.

Target node count: **~26–28** (down from 60). Kills after rework: **10**
(Variant B) — 4 mowzies headliner/miniboss + 4 Great Hunt mowzies + 2
alchemists_garden side bosses. (Variant A = 13, adding back the three BiC nodes.)

### 2.1 LANE 1 — The Beast-Forged Kit (Mowzies, ~9 nodes) — REUSE existing ids

All ids and coords below already exist; this lane is **kept nearly verbatim**.
Boss kills stay (mowzies bosses are legal and are the mod's whole point).

| id | keep/new | task → target (jar proof) | deps | x,y | reward |
|---|---|---|---|---|---|
| `6D7E8F901A2B100C` | keep | kill `mowziesmobs:ferrous_wroughtnaut` | `097AED7C91033D5E` | 3.0,0.0 | xp25 |
| `6D7E8F901A2B100D` | keep | item `mowziesmobs:wrought_helmet` `[P1]` | `...100C` | 5.5,0.0 | +item reward: `wrought_helmet` |
| `6D7E8F901A2B2101` | keep | item `mowziesmobs:wrought_axe` `[P1]` | `...100C` | 5.5,2.0 | xp25 |
| `6D7E8F901A2B1010` | keep | kill `mowziesmobs:sculptor` | `097AED7C91033D5E` | 3.0,4.0 | xp25 |
| `6D7E8F901A2B2102` | keep | item×4 geomancer set `[P1]` | `...1010` | 4.5,7.0 | xp50 |
| `6D7E8F901A2B1011` | keep | item `mowziesmobs:sculptor_staff` `[P1]` | `...1010` | 5.5,6.0 | +item reward |
| `6D7E8F901A2B1013` | keep | kill `mowziesmobs:naga` | `097AED7C91033D5E` | 3.0,6.0 | xp25 |
| `6D7E8F901A2B1014` | retarget-item | item `mowziesmobs:naga_fang_dagger` `[P1]` (currently `naga_fang`) | `...1013` | 3.5,8.0 | +item reward |
| `6D7E8F901A2B1019` | keep | kill `mowziesmobs:elokosa_howler` | `097AED7C91033D5E` | 3.0,14.0 | xp25 |
| `6D7E8F901A2B101A` | keep | item `mowziesmobs:elokosa_paw_full` | `...1019` | 5.5,14.0 | xp25 |
| `6D7E8F901A2B101D` | keep | item `mowziesmobs:elokosa_paw_crescent` | `097AED7C91033D5E` | 10.0,11.5 | xp25 |
| `0713486EDCE7D787` | keep | sf AND(crescent+full+gibbous) | `...102C` | 22.0,8.0 | xp50 |
| `42BFA7916F2CD4FC` | keep (opt) | item `mowziesmobs:umvuthana_mask_fury` | `097AED7C91033D5E` | 1.1,9.5 | xp75 |
| `6D7E8F901A2B101B` | keep (opt) | sf mask_fury/faith | `...101B` deps | 3.0,16.0 | xp25 |

> Jar proofs (`mods/mowziesmobs-1.21.1-1.8.2.jar`,
> `assets/mowziesmobs/lang/en_us.json`): `item.mowziesmobs.wrought_helmet`,
> `.wrought_axe`, `.sculptor`(entity)/`.sculptor_staff`, `.geomancer_beads`,
> `.geomancer_robe`, `.geomancer_belt`, `.geomancer_sandals`,
> `.naga_fang_dagger` ("Naga Fang Dagger" ✔ — the upgraded craftable, replaces
> raw `naga_fang`), `.elokosa_paw_full/_crescent/_gibbous`,
> `.umvuthana_mask_fury` — all present.
> OPTIONAL curios that may be pruned for tightness (all verified, keep only if
> the lane feels thin): `spear`, `bluff_rod`, `blowgun`+`dart`, `sand_rake`,
> `sol_visage`, `earthrend_gauntlet`, `glowing_jelly`.

Lane-1 retarget: `...1014` moves from raw `naga_fang` to the crafted
`naga_fang_dagger` (real usable weapon; the raw fang is only an ingredient).
`consume_items` handling unchanged from source.

### 2.2 LANE 2 — The Dark Metal Armory (Born in Chaos, ~7 nodes)

Convert the bestiary web into a crafting/equip progression. Anchor on the
existing dark-metal spine node; everything downstream is item-task or (Variant A
only) a single boss node.

| id | keep/new | task → target (jar proof) | deps | x,y | reward |
|---|---|---|---|---|---|
| `4F1787685B57BB4A` | keep | item `born_in_chaos_v1:pieceofdarkmetal` | `097AED7C91033D5E` | 8.25,8.25 | xp75 |
| `6D7E8F901A2B101F` | keep | item×2 `dark_metal_ingot`+`dark_metal_block` | `4F1787685B57BB4A` | 12.0,8.0 | xp25 |
| `6D7E8F901A2B2104` | **NEW** | sf item, dark-metal armor 4-piece: `dark_metal_armor_helmet/chestplate/leggings/boots` | `...101F` | 12.0,9.5 | +item reward: chestplate |
| `6D7E8F901A2B2105` | **NEW** | `choice`/sf one dark weapon: `darkwarblade` \| `nightmare_scythe` \| `soul_cutlass` \| `great_reaper_axe` \| `sharpened_dark_metal_sword` \| `spiritual_sword` | `...101F` | 13.5,10.5 | +item reward |
| `6D7E8F901A2B1024` | keep | item `born_in_chaos_v1:staff_of_magic_arrows` | `...101F` | 12.5,11.5 | xp25 |
| `6D7E8F901A2B2106` | **NEW** | `choice`/sf one charm: `charmof_power` \| `charmof_fury` \| `charmof_endurance` \| `charmof_resistance` \| `charmof_stealth` | `...2104` | 11.0,11.0 | xp25 |
| `6D7E8F901A2B102A` | keep | item `born_in_chaos_v1:elixir_of_vampirism` | `...2105` (re-dep; see §3) | 14.5,11.5 | xp25 |
| `6D7E8F901A2B102C` | keep | item `mowziesmobs:elokosa_paw_gibbous` | `...1024`,`...102A` (re-dep; see §3) | 18.0,10.5 | xp50 |

> Jar proofs (`mods/born_in_chaos_[Neoforge]_1.21.1_1.7.6.jar`,
> `assets/born_in_chaos_v1/lang/en_us.json`): `item.born_in_chaos_v1.` +
> `pieceofdarkmetal`, `dark_metal_ingot`, `dark_metal_block` (block-lang, resolves
> as item), `dark_metal_armor_helmet/_chestplate/_leggings/_boots`, `darkwarblade`,
> `nightmare_scythe`, `soul_cutlass`, `great_reaper_axe`,
> `sharpened_dark_metal_sword`, `spiritual_sword`, `charmof_power/_fury/_endurance/
> _resistance/_stealth`, `staff_of_magic_arrows`, `elixir_of_vampirism` — all present.

**`...102C` (elokosa_paw_gibbous) is load-bearing WITHIN the chapter** — it feeds
the Great Hunt fan-in, both alchemists_garden side bosses, and the paw collector.
Keep its id; only its upstream deps change (see §3). Its task item is unchanged.

**Variant A only:** re-add ONE born_in_chaos boss node inside Lane 2 as flavor
(reuse `6D7E8F901A2B3002` as `kill supreme_bonescaller`, deps `...101F`, x≈15,y≈6,
reward `bonescaller_staff` item). It must NOT become a required upstream of `...102C`
or the Great Hunt (keep it a leaf so it never re-introduces a kill gate).

### 2.3 LANE 3 — Relics of the Fallen (Monster Plus + Alchemist's Garden, ~7 nodes)

Monster Plus becomes a short item-only relic line (zero kills). Alchemist's Garden
side bosses stay as optional trophies at the tail. `ancient_hero` /`abyssologer`
retarget to item drops (Variant B treats both as ordinary — they are `rsquare`
minibosses, not true bosses; the Great Hunt no longer needs the `ancient_hero`
kill once its fan-in is re-pointed, see §3).

| id | keep/new | task → target (jar proof) | deps | x,y | reward |
|---|---|---|---|---|---|
| `31F70E7481C6CE82` | keep | item `monsterplus:ancient_broken_sword` | `097AED7C91033D5E` (re-dep; see §3) | 14.0,-4.0 | +item reward |
| `1F215CC13B2A1F81` | keep | item `monsterplus:ancient_scroll` | `31F70E7481C6CE82` | 12.0,-2.0 | xp25 |
| `6D7E8F901A2B300E` | keep | item `monsterplus:crystal_shard` | `1F215CC13B2A1F81` | 12.0,-4.0 | xp25 |
| `6D7E8F901A2B300F` | keep | item `monsterplus:dark_chestplate` | `...300E` | 10.0,-4.0 | xp25 |
| `55E3541DEC3D3BE4` | keep | item `monsterplus:dark_helmet` | `...300F` | 14.0,-6.0 | +item reward |
| `280E76D5A93E6B6C` | keep (opt) | item+kill `alchemists_garden:gnome_king` | `...102C` | 21.0,12.0 | gnome_king_loot_bag |
| `09B42DE5A859BA0D` | keep (opt) | item `alchemists_garden:kings_shovel` | `280E76D5A93E6B6C` | 23.0,12.0 | xp25 |
| `29DE51ABF8B5D7FA` | keep (opt) | item+kill `alchemists_garden:spider_queen` | `...102C` | 21.0,14.0 | spider_queen_loot_bag |
| `0ABD97C61DE42DCF` | keep (opt) | loot+item `alchemists_garden:queens_fang` | `29DE51ABF8B5D7FA` | 23.0,14.0 | loot table `8849093687305634787` |

> Jar proofs: monsterplus (`mods/MonsterPlus-Neoforge1.21.1-v1.2.0.0.jar`,
> `assets/monsterplus/lang/en_us.json`): `item.monsterplus.ancient_broken_sword`,
> `.ancient_scroll`, `.crystal_shard`, `.dark_chestplate`, `.dark_helmet`,
> `.dark_essence`, `.gnawing_jaw` — all present. **Monster Plus dark set is
> helmet+chestplate ONLY** (no dark_leggings/dark_boots in lang) — do NOT author a
> full 4-piece "dark set" node. alchemists_garden gear (`kings_shovel`,
> `queens_fang`) and the loot bags stay as in the current file.

> Design note: Monster Plus is the shallowest family. If, at author time, Lane 3
> feels like padding, fall back toward brainstorm Concept C (drop Monster Plus to a
> single optional `ancient_broken_sword` node). Default here keeps the short relic
> line. Do NOT expand it past what the jar actually holds.

### 2.4 CAPSTONE — The Great Hunt (UNCHANGED shape)

| id | keep | task → target | deps | x,y |
|---|---|---|---|---|
| `6D7E8F901A2B1050` | keep | kill `mowziesmobs:ferrous_wroughtnaut` | 4-dep set (minreq 2) — see §3 | 17.0,3.0 |
| `6D7E8F901A2B1051` | keep | kill `mowziesmobs:foliaath` | same | 19.5,2.5 |
| `6D7E8F901A2B1052` | keep | kill `mowziesmobs:frostmaw` | same | 20.5,3.0 |
| `6D7E8F901A2B1053` | keep | kill `mowziesmobs:grottol` | same | 18.5,2.5 |
| `6D7E8F901A2B1054` | keep | timer + 3 command grants | `...1050/1051/1052/1053` (minreq 3) | 18.75,5.25 |

The four beast kills, the 2-of-4 fan-in, the 3-of-4 capstone, and the three grant
commands are all **byte-identical to the current file**. Only the four leaf deps
inside `...1050–1053` are re-pointed (§3) because two of their current deps
(`...3002`, `5468102A19D28104`) change task type in Variant B.

---

## 3. NODE-BY-NODE MIGRATION TABLE

Legend: **KEEP** (byte-identical), **RETARGET** (same id, change task type/target),
**DELETE** (remove node + its lang keys), **NEW** (fresh 16-hex id).

### 3.1 Mowzies lane

| current node | action | dep rewiring |
|---|---|---|
| `...100C`,`...100D`,`...2101`,`...1010`,`...2102`,`...1011`,`...1013`,`...1019`,`...101A`,`...101D`,`0713486EDCE7D787`,`42BFA7916F2CD4FC`,`...101B` | KEEP | none |
| `...1014` | RETARGET | item `naga_fang` → item `naga_fang_dagger`; dep `...1013` unchanged |
| `...1016` (spear), `...1018` (bluff_rod), `...2103` (glowing_jelly) | KEEP-or-DELETE (curio prune, author's call for lane tightness) | all leaves; if deleted, delete lang keys, no dep impact |

### 3.2 Born in Chaos cluster

| current node | action | dep rewiring |
|---|---|---|
| `4F1787685B57BB4A`, `...101F`, `...1024`, `...102A` | KEEP | `...102A` re-dep: was `...102C` → now `...2105` (dark weapon), so the elixir hangs off the armory not the paw. `...102C` deps change (below). |
| `...102C` (elokosa_paw_gibbous) | KEEP task | deps was `...1024`,`...1029` → now `...1024`,`...102A`. (`...1029` transmuting_elixir is deleted; substitute the vampirism elixir as the second upstream so `...102C` still requires two armory steps.) |
| `...1020` (orb_summoner), `...1021` (death_totem), `...1022` (monster_skin, opt), `...1023` (seedof_chaos), `...1025` (spiritual_dust), `...1027` (elixir_wither_res), `...1028` (frog tombstone), `...1029` (transmuting_elixir) | DELETE (brew/curio sprawl; all leaves or leaf-adjacent) | delete lang keys. `...1027` dep was `...2103`; `...1028` dep was `...102C`; none are depended-on by kept nodes → safe. |
| `...1026` (kill nightmare_stalker) | DELETE | leaf; delete lang keys |
| `...3001` (kill bonescaller), `...3003` (kill dread_hound), `...3006` (kill door_knight/fallen_chaos_knight), `...3007` (kill lifestealer), `...3008` (kill zombie_bruiser/bone_imp), `...3009` (kill corpse_fly/mr_pumpkin) | DELETE | all leaves; delete lang keys. `...3001`/`...3003` were the chain feeding `...3002`/`...3004` — see toggle rows. |
| `...3002` (supreme_bonescaller) | **VARIANT B: DELETE** / **VARIANT A: KEEP** (re-dep to `...101F`, becomes leaf) | It is a current dep of all 4 Great Hunt nodes. In BOTH variants, **re-point the Great Hunt deps off it** (§3.5). In A it survives as a leaf flavor kill. |
| `...3004` (dire_hound_leader) | **VARIANT B: DELETE** / **VARIANT A: KEEP** (re-dep to `...101F`, leaf) | Current dep of all 4 Great Hunt nodes → re-point (§3.5). |
| `...3005` (sir_pumpkinhead) | **VARIANT B: DELETE** (its drop is optional; or RETARGET to `lord_pumpkinheads_lamp` if kept as flavor) / **VARIANT A: KEEP** (re-dep to `31F70E7481C6CE82` or `...101F`, leaf) | not referenced by Great Hunt; leaf either way |
| `2902...` deorum? n/a | — | — |
| **NEW** `...2104` (dark armor sf), `...2105` (dark weapon choice), `...2106` (charm choice) | NEW | see §2.2 deps |

### 3.3 Monster Plus cluster

| current node | action | dep rewiring |
|---|---|---|
| `7B26069EC5CF71D4` (kill desert_sorceress/acolyte) | DELETE | It is the lane root (deps metallurgy `2902E58DB70F9442`) and is depended on by `...300A`,`1F215CC13B2A1F81`,`...300E`,`...300F` (minreq-1 branches). Re-root the relic line on `31F70E7481C6CE82` instead (§2.3). Delete lang keys. |
| `...300A` (kill crystal_zombie/spectral_skull) | DELETE | depended on by `442C27F2E00B325C`; that node also deleted → safe |
| `442C27F2E00B325C` (kill abyssologer) | DELETE (Variant B) | depended on by `1F215CC13B2A1F81`,`...300E`,`...300F` as a minreq-1 alt with `7B26069...`. After both deleted, re-dep those three onto the relic chain (§2.3). |
| `1F215CC13B2A1F81` (ancient_scroll) | KEEP task | dep set was `442C27...`,`7B26069...` (minreq 1) → now single dep `31F70E7481C6CE82`; drop `min_required_dependencies`. |
| `...300E` (crystal_shard) | KEEP task | dep → `1F215CC13B2A1F81`; drop minreq |
| `...300F` (dark_chestplate) | KEEP task | dep → `...300E`; drop minreq |
| `55E3541DEC3D3BE4` (dark_helmet) | KEEP | dep was `...300F`,`...300E` → now `...300F` only |
| `5468102A19D28104` (kill ancient_hero) | **VARIANT B: RETARGET** to item (drop) or DELETE / **VARIANT A: KEEP** | It is a current Great Hunt dep. Re-point Great Hunt (§3.5). If retargeted, its drop is `monsterplus` — verify a real drop item at author time; if none clean, DELETE and rely on the re-pointed fan-in. `31F70E7481C6CE82` (ancient_broken_sword) currently deps on it → re-root `31F70E...` on `097AED7C91033D5E` (§2.3). |

### 3.4 Alchemist's Garden + tail

| current node | action | dep rewiring |
|---|---|---|
| `280E76D5A93E6B6C`,`09B42DE5A859BA0D`,`29DE51ABF8B5D7FA`,`0ABD97C61DE42DCF` | KEEP (mark `optional:true` on the two boss nodes if not already) | deps unchanged (both root on `...102C`, which is preserved) |
| `E101BB0D29F60954`,`92614B6AD7E19E44` (crittersandcompanions ambient) | DELETE (off-theme filler per brainstorm) | both `opt` leaves; delete lang keys |

### 3.5 Great Hunt fan-in re-point (BOTH variants) — critical

Current `...1050/1051/1052/1053` deps =
`["...3004","...3002","...102C","5468102A19D28104"]`, minreq 2.
Two of those (`...3002`, `5468102A19D28104`) change task type or are deleted in
Variant B, so the fan-in must be re-pointed to four PRESERVED item/boss anchors,
keeping the "2-of-4, boss-anchored" character:

- **New 4-dep set (Variant B):**
  `["6D7E8F901A2B102C","0713486EDCE7D787","55E3541DEC3D3BE4","6D7E8F901A2B2104"]`
  = {elokosa_paw_gibbous, three-paw collector, monsterplus dark_helmet, dark-metal
  armor set}. minreq 2 unchanged. This keeps the gate as "prove two of your three
  equip-lanes' capstones before the Great Hunt opens," which is stronger and fully
  item/boss-anchored (no ordinary-mob kill in the gate).
- **Variant A:** keep the current set but swap the two toggle nodes' task type is
  moot (they stay kills); simplest is to use the SAME new item set as Variant B for
  consistency, and let `...3002`/`...3004` live as leaf flavor. Recommended: use the
  Variant-B dep set in both variants so the gate is identical regardless of the
  canon call. The toggle then only affects whether the three BiC nodes exist.

Capstone `...1054` deps (`...1050–1053`, minreq 3) and its three grant commands:
**UNCHANGED in both variants.**

### 3.6 Deletion summary

- **Variant B deletes (leaves/re-rootable, no external refs):** `...1020`,
  `...1021`, `...1022`, `...1023`, `...1025`, `...1026`, `...1027`, `...1028`,
  `...1029`, `...3001`, `...3002`, `...3003`, `...3004`, `...3005` (or retarget),
  `...3006`, `...3007`, `...3008`, `...3009`, `7B26069EC5CF71D4`, `...300A`,
  `442C27F2E00B325C`, `E101BB0D29F60954`, `92614B6AD7E19E44`; RETARGET/DELETE
  `5468102A19D28104`; optional curio prune `...1016`,`...1018`,`...2103`.
- **Variant A keeps** `...3002`, `...3004`, `...3005` (as re-dep'd leaf kills).
- **NEW ids:** `...2104` (dark armor), `...2105` (dark weapon), `...2106` (charm).
  Generate fresh 16-hex ids not colliding with any existing grove/other-chapter id
  (anchored `grep -P '^\s+id: "'` across all chapters before assigning).

---

## 4. LANG-KEY PLAN (`config/ftbquests/quests/lang/en_us.snbt`)

Fable emits `[STUB]`/`[BRIEF]` per `01_MASTER_PREAMBLE.md §5`; Opus writes final
prose later. All new keys bare-LF, `.quest_desc` as a string array.

### 4.1 SURVIVE unchanged (do not touch)

- `chapter.6D7E8F901A2B0501.*` (title/subtitle) — chapter stays.
- Capstone `quest.6D7E8F901A2B1054.{title,quest_subtitle,quest_desc}` — verbatim.
- Great Hunt `quest.6D7E8F901A2B1050/1051/1052/1053.*` — verbatim.
- All KEEP nodes in §2 retain their existing keys: mowzies lane
  (`...100C/100D/2101/1010/2102/1011/1013/1019/101A/101D/101B/42BFA.../0713...`),
  BiC (`4F17.../101F/1024`), Monster Plus relic (`31F7.../1F21.../300E/300F/55E3...`),
  alchemists_garden (`280E.../09B4.../29DE.../0ABD...`).

### 4.2 RETARGET nodes — refresh prose (existing keys, mark for Opus rewrite)

These keep their id but change what they teach, so their prose is now stale.
Overwrite the three keys with `[STUB]`/`[BRIEF]` so Opus re-writes:

- `quest.6D7E8F901A2B1014.*` — now teaches crafting the **Naga Fang Dagger** from
  the naga fang (was: collect raw fang).
- `quest.6D7E8F901A2B102A.*` — now the elixir hangs off the dark-metal armory
  (re-dep), teaching Elixir of Vampirism use in a drawn-out fight.
- `quest.6D7E8F901A2B102C.*` — upstream deps changed; re-teach as "gather the
  gibbous paw once your armory is proven."
- `quest.1F215CC13B2A1F81.*`, `quest.6D7E8F901A2B300E.*`,
  `quest.6D7E8F901A2B300F.*`, `quest.55E3541DEC3D3BE4.*` — relic line is now
  item-only, re-rooted; refresh to remove any kill framing.
- (Variant A) `quest.6D7E8F901A2B3002/3004/3005.*` — reframe as single flavor
  boss kills, not a bestiary chain.

### 4.3 NEW keys — add `[STUB]`/`[BRIEF]` (three nodes)

For each new id add `.title`, `.quest_subtitle`, `.quest_desc` (array), e.g.:

```
quest.<NEW_2104>.title: "[STUB] title"
quest.<NEW_2104>.quest_subtitle: "[STUB] subtitle"
quest.<NEW_2104>.quest_desc: ["[BRIEF] teaches: craft the full Born in Chaos dark_metal armor 4-piece (helmet/chestplate/leggings/boots) from dark_metal_ingot; smart_filter accepts any of the four; prior node = ...101F dark metal spine; set bonus = rampage-at-low-HP + wither resistance. Opus: 2-4 para instruction-first, no em dashes."]
```

- `<NEW_2104>` — dark-metal armor set (BRIEF as above).
- `<NEW_2105>` — dark weapon choice (BRIEF: choice/sf across darkwarblade /
  nightmare_scythe / soul_cutlass / great_reaper_axe / sharpened_dark_metal_sword /
  spiritual_sword; pick one; each has a distinct combat gimmick; prior = ...101F).
- `<NEW_2106>` — charm choice (BRIEF: choice/sf across charmof_power/_fury/
  _endurance/_resistance/_stealth; requires Ethereal Spirit to activate; prior =
  ...2104 armor).

### 4.4 DELETE keys

For every DELETED node in §3.6, remove its three `quest.<id>.*` keys from
`en_us.snbt` (they are otherwise orphaned). Anchored removal by id prefix; verify
no other file references the key first (none do — §1.1 shows only en_us.snbt).

---

## 5. THE BORN IN CHAOS DECISION POINT (A/B) — collected

Set ONE flag at author time. Default = **B**.

| | VARIANT A (bosses) | VARIANT B (ordinary — DEFAULT) |
|---|---|---|
| `...3002` supreme_bonescaller | KEEP as leaf kill, dep `...101F`, reward `bonescaller_staff` | DELETE (or Lane-2 leaf item `bonescaller_staff`) |
| `...3004` dire_hound_leader | KEEP as leaf kill, dep `...101F` | DELETE (or leaf item `fangofthe_hound_leader`) |
| `...3005` sir_pumpkinhead | KEEP as leaf kill, dep `...101F` | DELETE (or leaf item `lord_pumpkinheads_lamp`) |
| Great Hunt fan-in | use §3.5 item set (recommended, identical to B) | §3.5 item set |
| Remaining kills in chapter | 13 | 10 |
| Lang | keep/refresh `...3002/3004/3005.*` | delete those keys |

**Nothing else in the plan changes between A and B.** The capstone, grant, Great
Hunt beasts, all three equip-lanes, and the fan-in dep set are identical. The
toggle is fully localized to these three node ids. `bonescaller`, `dread_hound`,
`door_knight`, `fallen_chaos_knight`, `lifestealer`, `zombie_bruiser`, `bone_imp`,
`corpse_fly`, `mr_pumpkin`, `nightmare_stalker`, `crystal_zombie`,
`spectral_skull`, `desert_sorceress`, `desert_acolyte` are DELETED in BOTH
variants (they are rank-and-file, not in question).

---

## 6. EXECUTION TASK LIST (bite-sized, verify per step)

Work directly in the working tree; **no git** (per repo memory: commit is done by
the human, agents leave changes in the tree). Use Desktop Commander / Python byte
reads as ground truth, not the editor mount.

1. **Freeze the canon flag.** Record A or B at top of the work session. Default B.
   *Verify:* flag written before any edit.
2. **Re-confirm externally-referenced ids unchanged target.** Anchored grep the
   four Ren/journey references to `6D7E8F901A2B1054` still resolve.
   *Verify:* `grep -rn 6D7E8F901A2B1054 config/ftbquests/quests/chapters` shows
   the same 4 files + capstone def.
3. **Assign three NEW ids.** Generate `...2104/2105/2106` (or any fresh 16-hex),
   confirm no collision.
   *Verify:* `grep -P '^\s+id: "'` across all chapters returns 0 hits for each.
4. **Read the grove file as CRLF bytes; snapshot line-ending count.**
   *Verify:* Python `raw.count(b'\r\n')==2684`, bare-LF `==0` (baseline to match
   after edit).
5. **Delete rank-and-file kill nodes + curio sprawl (§3.6).** Remove whole quest
   objects; keep surrounding CRLF structure intact.
   *Verify:* node count drops as expected; `node`-equivalent SNBT sanity — file
   still parses via the §1.2 brace parser with no orphaned braces.
6. **Retarget `...1014` and the Monster Plus relic chain (§3.1/§3.3).** Change
   task item ids + dep sets; drop stale `min_required_dependencies` where a node
   goes single-dep.
   *Verify:* each retargeted item id present in the relevant jar lang (re-run the
   §2 grep proofs).
7. **Build Lane 2 armory: add `...2104/2105/2106`, re-dep `...102A`, `...102C`
   (§2.2/§3.2).**
   *Verify:* smart_filter / choice task syntax matches an existing working example
   (`...101B` for sf; a live `choice` node elsewhere); all item ids jar-proven.
8. **Re-point Great Hunt fan-in to the §3.5 item set.** Edit deps of
   `...1050/1051/1052/1053` only; leave their kill tasks and `min_required_dependencies:2`.
   *Verify:* capstone `...1054` deps + grant commands byte-identical to pre-edit
   (diff those specific lines).
9. **Apply the A/B toggle to `...3002/3004/3005`.**
   *Verify:* if B, those ids absent from chapter + lang; if A, present as leaf
   nodes not upstream of `...102C` or Great Hunt.
10. **Lang pass:** delete orphaned keys, refresh retargeted keys to `[STUB]`,
    add three NEW keys with `[BRIEF]` (§4). Bare-LF only.
    *Verify:* every remaining `quest.<id>.*` in en_us.snbt maps to a live grove
    node; every live node has three keys; no `[STUB]` left on a KEEP node.
11. **Line-ending + integrity re-check.**
    *Verify:* grove file CRLF count unchanged (all `\r\n`, 0 bare LF); en_us.snbt
    all bare LF; `SkillsLevel`/`PlayerSpells` blocks intact on every task.

---

## 7. VERIFICATION CHECKLIST (final, before handing to Opus/human)

- [ ] **Age/tier audit.** Every item/entity in the reworked chapter is legal at
      `medieval_times`. mowziesmobs / born_in_chaos / monsterplus / alchemists_garden
      / crittersandcompanions are overworld Medieval-fauna mods with NO AStages item
      locks pushing them later (re-confirm: `grep -rn "mowziesmobs\|born_in_chaos\|monsterplus" kubejs/server_scripts/aoa_astages_*.js` → expect no later-age lock). No later-tier tech introduced.
- [ ] **Dependency graph.** Rebuild the node→deps map with the §1.2 parser; assert
      (a) no dep points at a deleted id, (b) every non-root node reaches a metallurgy
      gate (`097AED7C91033D5E` or `2902E58DB70F9442`) transitively, (c) capstone
      reachable, (d) no cycle.
- [ ] **Capstone grant unchanged.** `6D7E8F901A2B1054` id, its four deps, `minreq 3`,
      and the three commands (`/advancement grant {p} only aoa:journey/grove_trials`,
      `/astages add {p} the_renaissance true true`,
      `/advancement grant {p} only aoa:age/the_renaissance`) are byte-identical to the
      pre-edit file. It remains the pack's sole `the_renaissance` grant.
- [ ] **Journey mirror unaffected.** Run `python .aoa_reveal_audit/verify_j2a.py`;
      it extracts stage-granting nodes and checks the J2A `check_quest` mirror
      (`journey_to_ascension.snbt:87 targets:["6D7E8F901A2B1054"]`). Expect PASS
      (capstone id + grant preserved → mirror still resolves).
- [ ] **Crossing check.** Plot the final node coords on the 0.5 grid; confirm the
      three lanes (Mowzies x≈1–6 left; Monster Plus x≈8–14 top y-neg; Born in Chaos
      x≈8–18 middle) and the Great Hunt column (x≈17–22) do not cross dependency
      lines. Lanes are vertically separated by construction; re-verify after any
      coord nudge. Manual — the pack has no automated crossing tool.
- [ ] **Item-id proofs re-run.** Re-grep every item/entity id placed against the
      jar lang (§0/§2 proof commands) — no hallucinated id survives.
- [ ] **Duplicate-id scan.** Anchored `grep -P '^\s+id: "'` in the grove file →
      no duplicate quest/task/reward ids (loose `id:` false-positives on
      `autofocus_id:` — do not use it).
- [ ] **Line endings.** Grove file 100% CRLF (Python byte count); en_us.snbt 100%
      bare LF. `SkillsLevel` block present on every task (`check:0b`).
- [ ] **No leftover offending kills.** `grep 'type: "kill"'` in grove → only
      mowziesmobs (headliners + Great Hunt + elokosa_howler) + alchemists_garden
      (+ 3 BiC nodes iff Variant A). Zero rank-and-file born_in_chaos/monsterplus
      kills.
- [ ] **Prose separation.** No player-facing text added to the `.snbt`; all prose
      lives as `[STUB]`/`[BRIEF]` in en_us.snbt for Opus.

---

## 8. ASSUMPTIONS / OPEN ITEMS FOR THE EXECUTOR

- The `min_required_dependencies` field must be dropped (not set to 1) on nodes
  that go from a 2-dep alt-gate to a single dep, matching FTBQ convention seen in
  the file. Confirm against a live single-dep node before mass-applying.
- `choice` task type: verified live-usable per pack memory (More Quest Types).
  If a `choice` node proves fiddly, use `ftbfiltersystem:smart_filter` with an
  `or(...)` expression instead (pattern proven in `...101B`).
- Monster Plus `ancient_hero` retarget item: if no clean drop exists, DELETE the
  node and rely on the re-pointed Great Hunt fan-in (§3.5) rather than inventing a
  drop. Do not fabricate an item id.
- Curio prune (`spear`/`bluff_rod`/`glowing_jelly`) is discretionary; default is
  KEEP if the Mowzies lane looks thin after deletions, DELETE if it reads as
  filler. Either way they are safe leaves.
