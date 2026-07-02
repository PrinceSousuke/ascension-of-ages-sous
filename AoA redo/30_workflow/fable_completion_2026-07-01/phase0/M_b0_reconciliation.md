# M — B0 Whole-Roster Coverage Reconciliation — 2026-07-02

**Audit:** B0 (`02_VERIFICATION_PASS.md` §B0). Owner: CC.
**Inputs verified present:** `mod_quest_coverage_census_2026-07-02.md`, `02a_COMPLETION_BACKLOG.md`
(both loaded; neither missing — no reconstruction from `I_fomo_coverage.md` needed).
**Method:** independent hand-grep of `config/ftbquests/quests/chapters/*.snbt`. Ground-truth grep
used a left-boundary pattern `(^|[^a-z_])<modid>:` to avoid the substring false-positive that bit
the first pass (`artifacts` matching inside `reliquified_artifacts`).

---

## 1. Sample

- Enumerable PARTIAL/ZERO universe reconstructed from the census: **178 mods** (50 named bullet rows
  with counts + 128 additional distinct ZERO modids from the compact UNGATED list). The census
  headline "216 not fully done" counts 56 PARTIAL + 160 ZERO; the 178 here is the subset whose modid
  is individually enumerable from the census text (some ZERO mods are only summarized in prose groups).
- **15% sample = 27 mods** (`random.seed(700702)`), spanning PARTIAL and ZERO, decor / structure /
  RPG / tech / dimension / boss families.

Sampled: `abyssal_decor, adchimneys, aeronautics_bundled, amendments, artifacts,
betterendcities_raijin_structure, biomeswevegone, cabletiers, cataclysm, critical_strike,
draconicevolution, forgeendertech, hearth_and_timber, hellish_trials, immersiveengineering,
mahou_tsukai_combat, mcwbyg, mcwdoors, mcwpaintings, mcwstairs, mcwwindows, moogs_structures,
mr_lukis_ancientcities, sable, simulated, taxov, unusualend`.

---

## 2. Agreement rate

**Verdict agreement: 27 / 27 = 100%.** Every sampled PARTIAL stayed PARTIAL and every ZERO stayed
ZERO on independent grep. One count drifted (below). No verdict was wrong.

Proof grep (per-mod unique `modid:path` refs in chapters):

| mod | census | on-disk | verdict | note |
|---|---|---|---|---|
| cabletiers | 15 | 15 | PARTIAL ✓ | exact |
| cataclysm | 18 | 18 | PARTIAL ✓ | exact |
| draconicevolution | 21 | 21 | PARTIAL ✓ | exact |
| immersiveengineering | 86 | 86 | PARTIAL ✓ | exact |
| unusualend | 23 | **28** | PARTIAL ✓ | **count drift +5** (verdict unchanged) |
| artifacts | 0 (ZERO) | 0 | ZERO ✓ | see disagreement table |
| abyssal_decor, adchimneys, aeronautics_bundled, amendments, betterendcities_raijin_structure, biomeswevegone, critical_strike, forgeendertech, hearth_and_timber, hellish_trials, mahou_tsukai_combat, mcwbyg, mcwdoors, mcwpaintings, mcwstairs, mcwwindows, moogs_structures, mr_lukis_ancientcities, sable, simulated, taxov | 0 | 0 | ZERO ✓ | all 21 confirmed 0 with boundary-correct grep |

---

## 3. Disagreements

| mod | census | on-disk | class | detail |
|---|---|---|---|---|
| `unusualend` | 23 refs | 28 refs | **census stale (undercount)** | 5 more unique `unusualend:*` task ids on disk than the census recorded. Verdict PARTIAL is still correct; only the count is low. Likely authoring landed after the census snapshot. |
| `artifacts` | ZERO / 0 | 0 (re-confirmed) | **not a disagreement — my first-pass grep artifact** | A naive `artifacts:` grep returned 1 hit, but it is `reliquified_artifacts:mimi_dust` in `ren_deeper_darker_otherside.snbt:1216` — a *different* mod. Boundary-correct grep = 0. Census ZERO is **correct**. Recorded here for transparency. |

