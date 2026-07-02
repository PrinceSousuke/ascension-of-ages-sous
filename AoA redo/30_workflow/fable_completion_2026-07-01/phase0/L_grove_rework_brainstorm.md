# Grove chapter rework brainstorm — `what_waits_in_the_grove.snbt`

Phase 0 brainstorm. BRAINSTORM ONLY — nothing edited. Age: **medieval_times**
(group `508B59840C508057`). Subject file: `config/ftbquests/quests/chapters/what_waits_in_the_grove.snbt`
(2685 lines, 48 quest nodes). Prose: `config/ftbquests/quests/lang/en_us.snbt`
(keys `quest.6D7E8F901A2B*`, `chapter.6D7E8F901A2B0501.*`).

All item/entity IDs below were confirmed in the live jars in `mods/`:
`mowziesmobs-1.21.1-1.8.2.jar`, `born_in_chaos_[Neoforge]_1.21.1_1.7.6.jar`,
`MonsterPlus-Neoforge1.21.1-v1.2.0.0.jar`, `alchemists_garden_regrowth-v9.2.jar`,
`crittersandcompanions-neoforge-1.21.1-2.4.1.jar`.

---

## 1. Current structure map

**Chapter role.** `chapter.6D7E8F901A2B0501.title = "What Waits in the Grove"`,
subtitle "Face the guardian that seals the Medieval era." It is the **Medieval age
capstone gate**: node `6D7E8F901A2B1054` ("Master of the Grove") carries the
`/astages add {p} the_renaissance true true` grant + `aoa:age/the_renaissance` +
`aoa:journey/grove_trials` advancements. This is the ONLY the_renaissance grant in
the pack's Medieval tab.

**Entry gate (external).** 20+ grove nodes depend on `097AED7C91033D5E`, which is
NOT in this file — it is metallurgy's node "Entering the Iron Era / Cross into the
Medieval age" (`config/ftbquests/quests/chapters/metallurgy.snbt:915`). So the grove
chapter opens off the Medieval metallurgy spine.

**Dependency flow.** Three loosely-connected clusters, all rooted on the metallurgy
gate, converging on the capstone:

- **Mowzies column (x≈1–6, left):** four boss kills each feeding a gear/drop node.
  - `...100C` kill Ferrous Wroughtnaut → `...100D` Wrought Helmet (item),
    `...2101` Wrought Axe (item, `consume_items:false`).
  - `...1010` kill Sculptor → `...1011` Sculptor Staff, `...2102` Geomancer 4-piece set.
  - `...1013` kill Naga → `...1014` Naga Fang.
  - `...1019` kill Elokosa Howler → `...101A` Paw of Full Moon.
  - Standalone item nodes: `...1016` Spear, `...1018` Bluff Rod, `...101D` Paw of
    Crescent, `...101B`/`42BFA7916F2CD4FC` Umvuthana masks (fury/faith, smart_filter +
    a solo Mask of Fury diamond).
  - Elokosa paw set collector `0713486EDCE7D787` (smart_filter AND of crescent+full+gibbous).
- **Born in Chaos cluster (x≈9–18, middle):** `...101F` Dark Metal (smelt ingot +
  block — the one genuine crafting spine) fans out to a large web of drop-collect and
  brew nodes (Orb of Summoner, Death Totem, Monster Parts, Seed of Chaos, Staff of
  Magic Arrows, Spiritual Dust, elixirs, Gentleman Frog tombstone) PLUS a **kill
  bestiary**: bonescaller→supreme_bonescaller→dread_hound(x5)→dire_hound_leader chain,
  sir_pumpkinhead, door_knight+fallen_chaos_knight, lifestealer, zombie_bruiser+bone_imp,
  corpse_fly+mr_pumpkin (optional), nightmare_stalker.
- **Monster Plus cluster (x≈8–14, top, y negative):** crystal_zombie+spectral_skull →
  desert_sorceress+desert_acolyte → abyssologer(rsquare) → ancient_scroll / crystal_shard
  +dark_essence / dark armor. Plus `5468102A19D28104` Corrupted Ancient Hero (rsquare)
  → `31F70E7481C6CE82` Ancient Broken Sword.
