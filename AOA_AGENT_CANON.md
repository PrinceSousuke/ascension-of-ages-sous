# Ascension of Ages — Agent Canon

Single source of truth for every AI agent that authors or edits content in this
pack: Claude Code CLI (via `CLAUDE.md`), Codex (via `AGENTS.md`), and Cursor
(via `.cursor/rules/aoa-canon.mdc`). All three import or reference this file.
Edit rules HERE, not in three places.

Pack: NeoForge 1.21.1, CurseForge. Quest layer: FTB Quests.

---

## 0. Non-negotiables

- **Verify, never assume.** Do not reference a mod, item, block, fluid, tag,
  recipe, or mechanic without confirming it exists on disk or inside the actual
  mod jar. If you cannot verify it, say so and stop. Do not fabricate to keep
  moving. Guessing an item ID is a defect.
- **Act as a senior developer.** Ask when a decision needs a canon call. Flag
  anything questionable rather than papering over it.
- **Never `PASS_WITH_TODOS`.** A pass is clean or it is not a pass. No `.bak`
  files left in runtime paths. A duplicate-item scan is mandatory before you
  call an authoring task done.

---

## 1. Age-tier discipline (the most important rule)

The pack has **8 ages, in strict order**, mapped to real-world tech eras:

`dark_ages` → `medieval_times` → `the_renaissance` → `industrial_revolution`
→ `gilded_age` → `atomic` → `otherworldly` → `ascension`

(Note the exact IDs: `the_renaissance` has the `the_` prefix; `atomic` has no
`_age` suffix; `dark_ages` is plural.)

**A quest may only require items, mods, or mechanics that are legal at or before
its chapter's age.** Placing later-tier tech in an earlier age is a hard defect —
it is both a lore anachronism and, usually, a real softlock. A diving suit,
firearm, reactor, or any post-medieval device does NOT belong in a Dark Age
line. Before you place ANY item task in a chapter, confirm the item's unlock
stage and confirm that stage is at or before the chapter's age.

**Where the gate is defined (verify against these, do not trust memory):**

- Live stage registry: `kubejs/server_scripts/aoa_astages_00_register_stages.js`
- Live restriction surface: `kubejs/server_scripts/aoa_astages_*.js`
- Item→stage locks are the machine-staging contract. If an item's unlock stage
  is later than the chapter it appears in, do not place it. Down-tier the
  blocker or move the quest — never ship the inversion.

When you introduce or move a required quest, recursively check that you did not
create a NEW cross-age inversion downstream. Big cascades get a checkpoint.

---

## 2. FTB Quests authoring

- Quests live in `config/ftbquests/quests/chapters/*.snbt`. **FTBQ is the
  canonical quest layer** (Questlog is retired for go-forward work).
- Preserve the `.snbt` format exactly: line endings, quest `id`s, structure.
  For layout work, prefer coordinate-only edits that leave everything else byte
  identical.
- **Do NOT strip the `SkillsLevel` block.** It is an inert artifact of the
  More Quest Types mixin and regenerates on save. Removing it fixes nothing and
  only churns the file.
- Use the **More Quest Types** addon's extended task/reward types for completion
  variety, plus other installed quest-addition mods on top of base FTBQ. Always
  verify the addon's REAL task-type IDs in its jar before use. Never invent a
  task-type ID.
- `id:`-style duplicate scans must be anchored (`grep -P '^\s+id:'`); a loose
  `id:` grep matches `autofocus_id:` and reports false duplicates.

---

## 3. Chapter layout

- **Crossing-free layouts are a hard constraint.** Dependency lines must not
  cross. Flow direction is negotiable (vertical/backward allowed); crossings are
  not.
- Tight spacing on a 0.5 grid. Pool related mods. First-placement-wins for a
  shared item. Bundle multiblock steps into one node rather than scattering them.
- No filler: no vanilla-recipe quests, no checkmark quests, no near-duplicate
  variants, no padding.
- Icons: a quest's icon is its task item. A non-item quest gets a verified,
  distinct mod icon — check the jar's item models, never guess an icon ID.

---

## 4. Density

Quality over quantity, always. Density floors are aspirational, not mandatory,
and there are no ceilings. **Padding to hit a number is forbidden.** If you are
short on real content, under-author — do not invent quests to reach a count.

---

## 5. Prose voice

- Instruction-first. Teach the mechanic. Roughly 2–4 paragraphs per quest that
  actually explains how to progress, slightly over-explaining is fine.
- **No em dashes anywhere.** No AI-isms. No "the X is the lesson" aphorisms.
  Short declarative sentences. Bundle the items a quest needs into that quest.

---

## 6. Tooling and process

- The Cowork/editor mount can misreport file contents (apparent truncation,
  `node --check` failures, "binary file matches"). This is usually the read
  layer lying, not real corruption. Use Desktop Commander or a direct
  `node --check` as ground truth for counts and integrity. Do NOT rewrite or
  "repair" a file on a truncation report alone — only if the user asks.
- Verify every edited KubeJS script with `node --check` before finishing.
- Do not restore retired stage config trees, stage-history configs, KubeJS
  stage-mutation shims, or bootstrap helpers. KubeJS registers restrictions; it
  does not grant or revoke progression stages. FTBQ awards stages via explicit
  AStages command rewards.
- Keep launcher caches, crash-assistant caches, backup folders, generated
  reports, and stale planning mirrors out of runtime config paths.
- **Authoritative docs live under `AoA redo/`.** Anything outside it (root
  `reports/`, scattered older mirrors) is treated as non-authoritative for
  state-of-pack. Newer `AoA redo/` docs supersede older ones. Do not cite a
  stale/superseded file as current.

---

## 7. Removed content (do not reference)

Mods pulled from the pack are gone. Notable examples: `phantasm`,
`luminous_nether`, `gardens_of_the_dead`. Alloy Forgery does not exist on
NeoForge 1.21.1 — do not suggest it (the separate mod "Alloyed" IS installed and
is unrelated). Before referencing any borderline mod, confirm its jar is present.

---

## 8. Delegation

Prefer high-reasoning models for authoring and audits, not the smallest ones.
Always verify findings before reading them back to the user. When a task spans
Codex and Claude Code, split it to each tool's strength and state the split
explicitly.

---

## 9. Quest scope registry (read before any coverage/gating work)

`AOA_QUEST_SCOPE_REGISTRY.md` (repo root) is the standing, authoritative list of
mods that are deliberately OUT of quest scope, plus the pack's gating policy. Load
it at the start of any coverage census, "not-fully-done" audit, gap report, or
gating proposal.

- **No coverage-driven gating.** Ungated mods do not need gates. Do not propose or
  flag new AStages gates for coverage/age-discipline reasons. Any "N ungated mods
  need gating" finding is void.
- **Excluded mods are not "missing coverage."** If a census flags a registry-excluded
  mod as unquested/not-done, the census is wrong — reconcile against the registry,
  do not re-raise it.
- Update rulings in the registry (with a date), not scattered across reports.
