# PLAN 02b — Renaissance + Earlier-Age Completion (STRUCTURAL DESIGN)

**Status:** DESIGN COMPLETE, ready to dispatch. **Owner chain:** Fable (structure) -> Opus (prose) -> CC (age-discipline + merge).
**Prepend `01_MASTER_PREAMBLE.md` to every dispatched task.** DESIGN ONLY doc: no config/kubejs/lang edits were made producing it.
**Authored by:** structural designer pass, 2026-07-02. All item IDs jar-verified (see Verification Log, sec. 9).

---

## 0. Executive summary + what the census got wrong

Two backlog assumptions were **falsified on disk** during this pass. The plan below is built on the corrected reality, not the backlog text.

| Backlog / 02b claim | Reality on disk | Consequence |
|---|---|---|
| Spectrum front door (pedestals, nodes, hue tools) = 0 quests, host in `ren_magic_foundations` | Confirmed 0 quests. But `ren_magic_foundations` is a **dense 4-lane chapter** (61 nodes, x=[-10.5,21.0]) with no room for a coherent Spectrum arc without crossings. Spectrum has ZERO presence in any Renaissance chapter. | **New dedicated chapter** `ren_spectrum_academy`. Rationale in sec. 1. |
| IE "coke_oven + tank intro = 0 quests" (Medieval) | **FALSE.** `metallurgy.snbt` already has a full coke-oven lane (cokebrick -> `mb_cokeoven` advancement -> coal_coke -> coke -> creosote -> treated wood) AND a `mb_tank` advancement node. The census missed them because they are **advancement tasks**, not item tasks. | P2 IE shrinks to a **3-node repair** (tank is a dead-end leaf; no bridge toward the IR multiblock fleet). Not a new lane. |
| Malum "5 elemental spirit types + ritual_plinth = no ladder" (Renaissance) | The IR chapter `ir_magic_feedstock_and_spectrum_network` already has `spirit_crucible`/`spirit_catalyzer`/`spirit_jar` (6-type smart filter)/`arcane_spirit`/`ritual_plinth`. AStages gates `spirit_crucible`+`spirit_catalyzer` to **industrial_revolution**; only `spirit_altar` is Renaissance. | The Malum "ladder" is an **IR** concern already partly covered. The Renaissance gap is narrow: the altar intro exists but the **spirit-harvest loop** (crucible/catalyzer are IR-gated, so cannot move earlier). Plan a small **Renaissance soulstone->altar->spirit-jar** completion, no IR duplication. See P2-Malum. |

`[CANON]` blockers dissolved by `AOA_QUEST_SCOPE_REGISTRY.md` (Policy 1, GATING CLOSED): **apothic_enchanting and mahoutsukai need NO gate**. Author them ungated. Nothing goes to the `08` decision queue from 02b.

**Chapter-allocation decisions (one line each):**
- **P1 Spectrum -> NEW chapter `ren_spectrum_academy`** — `ren_magic_foundations` is already a 4-lane, 61-node, 31.5-wide chapter; a coherent pedestal->fusion->instiller arc (~14 nodes) cannot be added without crossing its dependency fan. A clean new Renaissance chapter is the correct home.
- **P2 IE -> EXTEND `metallurgy`** — coke/tank lane already exists; only wire the tank leaf + add a treated-wood->IR bridge stub. First-placement-wins; no new chapter.
- **P2 Malum -> EXTEND `ren_magic_foundations`** — the Malum lane (x=-7.5..-10.5) has adjacent open space; add the soulstone-harvest completion there. Depths of Malum dimension: **SKIP** (jar has no dimension; verified sec. 9).
- **P2 Neo Vitae -> WIRE ONLY** — Ren line + IR segment both exist; add one cross-chapter reveal dependency so the graph teaches Ren->IR continuity. No new nodes.
- **P3 apothic_enchanting -> NEW small line inside `ren_observation_experimentation`** (the late-Renaissance "study/instruments" chapter) — controlled, ungated, ~6 nodes.
- **P3 mahoutsukai -> NEW explicitly-optional chapter `ren_mahou_tsukai`** — metadata optional, never a capstone dependency.

---

## 1. P1 [SPINE] — Spectrum front door: NEW chapter `ren_spectrum_academy`

