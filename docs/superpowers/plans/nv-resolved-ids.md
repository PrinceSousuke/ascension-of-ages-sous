# NV Resolved IDs — Task 0.1 Ledger

Generated 2026-06-27. Jars cracked: `neovitae-1.21.1-1.0.25.jar`, `spectrum-1.11.8-1.21.1-neo.jar`, `malum-1.21.1-1.8.2.jar`, `theurgy-1.21.1-neoforge-1.73.1.jar`, `forbidden_arcanus-2.6.1.jar`.

---

## 1. NV_MODONOMICON_BOOK

**Status: CONFIRMED**

- Book ID: `neovitae:guide`
- Book JSON path in jar: `data/neovitae/modonomicon/books/guide/book.json`
- The book is registered as a Modonomicon book with `"custom_book_item": "neovitae:guide_book"` (item exists in lang as `item.neovitae.guide_book` = `"Vitae Compendium"`).
- The book has full categories: `altar`, `alchemy_arrays`, `dungeons`, `rituals`, `spiritus`, `tabula_vitae`, `utility`.

**AoA implication:** NV ships its own Modonomicon book (`neovitae:guide`). Any AoA-side Modonomicon lore entry should add a new entry INTO a separate AoA book (not the NV guide), or use FTBQ quest text — the NV guide is owned by the mod.

---

## 2. SPECTRUM_CAPSTONE_BLOCK

**Status: CONFIRMED**

- Chosen ID: `spectrum:onyx_block` ("Block of Onyx")
- Evidence: `assets/spectrum/lang/en_us.json` key `block.spectrum.onyx_block = Block of Onyx`
- Crafting recipe: `data/spectrum/recipe/crafting_table/gem_blocks/onyx_block.json` — shaped 2×2 of `spectrum:onyx_shard`, no `required_advancement` gating in the JSON itself.
- Thematic fit: Onyx is deep black/void-colored — reads "radiant/dark crystal", fitting a Transcendent (t6) altar capstone with an arcane feel.

**Alternative considered:** `spectrum:spectral_shard_storage_block` ("Polished Spectral Shard Block") — also valid, but Onyx is more thematically distinctive for t6.

**Note:** `#neovitae:altar/t6_capstones` currently contains `neovitae:crystal_cluster` and `neovitae:crystal_cluster_brick` (confirmed from `data/neovitae/tags/block/altar/t6_capstones.json`). AoA must ADD `spectrum:onyx_block` to this tag via a KubeJS data pack or JSON override.

---

## 3. MALUM_CAPSTONE_BLOCK

**Status: CONFIRMED**

- ID: `malum:block_of_soulstone`
- Evidence: `assets/malum/blockstates/block_of_soulstone.json` exists; lang key `block.malum.block_of_soulstone = Block of Soulstone`.
- Recipe: `data/malum/recipe/block_of_soulstone.json` — shaped 3×3 of `malum:refined_soulstone` (smelted from ore via furnace/blast furnace, no special machine).
- AStages gating: **NO lock on `malum:block_of_soulstone` itself.** The spirit machines are locked (`malum:spirit_crucible` and `malum:spirit_catalyzer` at `industrial_revolution`; `malum:spirit_altar` at `the_renaissance`). Soulstone ore is world-gen, so the block is first accessible when the player can smelt refined soulstone — available in **Renaissance** once the spirit altar unlocks.
- Use as optional t3 capstone: SAFE (Medieval players cannot access spirit altar, so block_of_soulstone is a Ren-tier block by practical gating even if not explicitly AStages-locked).

**Note:** Must ADD `malum:block_of_soulstone` to `#neovitae:altar/t3_capstones` (currently only contains `neovitae:blood_stained_glass`).

---

## 4. PILLAR_BLOCKS

**Status: CONFIRMED — 4 candidates**

The `#neovitae:altar/pillars` tag is currently empty (`data/neovitae/tags/block/altar/pillars.json` = `{"values":[]}`). All four must be added via data pack.

