# Opus verification — GPT 5.5 prose audit (2026-06-16)

Verifier: Claude Opus 4.8 (independent pass). Verification date: 2026-06-17.
Scope: file-level mechanical verification of the 39 applied lang fixes + the 5 priority blocks (A–E). No in-game/runtime claims.

## Overall verdict
**SHIP**

Completion label: **VERIFIED**

All 39 applied fixes were independently confirmed against live SNBT/JSON and the named backup. The 27 SNBT edits diff exactly 1:1 against the backup `en_us.snbt.20260616_231503.bak` (27 changed lines, no others), each matching the PROSE_FIXES_APPLIED "after" text and the live task shape. The 12 JSON Modonomicon edits all show the corrected "after" text in the live `en_us.json`, which is valid JSON. The two Renaissance Modonomicon BLOCKERs (realm proofs / Nether route) are CONFIRMED against the live chapter SNBT: the Nether grant (`ren_nether_threshold_complete`) gates on a filled `create:blaze_burner` task — Mundabitur Dust is only an earlier reagent/icon — and the End grant gates on a return-to-overworld dimension task, exactly as the corrected prose now states. The regression grep for all pre-fix stale phrases is clean (the only non-zero hits are semantically-correct or intentionally-left-alone strings). GPT introduced no new false claims in the edited set. One WARN-level prose mislabel was found OUTSIDE the 39-fix scope (otherworldly capstone copy-paste); it is non-blocking, does not touch any applied fix, and is logged under Missed for a follow-up pass per the hard rules (a WARN does not authorize scope expansion). Because nothing GPT applied is wrong and both BLOCKERs are right, the applied batch is safe to ship.

## GPT self-check audit
| Check | Opus agrees? | Notes |
|-------|--------------|-------|
| `snbt_guard.py --compare` vs backup passed | Yes (re-derived) | Direct `diff` of backup vs live (CRLF-normalized) shows exactly 27 changed lines, all intended edits; no structural/format damage. |
| `python -m json.tool en_us.json` passed | Yes (re-ran) | `python -m json.tool` → JSON_VALID. Keys unchanged; only values edited. |
| CRLF / no BOM on `en_us.snbt` | Yes | `file` reports CRLF terminators; first 3 bytes `7b 0d 0a` (`{` + CRLF), no BOM. |
| Regression grep for stale phrases | Yes (re-ran) | All "before" phrases absent except benign/left-alone cases (see Block E + Phase 3). |
| In-game FTBQuests round-trip | Not run (agree) | Not claimed by GPT; not claimed by Opus. Pending. |

## Priority blocks (A–E)

### A. Renaissance BLOCKERs — both CONFIRMED
- **Fix #9 (`realm_proofs.page1`)** — CONFIRM. Live `ren_nether_threshold.snbt`: grant quest `0B03102000000062` rewards `/astages add {p} ren_nether_threshold_complete` and its task is `item: create:blaze_burner` (filled burner). Mundabitur Dust (`forbidden_arcanus:mundabitur_dust`) appears only as an earlier reagent task and as the grant reward's decorative icon — not the gating proof. Live `ren_end_threshold.snbt`: grant `0B03109000000060` (`ren_end_threshold_complete`) gates on a `type: "dimension"` / `minecraft:overworld` task = the return line, after the `minecraft:ender_dragon` kill earlier in the chapter. Live `ren_starlight_observation.snbt`: grant gates the chapter that contains the `eternal_starlight:the_gatekeeper` route. Corrected prose ("Nether closes on a Blaze Burner … End closes on the return line … Eternal Starlight closes on the Gatekeeper route") matches mechanics. **SHIP is not blocked.**
- **Fix #10 (`nether_route.page1`)** — CONFIRM. Same chapter evidence: the proof is the Blaze Burner; Mundabitur Dust is the F&A reagent step (and gates Deorum downstream). Corrected prose is exact.

