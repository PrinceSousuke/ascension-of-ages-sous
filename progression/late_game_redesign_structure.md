# Late-Game Redesign Structure

## Purpose

This file is the source-of-truth for the late-game redesign that begins after `Automation Age`.

It exists to solve five structural problems at once:

- `Industrial Age` is currently doing too much at once.
- `Mekanism`-scale hazardous tech has no truthful home between ordinary factories and off-world play.
- `Space Age` is overloaded because it currently owns both pre-launch hazardous escalation and true off-world progression.
- several installed late-game content mods are under-positioned or flattened into generic "more tech" placement.
- the boss framework after `Industrial Age` is not yet aligned to the real mod set.

This document is planning authority for:

- the insertion of `Nuclear Age`
- late-game age identity and boundaries
- mod and cluster placement from `Industrial` onward
- late-game chapter architecture
- late-game boss ownership
- late-game quest-writing standards

## Protected Ground

Do not rewrite or replace the current authored quest graph in this redesign pass.

Current live authored late-game foundation to preserve:

- `industrial_nether_logistics_and_ore_escalation`
- `industrial_oritech`
- `industrial_factory_logistics`
- `industrial_power_grids`
- `industrial_modern_industrialization`
- `industrial_create_process_infrastructure`
- `industrial_petroleum_and_extraction`
- `industrial_industrial_foregoing`
- `industrial_hostile_neural_networks`

The redesign below expands around those chapters and reclassifies their long-term ownership where needed.

## Phase 1 Audit

### What is working

- `Automation Age` already has a believable opening factory identity through Oritech, routing, and first stable power.
- `Industrial Age` already has the right kinds of live support arcs: MI, Create industrial support, petroleum, IF, and bounded HNN.
- the current live quest graph already teaches the player that Expedition feeds Automation and Automation feeds larger factory systems.
- the late-game modlist is strong enough to support a real post-Industrial bridge instead of jumping straight to "Space means everything advanced."

### What is underdeveloped

- `Industrial Age` does not yet feel like a fully owned factory-campus age because too many future systems are still waiting off-screen.
- `Mekanism`, `Ballistix`, `Nuclear Science`, `Dynamic Electricity`, `Advanced AE`, `Applied Mekanistics`, `Stellaris`, `Draconic Evolution`, `ProjectE`, `Dyson Cube Project`, and `Re-Avaritia` are not yet given a coherent place in the age ladder.
- late-game boss surfaces exist in the modlist, but they are not yet organized into one readable progression story after `Industrial`.

### What is misplaced

- `Mekanism Core` living in `Space Age` is too late for a mod family that includes hazardous chemical processing, reactors, containment-minded infrastructure, military tooling, and advanced facility logic.
- `Space Age` is currently acting as both "hazardous terrestrial escalation" and "actual launch/off-world progression."
- `Extreme Reactors` and related power content are only represented as early grid support right now, which understates their reactor-scale role.

### What is missing

- `Nuclear Age` as the bridge between mature industry and off-world capability
- a truthful late-game home for:
  - hazardous power
  - isotopes and reactor infrastructure
  - strategic weapons and defense systems
  - chemical logistics
  - hardened facility infrastructure
  - pre-launch launch-authorization pressure
- a true off-world-owned `Space Age` instead of treating space as a generic "late tech" bucket

### Where pacing breaks

- the jump from `Industrial factory mastery` to `Space-scale systems` is too large.
- `Industrial Age` currently risks bloat because it wants to own every serious machine system.
- `Space Age` currently risks incoherence because it wants to own both launch prep and every advanced terrestrial technology.

## Revised Age Structure

| age | identity | what completion should mean |
| --- | --- | --- |
| Stone | survival stabilization | the player can reliably live, travel, and recover |
| Mechanical Age | first machine space | the player can run an honest workshop and support basic structure travel |
| Expedition Age | breadth and outward travel | the player can survive realms, branch into multiple systems, and conquer the Nether capstone |
| Automation Age | first powered factory | the player can run repeatable machine lines with routing, stock, and stable grids |
| Industrial | factory-campus maturity | the base becomes a serious industrial site with metallurgy, fluids, throughput, petroleum, control, and branch specialization |
| Nuclear | hazardous escalation | the player can run reactors, containment, chemical logistics, strategic force, and hardened infrastructure safely |
| Space | launch and off-world mastery | the player can leave the world, sustain remote operations, and scale advanced networks, synthesis, and cosmic-grade power |
| Ascension | prestige convergence | every late system is folded into final synthesis, prestige crafting, and world-shaping power |