- **Great Hunt convergence (x≈17–20):** four `min_required_dependencies:2` kill nodes
  (Wroughtnaut/Foliaath/Frostmaw/Grottol, all mowzies) feed the capstone
  `...1054` (`min_required_dependencies:3`) which grants the age.
- **Alchemist's Garden side bosses (x≈21–23):** Gnome King → Kings Shovel,
  Spider Queen → Queens Fang + loot table. Both `rsquare`, real side bosses with
  loot-bag rewards. Gated off `...102C` (Paw of Gibbous).
- **Crittersandcompanions optional tail (x≈0–2, y19):** grappling_hook, silk_lead
  (both `optional:true`, `hide_until_deps_visible`). Ambient filler.

**Rewards.** Almost entirely `xp` (25 typical, 50/75/100 on shaped nodes). Real item
rewards only on `...1019` (elokosa_paw_crescent), `280E76D5A93E6B6C`
(gnome_king_loot_bag), `29DE51ABF8B5D7FA` (spider_queen_loot_bag), `0ABD97C61DE42DCF`
(loot table `8849093687305634787`). Capstone grants stage+advancements only.

**Stage grant / fan-in.** Only `...1054` grants a stage. It fans in via the four Great
Hunt nodes (`min_required_dependencies:3` of 4), each of which needs 2-of-4 of
`{dire_hound_leader kill, supreme_bonescaller kill, Paw of Gibbous, Ancient Hero kill}`.
So the effective gate = "kill Wroughtnaut-tier bosses" — solid, boss-anchored, NOT a
checklist grant. **This spine is good and must be preserved.**

### Node classification (48 nodes)

| Category | Count | Verdict |
|---|---|---|
| Mowzies boss kill (real bosses/minibosses) | 4 + 4 Great Hunt | KEEP (bosses legal) |
| Mowzies drop/gear item nodes | 8 | GOOD (drop-item, real uses) |
| Born in Chaos Dark Metal spine + drops/brews | ~11 | MOSTLY GOOD (item tasks) |
| **Born in Chaos ordinary-mob kills** | 8 | **OFFENDING** (bestiary) |
| **Monster Plus ordinary-mob kills** | 3 | **OFFENDING** (bestiary) |
| Monster Plus drop/gear item nodes | 3 | GOOD |
| Monster Plus miniboss kills (abyssologer, ancient_hero) | 2 | BORDERLINE (rsquare; not true bosses) |
| Alchemist's Garden side bosses (gnome_king, spider_queen) | 2 + 2 drops | KEEP (real side bosses w/ loot) |
| Crittersandcompanions optional ambient | 2 | DROP or move (off-theme) |
| Capstone + masks/collectors | ~4 | KEEP |

**The defect the user flagged:** ~11–13 ordinary-mob kill nodes (all born_in_chaos +
monsterplus rank-and-file: bonescaller, dread_hound, door_knight, fallen_chaos_knight,
lifestealer, zombie_bruiser, bone_imp, corpse_fly, mr_pumpkin, nightmare_stalker,
crystal_zombie, spectral_skull, desert_sorceress, desert_acolyte). These are the
"Great Hunt bestiary" — checklist creep, violates the go-forward "bosses only" rule.

---

## 2. What the chapter is FOR

Medieval combat/darkness capstone. The player has iron-tier metallurgy (from the
metallurgy chapter) and now proves mastery of the overworld's dangerous fauna before
crossing into the Renaissance. Three mob families anchor it:

- **Mowzies Mobs** — the marquee content. Genuine hand-built world bosses
  (`ferrous_wroughtnaut`, `sculptor`, `naga`, `frostmaw`) + minibosses/critters
  (`foliaath`, `grottol`, `elokosa_howler`, `umvuthana`). Each boss drops signature
  **gear**: Wrought Helmet + Axe of a Thousand Metals (`wrought_axe`), Geomancer
  4-piece set + `sculptor_staff`, `naga_fang`→`naga_fang_dagger`, elokosa moon-paws
  (`elokosa_paw_crescent/full/gibbous/half/new`), `earthrend_gauntlet`, `sol_visage`,
  Umvuthana masks (fury/faith/fear/bliss/misery/rage). This is a rich, gear-first mod —
  ideal for an "arm yourself from the hunt" theme.
