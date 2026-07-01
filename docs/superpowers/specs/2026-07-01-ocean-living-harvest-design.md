# The Living Harvest — Ocean Ecosystem Quest Layer (Design)

Date: 2026-07-01
Branch: quest-prose-cc1-cc2
Pack: NeoForge 1.21.1, CurseForge. Quest layer: FTB Quests.
Status: design approved (shape + three user amendments), ready to turn into an
implementation plan.

## 1. Problem

The pack's ocean answers "why be down there" (industry) but not "what is the
ocean" (a living, hostile place). Current on-disk reality, verified:

- `g6_circuits_and_current` (Gilded) already has the industrial ocean: a full
  NauTec deep-sea line (`nautec:aquatic_catalyst`, `deep_sea_drain`,
  `bacterial_containment_shield`, `bio_reactor`, `aquarine_steel`, etc., lines
  ~1292-1844) granting `g_nautec_oceanic_industry_complete`, plus a small
  Create: Aquatic Ambitions branch (lines ~2695-2773). **33 NauTec + machine
  tasks, zero life/danger/food.**
- Aquaculture Neptunium deep-sea gear is installed but **quest-mapped nowhere**.
- The living-ecosystem layer (Hybrid Aquatic creatures, ocean food) is **absent**
  from the questbook. An earlier attempt to place it in the Dark-Age
  `stone_water_weather_and_wounds` chapter was an age-discipline defect and was
  correctly reverted (that chapter now has no aquatic content).

Age discipline: the earliest legal *structured* ocean beat is Industrial
Revolution (Neptunium); the deep industrial ocean is Gilded. No ocean quest
content may attach to Dark Ages / Medieval / Renaissance (all Renaissance
chapters are magic/dimensional and have no ocean home).

## 2. Goal

Make the deep feel **alive, dangerous, and worth braving** — expressed through
the *gear and yield you earn*, not through mob-hunt quests. Danger stays
**ambient** (Hybrid Aquatic apex predators and stinging jellyfish spawn
naturally and threaten the player while they work; no quest forces a kill).

## 3. Verified facts (source of truth for authoring)

- **Installed** (live `/mods`): `Aquaculture-1.21.1-2.7.21`,
  `[1.21.1-Neoforge] Hybrid Aquatic 1.5.5`, `create_aquatic_ambitions-1.21.1-2.0.2`,
  `crittersandcompanions-2.4.1`, `oceansdelight-1.0.4`, `nautec-0.4.1`.
- **Nothing is quested yet**: zero occurrences of `hybrid-aquatic`,
  `oceansdelight`, or `neptunium` across `config/ftbquests/quests`.
- **Hybrid Aquatic spine is fully craftable** — recipes confirmed for
  `diving_helmet/diving_suit/diving_leggings/diving_boots`, `prismarine_rod`,
  `fishing_net`, `barbed_hook`, `glowing_hook`, `magnetic_hook`, `crab_pot`,
  `pearl`, `black_pearl`, `coral_blade`.
- **Diving suit is a cheap entry-tier kit**: `diving_suit` = copper + leather;
  `diving_helmet` = copper + glass pane (with a vision overlay). Lower tier than
  Neptunium — forms an intentional ladder, not a redundant twin.
- **Neptunium is the mastery dive kit** (verified tooltips):
  `neptunium_chestplate` = "Neptune's Lungs: Allows you to breathe underwater";
  `neptunium_helmet` = underwater vision; `neptunium_leggings` = weightless;
  `neptunium_boots` = swim speed; `neptunium` tools = no underwater penalty;
  `neptunium_fishing_rod` = fish bite more often.
- **Ocean's Delight cooking can be fully hunt-free**: `stuffed_cod`,
  `stuffed_squid`, `seagrass_salad`, `kelp_encrusted_cod`, `honey_fried_kelp`,
  `squid_rings` use kelp/fish/squid/farm crops. **Exclude** the guardian dishes
  (`guardian_soup`, `elder_guardian_roll`, `cabbage_wrapped_elder_guardian`,
  `cooked_guardian_tail`) which require guardian/elder-guardian drops.
- **ftboceanmobs is inert** (no spawn wiring, only spawn eggs + a Rift Weaver
  arena-size config) and has **zero questbook wiring** — safe to drop.

## 4. Design

Three layers. Only the two quest layers are authored here.

### Layer 0 — Ambient life (no quests)
Hybrid Aquatic fish/reef/predators, Critters & Companions fauna, and ocean flora
already spawn everywhere via the mod installs. This is the "world feels alive"
layer and needs **no quests** (canon forbids bestiary/checklist questing).
Danger = these ambient predators, braved with the gear below.

### Layer 1 — IR: the personal deep-sea kit (`ir_ir_side_gear_hidden_equipment`)
An optional-depth cluster in the existing hidden-equipment side chapter. Frame:
the survival gear you earn before the Gilded ocean base. A dive ladder:

1. **Diving kit (entry rung)** — obtain the Hybrid Aquatic set:
   `hybrid-aquatic:diving_helmet`, `diving_suit`, `diving_leggings`,
   `diving_boots`. Cheap copper/leather/glass. First safe descent.
2. **Neptunium ingot** — `aquaculture:neptunium_ingot` (cluster material node).
3. **Neptunium dive armor (mastery rung)** — `aquaculture:neptunium_helmet`,
   `neptunium_chestplate`, `neptunium_leggings`, `neptunium_boots`. The
   breathe/see/move-underwater upgrade.