## Late-Age Boundaries

### Industrial Age

Industrial owns:

- serious factory depth
- metallurgy and process chains
- shared petroleum backbone
- broader machine specialization
- mature routing and control
- dragonfall pressure

Industrial does **not** fully own:

- hazard-scale reactors as the main identity
- antimatter-tier Mekanism
- large military hardware as the main loop
- off-world launch infrastructure

### Nuclear Age

Nuclear owns:

- Mekanism hazardous processing as a real progression pillar
- reactor and isotope infrastructure
- containment, shielding, and hardened-grid logic
- military and defense systems
- chemical storage and transport
- pre-launch strategic maturity

Nuclear does **not** fully own:

- rocket launch and life-support as its main identity
- planetary/off-world logistics
- full prestige crafting

### Space Age

Space owns:

- launch pads, rockets, oxygen, and stations
- off-world materials and logistics
- advanced digital scaling
- late cosmic refinement
- Draconic-tier escalation
- off-world synthesis and infrastructure

Space does **not** own:

- the first truthful hazardous power bridge
- the first truthful military/defense bridge
- the entire prestige economy

### Ascension

Ascension owns:

- prestige crafting
- exchange ethics
- mega-project progression
- final convergence of power, synthesis, and boss progression

## Mod-To-Age Placement Map

| cluster | primary age | secondary age | role | why it belongs there | what it unlocks or supports |
| --- | --- | --- | --- | --- | --- |
| `Oritech + Oritech Things` | Automation | Industrial | main pillar | first honest powered-processing spine and later exotic-machine payoff | factory throughput, late Create/Oritech bridges, early industrial literacy |
| `Modern Industrialization + Extended Industrialization + Modern Dynamics + MI Sound Addon` | Industrial | Nuclear | main pillar | layered metallurgy and process-heavy factory play fit mature industry better than Automation | petroleum consumption, heavier routing, steel and beyond, late factory scale |
| `Create + Create Additions + Create New Age + Create Metalwork + Create Oritech Compat` | Industrial | Nuclear | secondary pillar | Create should remain meaningful as transport, fluid, heat, electric-bridge, and integration support | MI/Oritech support, petroleum handling, branch throughput, reactor support bridges |
| `TFMG + Create Ore Excavation + Railways` | Industrial | Nuclear | main pillar | shared extraction and petroleum infrastructure belongs in the industrial campus stage | PneumaticCraft, long-distance fuel, heavier factory specialization |
| `Industrial Foregoing + Souls` | Industrial | Nuclear | main pillar | large-scale applied automation, fluid, rubber, and farm systems fit factory maturity first | HNN, later synthesis, MA integration |
| `PneumaticCraft + Applied Pneumatics` | Industrial | Nuclear | secondary pillar | pressure logic is industrial specialization that should consume shared oil rather than compete with it | advanced control, processing specialization, later air-to-digital integration |
| `Integrated Dynamics + Tunnels + Crafting + Terminals` | Industrial | Nuclear | support pillar | high-control routing belongs after the factory campus is already real | logistic intelligence, automation policy, digital handoff |
| `Hostile Neural Networks + Hostile Neural Industrialization` | Industrial | Space | secondary pillar | first mob-data loops belong in Industrial, but serious synthesis belongs later | MA, synthesis, off-world farming shortcuts only after later gates |
| `Mekanism Core + Generators + Additions + Tools + MoreMachine + TFMG Compat` | Nuclear | Space | main pillar | hazardous chemicals, reactor logic, higher circuits, and facility-grade machines are the core Nuclear bridge | isotope handling, advanced power, launch-grade materials, later SPS and antimatter |
| `Nuclear Science + Ballistix + Dynamic Electricity` | Nuclear | Space | main pillar | these mods are the clearest expression of the missing bridge age: reactors, force, and hardened electrical infrastructure | strategic force, grid hardening, reactor discipline, launch authority pressure |
| `Electrodynamics + Extreme Reactors + Generator Galore` | Nuclear | Industrial | secondary pillar | the live Automation support lane is only the start; fuller reactor and grid ownership belongs in Nuclear | substation logic, scaled power, reactor campuses, heavy facility readiness |
| `Mekanism Turrets + Mekanism Lasers + Modular Force Fields + Evolved Mekanism` | Nuclear | Space | combat / defense pillar | this is strategic force, base hardening, and military tech, not ordinary factory progression | Nuclear boss prep, hardened facilities, later Space defense and hazard prep |
| `Applied Mekanistics + RS Mekanism Integration + Mekanism Covers` | Nuclear | Space | support pillar | hazardous gases, slurries, and chemical inventories need their own logistics bridge before full space-scale networks | safe chemical storage, digital chemical transport, later AE2 scaling |
| `Stellaris` | Space | Ascension | main pillar | current front-runner launch and off-world owner in the installed pack, pending the final Space-owner decision | rockets, oxygen, stations, moon/mars progression, off-world industry |
| `AE2 + AdvancedAE + ExtendedAE + Mega Cells` | Space | Ascension | main pillar | large-scale digital networks belong after hazardous material maturity and launch readiness | macro logistics, massive autocrafting, late synthesis |
| `Ender IO + Immersive Energistics` | Space | Ascension | support pillar | conduit-scale utility and cross-power integration fit post-launch infrastructure and dense remote sites | network cleanup, machine interop, remote base utility |
| `Mystical Agriculture + Mystical Agradditions + Solar Flux Reborn` | Space | Ascension | main pillar | resource multiplication and photovoltaic scale belong after off-world systems and late power discipline | late synthesis, prestige resources, long-horizon automation |
| `Draconic Evolution + Draconic Additions` | Space | Ascension | main pillar | reactor-scale instability, chaos materials, and draconic combat/power belong after launch and late network maturity | ascension threshold, chaos resources, prestige combat |
| `Extended Crafting + Modular Machinery Reborn + Modular Machinery Reborn Mekanism` | Ascension | Ascension | main pillar | prestige fabrication backbone for ultimate multi-system recipes | ProjectE, Dyson, Avaritia, final convergence |
| `ProjectE` | Ascension | Ascension | prestige pillar | exchange trivializes too much if opened earlier | prestige economy, EMC ethics, final optimization |
| `Dyson Cube Project` | Ascension | Ascension | prestige pillar | macro-project payoff belongs after off-world and draconic scale | mega-project progression, final energy/economy goals |
| `Re-Avaritia` | Ascension | Ascension | final capstone | final prestige crafting and impossible-scale resource convergence must remain last | final completion state and prestige boss access |

