# H2 — Mid-game progression critique: Industrial Revolution + Gilded Age

Audit only. No files edited outside phase0/. No git. Every finding carries a proof command + file.

Scope: 9 IR chapters + 7 Gilded chapters (group ids `3F77A31B7D30C0AA` / `5E42E6B4A7C91D30`),
prose from `config/ftbquests/quests/lang/en_us.snbt`, weave scripts under `kubejs/server_scripts/`.

Severity legend: SOFTLOCK > BROKEN > CANON > HYGIENE.

---

## Verdict up front

The **domain-proof spine is clean and complete for BOTH ages** — this is the strongest part of
the mid-game. Every one of the 6 IR proofs and 8 Gilded proofs is granted by a live quest and
fans into a single age-grant capstone with no bypass. The problems are in **mod-lane balance**
(Mekanism base has no mid-game home; Industrial Foregoing is over-quested into filler) and **one
woven recipe with no quest teaching it in its age**. No new cross-age inversion found; entry gates
resolve correctly.

---

## Lens 1 — Domain-proof spine (VERIFIED clean)

### IR: 6 proofs → single `gilded_age` grant

Fan-in node **`4954631000000000`** in `ir_netherite_citadel_obsidilith.snbt` carries
`/astages add {p} ir_capstone_complete`, `gilded_age`, `aoa:age/gilded_age`. Its `dependencies`
are exactly the 6 proof-grant nodes:

| IR proof | Grant node | Chapter |
|---|---|---|
| ir_factory_discipline_complete | `4954021000000016` | ir_modern_industrialization_steam_industry |
| ir_power_motion_complete | `4954051000000011` | ir_power_motion_and_grid |
| ir_pressure_chemistry_entry_complete | `495406100000001D` | ir_pneumaticcraft_pressure_plastic |
| ir_digital_logistics_complete | `49540A100000000F` | ir_automation_safety_and_routing |
| ir_magic_feedstock_complete | `49540B1000000015` | ir_magic_feedstock_and_spectrum_network |
| obsidilith_defeated | `49540C1000000006` | ir_netherite_citadel_obsidilith |

Proof: `grep -A2 '"4954631000000000"' ir_netherite_citadel_obsidilith.snbt` shows deps
`[4954021000000016, 49540A100000000F, 49540B1000000015, 49540C1000000006, 4954051000000011, 495406100000001D]`
and the five command rewards. All 6 dep nodes independently confirmed to carry their `/astages add`.
**No missing fan-in.** `ir_capstone_complete` is granted only here.

### Gilded: 8 proofs → single `atomic` grant

Fan-in node **`5057011000000004`** in `g_power_beyond_wires.snbt` carries
`/astages add {p} atomic` + `aoa:age/atomic`. Its 7 deps + one bundled proof cover all 8:

| Gilded proof | Grant node | Chapter |
|---|---|---|
| g_advanced_applied_industry_complete | `4D4F011000000005` | g5_empire_of_iron |
| g_scaled_logistics_computation_complete | `4D4E011000000006` | g4_the_infinite_grid |
| g_nautec_oceanic_industry_complete | `4D50011000000003` | g6_circuits_and_current |
| g_atomic_license_complete | `4F47011000000002` | g6_circuits_and_current |
| g_biotech_hazard_readiness_complete | `5246011000000007` | g2_the_refinery |
| g_magic_authorization_complete | `4341011000000004` | g7_chartered_arcana |
| g_temporal_authorization_complete + void_titan_defeated | `5057011000000003` | g_power_beyond_wires |

Proof: `grep -A2 '"5057011000000004"'` shows deps
`[4D50011000000003, 5246011000000007, 5057011000000003, 4D4E011000000006, 4D4F011000000005, 4F47011000000002, 4341011000000004]`.
`void_titan_defeated` and `g_temporal_authorization` are both granted on `5057011000000003` (one node),
which is a dep of the atomic grant. **All 8 proofs fan in. `atomic` is granted only here.** This is the
reference-quality invariant the capstone-fan-in fix (memory 2026-06-22) was meant to guarantee — it holds.

**Note (CANON, low):** g6 owns TWO proofs (`nautec` + `atomic_license`). Structurally fine (both fan in
independently), but it means the "atomic license" domain has no chapter of its own — it rides inside the
oceanic-industry chapter. Acceptable, worth an explicit canon note so a future editor doesn't "split" it.

---

## Lens 2 — Intra-age ordering + entry gates (SANE, one note)

Entry topology (external deps resolved to their source file):

- **IR opens on the Renaissance capstone** `0B0310A0000000F0` (= `ren_maledictus_vigil.snbt`). Three
  IR chapters root directly on it in parallel: IE early-factory (`4954011000000001`), MI steam
  (`4954021…`), Power/grid (`4954051…`). IE early-factory is the de-facto trunk — `ir_automation`,
  `ir_create_addons`, and the citadel all dep `4954011000000001`.
