# Gilded + Atomic Quest Rewrite Plan - 2026-06-24

## 1. Status

DONE_WITH_CONCERNS

This is a read-only evidence pass plus this report. I did not edit live SNBT, lang, KubeJS, or Modonomicon book files. Live files win over older audit docs in all conclusions below.

## 2. Files Inspected And File Written

Read:

- `AGENTS.md`
- `kubejs/AGENTS.md`
- `config/ftbquests/quests/chapters/g1_the_golden_workshop.snbt`
- `config/ftbquests/quests/chapters/g2_the_refinery.snbt`
- `config/ftbquests/quests/chapters/g4_the_infinite_grid.snbt`
- `config/ftbquests/quests/chapters/g5_empire_of_iron.snbt`
- `config/ftbquests/quests/chapters/g6_circuits_and_current.snbt`
- `config/ftbquests/quests/chapters/g7_chartered_arcana.snbt`
- `config/ftbquests/quests/chapters/g_power_beyond_wires.snbt`
- `config/ftbquests/quests/chapters/at1_nuclear_dawn.snbt`
- `config/ftbquests/quests/chapters/at2_the_periodic_table.snbt`
- `config/ftbquests/quests/chapters/at3_chain_reaction.snbt`
- `config/ftbquests/quests/chapters/at4_machine_soul.snbt`
- `config/ftbquests/quests/chapters/at5_threshold_of_war.snbt`
- `config/ftbquests/quests/chapters/at7_chaos_convergence.snbt`
- `config/ftbquests/quests/chapters/atomic_oritech_convergence.snbt`
- `config/ftbquests/quests/chapters/ow3_dragon_technology.snbt`
- `config/ftbquests/quests/chapters/asc3_the_impossible_machine.snbt`
- `config/ftbquests/quests/lang/en_us.snbt`
- `kubejs/assets/aoa/lang/en_us.json`
- `kubejs/data/aoa/**`
- `kubejs/server_scripts/aoa_astages_00_register_stages.js`
- `kubejs/server_scripts/aoa_astages_*.js`
- `kubejs/server_scripts/aoa_recipes_gilded_weaves.js`
- `kubejs/server_scripts/aoa_recipes_atomic_weaves.js`
- `kubejs/server_scripts/aoa_recipes_oritech_weaves.js`
- `docs/audits/prose_audits_2026-06-16/*`
- `docs/audits/sweep_2026-06-18/*`
- `progression/` search targets

Written:

- `docs/Evidence/Current/GILDED_ATOMIC_QUEST_REWRITE_PLAN_2026-06-24.md`

## 3. Gilded Findings

### BLOCKER: Chartered Arcana optional flag/prose contradict required capstone mechanics

Live mechanics:

- `g7_chartered_arcana.snbt`
  - `4341011000000001` / "Book of Binding Afrit" has `optional: true`.
  - `4341011000000002` / "Reformation Result Pedestal" has `optional: true`.
  - `4341011000000003` / "Spirit Catalyzer" has `optional: true`.
  - `4341011000000004` / "Spirit Instiller" depends on all three above and rewards `/astages add {p} g_magic_authorization_complete true true`.
- `g_power_beyond_wires.snbt`
  - `5057011000000004` / "Atomic Disassembler" depends on `4341011000000004`.
- `aoa_astages_00_register_stages.js`
  - Registers `g_magic_authorization_complete`.

Current player-facing text:

- `quest.4341011000000001.quest_subtitle`: "Optional: a hotter contract."
- `quest.4341011000000002.quest_subtitle`: "Optional: the array, complete."
- `quest.4341011000000003.quest_subtitle`: "Optional: hotter focusing."
- `quest.4341011000000004.quest_desc`: "The earlier magic quests are optional branches, but this capstone is a hard dependency of the atomic age grant."
- `book.aoa.gilded_ledger.mechanics.chartered_arcana.page1.text`: "Afrit binding, the Theurgy reformation array, Malum's spirit catalyzer, and Spectrum's spirit instiller converge into the magic authorization proof required by the Atomic Disassembler handoff."

Recommended patch intent:

