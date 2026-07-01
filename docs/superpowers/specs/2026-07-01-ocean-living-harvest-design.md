# The Living Harvest — Ocean Ecosystem Quest Layer (Design)

Date: 2026-07-01 (rev 2)
Branch: quest-prose-cc1-cc2
Pack: NeoForge 1.21.1, CurseForge. Quest layer: FTB Quests.
Status: design approved through all amendments; ready to turn into an
implementation plan. (The Create: Aquatic Ambitions portion may be absorbed into
the separate Create-addon tutorial questline initiative now in research — see §9.)

## 1. Problem

The pack's ocean answers "why be down there" (industry) but not "what is the
ocean" (a living, hostile place). Verified on-disk reality:

- `g6_circuits_and_current` (Gilded) has the industrial ocean: a full NauTec
  deep-sea line (`nautec:aquatic_catalyst`, `deep_sea_drain`,
  `bacterial_containment_shield`, `bio_reactor`, `aquarine_steel`, lines
  ~1292-1844) granting `g_nautec_oceanic_industry_complete`, plus a small Create:
  Aquatic Ambitions branch (lines ~2695-2773). **Machine tasks only, zero
  life/danger/food.**
- Aquaculture Neptunium deep-sea gear is installed but **quest-mapped nowhere**.
- The living-ecosystem layer (Hybrid Aquatic creatures, ocean food) is **absent**
  from the questbook. An earlier attempt to place it in the Dark-Age
  `stone_water_weather_and_wounds` chapter was an age-discipline defect and was
  correctly reverted.

Age discipline governs quest *placement*, not ambient life. Ambient sea life is
fine everywhere. The *structured* ocean quest layer attaches from Industrial
Revolution onward.

## 2. Goal

Make the deep feel **alive, dangerous, and worth braving** — expressed through
the *gear and yield you earn*, not through mob-hunt quests. Danger stays
**ambient** (Hybrid Aquatic apex predators and stinging jellyfish spawn
naturally; no quest forces a kill).

## 3. Verified facts (source of truth)

- **Installed** (live /mods): Aquaculture 2.7.21, Hybrid Aquatic 1.5.5, Create:
  Aquatic Ambitions 2.0.2, Critters & Companions 2.4.1, Ocean's Delight 1.0.4,
  NauTec 0.4.1.
- **Nothing is quested yet**: zero `hybrid-aquatic`, `oceansdelight`, or
  `neptunium` occurrences across `config/ftbquests/quests`.
- **Hybrid Aquatic spine is fully craftable** — verified recipes for the diving
  set (`diving_helmet/suit/leggings/boots`, cheap copper+leather+glass), every
  hook, `fishing_net`, `prismarine_rod`, `crab_pot`, `pearl`, `black_pearl`,
  `coral_blade`.
- **Aquaculture Neptunium is the mastery dive kit** (verified tooltips):
  chestplate = breathe underwater, helmet = underwater vision, leggings =
  weightless, boots = swim speed, tools = no underwater penalty, rod = fish bite
  more often. Higher tier than the diving suit -> intentional ladder.
- **Ocean's Delight cooking is hunt-free** using `stuffed_cod`, `stuffed_squid`,
  `seagrass_salad`, `kelp_encrusted_cod`, `honey_fried_kelp`, `squid_rings`.
  **Exclude** guardian dishes (`guardian_soup`, `elder_guardian_roll`, etc.).
- **`m3_relics_and_burrows`** is a Medieval **exploration** chapter (icon
  `alchemists_garden:leather_glove`) using `hide_quest_until_deps_complete: true`
  — the chosen host for the hidden diving-suit node.
- **The hidden-reveal mechanic** is `hide_until_deps_complete: true` at the quest
  level (proven in `ir_ir_side_gear_hidden_equipment`) — a node stays invisible
  until the node it depends on is *completed*. Distinct from the pack's normal
  progressive reveal (visible when deps become available).
- **Create: Aquatic Ambitions** is a pure automation addon (no worldgen/entities).
  Core mechanic: **Conduit Channeling** (encased-fan air through a Conduit's water
  or a compact **Conduit Cage** = `mechanical_conduit`). Automates prismarine,
  coral revival, copper weathering, and — key — channels an ender-eye into
  Heart of the Sea and processes `suspicious_rock` (a limestone-milling byproduct,
  alongside `calcium_rich_powder`) into nautilus shells + `spiky_shell`, making
  **whole conduits farmable**. **RULE TRAP:** the useful outputs (Heart of the
  Sea, nautilus shells, copper, lapis, prismarine, trident) are all `minecraft:`
  vanilla items, which cannot be quest task items here. Tasks must gate on CAA's
  own intermediates: `prismarine_alloy`, `prismarine_alloy_rod`, `spiky_shell`,
  `suspicious_rock`, `calcium_rich_powder`, `mechanical_conduit`. (`nautilus_shard`
  is a crushing *process* on a nautilus shell, not a Cage ingredient — do not
  quest it.)
- **ftboceanmobs is inert** (no spawn wiring; spawn eggs + a Rift Weaver arena
  config only) with zero questbook wiring — safe to drop.

## 4. Design

### Layer 0 — Ambient life (no quests)
Hybrid Aquatic fish/reef/predators, Critters & Companions fauna, ocean flora —
already spawn everywhere via the installs. No quests (canon forbids
bestiary/checklist questing). Danger = these ambient predators.

### Layer 1 — Hidden gear (surprise reveals, `hide_until_deps_complete: true`)
Per user rule: hidden gear lives as hidden side-nodes on main-chapter quests,
never its own chapter. Split by tier:

- **Diving suit — one hidden node in `m3_relics_and_burrows`** (Medieval
  exploration). Obtain the Hybrid Aquatic set (`diving_helmet`, `diving_suit`,
  `diving_leggings`, `diving_boots`). The cheap early on-ramp, framed as gear for
  delving flooded ruins. Hangs off an existing m3 quest, revealed on its
  completion. Item-legal (ungated copper/leather/glass).
- **Neptunium mastery kit — hidden nodes off the g6 ocean line.**
  `neptunium_ingot` -> the armor set (breathe/see/move) -> rod + fillet knife ->
  optional tools. Revealed as you complete the relevant NauTec/harvest
  prerequisites. The deep-op mastery gear, at the deep op.

### Layer 2 — g6 "Living Harvest" branch (normal reveal, optional depth)
A branch off the existing NauTec oceanic line. Frame: you run the deep-sea drain;
now build the biological harvest arm. ~10-12 craft/obtain nodes, crossing-free:

Harvest tooling: `prismarine_rod` + `fishing_net` (root) -> hooks (`barbed_hook`
day, `glowing_hook` night, `magnetic_hook` treasure) -> `crab_pot`.
Yield & materials: `pearl` -> `black_pearl` (+ blocks); `coral_blade` + a coral
tool (light).
Cooking sub-cluster (fuller, hunt-free): Hybrid Aquatic cooked seafood
(`cooked_fish_steak`, `cooked_lobster`, `cooked_crab`, `cooked_shrimp`) +
Ocean's Delight dishes (`stuffed_cod`, `stuffed_squid`, `seagrass_salad`,
`kelp_encrusted_cod`, `honey_fried_kelp`, `squid_rings`).
Flavor: `giant_clam` + `hydrothermal_vent_shaft` "a life down here" node.

### Create: Aquatic Ambitions extension (g6, 2 nodes — extends the existing CAA branch)
Task items = CAA intermediates only (rule trap above); mechanics taught in prose.
1. **Conduit Channeling** — task: obtain `create_aquatic_ambitions:suspicious_rock`
   + `calcium_rich_powder`. Prose teaches building the encased-fan + Conduit Cage
   channeling setup and its payoff: renewable prismarine/coral/copper and
   automating Heart of the Sea + nautilus shells into **farmable conduits**.
2. **Conduit Cage Station** — task: a second `mechanical_conduit` (or
   `prismarine_alloy_block`). Prose teaches awakening the Cage with fluids for
   area effects (Conduit Power / buffs / hazards) with the entity filter. Utility
   flavor.

### Explicitly excluded / rejected
- No mob-hunt / kill tasks anywhere. No `ominous_hook` (Karkinos summon).
- **No standalone "hidden equipment" chapter** — hidden gear is side-nodes in
  main chapters (`ir_ir_side_gear_hidden_equipment` is a pre-existing anti-pattern;
  we do not add to it).
- ftboceanmobs roster (jar to be dropped). Ocean's Delight guardian dishes.
- CAA vanilla-output items as task items (trident, Heart of the Sea, etc.).
- Renaissance placement for the suit (no ocean home there).

## 5. Authoring constraints

- **All new content is optional depth.** No AStages grants; the Gilded/IR gates
  and capstone fan-ins stay byte-untouched.
- **Reveal model:** normal branch quests use standard progressive reveal; the two
  hidden-gear placements use `hide_until_deps_complete: true` on the node.
- **Crossing-free**, coordinate-only additions off existing lines; exact node
  ids/coords at authoring. Every quest needs >=1 dependency (no rootless leaks).
- **First-placement-wins**: none of these items are quested elsewhere (verified).
- SNBT format + per-file line endings preserved; text in
  `config/ftbquests/quests/lang/en_us.snbt`, structure in chapter files.
- Prose: instruction-first, teach the mechanic, no em dashes, no AI-isms. CAA
  descriptions must be **mechanically accurate** (channeling steps, rule traps).
- Icons = task item; non-item nodes get a verified distinct icon.
- Verify every item ID against the jar before it lands (all IDs above verified).

## 6. Companion action (separate execution)

Dropping `ftboceanmobs-21.1.4.jar` (Mob/Ocean plan step 2) is greenlit and safe.
Separate jar/config change; ship coordinated so no quest references a removed mod.

## 7. Validation checklist (post-authoring)

- [ ] FTBQ validation passes (IDs, chapter links, deps, no broken refs).
- [ ] All new quests optional depth: no `astages add` reward, no stage grant, no
      change to `g_nautec_oceanic_industry_complete` / IR capstone fan-in.
- [ ] The two hidden-gear nodes use `hide_until_deps_complete: true` and each has
      a real dependency in its host chapter (m3 suit node; g6 Neptunium nodes).
- [ ] No standalone hidden-equipment chapter created or extended.
- [ ] No kill/hunt tasks; no `ominous_hook`; no guardian dishes; no vanilla-item
      task items (incl. CAA outputs).
- [ ] Every CAA task gates on a CAA intermediate, never a `minecraft:` output.
- [ ] Every item ID resolves in-jar. Dependency lines do not cross.
- [ ] Lang keys added for every new node; chapter files structure-only.
- [ ] Duplicate-item scan clean.

## 8. Open items / risks

- Node counts may flex during authoring (quality over count; no padding).
- `crab_pot` may be an item task or a place-block task (default: item task).
- Confirm the exact host quest in `m3_relics_and_burrows` to hang the suit node on.

## 9. Relationship to the Create-addon tutorial questline

A separate initiative (workflow `w8oz2cc5s`, 2026-07-01) is researching every
Create add-on to seed a new-player Create tutorial/motivating questline. The two
CAA nodes here may be absorbed into that questline once its design lands; keep
them mechanically consistent with the CAA reference doc at
`AoA redo/40_create_addons/create_aquatic_ambitions.md`.