**Why a new chapter (weighed 3 approaches):**
1. *Cram into `ren_magic_foundations`* — rejected. That chapter fans four vertical lanes from root `0B03101000000001` across x=[-10.5,21.0]; the only "open" band (x>21 or y<-7.5) would force the Spectrum arc's dependency lines to cross the neovitae/theurgy columns. Hard crossing-constraint violation.
2. *Cram into `ren_deeper_darker_otherside`* (which already hosts the Deeper-Down endgame) — rejected. Deeper Down is Spectrum's *late* content and is Atomic-gated at the portal (`spectrum:deeper_down_portal` = atomic). Putting the Renaissance front door in the same chapter as the atomic-tier endgame muddles age reading and risks the front-door nodes hiding behind late gates.
3. *New chapter `ren_spectrum_academy`* — chosen. Spectrum is a stated main magic pillar with literally zero questbook presence at its own gated age. It earns a tab. Clean lanes, foundation->apparatus reading, and a single outbound wire to the existing IR/Deeper-Down content.

**Chapter header (Fable authors):**
- `filename: "ren_spectrum_academy"`, `group: "0B038EB15EBBFD95"` (the_renaissance), `order_index: 11` (Second Mill is 10; this is next).
- `icon:` `spectrum:pedestal_all_basic` (Pigment Pedestal — the front door item).
- Entry node depends on Medieval->Renaissance gateway `6D7E8F901A2B1054` (in `what_waits_in_the_grove`) for progressive reveal — the tab opens when the player enters the Renaissance, matching the reveal spine.

**Node table** (all IDs jar-verified sec. 9; all Renaissance-gated per `aoa_astages_01_item_restrictions.js` L730-736 + `01m_magic.js` L64-72). Coordinates use a 0.5 grid, single-source root, three short lanes fanning right — no crossings.

| # | proposed id | x | y | deps | task | icon | flags |
|---|---|---|---|---|---|---|---|
| N1 | 0B03105000000001 | 0.0 | 0.0 | `6D7E8F901A2B1054` | item `spectrum:pigment_palette` | pigment_palette | hide_until_deps_complete (entry) |
| N2 | 0B03105000000002 | 1.5 | 0.0 | N1 | item `spectrum:color_picker` | color_picker | — |
| N3 | 0B03105000000003 | 3.0 | 0.0 | N2 | item `spectrum:titration_barrel` | titration_barrel | — |
| N4 | 0B03105000000010 | 1.5 | -1.5 | N1 | item `spectrum:pedestal_all_basic` | pedestal_all_basic | — |
| N5 | 0B03105000000011 | 3.0 | -3.0 | N4 | item(smart_filter: pedestal_basic_amethyst OR _citrine OR _topaz) | pedestal_basic_topaz | — |
| N6 | 0B03105000000012 | 4.5 | -1.5 | N5 | item `spectrum:pedestal_moonstone` | pedestal_moonstone | — |
| N7 | 0B03105000000013 | 6.0 | -1.5 | N6 | item `spectrum:pedestal_onyx` | pedestal_onyx | shape diamond (tier peak) |
| N8 | 0B03105000000020 | 4.5 | 1.5 | N3 | item(smart_filter: 5 network nodes) | provider_node | — |
| N9 | 0B03105000000021 | 6.0 | 1.5 | N8 | item `spectrum:fusion_shrine_basalt` | fusion_shrine_basalt | shape hexagon |
| N10 | 0B03105000000022 | 7.5 | 0.0 | N7,N9 | item `spectrum:spirit_instiller` | spirit_instiller | shape gear (apparatus convergence) |
| N11 | 0B03105000000023 | 9.0 | -1.5 | N10 | item `spectrum:particle_spawner` | particle_spawner | optional: true |
| N12 | 0B03105000000024 | 9.0 | 1.5 | N10 | advancement `spectrum:milestones/build_spirit_instiller` (VERIFY id sec.9 note) OR item `spectrum:ink_assortment` | ink_assortment | optional: true |

**Smart-filter nodes (FTB Filter System, `ftbfiltersystem:smart_filter`):**
- N5 accepts any basic pedestal: `spectrum:pedestal_basic_amethyst`, `spectrum:pedestal_basic_citrine`, `spectrum:pedestal_basic_topaz` (one node, per no-per-variant rule).
- N8 accepts any Pastel Network node: `spectrum:connection_node`, `spectrum:gather_node`, `spectrum:provider_node`, `spectrum:sender_node`, `spectrum:storage_node` (the "5 network nodes").

**Re-wire table (teach foundation -> endgame):** add ONE outbound reveal dependency from the existing IR Spectrum entry to this chapter's apparatus convergence, so a player pathing the IR magic chapter is shown the Renaissance apparatus was the prerequisite.

| existing node | file | current deps | ADD dep | effect |
|---|---|---|---|---|
| `49540B100000000C` (Spectrum IR entry, Paltaeria Gem) | `ir_magic_feedstock_and_spectrum_network.snbt` | `49540A100000000F` | ADD `0B03105000000022` (N10 spirit_instiller) | IR Spectrum reveals only after the Renaissance apparatus arc is built. Confirm this does not create a crossing inside the IR chapter (N10 is external, so it is a cross-file dep with no in-file line — safe). |

