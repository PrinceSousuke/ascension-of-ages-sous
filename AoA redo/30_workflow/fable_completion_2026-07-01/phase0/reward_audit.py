#!/usr/bin/env python3
"""Phase 0 reward audit: age-leak + trivialization scan for AoA quest rewards.
AUDIT ONLY. Writes report + this script under phase0/. No edits elsewhere, no git.
"""
import re, glob, os, json
from collections import defaultdict

ROOT = r"C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)"
CH_DIR = os.path.join(ROOT, "config/ftbquests/quests/chapters")
RT_DIR = os.path.join(ROOT, "config/ftbquests/quests/reward_tables")
KJS = os.path.join(ROOT, "kubejs/server_scripts")

AGES = ["dark_ages","medieval_times","the_renaissance","industrial_revolution",
        "gilded_age","atomic","otherworldly","ascension"]
AGE_IDX = {a:i for i,a in enumerate(AGES)}

# chapter file -> age (from SHARED_CONTEXT verified map)
CH_AGE = {}
def _add(age, files):
    for f in files.split(): CH_AGE[f] = age
_add("dark_ages","stone_food_and_farming_pressures stone_water_weather_and_wounds entering_the_iron_era")
_add("medieval_times","m1_first_mill m3_relics_and_burrows metallurgy what_waits_in_the_grove")
_add("the_renaissance","ren_aether_literacy ren_archive_recordkeeping ren_deeper_darker_otherside ren_end_threshold ren_magic_foundations ren_maledictus_vigil ren_nether_threshold ren_observation_experimentation ren_second_mill_steam_rail_logistics ren_starlight_observation ren_undergarden_descent")
_add("industrial_revolution","ir_automation_safety_and_routing ir_create_industrial_addons ir_immersive_engineering_early_factory ir_ir_side_gear_hidden_equipment ir_magic_feedstock_and_spectrum_network ir_modern_industrialization_steam_industry ir_netherite_citadel_obsidilith ir_pneumaticcraft_pressure_plastic ir_power_motion_and_grid")
_add("gilded_age","g1_the_golden_workshop g2_the_refinery g4_the_infinite_grid g5_empire_of_iron g6_circuits_and_current g7_chartered_arcana g_power_beyond_wires")
_add("atomic","at1_nuclear_dawn at2_the_periodic_table at3_chain_reaction at4_machine_soul at5_threshold_of_war at7_chaos_convergence atomic_oritech_convergence")
_add("otherworldly","ow1_launch_window ow2_strange_dimension_operations ow3_dragon_technology ow4_the_dyson_project ow5_the_digital_cosmos ow6_beyond_the_veil")
_add("ascension","asc1_the_table_of_infinities asc2_the_philosophers_dream asc3_the_impossible_machine asc4_singularity asc5_the_draconic_heart asc6_bosses_rise asc7_ascension")
# journey + annexes: meta / age-agnostic -> treat as no age constraint
CH_AGE["journey_to_ascension"] = None
CH_AGE["minecolonies"] = None

def read(p): return open(p, encoding="utf-8", errors="replace").read()

# ---------------------------------------------------------------------------
# 1. Build item/tag -> effective (max) stage from AStages scripts
# ---------------------------------------------------------------------------
item_stage = {}   # id -> highest age idx
tag_stage = {}

def note(mapping, ident, stage):
    if stage not in AGE_IDX: return
    i = AGE_IDX[stage]
    if ident not in mapping or i > mapping[ident]:
        mapping[ident] = i

astages_files = glob.glob(os.path.join(KJS, "aoa_astages_*.js"))
# pattern A: array literal  ["stage", "namespace:id", ...]
arr_re = re.compile(r'\[\s*"([a-z_]+)"\s*,\s*"([^"]+)"')
# pattern B: softItemLock('stage', 'id'  / addOreRestriction('stage', 'ore'
call_re = re.compile(r"(?:softItemLock|addOreRestriction|softTagLock)\(\s*'([a-z_]+)'\s*,\s*'([^']+)'")
callq_re = re.compile(r'(?:softItemLock|addOreRestriction|softTagLock)\(\s*"([a-z_]+)"\s*,\s*"([^"]+)"')

