# H3 — Upper-age progression critique + full capstone-spine verification

Scope: Atomic (done, dense), Otherworldly (spine only), Ascension (spine only), plus a
full 8-age capstone fan-in verification. Audit only. All findings carry a file:line +
proof command. Severity ladder: SOFTLOCK > BROKEN > CANON > HYGIENE.

Method note: FTBQ command rewards in `chapters/*.snbt` are mirrored authoritatively in
`kubejs/server_scripts/aoa_astages_team_grant.js` (quest-id -> [stages]). I cross-checked
both. Fan-in reachability was computed with a transitive-ancestor walk over every quest's
`dependencies:` array across all chapters (script logic in the run log below).

---

## LENS 1 — FULL CAPSTONE SPINE VERIFICATION (highest priority)

Registry of proofs: `kubejs/server_scripts/aoa_astages_00_register_stages.js:32-126`.
Age-grant model: each age's NEXT-age stage is granted by the CURRENT age's capstone quest,
which must transitively depend on (fan in) every registered domain proof of the current age
plus that age's required boss proof(s). Reference invariant = at7 / ow6.

### Verdict table

| Age | Grant quest (stage granted) | File:line of grant | Proofs fanned in | Proofs MISSING | Verdict |
|---|---|---|---|---|---|
| dark_ages | (world-entry root, no fan-in; Dark has no domain proofs) | `journey_to_ascension` root `5350010000010000` | n/a (entry gate only) | none | PASS |
| medieval_times | `097AED7C91033D5E` (medieval_times) | `entering_the_iron_era.snbt` | Dark entry line (no Dark domain proofs registered) | none | PASS |
| the_renaissance | `6D7E8F901A2B1054` (the_renaissance) | `what_waits_in_the_grove.snbt` | Medieval line | none | PASS |
| industrial_revolution | `0B0310A0000000F0` (industrial_revolution + ren_seal) | `ren_maledictus_vigil.snbt` | all 10 ren_* domain proofs + maledictus (ren_maledictus_vigil node co-grants maledictus_defeated) | none | PASS |
| gilded_age | `4954631000000000` (gilded_age + ir_capstone) | `ir_netherite_citadel_obsidilith.snbt` | 5 ir_* domain proofs + obsidilith_defeated | none | PASS |
| atomic | `5057011000000004` (atomic) | `g_power_beyond_wires.snbt` | 7 g_* domain proofs + void_titan_defeated (g_temporal co-granted on the void_titan node `5057011000000003`) | none | PASS |
| otherworldly | `4358010000010003` (otherworldly + at_capstone) | `at7_chaos_convergence.snbt` | 7 at_* domain proofs + macabre 4 (baal chain) + geburah | none (tremorzilla optional by design) | PASS |
| ascension | `4256010000010006` (ascension + ow_capstone) | `ow6_beyond_the_veil.snbt` | all 7 ow_* domain proofs + leviathan_defeated | none | PASS |
| final (aoa_complete) | `4153010000010002` (aoa_complete + asc_capstone) | `asc7_ascension.snbt` | 5 asc_* domain proofs + asc_final_boss_convergence + draconic_guardian + asc_archive | none | PASS |

**All 8 age grants + the final grant fan in every registered domain proof of their age.**
No dead (registered-but-ungranted) proof stage is fanned into any capstone; no capstone
is missing a fan-in. The reference invariant (at7/ow6) holds across the whole spine.

### (a) existence, (c) grant mechanism
Every age-boundary grant fires via an FTBQ `command` reward with
`command: "/astages add {p} <stage> true true"`, `auto: "enabled"`, `silent: true`,
`team_reward: true`, `permission_level: 2`. Proof: `grep -rn "astages add {p}" chapters/*.snbt`
returns 68 unique grants; every registered non-legacy proof has exactly one granter.

### (b) fan-in — programmatic confirmation
Transitive-ancestor walk of each grant quest confirmed every domain-proof terminal is an
ancestor. Sample output:
```
PASS IR->gilded (4954631000000000)   — missing: none
PASS Atomic->otherworldly (4358010000010003) — missing: none
PASS OW->ascension (4256010000010006)   — missing: none
PASS Ascension->aoa_complete (4153010000010002) — missing: none
PASS Renaissance->IR (0B0310A0000000F0) — 10/10 ren proofs present
PASS Gilded->atomic (5057011000000004) — 7/7 g proofs (temporal co-granted w/ void_titan)
```

