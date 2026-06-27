# Neo Vitae Magic Spine — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Neo Vitae the required AoA magic spine (Renaissance→Industrial→Gilded), demote Forbidden & Arcanus to optional + maximally cross-woven content, patch both F&A pain points, and keep every existing stage-grant / J2A mirror intact.

**Architecture:** Pure datapack + KubeJS + FTBQ-SNBT edits — no Java, no new mods. Three existing required magic chapters are rewired from F&A IDs to verified Neo Vitae IDs (node IDs/edges/command-rewards preserved). NV gets its first-ever AStages locks. F&A keeps its liked content unlocked and gains cross-mod weaves. Atomic/OW NV content is optional depth folded into those ages' existing required chapters (no new/optional chapters).

**Tech Stack:** NeoForge 1.21.1; FTB Quests 2101.1.27 (+more_quest_types/ExtraQuests); KubeJS (server_scripts + data); AStages 2.0.4; Neo Vitae 1.0.25; Forbidden & Arcanus 2.6.1. Validation: `python -m json.tool`, ripgrep, `.aoa_reveal_audit/verify_j2a.py`.

**Source of truth:** the design spec `docs/superpowers/specs/2026-06-26-neovitae-magic-spine-design.md` (committed `a16e308`). Section refs below (e.g. "spec §5") point there.

## Global Constraints

- **No invented IDs.** Every `neovitae:*` / `forbidden_arcanus:*` ID used here is jar-verified (spec §1). IDs flagged `[verify]` must be resolved in Task 0.1 before use; never ship a guessed ID.
- **No optional whole-chapters; no new chapters.** Required chapters with optional *depth* only. Atomic/OW NV content = optional-depth quests inside existing required chapters.
- **Magic never grants the atomic stage.** Atomic stays the single authorization-convergence grant. NV capstones may be a fan-in dependency but never run `/astages add` for atomic.
- **Preserve node IDs + dependency edges + command rewards + J2A mirrors** on every load-bearing rewire (spec §5). REWIRE, never delete, load-bearing nodes.
- **No checkmark/bare-staple/vanilla quest tasks.** Capstones grant via command reward on a real item/advancement task.
- **Quest TEXT lives in `config/ftbquests/quests/lang/en_us.snbt`** (keyed `quest.<id>.title/.quest_subtitle/.quest_desc`); chapters carry structure only.
- **Preserve per-file line endings.** FTBQ SNBT files have MIXED CRLF/LF per file — detect with a Python byte count (`raw.count(b'\r\n')` vs `b'\n'`) and preserve; do not let an editor normalize them.
- **Weave hygiene:** any weave whose output already has a native NV recipe must `event.remove(...)` the native route first, then re-add the single woven route (no additive bypass). Tag-membership weaves are JSON files with block-tag + item-tag mirrors kept in sync.
- **Pin Neo Vitae 1.0.25.** Re-verify schemas on any version bump.
- **Materials:** never depend on a non-default NV material (generation is SP/integrated-only + relaunch-gated). Default set: iron/gold/copper/coal/demonite/hellforged.

---

## Phase 0 — Resolve open IDs (gates Phases 4–5)

### Task 0.1: Resolve `[verify]` IDs by jar-cracking

**Files:**
- Create: `docs/superpowers/plans/nv-resolved-ids.md` (the resolved-ID ledger consumed by Tasks 4.1–4.3, 5.4)

**Interfaces:**
- Produces: confirmed IDs for `NV_MODONOMICON_BOOK`, `SPECTRUM_CAPSTONE_BLOCK` (a real Spectrum gem/storage block for t6), `MALUM_CAPSTONE_BLOCK` (`malum:block_of_soulstone` confirm + craft age), `PILLAR_BLOCKS` (1 F&A darkstone-pillar + 1 Malum + 1 Spectrum block + 1 plain NV fallback), `MALUM_SPIRIT` (a Renaissance-obtainable Malum spirit for NV1), `THEURGY_SALT` (exact `alchemical_salt` id or `c:` tag), `NV_SENTIENT_UPGRADE_OK` (bool: is NV Sentient gear a valid `hellfire_forge_upgrade` target).

- [ ] **Step 1: Crack the jars for each open ID.** Use python zipfile against `mods/neovitae-1.21.1-1.0.25.jar`, `mods/spectrum-1.11.8-1.21.1-neo.jar`, `mods/malum-1.21.1-1.8.2.jar`, `mods/theurgy-1.21.1-neoforge-1.73.1.jar`, `mods/forbidden_arcanus-2.6.1.jar`. For the Modonomicon book: list `data/neovitae/modonomicon/books/*`. For Spectrum/Malum/F&A pillar+capstone blocks: read each `assets/<mod>/lang/en_us.json` `block.*` keys and pick a thematically-right, craftable block. For `malum:wicked_spirit` / a Renaissance spirit: read malum recipes + `kubejs/server_scripts/aoa_astages_01m_magic.js` (malum staging) to confirm Renaissance obtainability; if IR-gated, pick an earlier spirit. For Theurgy salt: find the exact `alchemical_salt*` registry form. For NV Sentient upgrade target: inspect `data/neovitae/recipe/hellfire_forge/*upgrade*` + any `sentient`/`upgradeable` tag/registry to judge whether a custom `hellfire_forge_upgrade` can target Sentient gear (if undetermined, mark `NV_SENTIENT_UPGRADE_OK=UNKNOWN` → NV4 uses its fallback).

- [ ] **Step 2: Write the ledger.** Record each resolved ID with its jar evidence (file path inside the jar). Mark anything still unresolvable as `BLOCKED-NEEDS-INGAME` with the chosen fallback.

- [ ] **Step 3: Verify each chosen ID exists.** For every item/block ID in the ledger, confirm it appears in the relevant jar's lang/registry (python one-liner). Expected: all `CONFIRMED` or explicitly `BLOCKED-NEEDS-INGAME` with a fallback.

- [ ] **Step 4: Commit.**
```bash
git add "docs/superpowers/plans/nv-resolved-ids.md"
git commit -m "docs: resolve open NV/weave IDs for the magic-spine plan"
```

---

## Phase 1 — AStages gating (PARALLEL-SAFE: three independent files)

### Task 1.1: Lock the Neo Vitae dungeon dimension at Industrial

**Files:**
- Modify: `kubejs/server_scripts/aoa_astages_03_dimension_restrictions.js:24` (append to `dimensionLocks`)

