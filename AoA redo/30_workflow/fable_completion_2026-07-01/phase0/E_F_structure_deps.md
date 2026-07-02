# Phase 0 — Audits E + F: FTBQ structural hygiene + dependency-graph sanity

Scope: `config/ftbquests/quests/lang/en_us.snbt` + all 56 `config/ftbquests/quests/chapters/*.snbt`.
AUDIT ONLY. No files under `config/` touched. No git.

Method: Python brace-scan parser (`ef_audit.py` in this folder) reads every chapter via raw
byte reads (mount-truncation-proof), isolates top-level quest objects inside `quests: [ ]`,
extracts each quest `id` and its `dependencies` list (handles inline and multiline arrays),
and parses `lang/en_us.snbt` for `quest.<id>.quest_desc` presence, array-vs-string form, and
em/en dashes. Data dump: `ef_audit_data.json`, `em_rows.json`.

## Headline counts

| Metric | Value | Severity |
|---|---|---|
| Quest objects parsed (whole pack) | **1930** | — |
| Em dashes (U+2014) in en_us.snbt | **87** | HYGIENE |
| En dashes (U+2013) in en_us.snbt | **0** | — |
| Distinct quests carrying em dashes | 78 keys (+ multiline continuation lines) | HYGIENE |
| Missing `quest_desc` — total | **66** | mixed |
| Missing `quest_desc` — real content chapters (excl. journey mirrors) | **10** | BROKEN |
| Missing `quest_desc` — journey mirror nodes (by design) | 56 | not a defect |
| Non-array `quest_desc` (single-string form) | **7** (all ow6) | HYGIENE |
| Duplicate quest ids across all chapters | **0** | — |
| Dangling deps (target id missing) | **0** | — |
| Orphan quests (no dep + nothing depends) | **0** | — |
| Backward-age deps (lower age → higher age) | **0** | — |

Parser validation: 1930 parsed vs 1937 `x:`-coord lines. The 7-quest gap is entirely in
`minecolonies.snbt` and is NOT missing quests — those 7 `x:` lines are chapter-header
**image objects** (`questinstaller:textures/quests/*.png` logo/category art) that have
`x/y/width/height/rotation/image` but no `id`. True minecolonies quest count = 74. Parser is
correct; no quests were dropped, so dangling/orphan/backward = 0 are trustworthy.

---

## E. Structural defect sweep

### E1. Em dashes (U+2014) — 87 total, EXPECTED ~87 CONFIRMED

All 87 sit inside quest prose. 55 of them are in `journey_to_ascension` mirror-node descs.
The remaining 23 quest keys (32 em chars) are in real content chapters and are the real
cleanup targets:

| Chapter | Quest ids (em-dash count) |
|---|---|
| ow6_beyond_the_veil | 4256011000EE0001..0007 (2 each — 14 total) |
| ren_nether_threshold | 0B03102000000040, 0B03102000000046, 0B03102000000081, 1E5A8AEE45E9DDCA, FAB07684061A284D |
| at7_chaos_convergence | 4358011000EE0001/0002/0004/0005/0007 |
| ren_archive_recordkeeping | 3D0C727EB7D7D9FC, 936044D132622461 |
| what_waits_in_the_grove | 92614B6AD7E19E44, E101BB0D29F60954 |
| g1_the_golden_workshop | 4757011020010001 (2) |
| ren_observation_experimentation | 0B031080000000C2 |

Note: the count 78 "distinct keys" undercounts vs 87 chars because multiline `quest_desc`
arrays put some em dashes on continuation lines not adjacent to the key (e.g. quest
`4954021000000009` Steam Quarry desc, en_us.snbt line 3005-3006). All 87 are genuine prose
em dashes; en dashes = 0. **Canon rule: no em dashes in prose — these 87 need replacing with
period/comma per project style, prioritizing the 23 non-journey keys.**

### E2. Missing `quest_desc` — 10 real (BROKEN), 56 journey mirrors (by design)

The 4 known g6 ids confirmed, plus 6 more found across Renaissance + Medieval exactly as
predicted:

| Chapter | Missing-desc quest ids |
|---|---|
| g6_circuits_and_current | 051AB096CA0848B4, 7C0AC10000000001, 7C0AC10000000002, A818144300D946A8 |
| ren_archive_recordkeeping | 3D0C727EB7D7D9FC, 936044D132622461 |
| ren_nether_threshold | 1E5A8AEE45E9DDCA, FAB07684061A284D |
| what_waits_in_the_grove (Medieval) | 92614B6AD7E19E44, E101BB0D29F60954 |

