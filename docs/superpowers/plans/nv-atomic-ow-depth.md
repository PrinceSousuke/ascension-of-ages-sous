# Neo Vitae Atomic / OW Optional-Depth Insertion Design

**Status:** Design checkpoint — DO NOT edit any chapter or lang file based on this doc until Tasks 5.2 / 5.3 are authorised.

---

## 1. Host Selection

### 1.1 Atomic Wing Host

**Chosen file:** `config/ftbquests/quests/chapters/at7_chaos_convergence.snbt`

**Rationale:** at7 is the final Atomic chapter and already hosts a mix of required boss-proof nodes and existing optional side wings (Spectrum Deeper Down, AlexsCaves, Industrial Foregoing, FDBosses). The capstone node `4358010000010003` (fan-in from all Atomic proof chains, grants `at_capstone_complete` + `otherworldly`) is available as a convergence target for optional fan-in dependencies. The chapter ends at x ≤ 17.0, leaving clear open space to the right and below.

**Group ID:** `7D28E4AEBC440F10`

**Existing node-id prefix patterns in at7:**
- Required chain: `4646xxxxxxxxxxxxxx` (Macabre bosses) and `4358010000010xxx` (Spectrum / Geburah required)
- Optional wings already authored: `4358011000000100` through `4358011000000107` (Spectrum Bedrock/Portal, AlexsCaves wings, FDBosses loot, IF Infinity, IF Hammer)
- Task ids: `4358012000xx0001`, Reward ids: `4358013000xx0001`
- Highest optional suffix pair in use: quest `4358011000000107` / task `43580120000E0002`

**Free id block for NV Atomic wing:**

Use a new prefix block: `NV` signal = second byte `EE` in the quest octet. Proposed range:

| Role | Prefix | Example first id |
|---|---|---|
| Quest nodes | `4358011000EE0001`..`4358011000EE000A` | `4358011000EE0001` |
| Task nodes  | `4358012000EE0001`..`4358012000EE002F` | `4358012000EE0001` |
| Reward nodes | `4358013000EE0001`..`4358013000EE001F` | `4358013000EE0001` |

Verify no collision: existing optional quest ids stop at `4358011000000107`; `EE` in byte position 10-11 is unused (verified via grep — existing ids use `00`, `01` in that position only).

**Free x/y region:**

Existing nodes occupy x range –4 to 17, y range –4 to 10.5 (at5) and –4 to 4 (at7 main). The NV wing will hang off the capstone node `4358010000010003` at (x=13.0, y=–3.0) and expand **downward** into the clear region:

- NV branch anchor: x = 13.0, y = –6.0 (first NV node, dep on `4358010000010000` Spectrum entry)
- Wing spans: x = 11 to 16, y = –6 to –14 (clear; nothing exists below y = –4.5 in at7)

---

### 1.2 OW Wing Host

**Chosen file:** `config/ftbquests/quests/chapters/ow6_beyond_the_veil.snbt`

**Rationale:** ow6 is the only OW chapter and already contains the OW capstone `4256010000010006` (grants `ow_capstone_complete` + `ascension`). The Sentient gear and Spiritus economy are OW-depth content that naturally clusters here as an optional magic-flavour wing.

**Group ID:** `080F7BA9FFB8FC07`

**Existing node-id prefix patterns in ow6:**
- Quests: `4256010000010001` through `4256010000010006`
- Task ids: `4256020000010xxx`
- Reward ids: `4256030000010xxx`
- x range: –4.0 to 8.0, y range: 0.0 to 3.0

**Free id block for NV OW wing:**

Use prefix block `NV` signal = `EE` in octet 5:

| Role | Prefix | Example first id |
|---|---|---|
| Quest nodes | `4256011000EE0001`..`4256011000EE000F` | `4256011000EE0001` |
| Task nodes  | `4256012000EE0001`..`4256012000EE002F` | `4256012000EE0001` |
| Reward nodes | `4256013000EE0001`..`4256013000EE001F` | `4256013000EE0001` |

Verify no collision: existing quest ids use `4256010000010001..6`; `4256011000EE...` is entirely unused.

**Free x/y region:**

Existing nodes occupy x = –4.0 to 8.0, y = 0.0 to 3.0. The NV wing hangs off quest `4256010000010001` (fusion reactor entry, x=–4, y=0) and expands **upward** (negative y direction in FTBQ canvas):

- NV branch anchor: x = –4.0, y = –3.0 (first NV node, dep on `4256010000010001`)
- Wing spans: x = –7 to 2, y = –3 to –15 (clear; nothing exists above the y=0 row in ow6)

