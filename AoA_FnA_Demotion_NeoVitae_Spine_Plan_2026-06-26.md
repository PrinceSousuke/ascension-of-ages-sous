# AoA — Demote Forbidden & Arcanus, Adopt Neo Vitae as Magic Spine

Plan date: 2026-06-26. Status: APPROVED-IN-PRINCIPLE, pre-implementation. Author: senior-dev pass with verified research.

This is a planning runbook, not final recipes. Every JSON block below is built on a VERIFIED Neo Vitae schema (recipe types and fields confirmed from the mod wiki source). Item IDs flagged `[jar-verify]` must be confirmed by cracking the jar before they go live. The user is strict about not shipping invented IDs, so respect those flags.

---

## 1. The decision (locked 2026-06-26)

1. Forbidden & Arcanus comes OFF the core magic spine. It is not removed. Useful pieces stay as woven supporting content and the known annoyances get patched down.
2. Neo Vitae becomes the new core magic spine, spanning the_renaissance through otherworldly (five ages).
3. Both Neo Vitae dungeon sub-zones are integrated (Antechamber + Endless Realm in the single `neovitae:dungeon` dimension).

New magic spine after this change: Spectrum + Neo Vitae as the two main pillars, with Malum, Occultism, and Theurgy as required-supporting weave. This supersedes the "Spectrum + F&A = main spine" line in the magic-pillar-canon memory once executed.

---

## 2. Verified facts that adjust earlier assumptions

These are corrections found during research. Read them before planning around old assumptions.

- The divisive "deciphering / research-table RNG" people complain about is OLD 1.16 F&A. It is GONE from the 2.6.1 build in this pack. The real current pain is the Soul Looting RNG entry gate and the Black Hole item-deletion hazard. Conclusion (demote from core) is still community-supported, just for different reasons than originally thought.
- "No one likes this mod" is false. Verified consensus: players like the aesthetics (Darkstone, Edelwood), the Clibano (zero complaints found), the Hephaestus Forge as an Eternal Stella / Indestructible endgame hook, and QoL trinkets (Obsidian Skull, Spectral Eye, Quantum Catcher). They dislike the grind to REACH the Forge.
- Neo Vitae does NOT world-generate overworld ores. `config/neovitae/materials.json` is a processing-chain layer that absorbs existing `c:ores/*` tags and auto-generates fragment/gravel/dust + Athanor recipes. The only true ore generation is inside the dungeon (Demonite / Prismatic Demonite, controlled by a room `oreDensity` field). The span Ren->Otherworldly is still justified by the Athanor processing tiers plus the dungeon material gates (Tau Fruit, Bloodstone, Hellforged, Crystal Clusters), not by overworld ore spawns.
- "Demon Realm + Endless Dungeon" is one dimension: `neovitae:dungeon`. The Antechamber is reached by the Tier-2 ritual "Breaching the Edge of Demon Realm"; the persistent Endless Realm by the Tier-3 ritual "Highway to Hell". Treat it as one dimension with two access gates.
- Altar tier geometry and capstone blocks are data-driven. Tier shapes live in `data/neovitae/neovitae/altar_tier/`, and capstone blocks resolve against block tags `#neovitae:altar/t3_capstones` through `t6_capstones`. This means cross-mod blocks can be made into valid altar capstones by retagging, with zero Java. This is the single most powerful weave lever in the mod.

---

## 3. F&A footprint that must be rewired (verified on-disk)

22 required + 16 optional F&A task entries across 7 chapters. No OTHER chapter references F&A quest node-ids, so the rewire is contained. Four anchors are load-bearing:

| # | Anchor | Location | Why it blocks |
|---|--------|----------|---------------|
| A1 | Renaissance "Frontier" capstone aggregator `0B0310100000CAFE` all-AND depends on F&A `arcane_bone_meal` node `0B03101000000039` | `config/ftbquests/quests/chapters/ren_magic_foundations.snbt` | The Renaissance progression advancement cannot be earned without the F&A arcane_crystal -> clibano line (interleaved with `malum:runic_workbench`). |
| A2 | Oritech `foundry_block` recipe hard-requires F&A `deorum_ingot` | `kubejs/server_scripts/ir_native_capstone_recipes.js` (recipe id `aoa:ir_magic_feedstock/aureal_foundry`) | Tech progression gated on an F&A ingot. |
| A3 | Oritech `machine_core_5` recipe hard-requires F&A `deorum_ingot` | `kubejs/server_scripts/magic_spine_bridges.js` (recipe id `aoa:magic_spine/oritech_machine_core_5`) | Same, alongside `malum:hallowed_gold_ingot` + `theurgy:mercury_catalyst`. |
| A4 | Hephaestus Forge Tier-3 ritual override forces `malum:spirit_jar` | `kubejs/data/forbidden_arcanus/forbidden_arcanus/hephaestus_forge/ritual/upgrade_tier_3.json` | Only matters if the Forge stays on a required path. It will not, so this becomes optional. |

