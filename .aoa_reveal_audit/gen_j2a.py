#!/usr/bin/env python3
"""Generate the Journey to Ascension full-roadmap chapter (table of contents, check_quest gated).

Rewrites config/ftbquests/quests/chapters/journey_to_ascension.snbt as a 55-node arc
roadmap (one mirror node per stage-granting quest) and merges quest.<id>.title/.quest_subtitle
keys into config/ftbquests/quests/lang/en_us.snbt. CRLF preserved. No script changes.

Mechanism: every mirror node carries a More Quest Types `check_quest` task (type "check_quest")
targeting its real capstone quest. The task self-polls (autoSubmitOnPlayerTick) and completes the
node the moment that capstone is completed by the team -- so a fresh world grants nothing, and
each node lights up exactly when its capstone is earned. This is REQUIRED because the quest file
is progression_mode "flexible", under which a task-LESS quest auto-completes on world entry
(canStartTasks ignores dependencies) and would fire every /astages reward at once.

Granting is owned solely by the real capstone quests (+ aoa_astages_team_grant.js); the mirror
nodes grant nothing. The ONLY exception is the Dark entry node, which stays task-less and
auto-grants dark_ages at world entry (the intended starting-age grant).

Dependency lines are purely the visual table of contents: each band's capstones converge INTO the
gate they unlock (diamond), so a player reads "complete these capstones to open this gate". Because
check_quest decouples completion from dependencies, this convergence never stalls a gate even if an
optional boss capstone is skipped.
"""
import re, os, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH   = os.path.join(ROOT, 'config', 'ftbquests', 'quests', 'chapters')
JF   = os.path.join(CH, 'journey_to_ascension.snbt')
LANG = os.path.join(ROOT, 'config', 'ftbquests', 'quests', 'lang', 'en_us.snbt')

# Live authority + the copy-if-absent modpack_defaults tree (doubled config/ nesting).
# Both are regenerated so a fresh install matches an existing one.
MD   = os.path.join(ROOT, 'config', 'modpack_defaults', 'config', 'ftbquests', 'quests')
WRITE_TARGETS = [
    (JF, LANG),
    (os.path.join(MD, 'chapters', 'journey_to_ascension.snbt'), os.path.join(MD, 'lang', 'en_us.snbt')),
]

CHAPTER_ID = "5350010000000001"
GROUP_ID   = "5350010000000000"
START_ID   = "5350010000010000"   # keep; rootless dark_ages grant

AGE_STAGES = {"dark_ages","medieval_times","the_renaissance","industrial_revolution",
              "gilded_age","atomic","otherworldly","ascension","aoa_complete"}

# ---- band order: (band_label, [real_quest_id ...] capstones-then-gateway) ----
# Gateway is the LAST id in each band's list. Derived from capstone_map.py output.
BANDS = [
    ("Dark",         ["097AED7C91033D5E"]),                         # gateway -> medieval_times (start node prepended separately)
    ("Medieval",     ["6D7E8F901A2B1054"]),                         # gateway -> the_renaissance
    ("Renaissance",  ["0B03101000000039","0B03102000000062","0B03103000000101","0B03104000000100",
                      "0B03105000000100","0B03106000000050","0B03107000000050","0B031080000000F2",
                      "0B03109000000060","0B0310A000000014","0B0310A0000000F0"]),   # last = gateway -> industrial_revolution
    ("Industrial",   ["4954021000000016","4954051000000011","495406100000001D","49540A100000000F",
                      "49540B1000000015","49540C1000000006","49540C100000002F","4954631000000000"]),   # last = gateway -> gilded_age; 2F = Chesed exam
    ("Gilded",       ["5246011000000007","4D4E011000000006","4D4F011000000005","4D50011000000003",
                      "4F47011000000002","4341011000000004","5057011000000003","505701100000000C","5057011000000004"]), # last = gateway -> atomic; 0C = Malkuth exam
    ("Atomic",       ["4E44010000010004","4348010000010004","4D53010000010003","5457010000010003",
                      "4646010000010000","4646010000010001","4646010000010002","4646010000010003",
                      "4358010000010001","4358010000010002","4358010000010003"]),   # last = gateway -> otherworldly
    ("Otherworldly", ["4C57010000010004","4C58010000010005","4454010000010005","4C59010000010004",
                      "4443010000010006","4256010000010004","4256010000010005","4256010000010006"]), # last = gateway -> ascension
    ("Ascension",    ["5449010000010006","5044010000010006","494D010000010006","5347010000010002",
                      "4448010000010005","425201000001000B","4153010000010001","4153010000010002"]),   # last = finale -> aoa_complete; 494D=asc3 (no stage, gates finale)
]

