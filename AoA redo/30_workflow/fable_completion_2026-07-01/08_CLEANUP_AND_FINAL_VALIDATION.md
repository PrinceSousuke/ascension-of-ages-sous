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
1. **Ungated content sweep (big one):** 139 content mods have no AStages gate. Some are
   intentional (Quark decor, per canon "don't lock decor mods"). Most tech/magic ones are not.
   Produce the list, split "intentional-open" vs "needs a gate," and gate the latter at their
   tier. This is an age-discipline hole, not just a coverage gap.
2. **apotheosis** — real gem/affix apparatus, **no gate at all**. Capstone-only by design
   (current state), or add a gate + a teaching questline? Gear can leak arbitrarily early today.
3. **apothic_enchanting** — ungated + 0 quests; canon wants "late-Renaissance controlled." Set
   the gate, then `02b` authors the line.
4. **mekanismadditions** — 0 gate + 0 quests. Confirm jar contents → chapter slot or explicit skip.
5. **Depths of Malum** dimension — no gate, no quest. In scope or explicit skip?
6. **Mekanism SPS** (`sps_casing`/`sps_port`) — ungated; is antimatter production in scope?
7. **enderio `powered_spawner`** — real block, ungated + unquested. Gate + quest or skip?
8. **extradisks** `chemical_p2p_tunnel` / portable cell line — ungated; scope decision.
9. **Malum** 5 elemental Spirit types — need a gate, or leave as flavor?
10. **Extended Crafting `advanced_table`** — its AoA recipe needs only Gilded ingredients but the
    block stays Ascension-locked. Not a softlock; reconcile gate vs recipe.
11. **Neo Vitae anchor A1** — `ren_magic_foundations` still deps F&A `0B03101000000039` into
    capstone `0B0310100000CAFE`. Repoint to Ara Vitae T1, or leave?
12. **Hephaestus Forge** non-monotonic tier gating (T4/T5 lock back to Renaissance) — bug or intent?

## Definition of done (the whole pack)
- IR/Gilded/Atomic: verified clean, Create gaps closed, g6 descs filled.
- OW + Ascension: built to endgame depth, crossing-free, capstones wired, weaves clean.
- All Create add-ons: quested or explicitly deferred-with-reason.
- Zero SOFTLOCK, zero dangling deps, zero em dashes, zero `[STUB]`, zero failed `node --check`.
- `LEDGER.md` closed out; `DECISIONS NEEDED` surfaced to Andrew.