Staging lives in `kubejs/server_scripts/aoa_astages_01m_magic.js` (header lists forbidden_arcanus, theurgy, occultism, spectrum, malum, actuallyadditions, psi).

---

## 4. F&A keep / cut / patch matrix

| Piece | Verdict | Action |
|-------|---------|--------|
| Darkstone + Edelwood decoration blocks | KEEP unlocked | Per dont-lock-decor-mods canon, no gating. |
| Clibano multiblock | KEEP as optional early-mid ore bonus | Re-home as an optional Renaissance ore-processing companion to the Athanor. Liked, zero complaints. |
| Hephaestus Forge (+ Eternal Stella / Indestructible) | KEEP as optional late reward | Move to an optional Gilded/Atomic gear-finishing lane. Off the required path. |
| Obsidian Skull, Spectral Eye, Quantum Catcher | KEEP as optional QoL | Craftable, no progression gate. |
| Soul Looting entry gate | PATCH | Make the enchantment / Lost Soul deterministically obtainable (grant via quest reward or add a craftable enchanted book). Removes the soft-lock. |
| Black Hole hazard (Dark Matter + Corrupti Dust) | PATCH | Config-disable the accidental black-hole creation, or provide an alt Xpetrified Orb recipe so nothing depends on the hazard. |
| Aureal obelisk bottleneck | DROP from required path | Was only painful when required. Now optional, so leave as-is. |
| arcane_bone_meal / arcane_crystal / clibano required ladder | DEMOTE to optional | These nodes lose their `dependencies` role in the capstone (see Section 6 rewire). |
| Tyr / Draco / Mortem armor, Arcane Obelisk, soul-line, 16 optional tasks | KEEP optional | Already `optional:true`, no dependency touches them. No action. |

---

## 5. Neo Vitae age-spine distribution (Renaissance -> Otherworldly)

Mapping verified altar tiers, orb caps, and material gates onto the five ages. EV caps and gates are VERIFIED; orb registry IDs are `[jar-verify]`.

| Age | Altar tier | Orb (Anima cap) | Headline unlock | Dungeon | Material / Athanor layer | Cross-mod weave anchor |
|-----|-----------|-----------------|-----------------|---------|--------------------------|------------------------|
| the_renaissance | T0 -> T1 (0 -> 8 runes) | Novicius 5k, Discipulus 25k | Place Ara Vitae, bind first orb, self-sacrifice, first sigils (Blood Light, Magnetism), Tabula Vitae basics | none yet | Athanor T1: basic ore fragment/dust on early `c:ores/*` | New Ren magic capstone tail = Ara Vitae T1 (replaces F&A). Malum soulstone feeds reagents. |
| industrial_revolution | T2 (24 runes) | Veneficus 150k | Hellfire Forge activation, first Sentient weapon, Spiritus aspects, ritual "Breaching the Edge" -> Antechamber | Antechamber (limited) | Athanor mid: cutting-fluid / explosive tools; Tau Fruit appears | Theurgy mercury as Athanor fluid; Occultism summon as alt dungeon key. |
| gilded_age | T3 (52 runes, Bloodstone caps) | Magus 1M | "Highway to Hell" -> Endless Realm, The Foreman boss -> Mines, Demonite ore, Sentient armor tree, Routing Network automation | Endless Realm + Mines | Bloodstone (Weak Blood Shard from Saturated Tau) | Make a Malum/Occultism block a valid `t3_capstones` block (block-tag weave). |
| atomic | T4 (100 runes, Hellforged caps) | Dominus 5M | Deep mines, Hellforged materials, advanced Sentient gear, Spiritus crystal farming, alchemy arrays at scale | deep Mines | Hellforged Block chain | Optional F&A Hephaestus Forge finishing (Eternal Stella on Sentient gear). |
| otherworldly | T5 (172 runes, Crystal Cluster caps) | Divinus 10M | Full Sentient armor set, Crystal Clusters (Sculk + Nether Star), capstone rituals, Endless Realm deep loop as lateral endgame | Endless Realm endgame | Crystal Cluster Bricks | Spectrum light/ink into endgame alchemy arrays; feeds Ascension. |