# friendly titles per real quest id (roadmap readability; colour-coded by band)
TITLES = {
 "5350010000010000":"Dark Ages","097AED7C91033D5E":"Medieval Times","6D7E8F901A2B1054":"The Renaissance",
 "0B03101000000039":"Magic Foundations","0B03102000000062":"Nether Threshold","0B03103000000101":"Aether Literacy",
 "0B03104000000100":"Starlight Observation","0B03105000000100":"Undergarden Descent","0B03106000000050":"Deeper & Darker",
 "0B03107000000050":"Archive Recordkeeping","0B031080000000F2":"Observation & Experimentation","0B03109000000060":"End Threshold",
 "0B0310A000000014":"Maledictus Vigil","0B0310A0000000F0":"Industrial Revolution",
 "4954021000000016":"Factory Discipline","4954051000000011":"Power & Motion","495406100000001D":"Pressure Chemistry",
 "49540A100000000F":"Digital Logistics","49540B1000000015":"Magic Feedstock","49540C1000000006":"Obsidilith",
 "49540C100000002F":"Chesed","505701100000000C":"Malkuth",
 "4954631000000000":"Gilded Age",
 "5246011000000007":"Biotech Hazard Readiness","4D4E011000000006":"Scaled Logistics","4D4F011000000005":"Advanced Applied Industry",
 "4D50011000000003":"NauTec Oceanic Industry","4F47011000000002":"Atomic License","4341011000000004":"Magic Authorization",
 "5057011000000003":"Power Beyond Wires (Void Titan)","5057011000000004":"Atomic Age",
 "4E44010000010004":"Nuclear Dawn","4348010000010004":"Chain Reaction","4D53010000010003":"Machine Soul",
 "5457010000010003":"Threshold of War","4646010000010000":"Valamon","4646010000010001":"Gomoria",
 "4646010000010002":"Gargamaw","4646010000010003":"Baal","4358010000010001":"Tremorzilla","4358010000010002":"Geburah",
 "4358010000010003":"Otherworldly",
 "4C57010000010004":"Launch Window","4C58010000010005":"Strange Dimension Ops","4454010000010005":"Dragon Technology",
 "4C59010000010004":"Dyson Project","4443010000010006":"Digital Cosmos","4256010000010004":"Leviathan",
 "4256010000010005":"Beyond the Veil","4256010000010006":"Ascension",
 "5449010000010006":"Table of Infinities","5044010000010006":"Philosopher's Dream","494D010000010006":"The Impossible Machine","5347010000010002":"Singularity",
 "4448010000010005":"Draconic Heart","425201000001000B":"Bosses Rise","4153010000010001":"Archive of Ages",
 "4153010000010002":"Ascension Complete",
}
BAND_COLOR = {"Dark":"&8","Medieval":"&6","Renaissance":"&5","Industrial":"&7","Gilded":"&e",
              "Atomic":"&a","Otherworldly":"&b","Ascension":"&d"}

def norm(qid): return qid.strip().upper()

def iter_quest_blocks(text):
    # quests:[ ... ] then top-level { } objects separated at 2-tab depth
    m = re.search(r'\n\tquests: \[\n', text)
    if not m: return []
    body = text[m.end():]
    blocks, depth, start = [], 0, None
    i = 0
    while i < len(body):
        c = body[i]
        if c == '{':
            if depth == 0: start = i
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0 and start is not None:
                blocks.append(body[start:i+1]); start = None
        elif c == ']' and depth == 0:
            break
        i += 1
    return blocks

def top_id(blk):
    m = re.search(r'\n\t\t\tid: "([0-9A-Fa-f]{16})"', blk) or re.search(r'\bid: "([0-9A-Fa-f]{16})"', blk)
    return m.group(1) if m else None

def extract_icon(blk):
    m = re.search(r'\n(\t+)icon: \{(.*?)\n\1\}', blk, re.S)
    return m.group(0).strip('\n') if m else None