- **Born in Chaos** — the "dark host." Anchored on a real crafting metal:
  `dark_metal_ingot`/`dark_metal_block`/`pieceofdarkmetal`/`pileof_dark_metal`, feeding
  `dark_metal_armor_*` (full 4-piece set) + `nightmare_mantleofthe_night_*` set,
  weapons (`darkwarblade`, `nightmare_scythe`, `great_reaper_axe`, `soul_cutlass`,
  `spiritual_sword`, `sharpened_dark_metal_sword`), charms (`charmof_power/fury/
  endurance/resistance/stealth`), and elixirs. Deep enough to be an equip line, not a
  bestiary. Bosses: `supreme_bonescaller`, `sir_pumpkinhead`, `dire_hound_leader`,
  `lord_pumpkinhead`/`krampus` (event-tier).
- **Monster Plus** — support darkness fauna. Crystal + dark gear sets
  (`crystal_helmet/chestplate/leggings/boots/sword`, `dark_helmet`+`dark_chestplate`
  only — no dark_leggings/boots), scrolls/staves (`skull_staff`, fire/soul/dark
  scrolls), `ancient_broken_sword`, `gnawing_jaw`. Miniboss `ancient_hero`,
  `abyssologer`. Shallower; best as a support/optional lane, not a co-headliner.

**Questable items instead of raw kills (all jar-verified):**
Mowzies gear (`wrought_axe`, `wrought_helmet`, `sculptor_staff`, geomancer set,
`naga_fang_dagger`, `earthrend_gauntlet`, `sol_visage`, moon paws, masks, `spear`,
`blowgun`+`dart`, `sand_rake`, `glowing_jelly`). Born in Chaos metal+armor+weapons+
charms+elixirs (all confirmed). Monster Plus crystal/dark sets, scrolls, `ancient_scroll`,
`crystal_shard`, `dark_essence`, `ancient_broken_sword`. **No structure/advancement
targets found** for these three mods (no `data/*/advancement` player-facing chain and
mowzies has no craftable structure item beyond `test_structure` dev item) — so
retargeting is **drop-item and craft-item**, matching the Living Harvest precedent.

---

## 3. Three rework concepts

### Concept A — "Minimal surgery: bosses stay, bestiary becomes loot" (LOW RISK)
**Pitch:** Keep the layout and every ID; convert the ~11 ordinary-mob `kill` tasks into
the drop-item they were implicitly farming, and delete the pure-pest nodes.

- Keep ALL mowzies boss kills (4 headliners + 4 Great Hunt) — legal, they are bosses.
- Keep alchemists_garden Gnome King / Spider Queen (real side bosses).
- Keep the 3 born_in_chaos minibosses that carry rsquare/named prose:
  `supreme_bonescaller`, `sir_pumpkinhead`, `dire_hound_leader` (arguably minibosses;
  flag for canon call — if "bosses only" is strict, retarget these to their drops too:
  `supreme_bonescaller`→`bonescaller_staff`, `dire_hound_leader`→`fangofthe_hound_leader`,
  `sir_pumpkinhead`→`lord_pumpkinheads_lamp`/`pumpkinhandgun`).
- **Retarget** the rank-and-file kills to item tasks on their signature drops:
  `dread_hound`→drop item, `lifestealer`→`lifestealer_bone`, `nightmare_stalker`→
  `nightmare_claw` (already a separate node — fold), `zombie_bruiser`+`bone_imp`,
  `door_knight`/`fallen_chaos_knight`, `corpse_fly`/`mr_pumpkin` → **delete** (pure pests,
  no meaningful drop; boss_progression_proof.js is NOT needed since nothing gates on them).
- Monster Plus: `crystal_zombie`+`spectral_skull` and `desert_sorceress`+`desert_acolyte`
  kills → retarget to `crystal_shard`/`spectral_essence`/`dark_essence` item nodes (these
  drop nodes already exist downstream — collapse the kill+drop pairs into single item nodes).
  Keep `ancient_hero`/`abyssologer` as-is or retarget to `ancient_broken_sword`/`gnawing_jaw`.
- **Nodes:** ~48 → ~36. Same three clusters, same capstone fan-in, same IDs on all
  kept nodes. Crossing-free is preserved because we only delete leaves + swap task type
  inside existing nodes.