- IE early-factory also has backward deps into `metallurgy.snbt` (Medieval) and one into
  `stone_food_and_farming_pressures.snbt` (Dark Ages, node `11C25203906C0FD4`). Backward deps are
  canon-legal; no inversion (earlier age feeding later). Verified via
  `grep -rl 'id: "<dep>"'` for each — all resolve to Medieval/Renaissance/Dark, never a later age.
- `ir_pneumaticcraft` gates behind `ir_power_motion` (dep `4954051000000025`) — sensible: pressure
  chemistry wants power first.
- `ir_magic_feedstock` gates behind `ir_automation` digital-logistics grant (`49540A100000000F`) plus
  two Renaissance magic nodes — sensible.
- **Gilded opens on the IR capstone** `4954631000000000`. g1/g4/g5/g6/g7 root on it in parallel;
  g2 gates behind g1 (`4757011020010001`); g_power fans in g2/g4/g5/g6/g7. Clean funnel.

**No chapter frontloads another chapter's output without a dep expressing it** in the cases checked.
The parallel-open model (5 Gilded chapters unlocking at once) is intentional and matches the
"required chapters with optional depth, no N-of-M" canon.

**Ordering note (HYGIENE):** because IE, MI, and Power all open simultaneously at IR entry, a new
player sees three full factory chapters at once with no suggested reading order. Not a defect, but a
"start here" pointer (IE early-factory is the real trunk) would help. Prose-level fix only.

---

## Lens 3 — Mod-lane balance (the real problems)

Task-item namespace census per chapter (top lanes):

| Chapter | Dominant lanes |
|---|---|
| ir_immersive_engineering_early_factory | immersiveengineering:60 (single-mod, fine — deep mod) |
| ir_create_industrial_addons | create_new_age:28, immersivepetroleum:19, createdieselgenerators:17, oreexcavation:13 |
| ir_modern_industrialization_steam_industry | modern_industrialization:74, extended_industrialization:22 |
| ir_power_motion_and_grid | powergrid:37, createaddition:28, electrodynamics:24 |
| ir_pneumaticcraft_pressure_plastic | pneumaticcraft:98 (deep mod, defensible) |
| ir_automation_safety_and_routing | enderio:36, integrateddynamics:17, projectred:27 (spread) |
| ir_magic_feedstock | neovitae:16, occultism:15, spectrum:14, theurgy:11, malum:10 |
| ir_ir_side_gear | arsenal:26, mekanismtools:17, immersiveengineering:15, unusualend:14 |
| g1_the_golden_workshop | aether:22, deep_aether:19, extendedcrafting:10 |
| g2_the_refinery | **industrialforegoing:112 (71 distinct machines)** |
| g4_the_infinite_grid | megacells:40, ae2:14, pneumaticcraft:14, cabletiers:12, expandedae:10 |
| g5_empire_of_iron | modern_industrialization:77, **actuallyadditions:69**, enderio:24 |
| g6_circuits_and_current | oritech:43, extended_industrialization:34, nautec:33, electrodynamics:22 |
| g7_chartered_arcana | theurgy:6, spectrum:4, occultism:3, malum:3 (thin) |
| g_power_beyond_wires | astral_dimension:102 (boss/dungeon chapter — expected) |

### 3a. SOFTLOCK-adjacent CANON: **Mekanism base has NO mid-game home**

Canon §3 baseline states plainly: *"Mekanism (base) starts at industrial_revolution — processing
spine (infuser/enrichment/crusher/PRC/chem)."* On disk, the entire IR+Gilded span references
Mekanism base essentially zero times — only `mekanism:atomic_disassembler` (a tool) shows up.

Proof:
```
grep -roh "mekanism:[a-z_0-9]*" config/ftbquests/quests/chapters/*.snbt | grep -vE "tools|generators" | ...
# by chapter distinct-count:
at4_machine_soul: 88, at2_the_periodic_table: 55, at5_threshold_of_war: 42, at1_nuclear_dawn: 10,
ow5: 8, at3: 2, g6: 1, g_power: 1   (IR chapters: ZERO)
```

The Mekanism ore-tripling/quadrupling processing chain (Enrichment Chamber, Crusher, Purification
Chamber, Metallurgic Infuser, PRC, Chemical Injection/Dissolution, basic Factories) is one of the
single biggest mid-game FOMO showpieces in the modpack, and it is entirely deferred to Atomic. Either
(a) the canon baseline is wrong and Mekanism intentionally debuts at Atomic, or (b) there is a real
lane gap: IR players have no quest introduction to Mekanism processing even though it is stage-legal.
**This needs a canon call.** If Mekanism base is meant to be an IR spine, it deserves a home
(most naturally folded into `ir_modern_industrialization` or a shared "processing" node in
`ir_power_motion`), because leaving the pack's flagship processing mod un-taught for two whole ages is
the biggest under-quested showpiece in the mid-game.

