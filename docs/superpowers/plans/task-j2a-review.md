# J2A Chapter Task Review
**Reviewer:** Independent automated audit (Claude Sonnet 4.6)
**Date:** 2026-06-24
**Artifacts reviewed:**
- `config/ftbquests/quests/chapters/journey_to_ascension.snbt`
- `.aoa_reveal_audit/gen_j2a.py`
- Ground truth from `python -c` extraction against all live chapter files

---

## (1) SPEC COMPLIANCE: PASS with one Important finding

All hard constraints pass. One Important visual-stall issue found (no functional regression).

## (2) TASK QUALITY: Approved

The generator is correct, the SNBT is clean, reward faithfulness is 100%, and all structural constraints are met.

---

## Findings

### Critical — none

### Important

**OW Gateway visual stall (design gap, no functional regression)**

The real OW gateway quest (`4358010000010003`) requires only 6 Atomic quests as deps (nuclear dawn, chain reaction, machine soul, threshold of war, Baal, and Geburah). It does NOT require Valamon (`4646010000010000`), Gomoria (`4646010000010001`), Gargamaw (`4646010000010002`), or Tremorzilla (`4358010000010001`).

The J2A OW gateway node (`535001000002005C`) has all 10 Atomic mirror nodes as visual deps, including the 4 excluded bosses. This means the J2A OW gateway node will auto-complete LATER than the real quest fires (it waits until all 4 extra boss mirrors are also done). Consequence: roadmap shows the OW gateway as incomplete even after the player has received `otherworldly` and `at_capstone_complete` stages. The stages are NOT withheld (already granted by real quest), so there is no functional softlock — pure visual mismatch in the roadmap chapter.

Same pattern exists for the Atomic gateway (`5350010000020051`): the real Gilded band gateway (`5057011000000004`) does require `5057011000000003` as dep, so that pair is fine. All other tested gateway fan-ins are sound.

**Scope question on `aoa_complete` finale node shape**

Node `535001000002006B` (finale, binding `4153010000010002`) is `shape: "hexagon"`. The gen_j2a.py classifies a node as gateway (hexagon) if its stage list intersects `AGE_STAGES` which includes `aoa_complete`. This is correct per spec. However `aoa_complete` is the pack-completion sentinel, not a proper "age gate", so a circle might be more appropriate aesthetically. Not a spec violation.

### Minor

**`aoa:age/dark_ages` advancement only fires from J2A start node, never tested by real quest**

The spec mandates the start node grant `dark_ages + aoa:age/dark_ages`. No other chapter fires `aoa:age/dark_ages`, so this is original (not a mirror of a real quest command). This is intended — the start node is the sole origin. Verified present and correct. Noting it because there is no live counterpart to cross-check against.

**Ascension finale has no `aoa:age/ascension` re-fire**

The J2A node for `4153010000010002` (asc_capstone) does not grant `aoa:age/ascension`. The real quest grants `aoa:journey/ascension_sealed` (a different advancement namespace, not `aoa:age/`). The `aoa:age/ascension` advancement is already fired by the OW capstone gateway node (`5350010000020064`) which correctly mirrors `4256010000010006`. Verified correct — no missing advancement.

**Generator `capstone_map.py` referenced in task spec but does not exist**

The task description says "Run `python .aoa_reveal_audit/capstone_map.py` to get the authoritative list." That file does not exist in `.aoa_reveal_audit/` (only `gen_j2a.py` is present). Ground truth was extracted by direct chapter scanning instead. No functional impact to the artifact under review, but the missing utility should be created for future audits.

---

## Detailed Verification Results

### Node count
- Total nodes: **55** ✅
- Per-band: Dark=2, Medieval=1, Renaissance=11, Industrial=7, Gilded=8, Atomic=11, Otherworldly=8, Ascension=7 ✅

### Reward faithfulness (all 55 nodes)
- Every node's stage list exactly matches the stages found in the real grant quest ✅
- No extra stages, no missing stages ✅
- Multi-stage quests correct: `4E44010000010004` fires both `at_radiological_materials_complete` AND `at_create_nuclear_mainline_complete` ✅
- `0B0310A0000000F0` fires `industrial_revolution` + `ren_seal_obtained` + `aoa:age/industrial_revolution` ✅
- `5057011000000003` fires `void_titan_defeated` + `g_temporal_authorization_complete`, no advancement (correct — real quest has no `aoa:age/` grant) ✅
- All 8 gateway nodes fire the `aoa:age/<age>` advancement ✅ (except Ascension finale which correctly does not, and Dark start which fires it as original)
- `asc_capstone` finale fires no `aoa:age/` (real quest grants `aoa:journey/ascension_sealed`, not `aoa:age/`) ✅

### Structural constraints
- `tasks: [ ]` on all 55 nodes ✅
- `progression_mode: "default"` ✅
- All 4 hide flags = false on all nodes ✅
- `can_repeat: true` absent ✅
- Start node (`5350010000010000`) rootless (no deps) ✅
- Start node id matches spec ✅
- No other chapter references any J2A mirror node id ✅
- No duplicate node ids ✅

### Line endings
- SNBT: 1670 CRLF, 0 bare LF ✅
- Lang: 7460 CRLF, 0 bare LF ✅

### Lang keys
- 110 keys (55 nodes × 2) all present ✅
- Start node has exactly 2 keys (title + quest_subtitle), no duplicates ✅
- No orphan keys for old ids `5350010000010001`–`535001000001000E` ✅

### Dependency shape
- All gateway nodes (hexagon) have correct fan-in: real quest id first, then all prior-band capstone mirror node ids ✅
- IR gateway (20042): 11 deps, all 10 Ren capstone mirrors + real quest ✅
- Gilded gateway (20049): 7 deps ✅
- Atomic gateway (20051): 8 deps (Gilded capstones including 5057011000000003 mirror) ✅
- OW gateway (005C): 11 deps (10 Atomic mirrors including optional bosses — stall risk noted above) ⚠️
- Asc gateway (20064): 8 deps ✅
- Asc finale (006B): 7 deps ✅

### Mechanism soundness
- Task-less nodes under `progression_mode: "default"` auto-complete when all deps are satisfied ✅
- Real quest binding dep guarantees completion drive comes from actual gameplay ✅
- Visual-neighbour deps are always from the prior gateway (which itself completes when prior age's grant fires) — no cycles ✅
- Only stall risk is OW gateway waiting on optional-in-real-chapter boss mirrors (noted as Important)

### Generator quality
- `detect_eol`: correct for pure-CRLF, pure-LF, and majority-decides mixed files ✅
- `merge_lang`: strips `\r` before split, re-joins with detected eol — correct ✅
- Icon re-indent: `extract_icon()` strips leading tabs, re-indents to `\t\t\t` — verified in output, no misindented quest icons ✅
- ID collision check (`assert len(nids) == len(set(nids))`) present in dry-run path ✅
- Missing `capstone_map.py` means the stated "run this to get ground truth" workflow is broken for future maintainers ⚠️

---

## Bottom line

The artifact is correct and shippable. The one Important finding (OW gateway roadmap display lags behind stage grant by up to 4 optional bosses) is a visual cosmetic issue only and causes no functional regression — stages are always granted on time by the real quest. All 55 nodes, all 66 stages, all reward commands, line endings, lang keys, and dependency wiring are verified correct.
