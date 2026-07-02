# 08 — DETERMINISTIC CLEANUP + FINAL VALIDATION GATE

**Owner:** Codex (deterministic transforms) + CC (final reasoning review). **Prepend:**
`01_MASTER_PREAMBLE.md`. **Runs:** the mechanical items can run anytime after the ledger;
the final validation gate runs LAST, after 03–07 are merged.

---

## Part A — Codex deterministic transforms (mechanical, no judgment)
1. **Non-array `quest_desc` normalization** — convert the 7 single-string `quest_desc` in
   `ow6_beyond_the_veil`'s lang entries to the array form. Byte-safe, CRLF preserved.
2. **`entering_the_iron_era.snbt` rename** — it's a Dark Ages chapter, misnamed as IR. Before
   renaming: grep the whole repo for the string `entering_the_iron_era` (the `.snbt` has a
   `filename:` field that must match, and there may be references in KubeJS/docs). Rename the
   file AND the `filename:` field AND every reference in one atomic change. If ANY reference
   is load-bearing in a way that's unclear, STOP and hand to CC. (Low severity — only do this
   if it's clean.)
3. **Em-dash id extraction** — produce the exact list of quest ids whose lang values contain
   `—`, hand to Opus (prompt 07.1). Do NOT auto-replace em dashes with hyphens (that needs
   prose judgment — Opus rewrites, you don't).
4. **`node --check` sweep** — run on every KubeJS file touched this pack; collect PASS/FAIL.
5. **Anchored duplicate-id scan** — `grep -rnP '^\s+id: "' config/ftbquests/quests/chapters/`
   → confirm zero real duplicate ids across all chapters (remember `autofocus_id:` is not a
   quest id).
6. **Duplicate-jar hygiene** — `mods/` currently loads BOTH `aoacore-0.4.5.jar` and
   `aoacore-0.4.6.jar` (stale + active). Confirm 0.4.6 is the intended one and remove 0.4.5
   (two copies of the same modid loading is a real defect). Re-scan `mods/` for any other
   duplicate modid while you're there.

## Part B — CC final validation gate (reasoning; this is the merge gate)
Nothing merges to the live pack until CC signs this off.
1. **Age-discipline re-audit** — re-run the tier audit (prompt 02.A) across ALL new + edited
   chapters (Create gaps, OW, Ascension). Zero SOFTLOCK rows allowed. Hand-verify any the
   script flags.
2. **Crossing check** — for every new/edited chapter, confirm dependency lines don't cross
   (hard constraint). Use the layout engine referenced in the layout-cleanup workflow, or
   compute segment intersections directly. Any crossing = bounce back to Fable.
3. **Capstone chain integrity** — walk the full grant chain end to end:
   `...→ atomic → otherworldly (ow6 Leviathan) → ascension (asc7 Guardian) → aoa_complete`.
   Confirm each boundary node carries the correct `/aoa reward grant_team` + `/advancement
   grant` + stage grant, and that no age is reachable without its capstone proof.
4. **Weave sanity** — confirm the post-buildout tier audit is clean (no weave re-opened a
   softlock), and every weave id resolves.
5. **Prose gate** — `grep -c '\[STUB\]\|\[BRIEF\]'` = 0 and `grep -c '—'` = 0 in `en_us.snbt`.
6. **Parse gate** — load the pack (or run the FTBQ SNBT parser) and confirm all chapters
   parse; confirm `SkillsLevel` blocks are intact (not stripped).
7. **Canon-call queue** — collect everything flagged for a human decision (Neo Vitae A1
   repoint, Hephaestus non-monotonic T4/T5, any re-gate proposed during weaving, any new
   chapter added) into a short "DECISIONS NEEDED" list at the top of `LEDGER.md` for Andrew.

## Part C — CANON DECISION QUEUE (Andrew decides; do NOT author blind)
These surfaced during the census/audit. Each needs a human call before or during authoring.
CC collects answers, then routes to the right per-age prompt.

**RESOLVED 2026-07-02 — GATING IS CLOSED.** Per `AOA_QUEST_SCOPE_REGISTRY.md` (canon §9): no
coverage-driven gating. The 139-ungated-mod sweep is VOID — do not gate ungated mods. Every
"needs a gate" question below is settled (answer: no gate). Only genuine questing/content
decisions remain. Also honor the registry's EXCLUDED list before authoring anything.

1. ~~Ungated content sweep~~ — **VOID** (no gating; registry Policy 1).
2. ~~apotheosis gate~~ — no gate. Open question is only: capstone-only (current) or a teaching
   questline? (content decision, low priority).
3. ~~apothic_enchanting gate~~ — no gate. Author a small optional line only if desired.
4. **mekanismadditions** — 0 quests. Confirm jar contents → optional chapter slot or skip. (no gate)
5. **Depths of Malum** dimension — quest it or explicit skip? (no gate either way)
6. ~~Mekanism SPS gate~~ — no gate. Antimatter questing optional, low priority.
7. ~~enderio `powered_spawner` gate~~ — no gate. Optional quest only.
8. ~~extradisks p2p / portable cell gate~~ — no gate.
9. ~~Malum 5 elemental Spirit gate~~ — no gate. Author a ladder or leave as flavor (content call).
10. **Extended Crafting `advanced_table`** — AoA recipe needs only Gilded ingredients (recipe vs
    intended tier mismatch). Reconcile the RECIPE (not a gate) if it matters for progression.
11. **Neo Vitae anchor A1** — `ren_magic_foundations` still deps F&A `0B03101000000039` into
    capstone `0B0310100000CAFE`. Repoint to Ara Vitae T1, or leave? (content/wiring, not gating)
12. **Hephaestus Forge** non-monotonic tier ordering (T4/T5 vs T1-3) — bug or intent? (existing
    gate ordering, not a new gate)
13. **`aoacore-0.4.5` + `0.4.6`** duplicate jar loaded — remove the stale 0.4.5 (Part A.6).

## Definition of done (the whole pack)
- IR/Gilded/Atomic: verified clean, Create gaps closed, g6 descs filled.
- OW + Ascension: built to endgame depth, crossing-free, capstones wired, weaves clean.
- All Create add-ons: quested or explicitly deferred-with-reason.
- Zero SOFTLOCK, zero dangling deps, zero em dashes, zero `[STUB]`, zero failed `node --check`.
- `LEDGER.md` closed out; `DECISIONS NEEDED` surfaced to Andrew.