## Revised Chapter Structure

### Industrial Age

| chapter id | chapter identity | spine node | branch nodes | mods served | completion / handoff | why it belongs here |
| --- | --- | --- | --- | --- | --- | --- |
| `industrial_oritech_escalation` | heavier Oritech campus | advanced machine chaining and denser exotic-material throughput | atomic forge support, foundry support, deeper drill, accelerator-field support | Oritech, Oritech Things | proves the player can operate a serious powered line instead of a starter shop | Oritech is still the clearest bridge from Automation into true industry |
| `industrial_modern_industrialization` | layered process industry | steam-to-electric-to-serious metallurgy spine | bronze and steel branches, machine specialization, first digital discipline, routing expansion | MI, Extended MI, Modern Dynamics | establishes Industrial as process-heavy and serious | MI should be one of the age's main pillars |
| `industrial_create_process_infrastructure` | mechanical megaprocess support | larger fluid, heat, energising, and rolling infrastructure | Create New Age electrical support, Create Additions power bridges, molten handling, compat alloys | Create family, Assembly Line | supplies physical infrastructure to the other factory spines | Create remains meaningful as support, not the only mainline |
| `industrial_petroleum_and_extraction` | oil and extraction backbone | pumpjack and distillation spine | anchored extraction, fuel movement, rail fuel delivery, large-scale surveying | TFMG, Create Ore Excavation, Railways | opens the shared petroleum backbone for later branches | this is the age where the factory starts consuming real fuel systems |
| `industrial_industrial_foregoing` | applied automation | latex-to-plastic-to-utility machines spine | plant automation, biofuel, fluid utility, souls setup | Industrial Foregoing, IF Souls | creates the first large-scale "applied industry" branch | IF is a factory multiplier, not a token side quest |
| `industrial_pneumaticcraft` | pressure specialization | first honest pressure-processing spine | air tools, specialty processing, later applied pneumatics bridge | PneumaticCraft, Applied Pneumatics | adds controlled specialization without replacing the shared oil backbone | pressure logic is a specialization layer, not a rival industry tree |
| `industrial_integrated_dynamics` | industrial control logic | variable/control spine | tunnels, terminals, crafting logic, sensor policies | Integrated Dynamics stack | upgrades the factory from throughput to decision-making | logistics should mature into control here |
| `industrial_hostile_neural_networks` | simulated resource discipline | first serious model-to-output spine | controlled mob predictions, later HNI bridge, future synthesis hooks | HNN, HNI, IF | creates the first synthetic-resource foundation without exploding balance | Industrial is the first honest place for bounded mob simulation |
| `dragonfall_and_end_access` | industrial conquest threshold | End access, dragon prep, and the move into post-dragon scale | branch-prep checks from MI, IF, Oritech, and petroleum | Minecraft plus late Industrial branches | unlocks Nuclear Age after real factory and combat competence | Industrial should end on conquest, not just machine count |
| `industrial_boss_hunts` | cataclysmic industrial threats | mandatory branch bosses before Dragonfall | Cataclysm, Alex's Caves, Ice and Fire branch order | Cataclysmic threat cluster | keeps harder bosses legible and staged | industrial combat should test factory-backed power, not random wandering |