---

## 2. Atomic Wing Quest List

All quests: `optional: true`, `hide_until_deps_complete: true`, zero `/astages add ... atomic` command rewards.

Dependency anchor: the Spectrum entry quest `4358010000010000` (x=11, y=0) — already the branch-off point for all at7 optional wings.

### 2a. Transcendent Altar Sub-Wing

| # | Node ID | Task Type | Task Item | Dep On | Optional | Title Sketch | Desc Sketch |
|---|---|---|---|---|---|---|---|
| AT-NV-1 | `4358011000EE0001` | `item` | `neovitae:crystal_cluster` | `4358010000010000` | true | "Crystalline Resonance" | Grow and harvest a Crystal Cluster, the keystone material of the Transcendent altar tier. Place it in your sanctum to begin the highest Blood Magic progression. |
| AT-NV-2 | `4358011000EE0002` | `item` | `neovitae:crystal_cluster_brick` | `4358011000EE0001` | true | "The Sacred Masonry" | Craft Crystal Cluster Bricks to construct the Transcendent altar structure. The altar's power is contained in its geometry. |
| AT-NV-3 | `4358011000EE0003` | `item` | `neovitae:blood_orb_transcendent` | `4358011000EE0002` | true | "Apex of the Covenant" | Attune a Transcendent Blood Orb at the completed altar. This is the culmination of every blood ritual you have performed — the orb at the apex of the covenant. |

### 2b. Dungeon Line Sub-Wing

| # | Node ID | Task Type | Task Item / Dimension | Dep On | Optional | Title Sketch | Desc Sketch |
|---|---|---|---|---|---|---|---|
| AT-NV-4 | `4358011000EE0004` | `item` | `neovitae:simple_key` | `4358011000EE0003` | true | "Key to the Pit" | Forge a Simple Key from hellforged reagents. The dungeon does not announce itself — you must find the entrance and unlock it yourself. |
| AT-NV-5 | `4358011000EE0005` | `dimension` | `neovitae:dungeon` | `4358011000EE0004` | true | "Descent into the Dungeon" | Enter the Neo Vitae dungeon dimension. The architecture here is alien and hostile — study it. |
| AT-NV-6 | `4358011000EE0006` | `item` | `neovitae:standard_key` | `4358011000EE0005` | true | "Standard Clearance" | Obtain a Standard Key from the dungeon's inhabitants. The deeper corridors require this authorization. |
| AT-NV-7 | `4358011000EE0007` | `item` | `neovitae:hellforged_explosive_cell` | `4358011000EE0006` | true | "Hellforged Ordnance" | Craft a Hellforged Explosive Cell — the dungeon's deep reagent, distilled from demonite and blood. A weapon and a ritual component. |

### 2c. Gear Reward Sub-Wing (hangs off AT-NV-5)

| # | Node ID | Task Type | Task Item | Dep On | Optional | Title Sketch | Desc Sketch | Reward |
|---|---|---|---|---|---|---|---|---|
| AT-NV-8 | `4358011000EE0008` | `item` | `neovitae:demonite_trim_ingot` | `4358011000EE0005` | true | "Demonite Cache" | Mine Demonite from the dungeon ore veins. The ore's dark resonance makes it uniquely useful for weapon augmentation. | 250 XP |
| AT-NV-9 | `4358011000EE0009` | `item` | `neovitae:boss_key` | `4358011000EE0007` | true | "The Foreman's Gate" | Obtain a Boss Key from the dungeon's Foreman encounter. The reward is not the key — it is the gear the Foreman drops. | 350 XP + random loot |

### Node Positions (at7 canvas, hanging below y=–4.5)

```
AT-NV-1  x=13.0  y=–6.0    (dep: 4358010000010000)
AT-NV-2  x=13.0  y=–8.0    (dep: AT-NV-1)
AT-NV-3  x=13.0  y=–10.0   (dep: AT-NV-2)
AT-NV-4  x=13.0  y=–12.0   (dep: AT-NV-3)
AT-NV-5  x=13.0  y=–14.0   (dep: AT-NV-4)
AT-NV-6  x=11.0  y=–14.0   (dep: AT-NV-5)
AT-NV-7  x=11.0  y=–12.0   (dep: AT-NV-6)
AT-NV-8  x=15.0  y=–14.0   (dep: AT-NV-5)
AT-NV-9  x=15.0  y=–12.0   (dep: AT-NV-7)
```

### Task id assignments (AT wing)

