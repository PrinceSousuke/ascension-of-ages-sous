# Full pack prose audit - 2026-06-16

## Executive summary
- Status: AUDIT_COMPLETE
- Total quests reviewed: 1,806 across 8 age packets and 54 chapters.
- Truth source: `docs/audits/truth_packets_2026-06-16/ages/*.json`, with live fallback to `config/ftbquests/quests/lang/en_us.snbt`, `kubejs/assets/aoa/lang/en_us.json`, and chapter SNBT only where packet fields were missing or ambiguous.
- Existing Dark Ages audit folded: `entering_the_iron_era.md` and `entering_the_iron_era.judgment.md` cover the 4 WARN / 1 INFO Iron Era findings; they are not duplicated below.
- Fixes applied in this pass: 40 current string edits (28 quest-lang SNBT strings, 12 Modonomicon JSON strings). Folded Iron Era fixes were verified live, not re-applied.
- Mechanical prose follow-up: `MECHANICAL_PROSE_VALIDATION_2026-06-17.md` records a second all-age pass for player-facing mechanical truth. It applied 25 additional targeted field edits (22 SNBT lang fields, 3 Modonomicon JSON fields), regenerated `docs/audits/truth_packets_2026-06-17/`, and found no required chapter, recipe, loot, stage, or KubeJS behavior changes.
- Deferred mechanical fixes: 0. No confirmed finding required chapter SNBT, KubeJS logic, recipe, task, or reward changes.

| Age | Quests | BLOCKER | WARN | INFO |
|-----|--------|---------|------|------|
| dark_ages | 48 | 0 | 8 | 1 |
| medieval_times | 265 | 0 | 1 | 1 |
| the_renaissance | 406 | 2 | 4 | 1 |
| industrial_revolution | 401 | 0 | 0 | 0 |
| gilded_age | 348 | 0 | 1 | 0 |
| atomic | 264 | 0 | 12 | 0 |
| otherworldly | 32 | 0 | 1 | 0 |
| ascension | 42 | 0 | 6 | 0 |
| Total | 1,806 | 2 | 33 | 3 |

## dark_ages
### Summary
48 quests reviewed. Existing Iron Era findings were folded from the chapter audit; additional issues were in survival/comfort prose and Modonomicon survival pages.

### Findings table
| Quest ID | Chapter | Field | Severity | Excerpt | Mechanical truth | Fix applied? |
|----------|---------|-------|----------|---------|------------------|--------------|
| `entering_the_iron_era.md` | `entering_the_iron_era.snbt` | quest + Modonomicon prose | WARN/INFO folded | Poor blueprint, checkmark, optional-polishing, and repeatability wording | Chapter audit found 4 WARN / 1 INFO; judgment file confirms live strings are already fixed. | Verified live; not duplicated here. |
| `70D99BC8FE5F6FC7` | `stone_water_weather_and_wounds.snbt` | `quest_desc` | WARN | Hammock lets you "pass the night" | Comforts config has `hammockUse = "DAY"`. | Yes. Changed to pass the day. |
| `3CA98E14B6A82FF5` | `stone_water_weather_and_wounds.snbt` | `quest_desc` | WARN | Hoglin Hide comes from the Nether or hoglins reachable early | Nether access is a Renaissance gate unless a live task proves otherwise. | Yes. Removed early-Nether implication. |
| Modonomicon | `dark_ages_manual.mechanics.water_weather_wounds` | `page1.text` | WARN | Chapter starts with a checkmark quest | The chapter starts with the Campfire item task. | Yes. Changed to Campfire quest. |
| Modonomicon | `dark_ages_manual.mechanics.water_weather_wounds` | `page2.text` | WARN | Leather Armor set requires five leather | Live quest tasks require boots, chestplate, leggings, and helmet. | Yes. Changed to full armor set. |

### Capstone / grants
`097AED7C91033D5E` grants `medieval_times`, `apotheosis:progression/haven`, and `aoa:age/medieval_times`; live prose now says the capstone turns in a Poor-quality Overgeared blueprint and includes repeatability/desync recovery wording.

