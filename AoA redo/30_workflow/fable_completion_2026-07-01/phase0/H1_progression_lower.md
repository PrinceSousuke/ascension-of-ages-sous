# H1 — Progression-philosophy critique: Dark Ages + Medieval + Renaissance

Audit only. No files edited outside phase0/. No git. Every claim carries a proof
(file:line or grep). Severity ladder: SOFTLOCK > BROKEN > CANON > HYGIENE.

Scope: `config/ftbquests/quests/chapters/*.snbt` for the three lower ages, cross-checked
against `kubejs/server_scripts/aoa_astages_*.js` and prose in
`config/ftbquests/quests/lang/en_us.snbt`.

---

## 0. Executive summary

The Renaissance spine is well-built and the age-grant fan-in invariant is **satisfied**
for Renaissance (9 domain nodes + the Maledictus kill all fan into the IR-grant node). The
biggest structural problem is exactly the one the user flagged: **`ren_deeper_darker_otherside`
is gated at the very front of the age (only on the Renaissance-open gate) yet is the sole
structural predecessor of the age-capstone boss.** It also carries deep-gear content
(Warden carapace, netherite-tier smithing template, resonarium armor line) whose payoff is
locked to Industrial Revolution / Gilded — a real cross-age content inversion. This chapter
should be split: keep the crossing + sculk-gathering in late-Renaissance, move the
Warden/resonarium/netherite-upgrade gear tail into early IR.

Dark Ages and Medieval use a simpler *single-quest* age grant (no domain-proof fan-in),
which is defensible for those ages but is worth a canon call because it diverges from the
Renaissance-and-up invariant. Two non-boss kill tasks (alchemists_garden gnome/yeti) are a
canon violation.

Counts: **SOFTLOCK 0 · BROKEN 1 · CANON 6 · HYGIENE 4.**

---

## 1. Renaissance dependency spine (verified)

Reconstructed from first-quest `dependencies:` of each chapter and the age-grant node's
`dependencies:` list.

| Chapter | order_index | Entry gate (first quest dep) | Resolves to |
|---|---|---|---|
| ren_magic_foundations | 0 | `6D7E8F901A2B1054` | Renaissance-open gate (grants `the_renaissance` in what_waits_in_the_grove.snbt:1328) |
| ren_nether_threshold | 1 | `0B0310100000003D` | mid-node inside magic_foundations (chapters/ren_magic_foundations.snbt:1435) |
| ren_aether_literacy | 2 | `0B03101000000039` + `0B03102000000062` | magic_foundations cap + nether cap |
| ren_archive_recordkeeping | 6 | `0B03101000000039` | magic_foundations cap |
| ren_starlight_observation | 3 | `0B03107000000050` | archive cap |
| ren_undergarden_descent | 4 | `0B03107000000050` | archive cap |
| ren_observation_experimentation | 7 | `0B03107000000050` | archive cap |
| ren_end_threshold | 8 | `0B03104000000050` | starlight cap |
| **ren_deeper_darker_otherside** | 5 | `6D7E8F901A2B1054` | **Renaissance-open gate directly — no prerequisite chapter** |
| ren_second_mill_steam_rail_logistics | 10 | `6D7E8F901A2B1054` + check_quest on nether cap | Ren-open gate; also needs nether done (chapters/ren_second_mill_steam_rail_logistics.snbt:32) |
| ren_maledictus_vigil (capstone) | 9 | `0B03106000000050` | **deeper_darker capstone** (chapters/ren_maledictus_vigil.snbt:15) |

Proof of entry gates: `grep -n 'dependencies' <file>` line 15 of each chapter (see task log).
Proof deeper_darker floats free: `chapters/ren_deeper_darker_otherside.snbt:15` →
`dependencies: ["6D7E8F901A2B1054"]`.

So the intended difficulty ramp is:
`magic_foundations → nether → aether → archive → (starlight/undergarden/observation) → end`,
with deeper_darker and second_mill hanging off the age root as free-floating branches, and
Maledictus as the boss capstone.