The 56 `journey_to_ascension` misses are the check_quest mirror nodes, which intentionally
carry no player prose (verified against SHARED_CONTEXT: 56 mirror nodes, meta roadmap). NOT
a defect — do not author descs for them.

Cross-observation: 8 of the 10 missing-desc ids ALSO appear in the em-dash list (the ren/grove
ones) — these quests have prose in title/subtitle with em dashes but no desc key at all. The
2 g6 pairs (7C0AC10000000001/2) have no lang prose of any kind.

### E3. Non-array `quest_desc` (single-string form) — 7, EXPECTED 7 in ow6 CONFIRMED

All 7 are in `ow6_beyond_the_veil`: `4256011000EE0001` through `4256011000EE0007`. These use
`quest_desc: "..."` instead of the pack-standard `quest_desc: [ ... ]` array. Same 7 nodes
also carry em dashes (2 each). Normalize to array form to match the 1857/1864 pack standard.

### E4. at6 numbering gap — CONFIRMED clean, no dangling reference

No `at6_*.snbt` file exists (atomic chapters are at1–at5, at7, atomic_oritech_convergence).
Pack-wide case-insensitive grep for `at6` across `config/ftbquests/quests/` returns **zero
matches** — no file, no lang key, no dependency, no group ref points at an at6. The gap is a
pure numbering skip with no stale reference. Not a defect.

### E5. entering_the_iron_era — filename lies, no external cross-reference

- Internal `filename:` field = `"entering_the_iron_era"` (matches disk name).
- `group:` = `12B6640DF4C0DCFE` = **dark_ages** (verified). Chapter id = `620C470E078B2F83`.
- Chapter title (en_us.snbt line 109) = `"&6Entering the Medieval Age&r"`, subtitle
  "Forge iron and earn the right to leave this era." Confirms it is the Dark→Medieval
  transition chapter that lives in Dark Ages despite the "iron era" filename.
- Cross-references: grep for `entering_the_iron_era` and `620C470E078B2F83` across the whole
  quests tree returns ONLY its own file (lines 5, 11) and its own two lang keys. **No other
  file or dependency references it.** No stale/broken link.

### E6. Duplicate quest ids — 0

Anchored parser (quest-object-level `id:` capture, immune to `autofocus_id:`/task/reward id
false-positives): every one of the 1930 quest ids is unique across all 56 chapters.

---

## F. Dependency-graph sanity (whole pack)

Script parses all 1930 quest ids and every `dependencies:` edge, builds forward + reverse
adjacency, and classifies. Chapter→age resolved via the VERIFIED group map in SHARED_CONTEXT.

### F1. Dangling dependencies — 0

Every dependency target id resolves to a real quest id somewhere in the pack, including all
cross-chapter edges (e.g. ow6 nodes depending on ids in ow2/ow3 all resolve). No orphaned
edge points at a deleted or mistyped id.

### F2. Orphan clusters — 0

No quest has both zero dependencies AND zero dependents. Every quest is wired into the graph
(has a parent, a child, or both). This means there are no rootless always-visible UX-leak
quests introduced. (FTBQ shows rootless quests immediately; the corrected reveal spine relies
on only 3 Dark entries being rootless — those 3 are depended-upon roots of their trees, so
they are NOT flagged as orphans; they have dependents.)

### F3. Backward-age dependencies — 0

No quest in a lower age depends on a quest in a higher age. Age discipline holds across every
cross-chapter edge. Journey/annex (age-agnostic) edges were excluded from the age comparison
by design (they are meta/roadmap and would false-positive against the ordered ladder).

---

## Verdict

Structurally the pack is clean on the load-bearing checks: **0 duplicate ids, 0 dangling
deps, 0 orphans, 0 backward-age deps.** The graph is sound and age discipline is intact.

Remaining defects are prose/lang-layer, all in the Opus prose lane:
1. **BROKEN:** 10 real quests with no `quest_desc` key (4 g6 + 2 ren_archive + 2 ren_nether +
   2 grove) — players see blank descriptions. Author these.
2. **HYGIENE:** 87 em dashes (23 non-journey keys are the priority) — replace per style rule.
3. **HYGIENE:** 7 ow6 `quest_desc` in single-string form — normalize to array (these 7 also
   carry the em dashes and are the same nodes flagged in E1/E3).

No softlocks, no structural repair, no chapter edits required for E/F. Fix is entirely in
`lang/en_us.snbt`.