def load_quest_blocks():
    """real_quest_id -> {'stages':[...], 'adv':bool, 'icon':str_block, 'file':name}

    Indexes EVERY quest (not just stage-granting ones) so the roadmap can mirror required
    milestones that gate a finale via FTBQ dependencies without granting a stage themselves
    (e.g. asc3 'The Impossible Machine', a dependency of the Ascension finale)."""
    out = {}
    for f in sorted(glob.glob(CH + '/*.snbt')):
        if os.path.basename(f) == 'journey_to_ascension.snbt':
            continue
        text = open(f, 'rb').read().decode('utf-8').replace('\r\n', '\n')
        for blk in iter_quest_blocks(text):
            qid = top_id(blk)
            if not qid:
                continue
            stages = re.findall(r'astages add \{p\} ([a-z_0-9]+) ', blk)
            adv = bool(re.search(r'advancement grant \{p\} only aoa:age/', blk))
            icon = extract_icon(blk)
            out[norm(qid)] = {'stages': stages, 'adv': adv, 'icon': icon,
                              'file': os.path.basename(f)[:-5]}
    return out

def all_existing_ids():
    # Exclude the journey chapter itself so minted ids stay STABLE across re-runs
    # (otherwise a second --write sees the prior run's ids and shifts the new ones).
    ids = set()
    for f in glob.glob(os.path.join(ROOT,'config','ftbquests','quests','**','*.snbt'), recursive=True):
        if os.path.basename(f) == 'journey_to_ascension.snbt':
            continue
        raw = open(f,'rb').read().decode('utf-8','ignore')
        ids.update(x.upper() for x in re.findall(r'"([0-9A-Fa-f]{16})"', raw))
    return ids

def mint_ids(n, used):
    out, k = [], 0x5350010000020000
    while len(out) < n:
        cand = format(k, 'X').rjust(16, '0')
        if cand.upper() not in used:
            out.append(cand); used.add(cand.upper())
        k += 1
    return out

def detect_eol(path):
    b = open(path,'rb').read()
    return '\r\n' if b.count(b'\r\n') >= (b.count(b'\n') - b.count(b'\r\n')) else '\n'

def build():
    qmap = load_quest_blocks()
    ordered = [("Dark", START_ID, False)]
    for band, ids in BANDS:
        for j, rid in enumerate(ids):
            ordered.append((band, norm(rid), j == len(ids)-1))
    missing = [rid for (_,rid,_) in ordered if rid != START_ID and rid not in qmap]
    if missing:
        sys.exit("MISSING real quest ids (not found in live chapters): " + ", ".join(missing))
    used = all_existing_ids()
    node_id = {START_ID: START_ID}
    new_ids = mint_ids(len(ordered)-1, set(used) | {START_ID})
    for (_, rid, _), nid in zip([o for o in ordered if o[1] != START_ID], new_ids):
        node_id[rid] = nid
    # Mint check_quest task ids in a dedicated range (0x...5000, above the 0x...4000 reward range),
    # collision-checked against every existing id and the freshly minted node ids.
    used2 = {x.upper() for x in used} | {v.upper() for v in node_id.values()}
    task_id, k = {}, 0x5350010000005000
    for (_, rid, _) in ordered:
        if rid == START_ID:
            continue
        while True:
            cand = format(k, 'X').rjust(16, '0'); k += 1
            if cand.upper() not in used2:
                task_id[rid] = cand; used2.add(cand.upper()); break
    return ordered, qmap, node_id, task_id

def layout(ordered):
    """return real_id -> (x,y). 8 bands stacked; capstone rows wrap at 8; gateway centred below."""
    from collections import OrderedDict
    pos, y = {}, 0.0
    pos[START_ID] = (0.0, y); y += 2.0
    bands = OrderedDict()
    for band, rid, gw in ordered:
        if rid == START_ID: continue
        bands.setdefault(band, []).append((rid, gw))
    for band, items in bands.items():
        caps = [rid for rid,gw in items if not gw]
        gw   = [rid for rid,gw in items if gw]
        if caps:
            per = 8
            for ri in range(0, len(caps), per):
                row = caps[ri:ri+per]; n = len(row)
                x0 = -(n-1)
                for i, rid in enumerate(row):
                    pos[rid] = (round((x0 + i*2)*1.0, 2), round(y,2))
                y += 2.0
        for rid in gw:
            pos[rid] = (0.0, round(y,2)); y += 3.0
    return pos

