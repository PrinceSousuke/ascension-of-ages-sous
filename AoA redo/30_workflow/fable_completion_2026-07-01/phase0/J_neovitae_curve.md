# J — Neo Vitae progression curve: resolving the 12 tier mismatches

Phase 0, generated 2026-07-02. **Audit-only.** No files edited outside `phase0/`. No git.
Every claim below carries a jar path, a chapter file:line, or a KubeJS file:line.

Jar inspected: `mods/neovitae-1.21.1-1.0.25.jar` (extracted to scratchpad).
Locks: `kubejs/server_scripts/aoa_astages_01m_magic.js` + `aoa_astages_03_dimension_restrictions.js`.
Weaves: `kubejs/server_scripts/aoa_recipes_neovitae_weaves.js`.
Chapters: `config/ftbquests/quests/chapters/{ren_magic_foundations,ren_nether_threshold,ir_magic_feedstock_and_spectrum_network}.snbt`.

---

## 1. The REAL Neo Vitae progression chain (jar-verified)

Neo Vitae is a Blood Magic fork. Two apparatus pillars: the **Ara Vitae** (blood altar,
consumes Essentia Vitae) and the **Hellfire Forge** (consumes Spiritus). Progression runs
Orb tier + Altar tier in lockstep, with the Demon Realm dungeon as the mid-game gate.

### 1a. Two economies, two resources

- **Essentia Vitae (blood)** — self-sacrifice at the Ara Vitae, fills your **Orb of Vitae**.
  Orb tier = how much blood you can bank + which altar-crafts you can attempt.
- **Spiritus (demonic will)** — "coalesces naturally around certain creatures"
  (jar: `book.neovitae.guide.spiritus.aura.intro.text`). **You obtain Spiritus by killing
  ordinary overworld hostile mobs**, exactly like Blood Magic demon will. It does NOT
  require the dungeon. Spiritus is spent at the **Hellfire Forge**.

### 1b. Altar (Ara Vitae) tiers — jar `guide.altar.ara_vitae.tier1..tier6`

| NV Altar Tier | Structure | Corner capstone block | Gating material |
|---|---|---|---|
| T0 | lone Ara Vitae | none | furnace + gold + vitae_stone (craft) |
| T1 | 8 blank runes | none | blank runes only |
| T2 | 28 runes + pillars | **Blood Stained Glass** | craftable (Ren-legal) |
| T3 | 56 runes | **Bloodstone Bricks** | needs **Tau Fruit** (from "Breaching the Edge of Demon Realm" ritual) |
| T4 | 108 runes | **Hellforged Blocks** | **Demon Realm metal (dungeon)** |
| T5 | 184 runes | **Crystal Clusters** | sculk + Tabula Aetherea + weak_blood_shard + **nether star** |

**Cadence finding:** T0–T2 are fully craftable with Renaissance materials. **T3 is the
gate** — its capstone (Bloodstone Bricks) needs **Tau Fruit**, which comes from the
"Breaching the Edge" ritual that opens the Demon Realm. T4 needs Hellforged Blocks (dungeon
metal). T5 needs a nether star. So the natural altar cadence is **T0–T2 Renaissance,
T3–T4 IR (dungeon era), T5 late-IR/Gilded**. This matches the intended AoA spine well.

### 1c. Blood Orb tiers — jar `type: "neovitae:orb_tier"` used as a recipe *ingredient gate*

The 60 datapack recipes reference `orb_tier` as a minimum-orb ingredient (they do NOT make
orbs; orbs are code-registered). Observed thresholds:
- `orb_tier 0`: incense_altar, rune_blank, rune_orb, lava_crystal (Renaissance entry)
- `orb_tier 1`: ritual_stone_blank, rune_sacrifice
- `orb_tier 2`: athanor, ritual_stone_master, experience_tome, furnacecell
- `orb_tier 3`: ritual_reader, rune_charging, rune_acceleration, rune_capacity_augmented
- `orb_tier 4`: rune_efficiency

