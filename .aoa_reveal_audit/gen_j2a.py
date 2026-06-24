#!/usr/bin/env python3
"""Generate the Journey to Ascension full-roadmap chapter (Design D, every stage check).

Rewrites config/ftbquests/quests/chapters/journey_to_ascension.snbt as 55 task-less
mirror nodes (one per stage-granting quest) and merges quest.<id>.title/.quest_subtitle
keys into config/ftbquests/quests/lang/en_us.snbt. CRLF preserved. No script changes.

Mechanism: each node is task-less; its binding dependency is the real grant quest, so under
progression_mode "default" it auto-completes (and re-fires the /astages reward) when that
quest completes. Neighbour deps draw the Option-D funnel.
"""
import re, os, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH   = os.path.join(ROOT, 'config', 'ftbquests', 'quests', 'chapters')
JF   = os.path.join(CH, 'journey_to_ascension.snbt')
LANG = os.path.join(ROOT, 'config', 'ftbquests', 'quests', 'lang', 'en_us.snbt')

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
    ("Renaissance",  ["0B03101000000039","0B03102000000062","0B03103000000031","0B03104000000050",
                      "0B03105000000050","0B03106000000050","0B03107000000050","0B031080000000F2",
                      "0B03109000000060","0B0310A000000014","0B0310A0000000F0"]),   # last = gateway -> industrial_revolution
    ("Industrial",   ["4954021000000016","4954051000000011","495406100000001D","49540A100000000F",
                      "49540B1000000015","49540C1000000006","4954631000000000"]),   # last = gateway -> gilded_age
    ("Gilded",       ["5246011000000007","4D4E011000000006","4D4F011000000005","4D50011000000003",
                      "4F47011000000002","4341011000000004","5057011000000003","5057011000000004"]), # last = gateway -> atomic
    ("Atomic",       ["4E44010000010004","4348010000010004","4D53010000010003","5457010000010003",
                      "4646010000010000","4646010000010001","4646010000010002","4646010000010003",
                      "4358010000010001","4358010000010002","4358010000010003"]),   # last = gateway -> otherworldly
    ("Otherworldly", ["4C57010000010004","4C58010000010005","4454010000010005","4C59010000010004",
                      "4443010000010006","4256010000010004","4256010000010005","4256010000010006"]), # last = gateway -> ascension
    ("Ascension",    ["5449010000010006","5044010000010006","5347010000010002","4448010000010005",
                      "425201000001000B","4153010000010001","4153010000010002"]),   # last = finale -> aoa_complete
]

