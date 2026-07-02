# T9 — Journey to Ascension finishing pass (implementation log)

Date: 2026-07-02. No git operations performed; all changes left in the working tree.

Design goal (coordinator decision): J2A = pure table of contents, grants NOTHING. The
world-entry `dark_ages` grant relocated out of J2A into a Dark Ages chapter.

## Tool path note

The task prompt referenced `tools/gen_j2a.py` / `tools/verify_j2a.py`, but both actually
live under `.aoa_reveal_audit/` (gitignored). Confirmed on disk; there is no `tools/` copy.
All generator/verifier edits were made under `.aoa_reveal_audit/`.

## Files touched

1. `config/ftbquests/quests/chapters/stone_water_weather_and_wounds.snbt` — hand-added one
   invisible/optional/task-less `dark_ages` grant node (byte-level insert, bare-LF preserved).
2. `.aoa_reveal_audit/gen_j2a.py` — removed grant emission, fixed em-dashes, forced CRLF for
   the chapter output, neutralized dead `reward_blocks()`.
3. `config/ftbquests/quests/chapters/journey_to_ascension.snbt` — regenerated (grant-free, CRLF).
4. `config/ftbquests/quests/lang/en_us.snbt` — regenerated journey lang keys (em-dash-free).
5. `config/modpack_defaults/config/ftbquests/quests/chapters/journey_to_ascension.snbt` — regenerated.
6. `config/modpack_defaults/config/ftbquests/quests/lang/en_us.snbt` — regenerated journey keys.
7. `.aoa_reveal_audit/verify_j2a.py` — rewritten for the current check_quest / grant-free design.

## New Dark-chapter grant node

- Quest id: **`3400000000009000`** (verified free pack-wide before use via anchored `"[0-9A-Fa-f]{16}"` scan).
- Reward ids: `3400000000009001` (`/astages add {p} dark_ages true true`),
  `3400000000009002` (`/advancement grant {p} only aoa:age/dark_ages`).
- Flags: `invisible: true`, `optional: true`, `tasks: [ ]`, no dependencies.
- Placement: far corner `x: 12.0d, y: 12.0d` (chapter content spans x -7..2.5, y -6..2.5).
- Reward blocks copied verbatim from the old J2A entry (auto: "enabled", permission_level: 2,
  silent: true, team_reward: true, type: "command"), preserving auto-grant-at-world-entry
  semantics. The chapter inherits file-level `progression_mode: "flexible"` (data.snbt), under
  which a task-less quest auto-completes at world entry, firing both grants — identical to the
  old J2A entry behavior.
- No lang keys added: an invisible node is never shown, so FTBQ needs no title. (Confirmed
  invisible nodes can carry lang but do not require it.)

## Before / after grant location

| | Before | After |
|---|---|---|
| J2A entry `5350010000010000` | 2 command rewards (`dark_ages` + adv), task-less | task-less root, ZERO rewards/grants |
| `dark_ages` world-entry grant | J2A entry node | `stone_water_weather_and_wounds.snbt` node `3400000000009000` |
| J2A `astages add` count | 1 | **0** |
| J2A `advancement grant` count | 1 | **0** |

## gen_j2a.py changes

- START_ID branch no longer emits any `rewards:` block; comment added pointing to the Dark
  chapter grant node.
- `reward_blocks()` helper deleted and replaced with a warning comment (dead code that could
  reintroduce the mass-grant bug if re-wired).
- Em-dash subtitles (old lines ~363-364) rewritten em-dash-free:
  - `"Age gate. Clears when its capstone quest is complete."`
  - `"Capstone. Clears when its quest is complete."`
- Chapter EOL forced to CRLF (`feol = '\r\n'`); lang EOL still detected per-file (no wholesale
  rewrite of the live en_us line endings).

## Regeneration + verification

`python .aoa_reveal_audit/gen_j2a.py --write` wrote both live and modpack_defaults targets.

Regenerated chapter (live and md, identical):
- 56 nodes (unique), 55 `check_quest` tasks
- `astages add`: 0 | `advancement grant`: 0 | `rewards: [` blocks: 0 | `type: "command"`: 0
- braces 169/169, brackets 168/168 (balanced)
- CRLF 1240, bare-LF 0 (CRLF pure)
- em-dashes: 0

Lang em-dash counts (requirement: stays 0):
- live `en_us.snbt`: **0** em-dashes (EOL unchanged, bare-LF)
- md `en_us.snbt`: **0** em-dashes (EOL unchanged, CRLF)

### verify_j2a.py PASS output

```
Total J2A nodes: 56

Granters pack-wide: 55 | mirror targets: 55 | expected mirrors (granters+finale): 55
=== ISSUES (0; 0 critical) ===

PASS: J2A is a grant-free check_quest table of contents; coverage complete; Dark grant relocated.
```

(The `3400000000009000` Dark grant node is excluded from the expected-mirror set: it is the
relocated internal grant and is deliberately not surfaced in the TOC.)

### Final smoke (brace balance + EOL purity)

```
j2a live | braces 169/169 brackets 168/168 | balanced True | EOL crlf CRLF 1240 LF 0 pure True
j2a md   | braces 169/169 brackets 168/168 | balanced True | EOL crlf CRLF 1240 LF 0 pure True
stone_water | braces 167/167 brackets 83/83 | balanced True | EOL lf CRLF 0 LF 839 pure True
SMOKE PASS
j2a astages add count: 0
stone_water 3400000000009000 grants dark_ages: True
```

## Notes / non-changes

- The live `en_us.snbt` remains bare-LF (its pre-existing state); em-dash requirement is about
  content, not EOL, and it is 0. The md `en_us.snbt` remains CRLF. Neither file's line endings
  were rewritten wholesale — only the journey keys were merged, each in the file's own EOL.
- `stone_water_weather_and_wounds.snbt` remains bare-LF (its pre-existing state); the task
  scoped CRLF normalization to the J2A chapter only.