---

## 2. LENS 1 — Difficulty ordering + the deeper_darker split (user directive)

### 2a. The structural contradiction (BROKEN)

**Finding H1-01 (BROKEN):** `ren_deeper_darker_otherside` is simultaneously the *earliest-
available* Renaissance chapter (its first quest gates only on the age-open node
`6D7E8F901A2B1054`) **and** the *only* structural gate into the age capstone. The Maledictus
capstone's first node depends on the deeper_darker return node:
`chapters/ren_maledictus_vigil.snbt:15` → `dependencies: ["0B03106000000050"]`, and
`0B03106000000050` is the deeper_darker "Back to the Light" node
(`chapters/ren_deeper_darker_otherside.snbt:354`).

Consequence: the game hands the player the Warden dimension on day one of the Renaissance
(no gear ramp behind it) yet treats clearing it as the immediate pre-req for the boss. This
is backwards from the intended difficulty curve. The Warden crossing is arguably the single
hardest survival check in the whole age, and it currently sits *ahead of* the Nether, End,
Aether, and Undergarden in reachability.

The pack's own AStages tiering confirms the Warden content is out-of-tier for early Ren:
- `deeperdarker:resonarium_*` armor → **industrial_revolution**
  (`aoa_astages_01_item_restrictions.js:886-889`)
- `deeperdarker:warden_*` armor → **gilded_age**
  (`aoa_astages_01_item_restrictions.js:890-893`)
- `deeperdarker:warden_upgrade_smithing_template` "applies to **Netherite** Equipment"
  (jar `assets/deeperdarker/lang/en_us.json`), and netherite is thematically an IR milestone
  (the IR chapter is literally `ir_netherite_citadel_obsidilith`).

### 2b. What `ren_deeper_darker_otherside_complete` gates today

**Finding H1-02 (CANON):** The stage `ren_deeper_darker_otherside_complete` is **granted but
never consumed**. Only reference anywhere:
`grep -rn ren_deeper_darker_otherside_complete` → the single grant at
`chapters/ren_deeper_darker_otherside.snbt:358`. Nothing depends on it; the Maledictus
capstone fans in the *quest node* `0B03106000000050`, not the stage. So re-scoping the stage
is cheap: nothing downstream breaks if you split it into `..._complete` (late-Ren crossing)
and a new IR proof.

### 2c. Concrete split proposal

Node inventory of `ren_deeper_darker_otherside.snbt` (all `deeperdarker:` items verified in
jar `deeperdarker-neoforge-1.21.1-1.4.1.jar`):

**STAYS in late-Renaissance** (the crossing + basic in-dimension gathering; all native,
all age-legal):
- `0B03106000000001` enter Otherside (dimension) — gated Renaissance
  (`aoa_astages_03_dimension_restrictions.js:7`)
- `...000010` Ancient City structure, `...000011` Deep Dark biome, `...000012`
  heart_of_the_deep, `...000013` Into the Otherside, `...000020` gleam_gel, `...000021`
  bloom_berries, `...000030` soul_dust, `...000032` sculk_bone, `...000033`
  reinforced_echo_shard, `...000034` resonarium (material), `...000041/42/44` sherds/grime/
  soul_crystal, the gloomsherd/food/grime side rails (`...000080-008A`), `...000050` "Back
  to the Light" return node **(keep this as the late-Ren proof node)**.

**MOVES to early Industrial Revolution** (gear whose stage-lock or upgrade base is IR+):
- `0B0310600000008D` `resonarium_upgrade_smithing_template` — feeds resonarium armor (IR-locked)
- `0B0310600000008E` `warden_carapace` — a **Warden drop**; requires killing the Warden
- `0B0310600000008F` `warden_upgrade_smithing_template` — applies to **netherite** gear (IR+)
- `0B03106000000045` / `0B03106000000091` `sonorous_staff` and `0B03106000000044→0B03106000000090`
  `soul_crystal → lite` light line can stay (Ren-legal), but the staff pairs naturally with
  the resonarium gear tail — recommend moving the staff too for coherence.

