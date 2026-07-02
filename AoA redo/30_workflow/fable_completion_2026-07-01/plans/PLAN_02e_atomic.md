# PLAN 02e — ATOMIC COMPLETION (DESIGN ONLY)

**Designer pass:** structural. No config/kubejs/lang edits performed. No git.
**Prepend at author time:** `01_MASTER_PREAMBLE.md`.
**Chapter → age:** all Atomic chapters are group `7D28E4AEBC440F10`.
**Verified on disk 2026-07-02** against the live jars and the live `aoa_astages_*.js`.

---

## 0. Headline: the 02e/02a backlog is badly stale. Almost all of it is already done.

The Atomic section of `02a`/`02e` was written from the pre-authoring census. A live re-grep of
`config/ftbquests/quests/chapters/at*.snbt` shows the Atomic chapters are already among the
densest in the pack (`at3`=176, `at4`=303, `at5`=170 quests). Item-by-item verification:

| 02e backlog claim | Live truth (proof) | Verdict |
|---|---|---|
| draconicevolution IO/relay/wireless crystal base tier "at Atomic" | The entire DE base subsystem is gated **`otherworldly`**, not Atomic (`aoa_astages_01n_ascension.js:39-77`; `draconium_ingot` OW at `01_item_restrictions.js:56`). MASTER_PREAMBLE §3 agrees: "Draconic Evolution — otherworldly (base+wyvern)." | **[CANON] — move to `04` (OW). Cannot go in Atomic without a gate change, which Policy 1 forbids.** |
| ballistix `nuclear` + `thermobaric` warheads = 0 quests | Both already tasked in `at5`: `nuclear` at `at5:896`, `thermobaric` at `at5:757` (smart_filter, bundled w/ `rejuvination`). 41 unique ballistix ids already in `at5`. | **DONE. Claim is wrong.** |
| evolvedmekanism "one more factory family + personal-storage ladder (6 of 100+ taught)" | `at4` already tasks the FULL evolvedmekanism factory roster (basic→dense→elite→overclocked→ultimate alloying + every dense/overclocked factory conversion) AND the full personal chest/barrel ladder (advanced/dense/elite/overclocked/ultimate). ~65 ids in `at4`. | **DONE. Claim is wrong.** |
| mekmm "2-3 more large-factory reps beyond basic_oxidizing_factory" | `at4` already tasks the FULL mekmm roster: 14 factory families × 6 tiers + `large_chemical_infuser`, `large_rotary_condensentrator`, `planting_station`, `recycler`, `wireless_charging_station`, `wireless_transmission_station`. ~130 ids. | **DONE. Claim is wrong.** |
| cabletiers "mega tier (7 ids)" | mega tier (Atomic-gated, `01j_storage.js:70+`) all 7 already in `at4` (`mega_autocrafter/constructor/destructor/disk_interface/exporter/importer/interface`). `ultra` is **Gilded** (belongs to 02d/g4, already in `g4`). `creative_*` excluded. | **DONE. Claim is wrong.** |
| extrastorage `netherite_crafter`/`advanced_importer` | Both already in `at4` (+`advanced_exporter`). diamond/gold/iron crafters are Gilded (in `g4`). | **DONE.** |
| appmek remaining `chemical_storage_cell` tiers | All tiers 1k/4k/16k/64k/256k + `chemical_cell_housing` already in `at3`. | **DONE.** |
| nuclearscience `radioisotopegenerator` + full hazmat set | `radioisotopegenerator`, `radioactiveprocessor`, full `hazmat*` set AND `reinforcedhazmat*` set all already tasked. | **DONE.** |
| [CANON] Mekanism SPS antimatter | `sps_casing`/`sps_port`/`supercharged_coil`/`pellet_antimatter` = **0 pack-wide**, all ungated. The one genuine Atomic gap. | **REAL GAP — task it (T-02e-1).** |

**Net: exactly ONE authoring task remains for Atomic — Mekanism SPS antimatter production.**
Everything else the prompt lists is either already shipped or belongs to another age's file
(DE → OW `04`; cabletiers ultra → Gilded, already in `g4`). This plan authors the SPS beat,
records the four stale-backlog corrections, and escalates the two handshake/[CANON] calls.

Author must re-run the proof greps in §6 before touching a file — if any count moved since
2026-07-02, stop and re-scope.