- Treat the live dependency graph and book as authority: Chartered Arcana is required for the Atomic Disassembler handoff.
- Remove `optional: true` from `4341011000000001`, `4341011000000002`, and `4341011000000003`, or if design intentionally wants them optional, then change `4341011000000004` dependencies and the Atomic Disassembler fan-in. The lower-risk fix is to make the three prerequisite quests non-optional.
- Update `en_us.snbt`:
  - `4341011000000001.quest_subtitle`: "Required: a hotter contract."
  - `4341011000000002.quest_subtitle`: "Required: the array, complete."
  - `4341011000000003.quest_subtitle`: "Required: hotter focusing."
  - `4341011000000004.quest_desc`: replace the "earlier magic quests are optional branches" sentence with "The earlier magic quests are required steps in the authorization chain, and this capstone is a hard dependency of the atomic age grant."

### WARN: Power Beyond Wires has optional-title debt on many optional Astral branch quests

Live mechanics:

- `g_power_beyond_wires.snbt` marks many Astral side quests optional, including `5057011000000102`, `0104`, `0109`-`011C`, `011E`, and boss side quests `5057011000000005`-`0008`.
- Required Gilded/Atomic spine in the same chapter is clear:
  - `5057011000000001` "Astral Dimension" opens the dimension.
  - `5057011000000002` "Astranite Ingot" is required.
  - `5057011000000003` "Void Titan" rewards `void_titan_defeated` and `g_temporal_authorization_complete`.
  - `5057011000000004` "Atomic Disassembler" grants `atomic`.

Current player-facing text:

- Optional bosses are mostly clear in body text, for example `5057011000000005` says "It guards nothing you strictly need."
- Many optional collection/crafting side quests do not mark optional status in the subtitle, for example:
  - `5057011000000102.quest_subtitle`: "Obtain an Astranite Block."
  - `5057011000000109.quest_subtitle`: "Collect the full astranite toolset."
  - `505701100000010A.quest_subtitle`: "Collect the full astranite armor set."
  - `505701100000011B.quest_subtitle`: "Obtain a Supreme Helmet."

Recommended patch intent:

- Do not rewrite the whole Astral branch. Keep it dense and useful.
- Add "Optional:" to subtitles for optional non-spine Astral collection/crafting/boss quests where the live SNBT has `optional: true`.
- Do not add spawn or structure-location claims unless verified from live structure configs or jars.

### WARN: Gilded book covers systems but still underserves "structures" as a player guidance category

Evidence:

- `book.aoa.gilded_ledger` covers Golden Workshop, Infinite Grid, Data Economy, Oceanic Industry, Chartered Arcana, Heavy Industry, Silicon Chain, and Power Beyond Wires.
- `g_power_beyond_wires.snbt` covers Astral Dimension, Astral Stone, ore/metals, templates, bosses, and loot-like collectibles, but there is no dedicated Gilded Modonomicon structures/loot entry analogous to earlier age books.
- `rg "Yggdrasil|yggdrasil"` returned no live quest/book hits in the inspected live quest/lang/book surfaces.

Recommended patch intent:

- Add one Gilded Ledger entry under `kubejs/data/aoa/modonomicon/books/gilded_ledger/entries/...` and matching `kubejs/assets/aoa/lang/en_us.json` keys for Astral exploration and structure caution.
- Suggested design text, conservative:
  - "Astral exploration is part of Gilded, but the questbook only requires the route to Astral, core materials, the Void Titan, and the Atomic Disassembler handoff. Treat side bosses, templates, presents, and equipment sets as optional mastery unless their quest says otherwise."
- Only mention Yggdrasil if the main agent verifies a live mod/structure/item/source path. I did not verify it locally.

### INFO: Rolling Mill missing-lang concern appears resolved in current live lang

Evidence:

- `config/ftbquests/quests/lang/en_us.snbt`
  - `quest.7A1F050000000005.*` exists for Medieval "Rolling Mill".
  - `quest.495405100000000D.*` exists for IR "Rolling Mill".

No Gilded/Atomic patch needed unless the main agent is doing a separate duplicate ownership pass.

## 4. Atomic Findings

### WARN: Atomic continuation should preserve the corrected chaos-gate dependency list

Live mechanics:

- `at7_chaos_convergence.snbt`
  - `4358010000010003` / "The Chaos Gate" depends on:
    - `4E44010000010004` / Nuclear Dawn capstone
    - `4348010000010004` / Chain Reaction capstone
    - `4D53010000010003` / Machine Soul capstone
    - `5457010000010003` / Threshold of War capstone
    - `4646010000010003` / Baal, after the four false prophets
    - `4358010000010002` / Geburah
  - It grants `at_capstone_complete`, `otherworldly`, `aoa:age/otherworldly`, and `apotheosis:progression/pinnacle`.

