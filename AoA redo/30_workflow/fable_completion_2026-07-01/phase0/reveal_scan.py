#!/usr/bin/env python3
# Reveal-discipline audit for AoA. AUDIT ONLY. Reads chapters + lang + astages.
import os, re, glob, json, sys

ROOT = r"C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)"
CH = os.path.join(ROOT, "config", "ftbquests", "quests", "chapters")

GROUP_AGE = {
 "12B6640DF4C0DCFE":"dark_ages","508B59840C508057":"medieval_times",
 "0B038EB15EBBFD95":"the_renaissance","3F77A31B7D30C0AA":"industrial_revolution",
 "5E42E6B4A7C91D30":"gilded_age","7D28E4AEBC440F10":"atomic",
 "080F7BA9FFB8FC07":"otherworldly","6A196D2B21EDE4C0":"ascension",
 "5350010000000000":"journey","1A7F0E9D4C22B6F1":"annex",
}
AGE_ORDER = ["dark_ages","medieval_times","the_renaissance","industrial_revolution",
             "gilded_age","atomic","otherworldly","ascension"]

def age_rank(a):
    return AGE_ORDER.index(a) if a in AGE_ORDER else -1

# --- crude SNBT quest splitter. Chapters are one big object with quests:[ ... ].
def read(f):
    with open(f,'rb') as fh: return fh.read().decode('utf-8',errors='replace')

def chapter_meta(txt):
    m = {}
    g = re.search(r'group:\s*"([0-9A-Fa-f]+)"', txt); m['group']=g.group(1) if g else None
    fn = re.search(r'filename:\s*"([^"]+)"', txt); m['filename']=fn.group(1) if fn else None
    cid = re.search(r'\n\tid:\s*"([0-9A-Fa-f]+)"', txt) or re.search(r'^\tid:\s*"([0-9A-Fa-f]+)"',txt,re.M)
    m['chapter_id']=cid.group(1) if cid else None
    # chapter-level icon: first icon: block before quests: [
    head = txt.split('quests: [',1)[0]
    ic = re.search(r'icon:\s*{[^}]*id:\s*"([^"]+)"', head, re.S) or re.search(r'icon:\s*"([^"]+)"', head)
    m['chapter_icon']=ic.group(1) if ic else None
    m['hide_quest_until_deps_complete'] = 'hide_quest_until_deps_complete: true' in head
    m['always_invisible'] = 'always_invisible: true' in head
    return m

def split_quests(txt):
    # find quests: [ ... ] top-level array; brace-match quest objects
    i = txt.find('quests: [')
    if i<0: return []
    i = txt.find('[', i)
    # walk to matching close
    depth=0; j=i
    while j < len(txt):
        c=txt[j]
        if c=='[': depth+=1
        elif c==']':
            depth-=1
            if depth==0: break
        j+=1
    body = txt[i+1:j]
    quests=[]
    # brace-match objects at depth 1
    k=0; d=0; start=None
    while k < len(body):
        c=body[k]
        if c=='{':
            if d==0: start=k
            d+=1
        elif c=='}':
            d-=1
            if d==0 and start is not None:
                quests.append(body[start:k+1]); start=None
        k+=1
    return quests

def quest_fields(q):
    d={}
    m=re.search(r'\bid:\s*"([0-9A-Fa-f]+)"',q); d['id']=m.group(1) if m else None
    deps=re.search(r'dependencies:\s*\[([^\]]*)\]',q,re.S)
    if deps:
        d['deps']=re.findall(r'"([0-9A-Fa-f]+)"',deps.group(1))
    else:
        d['deps']=[]
    d['has_dep_key']= 'dependencies:' in q
    # icon override
    ic=re.search(r'icon:\s*{[^}]*id:\s*"([^"]+)"',q,re.S) or re.search(r'\bicon:\s*"([^"]+)"',q)
    d['icon']=ic.group(1) if ic else None
    # first task item = de-facto icon if no override
    ti=re.search(r'tasks:\s*\[.*?item:\s*{[^}]*id:\s*"([^"]+)"',q,re.S) or re.search(r'tasks:\s*\[.*?\bitem:\s*"([^"]+)"',q,re.S)
    d['task_item']=ti.group(1) if ti else None
    d['hide_until_deps_complete']= 'hide_until_deps_complete: true' in q
    d['optional']= 'optional: true' in q
    return d

chapters=[]
for f in sorted(glob.glob(os.path.join(CH,'*.snbt'))):
    txt=read(f)
    meta=chapter_meta(txt)
    meta['file']=os.path.basename(f)
    meta['age']=GROUP_AGE.get(meta['group'],'UNKNOWN')
    qs=[quest_fields(q) for q in split_quests(txt)]
    meta['quests']=qs
    chapters.append(meta)

# ---- 1. ROOTLESS LEAK SCAN ----
print("="*70)
print("1. ROOTLESS (zero-dependency = always visible) quests per chapter")
print("="*70)
rootless_by_age={}
for ch in chapters:
    rootless=[q for q in ch['quests'] if not q['deps']]
    if rootless:
        rootless_by_age.setdefault(ch['age'],[])
        print(f"\n[{ch['age']}] {ch['file']}  (group {ch['group']}, {len(ch['quests'])} quests, {len(rootless)} rootless)")
        for q in rootless:
            item = q['task_item'] or q['icon'] or '(no item)'
            print(f"    rootless id={q['id']}  item={item}")
            rootless_by_age[ch['age']].append((ch['file'],q['id'],item))

# Chapters that become visible at world entry (>=1 rootless quest)
print("\n--- Chapters VISIBLE at world entry (have >=1 rootless quest) ---")
for ch in chapters:
    if any(not q['deps'] for q in ch['quests']):
        print(f"    VISIBLE-TAB [{ch['age']}] {ch['file']}")

print("\nRootless count by age:")
for a in AGE_ORDER+['journey','annex','UNKNOWN']:
    if a in rootless_by_age:
        print(f"    {a}: {len(rootless_by_age[a])} rootless quests")

# ---- summary counts ----
print("\n"+"="*70)
print("TOTALS")
print("="*70)
tot_q=sum(len(c['quests']) for c in chapters)
tot_root=sum(1 for c in chapters for q in c['quests'] if not q['deps'])
print(f"chapters={len(chapters)} quests={tot_q} rootless={tot_root}")
