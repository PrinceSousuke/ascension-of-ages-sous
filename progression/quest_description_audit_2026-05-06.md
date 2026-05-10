# Quest Description Audit — 2026-05-06

Full audit pass over every player-facing string in `config/ftbquests/quests/lang/en_us.snbt`. Cleanup of stale references to removed mods and structural cleanup of orphan lang entries.

## Scope

- All quest titles, descriptions, subtitles, and chapter titles in `en_us.snbt`
- Encoding sanity (single + double-encoded mojibake, HTML entity escapes, BOM, line endings)
- Color-code (`&x...&r`) reference syntax
- References to removed mods: DivineRPG, Ice and Fire, When Dungeons Arise + Seven Seas, Iron Jetpacks, Journey to the Lights
- Awareness of new/integrated mods: Chrono Dawn (DRPG replacement), Astral Dimension (probationary), Yggdrasil

## Stage 1 — Encoding cleanup

### Mojibake fixes — 296 lines

Library used: `ftfy` 6.3.1. Single-encoded UTF-8-as-CP1252 mojibake AND double-encoded mojibake (the latter showed up as long sequences like `ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â`) both resolved correctly.

Examples:

| Before | After |
|---|---|
| `mulch&r â€" the best tier` | `mulch&r — the best tier` |
| `&6â€¢ Brambleroot&r` | `&6• Brambleroot&r` |
| `&fkey&r ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â proof` | `&fkey&r — proof` |
| `Cataclysm boss ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â End-adjacent.` | `Cataclysm boss — End-adjacent.` |

### `&amp;` HTML entity → SNBT escape — 7 lines

Lines using HTML escape `&amp;` were converted to the SNBT-correct `\&` (file bytes `\\&` to render as a literal `&` in-game). Examples: `Flint &amp; Steel` → `Flint \& Steel`, `F&amp;A reagent` → `F\&A reagent` (so the `A` doesn't get interpreted as the green color code).

### Validations passed

- No BOM
- All CRLF line endings (no bare LF)
- No `\uXXXX` Unicode escapes (forbidden per project SNBT rules)
- No NULL bytes
- Brace and bracket balance preserved

## Stage 2 — Orphan lang entry cleanup

Scanned every quest ID referenced in `en_us.snbt` against the IDs actually present in chapter SNBT files. Result: **49% of lang entries were orphans** — referencing quests that had been deleted from chapter files.

| Bucket | Count |
|---|---|
| Unique quest IDs referenced in lang (before) | 3,601 |
| Live (still in a chapter file) | 1,833 |
| Orphan (no longer in any chapter) | 1,768 |
| Lang statements removed | 3,499 |
| Lang lines removed | 6,263 |

Orphan removal also resolved most of the residual references to removed mods, since the deleted quests were largely the DRPG / I&F / JITL chains.

## Stage 3 — Targeted live content fixes

Two live quests still referenced removed-mod content after orphan cleanup. Both fixed inline:

### Atomic Convergence intro (quest `4F43010000010001`)

```diff
- Both Lady Luna's death and the Gilded Oritech capstone gate this chapter.
+ Both the Time Tyrant's death and the Gilded Oritech capstone gate this chapter.
```

Aligns with the locked decision from the prior session: Time Tyrant (Chrono Dawn) replaces Lady Luna (DRPG) as the gate.

### End Remastered eye gate (quest `4FC72031CD12A930`)

The historical eye-source examples mentioned three DRPG bosses by name. Genericized so the description doesn't pin specific eye sources to bosses that no longer exist:

```diff
- (Iceika's Kitra → Cold Eye, Eden's Sunstorm → Exotic Eye, Deeper Darker's Lich → Black Eye, etc.)
+ (boss kills, dimension-specific encounters, and structure clears)
```

End Remastered's actual eye-source mappings live in its own config and are subject to change as the modlist evolves.

## Stage 4 — When Dungeons Arise chapter deletion

Mod jar removed from `mods/`. Chapter file (`when_dungeons_arise.snbt`) and 38 quests still existed. All 38 quests were `dungeons_arise:find_*` advancement trackers — completely unfulfillable without the mod. Zero cross-chapter dependencies pointed in.

Actions:

- Backed up and deleted `chapters/when_dungeons_arise.snbt` (now `.bak.deleted_<timestamp>`)
- Removed 39 lang entries (chapter title + 38 quest titles/subtitles/descriptions)
- Annexes chapter group preserved — still hosts Minecolonies

## Final integrity

| Metric | Before | After |
|---|---|---|
| Lang file size | 1,061,256 bytes | 648,409 bytes (-38.9%) |
| Lang line count | 17,397 | 10,939 (-37.1%) |
| Unique quest IDs in lang | 3,601 | 1,795 |
| Description entries | 98 → restored to 1,878 (proper count after correct parse) | |
| Title entries | 2,939 | 1,358 |
| Subtitle entries | 27 | 694 (proper count after correct parse) |
| BOM | none | none |
| Line endings | CRLF | CRLF |
| Brace/bracket balance | balanced | balanced |
| Removed-mod references (DRPG/I&F/WDA/JITL) | 217+ | 0 |
| Mojibake lines | 296 | 0 |
| `&amp;` HTML entities | 7 | 0 |

## Deferred / pending

### Chrono Dawn integration (in-flight, separate prompt)

The previous "Analyze mods and rewire questlines" session already produced a detailed Codex prompt for this — `outputs/codex_prompt_astral_chrono_implementation.md`. Locked decisions:

- Chrono Dawn = serious DivineRPG replacement gate path
- `chronodawn:clockstone` becomes Atomic chokepoint (also plugs the Ancient Ruins Overworld leak)
- Time Tyrant kill replaces Lady Luna in `triggers.toml`
- Astral Dimension stays optional/probationary as a Gilded side branch with Lucid tier locked behind Atomic
- Hex prefixes 4344 (Atomic Chrono Dawn) and 4150 (OW Astral Pilgrimage) reserved
- New chapters `atomic_chrono_dawn.snbt` and `g_astral_side_branch.snbt` to be authored when running that prompt

That prompt is the right place to do the chapter authoring, not this audit. This audit cleared the stage by removing every stale lang reference that could conflict.

### Other structure mods added

User mentioned Astral Dimension, Chrono Dawn, Yggdrasil, plus other unspecified structure mods are now in the modlist. None of them have quests yet — to be authored in a future pass.

## Backup files created

- `lang/en_us.snbt.bak.audit_20260506_213020` — pre-audit lang
- `lang/en_us.snbt.bak.audit_swap_20260506_213348` — pre-Stage-3 lang
- `lang/en_us.snbt.bak.wda_delete_20260506_213619` — pre-WDA-delete lang
- `chapters/when_dungeons_arise.snbt.bak.deleted_20260506_213619` — deleted WDA chapter

## In-game round-trip status

**PENDING** — per project SNBT write-safety rule, only the user can validate this by loading the world and confirming the quest book opens cleanly. Static validation passed all gates.