def deps_for(ordered, node_id):
    """real_id -> [journey-node ids] (purely visual table-of-contents lines).

    Diamond per band: the prior gate fans out to the band's capstones, and those capstones
    converge INTO this band's gate. Completion is gated by each node's own check_quest task,
    NOT by these dependencies (flexible mode ignores deps for completion), so converging the
    caps into the gate is safe -- an optional boss capstone left undone never stalls the gate.
    """
    from collections import OrderedDict
    bands = OrderedDict()
    for band, rid, gw in ordered:
        if rid == START_ID: continue
        bands.setdefault(band, []).append((rid, gw))
    prev_gateway_nid = node_id[START_ID]
    deps = {START_ID: []}
    for band, items in bands.items():
        caps = [rid for rid,gw in items if not gw]
        gws  = [rid for rid,gw in items if gw]
        for rid in caps:
            deps[rid] = [prev_gateway_nid]                     # prior gate -> band caps (top of diamond)
        for rid in gws:
            if caps:
                deps[rid] = [node_id[c] for c in caps]         # band caps -> this gate (convergence)
            else:
                deps[rid] = [prev_gateway_nid]                 # gateway-only band (Dark/Medieval): spine
            prev_gateway_nid = node_id[rid]
    return deps

# NOTE: this generator intentionally emits ZERO command rewards. The roadmap is a pure
# table of contents. The only world-entry grant (dark_ages + aoa:age/dark_ages advancement)
# lives on a hand-authored invisible/optional/task-less node in the Dark Ages chapter
# stone_water_weather_and_wounds.snbt (quest id 3400000000009000). Do NOT reintroduce a
# reward_blocks() helper or wire per-node grants here -- that reintroduces the mass-grant bug
# (task-less/mirror nodes under flexible mode would fire every /astages reward at world entry).

def emit(ordered, qmap, node_id, task_id, pos, deps, eol):
    T = "\t"
    L = []
    def w(s=""): L.append(s)
    w("{")
    w(T+'default_hide_dependency_lines: false')
    w(T+'default_quest_shape: "circle"')
    w(T+'filename: "journey_to_ascension"')
    w(T+'group: "%s"' % GROUP_ID)
    w(T+'icon: {'); w(T*2+'id: "minecraft:compass"'); w(T+'}')
    w(T+'id: "%s"' % CHAPTER_ID)
    w(T+'order_index: 0')
    w(T+'progression_mode: "default"')
    w(T+'quest_links: [ ]')
    w(T+'quests: [')
    for band, rid, gw in ordered:
        nid = node_id[rid]
        x, y = pos[rid]
        # Dependencies are PURELY the visual table-of-contents lines (no cross-chapter binding
        # dep): completion is gated by each mirror node's check_quest task, not by these.
        dep_ids = list(deps[rid]) if rid != START_ID else []

        if rid == START_ID:
            # Dark entry: task-less root of the roadmap. It grants NOTHING. The roadmap is a
            # pure table of contents and must not itself grant any stage.
            # The world-entry dark_ages grant now lives on an invisible, task-less, optional
            # node in the Dark Ages chapter stone_water_weather_and_wounds.snbt
            # (quest id 3400000000009000, hand-authored, NOT emitted here). That node preserves
            # the auto-grant-at-world-entry semantics (flexible mode auto-completes a task-less
            # quest) while keeping this roadmap grant-free.
            w(T*2+"{")
            w(T*3+'hide_details_until_startable: false')
            w(T*3+'hide_text_until_complete: false')
            w(T*3+'hide_until_deps_complete: false')
            w(T*3+'hide_until_deps_visible: false')
            w(T*3+'icon: {'); w(T*4+'id: "minecraft:campfire"'); w(T*3+'}')
            w(T*3+'id: "%s"' % nid)
            w(T*3+'shape: "circle"')
            w(T*3+'size: 1.0d')
            w(T*3+'tasks: [ ]')
            w(T*3+'x: %sd' % x)
            w(T*3+'y: %sd' % y)
            w(T*2+"}")
            continue

        # Mirror node: check_quest task gates completion on the real capstone; grants nothing.
        icon = qmap.get(rid, {}).get('icon')
        tid = task_id[rid]
        w(T*2+"{")
        if dep_ids:
            w(T*3+'dependencies: [%s]' % ", ".join('"%s"' % v for v in dep_ids))
        w(T*3+'hide_details_until_startable: false')
        w(T*3+'hide_text_until_complete: false')
        w(T*3+'hide_until_deps_complete: false')
        w(T*3+'hide_until_deps_visible: false')
        if icon:
            ic_lines = re.sub(r'^\t*', '', icon, flags=re.M).splitlines()
            for ic_ln in ic_lines:
                w(T*3 + ic_ln if ic_ln.strip() else ic_ln)
        else:
            w(T*3+'icon: {'); w(T*4+'id: "minecraft:paper"'); w(T*3+'}')
        w(T*3+'id: "%s"' % nid)
        w(T*3+'shape: "%s"' % ("hexagon" if gw else "circle"))
        w(T*3+'size: %sd' % ("1.5" if gw else "1.0"))
        w(T*3+'tasks: [{')
        w(T*4+'id: "%s"' % tid)
        w(T*4+'mode: "ALL"')
        w(T*4+'required: 1L')
        w(T*4+'targets: ["%s"]' % rid)
        w(T*4+'type: "check_quest"')
        w(T*3+'}]')
        w(T*3+'x: %sd' % x)
        w(T*3+'y: %sd' % y)
        w(T*2+"}")
    w(T+']')
    w("}")
    return eol.join(L) + eol

