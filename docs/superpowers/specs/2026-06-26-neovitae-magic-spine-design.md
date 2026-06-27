# Design — Neo Vitae as the AoA Magic Spine (Forbidden & Arcanus demoted + maximally cross-woven)

**Date:** 2026-06-26
**Status:** DESIGN — approved in brainstorming; pre-implementation. Next step: implementation plan (writing-plans).
**Branch context:** quest-prose-cc1-cc2
**Supersedes:** the unverified assumptions in `AoA_FnA_Demotion_NeoVitae_Spine_Plan_2026-06-26.md` (that doc was wiki-derived; this spec is jar-verified and reflects three user decisions + a node-level quest audit + cited sentiment).

Every Neo Vitae and Forbidden & Arcanus ID in this document was confirmed present in the installed jars by an adversarial verification pass (verdict: PASS-WITH-CORRECTIONS — zero invented item/block IDs across ~187 `neovitae:*` + 41 `forbidden_arcanus:*` IDs). Where an ID still needs a final in-game confirmation it is flagged `[verify in-game]`.

---

## 0. Decision summary

User decisions locked 2026-06-26:

1. **Spine span:** Neo Vitae is a **required, stage-proof-bearing magic spine through Renaissance → Industrial → Gilded** (three ages). In **Atomic and Otherworldly** the NV content is **optional-depth quests folded into those ages' existing required chapters** — never a standalone or optional chapter, and **never grants the atomic stage** (the atomic stage stays the single authorization convergence per canon).
2. **F&A pain points:** **Patch both** — neutralize the Black Hole item-deletion hazard, and make Soul Looting deterministic. (Both are confirmed *not* config-toggleable in 2.6.1; both require datapack intervention.)
3. **F&A retention:** **Maximal cross-weave** — keep the liked F&A pieces as optional, unlocked content *and* invest heavily in cross-mod weaves so F&A and Neo Vitae fuse rather than sit adjacent.

Hard canon constraints honored throughout: **no optional whole-chapters**; required chapters with optional *depth* (never N-of-M); capstones grant stages via command reward on a **real item/advancement task** (no checkmark tasks); no vanilla/bare-ingot quest tasks; Renaissance is the magic-entry age (no blood magic in Medieval); every age stage grant fans in all current-age domain proofs; magic never directly grants the atomic stage.

---

## 1. Verified ground truth

### 1.1 Installed jars + dependencies
- `mods/neovitae-1.21.1-1.0.25.jar` (mod id `neovitae`) — NeoForge Blood Magic successor. Deps present: `geckolib`, `modonomicon`.
- `mods/forbidden_arcanus-2.6.1.jar` (mod id `forbidden_arcanus`).
- Weave partner mods present: `malum-1.21.1-1.8.2`, `occultism-1.21.1-neoforge-1.223.0`, `theurgy-1.21.1-neoforge-1.73.1`, `spectrum-1.11.8-1.21.1-neo`.
- **Neo Vitae has NO on-disk integration yet** — no `config/neovitae`, no `data/neovitae` overlay, and **zero AStages references** anywhere in `kubejs/` or `config/ftbquests/`. The spine is greenfield and currently world-entry-open.

### 1.2 Neo Vitae registry — key verified IDs
- **Orbs of Vitae** (registry `blood_orb_<rank>`, display = Latin): `blood_orb_weak` (Novicius, 5k anima, tier 0), `blood_orb_apprentice` (Discipulus, 25k, t1), `blood_orb_magician` (Veneficus, 150k, t2), `blood_orb_master` (Magus, 1M, t3), `blood_orb_archmage` (Dominus, 5M, t4), `blood_orb_transcendent` (Divinus, 10M, t5).
- **Altar + economy:** `ara_vitae` (the altar), `incense_altar`, `alchemy_array` (block), `athanor` (block), `tabula_vitae` (block), `hellfire_forge` (block), `vas_maleficum`, `spira_infernalis`, `crystallarium_maleficum`, `spirit_cache`.
- **Runes:** `rune_blank/speed/efficiency/sacrifice/sacrifice_self/capacity/capacity_augmented/orb/acceleration/charging/dislocation` and reinforced `rune_2_*` equivalents.
- **Sigils (stat-bearing):** `sigil_air/water/lava/void/blood_light/divination/seer/fast_miner/frost/green_grove/holding/magnetism/suppression/teleposition` (+ `sigil_phantom_bridge/bound_treasures/damned/necromancy`).
- **Sentient gear:** `sentient_sword/axe/pickaxe/shovel/scythe/helmet/plate/leggings/boots`, `training_bracelet`.
- **Demonite → Hellforged chain:** `dungeon_ore` (Demonite Ore), `raw_demonite`, `demonite_fragment`, `demonite_gravel`, `demonite_trim_ingot` (Hellforged Trim Ingot), `ingot_hellforged`, `hellforged_dust`, `hellforged_parts`, `hellforged_resonator`, `hellforged_explosive_cell`, `hellforged_block`. (`prismatic_demonite` exists but is code/feature-driven — lang-only.)
- **Blood shards / stone:** `weak_blood_shard` (the **only** shard rank — no `strong_blood_shard`), `blood_pearl`, `bloodstone`, `bloodstone_brick`, `blood_tank`, `blood_battery`, `blood_stained_glass(_pane)`.
- **Dungeon keys / access:** `simple_key`, `standard_key`, `mine_key`, `mine_entrance_key`, `boss_key` (boss-drop), `teleposer` + `teleposer_focus`/`reinforced_teleposer_focus`/`enhanced_teleposer_focus`. Dimension id `neovitae:dungeon`.
- **Spiritus (demon-will):** gems `spiritus_gem_petty/lesser/common/greater/grand`; shards `spiritus_{ruina,nihilum,invictus,vindicta}_shard`; essences `base_spiritus_soul_raw` + `..._{ruina,nihilum,invictus,vindicta}`; catalysts `spiritus_*_catalyst`; `raw_spiritus`, `crystal_cluster`, `raw_crystal_shard`.
- **Reagents / residue:** `reagent_*` family (sigil crafting), `corrupted_dust`, `ectoplasmic_residue`, `tau_oil`, `lava_crystal`. **`arcane_ash` does NOT exist** (it was invented in the old plan).
- **Ritual stones:** `ritual_stone`, `master_ritual_stone`, `inverted_master_ritual_stone`, `imperfect_ritual_stone`, elemental `*_ritual_stone`, scribe tools `*_scribe_tool`, `ritual_diviner(_dusk)`, `ritual_designer`, `ritual_reader`.