### Nuclear Age

| chapter id | chapter identity | spine node | branch nodes | mods served | completion / handoff | why it belongs here |
| --- | --- | --- | --- | --- | --- | --- |
| `nuclear_entry_and_containment_protocols` | age entry and hazard discipline | sealed-facility mindset and containment readiness | shielding, waste awareness, radiation handling, facility zoning | Minecraft, Mekanism support, Nuclear Science support | tells the player this age is about safe operation, not just bigger machines | Nuclear needs a distinct identity immediately |
| `nuclear_mekanism_processing_and_chemicals` | hazardous machine backbone | higher-tier Mekanism processing and chemical routing | slurries, gases, infusing, factory upgrades, advanced circuits | Mekanism core, MoreMachine, compat | proves the player can run hazardous processing lines | this is the clearest missing bridge between industry and space |
| `nuclear_reactors_isotopes_and_hazardous_power` | reactor and isotope campus | fission-grade and isotope-ready infrastructure | coolant, waste handling, nuclear science machines, reactor peripherals | Mekanism Generators, Nuclear Science, Extreme Reactors, Create New Age support | transitions from ordinary grids into dangerous power | hazardous energy deserves its own age, not a side lane |
| `nuclear_strategic_power_and_hardened_grids` | high-voltage facility support | substations, transformers, buffers, hardened lines | dynamic electricity machines, electrodynamics infrastructure, generator specialization | Electrodynamics, Dynamic Electricity, Generator Galore | keeps hazardous sites stable and expandable | Nuclear should feel infrastructural, not only reactor-centric |
| `nuclear_defense_systems_and_strategic_force` | weapons and hardened defense | strategic force spine | missiles, launch systems, turrets, lasers, force fields, armored gear | Ballistix, Mekanism Turrets, Mekanism Lasers, Modular Force Fields, Evolved Mekanism | prepares the player for severe boss pressure and late-world threats | this is the military/defense identity missing from the current ladder |
| `nuclear_chemical_storage_and_digital_bridges` | hazardous logistics | digital chemical storage and transport spine | Applied Mekanistics, RS chemical bridge, covers, safe inventory discipline | Applied Mekanistics, RS Mek integration, Mekanism Covers | unlocks clean handoff into Space-scale digital logistics | hazardous materials need their own logistics curriculum |
| `space_launch_threshold` | move-on gate to Space | launch authority after hazardous mastery | requires reactor, defense, logistics, and boss completion | Nuclear branches plus boss gate | unlocks `Space Age` and the true launch chapter group | Space should open only after terrestrial hazard mastery |
| `nuclear_boss_hunts` | hazardous conquest spine | mandatory branch bosses tied to sealed-facility and military escalation | Alex's Caves toxic/technology threats, Cataclysm war-machine bosses, optional BOMD/other annex targets | Alex's Caves, Cataclysm, BOMD, other high-threat content | main-boss payoff should be a final launch-authorizing conquest surface | Nuclear combat should feel like hardened-base warfare, not generic adventuring |

### Space Age

