# Audit A -- item -> stage tier / softlock analysis

Phase 0, generated 2026-07-02. Audit-only. Source of truth:
`config/ftbquests/quests/chapters/*.snbt` (quest structure) and
`kubejs/server_scripts/aoa_astages_*.js` (stage locks). Full row table:
`A_tier_softlock_table.md`. Script: `tier_audit.py`.

## Method

- Parsed all 56 chapter `.snbt` files as bytes (utf-8, mixed line endings
  normalized in-memory only). Resolved each chapter's age from its `group:`
  field against the SHARED_CONTEXT map (verified: every chapter's group is one
  of the 10 known groups; 8 real ages + Journey meta + Annex).
- Extracted every `type: "item"` task via a brace-depth walk that isolates each
  quest object and each task's `item: { ... }` block. Both forms are handled:
  inline `item: { count:N, id: "ns:x" }` and
  `ftbfiltersystem:smart_filter` NBT (`item(ns:x)` / `tag(ns:x)` extracted from
  the filter expression). Tags are reported separately as UNRESOLVED_TAG rather
  than guessing membership.
- `type: "checkmark"` tasks are flagged ILLEGAL separately. **None exist**
  (0 checkmark tasks pack-wide -- clean on that rule).
- Built item->stage and tag->stage maps from every literal
  `["stage","id","kind"]` array entry across all `aoa_astages_*.js` files.
  AStages is most-restrictive-wins, so effective stage = MAX age index across
  all files. 3443 item locks + 37 literal tag locks parsed.
- Verdicts: **SOFTLOCK** = item task whose effective unlock stage is a LATER age
  than its chapter. **CANON** = item with no explicit lock but from a mod family
  whose preamble floor is a later age than the chapter (tier inversion by family
  even though not literally locked). **ILLEGAL** = checkmark. OK otherwise.

## Summary counts

| verdict | count |
|---|---|
| SOFTLOCK | 12 |
| ILLEGAL (checkmark) | 0 |
| CANON (family inversion, unlocked) | 21 |
| UNRESOLVED_TAG | 0 |
| OK (locked at/before, or no-lock legal family) | 2614 |
| skipped (Journey meta + Annex, age-agnostic) | 32 |

Item tasks scanned: 2646 age-bound + 32 meta/annex. No checkmark tasks and no
tag-based item tasks that reference a locked tag (all 91 smart_filters resolved
to concrete `item(...)` ids; zero `tag(...)` filters).

## SOFTLOCK rows -- every one explained

All 12 are **NeoVitae** items placed as quest tasks in a chapter EARLIER than the
age at which `aoa_astages_01m_magic.js` unlocks them. NeoVitae is the required
magic spine (Ren -> Gilded per canon), but its live stage locks push the
hellforged/spiritus/sentient tiers past the chapters that demand them. Each is a
real block: the AStages soft-lock hides the item in JEI and prevents pickup
until the stage is granted, so the player physically cannot complete the task at
the chapter's age.

### Renaissance chapters requiring IR-locked NeoVitae (7 rows)

`ren_magic_foundations` (the_renaissance) requires spiritus gems locked to
`industrial_revolution`:
- `neovitae:spiritus_gem_petty` -- quest `0B03101000000038` -- lock `01m_magic.js:133`
- `neovitae:spiritus_gem_lesser` -- quest `0B03101000000070` -- lock `01m_magic.js:134`
- `neovitae:spiritus_gem_common` -- quest `0B03101000000075` -- lock `01m_magic.js:135`

`ren_nether_threshold` (the_renaissance) requires the Hellforged chain, which is
IR-locked because it is sourced from `neovitae:dungeon`, itself gated
`industrial_revolution` in `aoa_astages_03_dimension_restrictions.js`:
- `neovitae:ingot_hellforged` -- quest `0B03102000000042` -- lock `01m_magic.js:145`
- `neovitae:hellforged_dust` -- quest `0B03102000000041` -- lock `01m_magic.js:146`
- `neovitae:hellforged_parts` -- quest `0B03102000000046` -- lock `01m_magic.js:147`
- `neovitae:hellforged_block` -- quest `0B03102000000047` -- lock `01m_magic.js:149`
- `neovitae:spiritus_gem_petty` (again) -- quest `0B03102000000081` -- lock `01m_magic.js:133`

This is the sharpest inversion: `ren_nether_threshold` is a Renaissance realm-
entry chapter, but every hellforged task depends on a dimension that does not
open until IR. Either the hellforged tasks must move to an IR chapter, or the
`neovitae:dungeon` + hellforged chain must be down-tiered to the_renaissance.
A canon call is required -- do not silently pick one (out of scope for this
audit-only pass).

### IR chapter requiring Gilded-locked NeoVitae Sentient armor (4 rows)

`ir_magic_feedstock_and_spectrum_network` (industrial_revolution) requires the
Sentient armor set, which `01m_magic.js:153-156` locks to `gilded_age`
(alongside `spiritus_gem_greater/grand` and the sentient tools):
- `neovitae:sentient_helmet` -- quest `49540B100000001B` -- lock `01m_magic.js:153`
- `neovitae:sentient_plate` -- quest `49540B100000001C` -- lock `01m_magic.js:154`
- `neovitae:sentient_leggings` -- quest `49540B100000001D` -- lock `01m_magic.js:155`
- `neovitae:sentient_boots` -- quest `49540B100000001E` -- lock `01m_magic.js:156`

