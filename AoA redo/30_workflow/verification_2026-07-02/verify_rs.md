# Refined Storage family — coverage verification

Verifier: read-only. Date 2026-07-02. Jars extracted from live `/mods`.

## Installed (jar-verified)
- `refinedstorage-neoforge-2.0.9` — **RS2** for 1.21.1
- `ExtraStorage-1.21.1-5.0.10`
- `cabletiers-neoforge-1.21.1-0.6.12`
- `ExtendedTerminal-1.21.1-19.0.4`
- `refinedstorage-quartz-arsenal-neoforge-1.0.8`
- `interdimensionalwirelesstransmitter-neoforge-1.21.1-0.1.5`
- (+ RS integration jars: curios, emi, mekanism-integration)

## VERDICT

**The census figure ("refinedstorage 7 refs, 0.009 ratio") is WRONG / a massive undercount.**
RS is already authored as a genuine parallel IR→OW storage lane. Distinct RS-namespace
ids/tags referenced across chapters: **~18** (not 7); whole-family distinct refs: **48**.
The census almost certainly counted only direct item-task `id:` lines and missed:
1. `block_item` tasks (controllers, grids, disk drive, etc. are BLOCKS → block_item task type).
2. RS refs living inside `ftbfiltersystem:filter` smart-filter strings (tag-based any-variant tasks).
3. The entire cabletiers/extrastorage/interdim tiers that ARE the RS lane's upper rungs.

No new "parallel storage lane" needs to be built. The lane exists, is tiered, and is gated.
The real gaps are small and specific (below). No per-color / per-disk-tier filler is warranted.

## Phantom / defect check — CLEAN
- `refinedstorage:autocrafting_monitors`, `refinedstorage:wireless_transmitters` — NOT phantom.
  They appear only inside `item_tag(...)` filters and both exist as real item tags in the jar
  (`data/refinedstorage/tags/item/{autocrafting_monitors,wireless_transmitters}.json`).
- `interdimensionalwirelesstransmitter:black_interdimensional_wireless_transmitter` — VALID.
  16 dyed variants are separately registered (blockstates+models per color); lang shares one key.
- RS2 rename confirmed: old "Crafter" → **"Autocrafter"**; quests correctly use
  `refinedstorage:autocrafter` + `autocrafter_manager` (RS2 ids), not legacy `crafter`.
- All ~18 sampled RS ids resolve against jar registry. No bad ids found in quests.

## Beats table (live state)

| Chapter | Age | RS-lane beats present |
|---|---|---|
| `ir_digital_storage_foundations` | Industrial Rev. | RS network entry: controller, cable, grid, crafting_grid, portable_grid, disk_drive, 1k_storage_disk, disk_interface, detector, storage_monitor, security_manager; cabletiers **elite** importer/exporter/constructor/destructor/disk_interface |
| `g4_the_infinite_grid` | Gilded | RS **autocrafter** + autocrafter_manager; extrastorage crafters iron/gold/diamond; cabletiers **ultra** full set + elite/ultra autocrafter |
| `at4_machine_soul` | Atomic | RS wireless: wireless_grid, wireless_autocrafting_monitor(+tag), wireless_transmitters(tag), range_upgrade; quartz_arsenal wireless_crafting_grid; extrastorage netherite_crafter + advanced import/export; cabletiers **mega** full set |
| `ow4_the_dyson_project` | Otherworldly | RS network_transmitter + network_receiver; interdim black_interdimensional_wireless_transmitter |
| `journey_to_ascension` | (spine mirror) | RS autocrafter reference |

Tier discipline matches gates: elite=IR, ultra=Gilded, mega=Atomic, netherite crafter=Atomic,
network transmitter/interdim=OW. Consistent, no cross-age inversions observed.

## Gates (kubejs — authoritative)
`aoa_astages_01j_storage.js` + `aoa_astages_01_item_restrictions.js` gate the whole family:
- RS network entry (controller/grid/disk_drive/detector/security/storage_monitor/portable_grid) → **industrial_revolution**
- RS autocrafting + extrastorage iron/gold/diamond crafter + cabletiers ultra → **gilded_age**
- RS wireless_grid / wireless_autocrafting_monitor / range_upgrade, extrastorage netherite + advanced io, cabletiers mega, RSMek 8192b, quartz_arsenal wireless_crafting_grid → **atomic**
- RS network_transmitter / network_receiver → **otherworldly**
Gate surface is broad and correctly tiered. No missing-gate softlock risk found for placed items.

## Ranked jar-verified GAP list (real, bundle-sized — no filler)

1. **ExtendedTerminal — 0 quest refs, 0 gates.** (jar: basic/advanced/elite/extreme/ultimate/
   neo_extreme terminal, wireless_et_terminal, nether/end/sculk_terminal, et_terminal, +
   compat_processor/press). This is the one genuinely absent sub-mod. It's a Grid-replacement
   terminal ladder that parallels the RS grid line. Suggested: **one bundled beat** in
   `at4_machine_soul` (Atomic) — advanced/elite/extreme terminal + `wireless_et_terminal` as a
   single node, mirroring the wireless-grid rung. Do NOT split per-terminal. Also currently
   **UNGATED** — flag for gate parity (terminals = grid access; align to RS wireless→atomic).
   Note per registry policy: ungated ≠ mandatory gate; raise as coverage-only, not a gate demand.

2. **RS `external_storage` + `constructor`/`destructor` + `relay` + `interface`/`network_card`**
   — RS-namespace ids present in jar, not referenced in quests (cabletiers covers tiered
   constructor/destructor/interface, but the **base RS** versions are unquested). Optional single
   IR bundle beat ("connect the network to the world: importer/exporter/external_storage/
   constructor/destructor") in `ir_digital_storage_foundations`. Low priority — mechanics are
   already taught via cabletiers elite tier.

3. **extrastorage high-cap disks (256k / 1024k / 4096k / 16384k) + fluid disks + neural_processor**
   — jar has the big-disk ladder; quests reference extrastorage crafters but not the disks.
   Optional: fold `disk_16384k` (top tier) into the Atomic beat as the storage-capacity capstone.
   Avoid per-tier filler; one top-disk node max.

4. **RSMek integration chemical storage** — gated (IR01j) but **no quest beat**. Optional Gilded/
   Atomic bundle tying RS to Mekanism chemicals (256b/1024b/8192b chemical disk). One node.

5. **quartz_arsenal** — 1 ref (wireless_crafting_grid, Atomic). Jar only has that + creative
   variant. Effectively complete; no gap.

## Bottom line
Coverage is FINE, not a 0.009-ratio hole. Do RS-family census by counting block_item tasks and
ftbfiltersystem tag filters, not just item `id:` lines. Only real add: **ExtendedTerminal** (1
bundled Atomic node + gate parity). Everything else is optional depth, single-node, no per-color/
per-tier padding.
