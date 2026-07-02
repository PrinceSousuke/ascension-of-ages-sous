# Phase 0 audit E + F: FTBQ structural hygiene + dependency graph
# AUDIT ONLY. Reads chapters/*.snbt and lang/en_us.snbt. Writes nothing but the report (done by caller).
import os, re, json, collections

ROOT = r"C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)\config\ftbquests\quests"
CHAP = os.path.join(ROOT, "chapters")
LANG = os.path.join(ROOT, "lang", "en_us.snbt")

# chapter file -> age (from SHARED_CONTEXT verified map)
AGE_ORDER = ["dark_ages","medieval_times","the_renaissance","industrial_revolution",
             "gilded_age","atomic","otherworldly","ascension","journey","annex"]
AGE_IDX = {a:i for i,a in enumerate(AGE_ORDER)}

FILE_AGE = {
 "stone_food_and_farming_pressures":"dark_ages","stone_water_weather_and_wounds":"dark_ages",
 "entering_the_iron_era":"dark_ages",
 "m1_first_mill":"medieval_times","m3_relics_and_burrows":"medieval_times",
 "metallurgy":"medieval_times","what_waits_in_the_grove":"medieval_times",
 "ren_aether_literacy":"the_renaissance","ren_archive_recordkeeping":"the_renaissance",
 "ren_deeper_darker_otherside":"the_renaissance","ren_end_threshold":"the_renaissance",
 "ren_magic_foundations":"the_renaissance","ren_maledictus_vigil":"the_renaissance",
 "ren_nether_threshold":"the_renaissance","ren_observation_experimentation":"the_renaissance",
 "ren_second_mill_steam_rail_logistics":"the_renaissance","ren_starlight_observation":"the_renaissance",
 "ren_undergarden_descent":"the_renaissance",
 "ir_automation_safety_and_routing":"industrial_revolution","ir_create_industrial_addons":"industrial_revolution",
 "ir_immersive_engineering_early_factory":"industrial_revolution","ir_ir_side_gear_hidden_equipment":"industrial_revolution",
 "ir_magic_feedstock_and_spectrum_network":"industrial_revolution","ir_modern_industrialization_steam_industry":"industrial_revolution",
 "ir_netherite_citadel_obsidilith":"industrial_revolution","ir_pneumaticcraft_pressure_plastic":"industrial_revolution",
 "ir_power_motion_and_grid":"industrial_revolution",
 "g1_the_golden_workshop":"gilded_age","g2_the_refinery":"gilded_age","g4_the_infinite_grid":"gilded_age",
 "g5_empire_of_iron":"gilded_age","g6_circuits_and_current":"gilded_age","g7_chartered_arcana":"gilded_age",
 "g_power_beyond_wires":"gilded_age",
 "at1_nuclear_dawn":"atomic","at2_the_periodic_table":"atomic","at3_chain_reaction":"atomic",
 "at4_machine_soul":"atomic","at5_threshold_of_war":"atomic","at7_chaos_convergence":"atomic",
 "atomic_oritech_convergence":"atomic",
 "ow1_launch_window":"otherworldly","ow2_strange_dimension_operations":"otherworldly",
 "ow3_dragon_technology":"otherworldly","ow4_the_dyson_project":"otherworldly",
 "ow5_the_digital_cosmos":"otherworldly","ow6_beyond_the_veil":"otherworldly",
 "asc1_the_table_of_infinities":"ascension","asc2_the_philosophers_dream":"ascension",
 "asc3_the_impossible_machine":"ascension","asc4_singularity":"ascension",
 "asc5_the_draconic_heart":"ascension","asc6_bosses_rise":"ascension","asc7_ascension":"ascension",
 "journey_to_ascension":"journey","minecolonies":"annex",
}

# ---- parse chapters ----
# Each quest block: { id: "..." ... dependencies: [...] ... }
id_re = re.compile(r'^\s+id:\s*"([0-9A-Fa-f]+)"')
qid_to_file = {}          # quest id -> chapter basename
dup_ids = collections.defaultdict(list)
deps = {}                 # quest id -> list of dep ids
all_qids = set()

def read_bytes(p):
    with open(p, 'rb') as f:
        return f.read()

for fn in sorted(os.listdir(CHAP)):
    if not fn.endswith(".snbt"): continue
    base = fn[:-5]
    raw = read_bytes(os.path.join(CHAP, fn))
    text = raw.decode('utf-8', errors='replace')
    lines = text.splitlines()
    # We need per-quest parsing. Quests are objects in quests: [ {...}, {...} ].
    # Strategy: track brace depth; a quest starts at depth entering the quests array.
    # Simpler robust approach: split into quest objects by scanning for lines with `id: "..."`
    # then capture the surrounding dependencies. Use a stack-based object splitter.
    # We'll walk tokens by brace depth to isolate top-level quest objects inside `quests:`.
    # Find index of `quests: [`
    # Fallback simpler: regex each quest object.
    # Robust brace scan:
    depth = 0
    in_quests = False
    cur = []
    quest_objs = []
    quests_depth = None
    i = 0
    for line in lines:
        stripped = line.strip()
        # detect entry into quests array
        if not in_quests and re.match(r'quests:\s*\[', stripped):
            in_quests = True
            quests_depth = 0
            continue
        if in_quests:
            # count braces to segment objects at array level
            for ch in line:
                if ch == '{':
                    if quests_depth == 0:
                        cur = []
                    quests_depth += 1
                elif ch == '}':
                    quests_depth -= 1
                    if quests_depth == 0:
                        quest_objs.append("\n".join(cur))
                        cur = []
            if quests_depth >= 1:
                cur.append(line)
            # detect end of quests array: a `]` at array level (quests_depth 0) after we've seen objects
            if quests_depth == 0 and stripped.startswith(']'):
                in_quests = False
    for obj in quest_objs:
        m = id_re.search(obj) or re.search(r'id:\s*"([0-9A-Fa-f]+)"', obj)
        if not m:
            continue
        qid = m.group(1)
        if qid in qid_to_file:
            dup_ids[qid].append(base)
            if qid_to_file[qid] not in dup_ids[qid]:
                dup_ids[qid].insert(0, qid_to_file[qid])
        else:
            qid_to_file[qid] = base
        all_qids.add(qid)
        # dependencies
        dm = re.search(r'dependencies:\s*\[(.*?)\]', obj, re.DOTALL)
        dlist = []
        if dm:
            dlist = re.findall(r'"([0-9A-Fa-f]+)"', dm.group(1))
        deps[qid] = dlist

