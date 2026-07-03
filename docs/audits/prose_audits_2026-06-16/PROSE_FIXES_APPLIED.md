# Fixes applied - 2026-06-16

Current pass edits: 40 strings total, with 28 in `config/ftbquests/quests/lang/en_us.snbt` and 12 in `kubejs/assets/aoa/lang/en_us.json`.

Mechanical prose follow-up: `MECHANICAL_PROSE_VALIDATION_2026-06-17.md` records 25 additional targeted field edits (22 in `config/ftbquests/quests/lang/en_us.snbt`, 3 in `kubejs/assets/aoa/lang/en_us.json`) made after the OW6 fix to remove mechanically misleading player-facing text.

Folded but not re-applied: `entering_the_iron_era.md` already records 4 WARN and 1 INFO, and `entering_the_iron_era.judgment.md` confirms those live strings are fixed, including the repeatability/desync line for `097AED7C91033D5E`.

Backup for the current SNBT batch: `C:\Users\andre\.codex\backups\aoa\20260616_231503\en_us.snbt.20260616_231503.bak`.
Backup for the OW6 follow-up SNBT edit: `C:\Users\andre\.codex\backups\aoa\20260617_230032\en_us.snbt.pre_ow6_fix.bak`.
Backup for the mechanical prose follow-up SNBT edit: `C:\Users\andre\.codex\backups\aoa\20260617_230916\en_us.snbt.pre_mechanical_prose_batch.bak`.