**Dependency changes required:**
1. Re-anchor the moved gear nodes to a new **IR chapter** (suggest a small branch in
   `ir_ir_side_gear_hidden_equipment` — it already hosts hidden equipment) with their entry
   gated on `ren_deeper_darker_otherside_complete` **and** an early-IR proof so the player has
   netherite/resonarium access before being asked to upgrade it.
2. Keep the Maledictus capstone dep on `0B03106000000050` (the crossing proof) unchanged —
   the boss should require *reaching* the Otherside, not *mastering* its gear.
3. Split the stage: keep `ren_deeper_darker_otherside_complete` on `0B03106000000050`
   (crossing), add a new `ir_deep_gear_complete`-style stage on the moved IR tail if you want
   it to fan into the IR capstone. Register any new stage in
   `aoa_astages_00_register_stages.js`.

**Warden-vs-Dragon note (directive):** the chapter today has **no Warden kill task** (grep
`warden`/`Warden` in the chapter returns only `warden_carapace` and `warden_upgrade` item
tasks). The prose is explicitly a *stealth* crossing:
"Quiet and caution matter more than firepower" (lang en_us.snbt:951). That is the right call
for late-Ren — do not add a Warden kill to Renaissance. If you want the "Warden harder than
the Dragon" beat honored, the **carapace** node (which does require a Warden kill to obtain
the drop) is the correct thing to push into IR, where the player has netherite armor to
survive the fight. The End/Dragon content lives in `ren_end_threshold` (gated behind
starlight, `order_index` 8) and is already sequenced *earlier in the tree depth* than a
post-move Warden gear fight, which matches the directive.

---

## 3. LENS 2 — Intra-age gating sanity

**Finding H1-03 (CANON):** The tab `order_index` disagrees with the true dependency depth for
two chapters. deeper_darker is tab-slot 5 but dependency-depth 1 (front of age);
second_mill is tab-slot 10 but also dependency-depth ~2 (needs only Ren-open + nether). This
is cosmetic but misleads a player reading the book top-to-bottom. Recommend: after the split,
set deeper_darker's crossing to sit visually after the dimension chapters, or leave the tab
order but accept the note.

Ordering that IS sensible and verified:
- Nether before End: nether is depth-1 off magic_foundations; End gates behind starlight
  which gates behind archive. Good.
- Aether gated behind nether (`0B03102000000062`) — Aether needs a Nether-tier fight readiness.
  Reasonable.
- Undergarden/starlight/observation all fan off archive — a sensible "pick your exploration"
  hub. Good.

**Finding H1-04 (CANON):** `ren_second_mill_steam_rail_logistics` grants **no stage** (grep
`astages add` in file → none) and is **not fanned into** the Maledictus capstone (grep
`0B031B1` in ren_maledictus_vigil.snbt → 0). It is a fully optional side chapter. That is a
legitimate design choice (Create steam/rail is optional depth), but it means the age's
"Second Mill" showpiece is skippable and invisible to the capstone. If Create steam is meant
to be a required Renaissance beat, it needs a proof stage and a fan-in edge; if it is
intentionally optional, that is fine — just confirm the intent.

No chapter assumes gear the age cannot make, with the one exception in H1-01 (deeper_darker's
IR/Gilded gear tail).

---

## 4. LENS 3 — Pacing holes

**Finding H1-05 (HYGIENE):** Between the Renaissance-open gate and the first magic_foundations
objective there is a clean handoff, but deeper_darker and second_mill both dangle off the
age root with no narrative "you are ready for this now" gate. A player who wanders into the
deep dark on day one has zero guidance that it is meant to be a late beat. Adding a
dependency from deeper_darker's crossing onto (say) the Nether or Aether capstone would both
fix H1-01 reachability and remove this pacing hole. Recommend gating deeper_darker's entry on
the End or Aether capstone so it reads as a late-Renaissance destination.