**Note:** do NOT move the IR-gated Spectrum machines (`enchanter`, `cinderhearth`, `crystallarieum`, `crystal_apothecary` — all IR per `01m_magic.js` L67-72) into this Renaissance chapter. They are correctly IR. This chapter stops at the Renaissance-legal apparatus.

---

## 2. P2 [FOUND] — Immersive Engineering: 3-node repair in `metallurgy` (NOT a new lane)

The coke-oven + tank onboarding the backlog wanted **already exists** (advancement tasks, missed by the census). Genuine gaps:
1. `mb_tank` node `2902E58DB70F9441` (x=6.5,y=-4.0) is a **dead-end leaf** — nothing depends on it, so the tank reads as a throwaway.
2. No bridge from the Medieval IE basics toward the IR multiblock fleet (`02c` owns the fleet, but the graph should point at it).

**Weighed:** (a) leave as-is — rejected, the tank leaf is a small teach-gap the spec explicitly names; (b) add a full second IE mini-lane — rejected, that is the IR chapter's job and would duplicate; (c) minimal repair — chosen.

**Node table** (extend `metallurgy`, group `508B59840C508057`; open space confirmed at x>12 and the y=-4 spur):

| # | proposed id | x | y | deps | task | icon | flags |
|---|---|---|---|---|---|---|---|
| M1 | 2902E58DB70F9450 | 8.0 | -4.0 | `2902E58DB70F9441` (mb_tank) | item `immersiveengineering:fluid_pump` (VERIFY sec.9) | fluid_pump | wires the tank leaf onward |
| M2 | 2902E58DB70F9451 | 9.5 | -4.0 | M1 | advancement `immersiveengineering:multiblocks/mb_crusher` | — | forward pointer to IR multiblock line |
| M3 (optional) | 2902E58DB70F9452 | 13.5 | 4.5 | `2902E58DB70F9438` (stick_treated) | item `immersiveengineering:blueprint` (VERIFY sec.9) | blueprint | optional: true |

**Rationale:** the tank now feeds a pump (fluid handling), which feeds the FIRST IR multiblock (`mb_crusher` advancement) as a visible "next age" pointer. The `02c` IR IE chapter's entry should later depend on M2 (cross-file). **This must be recorded in `LEDGER.md` as a handoff to 02c**, not authored here.

**IE lane is otherwise DONE.** Do not re-author coke oven, coke, creosote, treated wood, or connectors — they exist.

---

## 3. P2 [SPINE] — Malum: soulstone-harvest completion in `ren_magic_foundations`

**Corrected scope.** The Renaissance Malum lane already has: `spirit_altar` (root of lane, `0B03101000000006`), `alchemical_calx`, `raw_soulstone`, `refined_soulstone`, `arcane_charcoal`, `runic_workbench`, `spirit_jar` (`0B0310100000000A`), `runewood_item_pedestal` (optional). The `spirit_crucible`/`spirit_catalyzer`/`ritual_plinth` are **IR-gated** and already quested in the IR chapter — they cannot move to Renaissance (would be a cross-age inversion). So the "5 elemental spirit type ladder" is genuinely an IR concern and largely present there via the `spirit_jar` 6-type smart filter.

**The real Renaissance gap:** the altar chain teaches building the altar but not the **spirit-harvest loop** (kill mobs near a soulstone-tipped scythe -> spirits -> spirit_jar). The existing `spirit_jar` node exists but nothing teaches the harvest that fills it. Add a short, honest completion (weighed against adding nothing: the spec calls Malum SPINE and names the spirit types, so a minimal harvest teach is warranted; but per no-mob-kill-quest rule, we teach via the apparatus items, not kill tasks).

**Node table** (extend the Malum lane; open space at x=-10.5..-12, y=13.5+ below `spirit_jar` / `runewood_item_pedestal`):

| # | proposed id | x | y | deps | task | icon | flags |
|---|---|---|---|---|---|---|---|
| MA1 | 0B0310100000000B | -12.0 | 10.5 | `0B0310100000000A` (spirit_jar) | item `malum:soulstone` (the refined harvesting stone) — VERIFY exact id sec.9 | soulstone | — |
| MA2 | 0B0310100000000C | -12.0 | 12.0 | MA1 | item(smart_filter: the spirit-type set) | wicked_spirit | teaches spirit collection |
| MA3 | 0B0310100000000D | -12.0 | 13.5 | MA2 | item `malum:cracked_soul_container` OR `malum:hex` (VERIFY sec.9) | (verified icon) | optional: true |

