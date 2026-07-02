# DEFECT LEDGER — Phase 0 verification pass — 2026-07-02

Produced by 9 parallel Opus audit agents + CC (Claude Code) independent re-verification.
Full evidence per audit lives in `phase0/` (A_tier_softlock*.md, B_create_coverage.md,
C_D_neovitae_weaves.md, E_F_structure_deps.md, G_illegal_targets.md, H1/H2/H3_progression_*.md,
I_fomo_coverage.md, plus the scripts `tier_audit.py` / `ef_audit.py` / `scratch/diff.py`).
Scope additions vs the 02 prompt (user directives 2026-07-02): illegal-target scan
(no non-boss mob quests, no decor/variant quests → ftbfiltersystem smart_filter), full
progression-philosophy critique, FOMO mod-coverage pass, Deeper & Darker late-Ren/IR split.

**CC sign-off: SIGNED.** Re-verified by hand: all 12 SOFTLOCK rows (items in chapters +
locks at `aoa_astages_01m_magic.js:133-159`, tag defense `06_ore_restrictions.js:846-851`);
Neo Vitae A1 (aggregator `0B0310100000CAFE` deps F&A node `0B03101000000039`,
`ren_magic_foundations.snbt` ~line 2131-2141); independent scripted 10% sample of the tier
table (262/264 verified; 2 flagged rows are documented smart_filter parse blind spots).

---

## Ledger