| Quest | Task id(s) | Reward id(s) |
|---|---|---|
| AT-NV-1 | `4358012000EE0001` | `4358013000EE0001` (xp 150) |
| AT-NV-2 | `4358012000EE0002` | `4358013000EE0002` (xp 200) |
| AT-NV-3 | `4358012000EE0003` | `4358013000EE0003` (xp 400) |
| AT-NV-4 | `4358012000EE0004` | `4358013000EE0004` (xp 100) |
| AT-NV-5 | `4358012000EE0005` | `4358013000EE0005` (xp 150) |
| AT-NV-6 | `4358012000EE0006` | `4358013000EE0006` (xp 150) |
| AT-NV-7 | `4358012000EE0007` | `4358013000EE0007` (xp 300) |
| AT-NV-8 | `4358012000EE0008` | `4358013000EE0008` (xp 250) |
| AT-NV-9 | `4358012000EE0009` | `4358013000EE0009` (xp 350), `4358013000EE000A` (random) |

---

## 3. OW Wing Quest List

All quests: `optional: true`, `hide_until_deps_complete: true`, zero stage grants.

Dependency anchor: `4256010000010001` (Fusion Reactor entry quest, x=–4, y=0) — the first required OW6 node and the thematic entry point for high-end OW content.

### 3a. Sentient Gear Set Sub-Wing

| # | Node ID | Task Type | Task Item | Dep On | Optional | Title Sketch | Desc Sketch |
|---|---|---|---|---|---|---|---|
| OW-NV-1 | `4256011000EE0001` | `item` | `neovitae:sentient_sword` | `4256010000010001` | true | "The Sentient Blade" | Forge a Sentient Sword — a weapon that learns from its wielder. Blood fuels it; mastery shapes it. |
| OW-NV-2 | `4256011000EE0002` | `item` (smart filter: helmet/plate/leggings/boots) | `ftbfiltersystem:smart_filter` (or(sentient_helmet, sentient_plate, sentient_leggings, sentient_boots)) | `4256011000EE0001` | true | "Armour of Living Metal" | Complete the Sentient armour set. Each piece is infused with blood-soul resonance. |
| OW-NV-3 | `4256011000EE0003` | `item` | `neovitae:sentient_pickaxe` | `4256011000EE0002` | true | "Sentient Toolkit" | Obtain both the Sentient Pickaxe and Axe — the living toolset that amplifies your extraction capabilities. Use a smart filter for either pickaxe or axe. |

### 3b. Spiritus Economy Sub-Wing

| # | Node ID | Task Type | Task Item | Dep On | Optional | Title Sketch | Desc Sketch |
|---|---|---|---|---|---|---|---|
| OW-NV-4 | `4256011000EE0004` | `item` | `neovitae:spiritus_gem_petty` | `4256010000010001` | true | "First Spiritus" | Collect a Petty Spiritus Gem — the smallest denomination of soul-matter. Begin cultivating the aspect economy. |
| OW-NV-5 | `4256011000EE0005` | `item` (smart filter: lesser/common/greater/grand) | `ftbfiltersystem:smart_filter` | `4256011000EE0004` | true | "Ascending Aspects" | Refine Spiritus Gems from Lesser through Grand. Each tier unlocks deeper ritual synthesis. |
| OW-NV-6 | `4256011000EE0006` | `item` (smart filter: raw/invictus/nihilum/ruina/vindicta) | `ftbfiltersystem:smart_filter` | `4256011000EE0005` | true | "The Five Souls" | Obtain all five Spiritus soul types: Raw, Invictus, Nihilum, Ruina, and Vindicta. The complete soul palette opens every high-tier ritual. |

### 3c. Ascension Flavour Capstone Sub-Wing

| # | Node ID | Task Type | Task Item | Dep On | Optional | Title Sketch | Desc Sketch | Reward |
|---|---|---|---|---|---|---|---|---|
| OW-NV-7 | `4256011000EE0007` | `item` | `neovitae:blood_orb_transcendent` | `4256011000EE0003`, `4256011000EE0006` | true | "Blood Beyond the Veil" | Bear the Transcendent Blood Orb into the Otherworldly age. The magic of Neo Vitae has accompanied you to the frontier of the known world. | 500 XP. This quest is a fan-in dep ONLY — no stage grant. |

Note: OW-NV-7 fans into `4256010000010006` (OW capstone) as an OPTIONAL dependency only if the design wishes to document it. Per the invariants, it must NOT be a required dep for the capstone — it remains a standalone optional quest. No fan-in wiring to the capstone is required.

### Node Positions (ow6 canvas, above y=0 row — negative y is upward on FTBQ canvas)

