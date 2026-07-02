# Misc-tech coverage verification — 7 mods (READ-ONLY)

Date 2026-07-02. All jars confirmed in /mods. The census's raw ref/model counts were
misleading: model counts are dominated by ore/decor/element variants, and several "0-ref"
mods are gated-but-deliberately-unquested. Actual mechanic coverage is far better than the
numbers implied. Verdicts respect AOA_QUEST_SCOPE_REGISTRY (no coverage-gating, no decor
tours, no re-teaching).

Legend: EXPAND = real untaught mechanics worth quests | ACKNOWLEDGE = 1 discovery beat max |
LEAVE = redundant/legacy/decor/utility, author nothing.

---

## 1. chemicalscience (jar 3.1.1) — VERDICT: LEAVE (already well-covered)
**What it is:** an **Electrodynamics addon** (its base machine tree — grinder/crusher/electric
furnace/arc furnace/coal+thermoelectric generator, all with double/triple variants — belongs to
Electrodynamics, seen in its own roadmap). Chemicalscience's own contribution is a
petro/organic-chemistry layer plus planet-ore variants.
**Real machines (jar-verified):** Redox Furnace (multiblock), Fractionating Column (13-tall
multiblock), Fume Hood / chemical_bench (multiblock organic chem), Steam Cracker, Catalytic
Reformer, HDS Unit, Circuit Assembler (circuitmaker), Spin Coater, Fuel Cell, Organic Solar Panel.
Plus fluorite/uranium/thorium planet ores.
**Live coverage:** 38 distinct ids across 4 chapters — at1_nuclear_dawn, at2_the_periodic_table,
at5_threshold_of_war, g2_the_refinery. Every core machine above is already a task
(redox_furnace_controller, fractionating_column, chemical_bench_controller, steam_cracker,
catalytic_reformer, hds_unit, circuitmaker, spincoater, organicsolarpanel) plus the nuclear
feedstock chain (uranium/thorium/plutonium dusts, planet ores). Gated in 9 kubejs scripts.
**Why the "26 vs 909" gap is void:** 909≈ ore variants (7 metals × 4 planets) + 118 element decor
blocks + scaffolding/lamp/asphalt/hazard-sign decor + Electrodynamics-owned tiered machines. None
of those are quest-worthy under anti-decor / no-re-teach policy. The chemistry SPINE is fully taught.
**Gap:** none worth authoring. Optional micro-beat only: the organic-chem card chain
(chromatography cards, DPP-DTT polymer path) is deep flavor — leave as free discovery.

## 2. actuallyadditions (jar 1.3.26) — VERDICT: LEAVE (near-complete)
**Machines (jar):** Crusher/Double Crusher, Empowerer, Atomic Reconstructor + lenses, Farmer,
Ranged Collector, Long-Range/Auto Breaker, Placer, Laser Relays (energy/adv/extreme/item/fluid),
Phantom faces (item/energy/redstone/liquid/placer/breaker), Bio Reactor, Leaf/Oil/Coal generators,
Canola Press, Fermenting Barrel, Battery Box, Energizer/Enervator, Powered Furnace, Coffee Maker,
Heat Collector, drills.
**Live coverage:** 42 distinct ids in g5_empire_of_iron + journey_to_ascension. Gated in 6 scripts.
The census claim "most machines unquested" is FALSE — atomic_reconstructor, empowerer, crusher,
lens, farmer, ranged_collector, all laser_relay tiers, phantom faces, bio_reactor, energizer,
canola_press, oil/leaf/coal generators, powered_furnace, vertical_digger (drill) are ALL tasks.
**Unquested residue:** dropper, feeder, greenhouse_glass, xp_solidifier, display_stand,
fluid_placer, mini_reactor. All QoL/decor/utility — correctly out of scope. No re-teaching the
crusher/reconstructor spine.
**Gap:** none. LEAVE.

## 3. create_sa / Create Stuff 'N Additions (jar v2.1.4a) — VERDICT: ACKNOWLEDGE (1 beat, optional)
**Content (jar+web):** power-gear axis — Brass/Copper/Andesite/Netherite Jetpacks & Exoskeletons,
Propeler armor, Grapplin Whisk (grapple), Brass Portable Drill, Nozzle Fan, Blaze Flamethrower,
Block Picker, Copper Magnet, Experience tools, filling/fueling tanks, drone_controller.
**Live coverage:** 0 chapter refs. BUT gated: drone_controller locked at IR (line 668) and copper
gear recipes staged (aoa_astages lines 77-84). Comment at kubejs line 14: "create_sa power-gear
(wearables, different axis) left ungated" — **this is a deliberate scope decision**, and it
overlaps the pack's standing "flight stays free/ungated" ruling (jetpacks = flight).
**Verdict:** the wearable/flight axis is intentionally free — do NOT build a gear chapter (would
collide with flight policy + decor-tour ban). At most ONE optional discovery beat pointing players
at the Brass Jetpack / Grapplin Whisk as a Create-tier mobility toy. Not a gap. ACKNOWLEDGE-optional.

## 4. immersive_machinery (jar 0.2.0) — VERDICT: ACKNOWLEDGE (1 beat)
**Content (jar+web):** tiny rustic-machinery set — Tunnel Digger (slow bore machine), Copperfin
(conduit-powered mini-submarine, upgradable w/ amethyst shards), Bamboo Bee (item-hauling drone),
Redstone Sheep (auto-harvest contraption), Iron/Diamond/Netherite Drill heads, Redstone Mechanism.
That's the ENTIRE mod — ~5 entities + a few items. Small by design.
**Live coverage:** 0 refs; gated (iron_drill @ IR, line 673).
**Verdict:** too thin for a chapter and thematically it's vanilla-adjacent QoL, not a tech spine.
The Copperfin (underwater work) is the one distinctive beat and overlaps the ocean/diving layer
already authored. ONE optional acknowledgment quest (Copperfin or Tunnel Digger) at IR is the
ceiling. No expand. Not a real gap.

