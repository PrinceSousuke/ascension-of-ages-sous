# Ascension of Ages Codex/CC Authority

This checkout uses the current AStages/KubeJS stage model.

**Read `AOA_AGENT_CANON.md` first** — it is the shared authoring canon for Claude Code, Codex, Cursor, Cline, OpenCode, and Hermes. This file is the KubeJS/stage-model addendum to it. Load-bearing rules, repeated so they are in-context here:

- **Age-tier discipline.** 8 ordered ages: `dark_ages`, `medieval_times`, `the_renaissance`, `industrial_revolution`, `gilded_age`, `atomic`, `otherworldly`, `ascension`. A quest may only require items/mods/mechanics legal at or before its chapter's age. Later-tier tech in an earlier age (e.g. a diving suit in a Dark Age line) is a hard defect and usually a softlock. Confirm each item's unlock stage against `kubejs/server_scripts/aoa_astages_*.js` before placing it.
- **Verify, never assume.** Never reference a mod/item/block/tag/mechanic without confirming it exists on disk or in the actual jar. Never guess an item ID. If you cannot verify it, say so and stop.
- **FTBQ.** Quests are `config/ftbquests/quests/chapters/*.snbt`. Preserve byte structure; do NOT strip the `SkillsLevel` block (inert, regenerates); only real, verified More Quest Types task IDs. Dependency lines must not cross. Quality over density, never pad to a count.
- **Prose.** Instruction-first, teach the mechanic, no em dashes, no AI-isms.

### KubeJS / stage-model addendum

- Treat `kubejs/server_scripts/aoa_astages_00_register_stages.js` as the live stage registry.
- Treat `kubejs/server_scripts/aoa_astages_*.js` as the live restriction surface.
- Do not restore retired stage config trees, stage-history configs, KubeJS stage-mutation shims, or bootstrap helpers.
- FTB Quests may award stages through explicit AStages command rewards; KubeJS should register restrictions, not grant or revoke progression stages.
- Before editing KubeJS restrictions, inspect `kubejs/AGENTS.md` and verify changed scripts with `node --check`.
- Keep launcher caches, crash-assistant caches, backup folders, generated reports, and stale planning mirrors out of runtime config paths.
