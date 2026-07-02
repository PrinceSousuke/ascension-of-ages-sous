#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 0 Audit A -- item->stage tier / softlock audit for Ascension of Ages.

Reads:
  config/ftbquests/quests/chapters/*.snbt   (quest structure; task item ids)
  kubejs/server_scripts/aoa_astages_*.js    (AStages item/tag stage locks)

Produces (written next to this script under phase0/):
  A_tier_softlock_table.md   full row table
  A_tier_softlock.md         analysis writeup

Logic:
  - Resolve each chapter's age from its `group:` field via the SHARED_CONTEXT map.
  - Extract every `type: "item"` task, capturing the item id(s). Inline
    `item: { id: "ns:x" }` and ftbfiltersystem:smart_filter (`item(ns:x)` /
    `tag(ns:x)`) forms are both handled. Tags -> reported UNRESOLVED_TAG.
  - Flag `type: "checkmark"` tasks separately as ILLEGAL (none expected).
  - Build item->effective-stage from every `["stage","id","kind"]` literal array
    entry across the astages scripts (item locks + tag locks). Most-restrictive
    wins: effective stage = MAX age index across all files. Tag locks feed a
    separate tag->stage map used only when a task references a tag directly.
  - Compare each item-task's effective unlock stage against its chapter age.
    Later unlock stage than chapter age  -> verdict SOFTLOCK.
  - Items with NO lock that belong to a later-age mod family (per preamble)
    -> verdict CANON (tier inversion by mod family).

AUDIT ONLY. Writes nothing outside phase0/.
"""

import glob
import os
import re

PACK_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")
)
CHAPTERS = os.path.join(PACK_ROOT, "config", "ftbquests", "quests", "chapters")
ASTAGES = os.path.join(PACK_ROOT, "kubejs", "server_scripts")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---- 8-age ladder (index = ordering) -------------------------------------
AGES = [
    "dark_ages", "medieval_times", "the_renaissance", "industrial_revolution",
    "gilded_age", "atomic", "otherworldly", "ascension",
]
AGE_IDX = {a: i for i, a in enumerate(AGES)}

# ---- group id -> age (SHARED_CONTEXT.md, VERIFIED 2026-07-02) --------------
GROUP_AGE = {
    "12B6640DF4C0DCFE": "dark_ages",
    "508B59840C508057": "medieval_times",
    "0B038EB15EBBFD95": "the_renaissance",
    "3F77A31B7D30C0AA": "industrial_revolution",
    "5E42E6B4A7C91D30": "gilded_age",
    "7D28E4AEBC440F10": "atomic",
    "080F7BA9FFB8FC07": "otherworldly",
    "6A196D2B21EDE4C0": "ascension",
    "5350010000000000": "__journey__",   # meta roadmap, not an age
    "1A7F0E9D4C22B6F1": "__annex__",      # age-agnostic
}

# ---- mod-family later-age baseline (preamble sec.3) ------------------------
# family key -> earliest legal age. Used only for CANON (unlocked-but-late)
# detection. Namespace-prefixed; matched by the item's namespace where a whole
# family shares a floor. Kept conservative: only families the preamble states
# start no earlier than the given age, and only where the whole namespace does.
FAMILY_FLOOR = {
    "mekanism": "industrial_revolution",
    "mekanismgenerators": "industrial_revolution",
    "mekanismtools": "industrial_revolution",
    "ae2": "industrial_revolution",
    "refinedstorage": "industrial_revolution",
    "oritech": "industrial_revolution",
    "modern_industrialization": "industrial_revolution",
    "pneumaticcraft": "industrial_revolution",
    "immersiveengineering": "industrial_revolution",
    "immersivepetroleum": "industrial_revolution",
    "enderio": "industrial_revolution",
    "createnuclear": "industrial_revolution",
    "nuclearscience": "industrial_revolution",
    "electrodynamics": "industrial_revolution",
    "ballistix": "industrial_revolution",
    "powergrid": "industrial_revolution",
    "industrialforegoing": "gilded_age",
    "nautec": "gilded_age",
    "draconicevolution": "otherworldly",
    "stellaris": "otherworldly",
    "avaritia": "ascension",     # Re:Avaritia namespace
}

# ---------------------------------------------------------------------------
# 1. Parse AStages scripts -> item->stage and tag->stage (MAX age wins)
# ---------------------------------------------------------------------------
# Every lock file feeds a helper from literal arrays of the form
#   ["stage", "namespace:id", "kind"]   (kind sometimes a prose string)
# We match those literal 2/3-tuples. This deliberately does NOT execute the JS
# loops in 06/07 (programmatic c:material tag generation) -- those are recorded
# as a blind spot in the writeup.
ARR_RE = re.compile(
    r'\[\s*"([a-z_]+)"\s*,\s*"([^"]+)"\s*(?:,\s*"[^"]*")?\s*\]'
)

def parse_astages():
    item_stage = {}   # id -> (age, "file:line")
    tag_stage = {}    # tag -> (age, "file:line")
    files = sorted(glob.glob(os.path.join(ASTAGES, "aoa_astages_*.js")))
    for path in files:
        raw = open(path, "rb").read().decode("utf-8", "replace")
        fname = os.path.basename(path)
        # Determine whether each literal array feeds itemLocks or tagLocks by
        # locating the array-list variable it sits inside. Simpler + robust:
        # scan line by line, track the most recent `... Locks = [` / `tags = [`
        # opener so we know the target map.
        cur_map = None  # 'item' or 'tag'
        for lineno, line in enumerate(raw.replace("\r\n", "\n").split("\n"), 1):
            low = line
            if re.search(r'\btagLocks\s*=\s*\[', low) or re.search(r'\bitemTagLocks\s*=\s*\[', low):
                cur_map = "tag"
            elif re.search(r'\bitemLocks\s*=\s*\[', low) or re.search(r'\blocks\s*=\s*\[', low):
                cur_map = "item"
            m = ARR_RE.search(line)
            if not m:
                continue
            stage, ident = m.group(1), m.group(2)
            if stage not in AGE_IDX:
                continue  # not an age stage (e.g. a proof/marker stage) -> skip
            # decide target: tag if it looks like a tag (has a '/' path segment
            # after namespace, or we're inside a tagLocks list) else item
            is_tag = cur_map == "tag" or ("/" in ident.split(":", 1)[-1])
            tgt = tag_stage if is_tag else item_stage
            prev = tgt.get(ident)
            proof = "%s:%d" % (fname, lineno)
            if prev is None or AGE_IDX[stage] > AGE_IDX[prev[0]]:
                tgt[ident] = (stage, proof)
    return item_stage, tag_stage


# ---------------------------------------------------------------------------
# 2. Parse chapter SNBT -> list of (chapter, quest_id, item_or_tag, is_tag,
#    is_checkmark)
# ---------------------------------------------------------------------------
SMART_ITEM_RE = re.compile(r'\bitem\(([a-z0-9_.-]+:[a-z0-9_./-]+)\)')
SMART_TAG_RE = re.compile(r'\btag\(([a-z0-9_.-]+:[a-z0-9_./-]+)\)')
INLINE_ID_RE = re.compile(r'\bid:\s*"([a-z0-9_.-]+:[a-z0-9_./-]+)"')

def parse_chapters():
    """Depth-aware walk. Quest objects sit at brace-depth 2 inside `quests: [`.
    We record the quest id, then within its `tasks: [ ... ]` capture each task's
    type and item id(s)."""
    rows = []          # dicts
    chapter_age = {}   # filename -> (age, group)
    for path in sorted(glob.glob(os.path.join(CHAPTERS, "*.snbt"))):
        raw = open(path, "rb").read().decode("utf-8", "replace")
        text = raw.replace("\r\n", "\n").replace("\r", "\n")
        fname = os.path.splitext(os.path.basename(path))[0]
        gm = re.search(r'group:\s*"([0-9A-Fa-f]*)"', text)
        group = gm.group(1) if gm else ""
        age = GROUP_AGE.get(group, "__unknown__")
        chapter_age[fname] = (age, group)

        # Split into quest objects. Quests begin at lines matching '\t\t{'
        # (depth-2 object opener inside `quests: [`). Use a brace counter from
        # the `quests: [` marker to segment quests robustly.
        qstart = text.find("quests: [")
        if qstart < 0:
            continue
        body = text[qstart:]
        # Walk braces to find each top-level quest object inside the array.
        depth = 0
        in_array = False
        obj_start = None
        i = 0
        n = len(body)
        while i < n:
            c = body[i]
            if c == '"':  # skip strings
                i += 1
                while i < n and body[i] != '"':
                    if body[i] == "\\":
                        i += 1
                    i += 1
            elif c == "[":
                if not in_array:
                    in_array = True
                depth_bracket = True
            elif c == "{":
                if in_array and depth == 0:
                    obj_start = i
                    depth = 1
                elif depth > 0:
                    depth += 1
            elif c == "}":
                if depth > 0:
                    depth -= 1
                    if depth == 0 and obj_start is not None:
                        seg = body[obj_start:i + 1]
                        _scan_quest(seg, fname, rows)
                        obj_start = None
            elif c == "]":
                if in_array and depth == 0:
                    break  # end of quests array
            i += 1
    return rows, chapter_age


def _scan_quest(seg, fname, rows):
    # quest id = first top-level `id: "16HEX"` in the quest object
    qid_m = re.search(r'\bid:\s*"([0-9A-Fa-f]{16})"', seg)
    qid = qid_m.group(1) if qid_m else "?"
    # find tasks array
    tstart = seg.find("tasks: [")
    if tstart < 0:
        return
    # segment individual task objects the same brace-walk way
    tbody = seg[tstart:]
    depth = 0
    in_array = False
    obj_start = None
    i = 0
    n = len(tbody)
    while i < n:
        c = tbody[i]
        if c == '"':
            i += 1
            while i < n and tbody[i] != '"':
                if tbody[i] == "\\":
                    i += 1
                i += 1
        elif c == "[":
            in_array = True
        elif c == "{":
            if in_array and depth == 0:
                obj_start = i
                depth = 1
            elif depth > 0:
                depth += 1
        elif c == "}":
            if depth > 0:
                depth -= 1
                if depth == 0 and obj_start is not None:
                    _scan_task(tbody[obj_start:i + 1], fname, qid, rows)
                    obj_start = None
        elif c == "]":
            if in_array and depth == 0:
                break
        i += 1


def _scan_task(task, fname, qid, rows):
    tm = re.search(r'type:\s*"([a-z_]+)"', task)
    ttype = tm.group(1) if tm else "?"
    if ttype == "checkmark":
        rows.append(dict(chapter=fname, qid=qid, item="(checkmark task)",
                         is_tag=False, checkmark=True))
        return
    if ttype != "item":
        return
    # isolate the `item: { ... }` region (may be inline or contain smart_filter)
    im = re.search(r'\bitem:\s*\{', task)
    if not im:
        return
    # brace-match the item block
    j = task.find("{", im.start())
    depth = 0
    k = j
    while k < len(task):
        ch = task[k]
        if ch == '"':
            k += 1
            while k < len(task) and task[k] != '"':
                if task[k] == "\\":
                    k += 1
                k += 1
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                break
        k += 1
    itemblk = task[j:k + 1]

    if "smart_filter" in itemblk:
        got_items = SMART_ITEM_RE.findall(itemblk)
        got_tags = SMART_TAG_RE.findall(itemblk)
        for it in got_items:
            rows.append(dict(chapter=fname, qid=qid, item=it,
                             is_tag=False, checkmark=False))
        for tg in got_tags:
            rows.append(dict(chapter=fname, qid=qid, item=tg,
                             is_tag=True, checkmark=False))
        if not got_items and not got_tags:
            rows.append(dict(chapter=fname, qid=qid,
                             item="(smart_filter: no item()/tag() parsed)",
                             is_tag=False, checkmark=False))
    else:
        idm = INLINE_ID_RE.search(itemblk)
        if idm:
            iid = idm.group(1)
            if iid == "ftbfiltersystem:smart_filter":
                return
            rows.append(dict(chapter=fname, qid=qid, item=iid,
                             is_tag=False, checkmark=False))


# ---------------------------------------------------------------------------
# 3. Compare + verdict
# ---------------------------------------------------------------------------
def family_floor(item):
    ns = item.split(":", 1)[0]
    return FAMILY_FLOOR.get(ns)


def audit():
    item_stage, tag_stage = parse_astages()
    rows, chapter_age = parse_chapters()

    out_rows = []
    counts = dict(SOFTLOCK=0, CANON=0, ILLEGAL=0, OK=0, UNRESOLVED_TAG=0,
                  SKIP_META=0, VANILLA=0)

    for r in rows:
        chap = r["chapter"]
        age, group = chapter_age.get(chap, ("__unknown__", ""))
        qid = r["qid"]
        item = r["item"]

        if r.get("checkmark"):
            out_rows.append((chap, qid, item, "-", age, "ILLEGAL",
                             "checkmark task type is forbidden by canon"))
            counts["ILLEGAL"] += 1
            continue

        # meta / annex chapters are age-agnostic -> record but do not softlock
        if age in ("__journey__", "__annex__", "__unknown__"):
            counts["SKIP_META"] += 1
            continue

        if r["is_tag"]:
            ts = tag_stage.get(item)
            if ts:
                st, proof = ts
                verdict = "SOFTLOCK" if AGE_IDX[st] > AGE_IDX[age] else "OK-TAG"
                if verdict == "SOFTLOCK":
                    counts["SOFTLOCK"] += 1
                out_rows.append((chap, qid, item + " (tag)", st, age,
                                 verdict, proof))
            else:
                counts["UNRESOLVED_TAG"] += 1
                out_rows.append((chap, qid, item + " (tag)", "UNRESOLVED",
                                 age, "UNRESOLVED_TAG",
                                 "tag not statically locked; membership out of scope"))
            continue

        ns = item.split(":", 1)[0]
        # vanilla task items are their own canon violation but out of tier scope;
        # still, some minecraft: ids ARE locked (diamond/emerald) -> check locks.
        lock = item_stage.get(item)
        if lock:
            st, proof = lock
            if AGE_IDX[st] > AGE_IDX[age]:
                out_rows.append((chap, qid, item, st, age, "SOFTLOCK", proof))
                counts["SOFTLOCK"] += 1
            else:
                out_rows.append((chap, qid, item, st, age, "OK", proof))
                counts["OK"] += 1
        else:
            floor = family_floor(item)
            if floor and AGE_IDX[floor] > AGE_IDX[age]:
                out_rows.append((chap, qid, item, "(none) fam>=" + floor, age,
                                 "CANON",
                                 "no lock; %s family floor=%s > chapter" % (ns, floor)))
                counts["CANON"] += 1
            else:
                out_rows.append((chap, qid, item, "(none)", age, "OK",
                                 "no lock; family legal at/before chapter"))
                counts["OK"] += 1

    return out_rows, counts, item_stage, tag_stage, chapter_age


def write_table(out_rows):
    order = {"SOFTLOCK": 0, "ILLEGAL": 1, "CANON": 2, "UNRESOLVED_TAG": 3,
             "OK-TAG": 4, "OK": 5}
    srt = sorted(out_rows, key=lambda x: (order.get(x[5], 9), x[0], x[1]))
    lines = []
    lines.append("# Audit A -- item->stage tier / softlock table")
    lines.append("")
    lines.append("Generated by `tier_audit.py`. Rows sorted by verdict severity.")
    lines.append("")
    lines.append("| chapter | quest id | item | effective unlock stage | chapter age | verdict | proof |")
    lines.append("|---|---|---|---|---|---|---|")
    for (chap, qid, item, st, age, verdict, proof) in srt:
        lines.append("| %s | %s | `%s` | %s | %s | **%s** | %s |" % (
            chap, qid, item, st, age, verdict, proof))
    lines.append("")
    open(os.path.join(OUT_DIR, "A_tier_softlock_table.md"), "w",
         encoding="utf-8").write("\n".join(lines))
    return srt


if __name__ == "__main__":
    out_rows, counts, item_stage, tag_stage, chapter_age = audit()
    srt = write_table(out_rows)
    print("=== COUNTS ===")
    for k in ("SOFTLOCK", "ILLEGAL", "CANON", "UNRESOLVED_TAG", "OK-TAG", "OK",
              "SKIP_META"):
        print("%-16s %d" % (k, counts.get(k, 0)))
    print("total item_stage locks parsed:", len(item_stage))
    print("total tag_stage locks parsed:", len(tag_stage))
    print("total chapters:", len(chapter_age))
    print()
    print("=== SOFTLOCK + ILLEGAL rows ===")
    for row in srt:
        if row[5] in ("SOFTLOCK", "ILLEGAL"):
            print(row)
    print()
    print("=== CANON rows ===")
    for row in srt:
        if row[5] == "CANON":
            print(row)