Otherwise pacing is dense and guided: every dimension chapter has an item ramp (gather →
refine → gear) rather than dead air.

---

## 5. LENS 4 — FOMO coverage

Verified themes by task-item namespace per chapter (`grep -oE 'id: "[a-z_]+:'`):

- **Magic literacy** (magic_foundations): neovitae + theurgy + malum + occultism — the Neo
  Vitae spine is present and prominent. Good.
- **Create Second Mill** (second_mill): `create:steam_engine`, `create:blaze_burner` present —
  the steam/rail showpiece IS shown, though optional (see H1-04).
- **Archaeology / storage** (archive): betterarcheology + sophisticatedstorage + jewelry —
  covered.
- **Dimensions**: Nether (betternether-family), End (betterend/unusualend/endrem/
  endermanoverhaul), Aether, Undergarden, Starlight (eternal_starlight), Otherside — all six
  Renaissance dimensions have dedicated chapters. Strong coverage.

**Gaps worth a look (HYGIENE):**
- **Cold Sweat**: the only temperature-gear surfacing in the lower ages is at the Maledictus
  chapter (`cold_sweat:goat_fur_leggings` at ren_maledictus_vigil.snbt:208). Cold Sweat is a
  survival-pressure mechanic that should be taught in **Dark Ages** (the survival-minimalism
  age), not first shown at the Renaissance boss gate. Recommend a Cold Sweat insulation beat
  in `stone_water_weather_and_wounds`.
- **Overgeared**: the forging substrate is taught (drafting_table gates the medieval grant,
  entering_the_iron_era.snbt:360) — covered.
- **Cataclysm early structures**: Maledictus (cursed_pyramid) is the Ren boss; the Medieval
  `what_waits_in_the_grove` uses mowziesmobs/born_in_chaos bosses. Cataclysm's early
  overworld structures are otherwise only surfaced at the boss. Acceptable.

---

## 6. LENS 5 — Capstone spine verification (the invariant)

### Renaissance — PASS

Age-grant node: `ren_maledictus_vigil.snbt` node **`0B0310A0000000F0`**, task
`cataclysm:cursium_ingot`, grants `industrial_revolution` + `ren_seal_obtained` + advancements
via FTBQ command rewards (`chapters/ren_maledictus_vigil.snbt:778,802`). It fans in 10 deps
(lines 748-758), each verified to be that chapter's domain grant node:

| Dep id | Chapter | Grants |
|---|---|---|
| 0B03101000000039 | ren_magic_foundations | ren_magic_foundations_complete (line 1290) |
| 0B03102000000062 | ren_nether_threshold | ren_nether_threshold_complete (line 520) |
| 0B03103000000031 | ren_aether_literacy | ren_aether_literacy_complete (line 255) |
| 0B03104000000050 | ren_starlight_observation | ren_starlight_observation_complete (line 1212) |
| 0B03105000000050 | ren_undergarden_descent | ren_undergarden_descent_complete (line 505) |
| 0B03106000000050 | ren_deeper_darker_otherside | ren_deeper_darker_otherside_complete (line 358) |
| 0B03107000000050 | ren_archive_recordkeeping | ren_archive_recordkeeping_complete (line 1150) |
| 0B031080000000F2 | ren_observation_experimentation | ren_observation_experimentation_complete (line 1069) |
| 0B03109000000060 | ren_end_threshold | ren_end_threshold_complete (line 617) |
| 0B0310A000000014 | (this chapter) | Maledictus kill (ren_maledictus_defeated) |

All 9 domain chapters + the boss kill are fanned in. **Invariant satisfied.**

**Finding H1-06 (CANON):** The *only* domain chapter NOT fanned in is
`ren_second_mill_steam_rail_logistics` (has no proof stage — see H1-04). If Create steam is a
required domain, this is a missing fan-in edge; if optional, this is correct. Needs a canon
call.

### Medieval → Renaissance — PASS (partial fan-in by design)