Lang orb names (`item.neovitae.blood_orb_*`): weak (Novicius, T0), apprentice (Discipulus, T1),
magician (Veneficus, T2), master (Magus, T3), archmage (Dominus, T4), transcendent (Divinus, T5).

**Dungeon-access rule (decisive quote):** `guide.dungeons.demon_crafting.intro.text` —
*"All recipes in this section require at minimum a tier 3 altar and blood orb to have reached
the dungeons in the first place."* → **The Demon Realm dungeon is gated behind T3 altar +
T3 (master) orb**, i.e. mid-progression, not entry.

### 1d. Spiritus Gems — jar `guide.spiritus.spiritus_gems.*`

Made in the **Hellfire Forge** from Spiritus (overworld-mob-sourced) + vanilla/altar mats.
**None of petty/lesser/common require the dungeon:**

| Gem | Recipe (jar guide) | Dungeon needed? |
|---|---|---|
| **Petty** | first vessel, forge-made from loose Spiritus | **No** |
| **Lesser** | petty + Diamond + Lapis + Redstone (forge) | **No** |
| **Common** | lesser + Tabula Animata + Diamond + Gold Block (forge) | **No** |
| **Greater** | common + Tabula Spiritus + Weak Blood Shard + Spiritus Crystal | No (Spiritus Crystal is Aura-grown via Crystallarium) |
| **Grand** | greater + Animus Mote + Tabula Aetherea + **Permafrost Core** | **YES — Permafrost Core drops from Glaciaris, a Demon Realm apex boss** (`guide.dungeons.demon_crafting.grand_gem.text`) |

So the gem ladder that is genuinely dungeon-gated is **Grand only**. Petty→Greater are all
obtainable from the Hellfire Forge with overworld Spiritus + craftable reagents.

### 1e. Hellforged / Demonite chain — **dungeon-only, verified**

- Advancements: *"Unearth a sliver of raw Demonite from the Endless Realm"*
  (`advancements.neovitae.demonite.description`) and *"Smelt raw Demonite into a Hellforged
  Ingot"* (`advancements.neovitae.hellforged_ingot.description`).
- Demon Realm dimension: `data/neovitae/dimension/dungeon.json` (`neovitae:dungeon`, biome
  `neovitae:dungeon_void`). Raw Demonite drops from mid/elite/apex Daemonium
  (`guide.dungeons.demon_bestiary.*` — Voraxis rare, Corrodis/Doloris/Fervidis/Ignis/Glaciaris).
- Block class `com/breakinblocks/neovitae/common/block/dungeon/BlockPrismaticDemonite.class`
  confirms the ore is a dungeon block. There is **no overworld / altar / smeltery route** to
  raw demonite in the datapack — hellforged is intrinsically Demon-Realm-sourced.
- Datapack only has crafting-grid recipes: `raw_demonite_from_block`, `hellforged_block_from_ingots`,
  `hellforged_ingot_from_block` (block↔ingot only; the demonite→ingot smelt is code/loot).

**Conclusion: hellforged is legitimately dungeon-gated and CANNOT be made Renaissance-legal
without inventing an off-design bypass.** No Ren-legal route exists or should be forged.

### 1f. Sentient Equipment — jar `guide.alchemy_arrays.sentient_equipment.*`

Requires: **Iron Armour + Arcane Scribe Tool + Binding Reagent + at least a Common Spiritus
Gem** charged with Spiritus. Created on an **Alchemy Array** (Renaissance-craftable table),
NOT the dungeon. Since a Common gem is reachable **without** the dungeon (§1d), **sentient
armor is obtainable as soon as you have: Hellfire Forge + Common gem + iron armor.** That
is a late-IR capability (Hellfire Forge is IR-locked), not a Gilded one. The pack's weave
`aoa_recipes_neovitae_weaves.js:9-17` confirms sentient gear is forge-transform output using
`spiritus_gem_petty` as a catalyst.

