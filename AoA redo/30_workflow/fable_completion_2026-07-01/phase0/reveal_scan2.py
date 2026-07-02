#!/usr/bin/env python3
# Part 2: item->stage map, icon leaks, gateway wiring. AUDIT ONLY.
import os, re, glob

ROOT = r"C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)"
CH = os.path.join(ROOT,"config","ftbquests","quests","chapters")
KJS = os.path.join(ROOT,"kubejs","server_scripts")

GROUP_AGE = {
 "12B6640DF4C0DCFE":"dark_ages","508B59840C508057":"medieval_times",
 "0B038EB15EBBFD95":"the_renaissance","3F77A31B7D30C0AA":"industrial_revolution",
 "5E42E6B4A7C91D30":"gilded_age","7D28E4AEBC440F10":"atomic",
 "080F7BA9FFB8FC07":"otherworldly","6A196D2B21EDE4C0":"ascension",
 "5350010000000000":"journey","1A7F0E9D4C22B6F1":"annex"}
AGE_ORDER=["dark_ages","medieval_times","the_renaissance","industrial_revolution",
           "gilded_age","atomic","otherworldly","ascension"]
def rank(a): return AGE_ORDER.index(a) if a in AGE_ORDER else 99

def read(f):
    with open(f,'rb') as fh: return fh.read().decode('utf-8',errors='replace')

# ---- Build item -> effective (max) stage from all 01* restriction files ----
item_stage={}
tag_stage={}
pat=re.compile(r'\[\s*"([a-z_]+)"\s*,\s*"([^"]+)"\s*(?:,\s*"([^"]*)")?\s*\]')
for f in glob.glob(os.path.join(KJS,"aoa_astages_01*.js")):
    txt=read(f)
    for m in pat.finditer(txt):
        stage,item,kind=m.group(1),m.group(2),m.group(3)
        if stage not in AGE_ORDER and not stage.startswith(('ren_','ir_','g_','at_','ow_','asc_')):
            # only care about the 8 public ages for icon-leak comparison
            pass
        # map ren_* etc to their base age for comparison
        base=stage
        if stage.startswith('ren_'): base='the_renaissance'
        elif stage.startswith('ir_'): base='industrial_revolution'
        elif stage.startswith('g_'): base='gilded_age'
        elif stage.startswith('at_'): base='atomic'
        elif stage.startswith('ow_'): base='otherworldly'
        elif stage.startswith('asc_'): base='ascension'
        if base not in AGE_ORDER: continue
        tgt = tag_stage if (item.startswith('#') or kind=='tag') else item_stage
        key=item.lstrip('#')
        if key not in tgt or rank(base)>rank(tgt[key]):
            tgt[key]=base

print(f"[map] items with stage locks: {len(item_stage)}; tag locks: {len(tag_stage)}")

def item_age(item):
    it=item.lstrip('#')
    if it in item_stage: return item_stage[it]
    # namespace-heuristic fallbacks for clearly-late mods not itemized
    return None

# ---- Parse chapters (reuse minimal) ----
def split_quests(txt):
    i=txt.find('quests: [')
    if i<0: return []
    i=txt.find('[',i); depth=0;j=i
    while j<len(txt):
        c=txt[j]
        if c=='[':depth+=1
        elif c==']':
            depth-=1
            if depth==0:break
        j+=1
    body=txt[i+1:j]; quests=[];k=0;d=0;start=None
    while k<len(body):
        c=body[k]
        if c=='{':
            if d==0:start=k
            d+=1
        elif c=='}':
            d-=1
            if d==0 and start is not None:
                quests.append(body[start:k+1]);start=None
        k+=1
    return quests