for f in astages_files:
    txt = read(f)
    for st, ident in arr_re.findall(txt):
        if st not in AGE_IDX: continue
        if ident.startswith("#") or ident.startswith("c:") or ident.startswith("minecraft:") and "/" in ident:
            note(tag_stage, ident.lstrip("#"), st)
        elif ":" in ident:
            note(item_stage, ident, st)
    for st, ident in list(call_re.findall(txt)) + list(callq_re.findall(txt)):
        if st not in AGE_IDX: continue
        if ident.startswith("#") or ident.startswith("c:"):
            note(tag_stage, ident.lstrip("#"), st)
        elif ":" in ident:
            note(item_stage, ident, st)

# material family -> stage (addAdvancedMaterialTags / addSourceMaterialTags calls)
mat_re = re.compile(r"add(?:Advanced|Source)MaterialTags\(\s*'([a-z_]+)'\s*,\s*'([a-z_]+)'")
mat_stage = {}
for f in astages_files:
    for st, mat in mat_re.findall(read(f)):
        if st in AGE_IDX:
            i = AGE_IDX[st]
            if mat not in mat_stage or i > mat_stage[mat]:
                mat_stage[mat] = i
# Also capture the loop form: materialsForStage arrays. Grab any list of materials tied to a stage var is hard; skip - explicit calls dominate.

def item_effective_stage(item_id):
    """Return (age_idx or None, source). Most-restrictive-wins across item + tag + material heuristics."""
    best = None; src = None
    if item_id in item_stage:
        best = item_stage[item_id]; src = "item-lock"
    # material family heuristic: ingot/dust/raw/nugget/plate of a gated material
    # derive material token from id suffix (best-effort, judgment)
    return best, src

# ---------------------------------------------------------------------------
# 2. Parse reward tables
# ---------------------------------------------------------------------------
def hex_id_of_table(txt):
    m = re.search(r'^\s*id:\s*"([0-9A-Fa-f]{16})"', txt, re.M)
    return m.group(1).upper() if m else None

item_in_block_re = re.compile(r'item:\s*\{[^{}]*?id:\s*"([^"]+)"', re.S)
# reward table entries: each has item + optional count + weight
tables = {}  # hexid -> {file, entries:[(item,count,weight)], loot_size}
for f in glob.glob(os.path.join(RT_DIR, "*.snbt")):
    txt = read(f)
    hid = hex_id_of_table(txt)
    name = os.path.basename(f)[:-5]
    ls = re.search(r'loot_size:\s*(\d+)', txt)
    entries = []
    # split reward objects
    for m in re.finditer(r'\{[^{}]*?item:\s*\{[^{}]*?id:\s*"([^"]+)"[^{}]*?\}[^{}]*?\}', txt, re.S):
        blk = m.group(0)
        iid = m.group(1)
        cnt = re.search(r'\n\s*count:\s*(\d+)', blk)
        # the item.count vs entry.count: entry-level count is the reward stack size
        wt = re.search(r'weight:\s*([\d.]+)', blk)
        # entry count (outside item{}) — take first count that's not the inner one
        entries.append((iid, int(cnt.group(1)) if cnt else 1, float(wt.group(1)) if wt else 1.0))
    tables[hid] = dict(file=name, entries=entries, loot_size=int(ls.group(1)) if ls else 1, hexid=hid)

# ---------------------------------------------------------------------------
# 3. Parse chapters: rewards per quest, table refs
# ---------------------------------------------------------------------------
# Extract each quest object's reward array items and any table_id references.
def split_quests(txt):
    """Yield (quest_id, quest_text) crude split on top-level quest objects via id: markers within quests array."""
    # simpler: find each 'rewards: [' ... and attribute to nearest preceding quest id
    return txt