4. **Neptunium harvest tools** — `aquaculture:neptunium_fishing_rod` +
   `neptunium_fillet_knife` (fish-fillet processing).
5. *(optional)* **Neptunium work tools** — `neptunium_pickaxe` + `neptunium_sword`
   (underwater mining/combat without penalty).

Depends on an existing IR anchor node so the cluster is hidden until IR (avoids
the rootless-always-visible trap). No stage grant.

### Layer 2 — Gilded: the "Living Harvest" branch (`g6_circuits_and_current`)
An optional-depth branch off the existing NauTec oceanic line. Frame: you already
run the deep-sea drain; now build the **biological harvest arm** of that
operation. All craft/obtain, ~10-12 nodes, crossing-free off the NauTec line:

Harvest tooling
1. **Harvest rig (branch root)** — `hybrid-aquatic:prismarine_rod` +
   `fishing_net`. Depends on the NauTec oceanic line.
2. **Specialized hooks** — `barbed_hook` (day), `glowing_hook` (night),
   `magnetic_hook` (treasure). Teaches the offhand-hook mechanic.
3. **Crab pot** — `hybrid-aquatic:crab_pot` passive seafood trap.

Yield & materials
4. **Pearls of the deep** — `hybrid-aquatic:pearl` -> `black_pearl`
   (+ `pearl_block` / `black_pearl_block` as a storage payoff).
5. **Reef tooling** *(light)* — `coral_blade` + one coral tool
   (e.g. `coral_pickaxe`).

Cooking sub-cluster (fuller, all optional, hunt-free)
6. **Dress the catch** — Hybrid Aquatic cooked seafood:
   `cooked_fish_steak`, `cooked_lobster`, `cooked_crab`, `cooked_shrimp`.
7. **The galley** — Ocean's Delight non-guardian dishes:
   `oceansdelight:stuffed_cod`, `stuffed_squid`, `seagrass_salad`.
8. **Signature plates** — `oceansdelight:kelp_encrusted_cod`, `honey_fried_kelp`,
   `squid_rings`.

Flavor
9. **A life down here** *(optional)* — `hybrid-aquatic:giant_clam` +
   `hydrothermal_vent_shaft` decorative "you settled the deep" node.

No stage grant. Rewards are light (the items are their own reward; small
comfort/cosmetic rewards only).

### Explicitly excluded
- **No mob-hunt / kill tasks** anywhere.
- **`hybrid-aquatic:ominous_hook` (summons Karkinos)** — omitted; it is a
  summon-a-miniboss item and the pack wants no forced hunts.
- **ftboceanmobs** roster — not used; jar to be dropped (see §6).
- **Ocean's Delight guardian dishes** — excluded (require guardian kills).
- **Renaissance placement** — rejected (no ocean home; violates no-ocean-before-IR).

## 5. Authoring constraints

- **All new content is optional depth.** It must not gate or grant any AStages
  stage. The existing Gilded/IR gates and capstone grants stay byte-untouched.
- **Crossing-free layout**, coordinate-only additions off existing lines.
  Exact node coordinates and `id`s decided at authoring time; a node-graph
  sketch can be produced then if useful.
- **First-placement-wins**: none of these items are quested elsewhere (verified),
  so no dedup conflicts.
- **Every quest needs >=1 dependency** so it is not rootless-always-visible;
  root each cluster/branch on an existing age-appropriate node.
- **SNBT format preserved**; per-file line endings detected and preserved.
  Text goes in `config/ftbquests/quests/lang/en_us.snbt` (keyed
  `quest.<id>.title/.quest_subtitle/.quest_desc`), structure in the chapter file.
- **Prose voice**: instruction-first, teach the mechanic, no em dashes, no AI-isms.
- **Icons**: each quest's icon is its task item; non-item nodes get a verified
  distinct icon.
- Verify every item ID against the jar before it lands (all IDs above are
  jar-verified as of this spec).

## 6. Companion action (separate execution)

Dropping `ftboceanmobs-21.1.4.jar` (Mob/Ocean plan step 2) is greenlit and safe:
inert, zero questbook wiring. This is a jar/config change, **not** part of this
SNBT work, but the two should ship coordinated so no quest ever references a
removed mod (none do).

## 7. Validation checklist (post-authoring)

- [ ] FTBQ validation passes (IDs, chapter links, deps, no broken refs).
- [ ] All new quests are optional depth: no `astages add` reward, no stage grant,
      no change to `g_nautec_oceanic_industry_complete` / IR capstone fan-in.
- [ ] Every new quest has >=1 dependency (no rootless leaks at world entry).
- [ ] No kill/hunt tasks; no `ominous_hook`; no guardian-dish recipes required.
- [ ] Every item ID resolves in-jar (Hybrid Aquatic / Aquaculture / Ocean's Delight).
- [ ] Dependency lines do not cross in either chapter.
- [ ] Lang keys added for every new node; chapter files structure-only.
- [ ] Duplicate-item scan clean.

## 8. Open items / risks

- Exact node counts may flex during authoring (quality over count; no padding to
  hit a number). Cooking sub-cluster may compress if any dish reads as filler.
- `crab_pot` may be authored as an item task or a `more_quest_types` place-block
  task; decide at authoring (default: item task).
- Confirm the IR side-gear chapter has a suitable existing anchor node to root
  the dive cluster on; if not, root it on the chapter's entry.