---

## 2. The live NV lock ladder (`aoa_astages_01m_magic.js`)

| Age | Items locked (lines 113-164) |
|---|---|
| **Renaissance** | ara_vitae, incense_altar, alchemy_array, athanor, tabula_vitae, blood_orb_weak, blood_orb_apprentice, weak_blood_shard, blood_pearl, bloodstone(+brick), blood_stained_glass, blood_tank, blood_battery |
| **IR** | hellfire_forge, vas_maleficum, spira_infernalis, crystallarium_maleficum, spirit_cache, **spiritus_gem_petty/lesser/common (133-135)**, teleposer, tabula_robur/animata/spiritus, **ingot_hellforged, hellforged_dust/parts/resonator/block (145-149)**, demonite_trim_ingot |
| **Gilded** | blood_orb_magician/master/archmage, spiritus_gem_greater/grand (151-152), **sentient_helmet/plate/leggings/boots/sword/pickaxe/axe (153-159)** |
| **Atomic** | blood_orb_transcendent, hellforged_explosive_cell, crystal_cluster(+brick) |

Dimension lock (`aoa_astages_03:25`): `["industrial_revolution", "neovitae:dungeon"]`.

**Internal contradiction in the lock file:** petty/lesser/common gems are locked **IR**
(133-135) but greater/grand are **Gilded** (151-152), while the jar makes petty→common with
*zero dungeon dependency* and greater without the dungeon too. The lock treats the whole gem
ladder as post-Hellfire-Forge (IR), which is correct for petty/lesser/common (they need the
forge). The mismatch is the **quests placing them in Renaissance**, not the lock.

---

## 3. The 12 mismatches, and which side is wrong

### Group A — Renaissance quests → IR-locked hellforged (5 rows, `ren_nether_threshold.snbt`)

Nodes (all `optional: true`, `hide_until_deps_visible: true`):
- `0B03102000000041` hellforged_dust (task line 179)
- `0B03102000000042` ingot_hellforged (task line 212)
- `0B03102000000046` hellforged_parts (task line 278)
- `0B03102000000047` hellforged_block (task line 312)
- `0B03102000000081` spiritus_gem_petty (task line 1019)

**Wrong side = the QUEST placement.** Hellforged is dungeon-sourced and the dungeon is
correctly IR (a T3-altar/orb mid-game gate per §1c). Down-tiering hellforged to Renaissance
would require breaking the dungeon gate and inventing an overworld demonite route — a canon
violation and a boss-buildup inversion (see §5). These tasks belong in an IR chapter. The
chapter is even ICON'd on `neovitae:ingot_hellforged` (line 8) — the whole hellforged branch
was scaffolded in the wrong age.

### Group B — Renaissance quests → IR-locked spiritus gems (3 rows, `ren_magic_foundations.snbt`)

- `0B03101000000038` spiritus_gem_petty (task line 1280, `optional: true`)
- `0B03101000000070` spiritus_gem_lesser (task line 1891)
- `0B03101000000075` spiritus_gem_common (task line 2056)

**Wrong side = the QUEST placement, BUT the tier is close.** Gems need the Hellfire Forge,
which is IR. They do NOT need the dungeon (§1d), so they are early-IR items, not Gilded. The
lock (IR) is correct; the Renaissance placement is one age too early. Move to IR.

### Group C — IR quests → Gilded-locked Sentient armor (4 rows, `ir_magic_feedstock_and_spectrum_network.snbt`)

Nodes (**NOT optional** — required-spine, `hide_until_deps_visible: true`):
- `49540B100000001B` sentient_helmet (task line 1098)
- `49540B100000001C` sentient_plate (task line 1143)
- `49540B100000001D` sentient_leggings (task line 1188)
- `49540B100000001E` sentient_boots (task line 1233)