table_refs = defaultdict(set)   # hexid -> set(chapter files referencing)
table_ref_age = {}              # hexid -> lowest age idx referencing
chapter_rewards = defaultdict(list)  # chapter -> list of (quest_id, kind, item/table, count)
xp_by_age = defaultdict(int)
reward_count_by_age = defaultdict(int)

qid_re = re.compile(r'\n\t+id:\s*"([0-9A-Fa-f]{16})"')

for f in glob.glob(os.path.join(CH_DIR, "*.snbt")):
    name = os.path.basename(f)[:-5]
    age = CH_AGE.get(name, "UNKNOWN")
    txt = read(f)
    # locate each quest block by 'rewards: [' ... find enclosing quest id (nearest preceding top-level id)
    # We'll walk quest objects: naive but effective — quests separated by lines with id at 3-tab depth
    # Instead, iterate reward arrays and grab the quest id preceding them.
    for rm in re.finditer(r'rewards:\s*\[(.*?)\n\t{3}\]', txt, re.S):
        block = rm.group(1)
        start = rm.start()
        # nearest preceding quest id
        pre = txt[:start]
        qids = qid_re.findall(pre)
        qid = qids[-1] if qids else "?"
        # each reward object
        for om in re.finditer(r'\{(.*?)\}', block, re.S):
            # careful: item{} nested — use type detection on the object; reparse robustly below
            pass
        # robust: find reward objects via 'type:' tokens
        for tm in re.finditer(r'type:\s*"(\w+)"', block):
            rtype = tm.group(1)
            # get surrounding object text
            s = block.rfind("{", 0, tm.start())
            e = block.find("}", tm.end())
            # for item rewards the object may contain nested item{}; expand end
            obj = block[s:e+1] if s>=0 and e>0 else block[max(0,tm.start()-200):tm.end()+200]
            if rtype == "item":
                mi = re.search(r'item:\s*\{[^{}]*?id:\s*"([^"]+)"', obj, re.S) or re.search(r'item:\s*\{.*?id:\s*"([^"]+)"', block[s:s+400], re.S)
                if mi:
                    iid = mi.group(1)
                    cm = re.search(r'\n\s*count:\s*(\d+)', obj)
                    cnt = int(cm.group(1)) if cm else 1
                    chapter_rewards[name].append((qid, "item", iid, cnt))
                    reward_count_by_age[age]+=1
            elif rtype == "xp" or rtype == "xp_levels":
                xm = re.search(r'xp:\s*(\d+)', block[s:e+40])
                if xm: xp_by_age[age]+=int(xm.group(1))
                reward_count_by_age[age]+=1
            elif rtype in ("loot","random","choice"):
                # find table_id in this object or nearby
                tid = re.search(r'table_id:\s*(\d+)L?', block[s:e+40])
                if tid:
                    hexid = format(int(tid.group(1)), "016X")
                    table_refs[hexid].add(name)
                    ai = AGE_IDX.get(age, 99)
                    if hexid not in table_ref_age or ai < table_ref_age[hexid]:
                        table_ref_age[hexid] = ai
                    chapter_rewards[name].append((qid, rtype, "table:"+hexid, 1))
                else:
                    chapter_rewards[name].append((qid, rtype, "table:UNLINKED", 1))
                reward_count_by_age[age]+=1
            elif rtype == "command":
                pass  # handled separately below (nested icon{} breaks per-object slicing)
    # command rewards: scan reward blocks directly (nested icon{} breaks object slicing)
    for rm in re.finditer(r'rewards:\s*\[(.*?)\n\t{3}\]', txt, re.S):
        block = rm.group(1)
        pre = txt[:rm.start()]
        qids = qid_re.findall(pre); qid = qids[-1] if qids else "?"
        for cm in re.finditer(r'command:\s*"([^"]+)"', block):
            chapter_rewards[name].append((qid, "command", cm.group(1), 1))

