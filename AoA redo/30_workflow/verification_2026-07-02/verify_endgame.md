# Endgame Coverage Verification — DE/DA, Re:Avaritia, Extended Crafting
Read-only census feeding the 05 Ascension buildout. All IDs jar-verified from live lang + data files.
Date 2026-07-02.

Jars: `Draconic-Evolution-1.21.1-3.1.4.632`, `Draconic-Additions-1.21.1-2.5.2.3`,
`ExtendedCrafting-1.21.1-7.0.8`, `Re-Avaritia-neoforge-1.21.1-1.3.9.9-release`.

Method: extracted `assets/*/lang/en_us.json` (registry-name truth) + `data/*/singularities/*`
from each jar; grepped all `config/ftbquests/quests/chapters/*.snbt` for each namespace;
read `aoa_astages_01n_ascension.js`, `01_item_restrictions.js`, `01p_gap_closure.js`,
`06_ore_restrictions.js`, `08_mob_boss_restrictions.js`, `team_grant.js`.

---

## HEADLINE VERDICT

Gating is essentially COMPLETE and correct for all four mods (every tier item is locked at the
right age in `01n`/`01`/`01p`). The **quest coverage is thin and top-heavy**: the census counts
(DE 21 / avaritia 7 / EC 15) map to a handful of hero machines per chapter. The registry rule
"avaritia + extendedcrafting get thorough endgame treatment" is **NOT yet met** — the Avaritia
neutron→singularity→catalyst production chain, the EC crystaltine/ultimate/singularity chain, the
DE awakened/chaotic tool+armor+staff line, the entire DE reactor rotor set, and the DA chaos-gear
line are all gated-but-unquested. These are the 05 buildout's real work.

Key mechanical fact for the author: **both Avaritia and EC expose ONE `singularity` item ID each**
(`avaritia:singularity`, `extendedcrafting:singularity`) that is data-driven across ~30 metal
variants — a quest task can only require the generic singularity item, not a per-metal ID. EC also
ships a discrete `extendedcrafting:ultimate_singularity`. Avaritia's `eternal_singularity` and
`infinity_catalyst` are discrete items and already turned in (asc4/asc2/asc7).

---

## 1. DRACONIC EVOLUTION — tier table

Gate authority: `01n` lines 39-111 (base+wyvern → otherworldly; awakened/draconic/chaotic/reactor → ascension),
`01` L52/56, `01p` L213-247, `06` ore L256-273, `08` boss L43.

| Tier / group | quested where | GAP |
|---|---|---|
| Base draconium (ore, dust, ingot, core, chest, generator, grinder, energy_transfuser, io/relay/wireless crystals, potentiometer, particle_generator) | ow6 (today) | covered |
| Energy Core multiblock (energy_core, stabilizer, pylon) | ow6 | covered (tiers 1-4 implied; **tiers 5-8 not taught as a scaling beat**) |
| Wyvern tools (sword/pick/axe/shovel/bow), wyvern_chestpiece, wyvern_capacitor, wyvern_core, wyvern_energy_core, wyvern crafting injector + crystals | ow6 | covered |
| Dislocators (dislocator, p2p, player, pedestal, receptacle, inhibitor), magnet, celestial_manipulator, disenchanter | ow6 + `01p` | covered |
| **Awakened tier** — awakened_core, awakened_draconium (dust/ingot/nugget/block), awakened_crafting_injector, draconic_energy_core, draconic io/relay/wireless crystals | asc3 (injector, awakened_core, draconic_energy_core only) | **GAP: awakened_draconium_ingot/dust/block, draconic crystals not taught** |
| **Draconic (mid) tools+armor** — draconic_sword/pick/axe/shovel/hoe/bow, draconic_staff, draconic_chestpiece, draconic_capacitor | NONE | **GAP (whole line). draconic_staff = the iconic tool, unquested** |
| **Chaotic tier** — chaotic_core, chaotic_crafting_injector, chaotic_energy_core, chaotic_sword/pick/axe/shovel/hoe/bow, chaotic_staff, chaotic_chestpiece, chaotic_capacitor | asc5 (chaotic_core, chaotic_crafting_injector only) | **GAP: all chaotic tools/armor/staff/capacitor unquested** |
| **Reactor** — reactor_core, reactor_injector, reactor_stabilizer + 5 rotor parts (prt_focus_ring, in_rotor, out_rotor, rotor_full, stab_frame) | asc3 (core/injector/stabilizer) | **GAP: 5 reactor rotor components not taught (reactor assembly under-explained)** |
| Chaos Island economy — chaos_crystal (block), chaos_shard, large/medium/small_chaos_frag, crystal_binder, dragon_heart, mob_soul, stabilized_spawner, flux_gate, fluid_gate, entity_detector | asc6 (chaos_shard, draconic_guardian boss) | **GAP: chaos_crystal harvest, frag tiers, dragon_heart, crystal_binder, mob_soul spawner economy unquested** |
| Modular upgrade system (item_*_energy/shield/speed/flight/undying/... ~120 module IDs) | NONE | intentional-ish (module bloat); teach the concept once, not 120 tasks |

