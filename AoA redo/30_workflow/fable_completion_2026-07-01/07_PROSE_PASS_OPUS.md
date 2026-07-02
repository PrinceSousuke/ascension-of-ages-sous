# 07 — PROSE PASS (Opus authors all language)

**Owner:** Opus. **Prepend:** `01_MASTER_PREAMBLE.md` (for voice §8 + the prose/structure
split §5). **Depends on:** Fable's structure passes (03/04/05) merged, so the stub lang keys
+ teaching briefs exist.
**You touch ONLY `config/ftbquests/quests/lang/en_us.snbt`.** Never edit a `.snbt` chapter,
never change an id, never change structure. If a brief is wrong or impossible, flag it in
the ledger — do not "fix" it in prose.

---

## Input
Fable left, for every new node, three keys with machine-readable placeholders:
```
quest.<id>.title: "[STUB] ..."
quest.<id>.quest_subtitle: "[STUB] ..."
quest.<id>.quest_desc: ["[BRIEF] teaches: <mechanic>; requires <item(s)> (gated <age>); prior node = <x>; edge case: <y>. Opus: ..."]
```
Your job: replace every `[STUB]`/`[BRIEF]` value with real, in-voice prose that teaches the
briefed mechanic.

## Voice (hard rules — canon)
- Instruction-first: tell the player what to build/do, then why it matters mechanically.
- 2–4 short paragraphs for `quest_desc`. Short declarative sentences.
- **No em dashes anywhere.** No AI-isms. No "the X is the lesson" aphorisms. No filler.
- Title: the machine/goal name (usually the task item). Subtitle: one punchy line.
- Match the live house voice — read real descriptions in `at4_machine_soul` /
  `ir_create_industrial_addons` before starting; mirror their register.
- `quest_desc` MUST be the **array-of-strings** form: `quest_desc: ["line one", "line two"]`.
  Do not emit the bare-string form.
- Preserve FTBQ formatting codes (`&b`, `&r`, etc.) already present in the file's style; use
  them the way existing entries do, sparingly.

## Also fix these prose defects (from the ledger)
1. **87 em-dash lines** in `en_us.snbt` — rewrite each to remove the em dash while keeping
   meaning + voice (do not just swap for a hyphen; restructure the sentence). Codex will give
   you the exact id list from the ledger.
2. **4 missing `g6` descriptions** — write real prose for:
   `051AB096CA0848B4` "Alloy From the Reef", `A818144300D946A8` "Conduit Cage",
   `7C0AC10000000001` "Forge the Rod", `7C0AC10000000002` "Awaken and Channel". (These are
   Aquatic Ambitions / conduit nodes — coordinate with prompt 03.9 for the mechanic.)
3. Any remaining `[STUB]` from an earlier partial pass.

## Method
- Work chapter by chapter so voice stays consistent within a chapter's arc.
- After each chapter, spot-check render assumptions: the desc should read correctly in order
  with its prerequisites (don't reference a mechanic the player hasn't unlocked yet — the
  brief tells you the prior node).
- Do NOT invent mechanics. If the brief says the item does X, teach X. If you think the brief
  is wrong, flag it; Fable/CC owns the mechanic truth.

## Deliverables
- Fully-authored `en_us.snbt` entries for every new node (zero `[STUB]`/`[BRIEF]` remaining —
  `grep -c '\[STUB\]\|\[BRIEF\]' en_us.snbt` must return 0).
- Zero em dashes (`grep -c '—' en_us.snbt` must return 0).
- A one-line note in `LEDGER.md`: nodes prosed + em-dashes cleared + g6 filled.
