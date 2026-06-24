# J2A Full Roadmap Implementation Report

**Branch:** quest-prose-cc1-cc2  
**Date:** 2026-06-24  
**Status:** DONE

## Summary

Applied `gen_j2a.py --write` to build 55 task-less mirror nodes into `journey_to_ascension.snbt`
and merged 110 lang keys into `en_us.snbt`. One bug found and fixed in the generator (bare LF in
icon blocks); all validation checks passed after fix.

---

## Step-by-Step Execution

### Step 1: Backups

```
cp config/ftbquests/quests/chapters/journey_to_ascension.snbt /tmp/j2a_journey.bak
cp config/ftbquests/quests/lang/en_us.snbt /tmp/j2a_lang.bak
```

Confirmed: both backed up to `/tmp/` (= `C:/Users/andre/AppData/Local/Temp/` on Windows).

### Step 2: First Apply (Before Fix)

```
python .aoa_reveal_audit/gen_j2a.py --write
```

Output:
```
nodes: 55 (start + 54 mirrors)
per band: {'Dark': 2, 'Medieval': 1, 'Renaissance': 11, 'Industrial': 7, 'Gilded': 8, 'Atomic': 11, 'Otherworldly': 8, 'Ascension': 7}
lang keys to add: 110
WROTE ...journey_to_ascension.snbt and merged lang.
```

### Step 3: CRLF Failure Found

CRLF check revealed:
```
journey_to_ascension.snbt: CRLF=1560  bareLF=110  PASS=False
en_us.snbt: CRLF=7460  bareLF=0  PASS=True
```

Root cause: `emit()` in gen_j2a.py used hardcoded `"\n".join(...)` when re-emitting icon blocks
(extracted from source chapters which use LF-internally after `replace('\r\n','\n')`) and also
hardcoded `\n` in the START_ID campfire icon string. Since the chapter target is CRLF, those 110
icon-block lines (2 per node × 55 nodes) were written as bare LF.

### Step 4: gen_j2a.py Fix

Rewrote the `emit()` function to handle the START_ID node inline (using `w()` calls, no string
concatenation), and changed the mirror-node icon rendering from:

```python
ic = "\n".join(T*3 + ln if ln.strip() else ln for ln in ic.splitlines())
w(ic)
```

to per-line `w()` calls:

```python
ic_lines = re.sub(r'^\t*', '', icon, flags=re.M).splitlines()
for ic_ln in ic_lines:
    w(T*3 + ic_ln if ic_ln.strip() else ic_ln)
```

This ensures every icon line goes through the `eol.join(L)` at the end, preserving CRLF.

### Step 5: Clean Re-run

Restored chapter from backup (lang was already clean from first run; restored lang from backup
before second run to avoid duplicate keys). Re-ran `--write`:

```
python .aoa_reveal_audit/gen_j2a.py --write
# same node/lang counts as before
```

### Step 6: Full Validation Results

#### Chapter Structural Checks

| Check | Expected | Actual | Pass |
|-------|----------|--------|------|
| `tasks: [ ]` count | 55 | 55 | YES |
| `type: "checkmark"` count | 0 | 0 | YES |
| `type: "advancement"` count | 0 | 0 | YES |
| `progression_mode: "default"` | 1 | 1 | YES |
| `hide_until_deps_complete: false` | 55 | 55 | YES |

#### Spot-Checks

**Nuclear Dawn node** (mirrors `4E44010000010004`):
- Contains `/astages add {p} at_radiological_materials_complete true true` ✓
- Contains `/astages add {p} at_create_nuclear_mainline_complete true true` ✓

**Medieval gateway node** (mirrors `097AED7C91033D5E`):
- Contains `/astages add {p} medieval_times true true` ✓
- Contains `/advancement grant {p} only aoa:age/medieval_times` ✓

#### Lang File Checks

| Check | Expected | Actual | Pass |
|-------|----------|--------|------|
| Brace balance (open==close) | equal | 1==1 | YES |
| Bracket balance (open==close) | equal | 1860==1860 | YES |
| Bare LF | 0 | 0 | YES |
| `quest.535001000002*` keys (54×2) | 108 | 108 | YES |
| `quest.5350010000010000.*` keys | 2 | 2 | YES |
| Orphan keys `535001000001000[1-9A-E]` | 0 | 0 | YES |

**Lang line delta note:** Net +5 CRLF lines vs backup. This is correct: 45 old single-line key
headers + 60 multi-line `quest_desc: [...]` array content lines removed (15 nodes × ~4 lines each)
= 105 lines removed; 110 new single-line keys added; net = +5.

**Brace delta note:** The backup lang had 27 `{` occurrences (from 13 old `quest_desc` entries
embedding JSON clickEvent objects with `{"action":"change_page",...}`). The new format uses plain
strings, so the new lang has only 1 `{` (the top-level wrapper). Delta of -26 is expected.

#### Dep Resolution

```
Total quest IDs: 7229
Dependency IDs in J2A: 108
All deps resolve: PASS
```

108 deps = 54 real-quest binding deps + 54 neighbour mirror-node deps (the start node has no deps).

#### CRLF Final

```
journey_to_ascension.snbt: CRLF=1670  bareLF=0  PASS=True
en_us.snbt: CRLF=7460  bareLF=0  PASS=True
```

#### Scope Check

```
git status --short -- config/ftbquests/quests/chapters/journey_to_ascension.snbt config/ftbquests/quests/lang/en_us.snbt
M  config/ftbquests/quests/chapters/journey_to_ascension.snbt
M  config/ftbquests/quests/lang/en_us.snbt
```

No other chapter files, no kubejs files changed by this work. Pre-existing working-tree changes
in other files are unrelated to this session.

---

## Commits

| Commit | Message |
|--------|---------|
| `0ecab08` | `feat(quests): J2A full roadmap - 55 stage-check mirror nodes (Design D)` |

Files committed: `config/ftbquests/quests/chapters/journey_to_ascension.snbt`,
`config/ftbquests/quests/lang/en_us.snbt`, `.aoa_reveal_audit/gen_j2a.py` (CRLF fix).

---

## Generator Fix Detail

**File:** `.aoa_reveal_audit/gen_j2a.py`  
**Bug:** `emit()` function wrote icon blocks using Python string `"\n"` instead of the CRLF `eol`
variable, producing 110 bare-LF lines in an otherwise CRLF chapter file.  
**Fix:** Restructured START_ID block to use `w()` calls inline; replaced `"\n".join()` icon emit
with per-line `w()` calls so all lines pass through `eol.join(L)` at the end.