# ---------------------------------------------------------------------------
# 4. AGE-LEAK CHECK
# ---------------------------------------------------------------------------
leaks = []  # (source, reward_id, reward_stage_name, source_age, cls)
def add_leak(source, reward, rstage_idx, src_age_idx, cls):
    leaks.append((source, reward, AGES[rstage_idx], AGES[src_age_idx] if src_age_idx is not None and src_age_idx<len(AGES) else "?", cls))

# direct item rewards in chapters
for ch, rewards in chapter_rewards.items():
    src_age = CH_AGE.get(ch)
    if src_age is None: continue
    src_idx = AGE_IDX[src_age]
    for qid, kind, val, cnt in rewards:
        if kind == "item" and val in item_stage:
            rstage = item_stage[val]
            if rstage > src_idx:
                add_leak(f"{ch}/{qid}", f"{val} x{cnt}", rstage, src_idx, "direct-item")

# reward-table entries reachable from a lower age
for hexid, tbl in tables.items():
    refs = table_refs.get(hexid, set())
    if not refs: continue
    low_idx = min(AGE_IDX[CH_AGE[c]] for c in refs if CH_AGE.get(c) is not None) if any(CH_AGE.get(c) is not None for c in refs) else None
    if low_idx is None: continue
    for iid, cnt, wt in tbl["entries"]:
        if iid in item_stage and item_stage[iid] > low_idx:
            reflist = ",".join(sorted(refs))
            add_leak(f"table:{tbl['file']}({hexid}) <- {reflist}", f"{iid} x{cnt} (w{wt})", item_stage[iid], low_idx, "table-leak")

# ---------------------------------------------------------------------------
# 5. Output data dump for report authoring
# ---------------------------------------------------------------------------
out = {
 "n_item_locks": len(item_stage),
 "n_tag_locks": len(tag_stage),
 "n_tables": len(tables),
 "n_leaks": len(leaks),
 "reward_count_by_age": dict(reward_count_by_age),
 "xp_by_age": dict(xp_by_age),
}
print(json.dumps(out, indent=2))
print("\n=== LEAKS ===")
for L in sorted(leaks, key=lambda x: (x[2])):
    print(" | ".join(str(s) for s in L))

# table -> referencing ages summary
print("\n=== TABLE REFS (hexid | file | loot_size | #entries | referencing chapters | lowest age) ===")
for hexid, tbl in sorted(tables.items(), key=lambda kv: table_ref_age.get(kv[0],99)):
    refs = table_refs.get(hexid, set())
    if not refs:
        continue
    low = table_ref_age.get(hexid)
    print(f"{hexid} | {tbl['file']} | ls={tbl['loot_size']} | {len(tbl['entries'])} entries | {sorted(refs)} | {AGES[low] if low is not None and low<len(AGES) else '?'}")

# unreferenced tables
unref = [t['file'] for h,t in tables.items() if not table_refs.get(h)]
print("\n=== UNREFERENCED TABLES ===")
print(unref)

# command rewards (non-standard)
print("\n=== COMMAND REWARDS ===")
STD = ("astages add","advancement grant","aoa reward grant_team")
for ch, rewards in chapter_rewards.items():
    for qid,kind,val,cnt in rewards:
        if kind=="command":
            v=val.lower()
            if not any(s in v for s in STD):
                print(f"{ch}/{qid}: {val}")

# dump chapter_rewards + tables for trivialization analysis
with open(os.path.join(os.path.dirname(__file__),"_reward_dump.json"),"w",encoding="utf-8") as fh:
    json.dump({
      "chapter_rewards":{k:v for k,v in chapter_rewards.items()},
      "tables":{h:t for h,t in tables.items()},
      "table_refs":{h:sorted(list(s)) for h,s in table_refs.items()},
      "item_stage":item_stage,
    }, fh, indent=1)
print("\nDump written.")