### (d) boss proofs vs preamble table — VERIFIED
`grep -rhoE 'entity: "(...)"' chapters/*.snbt` returns all expected kill entities:
`cataclysm:maledictus`, `bosses_of_mass_destruction:obsidilith`,
`astral_dimension:void_titan`, `macabre:valamon|gomoria|gargamaw|baal`, `fdbosses:geburah`,
`cataclysm:the_leviathan`, `draconicevolution:draconic_guardian`. All match the preamble
boss chain (§4). The Atomic required spine has all four macabre bosses (sequential chain
`4646010000010000` -> `...0003` in `at7`) plus `geburah` (`4358010000010002`) as the exam,
both fanned into the at7 capstone. `draconic_guardian` uses an MQT `kill_entity` task
(`asc6_bosses_rise.snbt` quest `425201000001000B`, `type: "kill"`,
`entity: "draconicevolution:draconic_guardian"`) — not a proof-item drop, exactly as the
preamble specifies.

### Registered-but-ungranted stages (NOT defects)
`comm` of registry vs granted stages surfaces 11 ungranted proofs, all documented legacy /
backward-compat markers, none fanned into any live capstone:
`ren_matriculated, ren_traditions_partial/complete, ren_worlds_partial/complete,
ren_void_studies_unlocked, ren_instruments_partial/complete, ren_magic_literacy_complete,
ren_dragon_proof_obtained, ender_guardian_defeated`. Registry comments already mark these
"backward compatibility" / "Optional ... retained for compatibility". **HYGIENE only** —
worth a one-line note in the registry that these are inert, but no action required.

---

## LENS 2 — Atomic ordering (at1 -> at7 + oritech convergence)

Entry gate: `at1_nuclear_dawn` root quest deps `["5057011000000003"]` — the Gilded
void_titan/temporal node, which is itself a direct dep of the Gilded->atomic grant
`5057011000000004`. So Atomic opens only once the player is deep in the Gilded capstone.
Sensible. **PASS.**

Chapter proof ownership is clean and non-overlapping:
- at1 -> at_radiological_materials + at_create_nuclear_mainline
- at2 (periodic_table) -> support, owns no proof (intentional)
- at3 -> at_nuclear_engineering
- at4 -> at_reactor_control + at_neural_industry
- at5 -> at_mff_containment + at_ballistix_policy
- at7 -> boss convergence + at_capstone + otherworldly
- atomic_oritech_convergence -> support, owns no proof (intentional)

No cross-age inversion found. The only later-tier-looking items are MI `quantum_helmet /
chestplate / leggings / boots / sword` in an **optional** node of `at5_threshold_of_war`
(`optional: true`). These are deliberately gated to **atomic** in
`aoa_astages_01p_gap_closure.js:157-161` (the quantum ARMOR line is atomic; the quantum
MACHINE line — casing/hull/barrel/tank — is otherworldly, `aoa_astages_01h:166-169`, gated
behind fusion). This split is intentional, not a defect. **No finding.**

---

## LENS 3 — Otherworldly spine critique (6 chapters vs 7 ow_* proofs)

The 7th proof is not a 7th chapter: `ow6_beyond_the_veil` owns TWO proofs
(`ow_beyond_the_veil_theme_complete` on `4256010000010005` and `ow_capstone_complete` on the
capstone `4256010000010006`). So 6 chapters map to 7 proofs cleanly:

| ow_* proof | granting chapter | grant quest |
|---|---|---|
| ow_launch_offworld_logistics_complete | ow1 | `4C57010000010004` |
| ow_strange_dimension_operations_complete | ow2 | `4C58010000010005` |
| ow_draconic_technology_complete | ow3 | `4454010000010005` |
| ow_dyson_project_complete | ow4 | `4C59010000010004` |
| ow_interdimensional_infrastructure_complete | ow5 | `4443010000010006` |
| ow_beyond_the_veil_theme_complete | ow6 | `4256010000010005` |
| ow_capstone_complete | ow6 | `4256010000010006` |