- **Rewards:** unchanged (xp), optionally sprinkle the drop item as a reward on boss nodes.
- **Migration safety:** trivial — only `097AED7C91033D5E`, `6D7E8F901A2B1054`,
  `6D7E8F901A2B0501` are externally referenced; none are touched. Deleted nodes are leaves
  with no external deps.

### Concept B — "Arm Yourself Against the Dark" (FULL RE-THEME, RECOMMENDED)
**Pitch:** Reframe the chapter from "kill a checklist of mobs" to "build the Medieval
combat kit from what the grove's guardians drop, then prove it on the four great beasts."
Three short equip-lines feeding one boss gate.

Narrative hook: the metallurgy chapter gave you iron; the grove is where iron is not
enough. Each of the three dark powers of the overworld yields a weapon or armor line, and
mastering the four great beasts (mowzies) is the final exam that seals the Medieval era.

Node sketch (~22–26 nodes, one visual lane per family):

1. **Lane 1 — The Beast-Forged Kit (Mowzies, ~9 nodes).** KEEP the 4 boss kills as the
   spine of this lane (bosses are legal and are the mod's whole point), each immediately
   followed by its gear payoff:
   - Ferrous Wroughtnaut → Wrought Helmet + Axe of a Thousand Metals (bundle into one node).
   - Sculptor → Geomancer 4-piece set + Sculptor Staff (one node, smart_filter or multi-task).
   - Naga → Naga Fang → Naga Fang Dagger (`naga_fang_dagger`, verified).
   - Elokosa → collect the three moon paws (existing `0713486EDCE7D787` smart_filter).
   - Optional side node: Umvuthana Mask of Fury/Faith (existing masks node), `earthrend_gauntlet`.
2. **Lane 2 — The Dark Metal Armory (Born in Chaos, ~7 nodes).** Convert the bestiary
   into a crafting progression: Dark Metal (existing `...101F`) → Dark Metal armor set
   (`dark_metal_armor_helmet/chestplate/leggings/boots`, smart_filter, verified) → one
   dark weapon choice (`choice`/smart_filter across `darkwarblade`/`nightmare_scythe`/
   `soul_cutlass`) → one charm (`charmof_power` etc.) → one elixir the player actually uses
   (`elixir_of_vampirism` for a drawn-out fight). Keep `supreme_bonescaller` / `sir_pumpkinhead`
   as the lane's ONE boss node each IF canon allows minibosses; otherwise fold to drops.
3. **Lane 3 — Relics of the Fallen (Monster Plus + Alchemist's Garden, ~5 nodes).**
   Monster Plus becomes a short relic line: `ancient_scroll` + `ancient_broken_sword`
   (item tasks, no kills) → optional crystal or dark gear piece. Alchemist's Garden Gnome
   King + Spider Queen stay as the two optional side-boss trophies (loot bags), tucked at
   the lane's tail with `optional:true`.
4. **Capstone — The Great Hunt (existing `...1050-1054`).** UNCHANGED. Four great beasts,
   3-of-4, grants the_renaissance. This is already the correct boss-anchored gate.

- **Kills remaining:** only genuine bosses — 4 mowzies headliners + 4 Great Hunt mowzies
  + 2 alchemists_garden side bosses (+ up to 3 born_in_chaos minibosses pending canon call).
  Zero ordinary-mob kills.
- **Dep-flow:** three parallel vertical lanes off the metallurgy gate, converging on the
  Great Hunt column on the right. Crossing-free by construction (lanes never interleave).
- **Reward pacing:** each lane-end gives the signature gear as an item reward + modest xp;
  capstone keeps the stage grant. Side bosses keep loot bags.
- **Migration safety:** preserve `...1054`, `...1050-1053`, `...100C`/`1010`/`1013`/`1019`
  boss ids and the metallurgy gate dep. Rebuild the middle/top clusters with fresh ids for
  new/merged nodes; delete pure-pest kill nodes (all leaves).

### Concept C — "Two-family focus: cut Monster Plus, deepen Mowzies + Born in Chaos" (SCOPE CUT)
**Pitch:** Monster Plus is the shallowest of the three and its cluster is where most of
the ordinary-mob kills + a phantom-feeling "corrupted ancient hero" lane live. Drop Monster
Plus from the chapter entirely (or reduce to a single optional `ancient_broken_sword`
node), and give the freed space to the two headliner families.

- **Mowzies:** full gear tour as in Concept B lane 1, plus add `blowgun`+`dart` and
  `sol_visage` / `sand_rake` as optional curios (all verified) so the marquee mod gets its
  due depth.
- **Born in Chaos:** the Dark Metal → armor → weapon → charm → elixir line from Concept B,
  plus keep 1–2 real bosses.
- **Monster Plus:** removed or a single optional relic node.
- **Nodes:** ~20, tightest of the three. Cleanest crossing-free layout (two lanes only).
- **Trade-off:** loses Monster Plus's crystal/dark gear content from the questbook, though
  the mod stays in the pack and its gear remains craftable. Best if the user wants the
  Medieval combat capstone lean and marquee-focused rather than comprehensive.
- **Migration safety:** same preserved-id set; Monster Plus nodes (`...300A`, `...300E/F`,
  `442C27F2E00B325C`, `7B26069EC5CF71D4`, `5468102A19D28104`, `31F70E7481C6CE82`, etc.) are
  all leaves/local — safe to delete. None are externally referenced.

---

## 4. Migration hazards (externally-referenced IDs — MUST preserve)

Grep across `config/ftbquests/quests/**` confirms only these grove IDs are referenced
outside the chapter:

| ID | What | Referenced by | Rule |
|---|---|---|---|
| `6D7E8F901A2B1054` | Capstone "Master of the Grove" (the_renaissance grant) | `ren_magic_foundations.snbt:15`, `ren_deeper_darker_otherside.snbt:15`, `ren_second_mill_steam_rail_logistics.snbt:15`, `journey_to_ascension.snbt:87` (`check_quest` mirror) | **NEVER re-id or remove.** All Renaissance tabs open off this. |
| `097AED7C91033D5E` | Entry gate — NOT in this file; it is metallurgy's "Entering the Iron Era" | grove nodes dep on it; also `journey_to_ascension.snbt:65` (`check_quest`) | External gate. Keep the grove's root nodes depending on it. |
| `6D7E8F901A2B0501` | Chapter id | chapter file self + lang `chapter.6D7E8F901A2B0501.*` | Keep chapter id + lang keys. |
| `6D7E8F901A2B1050/1051/1052/1053` | Great Hunt four beasts (feed capstone) | internal only, but they ARE the capstone fan-in | Keep as the boss gate. |

The other files that matched `097AED7C91033D5E` (`entering_the_iron_era`, `m1_first_mill`,
`m3_relics_and_burrows`, `stone_food_and_farming_pressures`, `minecolonies`) reference it
as a Medieval-progression dependency; none reference grove's internal kill/drop node ids.
So **all deletions/retargets in Concepts A–C touch only leaf nodes with no external deps.**

Also preserve on save: the inert `SkillsLevel` / `PlayerSpells` blocks on every task
(regenerating More Quest Types artifact), and the mixed CRLF byte structure.

**Verification note:** `dark_metal_block` and `tombstone_the_gentleman_frog` are
`block.*` lang keys (not `item.*`) but resolve as items in-game (verified present in
born_in_chaos lang). Monster Plus dark set is helmet+chestplate ONLY (no leggings/boots) —
do not author a full "dark set" node for it.

---

## Recommendation

**Concept B ("Arm Yourself Against the Dark").** It directly implements the user's ruling
(zero ordinary-mob kills, bosses only), fixes the "flow feels bad" complaint by replacing
one sprawling three-cluster web with three clean parallel equip-lanes, and honors the
mowzies gear-first design + the Living Harvest item-based precedent. It preserves the
load-bearing capstone/gate IDs and the correct boss-anchored age fan-in. Concept A is the
safe fallback if the user wants minimal churn; Concept C is the pick if they want the
Medieval capstone lean and mowzies-forward. One canon call needed for all three: are
born_in_chaos `supreme_bonescaller` / `sir_pumpkinhead` / `dire_hound_leader` "bosses" (keep
kills) or "ordinary" (retarget to drops)?