Notes. T5 needs a Nether Star, trivially available by Otherworldly. The Foreman (600 HP Daemonium Doloris variant) is a clean candidate for a Gilded or Atomic boss-proof. The dungeon's lateral endgame loop fits Otherworldly without competing with the Ascension capstone.

---

## 6. Rewiring the four anchors (concrete)

A1, capstone tail swap. In `ren_magic_foundations.snbt`, repoint the Frontier aggregator dependency `0B0310100000CAFE` away from F&A node `0B03101000000039` (arcane_bone_meal) and onto a new Neo Vitae node, for example "Build Ara Vitae Tier 1 and bind a Novicius Orb". The F&A arcane_crystal -> clibano ladder stays in the file but becomes `optional:true` with its dependency edges to the capstone removed. This keeps F&A content visible and rewarding without it being load-bearing.

A2 + A3, re-source the Oritech ingot. Change the two recipes so they no longer hard-require `forbidden_arcanus:deorum_ingot`. Two clean options:
- Spine-native swap: use `malum:hallowed_gold_ingot` (already present in `machine_core_5`) or a verified Neo Vitae ingot `[jar-verify]` as the magic-ingredient. Keep `deorum_ingot` as an OPTIONAL alternate recipe so F&A players still have a use for it.
- Tag swap: define an `aoa:magic_feedstock_ingot` item tag containing deorum_ingot + the Neo Vitae/Malum equivalent, and have the recipe accept the tag. Most future-proof.

A4, neutralize the Forge ritual coupling. Since the Hephaestus Forge moves to an optional reward lane, leave `upgrade_tier_3.json` in place but make sure nothing required depends on reaching Forge T3. If you want to fully decouple, delete the override and let the Forge use its default tier-3 ritual.

---

## 7. Cross-mod weave catalog (real schema, example JSON)

The magic cluster already cross-weaves F&A/Malum/Occultism/Theurgy/Spectrum in `aoa_recipes_renaissance_weaves.js`. These weaves make Neo Vitae the hub they hang off. Recipe `type` values and fields are VERIFIED from the wiki. Cross-mod item IDs (malum:, occultism:, theurgy:) are VERIFIED from the on-disk weave scripts. Neo Vitae item IDs marked `[jar-verify]`.

### Weave 1 — Soulbound Capstone (Malum/Occultism -> altar, block-tag weave)
The strongest weave, zero recipe needed. Make a Malum or Occultism block a valid Tier-3 altar capstone by adding it to the capstone tag. Player must integrate Malum/Occultism to physically grow the altar.

`data/neovitae/tags/block/altar/t3_capstones.json`
```json
{
  "replace": false,
  "values": [
    "malum:block_of_soulstone",
    "occultism:otherstone"
  ]
}
```
Status: mechanism VERIFIED (tag-driven capstones). Confirm exact malum/occultism block IDs `[jar-verify]`.

### Weave 2 — Mercurial Athanor (Theurgy -> Athanor processing)
Use Theurgy mercury as the Athanor fluid so the alchemy and blood lines share plumbing.

`data/aoa/recipe/athanor/mercurial_iron.json`
```json
{
  "type": "neovitae:athanor",
  "input": { "tag": "c:ores/iron" },
  "tool": { "tag": "neovitae:athanor_tool/cutting_fluids" },
  "output": { "id": "neovitae:iron_fragment", "count": 3 },
  "inputFluid": { "id": "theurgy:mercury", "amount": 100 },
  "addedOutput": [
    { "item": { "id": "theurgy:mercury_shard" }, "chance": 0.25 }
  ]
}
```
Status: schema VERIFIED. Confirm `theurgy:mercury` fluid id + `mercury_shard` item id (Theurgy is on-disk, verify exact IDs).

### Weave 3 — Demon Pact key (Occultism -> dungeon access)
Give players who built the Occultism summoning chain an alternate route to the dungeon, so the two demon-themed mods reinforce each other. Implement as a Hellfire Forge recipe producing the dungeon-access reagent from an Occultism summon item.