DE has **no boss summon item** — draconic_guardian spawns natively (asc6 kill quest exists, `08` gate L43).

## 2. DRACONIC ADDITIONS — tier table

Gate: `01` L1125-1148 (all ascension). All IDs jar-verified.

| Group | quested where | GAP |
|---|---|---|
| Chaos production — chaos_infuser, chaos_extractor, chaos_liquifier, chaos_crystalizer, chaos_container, chaos_heart | asc5 (chaos_infuser, chaos_heart, item_chaos_injector) | **GAP: extractor/liquifier/crystalizer/container (the 4-machine chaos processing loop) unquested** |
| Chaos gear — chaotic_necklace, draconic_necklace, wyvern_necklace | NONE | **GAP (necklace line)** |
| Potato armor — inert/infused potato helm/chest/legs/boots, hermal | NONE | novelty; low priority, one flavor node at most |
| Chaos stabilization items — item_stable/semi_stable/unstable_chaos, item_chaos_injector, item_chaotic_auto_feed | asc5 (item_chaos_injector) | **GAP: stable-chaos crafting ladder unquested** |

## 3. RE:AVARITIA — tier table

Gate: `01n` L112-144 (all ascension), `01` L57-62 (prestige ingots), `01p` L171-190 (infinity gear).
Singularities: **one `avaritia:singularity` item, ~30 data variants** (aluminum, bronze, coal, copper,
diamond, gold, iron, netherite, quartz, redstone, lapis, uranium, steel, etc. — jar `data/avaritia/singularities/`).

| Tier / group | quested where | GAP |
|---|---|---|
| Neutron production — neutron_collector, neutron_compressor + dense/denser/densest collector+compressor pairs, neutron (block) | asc2 (neutron_collector, neutron_compressor, neutron block) | **GAP: dense/denser/densest scaling tiers not taught** |
| Neutron materials — neutron_pile, neutron_nugget, neutron_ingot, neutron_gear, neutron_ring, neutron_horse_armor | NONE | **GAP: neutron ingot chain (feeds infinity catalyst) unquested** |
| **Singularity chain** — `avaritia:singularity` (the ~30-variant collector/compressor output) | NONE | **GAP: THE core Avaritia loop. Player never told to run the compressor to make singularities.** |
| Catalyst spine — crystal_matrix + crystal_matrix_ingot, diamond_lattice + block, infinity_catalyst, eternal_singularity, enhancement_core, endest_pearl | asc2 (crystal_matrix, infinity_catalyst, eternal_singularity), asc4 (eternal turn-in) | **GAP: crystal_matrix_ingot, diamond_lattice, endest_pearl, enhancement_core (all infinity-catalyst inputs) not taught** |
| Extreme crafting hardware — extreme_crafting_table, extreme_smithing_table, extreme_anvil, upgrade_smithing_template; compressed/double_compressed/nether/end/sculk crafting tables; tesseract, compressed_chest, infinity_chest | NONE | **GAP: the 9x9 dire table (extreme_crafting_table) — the workbench ALL infinity gear needs — is unquested** |
| Flavor consumables — cosmic_meatballs, ultimate_stew, blaze_cube+block, star_fuel+block, refined_coal, record_fragment, matter_cluster, full_matter_cluster | NONE | **GAP: cosmic_meatballs + ultimate_stew are infinity_catalyst inputs (web-confirmed); must be taught. rest optional flavor** |
| Infinity prestige — infinity_ingot, infinity_nugget | asc7 (infinity_ingot spine turn-in) | covered as final gate |
| Infinity gear (`01p` L171-190) — sword/pick/axe/shovel/hoe/bow/crossbow/trident/mace, helmet/chestplate/pants/boots/elytra, shield/totem/ring/clock/bucket/umbrella | NONE | **GAP: reward-tier; teach 1-2 hero pieces + reward-table the rest, don't 20-node it** |

Web (CurseForge/9minecraft): infinity_catalyst recipe = 7 singularities + diamond_lattice + crystal_matrix_ingot
+ neutron dust/nugget/ingot + ultimate_stew + cosmic_meatballs + endest_pearl + record_fragment, on the extreme
workbench. This is the natural asc2/asc7 spine — currently only endpoints exist, the middle is missing.

## 4. EXTENDED CRAFTING — tier table

Gate: `01n` L145-181. IR: basic_table/auto/handheld/frame/pedestal. Gilded: advanced_auto, ender+flux crafters+alternators.
Ascension: advanced_table, elite/ultimate tables+auto, compressor, crafting_core, crystaltine/ultimate/enhanced blocks+items.
`01` L53: ultimate_table (dup lock, harmless).