- [ ] **Step 1: Confirm the dimension is currently ungated.**
Run: `rg -n "neovitae" kubejs/server_scripts/aoa_astages_03_dimension_restrictions.js`
Expected: no matches (NV dungeon absent from the lock list).

- [ ] **Step 2: Add the lock.** Insert this line into the `dimensionLocks` array (after the `["atomic", "macabre:the_pit"],` line):
```javascript
    ["industrial_revolution", "neovitae:dungeon"],
```
(The existing `.forEach` already applies `.setBidirectional(false)` to every entry — no per-entry change needed.)

- [ ] **Step 3: Verify the edit.**
Run: `rg -n "neovitae:dungeon" kubejs/server_scripts/aoa_astages_03_dimension_restrictions.js`
Expected: one match inside `dimensionLocks`.

- [ ] **Step 4: Commit.**
```bash
git add kubejs/server_scripts/aoa_astages_03_dimension_restrictions.js
git commit -m "feat(astages): gate neovitae:dungeon at industrial_revolution"
```

### Task 1.2: Add the Neo Vitae item-lock table to the magic cluster

**Files:**
- Modify: `kubejs/server_scripts/aoa_astages_01m_magic.js` (append entries to the `itemLocks` array, ~line 70)

**Interfaces:**
- Consumes: the existing `softItemLock`/`itemLocks` machinery (the `[stage, item, kind]` tuple form; `softItemLock` auto-skips items where `Item.exists` is false, so unknown-but-harmless IDs degrade gracefully).

- [ ] **Step 1: Confirm NV is currently absent from magic staging.**
Run: `rg -n "neovitae" kubejs/server_scripts/aoa_astages_01m_magic.js`
Expected: no matches.

- [ ] **Step 2: Append the NV entries** to the `itemLocks` array (same `[stage, item, kind]` shape as the existing rows; `block_item` for placeable blocks, `item` for non-blocks):
```javascript
    // --- Neo Vitae magic spine (2026-06-26) ---
    // Renaissance entry: altar economy
    ["the_renaissance", "neovitae:ara_vitae", "block_item"],
    ["the_renaissance", "neovitae:incense_altar", "block_item"],
    ["the_renaissance", "neovitae:alchemy_array", "block_item"],
    ["the_renaissance", "neovitae:athanor", "block_item"],
    ["the_renaissance", "neovitae:tabula_vitae", "block_item"],
    ["the_renaissance", "neovitae:blood_orb_weak", "item"],
    ["the_renaissance", "neovitae:blood_orb_apprentice", "item"],
    ["the_renaissance", "neovitae:weak_blood_shard", "item"],
    ["the_renaissance", "neovitae:blood_pearl", "item"],
    ["the_renaissance", "neovitae:bloodstone", "block_item"],
    ["the_renaissance", "neovitae:bloodstone_brick", "block_item"],
    ["the_renaissance", "neovitae:blood_stained_glass", "block_item"],
    ["the_renaissance", "neovitae:blood_tank", "block_item"],
    ["the_renaissance", "neovitae:blood_battery", "block_item"],
    // Industrial: forge + spiritus + routing
    ["industrial_revolution", "neovitae:hellfire_forge", "block_item"],
    ["industrial_revolution", "neovitae:vas_maleficum", "block_item"],
    ["industrial_revolution", "neovitae:spira_infernalis", "block_item"],
    ["industrial_revolution", "neovitae:crystallarium_maleficum", "block_item"],
    ["industrial_revolution", "neovitae:spirit_cache", "block_item"],
    ["industrial_revolution", "neovitae:spiritus_gem_petty", "item"],
    ["industrial_revolution", "neovitae:spiritus_gem_lesser", "item"],
    ["industrial_revolution", "neovitae:spiritus_gem_common", "item"],
    ["industrial_revolution", "neovitae:teleposer", "block_item"],
    ["industrial_revolution", "neovitae:tabula_robur", "item"],
    ["industrial_revolution", "neovitae:tabula_animata", "item"],
    ["industrial_revolution", "neovitae:tabula_spiritus", "item"],
    // Gilded: high orbs, Sentient gear, Hellforged chain
    ["gilded_age", "neovitae:blood_orb_magician", "item"],
    ["gilded_age", "neovitae:blood_orb_master", "item"],
    ["gilded_age", "neovitae:blood_orb_archmage", "item"],
    ["gilded_age", "neovitae:ingot_hellforged", "item"],
    ["gilded_age", "neovitae:hellforged_dust", "item"],
    ["gilded_age", "neovitae:hellforged_parts", "item"],
    ["gilded_age", "neovitae:hellforged_resonator", "item"],
    ["gilded_age", "neovitae:hellforged_block", "block_item"],
    ["gilded_age", "neovitae:demonite_trim_ingot", "item"],
    ["gilded_age", "neovitae:spiritus_gem_greater", "item"],
    ["gilded_age", "neovitae:spiritus_gem_grand", "item"],
    ["gilded_age", "neovitae:sentient_helmet", "item"],
    ["gilded_age", "neovitae:sentient_plate", "item"],
    ["gilded_age", "neovitae:sentient_leggings", "item"],
    ["gilded_age", "neovitae:sentient_boots", "item"],
    ["gilded_age", "neovitae:sentient_sword", "item"],
    ["gilded_age", "neovitae:sentient_pickaxe", "item"],
    // Atomic: apex orb + explosives + deep reagents
    ["atomic", "neovitae:blood_orb_transcendent", "item"],
    ["atomic", "neovitae:hellforged_explosive_cell", "item"],
    ["atomic", "neovitae:crystal_cluster", "block_item"],
    ["atomic", "neovitae:crystal_cluster_brick", "block_item"],
```

- [ ] **Step 3: Verify.**
Run: `rg -c "neovitae:" kubejs/server_scripts/aoa_astages_01m_magic.js`
Expected: ≥ 44.

- [ ] **Step 4: Commit.**
```bash
git add kubejs/server_scripts/aoa_astages_01m_magic.js
git commit -m "feat(astages): stage Neo Vitae apparatus Ren->Atomic in the magic cluster"
```

### Task 1.3: Hellforged tag locks + capstone block-item locks

**Files:**
- Modify: `kubejs/server_scripts/aoa_astages_06_ore_restrictions.js` (add a Gilded `softTagLock` block for hellforged material tags, following the existing `addAdvancedMaterialTags` pattern)