### Modonomicon
The Dark Ages Manual now matches live chapter mechanics for Iron Era and water/weather/wounds. The packet's Modonomicon page arrays were incomplete, so live `kubejs/assets/aoa/lang/en_us.json` was the fallback source.

### Cross-chapter themes
No new Dark Ages lock or task contradictions were found beyond the folded Iron Era findings and the two survival-page issues fixed here.

## medieval_times
### Summary
265 quests reviewed. One MineColonies wording issue was fixed in the first pass. The 2026-06-17 mechanical follow-up also corrected Grove wording so players see that any three of the four beast proofs open the repeatable Renaissance grant.

### Findings table
| Quest ID | Chapter | Field | Severity | Excerpt | Mechanical truth | Fix applied? |
|----------|---------|-------|----------|---------|------------------|--------------|
| `3B91163DE3DA885C` | `minecolonies.snbt` | `quest_desc`, `quest_subtitle` | WARN | "Nether loot without the risk" and worker trips into Nether | Task is `minecolonies:blockhutnetherworker`; this is a worker-only MineColonies exception, not personal Nether access. | Yes. |
| `6D7E8F901A2B1050` | `what_waits_in_the_grove.snbt` | `quest_desc` | WARN follow-up | "All four" style mastery implication | Live Grove mastery needs any three of four beast proofs. | Yes, in 2026-06-17 mechanical follow-up. |
| `6D7E8F901A2B1054` | `what_waits_in_the_grove.snbt` | `quest_desc`, `quest_subtitle` | BLOCKER follow-up | All-four implication; hidden Renaissance repeatable grant | Grant quest has 4 deps, `min_required_dependencies: 3`, `can_repeat: true`, and grants Renaissance. | Yes, in 2026-06-17 mechanical follow-up. |

### Capstone / grants
The grove capstone grants the next stage and is repeatable for recovery. Follow-up prose now states the three-of-four requirement and desync recovery behavior.

### Modonomicon
Medieval Codex entries matched the age packet after the Nether Mine clarification.

### Cross-chapter themes
The main risk was Nether phrasing in a Medieval colony utility quest. That has been narrowed to a worker-only exception.

## the_renaissance
### Summary
406 quests reviewed. The largest first-pass issue cluster was Modonomicon prose that described realm proofs and capstone rewards differently from the age packet. The 2026-06-17 mechanical follow-up fixed additional Archive, Cursium, Infuser, and Four Magics clarity issues.

### Findings table
| Quest ID | Chapter | Field | Severity | Excerpt | Mechanical truth | Fix applied? |
|----------|---------|-------|----------|---------|------------------|--------------|
| `0B0310100000CAFE` | `ren_maledictus_vigil.snbt` | `quest_desc` | WARN | Trophy is "pure bragging rights" and "rather than a step" | Quest grants `apotheosis:progression/frontier`. | Yes. |
| Modonomicon | `renaissance_compendium.mechanics.realm_proofs` | `page1.text` | BLOCKER | Nether wants Mundabitur Dust; End and Starlight want sample items | Nether grant closes on Blaze Burner; End closes on the return line; Starlight closes on the Gatekeeper route. | Yes. |
| Modonomicon | `renaissance_compendium.recipes.nether_route` | `page1.text` | BLOCKER | Nether Threshold proof is Mundabitur Dust | Mundabitur Dust is an intermediate reagent; proof is the Blaze Burner. | Yes. |
| Modonomicon | `renaissance_compendium.loot.whats_open` | `page1.text` | WARN | Cursium is "boss proof only, never as loot" | Cursium is a Maledictus boss drop/proof, not random/chest loot. | Yes. |
| Modonomicon | `renaissance_compendium.capstone.leaving_renaissance` | `page1.text` | WARN | Four boss kills are required for the Vigil/capstone | Frostmaw and Nightmare Stalker are age content, but not direct capstone dependency proofs. | Yes. |
| Modonomicon | `renaissance_compendium.capstone.leaving_renaissance` | `page2.text` | WARN | Apotheosis Frontier is in the capstone reward chain | Optional Cursed Trophy grants Apotheosis Frontier; capstone grants Industrial Revolution chain. | Yes. |
| Modonomicon | `renaissance_compendium.welcome.where_you_are` | `page1.text` | INFO | Renaissance has eleven quest chapters | Packet and index list ten Renaissance chapters. | Yes, low-risk fact fix. |
| `0B03107000000001` | `ren_archive_recordkeeping.snbt` | `quest_desc` | BLOCKER follow-up | "None of it gates your progress" | Complete Record is a Renaissance subproof for the age close. | Yes, in 2026-06-17 mechanical follow-up. |
| `0B0310A0000000F0` | `ren_capstone_weave.snbt` | `quest_desc`, `quest_subtitle` | BLOCKER follow-up | Optional/trophy-like Cursium wording | Cursium Ingot is the end-of-age proof that opens Industrial Revolution. | Yes, in 2026-06-17 mechanical follow-up. |
| `0B03105000000036` | `ren_undergarden_threshold.snbt` | `quest_subtitle` | INFO follow-up | Missing optional marker | Quest is optional Undergarden gear depth. | Yes, in 2026-06-17 mechanical follow-up. |
| Modonomicon | `renaissance_compendium.mechanics.four_magics` | `description`, `page1.text` | WARN follow-up | One-action-per-magic-mod implication | Live flow requires starter chains across four magic mods and closes on Arcane Bone Meal. | Yes, in 2026-06-17 mechanical follow-up. |

