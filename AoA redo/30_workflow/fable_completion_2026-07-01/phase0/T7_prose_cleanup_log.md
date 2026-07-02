# T7 — Prose cleanup log (Opus lane)

Target file (only file edited): `config/ftbquests/quests/lang/en_us.snbt`
Date: 2026-07-02. No git, no chapter edits, no other config touched.

## File discipline

- Line endings: pure LF (`\r\n` count = 0) before and after. Preserved.
- No en dashes (U+2013) introduced (count = 0 before and after).
- No smart quotes/apostrophes introduced (scan = 0).
- Indentation of inserted lang keys matches existing keys (single leading tab).
- Line count 7702 -> 7712 (exactly +10, the ten inserted `quest_desc` keys).
- Brace/bracket balance after edit: `{`=`}`=1 (single root object), `[`=`]`=1930.
- Odd-quote line scan: 0.

## Counts

| Item | Before | After |
|---|---|---|
| Em dashes (U+2014) | 87 | **0** |
| Non-array `quest_desc` (ow6) | 7 | **0** (converted to array) |
| Missing `quest_desc` (10 real ids) | 10 | **0** (authored) |
| Lang key lines (`title`/`quest_subtitle`/`quest_desc`) | — | 5734 |

## 1. Em-dash replacements (87 -> 0)

Every U+2014 replaced by period/comma/colon restructuring per style rule (never a hyphen,
never an en dash). Grouped:

- **32 chars across 23 non-journey keys** (content chapters): ren_nether Neo Vitae subtitle
  + descs, ren_observation, ren_archive + grove + cnb flavor subtitles, at7 chaos convergence
  (5 descs), g1 Athanor (desc + subtitle), Steam Quarry multiline desc, ow6 Sentient/Spiritus
  (7 subtitles + 7 descs).
- **55 chars in journey_to_ascension mirror subtitles** (lines 7505–7613): two fixed phrases
  replaced globally —
  `Age gate — clears when...` -> `Age gate. Clears when...`
  `Capstone — clears when...` -> `Capstone. Clears when...`

Each replacement was matched on the full surrounding value substring (unique) so no false hits.

## 2. Non-array quest_desc -> array (ow6, 7 keys)

`quest.4256011000EE0001` … `4256011000EE0007` converted from `quest_desc: "..."` to
`quest_desc: ["..."]` (pack standard). Em dashes inside these same 7 descs were fixed in the
same pass, so the array bodies are already clean.

## 3. Authored 10 missing quest_desc keys

All task items verified against the live jar `en_us.json` before writing.

| id | Chapter | Task item (verified) | Item name |
|---|---|---|---|
| 051AB096CA0848B4 | g6_circuits_and_current | `create_aquatic_ambitions:prismarine_alloy` | Prismarine Alloy |
| A818144300D946A8 | g6 | `create_aquatic_ambitions:mechanical_conduit` | Conduit Cage |
| 7C0AC10000000001 | g6 | `create_aquatic_ambitions:prismarine_alloy_rod` | Prismarine Alloy Rod |
| 7C0AC10000000002 | g6 | `create_aquatic_ambitions:spiky_shell` | Spiky Shell (awaken/channel Conduit Cage) |
| 936044D132622461 | ren_archive_recordkeeping | `arcanelanterns:lantern_maker` | Lantern Maker |
| 3D0C727EB7D7D9FC | ren_archive_recordkeeping | `arcanelanterns:life_lantern` | Life Lantern |
| FAB07684061A284D | ren_nether_threshold | `cnb:cinder_furnace` | Cinder Furnace (Cindershell-worn) |
| 1E5A8AEE45E9DDCA | ren_nether_threshold | `cnb:cinder_sword` | Cinder Sword |
| E101BB0D29F60954 | what_waits_in_the_grove | `crittersandcompanions:grappling_hook` | Grappling Hook |
| 92614B6AD7E19E44 | what_waits_in_the_grove | `crittersandcompanions:silk_lead` | Silk Lead |

Mechanic sources used for accuracy:
- Conduit Cage awakening/channeling text taken from the mod's own ponder lang
  (`mechanical_conduit_awaken` / `_processing` / `_effects`): pump fluid through the bottom
  face to awaken; water gives Conduit Power; air through an awakened cage creates a channeling
  processing stream.
- Life Lantern / Lantern Maker from the jar block descriptions (crop-growth aura; Lantern
  Maker fuses a lantern placed on top with catalysts).
- Cinder Furnace from the jar tooltip ("Right click a Cindershell to equip") — a wearable
  furnace shell for the Cindershell mob.

**ren_nether caveat handled:** the two ren_nether ids (FAB07684061A284D, 1E5A8AEE45E9DDCA) are
CnB items and are NOT among the 8 Neo Vitae nodes being relocated
(0B03102000000041/42/46/47/81, 0B03101000000038/70/75). Prose teaches the mechanic without
naming a hosting chapter or age, so it stays correct if the chapter moves.

All descs are 2 short array entries, instruction-first, no em dashes, no AI-isms.

## 5 representative before/after fixes

1. **Journey mirror (x55)**
   before: `"Capstone — clears when its quest is complete."`
   after:  `"Capstone. Clears when its quest is complete."`

2. **g1 Athanor desc (4757011020010001)**
   before: `...activate the &bAthanor&r — Neo Vitae's apex Vitae-refinement station...`
   after:  `...activate the &bAthanor&r, Neo Vitae's apex Vitae-refinement station...`

3. **ow6 Sentient armor desc (4256011000EE0002)** — em fix + array conversion
   before: `quest_desc: "...leggings, and boots — each piece is infused..."`
   after:  `quest_desc: ["...leggings, and boots. Each piece is infused..."]`

4. **New desc — Conduit Cage awaken (7C0AC10000000002)** (was absent)
   after:  `quest_desc: ["Awaken the &bConduit Cage&r, then use it to channel the reef. Pump a
   fluid into the cage through its bottom face and it comes alive.", "Water gives it the
   Conduit Power effect... air blown through an awakened cage also creates a channeling stream
   that processes items... Submit a &bSpiky Shell&r..."]`

5. **New desc — Cinder Furnace (FAB07684061A284D)** (was absent)
   after:  `quest_desc: ["Obtain a &bCinder Furnace&r. This is a wearable furnace shell that a
   Cindershell can carry for you.", "Tame or approach a Cindershell, then right click it with
   the Cinder Furnace to equip the shell onto the creature..."]`

## Verification

- Post-edit: em = 0, en = 0, CRLF = 0, braces/brackets balanced, odd-quote lines = 0.
- All 10 new desc keys present and array-formed; all 7 ow6 descs now array-formed.
- No unverified item id: all 6 non-g6 task items and all 4 g6 items confirmed in their jars'
  `lang/en_us.json`.