- [ ] **Step 1: Read the existing tag-lock pattern.**
Run: `rg -n "addAdvancedMaterialTags|softTagLock|raw_materials" kubejs/server_scripts/aoa_astages_06_ore_restrictions.js`
Expected: shows the helper(s) used to lock material tags by age. Mirror that exact call shape.

- [ ] **Step 2: Add the hellforged material-tag locks at Gilded** using the file's existing helper (substitute the real helper name found in Step 1):
```javascript
  // Neo Vitae hellforged material tags -> Gilded (naturally dungeon-gated; explicit lock = defense-in-depth)
  ["c:raw_materials/hellforged", "c:dusts/hellforged", "c:fragments/hellforged",
   "c:gravels/hellforged", "c:ingots/hellforged"].forEach(function (tag) {
    softTagLock("gilded_age", tag) // <- use the file's actual tag-lock helper/signature
  })
```
(The block-item capstone locks `hellforged_block`/`crystal_cluster*`/`bloodstone*`/`blood_stained_glass` are already covered by Task 1.2; do not duplicate.)

- [ ] **Step 3: Verify.**
Run: `rg -n "hellforged" kubejs/server_scripts/aoa_astages_06_ore_restrictions.js`
Expected: the five `c:*/hellforged` tags present, gilded_age.

- [ ] **Step 4: Commit.**
```bash
git add kubejs/server_scripts/aoa_astages_06_ore_restrictions.js
git commit -m "feat(astages): lock hellforged material tags at gilded_age"
```

---

## Phase 2 — F&A rewire + oritech re-source

### Task 2.1: `#aoa:magic_feedstock` tag + re-source the oritech foundry recipes (PARALLEL-SAFE)

**Files:**
- Create: `kubejs/data/aoa/tags/item/magic_feedstock.json`
- Modify: `kubejs/server_scripts/ir_native_capstone_recipes.js` (recipe `aoa:ir_magic_feedstock/aureal_foundry`)
- Modify: `kubejs/server_scripts/magic_spine_bridges.js` (recipe `aoa:magic_spine/oritech_machine_core_5`)

**Interfaces:**
- Produces: item tag `#aoa:magic_feedstock` = `[neovitae:hellforged_block, neovitae:ingot_hellforged, forbidden_arcanus:deorum_ingot]`, consumed by the two re-sourced recipes (deorum kept as an optional alternate so F&A players retain a use).

- [ ] **Step 1: Inspect the two recipes' current deorum requirement.**
Run: `rg -n "deorum" kubejs/server_scripts/ir_native_capstone_recipes.js kubejs/server_scripts/magic_spine_bridges.js`
Expected: each recipe hard-requires `forbidden_arcanus:deorum_ingot` (or `deorum_block`).

- [ ] **Step 2: Create the tag.**
```json
{
  "replace": false,
  "values": [
    "neovitae:hellforged_block",
    "neovitae:ingot_hellforged",
    "forbidden_arcanus:deorum_ingot"
  ]
}
```

- [ ] **Step 3: Re-point both recipes** to accept the tag instead of the bare deorum id — replace each `Item.of('forbidden_arcanus:deorum_ingot')` / `'forbidden_arcanus:deorum_ingot'` ingredient with `'#aoa:magic_feedstock'` (KubeJS ingredient form). Keep every other ingredient and the output unchanged.

- [ ] **Step 4: Validate JSON + edits.**
Run: `python -m json.tool "kubejs/data/aoa/tags/item/magic_feedstock.json"`
Run: `rg -n "magic_feedstock" kubejs/server_scripts/ir_native_capstone_recipes.js kubejs/server_scripts/magic_spine_bridges.js`
Expected: JSON valid; each recipe now references `#aoa:magic_feedstock`.

- [ ] **Step 5: Commit.**
```bash
git add "kubejs/data/aoa/tags/item/magic_feedstock.json" kubejs/server_scripts/ir_native_capstone_recipes.js kubejs/server_scripts/magic_spine_bridges.js
git commit -m "feat(weave): re-source oritech foundry off deorum onto #aoa:magic_feedstock (hellforged+deorum)"
```

### Task 2.2: Rewire `ren_magic_foundations` (Renaissance required spine)