Grant node `6D7E8F901A2B1054` in `what_waits_in_the_grove.snbt:1314`, grants `the_renaissance`
(line 1328) via command reward. It fans in 3-of-4 Medieval boss trials
(`min_required_dependencies: 3`, deps `...1050-...1053`: Ferrous Wroughtnaut / Foliaath /
Frostmaw / Grottol). This is a boss-gauntlet grant, not a domain-proof fan-in, but it is a
real convergence node. Acceptable for Medieval.

### Dark Ages → Medieval — CANON (invariant divergence)

**Finding H1-07 (CANON):** `medieval_times` is granted by node `097AED7C91033D5E` in
`entering_the_iron_era.snbt:374`, which fans in a **single** dependency `6A1E8D4C0F2B7B03`
(the Overgeared drafting_table quest). It does **not** fan in the three Dark Ages domain
chapters (stone_food_and_farming_pressures, stone_water_weather_and_wounds are not required).
This diverges from the Renaissance-and-up fan-in invariant. It is defensible (Dark Ages is
survival-minimalism with no proof stages), but if the invariant is meant to hold uniformly,
Dark Ages needs its two survival chapters fanned into the medieval grant. Canon call.

---

## 7. Other findings

**Finding H1-08 (CANON):** Non-boss kill tasks. `alchemists_garden:gnome` and
`alchemists_garden:yeti` are non-optional `type: "kill"` tasks in both
`stone_water_weather_and_wounds.snbt` (Dark) and `m3_relics_and_burrows.snbt`
(m3:1012, m3:1213). The canon rule: kill tasks are legal ONLY for bosses. alchemists_garden is
a farming/regrowth mod (`alchemists_garden_regrowth-v9.2.jar`); gnome/yeti are very likely
ambient mobs, not bosses. If they are ambient, convert to a drop-item task or drop the quest.
NEEDS boss-status confirmation against the jar before acting.

**Finding H1-09 (HYGIENE):** `minecraft:lectern` appears as a node/chapter **icon** only in
`ren_archive_recordkeeping.snbt` (lines 8, 19, 1157) — not as a task item, so it does not
violate the no-vanilla-task rule. Noted so a future scan does not false-positive it.

**Finding H1-10 (HYGIENE):** `deeperdarker:lite` (node `0B03106000000090`) is a real item
("Lite", jar-verified) but is a thin, obscure task item. Fine to keep as optional; flagged
for prose clarity only.

**Finding H1-11 (HYGIENE):** MI bronze_plate/bronze_gear and generatorgalore basic generators
appear as task items in `ren_observation_experimentation` and are **NOT** stage-locked (grep
in `aoa_astages_01_item_restrictions.js` → no rows), so they are craftable from world entry
and legal in Renaissance. Not a violation. Noted because MI base is IR-tier per the census —
these specific low-tier items are ungated, so the placement is fine, but confirm this is
intended rather than a missing lock.

---

## 8. Recommendation priority (concrete)

1. **Split deeper_darker (H1-01):** keep crossing + native gathering + `..._complete` proof in
   late-Ren; move `warden_carapace` (0B0310600000008E), `warden_upgrade_smithing_template`
   (0B0310600000008F), `resonarium_upgrade_smithing_template` (0B0310600000008D), and the
   sonorous_staff nodes into an early-IR branch (suggest `ir_ir_side_gear_hidden_equipment`).
2. **Re-gate deeper_darker entry (H1-05):** change its first-quest dep from the raw Ren-open
   gate to the End or Aether capstone so it reads as a *late* Renaissance destination and the
   Maledictus pre-req stops being reachable on day one.
3. **Resolve second_mill's status (H1-04/H1-06):** either give it a proof stage + fan-in edge
   (if Create steam is required) or confirm it is intentionally optional.
4. **Confirm gnome/yeti boss status (H1-08):** if ambient, convert the two kill tasks to
   drop-item tasks.
5. **Canon call on the Dark-Ages fan-in (H1-07)** and add a Cold Sweat insulation beat to
   Dark Ages (H1-05 FOMO) so temperature gear is taught before the Renaissance boss.