print("TOTAL quest ids parsed:", len(all_qids))
print("DUP ids:", dict(dup_ids))

# ---- lang parse ----
langraw = read_bytes(LANG)
langtext = langraw.decode('utf-8', errors='replace')

# em dash / en dash counts + which quest keys contain them
emdash = langtext.count('—')
endash = langtext.count('–')
print("EM DASH (U+2014) count:", emdash)
print("EN DASH (U+2013) count:", endash)

# map lines to quest id for dash-containing lines
key_re = re.compile(r'quest\.([0-9A-Fa-f]+)\.(title|quest_subtitle|quest_desc)')
em_quests = collections.Counter()
en_quests = collections.Counter()
for line in langtext.splitlines():
    km = key_re.search(line)
    qid = km.group(1) if km else None
    if '—' in line and qid:
        em_quests[qid] += line.count('—')
    if '–' in line and qid:
        en_quests[qid] += line.count('–')

print("EM DASH distinct quest ids:", len(em_quests))
print("EN DASH distinct quest ids:", len(en_quests))

# ---- which quest ids have quest_desc key present in lang ----
desc_present = set(re.findall(r'quest\.([0-9A-Fa-f]+)\.quest_desc', langtext))
missing_desc = sorted([q for q in all_qids if q not in desc_present], key=lambda q: (qid_to_file.get(q,''), q))
print("MISSING quest_desc count:", len(missing_desc))

# ---- non-array quest_desc values (single-string form) ----
# array form: quest.<id>.quest_desc: [ ... ]  (may be multiline)
# single form: quest.<id>.quest_desc: "..."
nonarray = []
for m in re.finditer(r'quest\.([0-9A-Fa-f]+)\.quest_desc:\s*(\S)', langtext):
    qid = m.group(1); firstchar = m.group(2)
    if firstchar == '"':
        nonarray.append(qid)
print("NON-ARRAY quest_desc count:", len(nonarray))

# ---- dependency graph analysis ----
# dangling deps
dangling = {}
for qid, dl in deps.items():
    for d in dl:
        if d not in all_qids:
            dangling.setdefault(qid, []).append(d)

# reverse deps
rev = collections.defaultdict(set)
for qid, dl in deps.items():
    for d in dl:
        rev[d].add(qid)

# orphans: no deps AND nothing depends on it
orphans = []
for qid in all_qids:
    has_dep = len(deps.get(qid, [])) > 0
    depended = len(rev.get(qid, set())) > 0
    if not has_dep and not depended:
        orphans.append(qid)

# backward-age deps: a quest depends on a target in a LATER age
backward = []
for qid, dl in deps.items():
    fa = FILE_AGE.get(qid_to_file.get(qid,''), None)
    if fa is None: continue
    fai = AGE_IDX.get(fa, None)
    for d in dl:
        if d not in all_qids: continue
        ta = FILE_AGE.get(qid_to_file.get(d,''), None)
        if ta is None: continue
        tai = AGE_IDX.get(ta, None)
        # skip journey/annex meta comparisons
        if fa in ("journey","annex") or ta in ("journey","annex"): continue
        if tai is not None and fai is not None and tai > fai:
            backward.append((qid, qid_to_file[qid], fa, d, qid_to_file[d], ta))

print("DANGLING dep sources:", len(dangling), "total dangling edges:", sum(len(v) for v in dangling.values()))
print("ORPHANS:", len(orphans))
print("BACKWARD-age deps:", len(backward))

# dump results to json for report building
out = {
 "total_qids": len(all_qids),
 "dup_ids": {k:v for k,v in dup_ids.items()},
 "emdash_count": emdash, "endash_count": endash,
 "em_quests": {k:v for k,v in em_quests.most_common()},
 "en_quests": {k:v for k,v in en_quests.most_common()},
 "missing_desc": [(q, qid_to_file.get(q,'?')) for q in missing_desc],
 "nonarray_desc": [(q, qid_to_file.get(q,'?')) for q in nonarray],
 "dangling": {k:v for k,v in dangling.items()},
 "dangling_files": {k:qid_to_file.get(k,'?') for k in dangling},
 "orphans": sorted([(q, qid_to_file.get(q,'?')) for q in orphans], key=lambda x:x[1]),
 "backward": backward,
}
with open(os.path.join(os.path.dirname(__file__), "ef_audit_data.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
print("wrote ef_audit_data.json")