**Spirit-type smart filter (MA2):** accept the harvestable spirits: `malum:wicked_spirit`, `malum:sacred_spirit`, `malum:infernal_spirit`, `malum:earthen_spirit`, `malum:aqueous_spirit`, `malum:arcane_spirit`, `malum:aerial_spirit`, `malum:eldritch_spirit`, `malum:umbral_spirit` (9 exist; jar-verified sec.9). One node accepts any — do NOT make 9 nodes. `min_count`/filter set covers the "5 elemental" the spec asked for plus the others the jar actually ships.

**Gate work:** NONE (Policy 1). The spirit types are ungated by design; leave them.
**Depths of Malum dimension:** **SKIP.** The malum jar contains **no dimension json and no noise_settings** (verified sec.9) — there is no accessible Depths dimension in this version. Record as "skipped: no dimension in jar" in `LEDGER.md`.
**ritual_plinth:** already in the IR chapter (`ir_magic_feedstock_and_spectrum_network`); do NOT duplicate in Renaissance.

---

## 4. P2 [SPINE] — Neo Vitae: Renaissance -> IR chain wire (WIRE ONLY, no new nodes)

**State verified:**
- Renaissance line (`ren_magic_foundations`): `weak_blood_shard` -> `blood_orb_weak` -> `ara_vitae` -> `rune_blank` -> `blood_orb_apprentice` (`0B03101000000034`) -> `sigil_divination` (optional); plus `hellfire_forge` (optional `0B03101000000037`) and `athanor` (`0B03101000000039`, hide_until_deps_complete); plus an optional spiritus column (`raw_spiritus`->...->`blood_pearl`->`incense_altar`).
- IR segment (`ir_magic_feedstock_and_spectrum_network`): entry `49540B1000000004` = **Hellfire Forge (use_block)**, depending on `49540A100000000F` (IR digital-logistics capstone). From there the moved hellforged/spiritus tier-fix nodes (0B031020-* dust/ingot/parts, 0B031010-* spiritus gem petty/lesser/common) plus foundry, blood tank, sentient armor.

**The gap:** the IR Neo Vitae entry depends only on IR digital logistics, so the graph never shows the player that the Renaissance blood-orb/hellfire-forge work is the prerequisite reading. Blood orbs ARE Renaissance-obtainable, so this is a *teaching* link, not a mechanical softlock.

**Weighed:** (a) add a hard dependency from IR entry onto the Ren `athanor` node — rejected, that would make IR magic gated behind an *optional* Renaissance node and could stall a player who skipped the optional forge; (b) add a soft reveal-only dependency — chosen; (c) do nothing — rejected, the spec explicitly asks to confirm/plan the chain.

**Re-wire table (the ONLY change for P2 Neo Vitae):**

| existing node | file | current deps | ADD dep | flag | effect |
|---|---|---|---|---|---|
| `49540B1000000004` (IR Hellfire Forge entry) | `ir_magic_feedstock_and_spectrum_network.snbt` | `49540A100000000F` | ADD `0B03101000000034` (Ren `blood_orb_apprentice`, a REQUIRED Ren node) | keep as ADDITIONAL dep (AND) only if `min_required_dependencies` stays default; SAFER: set `min_required_dependencies: 1` so either path reveals it | Player who did the Renaissance orb line sees IR magic as its continuation; player who came only through digital logistics still unlocks it. No softlock. |

**Decision to confirm with CC at merge:** whether to use AND (both deps) or `min_required_dependencies:1` (either dep). Recommend **min_required_dependencies:1** to avoid gating IR magic behind the *apprentice orb* for a player who rushed digital logistics. This is a one-field structural edit; no new nodes, no prose.

**Chain verdict:** VALID. Blood orbs (`blood_orb_weak`/`apprentice`) are Renaissance-legal; the IR segment's hellforged/spiritus tree is IR-gated and self-consistent. The only missing piece is the teaching wire above.

---

## 5. P3 — apothic_enchanting: small controlled line in `ren_observation_experimentation` (ungated)

**Gate call resolved:** `AOA_QUEST_SCOPE_REGISTRY.md` Policy 1 (GATING CLOSED) + grep confirms **zero apothic_enchanting AStages locks**. Author ungated. The mod is thematically "controlled late-Renaissance enchanting study," which is exactly what `ren_observation_experimentation` (the Renaissance study/instruments chapter, order 7) is for. Host there rather than a new chapter (avoids chapter sprawl for a 6-node line).