| # | Age | Quest/entry | File | Before | After | Severity |
|---|-----|-------------|------|--------|-------|----------|
| 1 | dark_ages | `70D99BC8FE5F6FC7` Hammock desc | `en_us.snbt` | pass the night | pass the day | WARN |
| 2 | dark_ages | `3CA98E14B6A82FF5` Hoglin Hide desc | `en_us.snbt` | Nether or early hoglins | reachable hoglins; Nether opens later | WARN |
| 3 | dark_ages | `dark_ages_manual.mechanics.water_weather_wounds.page1.text` | `en_us.json` | starts with a checkmark quest | starts with a Campfire quest | WARN |
| 4 | dark_ages | `dark_ages_manual.mechanics.water_weather_wounds.page2.text` | `en_us.json` | Leather Armor set requires five leather | Leather Armor quest requires a full armor set | WARN |
| 5 | medieval_times | `3B91163DE3DA885C` Nether Mine desc | `en_us.snbt` | worker trips into Nether, so you gain resources without going | worker-only MineColonies exception, not a portal or personal Nether unlock | WARN |
| 6 | medieval_times | `3B91163DE3DA885C` Nether Mine subtitle | `en_us.snbt` | Nether loot without the risk | A worker-only Nether route | WARN |
| 7 | the_renaissance | `0B0310100000CAFE` Cursed Trophy desc | `en_us.snbt` | pure bragging rights; not a path step | grants Apotheosis Frontier advancement | WARN |
| 8 | the_renaissance | `renaissance_compendium.welcome.where_you_are.page1.text` | `en_us.json` | eleven quest chapters | ten quest chapters | INFO |
| 9 | the_renaissance | `renaissance_compendium.mechanics.realm_proofs.page1.text` | `en_us.json` | each realm wants one proof item | access, survival, and grant-facing proof or return check | BLOCKER |
| 10 | the_renaissance | `renaissance_compendium.recipes.nether_route.page1.text` | `en_us.json` | Nether proof is Mundabitur Dust | proof is the Blaze Burner; Mundabitur is intermediate | BLOCKER |
| 11 | the_renaissance | `renaissance_compendium.loot.whats_open.page1.text` | `en_us.json` | Cursium never as loot | Cursium is not random/chest loot; it is a Maledictus boss proof | WARN |
| 12 | the_renaissance | `renaissance_compendium.capstone.leaving_renaissance.page1.text` | `en_us.json` | four required boss kills | major boss checks; not all direct capstone dependencies | WARN |
| 13 | the_renaissance | `renaissance_compendium.capstone.leaving_renaissance.page2.text` | `en_us.json` | Apotheosis Frontier in capstone reward chain | optional Cursed Trophy grants Apotheosis Frontier | WARN |
| 14 | gilded_age | `gilded_ledger.mechanics.infinite_grid.page2.text` | `en_us.json` | MEGA storage to 256M tier | storage cells to 64M here; 256M storage cells wait for Atomic | WARN |
| 15 | atomic | `4E44010000010001` Yellowcake desc | `en_us.snbt` | standard currency of every fuel line | standard currency of the main fission fuel lines | WARN |
| 16 | atomic | `4358010000010003` Chaos Gate desc | `en_us.snbt` | dawn, table, chain, soul, war, prophets | dawn, chain, soul, war, prophets | WARN |
| 17 | atomic | `5457011000000107` Hazard Payloads desc | `en_us.snbt` | stock chemical, contagious, infestive, debilitation, and condensive | stock any one payload from that set | WARN |
| 18 | atomic | `5457011000000108` Extremes desc | `en_us.snbt` | finish two extremes | craft either extreme | WARN |
| 19 | atomic | `4F43011000000111` Processing Ranks VII-IX desc | `en_us.snbt` | high ranks, ninth rung | any one high processing rank, seven through nine | WARN |
| 20 | atomic | `4F43011000000113` Speed Ranks VII-IX desc | `en_us.snbt` | finish speed ladder at rank nine | any one speed addon from ranks seven through nine | WARN |
| 21 | atomic | `4F43011000000115` Efficiency Ranks VII-IX desc | `en_us.snbt` | at rank nine | any one high efficiency rank, seven through nine | WARN |
| 22 | atomic | `4F43011000000117` Efficient Speed VII-IX desc | `en_us.snbt` | finish line at rank nine | any one efficient speed addon from ranks seven through nine | WARN |
| 23 | atomic | `4F43011000000119` Capacitor Ranks VII-IX desc | `en_us.snbt` | rank-nine buffer | any one high capacitor rank, seven through nine | WARN |
| 24 | atomic | `4F4301100000011B` Acceptor Ranks VI-IX desc | `en_us.snbt` | finish acceptor ladder at rank nine | any one acceptor addon from ranks six through nine | WARN |
| 25 | atomic | `atomic_dossier.mechanics.fuel_pipeline.description` | `en_us.json` | every reactor family | main fission families | WARN |
| 26 | atomic | `atomic_dossier.mechanics.fuel_pipeline.page1.text` | `en_us.json` | every fuel chain passes through yellowcake | main fission chains use yellowcake; thorium is separate | WARN |
| 27 | atomic | `atomic_dossier.capstone.chaos_convergence.page2.text` | `en_us.json` | dawn, table, chain, soul, war, choir | dawn, chain, soul, war, choir | WARN |
| 28 | ascension | `4252010000010001` Leviathan desc | `en_us.snbt` | keep Tidal Claws | defeat Leviathan for optional boss-route check | WARN |
| 29 | ascension | `4252010000010001` Leviathan subtitle | `en_us.snbt` | Boss fight and drop gate | Boss fight gate | WARN |
| 30 | ascension | `4252010000010007` Tremorzilla desc | `en_us.snbt` | keep Tremorzilla Egg | defeat Tremorzilla for optional boss-route check | WARN |
| 31 | ascension | `4252010000010007` Tremorzilla subtitle | `en_us.snbt` | Boss fight and drop gate | Boss fight gate | WARN |
| 32 | ascension | `4252010000010008` Ancient Hero desc | `en_us.snbt` | keep the boss drop | defeat Ancient Hero for optional boss-route check | WARN |
| 33 | ascension | `4252010000010008` Ancient Hero subtitle | `en_us.snbt` | Boss fight and drop gate | Boss fight gate | WARN |
| 34 | ascension | `4252010000010009` Infernal Dragon desc | `en_us.snbt` | keep the boss drop | defeat Infernal Dragon for optional boss-route check | WARN |
| 35 | ascension | `4252010000010009` Infernal Dragon subtitle | `en_us.snbt` | Boss fight and drop gate | Boss fight gate | WARN |
| 36 | ascension | `425201000001000A` Kraken desc | `en_us.snbt` | keep Kraken Tooth | defeat Kraken for optional boss-route check | WARN |
| 37 | ascension | `425201000001000A` Kraken subtitle | `en_us.snbt` | Boss fight and drop gate | Boss fight gate | WARN |
| 38 | ascension | `425201000001000B` Chaos Guardian desc | `en_us.snbt` | keep Chaos Shard for the stage flag | kill check awards the stage flags | WARN |
| 39 | ascension | `425201000001000B` Chaos Guardian subtitle | `en_us.snbt` | Boss fight and drop gate | Boss fight gate | WARN |
| 40 | otherworldly | `4256010000010006` Tidal Claws capstone desc/subtitle | `en_us.snbt` | Leviathan boss-drop wording | Otherworldly convergence capstone that turns in Tidal Claws and grants Ascension | WARN |

