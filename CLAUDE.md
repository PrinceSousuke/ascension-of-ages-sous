# Ascension of Ages — Claude Code project memory

NeoForge 1.21.1 CurseForge modpack. Quest layer: FTB Quests
(`config/ftbquests/quests/chapters/*.snbt`).

## Read this first

The full authoring canon lives in **@AOA_AGENT_CANON.md** — read it before you
create or edit any quest, chapter, KubeJS script, or config. It is the shared
source of truth for Claude Code, Codex, and Cursor. The live stage gate you must
respect is **@kubejs/server_scripts/aoa_astages_00_register_stages.js**.

## The rules that get broken most (also in the canon — repeated here so they
## survive subagent delegation)

Subagents you spawn do NOT inherit this file. If you delegate quest or config
work, restate these in the subagent's prompt.

1. **Age-tier discipline.** 8 ordered ages: `dark_ages`, `medieval_times`,
   `the_renaissance`, `industrial_revolution`, `gilded_age`, `atomic`,
   `otherworldly`, `ascension`. A quest may only require items/mods/mechanics
   legal at or before its chapter's age. Later-tier tech in an earlier age (e.g.
   a diving suit in a Dark Age line) is a hard defect and usually a real
   softlock. Confirm every item's unlock stage against the AStages scripts
   before placing it.
2. **Verify, never assume.** Do not reference a mod, item, block, tag, or
   mechanic without confirming it exists on disk or in the actual jar. Never
   guess an item ID. If you cannot verify it, say so and stop — do not fabricate.
3. **FTBQ format.** Preserve `.snbt` byte structure; coordinate-only edits for
   layout. Do NOT strip the `SkillsLevel` block (inert, regenerates). Only use
   real, verified More Quest Types task-type IDs — never invented ones.
4. **Layout.** Dependency lines must not cross (hard constraint). No filler /
   duplicate / vanilla-recipe quests. Quality over density; never pad to a count.
5. **Prose.** Instruction-first, teach the mechanic, no em dashes, no AI-isms,
   short declarative sentences.
6. **Tooling truth.** The mount can misreport truncation/corruption — use
   Desktop Commander or `node --check` as ground truth; do not "repair" on a
   truncation report alone. `node --check` every edited KubeJS script.
7. **Authoritative docs live under `AoA redo/`.** Treat anything outside it as
   non-authoritative for state-of-pack. Newer AoA-redo docs supersede older ones.

When in doubt, ask for a canon call rather than guessing. Act as a senior dev.