### Capstone / grants
The Renaissance capstone chain is now described as the ten subproofs plus Cursium Ingot detect, granting Renaissance Seal, Industrial Revolution, and the AoA Industrial Revolution advancement. Apotheosis Frontier is now assigned to optional Cursed Trophy. Follow-up prose now also names Cursium Ingot as the end-of-age proof rather than an optional trophy.

### Modonomicon
Realm-proof pages now distinguish access, survival, and grant-facing proof/return checks rather than treating every dimension as a simple proof-item hand-in.

### Cross-chapter themes
Renaissance prose tended to compress "important age content" into "required capstone proof." The fixes preserve the content list while separating optional/depth content from hard grant requirements.

## industrial_revolution
### Summary
401 quests reviewed. No confident BLOCKER, WARN, or INFO findings survived age-packet and live-source reconciliation.

### Findings table
| Quest ID | Chapter | Field | Severity | Excerpt | Mechanical truth | Fix applied? |
|----------|---------|-------|----------|---------|------------------|--------------|
| - | - | - | - | No findings. | - | - |

### Capstone / grants
Seven grants reviewed; no later-stage lock conflicts or grant prose contradictions were confirmed.

### Modonomicon
No Industrial book is listed in the age packet.

### Cross-chapter themes
No required action.

## gilded_age
### Summary
348 quests reviewed. One Modonomicon storage-tier statement overreached into Atomic content.

### Findings table
| Quest ID | Chapter | Field | Severity | Excerpt | Mechanical truth | Fix applied? |
|----------|---------|-------|----------|---------|------------------|--------------|
| Modonomicon | `gilded_ledger.mechanics.infinite_grid` | `page2.text` | WARN | MEGA Cells raises storage to 256M tier | Gilded storage-cell quests cap at 64M; 256M item/fluid/chemical cells wait for Atomic. 256M crafting storage is present in Gilded. | Yes. |

### Capstone / grants
Eight grants reviewed; no grant prose contradiction was confirmed.

### Modonomicon
Gilded Ledger now distinguishes 64M storage cells from 256M crafting storage.

### Cross-chapter themes
No additional Gilded issues beyond avoiding Atomic-tier storage-cell claims.

## atomic
### Summary
264 quests reviewed. Issues clustered around OR-task prose: several descriptions implied all listed items or rank-nine completion when the actual task accepted any one member of a set. The 2026-06-17 mechanical follow-up extended this to low-band Oritech rank quests and hazmat armor piece gates.