# friendly titles per real quest id (roadmap readability; colour-coded by band)
TITLES = {
 "5350010000010000":"Dark Ages","097AED7C91033D5E":"Medieval Times","6D7E8F901A2B1054":"The Renaissance",
 "0B03101000000039":"Magic Foundations","0B03102000000062":"Nether Threshold","0B03103000000031":"Aether Literacy",
 "0B03104000000050":"Starlight Observation","0B03105000000050":"Undergarden Descent","0B03106000000050":"Deeper & Darker",
 "0B03107000000050":"Archive Recordkeeping","0B031080000000F2":"Observation & Experimentation","0B03109000000060":"End Threshold",
 "0B0310A000000014":"Maledictus Vigil","0B0310A0000000F0":"Industrial Revolution",
 "4954021000000016":"Factory Discipline","4954051000000011":"Power & Motion","495406100000001D":"Pressure Chemistry",
 "49540A100000000F":"Digital Logistics","49540B1000000015":"Magic Feedstock","49540C1000000006":"Obsidilith",
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
 "5449010000010006":"Table of Infinities","5044010000010006":"Philosopher's Dream","5347010000010002":"Singularity",
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
    """real_quest_id -> {'stages':[...], 'adv':bool, 'icon':str_block, 'file':name}"""
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
            if not stages:
                continue
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
    return ordered, qmap, node_id

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
    """real_id -> [neighbour journey-node ids] (visual). Binding real-quest dep added in emit()."""
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
            deps[rid] = [prev_gateway_nid]
        for rid in gws:
            # Gateway hangs off the PRIOR gateway (age spine), NOT its band's caps.
            # Fanning in caps would stall the gateway (and the whole downstream chain) for
            # any player who skips an OPTIONAL boss-kill node in the band (Obsidilith,
            # Void Titan, the Macabre bosses, Tremorzilla, Leviathan, ...). The prior
            # gateway grants a prerequisite age stage, so it always completes first ->
            # binding dep stays the node's own real quest, with zero false stalls.
            deps[rid] = [prev_gateway_nid]
            prev_gateway_nid = node_id[rid]
    return deps

def reward_blocks(rid, qmap, base):
    """re-fire command rewards for this real quest's stage(s) (+ aoa:age adv on gateways)."""
    out, rid_n = [], base
    if rid == START_ID:
        stages, adv, age = ["dark_ages"], True, "dark_ages"
    else:
        info = qmap[rid]
        stages = info['stages']; adv = info['adv']
        age = next((s for s in stages if s in AGE_STAGES), None)
    for s in stages:
        out.append(("/astages add {p} %s true true" % s, rid_n)); rid_n += 1
    if adv and age:
        out.append(("/advancement grant {p} only aoa:age/%s" % age, rid_n)); rid_n += 1
    return out, rid_n

def emit(ordered, qmap, node_id, pos, deps, eol):
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
    rbase = 0x5350010000004000
    for band, rid, gw in ordered:
        nid = node_id[rid]
        x,y = pos[rid]
        dep_ids = []
        if rid != START_ID:
            dep_ids.append(rid)               # cross-chapter binding dep (real quest)
            dep_ids += deps[rid]              # neighbour mirror node ids (visual funnel)
        rblocks, rbase = reward_blocks(rid, qmap, rbase)
        if rid != START_ID:
            icon = qmap.get(rid,{}).get('icon')
        else:
            # Use eol-safe multiline icon for start node
            icon = None
            w(T*2+"{")
            if dep_ids:
                w(T*3+'dependencies: [%s]' % ", ".join('"%s"' % v for v in dep_ids))
            w(T*3+'hide_details_until_startable: false')
            w(T*3+'hide_text_until_complete: false')
            w(T*3+'hide_until_deps_complete: false')
            w(T*3+'hide_until_deps_visible: false')
            w(T*3+'icon: {'); w(T*4+'id: "minecraft:campfire"'); w(T*3+'}')
            w(T*3+'id: "%s"' % nid)
            if rblocks:
                w(T*3+'rewards: [')
                for cmd, rrid in rblocks:
                    w(T*4+'{')
                    w(T*5+'auto: "enabled"')
                    w(T*5+'command: "%s"' % cmd)
                    w(T*5+'id: "%s"' % format(rrid,'X').rjust(16,'0'))
                    w(T*5+'permission_level: 2')
                    w(T*5+'silent: true')
                    w(T*5+'team_reward: true')
                    w(T*5+'type: "command"')
                    w(T*4+'}')
                w(T*3+']')
            w(T*3+'shape: "%s"' % ("hexagon" if gw else "circle"))
            w(T*3+'size: %sd' % ("1.5" if gw else "1.0"))
            w(T*3+'tasks: [ ]')
            w(T*3+'x: %sd' % x)
            w(T*3+'y: %sd' % y)
            w(T*2+"}")
            continue
        w(T*2+"{")
        if dep_ids:
            w(T*3+'dependencies: [%s]' % ", ".join('"%s"' % v for v in dep_ids))
        w(T*3+'hide_details_until_startable: false')
        w(T*3+'hide_text_until_complete: false')
        w(T*3+'hide_until_deps_complete: false')
        w(T*3+'hide_until_deps_visible: false')
        if icon:
            # Strip leading tabs, re-indent to T*3 depth, join with eol-safe separator
            ic_lines = re.sub(r'^\t*', '', icon, flags=re.M).splitlines()
            for ic_ln in ic_lines:
                w(T*3 + ic_ln if ic_ln.strip() else ic_ln)
        else:
            w(T*3+'icon: {'); w(T*4+'id: "minecraft:paper"'); w(T*3+'}')
        w(T*3+'id: "%s"' % nid)
        if rblocks:
            w(T*3+'rewards: [')
            for cmd, rrid in rblocks:
                w(T*4+'{')
                w(T*5+'auto: "enabled"')
                w(T*5+'command: "%s"' % cmd)
                w(T*5+'id: "%s"' % format(rrid,'X').rjust(16,'0'))
                w(T*5+'permission_level: 2')
                w(T*5+'silent: true')
                w(T*5+'team_reward: true')
                w(T*5+'type: "command"')
                w(T*4+'}')
            w(T*3+']')
        w(T*3+'shape: "%s"' % ("hexagon" if gw else "circle"))
        w(T*3+'size: %sd' % ("1.5" if gw else "1.0"))
        w(T*3+'tasks: [ ]')
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
        else:
            sub = "Grants: " + ", ".join(qmap[rid]['stages'])
        out["quest.%s.quest_subtitle" % nid] = sub
    return out

def merge_lang(entries, eol):
    raw = open(LANG,'rb').read().decode('utf-8')
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
    ordered, qmap, node_id = build()
    pos = layout(ordered)
    deps = deps_for(ordered, node_id)
    eol = detect_eol(JF); leol = detect_eol(LANG)
    snbt = emit(ordered, qmap, node_id, pos, deps, eol)
    entries = lang_entries(ordered, qmap, node_id)
    from collections import Counter
    print("nodes: %d (start + %d mirrors)" % (len(ordered), len(ordered)-1))
    print("per band:", dict(Counter(b for b,_,_ in ordered)))
    print("lang keys to add:", len(entries))
    nids = list(node_id.values())
    assert len(nids) == len(set(nids)), "node id collision!"
    if dry:
        print("DRY-RUN (pass --write to apply). First mirror node id:", nids[1])
        return 0
    lang_out = merge_lang(entries, leol)
    open(JF,'wb').write(snbt.encode('utf-8'))
    open(LANG,'wb').write(lang_out.encode('utf-8'))
    print("WROTE", JF, "and merged lang.")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