### 3b. CANON/HYGIENE: **Industrial Foregoing over-quested into filler (g2)**

`g2_the_refinery` quests **71 distinct Industrial Foregoing machines across 61 quests**
(`grep -oh "industrialforegoing:[a-z_0-9]*" g2_the_refinery.snbt | sort -u | wc -l` = 71). This is the
"quest every machine" anti-pattern. IF is legitimately a Gilded showpiece (whole fleet is stage-legal),
but the chapter nodes the full decor/utility fleet: `animal_baby_separator`, `animal_feeder`,
`animal_rancher`, `block_breaker`, `block_placer`, `fluid_collector`, `fluid_placer`, `fluid_extractor`,
`dye_mixer`, and the four-machine enchantment sub-fleet (`enchantment_applicator/extractor/factory/sorter`).
The FOMO showpieces (laser drill + ore/fluid laser bases, mob_crusher/duplicator, black-hole storage,
bioreactor, material_stonework_factory, infinity tools) carry the chapter; the utility/decor machines are
padding. Recommend trimming the low-signal machines to reward-table drops or bundling variants under one
`ftbfiltersystem:smart_filter` node. Do NOT touch the biotech-hazard proof node (`5246011000000007`).

Corrected note: `industrialforegoing:mycelial_crimed` (node `52460120001C0005`) was previously suspected
phantom (memory: "unresolved 'crimed' item"). It **is a real registered block** — verified in
`unzip -p mods/industrialforegoing-1.21-3.6.38.jar assets/industrialforegoing/lang/en_us.json | grep mycelial_crimed`.
Not a softlock. The memory note should be corrected.

### 3c. HYGIENE: **Actually Additions heavy in g5 (69 refs)**

`g5_empire_of_iron` pairs MI:77 with `actuallyadditions:69`. Actually Additions is a support/utility mod,
not a Gilded showpiece on the scale of MI/EnderIO. 69 references in one chapter is a candidate for
filler review — verify these are meaningful production nodes and not lamp/decor/variant padding. Flagged
for the anti-bloat pass, not a hard defect.

### 3d. Thin but defensible: **g7_chartered_arcana**

Only ~18 magic-item references, 320 lines, 5 authorization quests (4 explicitly "Optional" in prose) +
1 side boss (Umvuthi). Each magic mod (Occultism/Malum/Spectrum/Theurgy) gets 1-2 nodes. The required
capstone is the Spectrum Spirit Instiller (`4341011000000004`). This is the sanctioned
"required-capstone-with-optional-depth" shape, so it is not a defect, but it is the **thinnest required
Gilded domain** and reads as an afterthought next to the 60-100-node industry chapters. If magic
authorization is a true peer domain, it is under-built. Prose is good (instruction-first, no em dashes).

### Well-balanced lanes (no action): AE2/RS in g4 (megacells/ae2/expandedae/extrastorage — the "Infinite
Grid," correctly Gilded not IR), PneumaticCraft in ir_pneumaticcraft (deep single-mod chapter),
Oritech/NauTec in g6, Astral in g_power (boss/dungeon). ProjectRed/Integrated Dynamics/EnderIO carry IR
digital logistics — matches canon (NOT AE2/RS at IR scale). This part of the design is on-philosophy.

---

## Lens 4 — Renaissance/IR boundary: where to host the Deep Dark / Warden IR half

User directive: Deep Dark / Warden content splits late-Ren → early-IR, with echo shards / warden-tier
loot feeding early industry.

Deeper & Darker content on disk today lives in exactly two mid-game chapters:
- `ir_netherite_citadel_obsidilith.snbt` — carries `deeperdarker:warden_helmet/chestplate/leggings/boots`
  and `resonarium_*` armor (proof:
  `grep -oh "deeperdarker:[a-z_0-9]*" ir_netherite_citadel_obsidilith.snbt`).
- `g1_the_golden_workshop.snbt` — a few deeperdarker refs.

**Recommended IR host: `ir_netherite_citadel_obsidilith`.** It is already the IR "descent + dungeon + boss
+ elite gear" chapter (its lanes are `eternal_starlight`, `bosses_of_mass_destruction`, `betterend`,
`undergarden`, `cataclysm`, `deeperdarker` — i.e. it is the deep-exploration/loot chapter, not a pure
factory chapter). It already hosts warden/resonarium armor, so echo-shard → early-industry crafting bridges
(e.g. sculk/echo-shard as a feedstock into an IE or PneumaticCraft component) belong here as a small
branch off the citadel trunk `49540C1000000001`. This keeps the D&D IR half thematically co-located with
the netherite/ancient-city descent material instead of scattering it into the factory chapters.

