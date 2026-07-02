# Transitive-closure tracer for FTBQ age-grant fan-in verification.
# AUDIT ONLY. Reads chapters/*.snbt. Given a target quest id, computes the full
# transitive dependency closure (all ancestors) and reports whether a set of
# "must-be-required" quest ids (by entity kill or by id) are inside it.
import os, re, sys, collections

ROOT = r"C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)\config\ftbquests\quests\chapters"

id_re = re.compile(r'^\s+id:\s*"([0-9A-Fa-f]+)"')

def parse():
    deps = {}            # qid -> [dep ids]
    minreq = {}          # qid -> int or None
    optional = {}        # qid -> bool
    entities = collections.defaultdict(list)  # qid -> [entity ids killed]
    qfile = {}
    for fn in sorted(os.listdir(ROOT)):
        if not fn.endswith(".snbt"): continue
        base = fn[:-5]
        raw = open(os.path.join(ROOT, fn), "rb").read().decode("utf-8","replace")
        text = raw.replace("\r\n","\n").replace("\r","\n")
        qstart = text.find("quests: [")
        if qstart < 0: continue
        body = text[qstart:]
        depth=0; in_array=False; obj_start=None; i=0; n=len(body)
        objs=[]
        while i<n:
            c=body[i]
            if c=='"':
                i+=1
                while i<n and body[i]!='"':
                    if body[i]=="\\": i+=1
                    i+=1
            elif c=="[":
                if not in_array: in_array=True
            elif c=="{":
                if in_array and depth==0: obj_start=i; depth=1
                elif depth>0: depth+=1
            elif c=="}":
                if depth>0:
                    depth-=1
                    if depth==0 and obj_start is not None:
                        objs.append(body[obj_start:i+1]); obj_start=None
            elif c=="]":
                if in_array and depth==0: break
            i+=1
        for obj in objs:
            m=re.search(r'\bid:\s*"([0-9A-Fa-f]{16})"',obj)
            if not m: continue
            qid=m.group(1)
            qfile[qid]=base
            dm=re.search(r'dependencies:\s*\[(.*?)\]',obj,re.DOTALL)
            dlist=re.findall(r'"([0-9A-Fa-f]+)"',dm.group(1)) if dm else []
            deps[qid]=dlist
            mr=re.search(r'min_required_dependencies:\s*(\d+)',obj)
            minreq[qid]=int(mr.group(1)) if mr else None
            optional[qid]= 'optional: true' in obj
            for em in re.finditer(r'entity:\s*"([a-z0-9_.:]+)"',obj):
                entities[qid].append(em.group(1))
    return deps,minreq,optional,entities,qfile

def closure(target, deps):
    # all transitive ancestors of target (nodes target depends on, recursively)
    seen=set(); stack=[target]
    while stack:
        q=stack.pop()
        for d in deps.get(q,[]):
            if d not in seen:
                seen.add(d); stack.append(d)
    return seen

if __name__=="__main__":
    deps,minreq,optional,entities,qfile=parse()
    # entity -> set of quest ids that kill it
    ent_to_q=collections.defaultdict(set)
    for q,elist in entities.items():
        for e in elist: ent_to_q[e].add(q)

    targets = {
        "medieval->ren grant (what_waits 1328 node)": None,  # resolve by finding node w/ that grant
    }
    # We pass targets on CLI: python trace_closure.py <target_qid> ent1 ent2 ...
    if len(sys.argv)>=2:
        tgt=sys.argv[1]
        want_entities=sys.argv[2:]
        clo=closure(tgt,deps)
        print("TARGET",tgt,"in file",qfile.get(tgt,"?"))
        print("closure size:",len(clo))
        for e in want_entities:
            qs=ent_to_q.get(e,set())
            inclo=[q for q in qs if q in clo]
            # also check the kill node itself isn't optional (optional node can still gate via deps if something requires it, but for "required" we want a non-optional path)
            status = "REQUIRED" if inclo else ("PRESENT-NOT-IN-CLOSURE" if qs else "ABSENT")
            details=[]
            for q in qs:
                details.append("%s(%s,opt=%s,inclosure=%s)"%(q,qfile.get(q),optional.get(q),q in clo))
            print("  %-45s %s  %s"%(e,status,"; ".join(details)))