| # | severity | class | location | finding | owner | proof |
|---|----------|-------|----------|---------|-------|-------|
| 1 | SOFTLOCK | tier | ren_nether_threshold: 0B03102000000041/42/46/47/81 | Hellforged chain (dust/ingot/parts/block) + spiritus_gem_petty quested in Renaissance; all locked industrial_revolution (source = IR-gated neovitae:dungeon) | CANON CALL then Fable | 01m_magic.js:133,145-149 |
| 2 | SOFTLOCK | tier | ren_magic_foundations: 0B03101000000038/70/75 | spiritus_gem_petty/lesser/common quested in Renaissance, locked IR | CANON CALL then Fable | 01m_magic.js:133-135 |
| 3 | SOFTLOCK | tier | ir_magic_feedstock…: 49540B100000001B-1E | Sentient armor set quested in IR, locked gilded_age | CANON CALL then Fable | 01m_magic.js:153-156 |
| 4 | BROKEN | prose | en_us.snbt | 10 real missing quest_desc: 4×g6 (051AB096CA0848B4, A818144300D946A8, 7C0AC10000000001/02) + 2×ren_archive + 2×ren_nether + 2×what_waits_in_the_grove (56 Journey mirrors excluded by design) | Opus | E_F report |
| 5 | BROKEN | weave | extendedcrafting:advanced_table | Gilded weave claims g1 teaches it; g1 doesn't — item quested only in asc1, so the woven recipe is untaught in its own age | Fable | H2 report |
| 6 | BROKEN | quest targets | minecolonies.snbt (Annex) | 56 vanilla `minecraft:` item tasks (armor/beds/dyes/ores) — violates no-vanilla rule | Fable | G report |
| 7 | CANON | design | what_waits_in_the_grove | 29-node kill bestiary; 14 ordinary-mob kill quests (born_in_chaos/monsterplus/mowzies) violate boss-only-kill rule — largest illegal cluster | CANON CALL then Fable | G report |
| 8 | CANON | design | ren_deeper_darker_otherside | USER DIRECTIVE: chapter reachable day-one yet is sole structural prereq of Maledictus capstone; Warden > dragon difficulty. Split: crossing stays late-Ren; gear tail (warden_carapace 8E, warden/resonarium smithing templates 8F/8D, sonorous_staff) → early IR, hosted in ir_netherite_citadel_obsidilith. Cheap: stage ren_deeper_darker_otherside_complete is granted but never consumed | Fable (structure) | H1+H2 reports |
| 9 | CANON | anchor | ren_magic_foundations.snbt ~2131 | Neo Vitae anchor A1 unfixed: F&A node 0B03101000000039 still fans into capstone aggregator 0B0310100000CAFE (A2/A3 done; #aoa:magic_feedstock verified) | Fable | C_D report; CC re-verified |
| 10 | CANON | gating | aoa_astages_01m_magic.js:31-35 | Hephaestus Forge tiers non-monotonic (T1 ren/T2 IR/T3 gilded/T4 ren/T5 ren) | CANON CALL | C_D report |
| 11 | CANON | coverage | IR/Gilded | Mekanism base processing spine has ZERO IR/Gilded quest home (all 185 Mek quests live in Atomic) despite canon "Mek starts IR" | CANON CALL | H2 report |
| 12 | CANON | tier | metallurgy (Medieval) | 19 unlocked immersiveengineering:* items (manual/coke/hammer/wire) — family floor is IR; likely intentional bootstrap, needs ruling | CANON CALL | A report |
| 13 | CANON | tier | ren_observation_experimentation | modern_industrialization bronze_plate/bronze_gear tasks (MI floor = IR), unlocked | CANON CALL | A report |
| 14 | CANON | quest targets | 3 Dark Ages chapters | 34 vanilla `minecraft:` item tasks — survival minimalism vs no-vanilla-ever rule | CANON CALL | G report |
| 15 | CANON | design | Dark→Medieval grant 097AED7C91033D5E | Fans in a single drafting_table quest, not the two Dark survival chapters — diverges from fan-in invariant | CANON CALL | H1 report |
| 16 | CANON | design | ren_second_mill_steam_rail_logistics | Only Ren chapter granting no stage / not fanned into age capstone — confirm optional-by-design | CANON CALL | H1 report |
| 17 | CANON | kills | alchemists_garden:gnome/yeti (Dark, m3) | Non-optional non-boss kill tasks | CANON CALL then Fable | H1+G reports |
| 18 | CANON | variants | metallurgy black_foundry_* (5 nodes) | Forces black variant of productivemetalworks foundry; 16 free-recolor variants exist — convert to smart_filter accepting any color | Fable | G report |
| 19 | CANON | filler | g2_the_refinery | Industrial Foregoing every-machine tour (71 machines/61 quests) — trim utility fleet, keep laser/mob/black-hole/bioreactor showpieces | Fable | H2 report |
| 20 | CANON | dupes | at7: 4358011000EE0008 + 0009 | Same bare neovitae:demonite_trim_ingot tasked twice in adjacent quests | Fable | G report |
| 21 | HYGIENE | prose | en_us.snbt | 87 em dashes (55 = Journey mirrors, 23 real keys: ow6, ren_nether, at7, ren_archive, grove, g1, ren_observation) | Opus | E_F report |
| 22 | HYGIENE | format | ow6 4256011000EE0001-0007 | 7 non-array quest_desc (same nodes carry em dashes) — normalize | Codex | E_F report |
| 23 | HYGIENE | naming | entering_the_iron_era.snbt | Dark Ages chapter titled "Entering the Medieval Age"; internal filename field matches file; zero external refs (safe to retitle/rename later) | Codex | E_F report |
| 24 | HYGIENE | registry | astages_00_register | 11 inert legacy proof stages registered but never granted/consumed | Codex | H3 report |
| 25 | HYGIENE | decor | ~4 pure-decor + 5 variant nodes pack-wide | Retarget or smart_filter (detail in G report) | Fable | G report |

## Clean bills of health (verified, not assumed)

- **Capstone spine: PASS all 8 ages.** Every age grant fans in every registered domain
  proof; boss chain matches canon (macabre×4 + geburah, leviathan, draconic_guardian);
  grants fire via FTBQ `/astages add {p} <stage> true true`. g_temporal is co-granted on
  the void_titan node 5057011000000003 which IS a dep of the atomic grant — not a gap.
- **Dependency graph: 1930 quests, 0 dangling, 0 duplicates, 0 orphans, 0 backward-age deps.**
- **KubeJS: 73/73 node --check PASS; 0 phantom ids in weaves/bridges** (~90 spot-verified).
- **at6 gap is clean** (no file, no references). No Create vanilla-output task traps found.
- **Tier table: 2646 item tasks, 2614 OK.**

## Buildout inputs (for prompts 03-06, not defects)

- **Create gaps (B):** create_sa engines→drone/drill line (Renaissance; do NOT gate/quest
  flight — user decision), createmetalwork molten-yield loop, createaddition low/high
  current teaching node, create_new_age entry rung, create_integrated_farming mechanics.
- **FOMO zero/under-covered content mods (I):** 13 ZERO / 19 UNDER. Top: relics (Ren, 26
  locks!), artifacts (Ren), psi (IR, chapter-worthy), railways/Steam 'n' Rails (fold into
  Second Mill — current rail chapter only quests createrailwaysnavigator), create_dragons_plus,
  mm_farming (IR), zoniex (Ren, 11 locks), alexsmobs gear. Gaps concentrate in Renaissance + IR.
  Corrections: hybrid_aquatic is covered (namespace is hyphenated); ftboceanmobs being dropped.
- **OW buildout:** Stellaris planet loop, MI fusion/plasma/superconductor line, Mek fusion beat.
- **Ascension buildout:** Re:Avaritia neutronium chain, Extended Crafting elite/crystaltine,
  Oritech apex expansion (asc4 thinnest lane at 6 items).

## Addendum 2026-07-02 — user canon calls + research pass (reports J/K/L in phase0/)

**User rulings on the ledger:**
- Rows 6/14/17/25 + the vanilla/decor/kill legality rules are GO-FORWARD ONLY — existing
  cluster-2 content stays. Rules bind new authoring.
- Row 19 WITHDRAWN: density is welcome ("every machine" questing is fine); the only
  defect class is the exact same item quested twice (row 20 stands).
- Coverage verdicts: zoniex / relics / artifacts = NOT quested. Steam 'n' Rails = a couple
  quests max. Psi = never required. Avaritia / Stellaris / MI / Extended Crafting = quest
  thoroughly (OW/Ascension buildout).
- Row 7 (grove): rework approved in principle — brainstorm delivered (L report), no changes yet.

**Neo Vitae resolution (J report, jar-verified; CC spot-checked sentient recipe chain):**
- Rows 1-2 (8 SOFTLOCK rows): QUESTS are wrong, locks right. Hellforged is Demon-Realm-only
  (IR-gated dungeon, correctly); spiritus gems need the IR Hellfire Forge. MOVE all 8 nodes
  from ren_nether_threshold/ren_magic_foundations to an IR magic chapter
  (ir_magic_feedstock_and_spectrum_network is the natural host).
- Row 3 (4 SOFTLOCK rows): LOCK is wrong. Sentient armor = Alchemy Array craft
  (reagent_binding [alchemytable: glowstone/redstone/gunpowder/gold nugget, upgradeLevel 3]
  + iron armor piece) — IR-capable. Down-tier the 4 locks gilded_age→industrial_revolution
  (01m_magic.js:153-156). Gilded keeps greater/grand gems, high orbs, T5 altar, rituals.
- Boss-buildup result: Renaissance stays clean for Maledictus; Hellfire Forge + Demon Realm
  + gems + sentient armor form the IR arc toward Obsidilith; Grand-gem/orb ceiling stays
  Gilded for Void Titan.

**Grove rework (L report):** recommended Concept B "Arm Yourself Against the Dark" — three
equip-lanes (Mowzies beast-gear / Born-in-Chaos dark-metal armory / Monster Plus relics)
feeding the unchanged 4-boss Great Hunt gate; ~22-26 nodes, zero ordinary kills, all
load-bearing ids preserved (capstone 6D7E8F901A2B1054 is the pack's sole the_renaissance
grant). Open canon call: are born_in_chaos supreme_bonescaller / sir_pumpkinhead /
dire_hound_leader bosses (keep kills) or ordinary (retarget to drops)?

**Reference packs (K report):** 15 tagged takeaways; headline adopts — protect the reveal
(audit that early chapters never preview later-age items in text/icon), extend age-tier
discipline to REWARD TABLES (ATM10's loudest failure), every obtuse weave ships teaching
prose (E2:E), avoid dimension-as-pure-time-gate + mid-age process grind (SevTech's named
resentments; AoA's Ren dimension gates + Gilded/Atomic band are the risk zones).

## Plain-English summary

The pack is structurally coherent: the full 8-age capstone spine, the dependency graph, and
every KubeJS weave check out clean — the skeleton is trustworthy to build on. The defects
cluster in exactly two places: (1) the mid-migration Neo Vitae magic spine (all 12 softlocks,
the A1 anchor, and the Hephaestus tier bug are one workstream), and (2) quest-target legality
in the oldest chapters (grove bestiary, vanilla items, black-foundry variants), which predate
the current rules. Top 5 before buildout: fix the Neo Vitae tier boundary (rows 1-3 + 9-10,
one canon call decides move-quests-vs-down-tier-locks); execute the Deeper & Darker
late-Ren→IR split (row 8); replace the grove bestiary + non-boss kills (rows 7/17); purge
vanilla/variant/decor targets (rows 6/14/18/25); give Mekanism its IR home or re-canon it
(row 11). Prose debt (rows 4/21/22) is a single Opus pass.
