# O — "Magic of Reveal" discipline audit (Phase 0)

AUDIT ONLY. No files edited outside this phase0/ directory. No git.
Scope: later-age content stays hidden until earned, across (a) stage locks,
(b) questbook icons, (c) chapter/quest revelation, plus prose text leaks.

Method: `phase0/reveal_scan.py` (rootless scan) + `phase0/reveal_scan2.py`
(item->stage map, icon leaks, gateway wiring) + inline Python probes quoted per
finding. Data: 56 chapters, 1930 quest nodes, 3222 item stage-locks parsed from
`kubejs/server_scripts/aoa_astages_01*.js` (most-restrictive-wins = MAX age).

Severity ladder (per SHARED_CONTEXT): SOFTLOCK > BROKEN > CANON > HYGIENE.
Task-defined reveal grades mapped on top: whole later-age tab visible at entry =
CRITICAL/SOFTLOCK; task-item age inversion = SOFTLOCK; icon-only leak = MEDIUM/CANON;
vague/forward prose = LOW/HYGIENE.

---

## Verdict

The reveal spine is in very good shape. The intended "3 Dark entries + Journey
visible at world entry, every later age tab gated on the prior age's capstone" is
implemented correctly. No later-age tab leaks. The only real defects are
**neovitae hellforged/spiritus item tasks placed in Renaissance chapters while
those items are AStages-locked to industrial_revolution** — a cross-age inversion
that shows as both an icon leak and a genuine softlock risk. That is one item
family (Neo Vitae), needs a canon call on which side is wrong.

Counts per class:
- Rootless/visible leaks: **0** (4 rootless total, all legal: 3 Dark + 1 Journey)
- Gateway mis-wires: **0** (all 6 age boundaries gate on the correct prior capstone)
- Icon leaks: **11** (all one cause: neovitae hellforged/spiritus in Ren chapters)
- Text leaks (early-age prose naming later marquee): **0 real** (4 raw hits, all
  false positives or legal — see class 4)
- Stage-lock surface (JEI/EMI hiding): **correct** across all 16 restriction files

---

## Class 1 — Rootless / world-entry visibility (CRITICAL if leaked)

Proof: `python phase0/reveal_scan.py`.

Rootless (zero-dependency, therefore always-visible) quests, complete list:

| Age | Chapter | Quest id | Item | Verdict |
|---|---|---|---|---|
| dark_ages | stone_food_and_farming_pressures.snbt | 34000000000003C1 | minecraft:stone_hoe | LEGAL (Dark entry) |
| dark_ages | stone_water_weather_and_wounds.snbt | 60D53613768CA1F3 | minecraft:campfire | LEGAL (Dark entry) |
| dark_ages | entering_the_iron_era.snbt | 6A1E8D4C0F2B7A11 | minecraft:flint | LEGAL (Dark entry) |
| journey | journey_to_ascension.snbt | 5350010000010000 | minecraft:campfire | LEGAL (Journey root, meta) |

Only 4 of 1930 quests are rootless. All 4 are the sanctioned world-entry set
(3 Dark Ages entries + the Journey roadmap root). **Every** later-age chapter has
zero rootless quests, so no later-age tab is visible at world entry.

Chapter-tab visibility at entry (a tab shows iff >=1 quest is visible):
- Visible: `stone_food_and_farming_pressures`, `stone_water_weather_and_wounds`,
  `entering_the_iron_era` (all Dark), `journey_to_ascension` (meta).
- Every other tab (Medieval through Ascension, Annex/minecolonies) is hidden until
  its gateway completes.

Chapter-level flags checked: `hide_quest_until_deps_complete: true` is set on the
Dark chapters (correct); no chapter carries `always_invisible`. FTBQ progressive
reveal is confirmed working the way memory describes: `hide_until_deps_complete` is
a NO-OP on rootless quests, so the discipline is enforced purely by making sure
non-entry quests all carry >=1 dependency — which they do.

**Class 1 severity: CLEAN. Zero leaks.**

---

## Class 2 — Gateway wiring (does each age gate on the prior capstone?)

Proof: `python phase0/reveal_scan2.py` (section 2) + inline task probe.