```
OW-NV-1  x=–4.0  y=–3.0   (dep: 4256010000010001)
OW-NV-2  x=–4.0  y=–5.0   (dep: OW-NV-1)
OW-NV-3  x=–4.0  y=–7.0   (dep: OW-NV-2)
OW-NV-4  x=–1.0  y=–3.0   (dep: 4256010000010001)
OW-NV-5  x=–1.0  y=–5.0   (dep: OW-NV-4)
OW-NV-6  x=–1.0  y=–7.0   (dep: OW-NV-5)
OW-NV-7  x=–2.5  y=–9.0   (dep: OW-NV-3, OW-NV-6)
```

### Task id assignments (OW wing)

| Quest | Task id(s) | Reward id(s) |
|---|---|---|
| OW-NV-1 | `4256012000EE0001` | `4256013000EE0001` (xp 200) |
| OW-NV-2 | `4256012000EE0002` (smart_filter) | `4256013000EE0002` (xp 300) |
| OW-NV-3 | `4256012000EE0003` (smart_filter) | `4256013000EE0003` (xp 250) |
| OW-NV-4 | `4256012000EE0004` | `4256013000EE0004` (xp 100) |
| OW-NV-5 | `4256012000EE0005` (smart_filter) | `4256013000EE0005` (xp 200) |
| OW-NV-6 | `4256012000EE0006` (smart_filter) | `4256013000EE0006` (xp 400) |
| OW-NV-7 | `4256012000EE0007` | `4256013000EE0007` (xp 500) |

### Smart filter expressions (OW wing)

- OW-NV-2: `root(or(item(neovitae:sentient_helmet),item(neovitae:sentient_plate),item(neovitae:sentient_leggings),item(neovitae:sentient_boots)))`
- OW-NV-3: `root(or(item(neovitae:sentient_pickaxe),item(neovitae:sentient_axe)))`
  - NOTE: `sentient_axe` was NOT found in the jar lang dump. Only `sentient_axe` appears in the lang as... checking: NOT present. The lang only has `sentient_axe` as... see verification note below. Use `sentient_pickaxe` as single `item` task instead of smart filter, and drop axe reference. See §5 below.
- OW-NV-5: `root(or(item(neovitae:spiritus_gem_lesser),item(neovitae:spiritus_gem_common),item(neovitae:spiritus_gem_greater),item(neovitae:spiritus_gem_grand)))`
- OW-NV-6: `root(or(item(neovitae:base_spiritus_soul_raw),item(neovitae:base_spiritus_soul_invictus),item(neovitae:base_spiritus_soul_nihilum),item(neovitae:base_spiritus_soul_ruina),item(neovitae:base_spiritus_soul_vindicta)))`

---

## 4. Invariants Checklist

| Invariant | Status |
|---|---|
| All NV optional-depth quests have `optional: true` | CONFIRMED — every quest in §2 and §3 is marked optional |
| Zero `/astages add ... atomic` command rewards | CONFIRMED — no AT wing quest carries a stage grant of any kind |
| Zero `/astages add` of any progression stage | CONFIRMED — OW-NV-7 has no stage grant; its only reward is XP |
| No new chapters created | CONFIRMED — insertion only into at7 and ow6 |
| No whole-chapter set optional | CONFIRMED — both host chapters remain required chapters |
| convergence link is fan-in-only | CONFIRMED — OW-NV-7 is a standalone optional quest; it does NOT appear as a required dep of the OW capstone `4256010000010006`. Optional fan-in is not wired to any grant node. |
| `observation` task type availability | NOT FOUND in any chapter file. Fallback chosen: `dimension` task type (confirmed present in `ren_magic_foundations.snbt` etc.), shape: `{ dimension: "neovitae:dungeon", id: "...", type: "dimension" }`. This is used for AT-NV-5. |
| `interact_block` task type availability | NOT FOUND in any chapter file — not used |
| All item ids jar-verified | See §5 |

---

## 5. Item ID Verification

### Confirmed present in `neovitae-1.21.1-1.0.25.jar` lang