No case of the census being *wrong* (verdict inversion) was found. Drift is limited to one low count.

---

## 4. Foundation-gap confirmations (all 8 = 0)

Checked with literal `grep -rF` (catches the id anywhere in the file, **including smart_filter /
ftbfiltersystem NBT bodies** — 16 chapters use smart_filter and were all covered), plus a variant
sweep for the spectrum pedestal family.

| foundation id | hits across all chapters | confirmed 0 |
|---|---|---|
| `ae2:controller` | 0 | ✅ |
| `ae2:drive` | 0 | ✅ |
| `refinedstorage:controller` | 0 | ✅ |
| `mekanism:enrichment_chamber` | 0 | ✅ |
| `oritech:machine_core_1` | 0 | ✅ |
| `immersiveengineering:blast_furnace` | 0 | ✅ |
| `spectrum:pedestal_moonstone` (+ every `spectrum:pedestal*` variant) | 0 | ✅ |
| `avaritia:extreme_crafting_table` | 0 | ✅ |

Supporting proofs:
- **Namespaces are present, the foundation items are not.** `ae2`=14, `refinedstorage`=9,
  `oritech`=54, `avaritia`=7 unique refs exist — so 0 for the specific onboarding items is a real
  gap, not a namespace-absent artifact.
- **g4 "The Infinite Grid"** (the AE2 chapter) opens on `ae2:molecular_assembler` + wireless/pattern
  content (`ae2:pattern_provider`, `ae2:wireless_*`, `refinedstorage:autocrafter`). No `controller`,
  no `drive`. The only "controller"/"drive" strings in the pack are unrelated
  (`pneumaticcraft:programmable_controller`, `occultism:storage_controller`). This is exactly the
  backlog's [FOUND] "endgame taught, onboarding missing" defect, confirmed by hand.
- **IE**: `immersiveengineering:blast_furnace` = 0; the mod appears only as `blastbrick` and
  `blastfurnace_preheater` (neither is the multiblock task). Gap real.
- **Spectrum pedestals**: zero `spectrum:pedestal*` of any variant anywhere.

---

## 5. Backlog edits made (`02a_COMPLETION_BACKLOG.md`, in place, structure preserved)

1. Added a **2026-07-02 B0 reconciliation note** blockquote under the legend: sample size, 100%
   agreement, the `unusualend` count drift, the `artifacts` re-confirmation, and the 8-gap
   confirmation.
2. Added a **"User coverage rulings applied 2026-07-02"** subsection encoding the standing decisions,
   and a new `[EXCLUDED]` legend entry.
3. Threaded `[RULING 07-02: …]` tags into the affected per-age line items:
   - `psi` (IR) → "optional-only, never required" (was `[CANON]` open question).
   - `avaritia` (Ascension) → "thorough endgame."
   - `extendedcrafting` (IR) → "thorough endgame."
   - `stellaris` (OW) → "thorough endgame — confirm depth."
   - Added IR-section lines for `modern_industrialization` (thorough), `railways` (minimal / couple
     quests), `relics`/`artifacts`/`zoniex` (EXCLUDED), flight `aeronautics/createpropulsion`
     (stays unquested), `createnuclear/oreexcavation/powergrid` (leave alone), `ftboceanmobs`
     (dropped).

No other files edited. No git actions taken.

---

## 6. Verdict

The census is **reliable as the coverage baseline**: 100% verdict agreement on a 27-mod random
sample, one benign count undercount (`unusualend` 23→28), and all eight named foundation gaps
independently re-confirmed at 0 (including inside smart_filter NBT). The dominant "foundations gap"
thesis holds on hand-inspection — g4 literally opens the AE2 chapter without a controller/drive
quest. Backlog refreshed with the drift note and the 2026-07-02 user rulings. B0 baseline is signed.
