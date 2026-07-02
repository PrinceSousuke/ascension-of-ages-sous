# Implementer contract — foundations program wave I (2026-07-02)

Binding for every implementation task in this wave. Your dispatch prompt names your TASK ID
and PLAN FILE — read the plan's section for your task id; it is your requirements, use its
exact ids/values verbatim.

Pack root: `C:\Users\andre\curseforge\minecraft\Instances\Ascension of Ages (codex and cc)`.

## Absolute rules
1. NO git commands, ever. Leave all changes in the working tree.
2. FILE SET IS A CONTRACT: you may edit ONLY the files your task declares (plus your own
   log + sidecar under phase0/). If correct implementation would require touching any other
   file, STOP and report BLOCKED with the reason. Do not improvise cross-file edits.
3. Do NOT edit `config/ftbquests/quests/lang/en_us.snbt`. All lang keys for your new nodes
   go to `phase0/stubs/<TASK-ID>_stubs.txt` (create it), one line per key, exactly:
   `\tquest.<id>.title: "[STUB] <short working title>"` (tab-prefixed, same for
   quest_subtitle; quest_desc as `["[BRIEF] teaches: ...; requires ...; prior node ...;
   Opus: 2-4 para instruction-first."]`). New CHAPTER title keys likewise
   (`\tchapter.<chapterid>.title: ...`). The coordinator merges these.
4. `.snbt` byte discipline: detect each file's line endings via Python byte count
   (raw.count(b'\r\n') vs b'\n') and preserve exactly (chapters are CRLF). Preserve tab
   structure. Copy `SkillsLevel`/`PlayerSpells` blocks from a sibling node — never strip,
   never hand-type. Coordinate values on the 0.5 grid, `d` suffix.
5. Quest ids: fresh 16-hex ids proven unique with an anchored scan of ALL chapters
   (`^\s+id: "`). Use a coherent per-task prefix.
6. NO rootless quests: every new quest has >= 1 dependency (rootless = always visible =
   reveal leak). A NEW CHAPTER's entry quest must copy the entry-gating pattern of its
   sibling chapters in the same age group (read 2 siblings' first quests and replicate how
   they dep on the age gateway). New chapter files copy a sibling's chapter-level structure
   (group id, order_index after the last sibling, default flags).
7. Verify-first: every item/advancement id you place must exist (the plan carries jar
   proofs — trust them, but if you use ANY id not in the plan, jar-verify it yourself and
   log the proof). Never invent ids. Icons = task items; non-item quests use a verified mod
   icon.
8. No vanilla `minecraft:` task items. No duplicate item tasks pack-wide: grep the whole
   chapters dir for each task item id before adding; if tasked anywhere, dep-reference that
   quest instead. Variants → one task with `ftbfiltersystem:smart_filter` (copy live NBT
   shape from stone_water or g4 examples).
9. Crossing-free: dependency lines in your edited chapter(s) must not cross. Compute/verify
   and state the result. Do not add crossings to dense chapters; re-lay your own nodes.

## Verification before hand-off (paste outputs in your log)
- `python "AoA redo/30_workflow/fable_completion_2026-07-01/phase0/tier_audit.py"` →
  0 SOFTLOCK (grep the regenerated A_tier_softlock_table.md).
- `python "AoA redo/30_workflow/fable_completion_2026-07-01/phase0/ef_audit.py"` →
  0 duplicates / 0 dangling / 0 backward-age.
- Era check: no item later-tier than your chapter's age (preamble §3).
- Brace/bracket balance + EOL purity per edited file (Python).
- `node --check` for any KubeJS file you touched.
- Crossing statement per chapter.

## Deliverables
Working-tree edits + `phase0/<TASK-ID>_log.md` (node ids created, deps, re-wires old→new,
audit outputs, crossing statement) + your sidecar stub file. Final message: STATUS
(DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED) + one line per node group + concerns.