---

## 1. Approaches considered (brief)

**DE base tier.** Prompt asked to host DE base at `at4` or `atomic_oritech_convergence`.
Rejected both: the DE base subsystem is `otherworldly`-gated on disk. Placing it in an Atomic
chapter is a cross-age inversion (later-tier tech in an earlier chapter = hard defect per
MASTER_PREAMBLE §1). Policy 1 (`AOA_QUEST_SCOPE_REGISTRY.md`) forbids moving the gate down for
coverage. Correct action: author DE base in the OW buildout (`04`) and let Ascension chain the
awakened/chaotic/reactor tier in `05`. Left as a clean tail hand-off note here (§4), no nodes.

**Ballistix / evolvedmekanism / mekmm / cabletiers / extrastorage / appmek / nuclearscience.**
Considered a "top-up" pass to find stragglers. Rejected: adding more nodes to `at4` (already 303
quests, the densest chapter in the pack) violates the anti-bloat rule and the no-duplicate rule,
and there is no meaningful unquested content left in these families at Atomic tier. Under-author
per Density §4. Recorded as DONE.

**Mekanism SPS.** Two placements considered:
- (A) New standalone Atomic chapter — rejected, one beat is not a chapter (density floor is
  aspirational, padding forbidden).
- (B) **Extend `at3_chain_reaction`** (the fission/turbine/reactor chapter, group
  `7D28E4AEBC440F10`) with a short antimatter lane hanging off the reactor spine. **Chosen** —
  SPS is thematically the endgame of the Atomic nuclear chain (fission power → polonium →
  antimatter), and `at3` already owns that chain. Its consumer (`antiprotonic_nucleosynthesizer`)
  is OW-gated, giving a clean tier boundary: **produce antimatter at Atomic, consume it at OW.**

---

## 2. Tasks (STRICTLY disjoint file sets)

### T-02e-1 — Mekanism SPS antimatter production lane (the only real gap)
- **File touched:** `config/ftbquests/quests/chapters/at3_chain_reaction.snbt` (ONLY).
- **Lang sidecar:** `phase0/stubs/T-02e-1_stubs.txt`.
- **Nodes (2, tight lane; no third node — SPS is a small subsystem):**
  1. **SPS structure** — `item` task on `mekanism:sps_casing` (icon = sps_casing). Bundle the
     other structure parts as additional `item` tasks in the SAME node so it stays one card:
     `mekanism:sps_port`, `mekanism:supercharged_coil`. Teaches building the Supercharged
     Particle System multiblock. All three ids verified in jar (`assets/mekanism/lang/en_us.json`),
     all ungated.
  2. **Antimatter pellet** — `item` task on `mekanism:pellet_antimatter` (icon = pellet_antimatter).
     Payoff node: run the SPS to convert polonium pellets + massive energy into antimatter.
     Depends on node 1. Verified ungated.