### 1.3 Neo Vitae recipe + data-map schemas (the customization surface)
All recipes are JSON under `data/neovitae/recipe/**`. NeoForge ingredient syntax (`{"item":...}` / `{"tag":...}` / `{"fluid":...}`); outputs use 1.21 stack form `{"count":N,"id":"ns:item"}`. Verified recipe types (corrected from the old plan's guesses):

| Type | Purpose | Key fields |
|---|---|---|
| `neovitae:ara_vitae_recipe` | Blood Altar infusion / orbs | `bloodNeeded`(int), `craftSpeed`, `drainSpeed`, `input`, `minTier`(0–5), `output`, opt `copyInputComponents` |
| `neovitae:hellfire_forge` | Soul forge standard craft | `inputs[]`(≤4), `drain`(float), `minDrain`(float), `output`, opt `spiritusType`(raw/ruina/nihilum/invictus/vindicta) |
| `neovitae:hellfire_forge_transform` | Transform item (Sentient gear) | `transformInput`, `catalysts[]`, `output`, `drain`, `minDrain` |
| `neovitae:hellfire_forge_upgrade` | Upgrade inserted item in place | `catalysts[]`, `drain`, `minDrain` (NO output) |
| `neovitae:hellfire_forge_spiritus_infusion` | Fill spiritus gems | `gemInput`(tag `neovitae:spiritus_gems`), `drain`, `minDrain` |
| `neovitae:athanor` | Tool-gated processing | `inputs[]`, `tool`(tag `neovitae:athanor_tool/*`), `guaranteed_outputs[]`, `chance_outputs[]`, opt `input_fluid`/`output_fluid`/`spiritus_costs`/`spiritus_boost` |
| `neovitae:alchemytable` | Alchemy Table | `input[]`(≤6), `output`, `syphon`(int LP), `ticks`, `upgradeLevel` |
| `neovitae:array` | In-world Alchemy Array | `baseinput`, `addedinput`, `texture`(req), then `output` OR `effect_type`, opt `ev_cost` |
| `neovitae:meteor` | Meteor ritual | `input`, `syphon`, `explosion`, `layers[]` |
| `neovitae:sentient_downgrade` | Living downgrade | `input`, `sentient_upgrade`(registry id) |
| `neovitae:flask_*` | Alchemy Flask effects | `flask_effect/effect_transform/length/potency/fill/cycle/item_transform` — each `input[]`, `syphon`, `ticks`, `upgradeLevel` + type-specific |
| `neovitae:fluid_tiered` | Tiered tank | shaped `pattern` + `primary`/`secondary` |

**Field-name gotchas:** the array uses `baseinput`/`addedinput` (no underscore) and **requires** a `texture` path. The bare strings `ara_vitae`, `alchemy_array`, `tabula_vitae`, `flask`, `living_downgrade` are **NOT recipe types** (they are block IDs or were invented) — use the `_recipe`/`array`/`sentient_downgrade`/`flask_*` forms above.

**Data maps** (`data/neovitae/data_maps/**`, NeoForge `{"values":{...}}`):
- `item/blood_orb_stats.json`: per orb `animaCapacity`, `fillRate`, `fluidCapacity`, `tier`.
- `item/sigil_stats.json`: per sigil `lp_cost` (+ opt `range`/`vertical_range`/`effect_duration`/`effect_level`).
- `item/spiritus_gem_max.json`: scalar float per gem (max will capacity).
- `neovitae/ritual/ritual_stats.json`: per ritual `activation_cost`, `refresh_cost`, opt `refresh_time`/`crystal_level`/`ambient_sound`. **Caveat:** the two dungeon-access rituals `neovitae:simple_dungeon` and `neovitae:standard_dungeon` are **absent** from this map — their tier is Java-hardcoded and **cannot** be retuned via datapack.

### 1.4 Altar tiers, capstone tags, and the empty-pillars gotcha
Tiers are a custom registry: `data/neovitae/neovitae/altar_tier/{weak,apprentice,mage,master,archmage,transcendent}.json`. Each lists `components[]` with `pos`, `valid` (block id or `#block-tag`), `upgrade`. Capstones/runes/pillars resolve against **block tags**:

```
#neovitae:altar/t3_capstones = [ neovitae:blood_stained_glass ]
#neovitae:altar/t4_capstones = [ neovitae:bloodstone, neovitae:bloodstone_brick ]
#neovitae:altar/t5_capstones = [ neovitae:hellforged_block ]
#neovitae:altar/t6_capstones = [ neovitae:crystal_cluster, neovitae:crystal_cluster_brick ]
#neovitae:altar/runes        = [ rune_*, rune_2_* ]
#neovitae:altar/pillars      = [ ]   ← EMPTY (ships {"values":[]})
```

Tier component counts: weak(0)=altar only; apprentice(1)=8 runes; mage(2)=24 runes+8 pillars+4×t3cap; master(3)=52 runes+8 pillars+4×t3+4×t4; archmage(4)=100 runes+8 pillars+caps; transcendent(5)=172 runes+36 pillars+caps.

**The `#neovitae:altar/pillars` tag ships EMPTY while tier-2+ altars reference 8–36 pillar slots.** If pillars are structurally required and not code-injected, **no orb above apprentice and no dungeon-access ritual is buildable** — a hard wall independent of staging. **This must be validated in-game (F6).** Resolution in §4.

### 1.5 Forbidden & Arcanus 2.6.1 facts
- All 41 quest-referenced F&A IDs confirmed present (incl. `hephaestus_forge_tier_1/2/3`, `deorum_*`, `clibano_core`, soul line, `eternal_stella`).
- **Hephaestus Forge has NO datapack recipe type** — its enhancing logic is entirely code-side. F&A's only data-driven custom recipe types are `forbidden_arcanus:clibano_combustion` and `forbidden_arcanus:apply_modifier` (smithing-table). `apply_modifier` recipes have **no base/target slot** (the target is code-determined), so you cannot JSON-target which items a modifier applies to. **Any "F&A forge does X to mod-Y item" weave is impossible via datapack** — route through the consuming mod's own machine instead.
- `upgrade_tier_3.json` ritual consumes 4× `arcane_crystal` + 4× `deorum_ingot` on a chiseled-polished-darkstone core (only matters if the Forge stays on a required path — it will not).
- **Config surface is tiny** (boom_arrow / stella_arcanum explosion + edelwood_ladder speed + mundabitur creeper-charge). **No config toggle exists for the Black Hole, Soul Looting, or Aureal systems** — all are datapack-gated (recipes/enchantment JSON/tags/loot).
- Black Hole mechanic: a dropped `dark_matter` item entity near a `corrupti_dust` item entity (with air at its position) consumes 1 corrupti_dust and places an invisible `forbidden_arcanus:black_hole` block that vacuums/voids items, mobs, and XP (petrifying XP into `xpetrified_orb`). `corrupti_dust` = shapeless craft (obsidiansteel_ingot + blaze_powder + nether_wart + arcane_crystal_dust + ender_pearl_fragment → 4).
- Soul Looting: enchantment (`data/forbidden_arcanus/enchantment/soul_looting.json`, max_level 3, on `#minecraft:enchantable/sword`) adding +5/10/15% Lost-Soul spawn chance on kills. Uncraftable; obtained only via enchanting/loot/trades (the cited RNG gate).

### 1.6 Cited community sentiment (verification of the old plan's claims)
- **CONFIRMED — pain points are the Black Hole + Soul Looting:** Black Hole has primary GitHub rage (#406 — accidental loss of "several double-chests"/"months of inventory", asking it not be accident-triggerable; #441 — even the intended `xpetrified_orb` vanishes on reload). Soul Looting is the cited early bottleneck (uncraftable, RNG, "completely blocks" progression if skipped). ATM-10 reports show recurring soul-acquisition frustration.
- **PARTIAL — "1.16 deciphering-RNG removed in 2.x":** there is no deciphering/research-table RNG in 2.x (confirmed), but no source substantiates that such a "divisive 1.16 research table" ever existed (likely a conflation; the modern research system is still `[Developing]`).
- **PARTIAL — liked: Forge endgame, Clibano, trinkets, aesthetics:** directionally confirmed and consistent across every source, but evidence is wikis/guides/store-copy/GitHub, **not first-person player voice** (Reddit was inaccessible to the crawler).
- Neo Vitae itself: a Blood Magic rewrite, modest adoption (~6k–151k downloads), **no substantive community reception found** — design on mechanics, not on reputation.

### 1.7 Available FTBQ quest types (bytecode-verified, install-gated)
- **Live & usable bare (`ftbquests` ns):** `item, custom, kill, kill_advanced, advancement, observation, biome, dimension, structure, location, stat, gamestage, fluid, forge_energy, xp, item_advanced, place_block, break_block, use_block, hold_item, find_entity, interact_entity, tame_mob, attributes, damage, receive_damage, check_quest, potion_effect, trading, timer, command, fishing_catch` + `cast_spell`/`spell_equipped` (spell_engine — installed) + `skills_level` (puffish_skills — installed).
- **NOT available (deps absent — do NOT author):** `dialogue` (needs blabber), `pay` (needs sg_economy), `origin`, `levelz`, `reskillable`, `easynpc_dialogue`. This **corrects** the prior memory note that listed `dialogue` as available.
- `checkmark` exists but is **forbidden by canon** for progression tasks.
- ExtraQuests `key_value` task/reward needs the `extraquests:` prefix (not bare).
- `certain_questing_additions` registers no types (visual only).

### 1.8 Adversarial ID verdict
PASS-WITH-CORRECTIONS. All item/block IDs real; the only defects were 5 recipe-*type* string slips already corrected in §1.3. Net: no invented mod IDs will ship if the §1.3 type names and the §5/§6 IDs are used as written.

---

## 2. Chapter architecture (corrected — zero optional chapters, zero new chapters)

The spine **rewires three existing required magic chapters** and **adds optional-depth quests to the Atomic/OW ages' existing required chapters**. No chapter is optional; no new chapter is created.

| Age | Home chapter (exists, required) | NV role | Stage behavior |
|---|---|---|---|
| **Renaissance** | `ren_magic_foundations` | Required proof — Ara Vitae → orbs/runes/sigils → Hellfire Forge → Spiritus → **Athanor capstone** | Capstone node `0B03101000000039` keeps `/astages add ren_magic_foundations_complete` + its J2A mirror |
| **Industrial** | `ir_magic_feedstock_and_spectrum_network` | Required proof — Demonite→Hellforged; **Hellforged Block feeds the oritech Foundry** | Bridge is a required dep of IR capstone `49540B1000000015` (`ir_magic_feedstock_complete`) |
| **Gilded** | `g1_the_golden_workshop` | Required proof — archmage altar / hellfire-tier machines wing | Chapter root `4757011020010001` (rewired to the Athanor) gates the Gilded golden-workshop chapter |
| **Atomic** | the age's existing required chapter(s) | **Optional depth** — transcendent altar, demon-realm dungeon, Divinus orb, Sentient endgame, the Foreman | NV quests are optional depth; **never** run `/astages` for atomic; the NV atomic proof MAY be one fan-in lane of the authorization convergence but is not the sole/direct granter |
| **Otherworldly** | the age's existing required chapter(s) | **Optional depth** — full Spiritus economy, maxed Sentient gear, optional Ascension-convergence flavor | flavor only; command-reward on a real NV apex item, never a checkmark |

Renaissance side-chapters also touched (rewired in place, structure preserved): `ren_nether_threshold` (deorum→hellforged metal lane), `ren_observation_experimentation` (one optional soul leaf). `journey_to_ascension` F&A references are **icon-only** on `check_quest` stage-mirrors — KEEP (optionally retheme the cosmetic icon).

---

## 3. AStages gating plan (NV currently has zero locks)

The natural diamond gate floors the whole spine at Renaissance for free (the tier-0 orb requires `c:gems/diamond`, Renaissance-locked), so there is **no current HARDLOCK** — but the spine is wide-open to sequence-breaking. Required locks:

1. **F1 (highest priority) — lock the dungeon dimension.** Add `["industrial_revolution", "neovitae:dungeon"]` to `dimensionLocks` in `kubejs/server_scripts/aoa_astages_03_dimension_restrictions.js` with `.setBidirectional(false)` (mirrors `macabre:the_pit`). This transitively gates demonite, all Hellforged items, mine keys, and the Foreman.
2. **F2 — add an NV item-lock table to `kubejs/server_scripts/aoa_astages_01m_magic.js`** using the existing `softItemLock`/`block_item` convention:
   - **Renaissance:** `ara_vitae`, `incense_altar`, `alchemy_array`, `athanor`, `tabula_vitae`, the rune set (`rune_blank/speed/efficiency/sacrifice/sacrifice_self/capacity/orb/dislocation`), `reagent_*`, basic `sigil_*`, `ritual_stone`, `master_ritual_stone`, `*_scribe_tool`, `ritual_diviner`, `blood_orb_weak`, `blood_orb_apprentice`, `weak_blood_shard`, `blood_pearl`, `bloodstone`, `bloodstone_brick`, `blood_stained_glass(_pane)`, `blood_tank`, `blood_battery`.
   - **Industrial:** `hellfire_forge`, `vas_maleficum`, `spira_infernalis`, `crystallarium_maleficum`, `spirit_cache`, `spiritus_gem_petty/lesser/common/greater/grand`, spiritus shards/essences/catalysts, routing nodes (`input/output/master_routing_node`, `routing_conduit`), `rune_2_*`, `teleposer(_focus)`, `tabula_robur/animata/spiritus`, `activation_crystal_weak`.
   - **Gilded:** `blood_orb_magician`, `blood_orb_master`, Sentient gear set + `training_bracelet`, Hellforged chain (`ingot_hellforged`, `hellforged_dust/parts/resonator/block`, `demonite_trim_ingot`), `enhanced_teleposer_focus`, `inverted_master_ritual_stone`, `blood_orb_archmage`.
   - **Atomic:** `blood_orb_transcendent`, `hellforged_explosive_cell`, `sanguine_reverter`, deep-dungeon reagents (`blight_marrow/whetstone`, `cinder_heart_fragment`, `frozen_marrow_shard`, `gore_clotted_fang`).
3. **F8/F9 (defense-in-depth) — tag/block-item locks:** add `c:raw_materials/hellforged`, `c:dusts/hellforged`, `c:fragments/hellforged`, `c:gravels/hellforged`, `c:ingots/hellforged` to a Gilded `softTagLock` in `aoa_astages_06_ore_restrictions.js`; lock capstone block-items `hellforged_block`/`bloodstone*` (Gilded), `crystal_cluster*` (Atomic), `blood_stained_glass` (Renaissance) so the altar-tier gate is enforced, not merely emergent.
4. **Do NOT invent an Otherworldly NV gate** — NV has no natural OW apparatus; OW's magic capstone is already `occultism:iesnium_anvil`. The required spine completes at Gilded; Atomic/OW are optional depth.
5. **Materials note (F7):** `/neovitae generate-materials` is single-player/integrated-only and relaunch-gated; defaults (iron/gold/copper/coal/demonite/hellforged) ship pre-registered. **Never make an AoA quest/recipe depend on a newly-absorbed (non-default) NV material.**

---

## 4. Pillars resolution (F6) — and it doubles as the flagship weave

**Step 1 (validation):** in-game, confirm whether a tier-2 altar validates with the empty `#neovitae:altar/pillars` tag. If it does, no fix needed. If it does not (expected), proceed.

**Step 2 (fix + fusion):** populate `#neovitae:altar/pillars` via a datapack tag at `kubejs/data/neovitae/tags/block/altar/pillars.json`, filling it with **cross-mod pillar blocks** so growing the altar *requires integrating the other magic mods* — the most aggressive realization of "maximal cross-weave." Candidate members (all `[verify in-game]` craftable at the relevant age): an F&A `forbidden_arcanus:polished_darkstone_pillar`/`runic_darkstone`, a Malum block, a Spectrum gem block, plus a plain NV fallback so the altar is always buildable without a hard third-mod dependency at the lowest tier. Keep a block-tag/item-tag pair in sync for JEI.

> This is a pack-data fix, not an AStages fix. If validation shows pillars are code-injected, drop Step 2 and only use the cross-mod blocks as an *optional* capstone weave (§6 W1/NV5).

---

## 5. F&A rewire — full node-by-node table

**Rule:** load-bearing nodes are **REWIRED** (keep node id + dependency edges + command rewards + J2A mirrors; swap only the task item/type). Non-load-bearing nodes are **REPLACE** (swap task). Two Medieval edelwood nodes are **DELETE**. Preserve CRLF/SNBT formatting on every edit. Quest *text* lives in `config/ftbquests/quests/lang/en_us.snbt` (keyed) — retitle/retheme there, not inline.

### `ren_magic_foundations` (Renaissance required spine)
| Node | Was | → Replacement | Type | Notes |
|---|---|---|---|---|
| `0B03101000000030` | arcane_crystal_dust | `neovitae:weak_blood_shard` | item | first sacrifice reagent |
| `0B03101000000031` | arcane_crystal_dust_speck | `neovitae:blood_orb_weak` | item | Novicius orb |
| `0B03101000000032` | elementarium | `neovitae:ara_vitae` | **interact_block** | build the altar |
| `0B03101000000033` | rune | `neovitae:rune_blank` | item | first altar rune |
| `0B03101000000034` | aureal_bottle | `neovitae:blood_orb_apprentice` | item | Discipulus orb |
| `0B03101000000035` | obsidian_skull *(opt)* | `neovitae:sigil_divination` | item | first sigil (lp 0) |
| `0B03101000000036` | arcane_crystal | `neovitae:weak_blood_shard` | item | forge feedstock |
| `0B03101000000037` | darkstone_pedestal | `neovitae:hellfire_forge` | **interact_block** | build the forge |
| `0B03101000000038` | clibano_core | `neovitae:spiritus_gem_petty` | item | first demon-will |
| **`0B03101000000039`** | arcane_bone_meal **(CAPSTONE)** | `neovitae:athanor` | item | **REWIRE** — keep `/astages add ren_magic_foundations_complete` + J2A mirror `5350010000020002`. (May use `use_block`/`interact_block` to prove the build; `item` preserves the existing shape with zero J2A breakage.) |
| `0B0310100000003D` | arcane_crystal_obelisk *(opt)* | `neovitae:incense_altar` | item | **preserve id** — dep root of `ren_nether_threshold` entry |
| `0B03101000000070` | artisan_relic *(opt soul lane head)* | `neovitae:spiritus_gem_lesser` | item | re-theme column = Spiritus deep-dive |
| `0B03101000000071` | corrupted_arcane_crystal *(opt)* | `neovitae:raw_spiritus` | item | |
| `0B03101000000072` | corrupti_dust *(opt)* | `neovitae:corrupted_dust` | item | 1:1 residue |
| `0B03101000000073` | soul *(opt)* | `neovitae:base_spiritus_soul_raw` | item | |
| `0B03101000000074` | enchanted_soul *(opt)* | `neovitae:spiritus_ruina_shard` | item | |
| `0B03101000000075` | soul_binding_crystal *(opt)* | `neovitae:spiritus_gem_common` | item | |
| `0B03101000000076` | blood_test_tube *(opt)* | `neovitae:blood_pearl` | item | |
| `0B03101000000077` | soul_extractor *(opt tail)* | `neovitae:incense_altar` | interact_block | |

### `ren_nether_threshold` (deorum→hellforged metal lane; this lane does NOT feed the chapter capstone `…062` create:blaze_burner)
| Node | Was | → Replacement | Type | Notes |
|---|---|---|---|---|
| `0B03102000000040` | hephaestus_forge_tier_1 | `neovitae:rune_speed` | item | **preserve id** (041 depends) |
| `0B03102000000041` | mundabitur_dust | `neovitae:hellforged_dust` | item | **preserve id** (042 depends) |
| `0B03102000000042` | deorum_ingot | `neovitae:ingot_hellforged` | item | **preserve id** (046/080 depend) |
| `0B03102000000046` | deorum_nugget | `neovitae:hellforged_parts` | item | **preserve id** (047 depends) |
| `0B03102000000047` | gilded_chiseled_polished_darkstone | `neovitae:hellforged_block` | item | leaf |
| `0B03102000000080` | xpetrified_orb *(opt)* | `neovitae:blood_pearl` | item | |
| `0B03102000000081` | stellarite_piece *(opt leaf)* | `neovitae:spiritus_gem_petty` | item | |

### `ir_magic_feedstock_and_spectrum_network` (Industrial required proof — the magic→industry bridge)
| Node | Was | → Replacement | Type | Notes |
|---|---|---|---|---|
| **`49540B1000000004`** | hephaestus_forge_tier_2 *(Aureal Foundry anchor)* | `neovitae:hellfire_forge` | **interact_block** | **REWIRE** — load-bearing; keep edges |
| **`49540B1000000018`** | deorum_block *(feedstock into oritech)* | `neovitae:hellforged_block` | item | **REWIRE** — load-bearing; re-point the oritech foundry recipe (see below); preserve id so `…0005` edge + capstone `…0015` fan-in survive |
| `49540B1000000019` | aureal_tank | `neovitae:blood_tank` | item | support |
| `49540B100000001A` | smelter_prism | `neovitae:hellforged_resonator` | item | support |
| `49540B100000001B` | tyr_helmet *(opt gear)* | `neovitae:sentient_helmet` | item | |
| `49540B100000001C` | tyr_chestplate *(opt gear)* | `neovitae:sentient_plate` | item | |
| `49540B100000001D` | tyr_leggings *(opt gear)* | `neovitae:sentient_leggings` | item | |
| `49540B100000001E` | tyr_boots *(opt gear)* | `neovitae:sentient_boots` | item | |

### `g1_the_golden_workshop` (Gilded required proof)
| Node | Was | → Replacement | Type | Notes |
|---|---|---|---|---|
| **`4757011020010001`** | hephaestus_forge_tier_3 *(chapter ROOT + icon)* | `neovitae:athanor` | **use_block** | **REWIRE** — keep node id, root position, use_block type, all 6 child edges; update chapter icon. (Alt block: `neovitae:vas_maleficum`.) |

### `metallurgy` (Medieval — DELETE)
| Node | Was | Action |
|---|---|---|
| `2902E58DB70F95F1` | edelwood_log | **DELETE** (no Medieval NV analog; canon: no blood magic in Medieval) |
| `2902E58DB70F95F2` | edelwood_oil | **DELETE** (leaf of above) |

### `ren_observation_experimentation`
| Node | Was | → Replacement | Type |
|---|---|---|---|
| `0B031080000000C2` | corrupt_soul *(opt leaf)* | `neovitae:base_spiritus_soul_raw` | item |

### `journey_to_ascension` — KEEP (icon-only)
`5350010000020003` (mirrors create:blaze_burner `…062`) and `5350010000020002` (mirrors ren capstone `…039`) reference F&A IDs only as **node icons**, not tasks. KEEP; optionally retheme the cosmetic icon to a Create/NV icon.

### Oritech foundry recipe re-source (KubeJS side of node `…0018`)
Re-point the two recipes that hard-require `forbidden_arcanus:deorum_ingot` — `aoa:ir_magic_feedstock/aureal_foundry` in `kubejs/server_scripts/ir_native_capstone_recipes.js` and `aoa:magic_spine/oritech_machine_core_5` in `kubejs/server_scripts/magic_spine_bridges.js` — to accept a new **`#aoa:magic_feedstock`** item tag whose members are `neovitae:hellforged_block`/`neovitae:ingot_hellforged` **and** `forbidden_arcanus:deorum_ingot` (deorum kept as an optional alternate so F&A players retain a use). Most future-proof; preserves the IR proof chain.

---

## 6. Cross-mod weave catalog (maximal; all on verified schemas/IDs)

**Hygiene (mandatory):** any weave whose output already has a native NV recipe (orbs, `simple_key`, `mine_entrance_key`, `sentient_*` transforms, etc.) must `event.remove` the native recipe first and re-add the single woven route — additive duplicates are bypasses. Tag-membership weaves are JSON tag files under `kubejs/data/<ns>/tags/...`, with the item-tag mirror kept in sync for JEI.

**Validated from the old plan (corrected):**
- **W1 — Soulbound Capstone (Malum→altar):** add `malum:block_of_soulstone` to `#neovitae:altar/t3_capstones` (block tag; mirror the item tag). *Adds an accepted alternative capstone — cannot be made "required" since the vanilla `blood_stained_glass` still works.* No softlock/bypass. **VALID (as an option).**
- **W6 — ritual_stats retune:** overlay `data/neovitae/data_maps/neovitae/ritual/ritual_stats.json` to age-pace the ~31 data-mapped rituals (bump `activation_cost`/`crystal_level`). **VALID.** Cannot retune the two dungeon rituals (Java-hardcoded).
- **DEAD — W2 (Theurgy "mercury" Athanor fluid):** `theurgy:mercury` is not a fluid (only `sal_ammoniac`); mercury exists only as items. Drop or convert to a solid-input weave (see NV2).
- **DEAD — W5 (F&A Hephaestus Forge applies eternal_stella):** F&A forge has no datapack recipe type; `apply_modifier` has no target slot. Replaced by NV4.

**New corrected weaves (the maximal-fusion set):**
- **NV1 — Spirit-Fed Sentient Forge (Malum↔NV, Ren):** `event.remove` the native `neovitae:hellfire_forge_transform` for `sentient_axe`/`sentient_sword` and re-add with `catalysts:[{item:neovitae:spiritus_gem_petty},{item:malum:wicked_spirit}]` so Malum's spirit harvest feeds NV's Sentient awakening. *Verify `malum:wicked_spirit` is Renaissance-obtainable; if it needs the IR crucible, down-tier to an early Malum spirit.*
- **NV2 — Calcined Salt Catalyst (Theurgy↔NV, Ren):** `event.remove`+re-add one single-route `neovitae:hellfire_forge` reagent recipe with a Theurgy `alchemical_salt` in `inputs[]`. *Verify the exact salt registry id (may need a `c:` tag for per-source variants).*
- **NV3 — Otherworld Bloom Flask (Occultism↔NV, Ren):** add/re-add a `neovitae:alchemytable` recipe (keep `upgradeLevel` 0–1) consuming `occultism:otherworld_essence` → a vision/insight flask, linking Occultism's clairvoyance to NV brewing.
- **NV4 — Stellar Tempering (F&A↔NV apex, IR/Gilded):** the salvage of W5 — a `neovitae:hellfire_forge_upgrade` whose `catalysts` include `forbidden_arcanus:eternal_stella` (+ `neovitae:tabula_robur`), mutating an inserted Sentient tool in place via NV's *own* upgrade system. *Verify NV Sentient gear is a valid upgrade target; if NV upgrades aren't datapack-extensible, fall back to a `hellfire_forge` recipe consuming eternal_stella into an NV apex item.*
- **NV5 — Prismatic Altar Capstone (Spectrum↔NV, OW):** add a luminous Spectrum gem block to `#neovitae:altar/t6_capstones` (+ item mirror) — radiant Transcendent capstone. *Verify a real Spectrum block id.*
- **Pillars weave (§4):** populate `#neovitae:altar/pillars` with cross-mod pillar blocks — the structural fusion lever.
- **deorum↔hellforged bridge (§5):** the `#aoa:magic_feedstock` tag uniting both metals into the oritech foundry recipe.
- **Clibano→Athanor companion:** keep the liked Clibano relevant by making its residue/output a valid Athanor input (or vice versa) so F&A's smelter feeds NV's processing — optional, unlocked, no progression gate.

---

## 7. F&A pain patches (both — datapack only)

- **Black Hole — neutralize the accident hazard.** It is independent of progression and the #1 documented complaint. Datapack-remove the `forbidden_arcanus:corrupti_dust` craft route (`kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js`, `event.remove({output:'forbidden_arcanus:corrupti_dust'})`) so a Black Hole cannot spawn by accident; preserve any *intended* `corrupti_dust` use by providing it only as a controlled quest/recipe output if needed. (If a fully-controlled black hole is desired later, gate `dark_matter` instead.) Verify nothing required depends on the removed route.
- **Soul Looting — make deterministic.** Provide a craftable enchanted book for `forbidden_arcanus:soul_looting` (KubeJS recipe or a quest-reward grant of the enchant) so the optional F&A soul lane is never RNG-walled. Tune the enchantment JSON if rebalancing the spawn chance.

Both patches live in/near the existing `kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js` + `soul_economy.js`. Re-run the gate audit after.

---

## 8. Quest authoring conventions

- Prefer **richer live types where the build matters**: `interact_block` (Ara Vitae, Hellfire Forge), `use_block` (g1 Athanor gateway), `observation` (Atomic dungeon-dimension entry), `check_quest` (capstone fan-in + J2A mirrors). Bare `item` elsewhere.
- **Forbidden:** `checkmark` tasks for progression; `dialogue`/`pay` (deps absent); vanilla `minecraft:` items; bare ingots/dusts/plates/decor/variants as quest tasks (quest a downstream item or drop it).
- Capstones grant stages via a **command reward** on a real item/advancement task; convergence fan-ins use `check_quest`.
- Quest text in `lang/en_us.snbt` (keyed); chapters carry structure only. Preserve per-file mixed CRLF/LF (detect via Python byte count, not grep).

---

## 9. Datapack capability matrix

**CAN do via datapack/KubeJS:** all NV recipes (every machine type in §1.3); altar capstone/rune/**pillar** membership (block tags); orb/sigil/spiritus/ritual tuning (data maps); F&A recipe add/remove (clibano_combustion, apply_modifier, vanilla); F&A enchantment JSON (soul_looting); AStages locks; FTBQ quests; Modonomicon book entries (NV book id `[verify in-game]`, likely `neovitae:scriptura_vitae`).

**CANNOT do via datapack (Java-locked — design around):** retune the two dungeon-access ritual tiers (`simple_dungeon`/`standard_dungeon`); make an altar capstone *required* (tags only add alternatives); target which items an F&A `apply_modifier` modifier applies to; new NV dungeon rooms (needs a one-line Java registration); register newly-absorbed NV materials on a dedicated server (SP/integrated + relaunch only).

---

## 10. Risks & validation gates

- **F6 (HIGH) — empty `#neovitae:altar/pillars`:** validate in-game before authoring tier-2+ content; if confirmed, §4 Step 2 is a prerequisite for the entire upper spine.
- **F7 (LOW) — material generation SP-only:** never depend on a non-default NV material.
- **NV release cadence:** pin `1.0.25`; re-verify schemas/data-maps on any bump (near-daily releases).
- **Single dungeon dimension:** Antechamber + Endless Realm share `neovitae:dungeon`; accept as one dimension (separating is Java).
- **Weave hygiene:** every native-recipe-targeting weave must remove-and-re-add (no additive bypass).
- **Final validation:** AStages gate audit + softlock/bypass pass + FTBQ node check (broken refs, unreachable, accidental skips) + JEI sanity + an in-game test-world run of the tier ladder Ren→Gilded.

---

## 11. Implementation phasing

- **P0 — Intake/verify:** in-game check of F6 (pillars) and the `[verify in-game]` IDs (NV Modonomicon book id, Spectrum/Malum block ids for weaves, `malum:wicked_spirit` Renaissance availability, `theurgy:alchemical_salt` id form). Capture default `materials.json`.
- **P1 — AStages staging:** §3 dimension lock + item-lock table + tag/capstone locks. Re-run gate audit.
- **P2 — F&A rewire + patches:** §5 node-by-node rewire/replace/delete (preserve ids/edges/J2A mirrors); §5 oritech foundry re-source via `#aoa:magic_feedstock`; §7 Black Hole + Soul Looting patches. Re-run softlock pass.
- **P3 — Quest authoring:** rebuild the three required chapters around the NV ladder; add Atomic/OW optional-depth quests to those ages' existing required chapters; retitle/retheme in `lang/en_us.snbt`.
- **P4 — Weaves:** §6 + §4 pillars weave (datapack JSON + KubeJS), with remove-and-re-add hygiene.
- **P5 — Lore/capstones:** Modonomicon (Scriptura Vitae) entries/overrides; capstone retags; Foreman boss-proof wiring (optional reward-gear only, no stage grant).
- **P6 — Verify:** full §10 validation suite.

---

## 12. Open items / `[verify in-game]` checklist

1. F6 — does a tier-2 altar validate with empty pillars? (gates P3/P4 upper tiers)
2. NV Modonomicon book id + entry JSON path (likely `neovitae:scriptura_vitae`).
3. Spectrum block id for NV5; Malum/F&A pillar block ids for §4; `malum:block_of_soulstone` craftability age for W1.
4. `malum:wicked_spirit` Renaissance obtainability for NV1 (down-tier if IR-gated).
5. `theurgy:alchemical_salt*` exact id form (bare vs `c:` tag) for NV2.
6. NV Sentient gear valid as a `hellfire_forge_upgrade` target for NV4 (else fall back).
7. Confirm nothing required depends on the removed `corrupti_dust` route before the Black Hole patch.
8. Default `config/neovitae/materials.json` contents (run `/neovitae generate-materials` on a test world).