def lang_entries(ordered, qmap, node_id):
    out = {}
    for band, rid, gw in ordered:
        nid = node_id[rid]
        title = TITLES.get(rid, qmap.get(rid,{}).get('file','Stage'))
        col = BAND_COLOR.get(band, "&f")
        gwmark = " ◆" if (gw and rid != START_ID) else ""
        out["quest.%s.title" % nid] = '%s%s%s&r' % (col, title, gwmark)
        if rid == START_ID:
            sub = "Granted at world entry."
        elif gw:
            sub = "Age gate. Clears when its capstone quest is complete."
        else:
            sub = "Capstone. Clears when its quest is complete."
        out["quest.%s.quest_subtitle" % nid] = sub
    return out

def merge_lang(entries, eol, lang_path):
    raw = open(lang_path,'rb').read().decode('utf-8')
    lines = [ln.rstrip('\r') for ln in raw.split('\n')]
    # Prune EVERY journey-node lang key before re-adding so the merge is idempotent and
    # self-cleaning: legacy nodes 5350010000010000..535001000001000E AND any minted mirror
    # id in the 535001000002xxxx range (incl. stale ones left by an earlier re-run).
    JOURNEY_KEY = re.compile(r'\tquest\.(535001000001000[0-9A-Ea-e]|535001000002[0-9A-Fa-f]{4})\.')
    keep, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if JOURNEY_KEY.match(ln):
            # single-line key -> skip it; array key ( ... [ ) -> skip until matching ]
            if ln.rstrip().endswith('['):
                depth = ln.count('[') - ln.count(']'); i += 1
                while i < len(lines) and depth > 0:
                    depth += lines[i].count('[') - lines[i].count(']'); i += 1
                continue
            i += 1; continue
        keep.append(ln); i += 1
    close = max(idx for idx,l in enumerate(keep) if l.strip() == '}')
    ins = ['\t%s: "%s"' % (k, entries[k].replace('"','\\"')) for k in sorted(entries)]
    keep = keep[:close] + ins + keep[close:]
    return eol.join(keep)

def main():
    dry = '--write' not in sys.argv
    ordered, qmap, node_id, task_id = build()
    pos = layout(ordered)
    deps = deps_for(ordered, node_id)
    entries = lang_entries(ordered, qmap, node_id)
    from collections import Counter
    print("nodes: %d (start + %d mirrors)" % (len(ordered), len(ordered)-1))
    print("per band:", dict(Counter(b for b,_,_ in ordered)))
    print("check_quest tasks:", len(task_id))
    print("lang keys to add:", len(entries))
    nids = list(node_id.values())
    tids = list(task_id.values())
    assert len(nids) == len(set(nids)), "node id collision!"
    assert len(tids) == len(set(tids)), "task id collision!"
    assert not (set(x.upper() for x in nids) & set(x.upper() for x in tids)), "node/task id overlap!"
    if dry:
        print("DRY-RUN (pass --write to apply). First mirror node id:", nids[1], "first task id:", tids[0])
        return 0
    for jf, lang in WRITE_TARGETS:
        if not (os.path.isfile(jf) and os.path.isfile(lang)):
            print("SKIP (absent):", jf)
            continue
        # Force CRLF for the chapter file: the pack standard is CRLF (all other chapters + the
        # modpack_defaults copy use it). The live j2a drifted to bare-LF during the mass-grant
        # hand-fix; detect_eol() would preserve that drift, so override to restore CRLF parity.
        # Lang EOL stays detected (do not rewrite the whole lang file's line endings here).
        feol = '\r\n'; leol = detect_eol(lang)
        # Compute BOTH outputs before opening for write -- merge_lang reads `lang`, and opening
        # it in 'wb' truncates first, so reading must happen before the open.
        snbt_out = emit(ordered, qmap, node_id, task_id, pos, deps, feol)
        lang_out = merge_lang(entries, leol, lang)
        open(jf,  'wb').write(snbt_out.encode('utf-8'))
        open(lang,'wb').write(lang_out.encode('utf-8'))
        print("WROTE", jf, "and merged", lang)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