### Findings table
| Quest ID | Chapter | Field | Severity | Excerpt | Mechanical truth | Fix applied? |
|----------|---------|-------|----------|---------|------------------|--------------|
| `4E44010000010001` | `at1_nuclear_dawn.snbt` | `quest_desc` | WARN | Yellowcake is the currency of every fuel line | Main fission lines use yellowcake; Create: New Age thorium is a side path. | Yes. |
| `4358010000010003` | `at7_chaos_convergence.snbt` | `quest_desc` | WARN | Requires dawn, table, chain, soul, war, and prophets | Live dependencies include dawn, chain, soul, war, Baal chain, and Geburah; no periodic-table lane dependency. | Yes. |
| `5457011000000107` | `at5_threshold_of_war.snbt` | `quest_desc` | WARN | Stock all five hazard payloads | Smart-filter task is OR over chemical, contagious, infestive, debilitation, and condensive shells. | Yes. |
| `5457011000000108` | `at5_threshold_of_war.snbt` | `quest_desc` | WARN | Finish two extremes | Smart-filter task is OR over rejuvination or thermobaric shell. | Yes. |
| `4F43011000000111`, `113`, `115`, `117`, `119`, `11B` | `atomic_oritech_convergence.snbt` | `quest_desc` | WARN | Rank-nine or full-ladder completion language | Live smart filters accept one high-rank addon from the listed band. | Yes. |
| Modonomicon | `atomic_dossier.mechanics.fuel_pipeline` | `description`, `page1.text` | WARN | Every fuel chain passes through yellowcake | Main fission chains use yellowcake; Create: New Age thorium is separate. | Yes. |
| Modonomicon | `atomic_dossier.capstone.chaos_convergence` | `page2.text` | WARN | Convergence requires dawn, table, chain, soul, war, and choir | Same dependency truth as `4358010000010003`; no table lane requirement. | Yes. |
| `4F43010000010003` | `atomic_oritech_convergence.snbt` | `quest_desc`, `quest_subtitle` | WARN follow-up | Oritech proof appeared to hand the global chaos gate | Magnetic Field proves the Oritech hangar/lane itself, not the whole chaos gate. | Yes, in 2026-06-17 mechanical follow-up. |
| `4E4401100000010B`, `4E4401100000010C` | `at1_nuclear_dawn.snbt` | `quest_desc` | WARN follow-up | Hazmat prose could imply full-set completion for an OR task | Live filters accept any one armor piece; full sets are advice for radiation work. | Yes, in 2026-06-17 mechanical follow-up. |
| `4F43011000000110`, `112`, `114`, `116`, `118`, `11A` | `atomic_oritech_convergence.snbt` | `quest_desc` | WARN follow-up | Low-band rank prose implied full rank ladders | Live filters accept any one addon from the listed low-rank band. | Yes, in 2026-06-17 mechanical follow-up. |
| Modonomicon | `atomic_dossier.capstone.chaos_convergence` | `description` | WARN follow-up | Summary hid the live dependency themes | Live themes are dawn, chain, soul, war, prophets, and justice. | Yes, in 2026-06-17 mechanical follow-up. |

### Capstone / grants
Atomic grants were checked against dependency lanes and stage grants. Chaos Convergence now lists the required lanes without inserting the periodic-table lane.

### Modonomicon
Atomic Dossier now separates main fission yellowcake from the thorium side path and mirrors the corrected convergence dependency list.

### Cross-chapter themes
OR-filter prose was the recurring issue. Fixed strings now say "any one," "either," or "one high rank" where the task accepts alternatives.

## otherworldly
### Summary
32 quests reviewed. The follow-up verification found one OW6 capstone copy-paste issue; the live lang now names it as the Otherworldly-to-Ascension capstone.

### Findings table
| Quest ID | Chapter | Field | Severity | Excerpt | Mechanical truth | Fix applied? |
|----------|---------|-------|----------|---------|------------------|--------------|
| `4256010000010006` | `ow6_beyond_the_veil.snbt` | `quest_desc`, `quest_subtitle` | WARN | Reused the sibling Leviathan boss-drop wording | This quest is the Otherworldly convergence capstone: seven lane dependencies, `cataclysm:tidal_claws` item task, and rewards granting `ow_capstone_complete`, `ascension`, and `aoa:age/ascension`. | Yes. |