def qf(q):
    d={}
    m=re.search(r'\bid:\s*"([0-9A-Fa-f]+)"',q);d['id']=m.group(1) if m else None
    dp=re.search(r'dependencies:\s*\[([^\]]*)\]',q,re.S)
    d['deps']=re.findall(r'"([0-9A-Fa-f]+)"',dp.group(1)) if dp else []
    ic=re.search(r'icon:\s*{[^}]*id:\s*"([^"]+)"',q,re.S) or re.search(r'\bicon:\s*"([^"]+)"',q)
    d['icon']=ic.group(1) if ic else None
    ti=re.search(r'tasks:\s*\[.*?item:\s*{[^}]*id:\s*"([^"]+)"',q,re.S) or re.search(r'tasks:\s*\[.*?\bitem:\s*"([^"]+)"',q,re.S)
    d['task_item']=ti.group(1) if ti else None
    return d

chapters=[]
qid2age={}   # quest id -> its chapter age
qid2ch={}
for f in sorted(glob.glob(os.path.join(CH,'*.snbt'))):
    txt=read(f)
    g=re.search(r'group:\s*"([0-9A-Fa-f]+)"',txt)
    grp=g.group(1) if g else None
    age=GROUP_AGE.get(grp,'UNKNOWN')
    head=txt.split('quests: [',1)[0]
    ic=re.search(r'icon:\s*{[^}]*id:\s*"([^"]+)"',head,re.S) or re.search(r'icon:\s*"([^"]+)"',head)
    ch={'file':os.path.basename(f),'group':grp,'age':age,'icon':ic.group(1) if ic else None,
        'quests':[qf(q) for q in split_quests(txt)]}
    chapters.append(ch)
    for q in ch['quests']:
        if q['id']: qid2age[q['id']]=age; qid2ch[q['id']]=ch['file']

# ---- 3. ICON LEAKS ----
print("\n"+"="*70)
print("3. ICON LEAKS (icon item locked at a LATER age than its chapter)")
print("="*70)
icon_leaks=[]
# chapter-tab icons
for ch in chapters:
    if ch['age'] not in AGE_ORDER: continue
    ci=ch['icon']
    if ci:
        ia=item_age(ci)
        if ia and rank(ia)>rank(ch['age']):
            icon_leaks.append(('CHAPTER-TAB',ch['file'],ch['age'],'(tab icon)',ci,ia))
# quest icons/task-items
for ch in chapters:
    if ch['age'] not in AGE_ORDER: continue
    for q in ch['quests']:
        icon = q['icon'] or q['task_item']
        if not icon: continue
        ia=item_age(icon)
        if ia and rank(ia)>rank(ch['age']):
            icon_leaks.append(('QUEST',ch['file'],ch['age'],q['id'],icon,ia))

for kind,f,age,qid,icon,ia in icon_leaks:
    print(f"  {kind} [{age} chapter] {f} q={qid} icon={icon} locked_at={ia}")
print(f"\nICON LEAKS: {len(icon_leaks)}")

# ---- 2. GATEWAY WIRING ----
print("\n"+"="*70)
print("2. GATEWAY WIRING (first-age quests' cross-age deps)")
print("="*70)
# For each age, find quests whose deps point to a PRIOR age (cross-age entry edges).
for age in AGE_ORDER:
    print(f"\n[{age}]")
    entries=[]
    for ch in chapters:
        if ch['age']!=age: continue
        for q in ch['quests']:
            prior_deps=[d for d in q['deps'] if d in qid2age and rank(qid2age[d])<rank(age)]
            if prior_deps:
                for d in prior_deps:
                    entries.append((ch['file'],q['id'],d,qid2age[d],qid2ch.get(d)))
    if not entries:
        # any rootless in this age? (leak) else fully internal
        roots=[(ch['file'],q['id']) for ch in chapters if ch['age']==age for q in ch['quests'] if not q['deps']]
        if roots:
            print(f"    ROOTLESS ENTRY (no gate): {roots}")
        else:
            print(f"    (no cross-age entry edge found; age revealed only via internal chain or unreachable-at-entry)")
    for f,q,d,da,dch in entries:
        print(f"    gate q={q} ({f}) <- dep {d} [{da}] in {dch}")