## Mechanical prose follow-up fixes - 2026-06-17
| # | Age | Quest/entry | File | Before | After | Severity |
|---|-----|-------------|------|--------|-------|----------|
| 41 | medieval_times | `6D7E8F901A2B1050` Great Hunt: Wroughtnaut desc | `en_us.snbt` | All-four grove mastery implication | Any three of four complete Grove mastery; Wroughtnaut is one valid proof | WARN |
| 42 | medieval_times | `6D7E8F901A2B1054` Master of the Grove desc/subtitle | `en_us.snbt` | All four implied; Renaissance grant/recovery hidden | At least three of four open the repeatable Renaissance grant; rerun after desync | BLOCKER |
| 43 | the_renaissance | `0B03107000000001` Archive and Recordkeeping desc | `en_us.snbt` | None of it gates progress | Complete Record is one Renaissance subproof for the age close | BLOCKER |
| 44 | the_renaissance | `0B0310A0000000F0` Cursium Ingot desc/subtitle | `en_us.snbt` | Optional/trophy-like Cursium wording | Cursium is the end-of-age proof that opens Industrial Revolution | BLOCKER |
| 45 | the_renaissance | `0B03105000000036` Infuser subtitle | `en_us.snbt` | Undergarden upgrade not marked optional | Optional: upgrade Undergarden gear | INFO |
| 46 | the_renaissance | `renaissance_compendium.mechanics.four_magics.description` | `en_us.json` | Four-magic action summary | Required starter chains across four magic mods | WARN |
| 47 | the_renaissance | `renaissance_compendium.mechanics.four_magics.page1.text` | `en_us.json` | One action from each magic mod | Required starter chains across Malum, Theurgy, Occultism, and F&A; subproof closes on Arcane Bone Meal | WARN |
| 48 | ascension | `4252010000010002`-`0006` boss-drop subtitles | `en_us.snbt` | Boss drop gate without optional marker | Optional: boss drop gate | INFO |
| 49 | atomic | `4F43010000010003` Magnetic Field desc/subtitle | `en_us.snbt` | Oritech proof seemed to hand the global chaos gate | Electronics/Oritech lane proof for the hangar itself | WARN |
| 50 | atomic | `atomic_dossier.capstone.chaos_convergence.description` | `en_us.json` | Ambiguous six-lane summary | Dawn, chain, soul, war, prophets, justice | WARN |
| 51 | atomic | `4E4401100000010B` Reinforced Hazmat desc | `en_us.snbt` | Full reinforced set implication | Any one reinforced hazmat armor piece completes the quest; full set advised before reactor-floor work | WARN |
| 52 | atomic | `4E4401100000010C` Alex's Caves Hazmat desc | `en_us.snbt` | Full Alex's Caves set implication | Any one Alex's Caves hazmat armor piece completes the quest; full set advised before cave radiation work | WARN |
| 53 | atomic | `4F43011000000110` Processing II-V desc | `en_us.snbt` | Low-band ladder implication | Any one processing addon from ranks two through five | WARN |
| 54 | atomic | `4F43011000000112` Speed II-V desc | `en_us.snbt` | Low-band ladder implication | Any one speed addon from ranks two through five | WARN |
| 55 | atomic | `4F43011000000114` Efficiency II-V desc | `en_us.snbt` | Low-band ladder implication | Any one efficiency addon from ranks two through five | WARN |
| 56 | atomic | `4F43011000000116` Efficient Speed II-VI desc | `en_us.snbt` | Low-band ladder implication | Any one efficient speed addon from ranks two through six | WARN |
| 57 | atomic | `4F43011000000118` Capacitor II-V desc | `en_us.snbt` | Low-band ladder implication | Any one capacitor addon from ranks two through five | WARN |
| 58 | atomic | `4F4301100000011A` Acceptor II-V desc | `en_us.snbt` | Low-band ladder implication | Any one acceptor addon from ranks two through five | WARN |

## Verification
- `snbt_guard.py --compare C:\Users\andre\.codex\backups\aoa\20260616_231503\en_us.snbt.20260616_231503.bak config\ftbquests\quests\lang\en_us.snbt` passed.
- `snbt_guard.py --compare C:\Users\andre\.codex\backups\aoa\20260617_230032\en_us.snbt.pre_ow6_fix.bak config\ftbquests\quests\lang\en_us.snbt` passed.
- `snbt_guard.py --compare C:\Users\andre\.codex\backups\aoa\20260617_230916\en_us.snbt.pre_mechanical_prose_batch.bak config\ftbquests\quests\lang\en_us.snbt` passed.
- `python -m json.tool kubejs\assets\aoa\lang\en_us.json` passed.
- `python tools\gen_chapter_truth_packets.py` regenerated `docs\audits\truth_packets_2026-06-17`.
- `python tools\quest_validate.py` and an independent DFS dependency check passed with 0 cycles.
- Regression grep across the edited source files found none of the targeted stale phrases.
- In-game FTBQuests round-trip is pending; the pack was not launched for this prose-only pass.