**Wrong side = the LOCK (down-tier to IR).** Per §1f the jar makes sentient armor from a
Common gem + iron armor on an Alchemy Array — all reachable at IR once the Hellfire Forge is
built. The Gilded lock is over-conservative. These are required IR-chapter nodes, so this is
the most severe mismatch (a required task the player physically cannot complete at its age).
Down-tiering sentient_helmet/plate/leggings/boots to `industrial_revolution` matches the jar
and unblocks the required node. (Leave sentient_sword/pickaxe/axe — used only in OW6 §4 — a
canon call, but they too are IR-capable; recommend also IR for consistency.)

### Reference (not a mismatch): `ow6_beyond_the_veil.snbt`

OW6 tasks petty/greater gems + sentient gear + smart_filters. All are legal at Otherworldly
(≥ their unlock age), so OW6 is fine — it is the intended optional depth re-use of the spine.

---

## 4. Per-mismatch recommendation table

| # | Item | Quest node | Chapter (age) | Lock age | Wrong side | Recommendation | Difficulty effect |
|---|---|---|---|---|---|---|---|
| 1 | hellforged_dust | 0B03102000000041 | ren_nether_threshold (Ren) | IR | **quest** | **(b) Move to an IR chapter** (ir_magic_feedstock or citadel) | Keeps dungeon as the IR mid-gate; no easier |
| 2 | ingot_hellforged | 0B03102000000042 | ren_nether_threshold | IR | **quest** | (b) Move to IR | same |
| 3 | hellforged_parts | 0B03102000000046 | ren_nether_threshold | IR | **quest** | (b) Move to IR | same |
| 4 | hellforged_block | 0B03102000000047 | ren_nether_threshold | IR | **quest** | (b) Move to IR | same |
| 5 | spiritus_gem_petty | 0B03102000000081 | ren_nether_threshold | IR | **quest** | (b) Move to IR (dedupe with #6) | forge-gated, natural IR |
| 6 | spiritus_gem_petty | 0B03101000000038 | ren_magic_foundations (Ren) | IR | **quest** | (b) Move to IR | forge-gated |
| 7 | spiritus_gem_lesser | 0B03101000000070 | ren_magic_foundations | IR | **quest** | (b) Move to IR | forge-gated |
| 8 | spiritus_gem_common | 0B03101000000075 | ren_magic_foundations | IR | **quest** | (b) Move to IR | forge-gated |
| 9 | sentient_helmet | 49540B100000001B | ir_magic_feedstock (IR) | Gilded | **lock** | **(a) Down-tier lock to IR** | jar-legal at IR; unblocks required node |
| 10 | sentient_plate | 49540B100000001C | ir_magic_feedstock | Gilded | **lock** | (a) Down-tier to IR | same |
| 11 | sentient_leggings | 49540B100000001D | ir_magic_feedstock | Gilded | **lock** | (a) Down-tier to IR | same |
| 12 | sentient_boots | 49540B100000001E | ir_magic_feedstock | Gilded | **lock** | (a) Down-tier to IR | same |

Route (c) "re-recipe via KubeJS weave for a Ren-legal hellforged route" is **rejected** for
#1–5: it would break the dungeon-as-IR-gate and create the boss-buildup inversion in §5.

---

## 5. Boss-buildup judgment (the user's criterion)

- **Renaissance → Maledictus.** A Ren player should have: Ara Vitae **T0–T2**, weak/apprentice
  orb, weak_blood_shard, incense altar, basic runes/sigils, the Alchemy Array, and self-sac
  blood tooling. They should **not** yet have Spiritus gems, the Hellfire Forge, or anything
  Demon-Realm. That is enough magic identity to face Maledictus without leaning on dungeon
  metal. **So the hellforged + gem tasks must LEAVE Renaissance** — putting them there both
  softlocks the optional node and would over-arm the Ren player if it worked.
- **IR → Obsidilith.** An IR player should build the **Hellfire Forge**, harvest Spiritus from
  overworld mobs, climb **petty → lesser → common** gems, breach the **Demon Realm** (T3
  altar/orb), farm **hellforged**, and forge **Sentient armor**. This is a full, satisfying
  mid-game arc that arms the player for Obsidilith. All 12 mismatched items land naturally in
  this band. Down-tiering sentient armor to IR (Group C) *completes* this arc rather than
  deferring its payoff to Gilded.
- **Gilded → Void Titan.** Gilded should own the **high orbs (magician/master/archmage),
  greater/grand gems**, T5 altar, and sentient *evolution/upgrades*. Those stay Gilded. So the
  Gilded magic tier is not emptied by moving sentient *armor* down — Gilded keeps the orb
  ceiling, the grand gem (dungeon-apex-boss gated), and the upgrade rituals.

Net: the corrected ladder makes each age's magic capability build toward its boss, with the
Demon Realm as the IR centerpiece (right where a T3-altar mid-game gate belongs).

---

## 6. Proposed final NV item → age placement ladder

| Age | Altar/Orb | Gems | Forge/Hellforged | Gear | Notes |
|---|---|---|---|---|---|
| **Renaissance** | Ara Vitae T0–T2, orb weak+apprentice, weak_blood_shard, blood_pearl, bloodstone(+brick/glass), blood_tank/battery, incense altar, blank/basic runes, Alchemy Array, Tabula Vitae | — | — | — | entry magic literacy; matches current Ren locks (correct) |
| **IR** | Ara Vitae **T3–T4**, orb **magician→master**, Tabula Robur/Animata/Spiritus, Vas Maleficum, Spira Infernalis, Crystallarium, spirit_cache, teleposer | **petty, lesser, common** (forge) | **Hellfire Forge; Demon Realm access (T3 gate); ingot/dust/parts/resonator/block; demonite_trim** | **Sentient helmet/plate/leggings/boots (+sword/pick/axe)** ← DOWN-TIER from Gilded | the mid-game centerpiece; unblocks the required IR node |
| **Gilded** | Ara Vitae **T5**, orb **archmage**, sentient *evolution/upgrade* rituals | **greater, grand** (grand = Glaciaris apex drop) | crystal cluster reagents remain higher | sentient upgrades / specialization | keeps orb ceiling + apex-boss-gated grand gem |
| **Atomic** | orb **transcendent** | — | **hellforged_explosive_cell, crystal_cluster(+brick)** | — | apex depth; unchanged (correct) |

### Changes this implies (for the implementation phase, not this audit)
1. **Move** the 5 hellforged/petty nodes out of `ren_nether_threshold` into an IR chapter
   (natural host: `ir_magic_feedstock_and_spectrum_network`, which already teaches the
   Hellfire Forge at node `49540B1000000004` and hellforged_block at `49540B1000000018`).
   Re-anchor `ren_nether_threshold`'s icon off `ingot_hellforged`.
2. **Move** the 3 gem nodes out of `ren_magic_foundations` into the same IR magic chapter,
   sequenced petty → lesser → common after the Hellfire Forge node.
3. **Down-tier** the AStages locks for `sentient_helmet/plate/leggings/boots` (and, recommended,
   `sentient_sword/pickaxe/axe`) from `gilded_age` → `industrial_revolution` in
   `aoa_astages_01m_magic.js:153-159`. Jar-justified (§1f).
4. No recipe weave needed; no dungeon gate change. Grand gem stays Gilded (its Permafrost Core
   is an apex-boss drop, a legitimately Gilded-tier reagent).

**Canon calls flagged (do not silently execute):** (i) whether hellforged/gem nodes move to IR
vs. the lock down-tiers — this report recommends MOVE for hellforged (dungeon is a real IR gate)
and MOVE for gems (forge is IR); (ii) whether sentient tools (sword/pick/axe) down-tier with the
armor. Both are design decisions for the authoring phase.