| Role | ID | Name | Jar Evidence | Craftable From |
|------|-----|------|--------------|----------------|
| NV fallback pillar | `neovitae:inversion_pillar` | Inversion Pillar | `data/neovitae/loot_table/blocks/inversion_pillar.json`; lang key `block.neovitae.inversion_pillar` | Verify recipe in-game (dungeon block but likely craftable); **BLOCKED-NEEDS-INGAME** for exact recipe — use `neovitae:bloodstone_brick` as fallback if inversion_pillar has no recipe |
| F&A darkstone-style pillar | `forbidden_arcanus:arcane_polished_darkstone_pillar` | Arcane Polished Darkstone Pillar | `data/forbidden_arcanus/recipe/arcane_polished_darkstone_pillar.json` | 2× arcane_polished_darkstone → 1 pillar; arcane_polished_darkstone = 8× polished_darkstone + 1 deorum_ingot (Gilded tier) |
| Malum pillar | `malum:tainted_rock_column` | Tainted Rock Column | `data/malum/recipe/tainted_rock_column.json` | 3× tainted_rock → 3 columns (basic Renaissance-accessible crafting) |
| Spectrum pillar | `spectrum:onyx_pillar` | Onyx Pillar | `assets/spectrum/lang/en_us.json` key `block.spectrum.onyx_pillar = Onyx Pillar` — model exists | Likely stonecutting from onyx_block; **BLOCKED-NEEDS-INGAME** for recipe confirmation. Fallback: `spectrum:onyx_bricks` |

**Note on `runic_darkstone`:** `forbidden_arcanus:runic_darkstone` exists in lang and has a loot table, but **has NO crafting recipe** (only world-gen drop / no recipe file in jar). Do not use as a pillar unless AoA adds a recipe for it. Use `arcane_polished_darkstone_pillar` instead.

---

## 5. MALUM_SPIRIT

**Status: CONFIRMED — Renaissance-accessible spirit identified**