| chapter id | chapter identity | spine node | branch nodes | mods served | completion / handoff | why it belongs here |
| --- | --- | --- | --- | --- | --- | --- |
| `space_launch_infrastructure_and_stellaris` | provisional launch ownership scaffold | rocket pad, oxygen, and first off-world trip | suit modules, station work, first moon/mars routing | current off-world owner placeholder, likely Stellaris or a later hybrid | proves the player has actually left the world and can survive there | Space needs a real owner, but this pass should not hard-bind the final choice yet |
| `space_orbital_life_support_and_logistics` | sustaining remote sites | oxygen distribution, remote resupply, return routing | station support, cargo planning, off-world staging | Stellaris plus support tech | keeps Space from being one rocket craft and done | off-world survival must feel operational |
| `space_advanced_storage_and_digital_networks` | macro digital infrastructure | late AE2 and massive storage spine | extended patterning, mega cells, large-scale automation, remote crafting | AE2, AdvancedAE, ExtendedAE, Mega Cells | gives late tech a real logistics backbone | full digital scale belongs after launch and hazardous maturity |
| `space_ender_io_networks` | conduit-era utility | conduit and machine-utility spine | remote power/fluid/item handling, integration cleanup | Ender IO, Immersive Energistics | makes remote/off-world sites cleaner and denser | Ender IO is best as space-era infrastructure support |
| `space_antimatter_and_cosmic_refinement` | post-launch hazardous refinement | SPS, antimatter, and cosmic-grade materials | late Mekanism high-end, chemical/digital synergy, exceptional late processing | Mekanism late systems, Applied Mekanistics | upgrades Nuclear tech into true cosmic-scale processing | high-end Mekanism belongs after launch, not before it |
| `space_late_game_agriculture_and_synthesis` | off-world synthesis | seed, essence, machine, and synthetic-resource convergence | IF/HNN/MA links, resource loops, photovoltaic scaling | Mystical Agriculture, Agradditions, IF, HNN, Solar Flux | supplies Ascension-scale recipe demand | synthesis must come after launch and mature power |
| `space_draconic_evolution` | cosmic power and chaos pressure | draconic tools, reactor, and chaos-resource spine | celestial manipulator, reactor control, chaos refinement, additions support | Draconic Evolution, Draconic Additions | unlocks the final Space threshold into Ascension | Draconic content is late-space, not ordinary factory progression |
| `ascension_threshold` | move-on gate to Ascension | final post-launch validation | requires advanced networks, synthesis, draconic power, and boss completion | Space branches plus boss gate | unlocks `Ascension` | Ascension should begin only after full off-world mastery |
| `space_boss_hunts` | cosmic conquest spine | post-dragon and off-world bosses | Draconic Guardian path, remaining Cataclysm/BOMD/cosmic validators | Draconic + late boss cluster | turns late combat into a readable Space campaign | Space needs a real cosmic-pressure track |

### Ascension

| chapter id | chapter identity | spine node | branch nodes | mods served | completion / handoff | why it belongs here |
| --- | --- | --- | --- | --- | --- | --- |
| `ascension_entry_and_scale_shift` | prestige tone reset | entry into final-scale progression | expectation reset, final prerequisite consolidation | Minecraft plus late-game boss output | starts final convergence cleanly | Ascension should feel distinct immediately |
| `ascension_prestige_crafting` | prestige fabrication backbone | extreme recipe infrastructure | modular machinery support, multi-system recipe convergence | Extended Crafting, MMR, MMR Mekanism | enables every other prestige branch | this is the real fabrication spine of the final age |
| `ascension_projecte_exchange_ethics` | EMC and exchange | controlled ProjectE unlock | exchange discipline, ethical gating, non-trivial late usage | ProjectE | introduces an economy-shaping system without flattening the whole pack too early | ProjectE must stay late and deliberate |
| `ascension_dyson_cube_project` | mega-project construction | Dyson structure and assembly | logistics, fabrication, resource sink discipline | Dyson Cube Project | supplies a true mega-project lane beside raw crafting power | gives Ascension a macro-scale objective |
| `ascension_avaritia_capstones` | final impossible crafting | singularity-scale and avaritia progression | late prestige resource convergence | Re-Avaritia | final crafting convergence | this is the clearest final-crafting lane |
| `ascension_boss_hunts` | prestige conquest | sequential final validators | late optional bosses and final completion threats | fdbosses, Block Factory's Bosses, ArPhEx, other final bosses | pack completion state | final combat should be legible, not random |

## Late-Game Boss Framework