- **Dependencies (crossing-free):**
  - Node 1 (SPS structure) deps the at3 fission-reactor anchor `4348010000000000`
    (`fission_reactor_casing`, the chapter's opening reactor node) — the reactor is the power
    source the SPS demands.
  - Node 1 also deps the at2 polonium producer `5054012000060001`
    (`mekanism:solar_neutron_activator`, in `at2_the_periodic_table.snbt`) — polonium is the SPS
    feedstock. **Cross-chapter dep is legal in FTBQ and creates no in-chapter line crossing.**
    Verify at author time that at3 already carries other at2 back-deps (it inherits the fission
    chain from at2) so this is consistent with existing flow; if it introduces the chapter's
    only cross-chapter edge, keep node 1's dep on the LOCAL reactor node only and drop the at2
    edge (polonium gating still enforces order via AStages).
  - Node 2 (antimatter) deps node 1 only.
- **Coordinates:** at3 spans x 0..29, y -4..4. Place the SPS lane in open space to the right of
  the reactor spine, e.g. node 1 at `x: 30.0, y: -4.0`, node 2 at `x: 31.5, y: -4.0` (0.5 grid,
  right of current max x=29, no existing node to cross). Confirm emptiness at author time.
- **New quest ids:** allocate two fresh 16-hex ids NOT colliding with any in the file (anchored
  scan `grep -oE 'id: "[0-9A-F]{16}"'`). Suggest the at3 family prefix `4D4E0120` + a free
  suffix, e.g. `4D4E012000SPS001`-style is NOT valid hex — use e.g. `4D4E0120005P5001`? no.
  Use plain unused hex: `4D4E012000240001`, `4D4E012000240002` (the file's last used suffix
  block is `...00230002`; `0024xxxx` is free — verify).
- **Rewards:** modest, in-age. Node 1: XP + a couple `mekanism:pellet_polonium` (feedstock
  primer) via a reward table or inline `item` reward. Node 2: XP + small loot. No future-age
  items, no mandatory OP gear (per reward canon). Reward ids must be jar-verified before use.
- **SkillsLevel / PlayerSpells blocks:** copy the inert block shape from an existing at3 node
  verbatim; do NOT strip.
- **[CANON] decision recorded (resolves the 08 queue item):** **SPS antimatter IS in scope,
  ungated, hosted at Atomic in at3.** Rationale: antimatter is a canonical Atomic-tier showpiece;
  its feedstock (polonium) is Atomic; its only real consumer (nucleosynthesizer) is OW-gated, so
  producing antimatter at Atomic does not leak OW content. No new gate needed (Policy 1 clean).

### T-02e-2 — Backlog reconciliation (DOC ONLY, no chapter edits)
- **File touched:** none in `config/`. This task records the four stale-claim corrections
  (ballistix / evolvedmekanism / mekmm / cabletiers-extrastorage-appmek-nuclearscience all DONE)
  into `LEDGER.md` and marks the 02a Atomic rows resolved, so no downstream agent re-authors them.
- No lang sidecar. No stubs.

**Disjointness:** T-02e-1 touches only `at3_chain_reaction.snbt`. T-02e-2 touches no chapter.
No file is edited by two tasks. (Note for the wider workflow: `02d`/g4 owns cabletiers `ultra`
and extrastorage diamond/gold/iron crafters — 02e must NOT touch g4.)

---

## 3. Handshake calls (explicit)

- **extrastorage / appmek ↔ 02d (Gilded g4):** **No collision, no work for either side on the
  atomic items.** `netherite_crafter` + `advanced_importer` + `advanced_exporter` are ALREADY
  tasked at Atomic in `at4`. The Gilded-tier crafters (`diamond/gold/iron_crafter`) are ALREADY
  in `g4`. appmek cells are ALL in `at3`. **02e authors none of these; 02d must not re-task the
  netherite/advanced-importer items (they are Atomic, already done).** The only extrastorage/appmek
  items 02d should confirm are the Gilded crafters it already has.
- **cabletiers ↔ 02d (Gilded g4):** `ultra` tier is **Gilded** and already in `g4`; `mega` is
  Atomic and already in `at4`. 02e authors zero cabletiers nodes. No handshake action needed.
- **Draconic Evolution ↔ 04 (OW):** DE base IO/relay/wireless crystal + `particle_generator`,
  `grinder`, `disenchanter`, `celestial_manipulator`, `dislocation_inhibitor`, `draconium_chest`,
  `crystal_binder` are all **otherworldly**-gated and belong to the `04` buildout, authored so
  `05` (Ascension) chains the awakened/chaotic/reactor tier. **02e authors zero DE nodes.**

---

## 4. Clean tail hand-off for later files (no nodes here)

For the `04` (OW) author, the DE base-tier subsystem to build (all verified `otherworldly` in
`aoa_astages_01n_ascension.js`, all ids jar-verified in `Draconic-Evolution-1.21.1-3.1.4.632.jar`
`assets/draconicevolution/lang/en_us.json`):
- Crystal energy network: `basic_io_crystal`, `basic_relay_crystal`, `basic_wireless_crystal`
  (+ `crystal_binder` tool to link them), plus `energy_pylon`, `energy_transfuser`, `flux_gate`,
  `fluid_gate` for the transfer subsystem.
- Wyvern tier network: `wyvern_io_crystal`, `wyvern_relay_crystal`, `wyvern_wireless_crystal`.
- Utility machines: `particle_generator`, `grinder`, `disenchanter`, `celestial_manipulator`,
  `dislocation_inhibitor`, `draconium_chest`, `energy_core` + `energy_core_stabilizer` (tiered
  energy storage sphere), `generator`.
- Leave a clean OW→Ascension tail: `05` chains `draconic_io/relay/wireless_crystal` (all
  `ascension`), `awakened_*`, `chaos_crystal`, `reactor_core/injector/stabilizer` on top.
- **Phantom-id caution:** `draconicadditions:chaotic_core` / `draconic_energy_core` /
  `wyvern_staff` DO NOT EXIST. The valid ids are the `draconicevolution:`-namespaced
  `chaotic_core`, `draconic_energy_core`, `chaotic_energy_core`, `draconic_staff`, `chaotic_staff`
  (all `ascension`) — verified present in the DE jar lang. Do not author the `draconicadditions:`
  forms.

---

## 5. Stub briefs

Written to `phase0/stubs/T-02e-1_stubs.txt` (2 nodes × 3 keys). Opus fills prose later.
Instruction-first, no em dashes.

---

## 6. Verification steps (author must re-run before editing, and after)

**Pre-edit (confirm nothing moved since 2026-07-02):**
```
# SPS must still be 0 pack-wide (else already authored — stop):
grep -rl "mekanism:sps_casing\|mekanism:sps_port\|mekanism:supercharged_coil\|mekanism:pellet_antimatter" config/ftbquests/quests/chapters/*.snbt   # expect: no output
# SPS parts still ungated (only nucleosynthesizer OW-gated):
grep -rn "sps_casing\|sps_port\|supercharged_coil\|pellet_antimatter\|antiprotonic_nucleosynthesizer" kubejs/server_scripts/*.js
#   expect: only the OW line for antiprotonic_nucleosynthesizer (01_item_restrictions.js:340)
# ids exist in jar:
unzip -p mods/Mekanism-1.21.1-10.7.19.85.jar assets/mekanism/lang/en_us.json | grep -oE '"block\.mekanism\.sps_(casing|port)"|"block\.mekanism\.supercharged_coil"|"item\.mekanism\.pellet_antimatter"'
# anchor nodes still present:
grep -n '4348010000000000' config/ftbquests/quests/chapters/at3_chain_reaction.snbt        # at3 fission anchor
grep -n '5054012000060001' config/ftbquests/quests/chapters/at2_the_periodic_table.snbt    # at2 polonium producer
# chosen new ids free (expect no output):
grep -oE 'id: "4D4E012000240001"|id: "4D4E012000240002"' config/ftbquests/quests/chapters/at3_chain_reaction.snbt
```

**Post-edit:**
```
# quest count grew by exactly 2:
python -c "import re;print(len(re.findall(r'^\s+id: \"[0-9A-F]{16}\"',open('config/ftbquests/quests/chapters/at3_chain_reaction.snbt',encoding='utf-8').read(),re.M)))"   # expect 178
# no duplicate ids introduced (anchored):
grep -oE 'id: "[0-9A-F]{16}"' config/ftbquests/quests/chapters/at3_chain_reaction.snbt | sort | uniq -d   # expect empty
# line endings preserved (at3 is LF-only):
python -c "r=open('config/ftbquests/quests/chapters/at3_chain_reaction.snbt','rb').read();print('CRLF',r.count(b'\r\n'),'LF',r.count(b'\n'))"   # expect CRLF 0
# SNBT parses: run FTBQ validation skill (aoa-ftb-quests-validation) or in-game /ftbquests reload
# every lang key present for the 2 new ids:
grep -c "4D4E012000240001\|4D4E012000240002" config/ftbquests/quests/lang/en_us.snbt   # expect >= 6 (3 keys x 2)
```

**Crossing check:** SPS lane sits at x≥30, right of the current max x=29, with only intra-lane
and back-to-anchor edges. Run the repo's dependency-crossing computation (Codex lane) after
authoring to confirm 0 new crossings.

---

## 7. Deliverables summary
- Edited chapter: `at3_chain_reaction.snbt` (+2 nodes, SPS antimatter lane). **T-02e-1 only.**
- Stub sidecar: `phase0/stubs/T-02e-1_stubs.txt`.
- LEDGER before/after: `at3` 176 → 178. All other Atomic families recorded DONE (no deltas).
- [CANON] resolved: SPS antimatter in-scope, ungated, Atomic/at3 (remove from 08 queue).
- [CANON] escalated: DE base tier belongs to OW `04`, NOT Atomic (do not down-gate; Policy 1).