**Every ow_* proof has a granter and every one fans into the ascension grant.** No dead
stage, no missing fan-in. **PASS.**

Skeleton assessment (as a spine to build ON, not "too thin"): the bones are right.
- ow1 Stellaris launch/logistics, ow2 Stellaris strange-dimension ops, ow3 Draconic base
  tech, ow4 Stellaris Dyson, ow5 advanced_ae quantum + Mek/RS digital cosmos, ow6 fusion +
  Leviathan capstone. Namespace spread per chapter is coherent (each chapter is dominated
  by one anchor mod family, which is the correct spine shape).
- ow6 correctly gates the `ascension` grant behind BOTH Mek fusion
  (`mekanismgenerators:fusion_reactor_controller/frame/port`) and MI fusion
  (`modern_industrialization:fusion_reactor / fusion_chamber`) plus the Leviathan kill.
  That is the right endgame wall for OW.
- Current depth ~11-14 task items per chapter, all correct-namespace, no vanilla items,
  no checkmarks. Good scaffold. Buildout targets in Lens 5.

---

## LENS 4 — Ascension spine (asc_* proofs + aoa_complete)

| asc_* proof | granting chapter | grant quest |
|---|---|---|
| asc_final_crafting_surface_complete | asc1 | `5449010000010006` |
| asc_avaritia_singularity_pressure_complete | asc2 | `5044010000010006` |
| (asc3 the_impossible_machine) | asc3 | support, owns no proof (intentional) |
| asc_oritech_apex_complete | asc4 | `5347010000010002` |
| asc_draconic_apex_complete | asc5 | `4448010000010005` |
| asc_final_boss_convergence_complete + draconic_guardian_defeated | asc6 | `425201000001000B` |
| asc_archive_of_ages_complete | asc7 | `4153010000010001` |
| asc_capstone_complete + aoa_complete | asc7 | `4153010000010002` |

**Draconic Guardian kill task EXISTS** and is the final exam: `asc6_bosses_rise.snbt`
`425201000001000B`, `type: "kill"`, `entity: "draconicevolution:draconic_guardian"`, gear
shape, co-grants `asc_final_boss_convergence_complete` + `draconic_guardian_defeated`. It is
a fanned-in dep of the aoa_complete grant. **PASS.**

**asc7 win-gate references the Draconic reactor requirement (indirectly, correct):** the
final `aoa_complete` grant sits behind `asc_draconic_apex_complete` (asc5), and asc5 gates
on the Draconic **reactor** (`draconicevolution:reactor_core / reactor_injector /
reactor_stabilizer` all present in `asc5_the_draconic_heart.snbt`) plus the chaotic tier
(`draconicevolution:chaotic_core / chaotic_crafting_injector`,
`draconicadditions:chaos_heart / chaos_infuser / item_chaos_injector`). So the Draconic
reactor is a hard prerequisite on the aoa_complete path. **PASS.**

Skeleton assessment: correct final shape — asc1 Extended Crafting Table of Infinities,
asc2 Avaritia singularity, asc3 impossible-machine support, asc4 Oritech apex, asc5
Draconic heart, asc6 boss convergence, asc7 the infinity ingot + aoa_complete. One-anchor-
per-chapter spine is right. Depth is currently 6-18 task items/chapter; asc4 (6 items) is
the thinnest lane and the most obvious buildout candidate.

---

## LENS 5 — Buildout guidance (showpiece FOMO gaps; NOT padding)

These are the highest-signal showpieces legal at each age that the current spine does not
yet task. Author as REQUIRED spine rungs or optional depth per the age vertical-slice rule
(required chapters first, then optional depth) — never as N-of-M main progression.

### Otherworldly — top 5
1. **Stellaris full planet/space-station loop** — the space-infra family (rocket tiers,
   fuel loop, cables/tanks/banks, planet landing) is OW's identity mod; ow1/ow2/ow4 touch
   it but a visible "reach + establish an off-world base" rung is the signature FOMO piece.
2. **advanced_ae Quantum tier** — `advanced_ae:quantum_core / quantum_accelerator /
   quantum_multi_threader / quantum_unit` (present in ow5) plus the OW-gated
   `advanced_ae:quantum_helmet/chestplate` (`aoa_astages_01p:195-196`) as the AE endgame
   armor showpiece; ow5 currently only lightly uses it.
