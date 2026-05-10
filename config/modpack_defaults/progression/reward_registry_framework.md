# AoA Reward Registry Framework

## Purpose

This file defines the reusable reward architecture for the AoA questbook.

It is designed to let future quest passes assign rewards by stable registry ids instead of hand-picking item rewards for every quest.

This pass is framework-only:

- define classes
- define quality tiers
- define age reward identity
- define reusable registry ids
- define mapping rules from quest type -> reward type
- define crate pool behavior

It is **not** a global reward placement pass.

## Scope And Non-Goals

### In Scope

- reusable reward classes (`support`, `choice`, `themed cache`, `boss/jackpot`, `proof`)
- tier policy (`T0` -> `T4`)
- age identity constraints for rewards
- stable id naming and registry families
- crate pool structure and roll policy
- quest-type mapping policy

### Out Of Scope

- assigning final rewards to the whole questbook
- converting every live quest to reward-bearing in one batch
- adding late-age identity items to early random crates
- stage migration or chapter-flow redesign

## Reward Classes

| class | purpose | typical use | strength envelope |
| --- | --- | --- | --- |
| `support_bundle` | reduce friction in active branch | ordinary progression, first-use quests, utility support beats | low to medium |
| `choice_bundle` | prevent branch dead-ends and over-constraining one recipe path | branch openers, branch completion, chapter completion | low to medium |
| `themed_cache` | reinforce chapter identity through curated crate-style rewards | branch completion, chapter completion, denser side arcs | medium to strong |
| `rare_boss_cache` | exciting, bounded combat payoff | boss validators, optional boss annexes, major capstones | strong but controlled |
| `proof_symbolic` | milestone marker with minimal power impact | gate quests, boss proofs, transition proofs | symbolic / low power |

## Tier Policy

| tier | label | purpose | suitable quest types | power ceiling | must not include |
| --- | --- | --- | --- | --- | --- |
| `T0` | utility drip | tiny sustain and route relief | ordinary build/use, tiny support beats | convenience only | age-defining metals, stage-skipping machines, late-network blocks |
| `T1` | meaningful support | practical lane assistance | ordinary build/use, first payoff, branch openers | one clear support improvement | progression-finishing outputs, premium combat jackpots |
| `T2` | strong themed cache | chapter-identity reward | branch completion, chapter completion | compact but noticeable package | full branch completion by reward alone |
| `T3` | rare/boss cache | conquest reward surface | boss validators, dangerous branch capstones | exciting bounded jackpot chance | cross-age identity skip rewards |
| `T4` | prestige/capstone cache | late-age convergence reward | final capstones, prestige milestones | high-value, still stage-safe | free full-system bypasses before the owning age |

## Age Reward Identity

| age | reward tone | good reward families | avoid |
| --- | --- | --- | --- |
| Stone Age | survival relief and route safety | food/water/medicine packs, primitive route kits, basic treasure caches | iron+, diamond+, advanced machine parts |
| Mechanical Age | workshop maturity and first machine comfort | Create support, storage relief, food-processing support, dungeon prep kits | industrial pressure systems, digital network cores |
| Expedition Age | outward preparation and dangerous travel support | explorer kits, realm prep, bounded magic/combat support, travel/route caches | full realm ladders, late factory identity packs |
| Automation Age | machine-campus startup and buffer stability | startup machine packs, routing buffers, first grid stabilization bundles | full industrial specialization jackpots |
| Industrial Age | process specialization and factory throughput | metal/process choices, petroleum/pressure/control packs, synthetic support | nuclear reactors, strategic-force gear |
| Nuclear Age | hazardous facility resilience | containment kits, hardened-grid caches, reactor support, strategic-force support | space-launch owner-specific rewards |
| Space Age | launch and remote operations | launch prep kits, orbital survival caches, off-world logistics packs | ascension-only prestige artifacts |
| Ascension | prestige convergence and reliquary rewards | catalyst bundles, convergence choices, capstone reliquary caches | low-tier filler packs as main rewards |

## Registry Id Convention

Use this shape:

`<age_or_global>_<theme_or_family>_<tier_or_variant>_<class>`

Examples:

- `stone_survival_t0_bundle`
- `mechanical_workshop_t1_bundle`
- `mechanical_storage_choice_1`
- `expedition_explorer_cache_t2`
- `industrial_petroleum_choice_1`
- `nuclear_hardened_grid_cache_t2`
- `industrial_boss_cache_t3`
- `ascension_proof_reward`
- `bonus_roll_low_utility`

Rules:

- ids are stable once introduced
- ids represent reusable families, not one-off quest jokes
- keep age identity in ids when age-bound
- keep `global_`/`bonus_` prefix for cross-age pools

## Registry Families

Primary families covered by this framework:

- utility/support packs
- food/travel packs
- workshop packs
- exploration packs
- storage/logistics packs
- factory/process packs
- industrial specialization packs
- nuclear hazard/containment packs
- prestige/convergence packs
- proof/trophy rewards
- bonus-roll pools (`low`, `mid`, `rare`, `jackpot`)

The structured library lives in:

- [`reward_registry_ids.json`](/C:/Users/andre/curseforge/minecraft/Instances/Ascension%20of%20Ages%20(test5)_/config/progression/reward_registry_ids.json)

## Quest Type -> Reward Mapping Policy

| quest type | preferred class | tier range | random/choice guidance | avoid |
| --- | --- | --- | --- | --- |
| ordinary build/use | `support_bundle` | `T0-T1` | optional low-roll bonus only | high-tier jackpots |
| branch opener | `support_bundle` or `choice_bundle` | `T1` | choice preferred if multiple valid starts | forcing one rigid recipe lane |
| first-use/payoff | `support_bundle` + optional small `themed_cache` | `T1-T2` | low variance | rewards that replace the system just taught |
| branch completion | `themed_cache` or `choice_bundle` | `T2` | one deterministic + one weighted roll | huge random jackpot dominance |
| chapter completion | `themed_cache` + optional low rare roll | `T2-T3` | curated weighted pool | full age leap rewards |
| gate quest | `proof_symbolic` + light support | `proof + T0/T1` | mostly deterministic | gate rewards that bypass next age |
| boss validator | `proof_symbolic` + `rare_boss_cache` | `proof + T3` | bounded rare/jackpot chance | guaranteed late-age identity items |
| optional boss annex | `rare_boss_cache` | `T3-T4` | higher jackpot chance allowed | mandatory-spine power bypass |
| prestige/final capstone | `proof_symbolic` + high cache | `T4` | curated high-value + symbolic | low-value clutter bundles |

## Crate Pool Structure

Pool bands:

- `common`: routine utility and sustain
- `useful`: stronger branch support pieces
- `rare`: high-value bounded components
- `jackpot`: exciting, tightly gated highlights

Default weighting:

- `T1`: `common 70`, `useful 30`, `rare 0`, `jackpot 0`
- `T2`: `common 45`, `useful 45`, `rare 10`, `jackpot 0`
- `T3`: `common 20`, `useful 50`, `rare 25`, `jackpot 5`
- `T4`: `common 0`, `useful 35`, `rare 45`, `jackpot 20`

Default crate assembly guidance:

- support bundle: deterministic profile, no jackpot roll
- themed cache: deterministic core + weighted roll set
- boss cache: deterministic proof-support + weighted rare/jackpot rolls
- proof reward: deterministic symbolic token

## Installed Mod Ecosystem Grounding

The registry is grounded in live installed ecosystems, including:

- food/survival: `FarmersDelight`, `Aquaculture`, `Ocean's Delight`
- workshop/mechanical: `Create`, `Create Integrated Farming`, `Slice and Dice`, `Create Additions`, `Immersive Engineering`
- storage/logistics: `Sophisticated Storage`, `Sophisticated Backpacks`, `Iron Chests`, `AE2`, `Refined Storage`
- expedition support: `Ars Nouveau`, `Apotheosis`, `Artifacts`, `Relics`, `NauTec`, `Small Ships`
- industrial clusters: `Oritech`, `Modern Industrialization`, `Industrial Foregoing`, `Hostile Neural Networks`, `PneumaticCraft`, `Integrated Dynamics`, `TFMG`
- nuclear clusters: `Mekanism`, `Ballistix`, `Nuclear Science`, `Electrodynamics`, `Dynamic Electricity`, `Applied Mekanistics`
- space/ascension anchors: `Stellaris` (space-owner-agnostic layer retained), `ProjectE`, `Dyson Cube Project`, `Re-Avaritia`

## Progression Safety Rules

Always enforce:

1. no reward should bypass the current chapter's taught loop
2. no early crate should grant late-age identity-defining machinery
3. gate and boss quests should prefer proof + bounded payoff, not lane replacement
4. optional jackpots should be exciting but never stage-collapsing
5. deterministic support is preferred over high-variance lotteries in early/mid ages

## Tiny Sample Uses (Illustrative Only)

These are examples to prove framework usability, not a full rollout:

1. Mechanical branch opener:
   - `mechanical_workshop_t1_bundle`
   - optional `bonus_roll_low_utility`
2. Expedition branch completion:
   - `expedition_explorer_cache_t2`
   - `expedition_route_choice_1`
3. Nuclear boss validator:
   - `nuclear_boss_cache_t3`
   - `nuclear_gate_proof_mark`

## Next Pass Integration

When assigning live rewards in future passes:

1. select quest type policy
2. pick one registry id per class (usually 1-2 total rewards)
3. validate tier safety against age identity
4. apply to quests in targeted chapter only (no global sweep)
5. record placements in change log with ids used