| Tier / group | quested where | GAP |
|---|---|---|
| Basic table + frame + handheld (3x3 entry) | ir_oritech_foundry (basic_table, frame, handheld_table) | covered |
| Ender Crafter + Flux Crafter + alternators (Gilded) | g1 (ender_crafter, auto_ender_crafter, flux_crafter, auto_flux_crafter, ender+flux alternator) | covered |
| Advanced table (5x5) + advanced_auto_table + advanced catalyst/component | NONE (advanced_auto is Gilded-gated but unquested) | **GAP: 5x5 tier skipped entirely** |
| Elite (7x7) table+auto + elite_catalyst/component | asc1 (elite_table only) | **GAP: elite_auto + elite catalyst/component chain not taught** |
| Ultimate (9x9) table+auto + ultimate_catalyst/component + ultimate_singularity | asc1 (ultimate_table, ultimate_catalyst, ultimate_component) | mostly covered; **ultimate_auto_table + ultimate_singularity gap** |
| Compressor + crafting_core (compression crafting machine) | asc1 (compressor, crafting_core) | covered (machine present; **compression-crafting singularity output not taught**) |
| **Singularity chain** — `extendedcrafting:singularity` (compressor output), ultimate_singularity | NONE | **GAP: EC singularity production unquested; ultimate_singularity (1-of-each capstone) not taught** |
| Material ladders — black_iron (slate/ingot/block), luminessence, redstone_ingot chain, ender_ingot/ender_star, flux_star, enhanced_ender + enhanced_redstone chains | NONE | **GAP: black_iron_ingot + luminessence are the basic_catalyst backbone; needed for the whole mod. Unquested.** |
| **Crystaltine** (crystaltine_ingot/nugget/component/catalyst/block) | NONE | **GAP: crystaltine tier (elite-table prestige alloy) unquested** |
| **The Ultimate** (the_ultimate_ingot/nugget/component/catalyst + the_ultimate_block) | asc7 (the_ultimate_block spine turn-in) | **GAP: the_ultimate crafting chain not taught; only final block gated** |

---

## RANKED GAP LIST for asc1–asc7 (jar-verified, bundled)

Rank = what an Ascension chapter must teach for the mod to be playable, not just gated.

1. **[asc2] Avaritia neutron→singularity→catalyst production spine.** Teach: neutron_collector/compressor
   scaling (dense/denser/densest), `avaritia:singularity` compressor output, then the infinity_catalyst
   input bundle (7× singularity + `crystal_matrix_ingot` + `diamond_lattice` + `neutron_ingot`/dust/nugget +
   `endest_pearl` + `cosmic_meatballs` + `ultimate_stew` + `record_fragment`). This is the single biggest gap.
2. **[asc2] Avaritia extreme crafting hardware.** `avaritia:extreme_crafting_table` (9x9 dire table),
   `extreme_smithing_table`, `extreme_anvil`, `upgrade_smithing_template` — every infinity item needs these.
3. **[asc1] EC material + tier backbone.** `black_iron_ingot` (+slate), `luminessence`, basic/advanced/elite
   catalyst+component ladders, `singularity`+`ultimate_singularity`, `crystaltine_ingot` chain, `the_ultimate_ingot`
   chain, advanced_table (5x5) + elite_auto/ultimate_auto tables. Fill the skipped 5x5 and the alloy ladders.
4. **[asc3] DE reactor assembly.** 5 rotor parts (`reactor_prt_focus_ring/in_rotor/out_rotor/rotor_full/stab_frame`)
   + energy_core tiers 5-8 scaling. Reactor is the required asc-win gate (per MEMORY) but its parts are unquested.
5. **[asc3/asc5] DE awakened+chaotic material ladders.** awakened_draconium (dust/ingot/nugget/block),
   draconic io/relay/wireless crystals; chaos_crystal harvest + chaos_shard + frag tiers + dragon_heart +
   crystal_binder + mob_soul spawner economy (asc6-adjacent).
6. **[asc5] DA chaos processing loop.** chaos_extractor/liquifier/crystalizer/container + stable/semi/unstable
   chaos ladder — the 4-machine chaos refinement the chaos_heart depends on.
7. **[asc5] DE draconic + chaotic tools/armor/staff.** draconic_staff + chaotic_staff (iconic), full
   tool sets, chestpieces, capacitors. Teach as a gear beat, not per-tool spam (bundle sets).
8. **[asc7 / reward-tables] Avaritia infinity gear + DA necklaces.** Teach 1-2 hero pieces (infinity_sword,
   infinity_chestplate) as spine; reward-table the remaining ~18 infinity items + DA necklaces. Do NOT 20-node it.

Bundling guidance: singularity chains are ONE item ID each (task the generic `singularity`); bundle each DE
tool tier into a single node; reward-table cosmetic/flavor (potato armor, most infinity gear, blaze/star_fuel
consumables) rather than authoring dedicated quests. Gating needs NO changes — do not propose new gates.