## 5. productivemetalworks (jar 1.15.0) — VERDICT: LEAVE (spine covered)
**What it is:** a Tinkers-style **smeltery/foundry** — single mechanic: melt metal → cast into
ingots/plates/rods/gears. Content = Foundry multiblock (controller/drain/tank/tap/window/capacitor
in 16 decorative color variants) + Casting Basin/Table + casts + fire bricks/clay + heating coils.
**Live coverage:** 15 ids in metallurgy.snbt + m3_relics_and_burrows. Foundry controller/drain/tank/
tap, casting_basin, casting_table, ingot/plate/rod casts, fire_brick, fire_clay, heating coils ALL
quested. Gated in 1 script.
**Why 15 "vs more" is fine:** the other ~200 blocks are the SAME foundry parts in 16 colors — pure
decor variants. The mechanic (build foundry, cast a shape) is taught once, correctly. Re-teaching a
second color is banned.
**Gap:** none. LEAVE.

## 6. mifa / More Industrial Foregoing Addons (jar 2.1.0) — VERDICT: LEAVE
**Content (jar):** lang file has exactly ONE item — `mifa:netherite_gear` — plus two creative-tab
strings. This is a near-empty cosmetic/compat addon to Industrial Foregoing, not a machine mod.
**Live coverage:** 0 refs; the single item (netherite_gear) IS already staged at IR (line 681) as a
crafting component. Nothing to teach — there is no mechanic here.
**Gap:** none. LEAVE (already gated where it matters).

## 7. sophisticatedstorage (jar 1.5.65) — VERDICT: ACKNOWLEDGE (upgrade ladder = 1 optional beat)
**Content (jar):** storage tiers (copper/iron/gold/diamond/netherite chests, barrels, limited
barrels, controller) + a large UPGRADE-CARD system: stack tiers 1-5+omega, compacting, feeding,
void, smelting/smoking/blasting, crafting, pickup, magnet, filter, xp/advanced pump, hopper,
jukebox, alchemy.
**Live coverage:** 13 ids in metallurgy.snbt + ren_archive_recordkeeping — chest tiers, tier-upgrade
items, stack_upgrade_tier_1/2, magnet_upgrade, storage_tool, upgrade_base, packing_tape, limited
barrels. The storage-tier ladder + entry upgrades ARE taught.
**Genuine untaught surface:** the FUNCTIONAL upgrade cards — compacting, feeding, void, auto-smelting,
crafting, hopper, pump — are not surfaced anywhere. These are real automation mechanics, not decor.
**Verdict:** but they are QoL convenience cards, not progression, and the pack already teaches the
concept via stack/magnet. A full card-by-card chapter = bloat. ONE optional "upgrade your storage"
beat that names compacting + auto-smelting + feeding as the next rung is the honest ceiling.
ACKNOWLEDGE, not EXPAND.

---

## Ranked gap list (jar-verified, bundled) — all LOW priority, all optional
Nothing here is a required-spine gap. In descending order of (weak) merit:

1. **[ACK-opt] sophisticatedstorage upgrade cards** — one optional quest in an existing storage/
   logistics chapter (metallurgy or a Gilded logistics chapter) naming
   `sophisticatedstorage:compacting_upgrade`, `:auto_smelting_upgrade`, `:feeding_upgrade`. IR/Gilded age.
   Rationale: only mod here with a real untaught mechanic surface. Still QoL, so 1 beat max.
2. **[ACK-opt] immersive_machinery Copperfin/Tunnel Digger** — one optional beat at IR
   (`immersive_machinery:copperfin` or `:tunnel_digger`). Ties to existing ocean/diving layer.
3. **[ACK-opt] create_sa mobility toy** — one optional beat pointing at `create_sa:brass_jetpack_chestplate`
   or `:grapplin_whisk`, Renaissance/IR. CAUTION: must not gate (collides with free-flight policy).

## Do NOT author (verified redundant/out-of-scope)
- chemicalscience chemistry spine — already fully taught (redox/column/fume hood/cracker/reformer/
  hds/circuit/spincoater/solar panel all quested). Its 909 models are ore+element+decor variants.
- actuallyadditions machines — 42 ids already cover crusher/reconstructor/empowerer/lenses/farmer/
  relays/phantoms/generators. Residue (dropper/feeder/greenhouse/xp_solidifier) is decor/QoL.
- productivemetalworks — foundry+casting mechanic taught once; remaining blocks are 16-color decor.
- mifa — one cosmetic item, already staged; no mechanic exists to teach.

## Sources
- Jar lang files: chemicalscience/actuallyadditions/create_sa/immersive_machinery/productivemetalworks/
  mifa/sophisticatedstorage en_us.json (read directly from /mods).
- Live chapters: config/ftbquests/quests/chapters/*.snbt (grep per namespace).
- Gates: kubejs/server_scripts/aoa_astages_*.js (lines 668/673/681 + recipe-stage 77-84, comment L14).
- CurseForge: https://www.curseforge.com/minecraft/mc-mods/create-stuff-additions ;
  https://www.curseforge.com/minecraft/mc-mods/immersive-machinery
- Policy: AOA_QUEST_SCOPE_REGISTRY.md (no coverage-gating; anti-decor/anti-re-teach).