| Item ID | Verification |
|---|---|
| `neovitae:blood_orb_transcendent` | `item.neovitae.blood_orb_transcendent` in lang |
| `neovitae:hellforged_explosive_cell` | `item.neovitae.hellforged_explosive_cell` in lang |
| `neovitae:crystal_cluster` | `block.neovitae.crystal_cluster` in lang |
| `neovitae:crystal_cluster_brick` | `block.neovitae.crystal_cluster_brick` in lang |
| `neovitae:sentient_helmet` | `item.neovitae.sentient_helmet` in lang |
| `neovitae:sentient_plate` | `item.neovitae.sentient_plate` in lang |
| `neovitae:sentient_leggings` | `item.neovitae.sentient_leggings` in lang |
| `neovitae:sentient_boots` | `item.neovitae.sentient_boots` in lang |
| `neovitae:sentient_sword` | `item.neovitae.sentient_sword` in lang |
| `neovitae:sentient_pickaxe` | `item.neovitae.sentient_pickaxe` in lang |
| `neovitae:spiritus_gem_petty` | `item.neovitae.spiritus_gem_petty` in lang |
| `neovitae:spiritus_gem_lesser` | `item.neovitae.spiritus_gem_lesser` in lang |
| `neovitae:spiritus_gem_common` | `item.neovitae.spiritus_gem_common` in lang |
| `neovitae:spiritus_gem_greater` | `item.neovitae.spiritus_gem_greater` in lang |
| `neovitae:spiritus_gem_grand` | `item.neovitae.spiritus_gem_grand` in lang |
| `neovitae:base_spiritus_soul_raw` | `item.neovitae.base_spiritus_soul_raw` in lang |
| `neovitae:base_spiritus_soul_invictus` | `item.neovitae.base_spiritus_soul_invictus` in lang |
| `neovitae:base_spiritus_soul_nihilum` | `item.neovitae.base_spiritus_soul_nihilum` in lang |
| `neovitae:base_spiritus_soul_ruina` | `item.neovitae.base_spiritus_soul_ruina` in lang |
| `neovitae:base_spiritus_soul_vindicta` | `item.neovitae.base_spiritus_soul_vindicta` in lang |
| `neovitae:simple_key` | `item.neovitae.simple_key` in lang |
| `neovitae:standard_key` | `item.neovitae.standard_key` in lang |
| `neovitae:boss_key` | `item.neovitae.boss_key` in lang |
| `neovitae:demonite_trim_ingot` | `item.neovitae.demonite_trim_ingot` in lang |
| `neovitae:dungeon` (dimension) | `data/neovitae/dimension/dungeon.json` exists in jar |

### Failed verification (items introduced but NOT in jar lang)

| Attempted ID | Status | Resolution |
|---|---|---|
| `neovitae:sentient_axe` | NOT FOUND — no `item.neovitae.sentient_axe` key | Removed from OW-NV-3. Quest tasks only `sentient_pickaxe` as single `item` task. Smart filter dropped for this quest. |
| `neovitae:sentient_scythe` | Found as `item.neovitae.sentient_scythe` — available as optional addition to OW-NV-3 if desired in authoring |

### NV items in lang but NOT used in this design (available for future expansion)

`sentient_scythe`, `sentient_shovel`, `ingot_hellforged`, `hellforged_resonator`, `raw_demonite`, `demonite_fragment`, `spiritus_invictus_shard` / `nihilum_shard` / `ruina_shard` / `vindicta_shard`, `alchemy_flask`, arrays, sigils, reagents, anointments.

---

## 6. dimension Task Shape Reference

Based on `ren_magic_foundations.snbt` line 44–46:

```snbt
{
    dimension: "neovitae:dungeon"
    id: "4358012000EE0005"
    type: "dimension"
}
```

The `PlayerSpells` and `SkillsLevel` boilerplate blocks (present on every task in these chapters) must also be included. They are inert but structurally required by the serializer.

---

## 7. Authoring Notes for Tasks 5.2 / 5.3

1. **NV Atomic wing (Task 5.2):** Insert 9 quests into `at7_chaos_convergence.snbt`. All use id prefix `4358011000EE`, task prefix `4358012000EE`, reward prefix `4358013000EE`. Chain starts at dep `4358010000010000` (Spectrum entry). Positions column in §2 above are implementation-ready.

2. **NV OW wing (Task 5.3):** Insert 7 quests into `ow6_beyond_the_veil.snbt`. All use id prefix `4256011000EE`, task prefix `4256012000EE`, reward prefix `4256013000EE`. Chain starts at dep `4256010000010001` (Fusion Reactor). Positions column in §3 above are implementation-ready.

3. **Lang entries:** All quest titles/descs must go into `config/ftbquests/quests/lang/en_us.snbt` as `quest.<id>.title` / `quest.<id>.quest_desc` keys per the FTBQ text convention. Do not inline.

4. **Line endings:** Detect per-file (`raw.count(b'\r\n')` vs `b'\n'`) before writing — these files may be CRLF.

5. **OW-NV-7 convergence:** This quest has `optional: true` and no stage grant. It does NOT need to be added to the dep list of `4256010000010006`. Its only function is flavour and XP.
