# P2 — Opus Prose Lane change log (phase0)

Date: 2026-07-02
Lane: Opus PROSE. Only file edited: `config/ftbquests/quests/lang/en_us.snbt`.
No git actions taken. Changes left in the working tree.

## Task 1 — Stub replacement (81 stub values across 27 quests)

Replaced every `[STUB]` title/subtitle and every `[BRIEF]` quest_desc with real
instruction-first prose (2-4 short paragraphs, array form, no em/en dashes). Each
brief was honored exactly; no mechanics invented beyond the brief. Every proof
item / entity ID named in prose was jar-verified in the mod's `lang/en_us.json`
before use (see verification note below).

Quests filled (grouped by line):

IR Qliphoth (Chesed exam):
- 49540C100000002D Eye of Chesed
- 49540C100000002E The Mercy Monolith
- 49540C100000002F Chesed, No Mercy

Gilded Qliphoth (Malkuth exam):
- 505701100000000A Eye of Malkuth
- 505701100000000B The Fallen King's Arena
- 505701100000000C Malkuth, the Tsar's Wrath

Renaissance Nether boss line:
- 0B03102000000100 Ignis
- 0B03102000000101 The Harbinger
- 0B03102000000102 Locate the Gauntlet Arena
- 0B03102000000103 Nether Gauntlet

Renaissance Aether:
- 0B03103000000100 Silver Dungeon
- 0B03103000000101 Valkyrie Queen

Renaissance promoted-boss proof terminals:
- 0B03104000000100 Starlight Proven
- 0B03105000000100 Forgotten Guardian Proven

Otherworldly boss lines (OW2/OW3/OW5/OW6):
- 4C580000EE000000 Sun Altar Chamber
- 4C580000EE010000 The Sun Spirit
- 4C580000EE020000 Eye of the Storm
- 44540000EE000000 Return to the End
- 44540000EE010000 The Ender Guardian
- 44540000EE020000 Helvar, the Underworld Knight
- 44430000EE000000 Permafrost
- 44430000EE010000 Lunar Monstrosity
- 42560000EE000000 Sirok, the Sandworm
- 42560000EE010000 The Void Worm

Atomic BL4 lane (at7):
- 4358010000EE0F02 Luxtructosaurus
- 4358010000EE0F01 The Watcher

Ascension BL4 (asc6):
- 4252010000EE0001 Scylla

## Task 2 — Stale-prose fixes on promoted bosses

Each target verified against its chapter file (`optional:` flag presence) before
rewriting. Rewrote to state the fight is REQUIRED:

- 4252010000010009 Infernal Dragon (asc6_bosses_rise) — chapter: no `optional`
  flag (required). Was "optional boss-route check". Rewritten as required
  pre-finale boss; subtitle -> "Required pre-finale boss."
- 425201000001000A Kraken (asc6_bosses_rise) — chapter: required. Was "optional
  boss-route check". Rewritten as required pre-finale boss; subtitle updated.
- 0B03104000000073 Starlight Golem (ren_starlight_observation) — chapter:
  required (no `optional`). Was "optional construct boss / not a required chapter
  gate". Rewritten as required; the Starlight proof depends on it.
- 4358010000010001 Tremorzilla (at7_chaos_convergence) — chapter: required
  (no `optional`, grants tremorzilla_defeated). Subtitle was "Optional: the
  cave's own deterrent." Rewritten desc + subtitle to "Required Atomic boss."

Checked and deliberately LEFT unchanged (chapter files confirm still optional):
- 4252010000010001 The Leviathan (asc6) — `optional: true`
- 4252010000010007 Tremorzilla (asc6, separate node) — `optional: true`
- 4252010000010008 Ancient Hero (asc6) — `optional: true`
- 0B03104000000072 Permafrost (ren, separate node) — `optional: true`
- 0B03105000000041 Forgotten Guardian — required, but prose already read as
  required (no "optional" wording); no change needed.

## ID verification (all present in jar lang/en_us.json)

fdbosses: eye_of_chesed, chesed, lightning_core, eye_of_malkuth, malkuth,
fire_and_ice_core. cataclysm: ignis, ignitium_ingot, the_harbinger,
witherite_block, ender_guardian, gauntlet_of_guard, scylla, essence_of_the_storm.
aether: silver_dungeon_key, gold_dungeon_key, valkyrie_queen, sun_spirit.
deep_aether: brass_dungeon_key, eots_controller. block_factorys_bosses:
underworld_knight, knight_sword, sandworm, sandworm_gauntlet, infernal_dragon,
kraken, kraken_tooth. alexsmobs: void_worm, void_worm_eye. alexscaves:
luxtructosaurus, tectonic_shard, watcher, occult_gem. undergarden:
forgotten_nugget, forgotten_guardian. eternalstarlight: permafrost,
lunar_monstrosity, orb_of_prophecy, starlight_golem. BOMD: gauntlet, blazing_eye
(gauntlet_arena is a structure, not a lang item, as the brief noted).

## Process note

Initial fill pass used a lazy `\[.*?\]` regex on quest_desc; on the 6 multi-line
`[BRIEF]` array blocks it matched only up to the `]` inside the `[BRIEF]` token,
leaving trailing brief text and orphan `]` lines. Caught by a bracket-balance
check against the HEAD baseline. Repaired by truncating each affected desc at its
array-close bracket and dropping the 6 orphan bracket lines. Re-verified balanced.

## Final counts (post-repair)

- Line endings: bare LF (CRLF = 0). Preserved.
- em-dash (U+2014): 0
- en-dash (U+2013): 0
- `[STUB]`: 0    `[BRIEF]`: 0    ` teaches:` / `Opus:` remnants: 0
- braces `{` `}`: 1 / 1 (unchanged)
- brackets `[` `]`: 1957 / 1957 (balanced; baseline was 2038/2038, minus 81 from
  removed `[STUB]`/`[BRIEF]` markers = 1957 — matches, still balanced)
- Key count: 5944 (identical to baseline; zero keys added/removed; order preserved)
- Line count: 7809 -> 7794 (delta -15). Explained: several `[BRIEF]` quest_desc
  values were authored by Fable in multi-line array form (key line, then the
  brief string on its own indented line, then a lone `]` close line = 3 lines
  each). Opus rewrote every filled quest_desc as a single-line array, which drops
  the per-block brief line and close line. The -15 delta is entirely this
  desc-array line-form normalization across the affected multi-line stub blocks.
  Verified no content lost: key count is identical to baseline (5944), key order
  preserved, and all 1901 quest_desc arrays are well-formed (integrity scan =
  zero issues). Single-line stub descs contributed no line delta.