`data/aoa/recipe/hellfire_forge/pact_key.json`
```json
{
  "type": "neovitae:hellfire_forge",
  "ingredients": [
    { "item": "occultism:datura" },
    { "item": "neovitae:weak_blood_shard" }
  ],
  "result": { "id": "neovitae:inversion_focus", "count": 1 },
  "minimumSouls": 64,
  "soulDrain": 16
}
```
Status: schema VERIFIED (hellfire_forge fields confirmed). `neovitae:inversion_focus` and `weak_blood_shard` are `[jar-verify]` (weak_blood_shard appears in the wiki example, the access item name is a guess).

### Weave 4 — Light into Life (Spectrum -> alchemy array sigil)
Spectrum pigment as the catalytic added_input for an endgame sigil, tying the two main pillars together at Otherworldly.

`data/aoa/recipe/array/radiant_air_sigil.json`
```json
{
  "type": "neovitae:alchemy_array",
  "base_input": { "item": "neovitae:arcane_ash" },
  "added_input": { "item": "spectrum:vibrant_ink" },
  "result": { "id": "neovitae:air_sigil" }
}
```
Status: schema VERIFIED. Confirm a real Spectrum pigment/ink id `[jar-verify]` (Spectrum is on-disk).

### Weave 5 — Salvaged Forge finish (F&A kept, optional)
Keep the Hephaestus Forge relevant by letting it apply Eternal Stella / Indestructible to a Neo Vitae Sentient tool as an optional Atomic-age reward. Implement at the F&A side (Hephaestus Forge recipe JSON in the `forbidden_arcanus` namespace) consuming a Sentient tool + eternal_stella. Keeps the liked Forge endgame without it gating anything.
Status: design-level. Confirm F&A Hephaestus Forge recipe schema before authoring.

### Weave 6 — Reagent retune for the age economy (datapack tuning)
Use the verified data maps to make high-tier rituals fit AoA's pacing and to disable rituals you do not want.

`data/neovitae/data_maps/neovitae/ritual/ritual_stats.json`
```json
{
  "values": {
    "neovitae:suffering": { "activation_cost": 50000, "refresh_cost": 2, "refresh_time": 25, "crystal_level": 0 },
    "neovitae:some_unwanted_ritual": { "enabled": false }
  }
}
```
Status: schema VERIFIED. Confirm ritual IDs `[jar-verify]`.

---

## 8. Datapack customization levers (why Neo Vitae beats F&A here)

- Altar tiers: `data/neovitae/neovitae/altar_tier/altar_<one..six>.json` reshape geometry; capstone block tags `#neovitae:altar/t3_capstones..t6_capstones` retag what counts. Cross-mod weaving with no Java.
- Recipes: every machine is JSON (`neovitae:ara_vitae`, `hellfire_forge`, `tabula_vitae`, `athanor`, `alchemy_array`, `flask`, `living_downgrade`). Full control of costs (totalBlood, lpDrained, minimumSouls) and tier gates (minTier).
- Data maps: `ritual_stats`, `sigil_stats`, `blood_orb_stats`, `spiritus_gem_max` retune costs/ranges and enable/disable content.
- Materials: `config/neovitae/materials.json` controls the entire processing chain and which ores feed it. Add or restage materials per age via the `c:ores/*` tags you already gate in `aoa_astages_06_ore_restrictions.js`.
- Lore: Scriptura Vitae is Modonomicon (already in the pack). Override altar multiblock previews at `data/neovitae/modonomicon/multiblocks/altar_<one..six>.json`. Book entry content is data-driven JSON.
- KubeJS event hooks (VERIFIED class paths) for dynamic behavior, e.g. bonus altar output at tier >= 3 via `com.breakinblocks.neovitae.common.event.AraVitaeCraftEvent$Crafting`. Useful for cross-mod reactive weaves the JSON recipes cannot express.

---

## 9. Open items / jar-verify checklist (do before authoring final JSON)

