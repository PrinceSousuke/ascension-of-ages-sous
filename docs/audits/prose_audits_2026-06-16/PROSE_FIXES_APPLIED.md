# Fixes applied - 2026-06-16

Current pass edits: 39 strings total, with 27 in `config/ftbquests/quests/lang/en_us.snbt` and 12 in `kubejs/assets/aoa/lang/en_us.json`.

Folded but not re-applied: `entering_the_iron_era.md` already records 4 WARN and 1 INFO, and `entering_the_iron_era.judgment.md` confirms those live strings are fixed, including the repeatability/desync line for `097AED7C91033D5E`.

Backup for the current SNBT batch: `C:\Users\andre\.codex\backups\aoa\20260616_231503\en_us.snbt.20260616_231503.bak`.

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

## Verification
- `snbt_guard.py --compare C:\Users\andre\.codex\backups\aoa\20260616_231503\en_us.snbt.20260616_231503.bak config\ftbquests\quests\lang\en_us.snbt` passed.
- `python -m json.tool kubejs\assets\aoa\lang\en_us.json` passed.
- Regression grep across the edited source files found none of the targeted stale phrases.
- In-game FTBQuests round-trip is pending; the pack was not launched for this prose-only pass.