Do NOT host it in `ir_create_industrial_addons` or `ir_modern_industrialization` — those are clean
single-theme factory chapters and a Deep Dark branch would break their lane focus. The late-Ren half
should stay in the Renaissance deep-descent chapter (`ren_deeper_darker_otherside` / `ren_undergarden_descent`
own the dimension-entry side); the IR half = the echo-shard-into-industry bridge, in the citadel chapter.

---

## Lens 5 — Cross-age recipe weaves: are the woven recipes taught?

### IR weaves (`aoa_recipes_ir_weaves.js`) — ALL 5 taught ✓

5 outputs, each present as a task in the matching IR chapter (proof: `grep -rl <output> chapters/ir_*.snbt`):

| Woven output | Taught in |
|---|---|
| pneumaticcraft:uv_light_box | ir_pneumaticcraft_pressure_plastic ✓ |
| immersiveengineering:sample_drill | ir_immersive_engineering_early_factory ✓ |
| integrateddynamics:materializer | ir_automation_safety_and_routing ✓ |
| pneumaticcraft:etching_tank | ir_pneumaticcraft_pressure_plastic ✓ |
| integrateddynamics:mechanical_squeezer | ir_automation_safety_and_routing ✓ |

Also the two `ir_magic_feedstock_bridges.js` targets (`integrateddynamics:logic_director`,
`pneumaticcraft:spawner_agitator`) are both taught in `ir_magic_feedstock_and_spectrum_network`. Fully covered.

### Gilded weaves (`aoa_recipes_gilded_weaves.js`) — 6 of 7 taught; **1 orphan**

| Woven output | Taught in | Status |
|---|---|---|
| chemicalscience:catalytic_reformer | g2_the_refinery | ✓ |
| hostilenetworks:sim_chamber | g2_the_refinery | ✓ |
| industrialforegoing:ore_laser_base | g2_the_refinery | ✓ |
| industrialforegoingsouls:soul_laser_base | g2_the_refinery | ✓ |
| nautec:bio_reactor | g6_circuits_and_current | ✓ |
| nautec:mutator | g6_circuits_and_current | ✓ |
| **extendedcrafting:advanced_table** | **NONE in Gilded** (only asc1) | **ORPHAN** |

**BROKEN (self-inconsistent doc + orphan weave):** The gilded weave rewrites
`extendedcrafting:advanced_table` to route through the Gilded silicon/electronics lane, and the script's
own comment claims *"Quest 4757011000000002 (g1) teaches the seam"* (`aoa_recipes_gilded_weaves.js:123`).
That is false. Quest `4757011000000002` in g1 teaches the Extended Crafting **auto-crafter** tier
(`ender_crafter`/`flux_crafter`), not `advanced_table` — verified:
`grep -o "extendedcrafting:[a-z_]*" g1_the_golden_workshop.snbt` returns only `ender_crafter`,
`flux_crafter`, `auto_ender_crafter`, `auto_flux_crafter`, `ender_alternator`, `flux_alternator` — no
`advanced_table`. The item `advanced_table` appears as a task ONLY in `asc1_the_table_of_infinities.snbt`
(Ascension). So a Gilded player who crafts the advanced_table hits the woven recipe with no quest anywhere
in Gilded teaching the changed recipe. Either add an advanced_table node to g1 (matching the weave's
stated intent) or correct the stale comment. This is the one woven output with zero quest presence in its
authored age.

---

## HYGIENE aside (out of core scope, noted in passing)

`config/ftbquests/quests/lang/en_us.snbt` contains **87 em-dash (U+2014) characters**
(`python3 -c "print(open(...).read().count(chr(0x2014)))"`). Canon forbids em dashes in prose. These may
be concentrated in other ages, but a mid-game prose pass should sweep them. Not a progression defect.

---

## Summary table of findings

| # | Severity | Finding |
|---|---|---|
| 1 | CANON (needs call) | Mekanism base processing spine has ZERO IR/Gilded quest home; deferred entirely to Atomic despite canon calling it an IR spine |
| 2 | BROKEN | `extendedcrafting:advanced_table` weave is orphaned — script comment claims g1 teaches it but g1 teaches the auto-crafters; item only quested in asc1 |
| 3 | CANON/HYGIENE | g2_the_refinery over-quests Industrial Foregoing (71 machines / 61 quests) — every-machine filler incl. animal/block/fluid/enchantment utility fleet |
| 4 | HYGIENE | g5 Actually Additions (69 refs) candidate for filler review; g7 is the thinnest required domain (defensible optional-depth shape) |
| 5 | (correction) | `industrialforegoing:mycelial_crimed` is REAL (jar-verified) — prior phantom flag was wrong |
| — | PASS | Both age proof-spines complete and single-granter; entry gates + ordering sane; no cross-age inversion; IR weaves + magic bridges fully taught |