### B. Atomic OR tasks — all CONFIRMED as OR/count-1 smart filters
Every spot-checked task is an `ftbfiltersystem:smart_filter` with `root(or(...))` and `count: 1` — i.e. ANY ONE member, never AND/all:
- `5457011000000107` (at5) → `or(chemical, contagious, infestive, debilitation, condensive)` → fix #17 "any one payload". CONFIRM.
- `5457011000000108` (at5) → `or(rejuvination, thermobaric)` → fix #18 "either extreme". CONFIRM.
- `4F43011000000111/113/115/117/119` → `or(tier_7, tier_8, tier_9)` count 1 (processing/speed/efficiency/efficient_speed/capacitor) → fixes #19–23. CONFIRM.
- `4F4301100000011B` → `or(acceptor tier_6..9)` count 1 → fix #24 "six through nine" (note the wider 6–9 band, correctly worded). CONFIRM.
- `4358010000010003` (at7 chaos gate) dependency list resolves to at1 dawn, at3 chain, at4 soul, at5 war, + two at7 prophet/Geburah steps — **no `at2_the_periodic_table` (table) dependency**. Fixes #16 & #27 ("dawn, chain, soul, war …"; table lane removed). CONFIRM.

### C. Ascension kill checks — CONFIRMED, leave-alone scope CORRECT
- `4252010000010001` (Leviathan): task is `type: "kill"`, `value: 1L`, `entity: cataclysm:the_leviathan` — pure kill check, no item turn-in. "keep Tidal Claws" correctly removed (fixes #28/#29). CONFIRM.
- `0007/0008/0009/000A` (Tremorzilla, Ancient Hero, Infernal Dragon, Kraken): packet + live show empty/`kill` tasks, no item turn-in → "keep …" removed (fixes #30–37). CONFIRM.
- `425201000001000B` (Chaos Guardian): task `entity: draconicevolution:draconic_guardian` (kill); rewards grant `asc_final_boss_convergence_complete` + `draconic_guardian_defeated`. Corrected prose "this kill check awards the stage flags" matches (fixes #38/#39). CONFIRM.
- Leave-alone `425601…`: `4252…`-vs-`4256…` distinction is correct. `4256010000010004`/`0006` ("Tidal Claws") are genuine **item/drop** gates (`item: cataclysm:tidal_claws`) in the otherworldly chapter, so GPT correctly did not convert their "keep" wording. CORRECT scope choice. (But see Missed — `4256010000010006`'s desc has a separate, unrelated copy-paste defect.)

### D. Folded Iron Era — still fixed (CLEAN)
- `097AED7C91033D5E` quest desc (en_us.snbt L231–233): "Turn in a &7Poor&r drafted Overgeared blueprint" + explicit desync/repeat recovery line. Not "any blueprint". Chapter task (entering_the_iron_era.snbt L392/L457) requires `overgeared:blueprint_data: { quality: "POOR" }` — prose matches NBT (hard rule satisfied).
- Modonomicon `capstone/leaving_dark_ages.page1`: "turn in a Poor-quality drafted blueprint" — no "any blueprint", no "checkmark".
- Modonomicon `recipes/entering_iron_era.page2`: "The final quest turns in a Poor-quality Overgeared blueprint" — no "checkmark" capstone lie.
All consistent with `entering_the_iron_era.judgment.md` (CLEAN).

### E. Zero-finding ages — skepticism pass
- `industrial_revolution` (401): NO CONFIDENT FINDINGS. High-risk chapters skimmed — IR capstone (`4954631000000000`, "Six proofs and a heart") matches its 6 lane-dependencies; magic-feedstock capstone matches its 5 lanes + turn-in; create-industrial-addons is a pure support chapter (no stage grants / OR filters / kill tasks, nothing to misstate); netherite/obsidilith boss-kill prose matches `type:"kill"` tasks. Zero-finding claim holds.
- `otherworldly` (32): ONE MISSED WARN (see Missed table). Zero-finding claim is *not* fully accurate, but the miss is cosmetic/non-blocking and unrelated to the 39 applied fixes.

## All 39 fixes
| # | Opus | Notes | Corrected text if TWEAK/REJECT |
|---|------|-------|--------------------------------|
| 1 | CONFIRM | SNBT L5508 "pass the night"→"pass the day"; Comforts `hammockUse=DAY`. | — |
| 2 | CONFIRM | SNBT Hoglin Hide; early-Nether implication removed; Nether is Renaissance-gated. | — |
| 3 | CONFIRM | JSON water_weather_wounds.page1 "Campfire quest"; no "checkmark". | — |
| 4 | CONFIRM | JSON page2 "Leather Armor quest requires a full armor set". | — |
| 5 | CONFIRM | SNBT Nether Mine desc; task `minecolonies:blockhutnetherworker` = worker-only exception. | — |
| 6 | CONFIRM | SNBT Nether Mine subtitle "A worker-only Nether route". | — |
| 7 | CONFIRM | SNBT Cursed Trophy desc; quest `0B0310100000CAFE` grants `apotheosis:progression/frontier`. | — |
| 8 | CONFIRM | JSON renaissance "ten quest chapters"; index lists 10 renaissance chapters. | — |
| 9 | CONFIRM (BLOCKER) | JSON realm_proofs; Blaze Burner / return line / Gatekeeper — all verified live. | — |
| 10 | CONFIRM (BLOCKER) | JSON nether_route; proof = Blaze Burner, Mundabitur = intermediate. Verified live. | — |
| 11 | CONFIRM | JSON loot "Cursium … is a Maledictus boss proof", not chest loot. Vigil drops `cataclysm:cursium_ingot`. | — |
| 12 | CONFIRM | JSON capstone.page1 "major boss checks", not "four required boss kills". | — |
| 13 | CONFIRM | JSON capstone.page2 "optional Cursed Trophy grants Apotheosis Frontier"; quest is `optional:true` + frontier grant. | — |
| 14 | CONFIRM | JSON infinite_grid.page2 "64M storage cells here; 256M … wait for Atomic; 256M crafting CPUs present". | — |
| 15 | CONFIRM | SNBT Yellowcake "main fission fuel lines"; thorium is a side path. | — |
| 16 | CONFIRM | SNBT chaos gate desc; "table" lane removed; deps have no at2 dependency. | — |
| 17 | CONFIRM | SNBT 107; `or(...)` 5-shell smart filter, count 1 → "any one payload". | — |
| 18 | CONFIRM | SNBT 108; `or(rejuvination, thermobaric)` count 1 → "either extreme". | — |
| 19 | CONFIRM | SNBT 111; `or(processing 7/8/9)` count 1. | — |
| 20 | CONFIRM | SNBT 113; `or(speed 7/8/9)` count 1. | — |
| 21 | CONFIRM | SNBT 115; `or(efficiency 7/8/9)` count 1. | — |
| 22 | CONFIRM | SNBT 117; `or(efficient_speed 7/8/9)` count 1. | — |
| 23 | CONFIRM | SNBT 119; `or(capacitor 7/8/9)` count 1. | — |
| 24 | CONFIRM | SNBT 11B; `or(acceptor 6/7/8/9)` count 1; "six through nine" correct. | — |
| 25 | CONFIRM | JSON fuel_pipeline.description "main fission families". | — |
| 26 | CONFIRM | JSON fuel_pipeline.page1 "main fission chains use yellowcake; thorium separate". | — |
| 27 | CONFIRM | JSON chaos_convergence.page2 "dawn, chain, soul, war, choir"; no "table". | — |
| 28 | CONFIRM | SNBT Leviathan desc; task `type:"kill" cataclysm:the_leviathan`, no item turn-in. | — |
| 29 | CONFIRM | SNBT Leviathan subtitle "Boss fight gate". | — |
| 30 | CONFIRM | SNBT Tremorzilla desc; kill check. | — |
| 31 | CONFIRM | SNBT Tremorzilla subtitle. | — |
| 32 | CONFIRM | SNBT Ancient Hero desc; kill check. | — |
| 33 | CONFIRM | SNBT Ancient Hero subtitle. | — |
| 34 | CONFIRM | SNBT Infernal Dragon desc; kill check. | — |
| 35 | CONFIRM | SNBT Infernal Dragon subtitle. | — |
| 36 | CONFIRM | SNBT Kraken desc; kill check. | — |
| 37 | CONFIRM | SNBT Kraken subtitle. | — |
| 38 | CONFIRM | SNBT Chaos Guardian desc; kill awards `asc_final_boss_convergence_complete` + `draconic_guardian_defeated`. | — |
| 39 | CONFIRM | SNBT Chaos Guardian subtitle "Boss fight gate". | — |

Totals: **39 CONFIRM / 0 TWEAK / 0 REJECT.**

## Missed issues
| Location | Severity | Evidence | Suggested fix |
|----------|----------|----------|----------------|
| otherworldly — `ow6_beyond_the_veil.snbt`, quest `4256010000010006` ("Tidal Claws"), prose at `en_us.snbt` L2445–2446 | WARN | Prose is a verbatim copy of the sibling Leviathan boss quest (`4256010000010004`, L2439): `"Find The Leviathan at its arena, prepare for the fight, and keep Tidal Claws for the stage flag."` / subtitle `"Boss drop gate."` But this quest is the **otherworldly→ascension convergence capstone**: `shape:"gear"`, `size:1.6`, **7 dependencies across all six OW chapters** (L430–437), and rewards grant `ow_capstone_complete`, `/astages add {p} ascension`, and `aoa:age/ascension` (L448/460/472). The `cataclysm:tidal_claws` turn-in is real, so WARN not BLOCKER, but the description hides the convergence + the `ascension` grant. | Rewrite desc to reflect the convergence, e.g. `["Converge every Otherworldly lane and seal the run by turning in &bTidal Claws&r. This capstone grants the &dAscension&r stage."]`; subtitle e.g. `"Otherworldly capstone — grants Ascension."` (NOT applied — outside the 39-fix scope; WARN does not authorize scope expansion this pass.) |

GPT's "0 findings for otherworldly" is therefore slightly overstated by one WARN. It does not affect any applied fix and is non-blocking.

## Coverage accounting
| Question | Result |
|----------|--------|
| Quests reviewed | 1,806 — index.json ages[] sum: 48+265+406+401+348+264+32+42 = 1,806. CONFIRMED. |
| Fixes applied | 39 (27 SNBT + 12 JSON). CONFIRMED — 27 SNBT diff lines + 12 JSON keys edited. |
| BLOCKERs fixed | 2 (Renaissance realm_proofs + nether_route). Both CONFIRMED live. |
| WARNs fixed | 30 (current pass) + folded Iron Era (4 WARN) verified separately. |
| INFO fixed | 1 (renaissance "eleven"→"ten" chapters). CONFIRMED. |
| Unfixed BLOCKER/WARN without Deferred | Applied-scope: 0. Newly discovered: 1 WARN (OW6 capstone copy-paste), logged in Missed for a follow-up pass — not a regression of GPT's work. |

## Pending (not Opus scope)
- In-game FTBQuests round-trip: **NOT VERIFIED** (pack not launched; file-level verification only).
- OW6 capstone WARN: not corrected this pass (out of the 39-fix scope; WARN, not BLOCKER).

## Commit recommendation
Files safe to commit:
- docs/audits/prose_audits_2026-06-16/PROSE_AUDIT_FULL.md
- docs/audits/prose_audits_2026-06-16/PROSE_FIXES_APPLIED.md
- docs/audits/prose_audits_2026-06-16/OPUS_VERIFY_PROSE_AUDIT.md
- config/ftbquests/quests/lang/en_us.snbt
- kubejs/assets/aoa/lang/en_us.json

Suggested message:
Fix quest and modonomicon prose to match mechanical truth (39 strings, 8 ages)

Follow-up (separate, optional): correct the OW6 `4256010000010006` capstone description (WARN) so it no longer reuses the Leviathan boss-drop text.