1. Orb registry IDs: wiki narrative uses Latin names (Novicius..Divinus) but a data-map example uses `weak_blood_orb`/`apprentice_blood_orb`. Crack `data/neovitae` or the item registry to get the real IDs.
2. Modonomicon book ID for Scriptura Vitae (likely `neovitae:scriptura_vitae`, unconfirmed).
3. Default `materials.json` contents (run `/neovitae generate-materials` on a test world, capture the file).
4. Exact dungeon-access item / reagent name used in Weave 3.
5. Hellforged Block exact recipe chain (Demonite -> Hellforged), check JEI in-game.
6. GeckoLib presence in mods/ (required dep). Modonomicon confirmed present. Curios optional, likely present.
7. KubeJS recipe builder signatures if you prefer scripts over JSON (undocumented in wiki, check the jar's KubeJS plugin or the NeoVitae Discord).

---

## 10. Implementation sequence (phased)

Phase 0, intake and verify. Add Neo Vitae + GeckoLib to mods/. Generate a test world, run `/neovitae generate-materials`, crack the jar for the seven items in Section 9. Capture real IDs.

Phase 1, staging. Add Neo Vitae items/blocks to the magic cluster staging across the five ages in `aoa_astages_01m_magic.js` (and a dungeon-access gate). Confirm its ores ride the existing `c:ores/*` gates.

Phase 2, F&A rewire + patches. Execute the four anchor rewires (Section 6) and the two annoyance patches (Soul Looting, Black Hole). Re-run the gate audit.

Phase 3, quest authoring. Rebuild `ren_magic_foundations` around the Ara Vitae as the Renaissance magic capstone tail. Add IR/Gilded/Atomic/Otherworldly magic chapters tracking the tier ladder. Demote F&A quests to optional.

Phase 4, weaves. Land Weaves 1 through 6 as datapack JSON + KubeJS where needed.

Phase 5, lore + capstones. Scriptura Vitae entries / overrides, capstone block retags, Foreman boss-proof wiring.

Phase 6, verify. Gate audit, machine-graph softlock pass, FTBQ node check, JEI sanity, test-world playthrough of the tier ladder.

---

## 11. Delegation prompts (complementary: Codex cracks/scaffolds, Claude Code rewires)

### Codex — schema extraction + datapack scaffold (good at exhaustive file/jar work)
"Crack `mods/neovitae-1.21.1-1.0.24.jar` for the Ascension of Ages pack. Extract and report, with exact strings: (1) the item registry IDs for all six Orbs of Vitae; (2) the Modonomicon book ID and book JSON path; (3) the shipped `config/neovitae/materials.json` default (or the datagen that produces it); (4) the Demonite -> Hellforged Block recipe chain; (5) the dungeon-access reagent item ID; (6) any KubeJS recipe builder method signatures. Then scaffold (do not finalize) the six cross-mod weave JSON files from `AoA_FnA_Demotion_NeoVitae_Spine_Plan_2026-06-26.md` Section 7, substituting the real IDs you found and leaving a `// VERIFY` comment on anything you could not confirm. Do not edit any .snbt or KubeJS files. Output a diff-ready file tree."

### Claude Code — F&A anchor rewire + annoyance patches (good at careful in-repo edits)
"In the Ascension of Ages pack, execute the four F&A anchor rewires and two patches from `AoA_FnA_Demotion_NeoVitae_Spine_Plan_2026-06-26.md` Sections 3-6. Specifically: (A1) in `ren_magic_foundations.snbt`, repoint Frontier aggregator `0B0310100000CAFE` off F&A node `0B03101000000039` onto a new Ara-Vitae-T1 node, and set the F&A arcane_crystal/clibano ladder to optional with no edges into the capstone; (A2/A3) change recipes `aoa:ir_magic_feedstock/aureal_foundry` and `aoa:magic_spine/oritech_machine_core_5` to accept a new `aoa:magic_feedstock_ingot` tag instead of hard-requiring `forbidden_arcanus:deorum_ingot`, keeping deorum as an optional tag member; (A4) confirm nothing required depends on Hephaestus Forge T3; patch Soul Looting to be deterministically obtainable and config-disable the Black Hole hazard. Preserve CRLF and snbt formatting. Re-run `aoa_gate_audit.py` and report softlocks. Make zero changes outside the listed files without flagging."

---

## 12. Risk notes

- Neo Vitae is on near-daily releases (1.0.24 shipped 2026-06-25). Pin a version and re-test on bumps; data-map and recipe schemas could shift.
- The single-dimension reality (`neovitae:dungeon`) means the Antechamber and Endless Realm share a dimension. If AoA dimension canon wants them separate, that is a Java-level change, not datapack. Recommend accepting the single dimension.
- Custom NEW dungeon rooms need a one-line Java registration; pure datapack can only re-skin existing pools. If bespoke rooms are wanted, that is a small addon, not a datapack.
- Spanning five ages is the most content of the three placement options. Author depth-per-tier, do not pad to hit a number (quality-over-quantity canon).