Sentient gear is deliberately Gilded-tier per the lock comment ("Gilded: high
orbs, Sentient gear"). It should not be a required task in an IR chapter. Fix is
either reclassify these four IR nodes as optional Gilded-facing depth, move them
to a Gilded chapter, or down-tier the Sentient set -- canon call needed.

**Root cause pattern:** the NeoVitae quest scaffolding was authored to the design
intent (Ren->Gilded spine) but the item stage locks landed one age later than
the chapters that consume them. This matches the known-open canon note in the
preamble sec.7 that NeoVitae "capstone anchor A1 is NOT done" -- the spine's
tier boundaries are still mid-migration. Every SOFTLOCK here is a spine item, not
a decorative straggler, so all 12 are genuine progression blockers, not cosmetic
noise.

## CANON rows (unlocked but later-family) -- notable

21 rows: items with no explicit AStages lock whose namespace floor (preamble
sec.3) is later than the chapter. These are NOT hard softlocks (nothing blocks
them), but they are tier inversions by mod family and worth a design look.

- **`metallurgy` (medieval_times) -- 19 Immersive Engineering rows.** The
  Medieval metallurgy chapter tasks a large block of `immersiveengineering:*`
  items: the `manual`, `coal_coke`/`coke`/`creosote_bucket`, treated-wood decor,
  `hammer`, `wirecutter`, copper wire/coil, `connector_lv`, `fluid_pipe`,
  `hempcrete`/`concrete`, `fertilizer`. IE's family floor is IR per the preamble.
  None of these are locked, so they function today, but a whole IE tool+coke
  bootstrap living in a Medieval chapter is a family-tier inversion. This is
  likely intentional (IE coke oven / hammer as an early-metallurgy bootstrap),
  but it contradicts the "IE starts IR" baseline and should get an explicit canon
  ruling: either accept IE hand-tools + coke as a Medieval exception (and note it
  in the ledger) or move this block to IR.
- **`ren_observation_experimentation` (the_renaissance) -- 2 Modern
  Industrialization rows:** `modern_industrialization:bronze_plate` and
  `modern_industrialization:bronze_gear`. MI floor is IR. Unlocked (only
  `bronze_plated_bricks` is IR-locked), so they work, but bronze MI parts in a
  Renaissance chapter invert the MI-starts-IR baseline. Lower severity than the
  IE block; likely a stray reference. Worth a down-tier confirmation or moving
  the two nodes to IR.

No CANON rows for the truly dangerous families (Draconic, Avaritia, Stellaris,
nuclear) appear in early chapters -- those are all either locked or absent from
early-chapter tasks. The inversions that exist are low-tech-into-slightly-earlier
(IE and MI bronze), not endgame-into-early.

## Known blind spots of this script

1. **Tag membership is out of scope.** Item tasks that reference a `tag(...)`
   in a smart_filter would be reported UNRESOLVED_TAG (there are currently none).
   Where a task item is a concrete id, that is resolved exactly; where the pack
   ever adds a tag-based item task, this script will not expand the tag to its
   members and cannot judge whether any member is later-tier.
2. **Programmatic AStages locks are not executed.** Files `06_ore_restrictions.js`
   and `07_progression_bypass_restrictions.js` generate many `c:material` tag
   locks and companion-item locks inside JS loops (e.g.
   `softTagLock(stage, 'c:'+family+'/'+material, ...)`). This script captures
   only their **literal** `["stage","id"]` array entries, not loop-generated ids.
   An item that is only gated by a computed `c:` tag from those loops could show
   as "(none)" here. This did not surface any missed SOFTLOCK in practice because
   the SOFTLOCKs found are all explicit literal locks, but a loop-only gate on an
   early quest item would be invisible to this pass. To close it, the locks would
   need to be extracted by running KubeJS or emulating the loops.
3. **Recipe-level bypasses and craftability are out of scope.** This audit only
   compares the item's stage lock to its chapter age. It does NOT verify that the
   item is actually craftable/obtainable by that age through a legal recipe
   chain (that is a separate softlock/recipe-chain audit). An item locked at the
   correct age can still be a softlock if its ingredients are not reachable --
   not detected here.
4. **Family-floor CANON detection is namespace-coarse.** `FAMILY_FLOOR` applies a
   single floor per namespace from the preamble. Sub-tiers within a family
   (e.g. Create's Medieval vs Renaissance split, Mekanism's IR vs Atomic tiers)
   are handled by the explicit item locks, not by the family floor, so CANON
   rows are only raised for whole-namespace-late families with no per-item lock.
   A family whose EARLY tier is legal but whose namespace floor is later could
   in principle raise a false CANON; the two MI bronze rows are borderline and
   flagged as low-confidence for that reason.
5. **Quest `optional`/`hidden` flags are not weighted.** A SOFTLOCK on an
   optional/hidden depth node is less severe than on a required spine node. This
   pass reports the tier inversion regardless; the 12 SOFTLOCKs are all on spine
   nodes by inspection, but the script does not encode required-vs-optional.