Current player-facing text:

- `quest.4358010000010003.quest_desc`: "Present the justice core once dawn, chain, soul, war, the silenced prophets, and Geburah are complete behind you. The periodic-table and Oritech lanes are not on this checklist."
- `book.aoa.atomic_dossier.capstone.chaos_convergence.page2.text`: "The chaos gate accepts that core only after dawn, chain, soul, war, the silenced prophets, and Geburah itself are complete. The periodic-table lane is not on that checklist."

Recommended patch intent:

- Keep this wording. It is aligned with live mechanics.
- If adding Atomic prose, do not reinsert "periodic table", "Oritech", or "table" as hard capstone lanes.

### WARN: Atomic Oritech is optional to the age capstone but required internally for its own hangar chain

Live mechanics:

- `atomic_oritech_convergence.snbt` has a required internal spine:
  - `4F43010000010000` Processing Addon depends on `4D53010000010003`.
  - `4F43010000010001` Accelerator Parts.
  - `4F43010000010002` Cross-Dimensional Addon.
  - `4F43010000010003` Magnetic Field.
  - `4F53010000010000` Drone Port.
  - `4F43011000000104` Augment Application.
  - `4F43011000000105` Advanced Augment Station.
  - `4F4301100000010E` Plutonium Pellet.
  - `4F4301100000010F` Prometheum.
  - `4F53010000010001` Processing Tier 6.
  - `4F53010000010002` Ultimate Addon.
- The Atomic age capstone `4358010000010003` does not depend on Atomic Oritech.

Current player-facing text:

- Existing quest text usually names internal function correctly, for example `4F43010000010003` says "A tuned loop means this Oritech hangar is ready for the recipes ahead."
- `book.aoa.atomic_dossier.mechanics.machine_empire.page1.text` says "Oritech raises core tier and opens the atomic forge beside the Mekanism ladder."

Recommended patch intent:

- Add or revise one Atomic Dossier page to explicitly distinguish "Atomic mainline" from "Atomic Oritech hangar":
  - "The Oritech hangar is an Atomic mastery lane, not a requirement for the Chaos Gate. Its own chain is still structured: processing addon, accelerator parts, magnetic field, drone freight, augment stations, plutonium, prometheum, and addon tiers."
- Do not make Oritech sound required for Otherworldly unless the live capstone dependency changes.

### INFO: Old `ow3_dragon_technology` stage-name concern is resolved in current live files

Evidence:

- `ow3_dragon_technology.snbt` quest `4454010000010005` grants `/astages add {p} ow_draconic_technology_complete true true`.
- `aoa_astages_00_register_stages.js` registers `ow_draconic_technology_complete`.
- I found no live grant of `ow_high_oritech_cosmic_systems_complete` in the inspected surfaces.

No Atomic/Gilded patch needed.

### INFO: `asc3_the_impossible_machine` appears to be a parallel Ascension Draconic reactor branch, not an Atomic/Gilded continuation blocker

Evidence:

- `asc3_the_impossible_machine.snbt` is in the Ascension group and starts from `5449010000010001`.
- It contains Draconic Evolution reactor/energy-core tasks and no observed stage grant in the inspected excerpt.
- `asc5_the_draconic_heart.snbt`, not `asc3`, grants `asc_draconic_apex_complete`.

No Gilded/Atomic patch needed unless the main agent expands scope to Ascension spine cleanup.

## 5. Concrete Implementation Plan

### Step 1: Fix Chartered Arcana required-vs-optional truth

Patch files:

- `config/ftbquests/quests/chapters/g7_chartered_arcana.snbt`
- `config/ftbquests/quests/lang/en_us.snbt`

Patch intent:

- Remove `optional: true` from:
  - `4341011000000001`
  - `4341011000000002`
  - `4341011000000003`
- Update subtitles and `4341011000000004.quest_desc` as described in the BLOCKER above.

Validation:

- `python tools\\quest_validate.py`
- `python tools\\ftbq_integrity_audit.py`
- `rg -n "434101100000000[1-4]|g_magic_authorization_complete|optional branches" config/ftbquests/quests/chapters/g7_chartered_arcana.snbt config/ftbquests/quests/lang/en_us.snbt`

### Step 2: Mark optional Astral side quests clearly without weakening required spine

Patch files:

- `config/ftbquests/quests/lang/en_us.snbt`

Patch intent:

- Add "Optional:" to subtitles for `g_power_beyond_wires.snbt` quests where `optional: true`, especially:
  - `5057011000000102`, `5057011000000104`, `5057011000000109`-`505701100000011C`, `505701100000011E`
  - `5057011000000005`-`5057011000000008` already read optional in body text; consider subtitle consistency only.
- Keep required wording for:
  - `5057011000000001`, `5057011000000002`, `5057011000000003`, `5057011000000004`
  - `505701100000011D` / Final Crystal, because it is not marked optional.

Validation:

- `rg -n "quest\\.5057011000000(00[1-8]|10[0-9A-F]|11[0-9A-F])\\.(quest_subtitle|quest_desc|title)" config/ftbquests/quests/lang/en_us.snbt`
- `python tools\\ftbq_integrity_audit.py`

### Step 3: Add conservative Gilded structure/exploration guidance

Patch files:

- `kubejs/assets/aoa/lang/en_us.json`
- A new or existing Gilded Ledger Modonomicon entry under `kubejs/data/aoa/modonomicon/books/gilded_ledger/entries/`

Patch intent:

- Add an Astral exploration/structures page that avoids exclusive spawn/location claims.
- Suggested copy:
  - "Astral exploration is part of Gilded, but the required path is narrow: enter the dimension, gather core materials, prepare the Void Titan route, and finish the Atomic Disassembler handoff. Side bosses, templates, presents, and equipment sets are optional mastery unless their quest says otherwise. Use the questbook as the source of truth for what feeds the age grant."

Validation:

- `python -m json.tool kubejs/assets/aoa/lang/en_us.json > $null`
- If KubeJS changed: `node --check kubejs/server_scripts/aoa_recipes_gilded_weaves.js` is not required for book/lang-only edits, but run `node --check` for any changed `.js` file if the main agent touches scripts.

### Step 4: Refine Atomic Dossier Oritech guidance

Patch files:

- `kubejs/assets/aoa/lang/en_us.json`
- A new or existing Atomic Dossier Modonomicon entry under `kubejs/data/aoa/modonomicon/books/atomic_dossier/entries/`

Patch intent:

- Add a page or paragraph that explains Atomic Oritech as an Atomic mastery/hangar lane, not an Otherworldly capstone dependency.
- Suggested copy:
  - "The Oritech hangar is Atomic mastery, not a Chaos Gate requirement. Its internal route still matters: processing addon, accelerator parts, magnetic field, drone freight, augment stations, plutonium, prometheum, and addon tiers. Finish it for the fleet's own endgame; finish dawn, chain, soul, war, prophets, and Geburah for Otherworldly."

Validation:

- `python -m json.tool kubejs/assets/aoa/lang/en_us.json > $null`
- `rg -n "periodic-table lane is not|Oritech hangar|Chaos Gate|4358010000010003|4F43010000010003" config/ftbquests/quests/lang/en_us.snbt kubejs/assets/aoa/lang/en_us.json`

### Step 5: Final file-level validation after main-agent patches

Recommended commands:

- `python tools\\quest_validate.py`
- `python tools\\ftbq_integrity_audit.py`
- `python tools\\ftbq_astages_progression_audit.py`
- `python -m json.tool kubejs/assets/aoa/lang/en_us.json > $null`
- `node --check kubejs/server_scripts/aoa_recipes_gilded_weaves.js`
- `node --check kubejs/server_scripts/aoa_recipes_atomic_weaves.js`
- `node --check kubejs/server_scripts/aoa_recipes_oritech_weaves.js`
- `node --check kubejs/server_scripts/aoa_astages_00_register_stages.js`

Run the Node checks only for changed or touched KubeJS files if the patch stays lang/SNBT/book-JSON only.

## 6. Claims Not Verified

- In-game `/reload` remains NOT_VERIFIED. I did not launch the pack.
- I did not verify actual mob spawn rules, biome exclusivity, or structure placement in jars. Avoid adding location/exclusivity claims until the main agent verifies them from live configs or jar data.
- I did not verify Yggdrasil as a live mod/item/structure target. Searches found no current quest/book hits for `Yggdrasil`/`yggdrasil`.
- I did not run the full validator stack after this report because no live quest/lang/KubeJS files were changed.
- The worktree already contains many unrelated modified/deleted/untracked files. This report does not interpret or revert them.