3. **MI fusion + plasma + superconductor line** — ow6 gates the fusion reactor as the wall,
   but the plasma-turbine / superconductor-coil / replicator progression that feeds it is
   the marquee MI-endgame build and deserves its own rung, not just the capstone item list.
4. **Mek fusion reactor as a standalone showpiece** — ow6 requires the controller/frame/
   port/laser_focus_matrix/hohlraum; a dedicated "ignite the fusion reactor" beat (with the
   Hohlraum ignition) is a classic FOMO moment currently folded into the capstone chain.
5. **Draconic wyvern-tier tech** (OW-legal per preamble §3: DE base+wyvern = otherworldly) —
   ow3 covers base draconic; the wyvern energy core / wyvern gear tier is the OW draconic
   showpiece before the ascension chaotic tier.

### Ascension — top 5
1. **Re:Avaritia prestige chain** — the Avaritia line (Neutronium -> Infinity Catalyst ->
   Infinity Ingot, `avaritia:infinity_ingot` is already the final task item) is THE
   ascension identity; asc2 touches it but the full Neutronium/Cosmic-tier compressor loop
   is the signature endgame grind and the biggest FOMO piece.
2. **Extended Crafting elite/ultimate + Crystaltine** (preamble §3: elite/ultimate/
   crystaltine = ascension) — asc1 uses `extendedcrafting:the_ultimate_block`; the
   Crystaltine catalyst + Ultimate Crafting Table tiers are the crafting-surface showpiece.
3. **Draconic Awakened + Chaotic tier + Draconic reactor** — asc5 has the reactor and
   chaotic core; a full "awakened -> chaotic -> reactor online" showpiece arc (Chaos Guardian
   islands -> chaos shards -> reactor) is the marquee DE-ascension build.
4. **Oritech apex tier** (atomic_forge/core_5-7/duratium ceiling) — asc4 is the thinnest
   lane (6 items); the Oritech top-tier machine/energy apex is the obvious buildout to give
   asc4 real weight.
5. **Ballistix antimatter / darkmatter ordnance** (preamble §3: ballistix antimatter =
   otherworldly, but its darkmatter apex reads as an ascension-tier destructive showpiece
   worth a canon call) — verify the exact gate before placing; a late antimatter/darkmatter
   beat is a strong optional-depth FOMO node if the gate supports ascension placement.

---

## Findings summary

| # | Severity | Finding | Proof |
|---|---|---|---|
| 1 | HYGIENE | 11 registered proof stages have no granter (all documented legacy/back-compat: ren_matriculated, ren_traditions_*, ren_worlds_*, ren_void_studies_unlocked, ren_instruments_*, ren_magic_literacy_complete, ren_dragon_proof_obtained, ender_guardian_defeated). None fanned into a live capstone. Consider a registry note; no action needed. | `comm -23 registry granted` |
| 2 | HYGIENE (informational) | Renaissance -> IR grant carries F&A node `0B03101000000039` (arcane_bone_meal) as the `ren_magic_foundations` fan-in dep — this is the un-migrated Neo-Vitae A1 anchor flagged in preamble §7. Not a spine break (it still grants the proof), but it is the known magic-spine migration debt. | `team_grant.js:` maps `0B03101000000039 -> ren_magic_foundations_complete` |

No SOFTLOCK, no BROKEN, no CANON violations found in the capstone spine or the atomic
ordering. The upper-age spine is structurally sound and correctly gated.

## Run log (key proof commands)
- `grep -rn "astages add {p}" chapters/*.snbt` — 68 unique stage grants
- transitive-ancestor walk over all `dependencies:` arrays — all 8 grants + final PASS
- `grep -rhoE 'entity: "..."' chapters/*.snbt` — all preamble bosses present as kill tasks
- `aoa_astages_team_grant.js:1-90` — authoritative quest-id -> stage map, matches chapters
- `aoa_astages_01p_gap_closure.js:157-161` — MI quantum armor = atomic (intentional split)
- `aoa_astages_01h_modern_industrialization.js:166-169` — MI quantum machines = otherworldly