**Weighed host:** new chapter (rejected — too small to earn a tab), `ren_magic_foundations` (rejected — full), `ren_archive_recordkeeping` (viable — it is the "library/records" chapter and apothic is bookshelf-heavy) vs `ren_observation_experimentation` (chosen — "study/experimentation" reads as enchanting research; confirm at author time which of the two has open layout space, prefer archive if it is the library-themed one and has room). **Author-time decision:** Fable picks archive vs observation by whichever has open non-crossing space; both are acceptable homes. Default: `ren_observation_experimentation`.

**Node table** (all IDs jar-verified sec.9; all ungated):

| # | proposed id | task | icon | flags | teaches |
|---|---|---|---|---|---|
| AE1 | (Fable-assign, chapter-prefixed) | item `apothic_enchanting:hellshelf` | hellshelf | entry (deps = chapter's local enchanting root or gateway) | first eterna bookshelf |
| AE2 | " | item `apothic_enchanting:infused_hellshelf` | infused_hellshelf | — | infusion upgrade |
| AE3 | " | item(smart_filter: `apothic_enchanting:seashelf` OR `deepshelf` OR `endshelf`) | endshelf | — | the three biome shelf families (one node) |
| AE4 | " | item `apothic_enchanting:library` | library | — | Enchantment Library storage |
| AE5 | " | item(smart_filter: any `*_tome`: weapon_tome/pickaxe_tome/etc.) | weapon_tome | optional: true | enchantment extraction tomes |
| AE6 | " | item `apothic_enchanting:ender_library` | ender_library | optional: true; shape diamond | Library of Alexandria capstone |

**Variant discipline:** AE3 (biome shelves) and AE5 (tomes) MUST be single smart_filter nodes, not per-variant. Do NOT quest `draconic_endshelf`/`pearl_endshelf` separately — fold under AE3's filter or drop (they are cosmetic tiers of the same mechanic). `draconic_endshelf` is ungated (grep confirmed) despite the name; still avoid featuring it (no separate node).
**No vanilla items, no bare enchant-material tasks.** Every node is a distinct apparatus/tome block-item.

---

## 6. P3 — mahoutsukai: NEW explicitly-optional chapter `ren_mahou_tsukai`

**Optional-chapter caveat:** AoA canon forbids *whole optional main-progression chapters on the spine*, but mahoutsukai is flavor-fun content that is **never a dependency of any capstone**. It is a legitimate standalone optional tab (like a side-content chapter), not an N-of-M main-progression chapter. Metadata: the chapter's quests carry `optional: true` and NOTHING in the age spine or any capstone aggregator depends on any mahoutsukai node.

**Weighed host:** fold into an existing Renaissance chapter (rejected — mahoutsukai is a self-contained spell-circle system with its own projector/scroll economy; folding it into e.g. magic_foundations would blow that chapter's crossing budget and mix an optional system into required lanes) vs new optional chapter (chosen — clean, clearly-optional tab).

**Chapter header:** `filename: "ren_mahou_tsukai"`, `group: "0B038EB15EBBFD95"` (the_renaissance), `order_index: 12`. `icon:` `mahoutsukai:mahoujin_projector`. Entry depends on `6D7E8F901A2B1054` (Renaissance gateway) for reveal. Every node `optional: true`.

**Node table** (all IDs jar-verified sec.9; ungated except the two pre-existing gated gear items which we AVOID):

| # | proposed id | task | icon | flags | teaches |
|---|---|---|---|---|---|
| MT1 | 0B03106000000001 | item `mahoutsukai:guidebook` | guidebook | entry; optional | the compendium (how to learn spells) |
| MT2 | 0B03106000000002 | item `mahoutsukai:attuner` | attuner | optional | attuning gems (attuned_diamond/emerald) |
| MT3 | 0B03106000000003 | item `mahoutsukai:mahoujin_projector` | mahoujin_projector | optional | the magic-circle projector (core mechanic) |
| MT4 | 0B03106000000004 | item `mahoutsukai:mystic_code` | mystic_code | optional | spell casting focus |
| MT5 | 0B03106000000005 | item(smart_filter: a small scroll set, e.g. `scroll_familiars_garden`, `scroll_gandr`, `scroll_fay_sight`) | scroll_familiars_garden | optional | familiar/utility spell scrolls (the "familiar" beat) |
| MT6 | 0B03106000000006 | item `mahoutsukai:mystic_staff` | mystic_staff | optional; shape diamond | capstone focus |

**AVOID:** `mahoutsukai:staff_emrys` (gated the_renaissance as high_tier_gear per `01p_gap_closure.js` L155 — legal at Ren but it is a reward-gear item, not a teaching target) and `mahoutsukai:morgan` (gated **otherworldly** per `01_item_restrictions.js` L354 — a cross-age inversion if placed here). Neither appears in the plan.
**Familiar verification note:** the mod's "familiar" mechanic is scroll-driven (`scroll_familiars_garden`); there is no standalone `familiar` item. MT5 teaches it via the scroll (jar-verified sec.9).

---

## 7. Dispatchable tasks (STRICTLY disjoint file sets)

Each task = one Fable dispatch. Prepend `01_MASTER_PREAMBLE`. Stub lang keys go to the named sidecar. File sets are disjoint so tasks can run in parallel EXCEPT where a re-wire touches a shared file (noted).

| Task | Scope | Files it MAY touch (exclusive) | Lang stub sidecar | New nodes |
|---|---|---|---|---|
| **T-02b-1** | P1 Spectrum new chapter | CREATE `config/ftbquests/quests/chapters/ren_spectrum_academy.snbt` | `phase0/stubs/T-02b-1_stubs.txt` | 12 (N1-N12) |
| **T-02b-2** | P1 Spectrum re-wire (IR reveal) | EDIT `config/ftbquests/quests/chapters/ir_magic_feedstock_and_spectrum_network.snbt` (add 1 dep to `49540B100000000C`) | none | 0 |
| **T-02b-3** | P2 IE repair | EDIT `config/ftbquests/quests/chapters/metallurgy.snbt` | `phase0/stubs/T-02b-3_stubs.txt` | 2-3 (M1,M2,+opt M3) |
| **T-02b-4** | P2 Malum + Neo Vitae wire | EDIT `config/ftbquests/quests/chapters/ren_magic_foundations.snbt` (add MA1-MA3) | `phase0/stubs/T-02b-4_stubs.txt` | 3 (MA1-MA3) |
| **T-02b-5** | P2 Neo Vitae IR-entry wire | EDIT `config/ftbquests/quests/chapters/ir_magic_feedstock_and_spectrum_network.snbt` (add dep + `min_required_dependencies:1` on `49540B1000000004`) | none | 0 |
| **T-02b-6** | P3 apothic_enchanting line | EDIT `config/ftbquests/quests/chapters/ren_observation_experimentation.snbt` (or `ren_archive_recordkeeping.snbt` if better layout) | `phase0/stubs/T-02b-6_stubs.txt` | 6 (AE1-AE6) |
| **T-02b-7** | P3 mahoutsukai optional chapter | CREATE `config/ftbquests/quests/chapters/ren_mahou_tsukai.snbt` | `phase0/stubs/T-02b-7_stubs.txt` | 6 (MT1-MT6) |

**Serialization note:** T-02b-2 and T-02b-5 BOTH edit `ir_magic_feedstock_and_spectrum_network.snbt` (two different quest nodes: `49540B100000000C` vs `49540B1000000004`). Run them **sequentially, T-02b-2 then T-02b-5**, or merge into one IR-edit task to avoid a write collision. Recommend **merging T-02b-2 + T-02b-5 into a single dispatch** ("T-02b-2/5: all IR-chapter re-wires"). All other tasks are fully parallel.

**Lang stub format (per preamble sec.5), example for N1:**
```
quest.0B03105000000001.title: "[STUB] title"
quest.0B03105000000001.quest_subtitle: "[STUB] subtitle"
quest.0B03105000000001.quest_desc: ["[BRIEF] teaches: Spectrum pigment_palette (Renaissance-gated, aoa_astages_01.js L730); it is the front-door tool that dyes ink for all Spectrum crafting; entry node of ren_spectrum_academy, deps = Renaissance gateway 6D7E8F901A2B1054; next node = color_picker. Opus: 2-4 para instruction-first, teach that Spectrum runs on colored pigment/ink and this is where color starts. No em dashes."]
```

---

## 8. Verification steps (run before LEDGER sign-off)

1. **Duplicate-id scan (pack-wide, anchored):** for every new id, `grep -rP '^\s+id: "<id>"' config/ftbquests/quests/chapters/` returns exactly ONE hit. Covers N*, M*, MA*, AE*, MT* ids.
2. **No duplicate item task pack-wide:** for each task item introduced (spectrum:pigment_palette, pedestal_*, malum:soulstone, apothic_enchanting:hellshelf, mahoutsukai:guidebook, etc.), `grep -rn '<item>' config/ftbquests/quests/chapters/` shows it is NOT already a task item elsewhere (dep-reference instead if it is). Spectrum pedestals/nodes/hue tools and mahoutsukai items were confirmed 0 in this pass; re-confirm at author time.
3. **Age-discipline (CC):** every task item's AStages gate is at-or-before its chapter age. Spectrum front-door items = the_renaissance (verified). Malum soulstone/spirits = ungated (Renaissance-legal). apothic/mahoutsukai = ungated. AVOID list (mahoutsukai:morgan @ OW, staff_emrys as reward-gear) confirmed absent from all node tables.
4. **Crossing check (Codex):** run the dependency-crossing computation on `ren_spectrum_academy`, `ren_mahou_tsukai`, and the edited `metallurgy`/`ren_magic_foundations`/`ren_observation_experimentation`. Zero crossings required.
5. **Reveal integrity:** each new chapter's entry node has >=1 dependency (`6D7E8F901A2B1054`) so the tab is not always-visible (per FTBQ rootless-always-visible rule).
6. **Cross-file dep resolves:** T-02b-2/5 target ids (`0B03105000000022`, `0B03101000000034`) exist after T-02b-1/T-02b-4 land. Run T-02b-1 and T-02b-4 BEFORE the IR re-wire task.
7. **`.snbt` byte discipline:** CRLF/tab preserved; SkillsLevel blocks not stripped; per-file line-ending detection via Python byte read (grep lies on mixed endings).
8. **min_required_dependencies:1 on `49540B1000000004`** verified to not orphan the node (it retains the IR digital-logistics dep as one of the two).
9. **before/after counts to LEDGER.md:** ren_magic_foundations 61->64; metallurgy +2/3; new ren_spectrum_academy = 12; new ren_mahou_tsukai = 6; ren_observation_experimentation +6; IR chapter +2 deps, +0 nodes. Record the "census-was-wrong" corrections (IE coke/tank present; Malum crucible/plinth are IR) as ledger notes so 02c does not re-raise them.

---

## 9. VERIFICATION LOG (jar + disk proofs, this pass)

All jars in `mods/`. Commands run 2026-07-02.

**Spectrum** (`spectrum-1.11.8-1.21.1-neo.jar`):
- `unzip -l ... | grep models/item/` confirmed: `pedestal_all_basic`, `pedestal_basic_amethyst`, `pedestal_basic_citrine`, `pedestal_basic_topaz`, `pedestal_moonstone`, `pedestal_onyx`, `color_picker`, `titration_barrel`, `pigment_palette`, `particle_spawner`, `ink_assortment`, `fusion_shrine_basalt`/`_calcite`, `spirit_instiller`, and the 5 network nodes `connection_node`/`gather_node`/`provider_node`/`sender_node`/`storage_node`.
- lang `assets/spectrum/lang/en_us.json` confirmed display names (Pigment Pedestal, Fusion Shrine, Spirit Instiller, Pastel Network *Node, Titration Barrel, Color Picker).
- **AStages:** `aoa_astages_01_item_restrictions.js` L730-736 gates pedestals + pigment_palette to `the_renaissance`; L485-489 gates the 5 nodes to `the_renaissance`; `aoa_astages_01m_magic.js` L64-72 gates titration_barrel/particle_spawner/color_picker/spirit_instiller/fusion_shrine_basalt to `the_renaissance`, and enchanter/cinderhearth/crystal_apothecary/crystallarieum to `industrial_revolution` (so those stay IR).
- **VERIFY-AT-AUTHOR:** N12's advancement id `spectrum:milestones/build_spirit_instiller` was NOT confirmed; fall back to item `spectrum:ink_assortment` if the advancement id does not exist in `data/spectrum/advancement/`.

**Malum** (`malum-1.21.1-1.8.2.jar`):
- item models confirmed 9 spirit types: `aerial_spirit`, `aqueous_spirit`, `arcane_spirit`, `earthen_spirit`, `eldritch_spirit`, `infernal_spirit`, `sacred_spirit`, `umbral_spirit`, `wicked_spirit`; plus `spirit_altar`, `spirit_crucible`, `spirit_catalyzer`, `ritual_plinth`, `spirit_jar`, `soulstone_ore`, `runewood_obelisk`, `brilliant_obelisk`, `totemic_staff`.
- lang confirmed soulstone forms: `raw_soulstone`, `crushed_soulstone`, `refined_soulstone` (item.malum.*), `soulstone_ore`, `deepslate_soulstone_ore`, `block_of_soulstone`. **MA1 should target `malum:refined_soulstone` (the usable refined stone) — the exact "soulstone" harvesting item; VERIFY whether the scythe/harvest item is `refined_soulstone` at author time.**
- **Depths of Malum dimension:** `unzip -l ... | grep -iE "dimension|noise_settings"` returned EMPTY. No dimension in jar. SKIP confirmed.
- **AStages:** `spirit_altar` = the_renaissance (`01_item_restrictions.js` L503); `spirit_crucible`/`spirit_catalyzer` = industrial_revolution (`01m_magic.js` L74-75); soulstone ores gated in `06_ore_restrictions.js`. Spirits themselves: no lock (ungated, Renaissance-legal).
- **VERIFY-AT-AUTHOR:** MA3 icon (`cracked_soul_container`/`hex`) not confirmed; pick a verified malum item model at author time.

**Neo Vitae** (`neovitae-1.21.1-1.0.25.jar`):
- lang confirmed orb tiers: `weak`(Novicius) / `apprentice`(Discipulus T1) / `magician`(Veneficus T2) / `master`(Magus T3) / `archmage`(Dominus T4) / `transcendent`(Divinus); apparatus `hellfire_forge`, `athanor`, `vas_maleficum`, `spira_infernalis`, `teleposer`. Magician/master/archmage = GILDED gap (02d), NOT in 02b scope.
- disk: Ren line reaches `blood_orb_apprentice` (`0B03101000000034`); IR entry `49540B1000000004` = hellfire_forge use_block dep on `49540A100000000F`.

**Apothic Enchanting** (`ApothicEnchanting-1.21.1-1.5.3.jar`):
- confirmed blocks/items: `hellshelf`, `infused_hellshelf`, `blazing_hellshelf`, `seashelf`, `deepshelf`, `endshelf`, `pearl_endshelf`, `draconic_endshelf`, `treasure_shelf`, `library` (Enchantment Library), `ender_library` (Library of Alexandria), tomes `weapon_tome`/`pickaxe_tome`/etc., `prismatic_web`.
- **AStages:** `grep apothic_enchanting kubejs/.../01*.js` returned NO item gates (only a loot-bypass restriction in `09`). Ungated -> author at Renaissance ungated (Policy 1).

**Mahoutsukai** (`mahoutsukai-1.21.1-v1.36.27.jar`; combat addon `mahou_tsukai_combat` has NO items — animations only):
- confirmed items: `guidebook` (Knowledge Compendium), `attuner`, `attuned_diamond`/`attuned_emerald`, `mahoujin_projector`, `mahoujin` (block), `mystic_code`(+`_first_sorcery`/`_1/2/3`), `mystic_staff`, scrolls incl. `scroll_familiars_garden`, `scroll_gandr`, `scroll_fay_sight`, `fog_projector`, `mana_circuit`, `proximity_projection_keys`.
- **AStages:** `mahoutsukai:staff_emrys` = the_renaissance (high_tier_gear, `01p_gap_closure.js` L155) — AVOID (reward-gear, not a teaching target); `mahoutsukai:morgan` = **otherworldly** (`01_item_restrictions.js` L354) — AVOID (cross-age inversion). Base circle/scroll items ungated -> author ungated at Renaissance.

**IE** (`ImmersiveEngineering-1.21.1-12.4.2-194.jar`):
- advancements confirmed: `immersiveengineering:main/mb_cokeoven`, `immersiveengineering:multiblocks/mb_tank`, `mb_crusher`, `mb_metalpress`, `mb_mixer`, `mb_squeezer`, `mb_refinery`, `mb_arcfurnace`, `mb_excavator`, `mb_silo`, `mb_fermenter`, `mb_improvedblastfurnace`, `mb_dieselgen`.
- disk (`metallurgy.snbt`): coke lane + tank leaf mapped (sec.2). **VERIFY-AT-AUTHOR:** M1 `immersiveengineering:fluid_pump` and M3 `immersiveengineering:blueprint` exact ids not yet confirmed against the jar item models; confirm before use or substitute a verified IE fluid/tool item.

**Renaissance gateway:** `6D7E8F901A2B1054` defined in `what_waits_in_the_grove.snbt` L1314; grants `the_renaissance` via command reward; `ren_magic_foundations` root deps on it. Correct reveal anchor for new Renaissance chapters.

---

## 10. Open items handed to LEDGER / 02c (not authored here)
- **02c handoff:** the IR IE multiblock chapter entry should depend on `metallurgy` M2 (`2902E58DB70F9451`, mb_crusher pointer) for foundation->fleet continuity.
- **Ledger correction notes:** (a) IE coke/tank onboarding was already present (census false-negative on advancement tasks); (b) Malum spirit_crucible/catalyzer/ritual_plinth are IR-placed, not a Renaissance gap; (c) Neo Vitae magician/master/archmage ladder is the Gilded (02d) gap, out of 02b scope.
- **Author-time VERIFY flags** (sec.9): Spectrum N12 advancement id; Malum MA1 exact soulstone id + MA3 icon; IE M1/M3 exact item ids. Each has a named fallback.
- **No `08` decision-queue items** — GATING CLOSED dissolved both prior [CANON] blockers.
