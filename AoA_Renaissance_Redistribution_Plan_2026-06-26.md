# Renaissance Redistribution + Apotheosis Tier Re-Pace — Implementation Spec
Date: 2026-06-26 · Status: decisions LOCKED, edits NOT yet applied · Source: live config verified by two opus agents (the `AoA redo/` anchor docs are absent from this mount; everything below is from live `.snbt`/`kubejs`).

## Locked decisions
1. **Warden kill** moves from Renaissance → **Industrial Revolution** (under Summit tier).
2. **Deeper-and-Darker / Otherside** chapter moves from Renaissance → **Gilded** (under Pinnacle tier).
3. **Renaissance capstone stays all-AND** — no relief valve. Relocated chapters simply leave the dependency list; every remaining realm stays required.
4. **Apotheosis tiers — grant at age ENTRY, not age EXIT.** No cross-age moves and no tier doubling. Ascent/Summit/Pinnacle are currently granted at their age's *capstone* (the exit), which is why they "feel late" — you only get the tier as you leave the age. Re-point each to its age's *entry/early* quest so you play the whole age with its tier. Haven and Frontier already grant at entry; leave them.

### Resulting tier schedule
| Tier | Age | Change |
|---|---|---|
| Haven | Medieval | **unchanged** — already at the Dark→Medieval onboarding (`entering_the_iron_era.snbt`) |
| Frontier | Renaissance | **unchanged** — already early/mid via `ren_magic_foundations.snbt` |
| Ascent | IR | **move grant** off the IR capstone (`ir_netherite_citadel_obsidilith.snbt:520`, exit) → an early-IR entry quest |
| Summit | Gilded | **move grant** off the Gilded capstone (`g_power_beyond_wires.snbt:2003`, exit) → an early-Gilded entry quest |
| Pinnacle | Atomic | **move grant** off the Atomic capstone (`at7_chaos_convergence.snbt:1010`, exit) → an early-Atomic entry quest |

Net effect: Ascent is live for the whole of IR (powers the relocated Warden), Summit for the whole of Gilded (powers the relocated Otherside), Pinnacle for the whole of Atomic. Atomic/OW/Ascension still cap at Pinnacle (only 5 tiers exist). The KubeJS impossible-trigger overrides at `kubejs/data/apotheosis/advancement/progression/*.json` stay untouched — tiers remain command-grant-only.

---

## Edit sites — CONTENT MOVES