Each age's earliest quests depend on a cross-age edge into the prior age. The
source quest at the end of each edge was inspected for its actual task/command:

| Boundary | Gateway dep source quest | What that source quest IS | Verdict |
|---|---|---|---|
| Dark -> Medieval | 097AED7C91033D5E (entering_the_iron_era) | grants `medieval_times` (Dark capstone) | CORRECT |
| Medieval -> Renaissance | 6D7E8F901A2B1054 (what_waits_in_the_grove) | `/advancement grant ... journey/grove_trials` (Medieval capstone) | CORRECT |
| Renaissance -> IR | 0B0310A0000000F0 (ren_maledictus_vigil) | Renaissance capstone/Maledictus vigil | CORRECT (primary IR entries dep this) |
| IR -> Gilded | 4954631000000000 (ir_netherite_citadel_obsidilith) | `/advancement grant ... journey/obsidilith` (Obsidilith kill capstone) | CORRECT |
| Gilded -> Atomic | 5057011000000003 (g_power_beyond_wires) | kill `astral_dimension:void_titan` -> `journey/void_titan` | CORRECT (matches memory) |
| Atomic -> Otherworldly | 4358010000010003 (at7_chaos_convergence) | grants `at_capstone_complete` (Atomic capstone) | CORRECT |
| Otherworldly -> Ascension | 4256010000010006 (ow6_beyond_the_veil) | grants `ow_capstone_complete` (OW capstone) | CORRECT |

All six real age boundaries reveal on the prior age's capstone (boss kill or
capstone grant), never on something earlier. No gateway skips a capstone.

Observations (not reveal leaks, flagged for hygiene):
- `ir_netherite_citadel_obsidilith` quest `49540E1000000006` deps on
  `11C25203906C0FD4`, a **Dark Ages** farming quest (eclipticseasons:hygrometer).
  That is a backward cross-age dependency. It does NOT leak reveal (the earlier
  quest is completed long before), but it is an odd wiring worth tidying. HYGIENE.
- `g7_chartered_arcana` quest `4341011000000002` deps on a Renaissance
  magic-foundations node (`0B03101000000058`) rather than the IR capstone. Again
  not a reveal leak (a Ren node is complete before Gilded opens), and g7's other
  three entries correctly dep the IR Obsidilith capstone, so the tab still opens
  on the right gate. HYGIENE / intentional magic through-line.

**Class 2 severity: CLEAN for reveal. 2 HYGIENE wiring notes.**

---

## Class 3 — Icon leaks (icon renders a later-age item than its chapter's age)

Proof: `python phase0/reveal_scan2.py` (section 3). Chapter-tab icons render on
the tab; quest icons/task-items render inside a chapter even when the quest body is
hidden. Compared each icon item's effective AStages lock to its chapter's age.

All 11 leaks share ONE root cause: **Neo Vitae hellforged / spiritus items used as
icons and task items in Renaissance chapters, but AStages-locked to
industrial_revolution** (`kubejs/server_scripts/aoa_astages_01m_magic.js:133-146`).

| Kind | Chapter (age) | Quest | Icon/task item | AStages lock |
|---|---|---|---|---|
| CHAPTER-TAB | ren_nether_threshold (the_renaissance) | (tab) | neovitae:ingot_hellforged | industrial_revolution |
| QUEST | ren_magic_foundations | 0B03101000000038 | neovitae:spiritus_gem_petty | industrial_revolution |
| QUEST | ren_magic_foundations | 0B03101000000070 | neovitae:spiritus_gem_lesser | industrial_revolution |
| QUEST | ren_magic_foundations | 0B03101000000075 | neovitae:spiritus_gem_common | industrial_revolution |
| QUEST | ren_nether_threshold | 0B03102000000001 | neovitae:ingot_hellforged | industrial_revolution |
| QUEST | ren_nether_threshold | 0B03102000000041 | neovitae:hellforged_dust | industrial_revolution |
| QUEST | ren_nether_threshold | 0B03102000000042 | neovitae:ingot_hellforged | industrial_revolution |
| QUEST | ren_nether_threshold | 0B03102000000046 | neovitae:hellforged_parts | industrial_revolution |
| QUEST | ren_nether_threshold | 0B03102000000047 | neovitae:hellforged_block | industrial_revolution |
| QUEST | ren_nether_threshold | 0B03102000000062 | neovitae:ingot_hellforged | industrial_revolution |
| QUEST | ren_nether_threshold | 0B03102000000081 | neovitae:spiritus_gem_petty | industrial_revolution |