### Capstone / grants
Eight grants reviewed; the OW6 capstone now explicitly says it grants Ascension.

### Modonomicon
No Otherworldly book is listed in the age packet.

### Cross-chapter themes
Keep `425601...` Otherworldly item/drop gates distinct from `425201...` Ascension kill-check boss routes.

## ascension
### Summary
42 quests reviewed. One repeated optional-boss wording pattern described drop hand-ins where the live tasks are kill checks.

### Findings table
| Quest ID | Chapter | Field | Severity | Excerpt | Mechanical truth | Fix applied? |
|----------|---------|-------|----------|---------|------------------|--------------|
| `4252010000010001`, `0007`, `0008`, `0009`, `000A`, `000B` | `asc6_bosses_rise.snbt` | `quest_desc`, `quest_subtitle` | WARN | Keep Tidal Claws, Tremorzilla Egg, boss drop, Kraken Tooth, or Chaos Shard | Live tasks are kill checks for those six optional boss-route quests; Chaos Guardian kill grants the stage flags. | Yes. |
| `4252010000010002` through `4252010000010006` | `asc6_bosses_rise.snbt` | `quest_subtitle` | INFO follow-up | Boss-drop item gates did not clearly advertise optional status. | These are optional boss-drop item gates, distinct from the kill-check routes and the Otherworldly capstone. | Yes, in 2026-06-17 mechanical follow-up. |

### Capstone / grants
Seven grants reviewed. The Chaos Guardian optional boss-route quest now says the kill check awards stage flags instead of implying a Chaos Shard hand-in.

### Modonomicon
No Ascension book is listed in the age packet.

### Cross-chapter themes
The `425201...` Ascension boss routes are kill-check quests; the `425601...` Otherworldly Tidal Claws capstone is an item turn-in plus stage grant, so its prose now names the convergence rather than repeating the sibling Leviathan fight wording.

## Cross-age themes
- Exact task shape matters. Several prose strings described all-list completion where live smart filters were OR conditions.
- Grant prose should mention recovery repeatability only where useful. The Iron Era grant now does; other INFO-only repeatability notes were not expanded without a stronger player-facing need.
- Modonomicon summaries age quickly when they compress a chapter into one "proof item." The Renaissance realm-proof pages had the biggest drift.
- Stage-gate wording must not imply early dimension access. Medieval Nether Mine prose now names the worker-only exception.

## Deferred mechanical fixes
None confirmed. All BLOCKER/WARN findings in this report were lang-only prose fixes in `config/ftbquests/quests/lang/en_us.snbt` or `kubejs/assets/aoa/lang/en_us.json`.

## Verification notes
- External SNBT backup used for the current batch: `C:\Users\andre\.codex\backups\aoa\20260616_231503\en_us.snbt.20260616_231503.bak`.
- OW6 follow-up SNBT backup: `C:\Users\andre\.codex\backups\aoa\20260617_230032\en_us.snbt.pre_ow6_fix.bak`.
- Mechanical prose follow-up SNBT backup: `C:\Users\andre\.codex\backups\aoa\20260617_230916\en_us.snbt.pre_mechanical_prose_batch.bak`.
- `snbt_guard.py --compare` passed for the edited SNBT file against both listed backups at their respective edit points.
- `python -m json.tool kubejs/assets/aoa/lang/en_us.json` passed.
- `python tools/gen_chapter_truth_packets.py` regenerated `docs/audits/truth_packets_2026-06-17/` after the mechanical prose follow-up.
- `python tools/quest_validate.py` and an independent DFS dependency check found no broken dependency refs, self-deps, missing-item tasks, or cycles.
- Regression grep across the edited source files found none of the stale phrases targeted by this pass.
- In-game FTBQuests round-trip is pending; this pass did not launch the pack.