**Files:**
- Modify: `config/ftbquests/quests/chapters/ren_magic_foundations.snbt`
- Modify: `config/ftbquests/quests/lang/en_us.snbt` (retitle/retheme this chapter's `quest.<id>.*` keys)

**Node mapping (spec §5; apply task-item swaps, preserve every node id + edge + reward):**
| Node | → task item | type |
|---|---|---|
| `0B03101000000030` | `neovitae:weak_blood_shard` | item |
| `0B03101000000031` | `neovitae:blood_orb_weak` | item |
| `0B03101000000032` | `neovitae:ara_vitae` | interact_block |
| `0B03101000000033` | `neovitae:rune_blank` | item |
| `0B03101000000034` | `neovitae:blood_orb_apprentice` | item |
| `0B03101000000035` | `neovitae:sigil_divination` | item |
| `0B03101000000036` | `neovitae:weak_blood_shard` | item |
| `0B03101000000037` | `neovitae:hellfire_forge` | interact_block |
| `0B03101000000038` | `neovitae:spiritus_gem_petty` | item |
| `0B03101000000039` **(CAPSTONE — keep `/astages add ren_magic_foundations_complete` + J2A mirror)** | `neovitae:athanor` | item |
| `0B0310100000003D` **(preserve id — dep root of ren_nether_threshold)** | `neovitae:incense_altar` | item |
| `0B03101000000070` | `neovitae:spiritus_gem_lesser` | item |
| `0B03101000000071` | `neovitae:raw_spiritus` | item |
| `0B03101000000072` | `neovitae:corrupted_dust` | item |
| `0B03101000000073` | `neovitae:base_spiritus_soul_raw` | item |
| `0B03101000000074` | `neovitae:spiritus_ruina_shard` | item |
| `0B03101000000075` | `neovitae:spiritus_gem_common` | item |
| `0B03101000000076` | `neovitae:blood_pearl` | item |
| `0B03101000000077` | `neovitae:incense_altar` | interact_block |

- [ ] **Step 1: Detect this file's line-ending style** (preserve it through every write):
```bash
python -c "raw=open(r'config/ftbquests/quests/chapters/ren_magic_foundations.snbt','rb').read(); print('CRLF',raw.count(b'\r\n'),'LF',raw.count(b'\n')-raw.count(b'\r\n'))"
```
Note which dominates; keep it.

- [ ] **Step 2: Capture pre-state.**
Run: `rg -c "forbidden_arcanus:" config/ftbquests/quests/chapters/ren_magic_foundations.snbt`
Expected: ~19 (the nodes above). Record the count.

- [ ] **Step 3: Apply the mapping.** For each node above: replace the F&A task `id`/`item` with the NV id; for the two `interact_block`/`interact_block`-typed rows, convert the `item` task into the richer task form (read the exact SNBT shape of an existing `interact_block`/`use_block` task in the repo first — e.g. via `rg -n "type: \"interact_block\"" config/ftbquests/quests/chapters` — and mirror it). Do NOT touch node `id:`, `dependencies:`, `rewards:` (esp. the `command` reward on `…039`), or the chapter group id.

- [ ] **Step 4: Retheme the lang keys.** In `lang/en_us.snbt`, update `quest.<id>.title/.quest_subtitle/.quest_desc` for the rewired nodes to Neo Vitae prose (Ara Vitae / orbs / Spiritus). Keep keys; change values.

- [ ] **Step 5: Verify residue + node preservation.**
Run: `rg -c "forbidden_arcanus:" config/ftbquests/quests/chapters/ren_magic_foundations.snbt` → Expected: `0`.
Run: `for id in 0B03101000000039 0B0310100000003D 0B03101000000032; do rg -q "$id" config/ftbquests/quests/chapters/ren_magic_foundations.snbt && echo "$id OK" || echo "$id MISSING"; done` → Expected: all OK.
Run: `rg -n "ren_magic_foundations_complete" config/ftbquests/quests/chapters/ren_magic_foundations.snbt` → Expected: still present (capstone reward intact).
Run the line-ending check from Step 1 again → Expected: same dominant style.

- [ ] **Step 6: Commit.**
```bash
git add config/ftbquests/quests/chapters/ren_magic_foundations.snbt config/ftbquests/quests/lang/en_us.snbt
git commit -m "feat(quests): rewire ren_magic_foundations from F&A to Neo Vitae (capstone + J2A mirror preserved)"
```

### Task 2.3: Rewire `ren_nether_threshold` (deorum→hellforged metal lane)

**Files:**
- Modify: `config/ftbquests/quests/chapters/ren_nether_threshold.snbt` (+ its chapter icon at the top, currently `forbidden_arcanus:mundabitur_dust`)
- Modify: `config/ftbquests/quests/lang/en_us.snbt`

**Node mapping (preserve all ids — 041/042/046/047 are intra-lane deps):**
| Node | → task item |
|---|---|
| `0B03102000000040` | `neovitae:rune_speed` |
| `0B03102000000041` | `neovitae:hellforged_dust` |
| `0B03102000000042` | `neovitae:ingot_hellforged` |
| `0B03102000000046` | `neovitae:hellforged_parts` |
| `0B03102000000047` | `neovitae:hellforged_block` |
| `0B03102000000080` | `neovitae:blood_pearl` |
| `0B03102000000081` | `neovitae:spiritus_gem_petty` |
Chapter icon → `neovitae:ingot_hellforged`.

- [ ] **Step 1:** line-ending check (as Task 2.2 Step 1, this file).
- [ ] **Step 2:** `rg -c "forbidden_arcanus:" config/ftbquests/quests/chapters/ren_nether_threshold.snbt` → record (~10 incl. icon + the `mundabitur_dust` mirror at line ~522 inside an OR task — verify whether that is a task ingredient or icon and swap accordingly).
- [ ] **Step 3:** apply the mapping; update the chapter icon; preserve ids/edges. Note the chapter capstone is `…062` (create:blaze_burner) — this F&A lane does NOT feed it, so no capstone edge changes.
- [ ] **Step 4:** retheme lang keys for these nodes (nether-forged hellforged metal theme).
- [ ] **Step 5:** `rg -c "forbidden_arcanus:" config/ftbquests/quests/chapters/ren_nether_threshold.snbt` → Expected `0`; confirm ids `0B03102000000042`, `0B03102000000040` present; line-ending unchanged.
- [ ] **Step 6:** commit `feat(quests): rewire ren_nether_threshold deorum lane to Neo Vitae hellforged`.

### Task 2.4: Rewire `ir_magic_feedstock_and_spectrum_network` (Industrial required proof)

**Files:**
- Modify: `config/ftbquests/quests/chapters/ir_magic_feedstock_and_spectrum_network.snbt`
- Modify: `config/ftbquests/quests/lang/en_us.snbt`

**Node mapping (REWIRE the two load-bearing nodes — keep ids/edges so IR capstone `49540B1000000015` fan-in survives):**
| Node | → task item | type | note |
|---|---|---|---|
| `49540B1000000004` | `neovitae:hellfire_forge` | interact_block | LOAD-BEARING anchor |
| `49540B1000000018` | `neovitae:hellforged_block` | item | LOAD-BEARING; pairs with Task 2.1 recipe re-source |
| `49540B1000000019` | `neovitae:blood_tank` | item | |
| `49540B100000001A` | `neovitae:hellforged_resonator` | item | |
| `49540B100000001B` | `neovitae:sentient_helmet` | item | optional gear |
| `49540B100000001C` | `neovitae:sentient_plate` | item | optional gear |
| `49540B100000001D` | `neovitae:sentient_leggings` | item | optional gear |
| `49540B100000001E` | `neovitae:sentient_boots` | item | optional gear |

- [ ] **Step 1:** line-ending check (this file).
- [ ] **Step 2:** `rg -c "forbidden_arcanus:" <file>` → record (~8); confirm the capstone `49540B1000000015` and edges `…0004 → …0018 → …0005` exist before editing (`rg -n "49540B1000000015|49540B1000000018|49540B1000000004" <file>`).
- [ ] **Step 3:** apply mapping; preserve ids/edges/rewards; the `…0018` → `…0005` (oritech foundry) → `…0015` chain must remain intact (Task 2.1 makes the foundry recipe accept hellforged).
- [ ] **Step 4:** retheme lang keys.
- [ ] **Step 5:** `rg -c "forbidden_arcanus:" <file>` → Expected `0`; ids `…0015/…0018/…0004` present; line-ending unchanged.
- [ ] **Step 6:** commit `feat(quests): rewire IR magic-feedstock bridge to Neo Vitae hellforged (proof chain preserved)`.

### Task 2.5: Rewire the `g1_the_golden_workshop` root + icon (Gilded required proof)

**Files:**
- Modify: `config/ftbquests/quests/chapters/g1_the_golden_workshop.snbt`
- Modify: `config/ftbquests/quests/lang/en_us.snbt`

- [ ] **Step 1:** line-ending check (this file).
- [ ] **Step 2:** confirm structure: `rg -n "4757011020010001|forbidden_arcanus:hephaestus_forge_tier_3" config/ftbquests/quests/chapters/g1_the_golden_workshop.snbt` → expect the root node (3 hits: chapter `icon`, the node `id`, and the `use_block` task `id`).
- [ ] **Step 3:** REWIRE node `4757011020010001`: change the chapter `icon` and the `use_block` task block from `forbidden_arcanus:hephaestus_forge_tier_3` to `neovitae:athanor`. Keep the node id, root position, `use_block` type, and all 6 child dependency edges. (Alt block if preferred at review: `neovitae:vas_maleficum`.)
- [ ] **Step 4:** retheme the root's lang keys (the golden-workshop Vitae apex station).
- [ ] **Step 5:** `rg -c "forbidden_arcanus:" config/ftbquests/quests/chapters/g1_the_golden_workshop.snbt` → Expected `0`; `rg -q "4757011020010001" <file>` → OK; confirm 6 children still reference it (`rg -c "4757011020010001" <file>` ≥ 7); line-ending unchanged.
- [ ] **Step 6:** commit `feat(quests): rewire g1 golden-workshop root from Hephaestus Forge T3 to Neo Vitae Athanor`.

### Task 2.6: Delete Medieval edelwood nodes + rewire the stray optional soul leaf

**Files:**
- Modify: `config/ftbquests/quests/chapters/metallurgy.snbt` (DELETE nodes `2902E58DB70F95F1`, `2902E58DB70F95F2`)
- Modify: `config/ftbquests/quests/chapters/ren_observation_experimentation.snbt` (REPLACE node `0B031080000000C2` → `neovitae:base_spiritus_soul_raw`)
- Modify: `config/ftbquests/quests/lang/en_us.snbt` (remove the deleted nodes' keys; retheme the replaced one)

- [ ] **Step 1:** line-ending check (both files).
- [ ] **Step 2:** confirm `2902E58DB70F95F1` (edelwood_log) → `2902E58DB70F95F2` (edelwood_oil) is a 2-node dead-end with no external dependents: `rg -n "2902E58DB70F95F1|2902E58DB70F95F2" config/ftbquests/quests/chapters/` → expect hits only within metallurgy.snbt.
- [ ] **Step 3:** delete both edelwood quest objects from metallurgy.snbt (and their lang keys). Replace the single optional `0B031080000000C2` task item with `neovitae:base_spiritus_soul_raw` (preserve its id + its dep `0B03108000000001`).
- [ ] **Step 4:** verify — `rg -c "forbidden_arcanus:edelwood" config/ftbquests/quests/chapters/metallurgy.snbt` → `0`; `rg -c "forbidden_arcanus:" config/ftbquests/quests/chapters/ren_observation_experimentation.snbt` → `0`; metallurgy still parses (brace balance, Step in Task 6.2); line-endings unchanged.
- [ ] **Step 5:** commit `feat(quests): delete Medieval edelwood nodes; rewire stray soul leaf to Neo Vitae`.

> Note on `journey_to_ascension.snbt`: its `forbidden_arcanus:mundabitur_dust` reference is an **icon only** on a `check_quest` stage-mirror — KEEP. Optionally retheme the icon to a Create/NV icon in Task 6.2; never change the `check_quest` target.

---

## Phase 3 — F&A pain patches (PARALLEL-SAFE)

### Task 3.1: Neutralize the Black Hole accident hazard

**Files:**
- Modify: `kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js`

- [ ] **Step 1: Confirm the corrupti_dust craft route exists.**
Run: `rg -n "corrupti_dust|black_hole|dark_matter" kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js`
Expected: no existing removal (the native craft is live).

- [ ] **Step 2: Remove the corrupti_dust craft** inside the existing `ServerEvents.recipes` block (the Black Hole cannot spawn without it):
```javascript
  // F&A Black Hole hazard neutralize (2026-06-26): remove the accidental item-deleter feedstock.
  event.remove({ output: 'forbidden_arcanus:corrupti_dust' })
```
If anything required consumed corrupti_dust (Task 2.2 replaced the ren node `…072` off it), there are no remaining required consumers; confirm with `rg -rn "corrupti_dust" config/ftbquests kubejs` → expect only this removal line.

- [ ] **Step 3: Verify.**
Run: `rg -n "remove\(\{ output: 'forbidden_arcanus:corrupti_dust'" kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js`
Expected: one match.

- [ ] **Step 4: Commit.**
```bash
git add kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js
git commit -m "fix(fna): neutralize Black Hole item-deletion hazard (remove corrupti_dust craft)"
```

### Task 3.2: Make Soul Looting deterministically obtainable

**Files:**
- Modify: `kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js` (add a craftable enchanted book)

- [ ] **Step 1: Confirm the enchant id.**
Run: `python -c "import zipfile; z=zipfile.ZipFile(r'mods/forbidden_arcanus-2.6.1.jar'); print([n for n in z.namelist() if 'soul_looting' in n])"`
Expected: `data/forbidden_arcanus/enchantment/soul_looting.json` present → enchant id `forbidden_arcanus:soul_looting`.

- [ ] **Step 2: Add a deterministic craft** for a Soul Looting I enchanted book (KubeJS `event.custom` enchanted-book recipe, or a shaped recipe producing `minecraft:enchanted_book` with the `stored_enchantments` component). Mirror an existing enchanted-book recipe in the repo if one exists (`rg -n "stored_enchantments|enchanted_book" kubejs/server_scripts`); else use:
```javascript
  // Deterministic Soul Looting I book (removes the RNG entry gate; F&A soul lane is optional now)
  event.shaped('minecraft:enchanted_book', ['SBS','B B','SBS'], {
    S: 'forbidden_arcanus:soul', B: 'minecraft:book'
  }).id('aoa:fna/soul_looting_book')
    .modifyResult((grid, result) => result.withChance ? result : result) // placeholder if NBT helper needed
```
> Implementer note: the enchant must be written into the book's `stored_enchantments`. Use the repo's established enchanted-book pattern from Step 2's grep; if none exists, use `Recipes.createSmithing`/`event.custom` with a `minecraft:crafting_shaped` JSON whose `result` carries `"components": {"minecraft:stored_enchantments": {"levels": {"forbidden_arcanus:soul_looting": 1}}}`. Verify the component key/shape against a vanilla enchanted-book give command output before finalizing.

- [ ] **Step 3: Verify the recipe id loads.**
Run: `rg -n "soul_looting_book|forbidden_arcanus:soul_looting" kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js`
Expected: present.

- [ ] **Step 4: Commit.**
```bash
git add kubejs/server_scripts/forbidden_arcanus_recipe_fixes.js
git commit -m "fix(fna): add deterministic Soul Looting book (remove RNG entry gate)"
```

---

## Phase 4 — Cross-mod weaves (PARALLEL-SAFE: independent files; consumes Task 0.1 ledger)

### Task 4.1: Populate `#neovitae:altar/pillars` with cross-mod pillar blocks

**Files:**
- Create: `kubejs/data/neovitae/tags/block/altar/pillars.json`
- Create: `kubejs/data/neovitae/tags/item/altar/pillars.json` (JEI mirror)

- [ ] **Step 1: Pull `PILLAR_BLOCKS` from the Task 0.1 ledger** (1 F&A darkstone-pillar + 1 Malum + 1 Spectrum + 1 plain NV fallback, all confirmed craftable).
- [ ] **Step 2: Write the block tag** (replace the empty shipped tag):
```json
{ "replace": false, "values": [ "<NV_FALLBACK_PILLAR>", "<FNA_PILLAR>", "<MALUM_BLOCK>", "<SPECTRUM_BLOCK>" ] }
```
Write the identical list to the item-tag mirror.
- [ ] **Step 3: Validate JSON.** `python -m json.tool` on both files → Expected: valid.
- [ ] **Step 4: Commit** `feat(weave): populate empty neovitae altar/pillars with cross-mod blocks (fixes tier-2+ altar softlock)`.
> Validation caveat (spec §4/F6): whether pillars are structurally required is confirmed in the Task 6.4 in-game test. Populating the tag is safe regardless (adds valid pillar blocks; cannot break a working altar).

### Task 4.2: Cross-mod altar capstones (W1 t3 + NV5 t6)

**Files:**
- Create: `kubejs/data/neovitae/tags/block/altar/t3_capstones.json` (+ item mirror) — adds `MALUM_CAPSTONE_BLOCK` alongside the shipped `neovitae:blood_stained_glass`
- Create: `kubejs/data/neovitae/tags/block/altar/t6_capstones.json` (+ item mirror) — adds `SPECTRUM_CAPSTONE_BLOCK` alongside shipped `crystal_cluster`/`crystal_cluster_brick`

- [ ] **Step 1:** pull `MALUM_CAPSTONE_BLOCK` + `SPECTRUM_CAPSTONE_BLOCK` from the ledger.
- [ ] **Step 2:** write each tag with `"replace": false` and the shipped members + the new cross-mod member (so the vanilla capstone still works — these are *added alternatives*, never required). Example t3:
```json
{ "replace": false, "values": [ "neovitae:blood_stained_glass", "<MALUM_CAPSTONE_BLOCK>" ] }
```
- [ ] **Step 3:** `python -m json.tool` all four files → valid.
- [ ] **Step 4:** commit `feat(weave): add Malum (t3) + Spectrum (t6) optional altar capstones`.

### Task 4.3: Neo Vitae recipe weaves (NV1–NV4 + Clibano→Athanor)

**Files:**
- Create: `kubejs/server_scripts/aoa_recipes_neovitae_weaves.js`

**Interfaces:**
- Consumes: `MALUM_SPIRIT`, `THEURGY_SALT`, `occultism:otherworld_essence` (verified), `forbidden_arcanus:eternal_stella` (verified), `NV_SENTIENT_UPGRADE_OK` from the ledger.

- [ ] **Step 1: Confirm native recipes to remove** (hygiene): `python -c "import zipfile; z=zipfile.ZipFile(r'mods/neovitae-1.21.1-1.0.25.jar'); print([n for n in z.namelist() if 'recipe/hellfire_forge/sentient_' in n])"` → note the native `sentient_axe`/`sentient_sword` transform recipe ids to `event.remove`.
- [ ] **Step 2: Author the weaves** using the verified `ServerEvents.recipes` + `event.custom(<json>)` form (KubeJS passes the JSON straight to the NV serializer). Each weave first removes the native route it overrides:
```javascript
ServerEvents.recipes(event => {
  // NV1 — Spirit-Fed Sentient Forge (Malum -> NV): remove native, re-add with a Malum spirit catalyst
  event.remove({ type: 'neovitae:hellfire_forge_transform', output: 'neovitae:sentient_axe' })
  event.custom({
    type: 'neovitae:hellfire_forge_transform',
    transformInput: { item: 'minecraft:iron_axe' },
    catalysts: [ { item: 'neovitae:spiritus_gem_petty' }, { item: '<MALUM_SPIRIT>' } ],
    drain: 0.0, minDrain: 0.0,
    output: { count: 1, id: 'neovitae:sentient_axe' }
  })

  // NV2 — Calcined Salt Catalyst (Theurgy -> NV): single-route hellfire_forge reagent + alchemical salt
  // (pick ONE NV reagent output that has exactly one native forge recipe; remove it first)
  // event.remove({ type: 'neovitae:hellfire_forge', output: '<NV_SINGLE_ROUTE_REAGENT>' })
  event.custom({
    type: 'neovitae:hellfire_forge',
    inputs: [ { tag: 'c:dusts/hellforged' }, { item: '<THEURGY_SALT>' } ],
    drain: 80.0, minDrain: 800.0,
    output: { count: 1, id: '<NV_SINGLE_ROUTE_REAGENT>' }
  })

  // NV3 — Otherworld Bloom Flask (Occultism -> NV): low-tier alchemytable recipe
  event.custom({
    type: 'neovitae:alchemytable',
    input: [ { item: 'neovitae:simple_catalyst' }, { item: 'occultism:otherworld_essence' } ],
    output: { count: 1, id: 'neovitae:alchemy_flask' },
    syphon: 500, ticks: 200, upgradeLevel: 1
  })

  // NV4 — Stellar Tempering (F&A -> NV): route eternal_stella through NV's OWN forge upgrade.
  // Only if NV_SENTIENT_UPGRADE_OK; else fall back to a hellfire_forge recipe consuming eternal_stella
  // into an NV apex trophy item.
  event.custom({
    type: 'neovitae:hellfire_forge_upgrade',
    catalysts: [ { item: 'forbidden_arcanus:eternal_stella' }, { item: 'neovitae:tabula_robur' } ],
    drain: 200.0, minDrain: 400.0
  })

  // Clibano -> Athanor companion: let F&A Clibano residue feed an NV Athanor processing recipe
  // (keep optional/unlocked; pick a residue item confirmed in the F&A jar).
  event.custom({
    type: 'neovitae:athanor',
    chance_outputs: [],
    guaranteed_outputs: [ { count: 1, id: '<NV_PROCESSED_OUTPUT>' } ],
    inputs: [ { item: '<FNA_CLIBANO_RESIDUE>' } ],
    tool: { tag: 'neovitae:athanor_tool/cutting_fluids' }
  })
})
```
Replace each `<…>` from the ledger / a quick jar check; leave a `// VERIFY` comment on any that resolves to a fallback. Do NOT ship a `<…>` placeholder.

- [ ] **Step 3: Verify the script parses and references only real types.**
Run: `rg -n "type: 'neovitae:" kubejs/server_scripts/aoa_recipes_neovitae_weaves.js`
Expected: only `hellfire_forge`, `hellfire_forge_transform`, `hellfire_forge_upgrade`, `alchemytable`, `athanor` (the verified types).

- [ ] **Step 4: Commit** `feat(weave): Neo Vitae cross-mod recipe weaves (Malum/Theurgy/Occultism/F&A/Clibano)`.

### Task 4.4: Age-pace rituals via `ritual_stats` overlay (W6)

**Files:**
- Create: `kubejs/data/neovitae/data_maps/neovitae/ritual/ritual_stats.json`

- [ ] **Step 1:** dump the shipped map for reference: `python -c "import zipfile; print(zipfile.ZipFile(r'mods/neovitae-1.21.1-1.0.25.jar').read('data/neovitae/data_maps/neovitae/ritual/ritual_stats.json').decode())"`.
- [ ] **Step 2:** write a `{"replace": false, "values": {...}}` overlay that bumps `activation_cost`/`crystal_level` on the high-tier rituals to match AoA pacing (do NOT reference `neovitae:simple_dungeon`/`standard_dungeon` — Java-hardcoded, untunable). Keep it conservative; only retune rituals that exist in the dumped map.
- [ ] **Step 3:** `python -m json.tool` → valid; confirm no `simple_dungeon`/`standard_dungeon` keys.
- [ ] **Step 4:** commit `feat(weave): age-pace Neo Vitae rituals via ritual_stats overlay`.

---

## Phase 5 — Atomic/OW optional depth + lore

### Task 5.1: Discover Atomic/OW host chapters + design insertion (no new/optional chapters)

**Files:**
- Read: `config/ftbquests/quests/chapters/ow6_beyond_the_veil.snbt`, plus the Atomic chapters (`at5_threshold_of_war.snbt`, `at7_chaos_convergence.snbt`, `atomic_oritech_convergence.snbt`)
- Create: `docs/superpowers/plans/nv-atomic-ow-depth.md` (insertion design)

- [ ] **Step 1:** read the candidate chapters; pick the best existing required chapter in each age to host NV optional-depth quests (likely `ow6_beyond_the_veil` for OW; an Atomic chapter for the transcendent altar / demon-dungeon line). Record each host chapter's group id + a free node-position region.
- [ ] **Step 2:** design the optional-depth quest set per spec §1/§2 (Atomic: transcendent altar via `crystal_cluster` t6, `blood_orb_transcendent`, dungeon ritual `simple_key`→`observation` on `neovitae:dungeon`, `standard_key`, mine Demonite + Foreman as optional reward-gear only; OW: maxed Sentient gear, full Spiritus aspects, optional Ascension-convergence flavor). Mark every quest `optional: true`; **none** runs `/astages add` for atomic; if any feeds a convergence, it is a fan-in dep only.
- [ ] **Step 3:** commit the design doc. (This is a reviewed checkpoint before authoring.)

### Task 5.2: Author Atomic NV optional-depth quests

**Files:**
- Modify: the Atomic host chapter from Task 5.1 + `config/ftbquests/quests/lang/en_us.snbt`

- [ ] **Step 1:** line-ending check (host file).
- [ ] **Step 2:** add the Atomic optional-depth quests (new unique hex node ids — generate non-colliding ids; verify uniqueness with `rg`), each `optional: true`, using `observation` for the `neovitae:dungeon` entry and `item`/`interact_block` elsewhere. No stage-grant command rewards.
- [ ] **Step 3:** add lang keys; verify `rg -c "forbidden_arcanus:"` unaffected; brace balance (Task 6.2 check); node-id uniqueness across the chapter.
- [ ] **Step 4:** commit `feat(quests): add Neo Vitae optional-depth wing to the Atomic age`.

### Task 5.3: Author OW NV optional-depth quests

**Files:**
- Modify: `config/ftbquests/quests/chapters/ow6_beyond_the_veil.snbt` (or the Task 5.1 OW host) + `lang/en_us.snbt`

- [ ] **Step 1–4:** same shape as Task 5.2 for the OW depth set (maxed Sentient gear, full Spiritus aspect economy, optional Ascension-convergence flavor — command-reward on a real NV apex item, never a checkmark). Commit `feat(quests): add Neo Vitae optional-depth wing to the Otherworldly age`.

### Task 5.4: Scriptura Vitae Modonomicon entry

**Files:**
- Create/Modify: a Modonomicon entry under `kubejs/data/aoa/modonomicon/books/<book>/entries/...` OR a `data/neovitae/modonomicon/...` override (use `NV_MODONOMICON_BOOK` from the ledger to decide).

- [ ] **Step 1:** from the ledger, decide whether to add an AoA renaissance-compendium entry pointing at the NV spine or override the NV Scriptura Vitae intro. Mirror an existing AoA Modonomicon entry's JSON shape (`rg -l "modonomicon" kubejs/data/aoa/modonomicon/books`).
- [ ] **Step 2:** author the entry (lore + the Ren→Gilded ladder pointer). `python -m json.tool` → valid.
- [ ] **Step 3:** commit `docs(lore): Scriptura Vitae / Neo Vitae spine Modonomicon entry`.

---

## Phase 6 — Validation

### Task 6.1: Datapack JSON lint (all new JSON)

- [ ] **Step 1:** `python -c "import json,glob,sys; bad=[f for f in glob.glob('kubejs/data/**/*.json',recursive=True)+glob.glob('config/ftbquests/**/*.json',recursive=True) if _try(f)]" ` — or simply loop: for every new JSON file from Tasks 2.1, 4.1, 4.2, 4.4, run `python -m json.tool "<f>" > /dev/null && echo "OK <f>"`. Expected: all OK.
- [ ] **Step 2:** commit nothing (validation only) unless a fix is needed.

### Task 6.2: FTBQ integrity sweep

- [ ] **Step 1: F&A residue scan** across rewired chapters: `rg -c "forbidden_arcanus:" config/ftbquests/quests/chapters/{ren_magic_foundations,ren_nether_threshold,ir_magic_feedstock_and_spectrum_network,g1_the_golden_workshop,metallurgy,ren_observation_experimentation}.snbt` → Expected: `0` for each (journey_to_ascension intentionally excluded — icon-only).
- [ ] **Step 2: Brace/paren balance** per edited chapter: `python -c "import sys;[print(f, open(f,encoding='utf-8',errors='replace').read().count('{')-open(f,encoding='utf-8',errors='replace').read().count('}')) for f in sys.argv[1:]]" config/ftbquests/quests/chapters/*.snbt` → Expected: `0` delta on every edited file.
- [ ] **Step 3: Stage-grant + capstone preservation:** `rg -n "ren_magic_foundations_complete|ir_magic_feedstock_complete" config/ftbquests/quests/chapters/` → Expected: both grants still present on their capstone nodes.
- [ ] **Step 4: J2A mirrors intact:** run `python ".aoa_reveal_audit/verify_j2a.py"` (if it needs args, read its `--help`/top comment first). Expected: the `check_quest` mirrors `5350010000020002`/`…0003` still target their real capstones; no broken mirror. If `verify_j2a.py` is stale/missing, instead `rg -n "5350010000020002|5350010000020003" config/ftbquests/quests/chapters/journey_to_ascension.snbt` and confirm targets unchanged.
- [ ] **Step 5: Node-id uniqueness** for any nodes added in Phase 5: `rg -o "id: \"[0-9A-F]{16}\"" config/ftbquests/quests/chapters/<host>.snbt | sort | uniq -d` → Expected: empty (no duplicate ids).

### Task 6.3: Softlock / bypass review

- [ ] **Step 1:** confirm NV is now staged: `rg -c "neovitae:" kubejs/server_scripts/aoa_astages_01m_magic.js kubejs/server_scripts/aoa_astages_03_dimension_restrictions.js` → Expected: both > 0.
- [ ] **Step 2:** confirm the diamond floor + dungeon gate reasoning holds (spec §3 F1/F3): `rg -n "neovitae:dungeon" kubejs/server_scripts/aoa_astages_03_dimension_restrictions.js` (1 hit, industrial_revolution). 
- [ ] **Step 3:** invoke the `aoa-softlock-hardlock-audit` and `aoa-bypass-sequence-break-audit` skills against the NV spine (Ren→Gilded route + dungeon access) and address any HARDLOCK/BYPASS finding. Report-only unless a fix is required.

### Task 6.4: Final in-game smoke test (HUMAN / pack owner)

> This task cannot be done headless — it requires launching the modpack. Hand this checklist to the user.

- [ ] **Pillars (F6):** build a tier-2 Ara Vitae using the populated `#neovitae:altar/pillars` blocks; confirm it validates and a `blood_orb_magician` can be crafted. (If a tier-2 altar validates with NO pillars, the pillars tag is cosmetic-only — harmless.)
- [ ] **Renaissance spine:** craft Ara Vitae → `blood_orb_weak` (needs diamond) → place runes → Hellfire Forge → `spiritus_gem_petty` → Athanor; confirm the `ren_magic_foundations` capstone completes and grants `ren_magic_foundations_complete`.
- [ ] **IR bridge:** confirm the oritech foundry recipe accepts `neovitae:hellforged_block` (via `#aoa:magic_feedstock`) and the IR magic-feedstock capstone still completes.
- [ ] **Gating:** confirm `neovitae:dungeon` cannot be entered before Industrial; confirm NV apparatus is locked before its age in JEI.
- [ ] **Weaves:** confirm NV1 (Malum spirit → Sentient axe), NV4 (eternal_stella forge upgrade or fallback), and the Black Hole patch (corrupti_dust uncraftable) behave as intended; confirm the Soul Looting book is craftable.
- [ ] **JEI/lang:** spot-check that rewired quests show NV items + new prose, not F&A.

---

## Self-Review (completed by plan author)

- **Spec coverage:** §2 chapter rewires → Tasks 2.2–2.6; §3 AStages → Phase 1; §4 pillars → 4.1 + 6.4; §5 node table → Tasks 2.2–2.6 (all rows); §6 weaves → Phase 4; §7 patches → Phase 3; §8 quest types → applied in 2.x/5.x; §9 capability → respected (no Java, no dungeon-ritual retune); §10 risks → Phase 6 + 6.4; §11 phasing → Phases 0–6; §12 open items → Task 0.1 + 6.4. No spec section is unaddressed.
- **Placeholder scan:** the only intentional `<…>` tokens are in Tasks 4.1/4.3, each explicitly resolved from the Task 0.1 ledger before authoring with a "do NOT ship a placeholder" instruction; Task 3.2's enchanted-book NBT shape carries a concrete fallback (the `stored_enchantments` component JSON). No "TBD/handle edge cases" steps.
- **Consistency:** node IDs, stage names (`the_renaissance`/`industrial_revolution`/`gilded_age`/`atomic`/`otherworldly`), recipe type strings (`ara_vitae_recipe`/`array`/`athanor`/`hellfire_forge*`/`alchemytable`/`sentient_downgrade`), and the `#aoa:magic_feedstock` tag name are used identically across tasks and match the spec.

## Parallelization map (for subagent-driven / dispatching-parallel-agents)

- **Sequential gate:** Task 0.1 before Phase 4/5.
- **Parallel-safe batches** (no shared files): Phase 1 (1.1 / 1.2 / 1.3); Phase 3 (3.1 / 3.2 share one file → run sequentially or one agent); Phase 4 (4.1 / 4.2 / 4.3 / 4.4 — independent files; 4.1–4.2 need the 0.1 ledger).
- **Must be sequential** (shared `lang/en_us.snbt`): Tasks 2.2 → 2.3 → 2.4 → 2.5 → 2.6 (each edits the shared lang file; run one at a time with review, or worktree-isolate + merge).
- **Task 2.1** is parallel-safe with the 2.2–2.6 chain (different files) but 2.4 depends on 2.1's recipe re-source conceptually (verify together in 6.4).
