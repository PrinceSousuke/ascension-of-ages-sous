# Neo Vitae Verification And Quest-Pass Prep

## Verdict

The live checkout has moved beyond the older planning docs. Neo Vitae is implemented in current files through AStages locks, FTBQ rewires, KubeJS/data overlays, cross-weaves, Atomic/Otherworldly optional quests, and AoA Modonomicon text.

No quest additions should happen until the current static risk is resolved: `ren_magic_foundations` appears to require `neovitae:athanor`, while the jar recipe for `athanor` requires `neovitae:tabula_animata` and tier-2 orb access that live gates place later.

## Verified Jar Surface

Jar: `mods/neovitae-1.21.1-1.0.25.jar`

Confirmed:

- Orbs: `blood_orb_weak`, `blood_orb_apprentice`, `blood_orb_magician`, `blood_orb_master`, `blood_orb_archmage`, `blood_orb_transcendent`.
- Machines and blocks: `ara_vitae`, `hellfire_forge`, `athanor`, `alchemy_array`, `tabula_vitae`, `incense_altar`.
- Dungeon/key/boss surface: `data/neovitae/dimension/dungeon.json`, `simple_key`, `standard_key`, `mine_key`, `mine_entrance_key`, `boss_key`, `entity.neovitae.daemonium_doloris.foreman`.
- Recipe types: `neovitae:ara_vitae_recipe`, `hellfire_forge`, `hellfire_forge_transform`, `hellfire_forge_upgrade`, `hellfire_forge_spiritus_infusion`, `athanor`, `alchemytable`, `array`, `meteor`, `sentient_downgrade`, `fluid_tiered`, flask variants.
- Data maps: `block/altar_rune_stats`, `block/routing_node_stats`, `block/tranquility`, `entity_type/entity_sacrifice_value`, `item/blood_orb_stats`, `item/sigil_stats`, `item/spiritus_gem_max`, `neovitae/imperfect_ritual/imperfect_ritual_stats`, `neovitae/ritual/ritual_stats`.
- Altar tiers: `weak`, `apprentice`, `mage`, `master`, `archmage`, `transcendent`.
- Shipped `data/neovitae/tags/block/altar/pillars.json` is empty. The pack overlay must remain the authority for pillar validity.

Static scan result from the Neo audit agents: all live `neovitae:*` references in KubeJS/FTBQ resolved against the installed jar or data/tag paths.

## Implemented Live State

Implemented in live files:

- `neovitae:dungeon` dimension gated in `kubejs/server_scripts/aoa_astages_03_dimension_restrictions.js`.
- Neo Vitae item locks in `kubejs/server_scripts/aoa_astages_01m_magic.js`.
- Hellforged tag locks in `kubejs/server_scripts/aoa_astages_06_ore_restrictions.js`.
- F&A Black Hole/corrupti-dust removal.
- Deterministic Soul Looting book JSON.
- `#aoa:magic_feedstock` bridge.
- Pillar/capstone tag overlays.
- Ritual stats overlay.
- Neo Vitae weave script.
- Ren/IR/Gilded quest rewires.
- Atomic/Otherworldly optional wings.
- AoA Modonomicon `Scriptura Vitae`.

## Stale Or Contradicted Planning Claims

- The primary spec says Neo Vitae has no on-disk integration. That is stale.
- The older F&A demotion plan says a five-age required spine through Otherworldly. Live files instead match required Renaissance to Gilded plus optional Atomic/Otherworldly depth.
- The `nv-atomic-ow-depth.md` note saying `neovitae:sentient_axe` was not found is stale; jar and live file evidence confirm it exists.
- Old IDs should not be authored without re-verification: `neovitae:arcane_ash`, `neovitae:inversion_focus`, `neovitae:air_sigil`, `weak_blood_orb`, `apprentice_blood_orb`, `neovitae:scriptura_vitae`, `theurgy:mercury`, `mercury_shard`.
- Correct guide surface: `neovitae:guide`, custom item `neovitae:guide_book`, and `data/neovitae/modonomicon/books/guide/book.json`.

## Quest-Pass Gaps

High-priority fixes:

| Gap | Recommendation |
|---|---|
| Atanor age hardlock risk | Verify JEI/runtime. If confirmed, move the capstone target, loosen locks, or replace the Renaissance capstone proof. |
| Ara Vitae tier validation | Smoke tier-2+ altar behavior with the pack pillar tags. |
| `hellfire_forge_upgrade` behavior | Confirm the custom Eternal Stella upgrade actually applies a useful upgrade. |
| F&A optional retention | Decide whether F&A gets optional content back. Currently only the Journey icon remains. |

Useful optional Neo targets after the hardlock is fixed:

- `neovitae:guide` or `neovitae:guide_book` as guide onboarding.
- Ritual stones/diviners.
- Teleposer line.
- Advanced sigils/runes.
- Flasks/anointments.
- `mine_key` and `mine_entrance_key`.
- `sentient_scythe`, `sentient_shovel`, and `training_bracelet`.
- Spiritus catalyst/shard economy.

## Cross-Weave State

Live verified weave concepts:

- `#aoa:magic_feedstock`.
- Malum/Spectrum capstone tags.
- Cross-mod altar pillar tag.
- Malum to Sentient Axe.
- Theurgy salts to raw Spiritus catalyst.
- Occultism essence to alchemy flask.
- F&A Eternal Stella to Neo Vitae upgrade.
- F&A arcane crystal dust to weak blood shard.

Runtime verification still needed for the Eternal Stella upgrade effect and altar pillar behavior.

## Validation Status

Static validation reported by the Neo agents:

- `node --check` passed for relevant Neo/F&A KubeJS files.
- JSON lint passed for new data files.
- SNBT brace/paren and duplicate quest ID checks passed for touched chapters.

Blocked/not performed:

- Full quest validator suite was unavailable in this checkout.
- In-game reload and JEI/runtime behavior were not verified.
- `config/neovitae/materials.json` is not generated yet in the live checkout.