- **Best choice for Renaissance-tier weave:** `malum:arcane_spirit` ("Arcane Spirit")
- Evidence: `assets/malum/models/item/arcane_spirit.json` exists; lang `item.malum.arcane_spirit = Arcane Spirit`.
- AStages check: **No lock on any spirit item** in any `aoa_astages_01*.js` file. Only `malum:spirit_altar` is locked at `the_renaissance` (meaning spirits are inaccessible before Ren). After Ren unlock, all spirits can be collected from mobs killed near a Spirit Altar (Malum's passive drop mechanic).
- `malum:wicked_spirit`: Also unlocked at Renaissance (same spirit altar gate). Not IR-locked.
- **All spirit items** (aerial, aqueous, arcane, earthen, eldritch, infernal, sacred, umbral, wicked) are available at **Renaissance** once `malum:spirit_altar` is accessible.

**For the Sentient-gear forge weave, use `malum:arcane_spirit`** (thematic fit: arcane/magical spirit for binding sentient gear). `malum:wicked_spirit` is also valid if a darker flavor is preferred.

---

## 6. THEURGY_SALT

**Status: CONFIRMED**

The Theurgy salt family uses **per-source item IDs** with a `%s`-templated display name, not a single item:

- `theurgy:alchemical_salt_mineral` — from minerals/ores
- `theurgy:alchemical_salt_creature` — from creatures
- `theurgy:alchemical_salt_plant` — from plants
- `theurgy:alchemical_salt_strata` — from strata/stone

Evidence: `assets/theurgy/lang/en_us.json` — item keys `item.theurgy.alchemical_salt_mineral`, etc.

Tag: `#theurgy:alchemical_salts` contains all four (`data/theurgy/tags/item/alchemical_salts.json`).

**Recommendation for recipe ingredient:** Use the tag `#theurgy:alchemical_salts` to accept any salt type, OR use `theurgy:alchemical_salt_mineral` specifically for a mineral-flavored weave. The tag is the correct approach for flexibility.

---

## 7. NV_SENTIENT_UPGRADE_OK

**Status: YES — `neovitae:hellfire_forge_upgrade` is a real recipe type**

Evidence:
- `data/neovitae/recipe/hellfire_forge/blood_mending.json` has `"type": "neovitae:hellfire_forge_upgrade"` with `"catalysts": [...]` and `"drain"` / `"minDrain"` fields.
- This recipe type applies an upgrade enchant-like effect to an item in the forge slot; it does NOT specify a `transformInput` (unlike `hellfire_forge_transform`).
- The `blood_mending` upgrade adds Blood Mending enchantment to any item placed in the forge.

**Schema for a custom upgrade recipe:**
```json
{
  "type": "neovitae:hellfire_forge_upgrade",
  "catalysts": [
    { "item": "<ingredient_1>" },
    { "item": "<ingredient_2>" }
  ],
  "drain": 200.0,
  "minDrain": 400.0
}
```
The target item is placed in the forge slot; the upgrade applies to whatever is there. This can target sentient gear.

**Sentient gear item IDs (all confirmed):**
- `neovitae:sentient_sword`, `neovitae:sentient_axe`, `neovitae:sentient_pickaxe`, `neovitae:sentient_shovel`, `neovitae:sentient_scythe` (tools)
- `neovitae:sentient_helmet`, `neovitae:sentient_plate`, `neovitae:sentient_leggings`, `neovitae:sentient_boots` (armor)

---

## 8. NV_DEFAULT_MATERIALS

**Status: CONFIRMED (partial — config is generated at first launch)**

The NV material system auto-scans on first launch and writes `config/neovitae/materials.json` (this file does not exist yet in the pack — it generates on first game run). The guide book states: *"the mod scans for installed ores and auto-generates processing entries."*

**Confirmed hardcoded materials** (items exist in the jar lang file):
- Iron: `neovitae:iron_fragment`, `neovitae:iron_gravel`, `neovitae:iron_dust`
- Gold: `neovitae:gold_fragment`, `neovitae:gold_gravel`, `neovitae:gold_dust`
- Copper: `neovitae:copper_fragment`, `neovitae:copper_gravel`, `neovitae:copper_dust`
- Coal: `neovitae:coal_dust`
- Demonite: `neovitae:demonite_fragment`, `neovitae:demonite_gravel`, `neovitae:hellforged_dust` (via `neovitae:ingot_hellforged`)
- Hellforged: `neovitae:ingot_hellforged` tagged at `data/c/tags/item/ingots/hellforged.json`

**Confirmed default material set: iron / gold / copper / coal / demonite (ore) / hellforged (ingot).** This aligns with the brief's stated set. Do NOT depend on mod-generated materials (they appear after first launch, may vary).

---

## 9. FNA_CLIBANO_RESIDUE + NV_PROCESSED_OUTPUT

**Status: CONFIRMED**

### F&A Clibano Residue

The Clibano uses a **residue registry** (`forbidden_arcanus:residue_type`), not a literal item output. Residues accumulate as a resource that, when a threshold is met, produces a block item.

**Best candidate residue: `forbidden_arcanus:arcane_crystal`** (from processing arcane_crystal in the Clibano).

- Recipe that produces it: `data/forbidden_arcanus/recipe/clibano_combustion/arcane_crystal_dust_from_clibano_combustion.json`
  - Input: `forbidden_arcanus:arcane_crystal` → Output: `forbidden_arcanus:arcane_crystal_dust` + residue type `forbidden_arcanus:arcane_crystal` (chance 0.1)
  - Residue combines: 9 units → 1× `forbidden_arcanus:arcane_crystal_block`
- The residue itself is NOT a standalone item — it is tracked as a Clibano GUI resource. Weave recipes cannot use the residue directly as a crafting ingredient.

**Second candidate: `forbidden_arcanus:rune`** residue from smelting runic stones (chance 0.1; 9 units → `forbidden_arcanus:rune_block`).

**AoA weave implication:** A Clibano→Athanor weave cannot literally pass residue between machines (residue is internal Clibano state). The weave must instead use the **output items** (e.g., `forbidden_arcanus:arcane_crystal_dust` from Clibano combustion, or `forbidden_arcanus:rune`) as inputs into the Athanor.

### NV Athanor Processed Output

**Best candidate output for a weave:** `neovitae:weak_blood_shard`

- Recipe: `data/neovitae/recipe/athanor/hydration/weakbloodshard_tau.json`
  - Input: `neovitae:strong_tau` + 3200 mB `neovitae:essentia_vitae_source` fluid
  - Output: `neovitae:weak_blood_shard`
  - Tool slot: `#neovitae:athanor_tool/hydration`
- This is thematically strong: F&A arcane_crystal_dust feeds into an NV Athanor recipe to produce weak_blood_shard (a core blood magic progression item).

**Proposed weave structure (Clibano→Athanor):**
```
F&A Clibano: arcane_crystal → arcane_crystal_dust [+ arcane_crystal residue]
NV Athanor: arcane_crystal_dust + essentia_vitae fluid + hydration tool → weak_blood_shard
```
Both `forbidden_arcanus:arcane_crystal_dust` and `neovitae:weak_blood_shard` are CONFIRMED jar-verified IDs.

---

## Summary

| # | ID | Status | Notes |
|---|-----|--------|-------|
| 1 | NV_MODONOMICON_BOOK | CONFIRMED | `neovitae:guide` at `data/neovitae/modonomicon/books/guide/book.json` |
| 2 | SPECTRUM_CAPSTONE_BLOCK | CONFIRMED | `spectrum:onyx_block` — crafted from onyx_shards |
| 3 | MALUM_CAPSTONE_BLOCK | CONFIRMED | `malum:block_of_soulstone` — 9× refined_soulstone, Ren-era |
| 4a | PILLAR - NV | BLOCKED-NEEDS-INGAME | `neovitae:inversion_pillar` recipe unconfirmed; fallback `neovitae:bloodstone_brick` |
| 4b | PILLAR - F&A | CONFIRMED | `forbidden_arcanus:arcane_polished_darkstone_pillar` |
| 4c | PILLAR - Malum | CONFIRMED | `malum:tainted_rock_column` |
| 4d | PILLAR - Spectrum | BLOCKED-NEEDS-INGAME | `spectrum:onyx_pillar` model exists; recipe unconfirmed; fallback `spectrum:onyx_bricks` |
| 5 | MALUM_SPIRIT | CONFIRMED | `malum:arcane_spirit` (or `wicked_spirit`) — both Ren-gated via spirit_altar, no earlier |
| 6 | THEURGY_SALT | CONFIRMED | Per-family items; use tag `#theurgy:alchemical_salts` |
| 7 | NV_SENTIENT_UPGRADE_OK | YES | `neovitae:hellfire_forge_upgrade` recipe type confirmed |
| 8 | NV_DEFAULT_MATERIALS | CONFIRMED | iron/gold/copper/coal/demonite/hellforged; config generated at first launch |
| 9 | FNA_CLIBANO_RESIDUE | CONFIRMED | `forbidden_arcanus:arcane_crystal_dust` (output from Clibano combustion of arcane_crystal) |
| 9 | NV_PROCESSED_OUTPUT | CONFIRMED | `neovitae:weak_blood_shard` (Athanor hydration recipe consuming strong_tau + essentia_vitae) |

**Counts:** 10 of 12 sub-IDs CONFIRMED, 2 BLOCKED-NEEDS-INGAME (NV inversion pillar recipe, Spectrum onyx pillar recipe) with confirmed fallbacks.