This is worse than a cosmetic icon leak: quests `0B03102000000041` and
`0B03102000000042` (verified with inline probe) carry real `item` tasks requiring
`neovitae:hellforged_dust` / `neovitae:ingot_hellforged`, which a Renaissance-stage
player cannot craft (locked to IR). That is a **cross-age task-item inversion =
SOFTLOCK risk**, not just a reveal cosmetic. The chapter-tab icon leak
(`neovitae:ingot_hellforged` on the Ren `ren_nether_threshold` tab) also renders
the IR item on a Renaissance tab, which additionally leaks IR content into the
Renaissance view.

Needs a canon call on which side is wrong (do NOT auto-fix):
- If hellforged/spiritus are meant to be Nether-tier Renaissance content (Nether
  unlocks at the_renaissance), the **AStages lock at IR is the bug** and should
  drop to `the_renaissance`.
- If they are meant to be IR-tier, the **Renaissance quest placement is the bug**
  and these nodes should move to an IR chapter (or the icons swapped to a real
  Renaissance-legal neovitae item).

Proof command:
`grep -n "hellforged\|spiritus_gem" kubejs/server_scripts/aoa_astages_01m_magic.js`

**Class 3 severity: SOFTLOCK (task-inversion subset) + MEDIUM/CANON (icon leak).
11 icon leaks, 1 root cause.**

---

## Class 4 — Text leaks (early-age prose naming later-age marquee content)

Proof: inline multi-line-aware scan over `config/ftbquests/quests/lang/en_us.snbt`,
2174 early-age quest strings (Dark/Medieval/Renaissance) vs a marquee term list
(Mekanism, fusion, fission, reactor, Draconic, AE2, rocket, nuclear, Avaritia,
Dyson, Oritech, MI, Void Titan, Obsidilith, Leviathan, etc.).

4 raw hits, all dispositioned:

| Quest | Field | Term | Disposition |
|---|---|---|---|
| 0B03101000000005 (Ren) | quest_desc | "fusion" | FALSE POSITIVE — word is "in**fusion**" (spirit infusion recipes) |
| 0B03101000000008 (Ren) | quest_desc | "fusion" | FALSE POSITIVE — "spirit in**fusion**" / soul-binding |
| 0B031080000000E1 (Ren) | quest_desc | "Modern Industrialization" | LEGAL — quest tasks `modern_industrialization:bronze_plate`, which is NOT stage-locked (only bronze_plated_bricks+ are IR-locked); MI is namable here because the bronze parts are Renaissance-craftable. Forward-naming the mod is at most LOW. |
| 0B031080000000E2 (Ren) | quest_desc | "Modern Industrialization" | LEGAL — tasks `modern_industrialization:bronze_gear`, also unlocked (not in the MI IR lock list). |

No Dark/Medieval/Renaissance prose names fusion reactors, Mekanism, AE2, Draconic,
rockets, atomic tech, or any capstone boss ahead of its age.

Proof:
`grep -n "bronze_plate\|bronze_gear" kubejs/server_scripts/aoa_astages_01h_modern_industrialization.js`
(returns nothing — those items are unlocked).

**Class 4 severity: CLEAN. 0 real leaks.**

---

## Class 5 — Stage-lock reveal surface (what a player SEES for a locked item)

Question: for a stage-locked item, does the player see it hidden, greyed, or
visible-with-warning? User wants locked content invisible.

Finding: **locked items are hidden from the recipe viewer and have their name and
tooltip suppressed.** Every one of the 16 item-restriction files
(`aoa_astages_01*.js`) routes each lock through a `softItemPolicy` helper that
sets, per item:

`aoa_astages_01_item_restrictions.js:14-24` (representative; identical helper in
all 16 files):
```
.setCanBeStoredInInventory(true)   // a leaked drop is not destroyed
.setCanBeStoredInContainers(true)
.setCanPickedUp(true)
.setCanBeEquipped(false)
.setCanBePlaced(false)
.setCanItemBeLeftClicked(false)
.setCanItemBeRightClicked(false)
.setCanInteractWithBlock(allowBlockInteraction === true)  // ores exempt
.setHideTooltip(true)       // no tooltip
.setRenderItemName(false)   // no name shown
.setHideInJEI(true)         // hidden from recipe viewer
```
Verify: `grep -c "setHideInJEI" kubejs/server_scripts/aoa_astages_01*.js` -> 1 per
file, 16 files; helper present in all 16
(`grep -l applySoftItemPolicy kubejs/server_scripts/aoa_astages_01*.js` = 16).

Recipe viewer: the active viewer is **EMI** (`mods/emi-1.1.24+1.21.1+neoforge.jar`;
JEI present as a dependency). `setHideInJEI(true)` is AStages' hide flag; EMI honors
JEI hide flags through its compat layer. There is **no** dedicated astages<->EMI or
astages<->JEI bridge config in the pack (`config/astages/`, `config/emixx/`,
`config/jei/` — none reference stages), so hiding relies entirely on the AStages
`setHideInJEI` policy above, which is applied uniformly.

AStages global config surface (`config/astages/astages-common.toml`):
- `astages-common.toml:3` `"Enable Titles" = true` and `:6 "Title color" = "RED"`
  — stage-grant titles show on screen when a stage is earned (intended reveal
  moment).
- `astages-common.toml:10` `"Enable Warning" = true` — dev-facing warning for a
  stage with no restriction; the barrier marker restrictions in
  `aoa_astages_00_register_stages.js` exist specifically to silence this. Not
  player-visible.
- No config toggles locked items to a "greyed/visible-with-warning" mode; the
  KubeJS soft policy is the sole surface and it hides.

Caveat (for the team, not a defect): the soft policy intentionally leaves locked
items **storable and pickup-able** (so a bypass drop is not deleted) while blocking
place/equip/interact and hiding them from EMI + tooltip. So a locked item obtained
out of band sits inertly in inventory with no name and no recipe entry, rather than
vanishing. That matches "invisible in the recipe book" but is not "cannot exist in
inventory". If the user wants truly zero-presence, that is a policy decision, not a
bug.

**Class 5 severity: CLEAN / working as intended. Reported for confirmation.**

---

## Fix list (all require a canon call before editing — this pass is audit-only)

1. **[SOFTLOCK] Neo Vitae hellforged/spiritus age inversion** — decide the correct
   age for `neovitae:ingot_hellforged`, `hellforged_dust`, `hellforged_parts`,
   `hellforged_block`, `spiritus_gem_petty/lesser/common`. Either drop their
   AStages lock from `industrial_revolution` to `the_renaissance`
   (`aoa_astages_01m_magic.js:133-146`) if they are Nether-tier Renaissance, OR
   move the `ren_nether_threshold` / `ren_magic_foundations` quests that task them
   to an IR chapter. Fixes both the task-inversion softlock and all 11 icon leaks
   at once, including the `ren_nether_threshold` tab icon.
2. **[HYGIENE] Backward cross-age dep** — `ir_netherite_citadel_obsidilith`
   `49540E1000000006` deps a Dark Ages hygrometer quest (`11C25203906C0FD4`);
   re-anchor to an age-appropriate prerequisite.
3. **[HYGIENE] g7 Renaissance dep** — confirm `4341011000000002` depping a Ren
   magic node is the intended magic through-line, not a stray edge.
4. **[LOW] MI forward-naming** — Renaissance quests 0B031080000000E1/E2 name
   "Modern Industrialization" in prose; items are legal, so optional to soften the
   wording. No action required.
5. **[CONFIRM] Locked-item inventory presence** — confirm the team is OK that
   locked items are storable/pickup-able (hidden + inert) rather than fully
   non-existent. Config working as designed.

Scripts: `phase0/reveal_scan.py`, `phase0/reveal_scan2.py`.