| age | main progression boss track | mandatory branch bosses | boss annex role | main boss / capstone recommendation |
| --- | --- | --- | --- | --- |
| Industrial | factory-backed conquest leading into the End | early Cataclysm / Alex's Caves / Ice and Fire threats that prove the player can handle high-pressure combat with real industrial support | organize remaining non-mandatory industrial-threat bosses by mod and escalation band | `Dragonfall and End Access` remains the age main-boss surface |
| Nuclear | hazardous conquest and war-machine pressure | first hardened facility boss, then one higher-threat mechanized or toxic-world boss before launch authority opens | organize optional Alex's Caves, Cataclysm, BOMD, and similar high-threat kills into a separate annex | `space_launch_threshold` should eventually own the final move-on gate after hardened grids, strategic force, chemical logistics, and the Nuclear boss spine are all live |
| Space | post-launch cosmic conquest | one off-world validator plus one draconic or post-dragon branch boss before the main capstone | hold optional cosmic and late-dimension bosses in a readable annex order | `Draconic Guardian` or the equivalent draconic chaos path should own the main Space capstone |
| Ascension | prestige validation and final convergence | one fabrication or economy-linked validator plus one prestige branch boss before the true final boss | keep extra prestige bosses and alternate high-difficulty clears in annex form | final boss remains the end-of-pack completion surface after ProjectE, Dyson, and Avaritia are complete |

## Quest Authoring Rules

- Do not edit existing authored quests in this redesign wave.
- Every quest must teach, verify, unlock, connect, or prepare. If it does none of those, it should not exist.
- No token mod coverage. One icon quest is not real integration.
- No inaccessible requirements. Validate materials, machines, dimensions, and power before questing them.
- Chapters must be system-based bushes, not unordered item buckets.
- Support mods should solve real player pain points or integration problems. They should not masquerade as rival spines.
- Main bosses belong on the main age path. Optional bosses belong in boss annex chapters with readable unlock order.
- If a chapter payoff is quested, its support pieces must also be present somewhere nearby.
- Preserve mod identity. Do not flatten every tech mod into "more machine progression."

## Balance, Exploit, and Overlap Risks

- `Mekanism Tools`, jetpack-adjacent mobility, and strong defensive gear can trivialize Industrial combat if they leak before Nuclear.
- `Applied Mekanistics` and `RS Mekanism Integration` can trivialize hazardous transport if chemical handling is not gated behind real Nuclear logistics chapters.
- `AdvancedAE`, `ExtendedAE`, and `Mega Cells` can erase meaningful storage pressure if they arrive before Space.
- `ProjectE` must stay in Ascension or it will flatten every other late resource ladder.
- `Mystical Agriculture` and late `HNN/IF` loops can trivialize extraction if they appear before post-launch synthesis.
- `Solar Flux Reborn` can flatten power pacing if it opens before Space infrastructure and real large-scale facility demands.
- `Ballistix`, `Mekanism Lasers`, and `Modular Force Fields` can bypass intended combat difficulty if they are not kept behind Nuclear containment and boss validation.
- `Create New Age`, `Electrodynamics`, `Extreme Reactors`, and `Nuclear Science` overlap in power identity; the solution is staged ownership, not deleting one system:
  - early stable power belongs in Automation
  - factory-campus power maturity belongs in Industrial
  - hazardous reactor campuses belong in Nuclear
- `PneumaticCraft` must consume the shared petroleum chain rather than open a second oil identity.
- `Assembly Line`, `Create`, `MI`, and `Oritech` overlap in machine fantasy; keep them in different roles:
  - Create = infrastructure bridge
  - Oritech = early powered automation and late machine escalation
  - MI = serious process industry
  - Assembly Line = facility support and machine-campus flavor, not a rival main pillar

## Recommended Implementation Order

1. Keep current live Automation and Industrial chapters intact as the base of the redesign.
2. Deepen the existing Industrial spines before opening Nuclear.
3. Author `nuclear_entry_and_containment_protocols` first so Nuclear feels distinct immediately.
4. Build the Nuclear Age around three required pillars in order:
   - hazardous Mekanism processing
   - reactors and hazardous power
   - strategic force and hardened logistics
5. Open the final off-world owner only after the Nuclear main-boss surface is in place.
6. Build Space around launch, off-world logistics, advanced networks, and draconic escalation.
7. Hold ProjectE, Dyson, and Avaritia until Ascension so late-game convergence still has a real identity.