### A. Deeper-and-Darker / Otherside → Gilded
Chapter: `config/ftbquests/quests/chapters/ren_deeper_darker_otherside.snbt` (chapter id `0B03001000000006`).
- Re-group the chapter from the Renaissance group `0B038EB15EBBFD95` to the **Gilded chapter group** (implementer: find the group id shared by `g_*`/`g1_*` chapters; verify, don't guess).
- Re-gate: change any stage lock on the chapter from `the_renaissance` → `gilded_age`. Check chapter-level visibility/dependency AND any in-chapter stage-lock task.
- Rename file to the Gilded prefix convention (verify the live scheme — likely `g_deeper_darker_otherside.snbt`).
- **Remove DD completion node `0B03106000000050` as a dependency from all four Renaissance sites:** `ren_maledictus_vigil` capstone (`0B0310A0000000F0`), Vigil chapter root (`0B0310A000000010`, ~line 15), `ren_end_threshold.snbt` (~line 157), `ren_magic_foundations.snbt` (~line 2133).
- **Add** DD completion as a required dependency of the **Gilded capstone** (`g_power_beyond_wires.snbt`, Void Titan) so it gates leaving Gilded.
- **Journey mirror:** `journey_to_ascension.snbt` node `5350010000020007` currently sits in the Renaissance mirror segment — re-point/move it to the Gilded mirror segment.

### B. Warden kill → Industrial Revolution
Source: `ren_undergarden_descent.snbt`, quest `0B03105000000011` "The Warden" (`type:kill minecraft:warden`).
- **Sever** the Warden quest from Undergarden's required spine so the Undergarden completion node `0B03105000000050` (a Renaissance-capstone dependency) no longer transitively requires it. The Undergarden dimension itself stays a Renaissance realm — just without the Warden gate.
- Re-home the Warden kill into an **IR** chapter (suggested host: the IR citadel/combat chapter) as a required dependency of the IR capstone (`ir_netherite_citadel_obsidilith.snbt`), or as its own short IR quest feeding that capstone.
- Verify Undergarden completion is still reachable (no orphaned/dangling required node).

---

## Edit sites — TIER GRANTS (move the `/advancement grant ... apotheosis:progression/<tier>` reward from each age's capstone/exit to that same age's entry/early quest)
| Tier | Remove from (capstone / exit) | Add to (entry / early in the SAME age) |
|---|---|---|
| Ascent | `ir_netherite_citadel_obsidilith.snbt:520` | an early-IR entry quest |
| Summit | `g_power_beyond_wires.snbt:2003` | an early-Gilded entry quest |
| Pinnacle | `at7_chaos_convergence.snbt:1010` | an early-Atomic entry quest |
Haven (`entering_the_iron_era.snbt:386`, Medieval onboarding) and Frontier (`ren_magic_foundations.snbt:2147`, early Renaissance) are already entry grants — leave them. No tier changes age; nothing doubles up. Line numbers are anchors only — re-grep before editing; they drift.

---

## Prerequisite (do NOT skip): Aether gravitite softlock
Because Renaissance stays **all-AND**, the existing softlock in `ren_aether_literacy` (requires `aether:gravitite_pickaxe`, which is Gilded-ore-locked) becomes a hard wall — Renaissance is uncompletable until fixed. Resolve in the same pass: drop the gravitite-pickaxe task (the Eye-of-the-Storm kill proof already exists). Ref: memory `project_aoa_aether_renaissance_softlock_2026_06_03`.

---

## Dependency-integrity rules (mandatory)
- After the moves, run a full cross-age graph pass: **no quest may depend on a node now living in a later age** (no new softlock). Recurse until clean.
- Re-grep `deeperdarker:*` and `minecraft:warden` across all **Renaissance** chapters after the move — confirm nothing Renaissance-required still asks for them. (DD item tasks that legitimately live in IR/Gilded/Atomic chapters are fine and stay.)
- Coords/format: CRLF-preserving, minimal edits, no reflow of untouched lines.

## Verification checklist (no PASS_WITH_TODOS)
- [ ] FTBQ/`node --check` parse passes on every edited `.snbt` — verify via Desktop Commander, **not** the truncating Cowork mount.
- [ ] `grep -c` the DD node `0B03106000000050` across all chapters → appears only at intended sites.
- [ ] No `.bak` files left behind.
- [ ] Duplicate-item / duplicate-quest scan clean.
- [ ] Dry-run unified diff produced and reviewed BEFORE final write.
- [ ] Aether gravitite softlock resolved.

---

## Delegation prompt (paste into Claude Code — recommended for this; it's integrity-critical multi-file graph surgery, cc's strength. The tier-grant string moves are mechanical and bundle into the same pass.)

```
ROLE: Senior modpack dev. NeoForge 1.21.1 pack "Ascension of Ages", FTBQuests .snbt at config/ftbquests/quests/chapters/.
TASK: Apply the redistribution in AoA_Renaissance_Redistribution_Plan_2026-06-26.md exactly. Do NOT improvise scope.

HARD RULES:
- Verify EVERYTHING with grep/ripgrep + Desktop Commander reads. The Cowork mount lies about truncation — never trust a truncation/parse-fail report from it; re-read real bytes.
- Re-grep all anchor line numbers before editing (they drift). CRLF-preserving, minimal-diff edits only.
- Produce a DRY-RUN unified diff of every change and STOP for my approval before writing anything.
- No .bak files. No PASS_WITH_TODOS. If a move would orphan a node or create a cross-age softlock, STOP and report — do not paper over it.

DO, in order:
1. Move the Deeper-and-Darker chapter (id 0B03001000000006) from the Renaissance group to the Gilded group; re-gate the_renaissance -> gilded_age; rename to the Gilded prefix. Remove DD completion node 0B03106000000050 from the 4 Renaissance dependency sites listed in the spec; add it as a required dep of the Gilded Void Titan capstone; re-point journey_to_ascension node 5350010000020007 to the Gilded mirror.
2. Sever Warden kill quest 0B03105000000011 from ren_undergarden_descent's required spine (Undergarden stays Renaissance, minus Warden); re-home the Warden kill into the IR citadel chapter as a required dep of the IR Obsidilith capstone. Confirm Undergarden completion node 0B03105000000050 stays reachable.
3. Move 3 Apotheosis tier-grant commands from their age's CAPSTONE (exit) to that age's ENTRY/early quest, same age, no cross-age move: Ascent off the IR Obsidilith capstone -> an early-IR quest; Summit off the Gilded power_beyond_wires capstone -> an early-Gilded quest; Pinnacle off the Atomic chaos_convergence capstone -> an early-Atomic quest. Leave Haven (Medieval onboarding) and Frontier (ren_magic_foundations) where they are. Leave the kubejs impossible-trigger overrides untouched.
4. Fix the Aether gravitite-pickaxe softlock in ren_aether_literacy (drop that task; EotS kill proof already exists).
5. Run the full verification checklist; output the grep counts + parse results as proof.

REPORT: the dry-run diff, then (after approval) the verification proof. Flag any canon ambiguity for me rather than deciding it.
```

### Model note
Claude Code for the whole pass (dependency-graph integrity + grep-verify loop is its strength). Codex would be fine for the isolated tier-grant string relocations, but splitting the work risks inconsistent graph state mid-edit — keep it one cc pass.
