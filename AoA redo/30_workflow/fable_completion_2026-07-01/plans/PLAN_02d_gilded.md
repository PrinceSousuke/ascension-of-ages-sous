# PLAN 02d — Gilded Age completion (DESIGN, implementation-ready)

**Role:** structural designer. **This doc only.** No config/kubejs/lang edits, no git.
**Prepend for the implementer:** `01_MASTER_PREAMBLE.md`. **Authority order:** `AOA_QUEST_SCOPE_REGISTRY.md`
> this plan > the 02d prompt (the 02d prompt was written from the pre-buildout census and is
stale on P2/P3 — see the drift table below).

**Headline finding:** the 02d backlog is almost entirely already-done census drift. Of the four
02d work items, **only P1 (the Neo Vitae orb ladder) is real Gilded authoring.** Everything in
P2/P3 is either already quested at the correct age, or belongs to a different age owned by
another prompt, or is excluded. The flight slot is dead. This plan authors **one new node
cluster** (3 nodes + 1 optional) into `g7_chartered_arcana` and reassigns/close-outs the rest.

---

## 0. Verification log (every id proven on disk)

### Neo Vitae orbs (P1)
Jar: `mods/neovitae-1.21.1-1.0.25.jar`.
Item ids (proof: `unzip -p … assets/neovitae/lang/en_us.json | grep item.neovitae`):
```
item.neovitae.blood_orb_weak        = Novicius   (T0 entry)
item.neovitae.blood_orb_apprentice  = Discipulus (T1)   ← Renaissance, quested ren_magic_foundations 0B03101000000034
item.neovitae.blood_orb_magician    = Veneficus  (T2)   ← GILDED, 0 quests  ← author
item.neovitae.blood_orb_master      = Magus      (T3)   ← GILDED, 0 quests  ← author
item.neovitae.blood_orb_archmage    = Dominus    (T4)   ← GILDED, 0 quests  ← author
item.neovitae.blood_orb_transcendent= Divinus    (apex) ← Atomic, quested at7 + ow6
```
Orb recipe data (proof: `unzip -p … data/neovitae/recipe/ara_vitae/<orb>.json`) — these are the
crafting facts Opus must teach:

| Orb | recipe file | Ara Vitae `minTier` | input | bloodNeeded |
|---|---|---|---|---|
| magician | `ara_vitae/magician_blood_orb.json` | **2** | `#c:storage_blocks/gold` (gold block) | 25000 |
| master | `ara_vitae/master_blood_orb.json` | **3** | `neovitae:weak_blood_shard` | 40000 |
| archmage | `ara_vitae/archmage_blood_orb.json` | **4** | `neovitae:hellforged_block` | 80000 |

All three inputs are legal at/before Gilded:
- gold block — vanilla, always legal.
- `neovitae:weak_blood_shard` — locked `the_renaissance` (`aoa_astages_01m_magic.js:120`).
- `neovitae:hellforged_block` — locked `industrial_revolution` (`aoa_astages_01m_magic.js:149`).

AStages gate on the orbs (proof: `aoa_astages_01m_magic.js:141-143`):
```
["gilded_age", "neovitae:blood_orb_magician", "item"]
["gilded_age", "neovitae:blood_orb_master",   "item"]
["gilded_age", "neovitae:blood_orb_archmage", "item"]
```
→ all three are exactly Gilded-legal. No new gate, no inversion.

**Altar-buildability softlock check — CLEARED.** T2/T3/T4 altars need pillars + capstones.
The mod ships `data/neovitae/tags/block/altar/pillars.json` **empty** (`{"values":[]}`) — the known
hard-softlock risk. BUT the live datapack overrides it:
`kubejs/data/neovitae/tags/block/altar/pillars.json` =
`[bloodstone_brick, forbidden_arcanus:arcane_polished_darkstone_pillar, malum:tainted_rock_column, spectrum:onyx_pillar]`
and `t3_capstones.json` = `[blood_stained_glass, malum:block_of_soulstone]`. So a player can
build the T2→T4 Ara Vitae at Gilded. The orb ladder is physically completable. (Implementer:
do NOT re-verify by editing tags — read-only confirm the two live json files still hold.)

### Sentient gear + greater/grand gems (P1 sub-question)
- Gilded-locked (proof `aoa_astages_01m_magic.js`): `sentient_sword`/`sentient_pickaxe`/`sentient_axe`
  (163-165), `spiritus_gem_greater` (151), `spiritus_gem_grand` (152).
- Sentient ARMOR (`sentient_helmet/plate/leggings/boots`) down-tiered **IR** on 2026-07-02
  (158-161) and is quested in the IR magic-feedstock chapter — out of Gilded scope entirely.
- The Gilded-locked sentient TOOLS + greater/grand gems are **already quested** as optional
  depth in `ow6_beyond_the_veil.snbt`:
  - `neovitae:sentient_sword` task node `4256011000EE0001` (line 546)
  - `sentient_pickaxe`/`sentient_axe` smart_filter node `4256011000EE0003` (line 622)
  - `spiritus_gem_greater` + smart_filter over lesser/common/greater/grand node `4256011000EE0005` (line 698)
  These are an intentional OW6 optional side-branch (Living Harvest hidden-gear pattern), a linear
  chain rooted at `4256010000010001`.

### P2 machine mods (all proven already-done — see drift table)
- IF ids (proof `unzip -p mods/industrialforegoing-1.21-3.6.38.jar … lang`): all 10 targets exist
  AND are already TASK items in `g2_the_refinery.snbt` (one `item: { count: 1, id: … }` line each):
  `sludge_refiner, sewer, sewage_composter, washing_factory, water_condensator, potion_brewer,
  stasis_chamber, spores_recreator, conveyor, infinity_charger`.
- extrastorage (proof `mods/ExtraStorage-1.21.1-5.0.10.jar` lang): `netherite_crafter`,
  `advanced_importer` exist; both gated **atomic** (`aoa_astages_01j_storage.js:43-44`) and already
  quested in `at4_machine_soul.snbt` (2096, 2115).
- appmek (proof `mods/Applied-Mekanistics-1.6.3.jar` lang): cells `1k/4k/16k/64k/256k` +
  `chemical_cell_housing` exist; gated **atomic** (`aoa_astages_01p_gap_closure.js:253-257`,
  `01_item_restrictions.js:636`) and already quested in `at3_chain_reaction.snbt`.

### P3 enderio (proven)
- `enderio:fluid_tank`, `enderio:pressurized_fluid_tank` exist; gated **industrial_revolution**
  (`aoa_astages_01l_tech_stragglers.js:39-40`); **0 quests anywhere** → real gap but IR-tier.
- `enderio:powered_spawner` exists; gated **gilded_age** (`01_item_restrictions.js:269`); **already
  quested** as a task item in `g5_empire_of_iron.snbt` node `4D4F011000000142` (line 3353).

### mekanismadditions (jar-inspected)
Jar `mods/MekanismAdditions-1.21.1-10.7.19.85.jar`. Content = plastic blocks/slabs/stairs/fences/
gates/roads (every color), glow panels (every color), balloons (every color), baby-mob variants,
plus exactly two "functional" items: `mekanismadditions:obsidian_tnt` and
`mekanismadditions:walkie_talkie`. No machine, no processing tier, no progression item.

---

## 1. Drift table — what the 02d prompt got wrong (reconcile, do not re-raise)

| 02d item | prompt says | Ground truth on disk (2026-07-02) | Action |
|---|---|---|---|
| P1 orb ladder | 0 quests, author it | Confirmed: magician/master/archmage = 0 everywhere; gate = gilded | **AUTHOR (T-02d-1)** |
| P1 sentient tools + hi-gems | verify coverage, maybe add Gilded home | Already quested in ow6 (optional depth); tools+gems Gilded-locked, armor is IR | **Reference by dep, do NOT re-task (no dupes)** |
| P2 industrialforegoing (10 machines) | unquested, extend g2 | All 10 already TASK items in g2_the_refinery | **DONE — no action** |
| P2 extrastorage netherite_crafter/advanced_importer | extend g4 | Gated atomic; already quested at4 | **DONE — Gilded placement would be dupe + inversion** |
| P2 appmek cells 1k/4k/16k/256k + housing | extend g4 | Gated atomic; all quested at3 (incl 64k) | **DONE — Gilded placement would be dupe + inversion** |
| P2 g4 sequencing after 02c re-wire | sequence after 02c | No g4 authoring left in 02d at all | **Moot — 02d no longer touches g4** |
| P3 enderio fluid tanks | polish, Gilded | Gated IR; 0 quests | **Reassign to 02c (IR) — see §4** |
| P3 enderio powered_spawner [CANON] | ungated OK / decision | Gilded-gated, already quested g5 | **DONE — [CANON] resolved, no queue entry** |
| P3 mekanismadditions [CANON] | check jar, slot vs skip | decor + 2 non-questable functional items | **SKIP — see §5 call** |
| Flight slot | reserve g-slot + dep link | createpropulsion/aeronautics EXCLUDED (registry Policy 2 + 3) | **DEAD — author nothing** |

---

## 2. T-02d-1 — Neo Vitae orb ladder (the only real Gilded authoring) [SPINE][FOUND]

**File (disjoint):** `config/ftbquests/quests/chapters/g7_chartered_arcana.snbt` (group
`5E42E6B4A7C91D30` = gilded_age; icon convention: task item). **No other 02d task touches g7.**

**Why here:** g7 is the verified Gilded magic home. It currently hosts the Occultism/Theurgy/
Malum/Spectrum magic-authorization convergence (capstone `4341011000000004` grants
`g_magic_authorization_complete`) but contains **zero Neo Vitae**. The blood-orb spine jumps
Renaissance-apprentice → Atomic-transcendent with the entire Gilded middle (magician/master/
archmage) missing. This is the one true continuity hole in the magic spine.

**Design: a 3-rung linear ladder + 1 optional capacity beat.** First-placement-wins: these three
orb ids appear nowhere else, so g7 owns them.

Node ids follow the live g7 scheme (`4341011000000XXX`; task `434101102XXXX001`; reward
`434101103XXXX000`). Reserve the `01A0`–`01A3` band to avoid collision with existing
`0001`–`0005`/`0100`:

| new node id | task item | type | deps | optional? | icon | grid (x,y) |
|---|---|---|---|---|---|---|
| `43410110000001A0` | `neovitae:blood_orb_magician` | item | `["0B03101000000034"]` (Ren apprentice-orb node) | no | `neovitae:blood_orb_magician` | (-8.0, 3.0) |
| `43410110000001A1` | `neovitae:blood_orb_master` | item | `["43410110000001A0"]` | no | `neovitae:blood_orb_master` | (-8.0, 5.0) |
| `43410110000001A2` | `neovitae:blood_orb_archmage` | item | `["43410110000001A1"]` | no | `neovitae:blood_orb_archmage` | (-8.0, 7.0) |
| `43410110000001A3` | `neovitae:rune_2_capacity_augmented` (Reinforced Augmented Capacity Rune) | item | `["43410110000001A1"]` | **yes** | `neovitae:rune_2_capacity_augmented` | (-6.0, 5.0) |

Notes for the implementer:
- **Cross-age dep into Renaissance is intentional and pattern-consistent.** g7 already deps
  backward/cross-age (`4954631000000000` into the IR Obsidilith citadel chapter,
  `0B03101000000058` into ren_magic_foundations). Depending `01A0` on the Ren apprentice-orb node
  `0B03101000000034` places the ladder as the natural continuation. Because g7 has
  `hide_quest_until_deps_complete: true`, these stay hidden until the player has the apprentice orb.
- **Layout / crossing-free:** the existing g7 graph occupies x ∈ [-4, +4], y ∈ [-3, +3]. Put the
  orb ladder as an isolated vertical column at **x = -8** (left of everything), y = 3→7, with the
  optional rune at x = -6. No dependency line crosses any existing g7 edge (the ladder is a
  disconnected left-hand column whose only external edge runs to a different chapter). Verify with
  the crossing checker on the touched file.
- **Preserve `PlayerSpells` + `SkillsLevel` inert blocks** in every task exactly as the sibling g7
  nodes carry them (they regenerate; do not strip).
- **No stage reward on this ladder.** It is spine *content*, not a gate; the Gilded→Atomic grant is
  owned elsewhere. Do not add an `/astages add` reward. Simple `xp` rewards only (suggest 200/300/
  400 for the three rungs, 150 for the optional rune) — reward-table detail is Opus/again-later, not
  load-bearing for structure.
- **`rune_2_capacity_augmented` verification before use:** id proven in jar lang
  (`block.neovitae.rune_2_capacity_augmented = Reinforced Augmented Capacity Rune`). It is a
  legitimate distinct altar-upgrade block and a good optional "why bigger altars matter" beat that
  reinforces the tier story. If the implementer cannot confirm it is craftable at Gilded from a
  recipe json, drop node `01A3` (it is optional and non-load-bearing) rather than guessing.

**Stub lang keys** → sidecar `phase0/stubs/T-02d-1_stubs.txt` (array form, `[STUB]`/`[BRIEF]` per
preamble §5). One `.title`/`.quest_subtitle`/`.quest_desc` triple per new node. BRIEF content to
encode for Opus (do NOT write final prose — that is Opus's lane):
- `01A0` magician (Veneficus): teaches upgrading the apprentice orb to magician on a **Tier-2 Ara
  Vitae**; input is a block of gold, costs 25000 Essentia Vitae; player must have raised their altar
  to T2 with pillars+runes first. Prior node = Renaissance apprentice orb.
- `01A1` master (Magus): **Tier-3** altar, input `weak_blood_shard`, 40000 EV; note the shard is the
  same reagent from the Renaissance line, now spent to climb.
- `01A2` archmage (Dominus): **Tier-4** altar, input a `hellforged_block` (the IR Hellfire-Forge
  metal), 80000 EV; this is the Gilded ceiling of the orb line and the setup for the Atomic
  transcendent orb.
- `01A3` (optional) augmented capacity rune: why altar capacity/tier gating exists; building bigger
  altars is what unlocks each successive orb; optional depth, not required.

**Verification steps (implementer):**
1. `node --check` N/A (no KubeJS). Instead: FTBQ SNBT byte discipline — CRLF/tab preserved,
   `SkillsLevel` intact.
2. Anchored dup scan on the touched file: `grep -P '^\s+id: "'` shows the 4 new node ids + their
   task/reward ids unique.
3. Confirm the 3 orb ids still appear as task items in exactly one place each (g7) after the edit:
   `grep -rn 'blood_orb_magician\|blood_orb_master\|blood_orb_archmage' config/ftbquests/quests/chapters`
   → only g7.
4. Re-run the tier/age audit on `g7_chartered_arcana.snbt`: every task item legal at/before gilded.
5. Crossing-free check on g7 only.
6. Confirm `kubejs/data/neovitae/tags/block/altar/pillars.json` still non-empty (softlock guard).

---

## 3. Sentient tools + hi-gems — decision: keep in ow6, reference by dependency (NO move)

The prompt offered two options: add a Gilded home, OR reference ow6 by dep, OR move the ow6 nodes
into g7 via the id-travel method. **Decision: leave them in ow6, add no g7 tasks for them.**

Rationale:
- No-dupe rule is absolute: ow6 already tasks `sentient_sword`, `sentient_pickaxe`/`axe`, and
  `spiritus_gem_greater`(+lesser/common/grand smart_filter). Re-tasking in g7 is a hard dupe.
- The ow6 nodes are an intentional OW6 optional-depth side-branch (Living Harvest hidden-gear
  pattern), a linear chain rooted at `4256010000010001`. Moving them to g7 breaks that chain and
  churns two chapters for no player-facing gain.
- The items are Gilded-*legal* but not Gilded-*spine*. The magic spine's Gilded obligation is the
  orb ladder (T-02d-1), which is now covered. Sentient tools are gear flavor, correctly surfaced as
  optional depth later.
- **No cross-reference dep is added either.** g7's orb ladder does not need to depend on the ow6
  gear nodes (different age, optional). Adding such an edge would create a forward Gilded→OW
  dependency, which is backwards. So: touch nothing in ow6.

If a future ruling wants a Gilded *pointer* to the gear, the clean move is a single optional g7
"further reading" node with a `check_quest` task pointing at the ow6 node id — but that is out of
scope here and not authored.

---

## 4. enderio fluid tanks — reassign to 02c (IR), not Gilded

`enderio:fluid_tank` + `enderio:pressurized_fluid_tank` are a genuine 0-quest gap, but both are
gated **industrial_revolution**, not Gilded. Age-tier discipline forbids questing an IR-tier item in
a Gilded chapter. Their correct home is the IR EnderIO/tech surface, owned by **02c**. 

**Action for the coordinator:** add these two ids to the 02c IR backlog (EnderIO already has an IR
presence — `void_chassis`/AssemblyLine per the preamble tech table). 02d authors nothing for them.
This plan flags it so the gap is not lost, but does not place it out-of-age.

---

## 5. [CANON] calls

- **mekanismadditions → SKIP (no chapter, no quests).** Jar contents are entirely decor
  (plastic blocks/slabs/stairs/fences/gates/roads in every color, glow panels, balloons) and
  baby-mob variants, plus exactly two functional items: `obsidian_tnt` (a crafting-recipe TNT
  variant) and `walkie_talkie` (a QoL radio toy). None is a legal AoA quest target: no processing
  tier, no progression, and both functional items are checkmark/decor-class (canon forbids
  bare/decor/checkmark tasks). This matches the prior audit note that it is "mostly variant/decor
  gear." **No 08 queue entry needed — the decision is SKIP.**
- **enderio powered_spawner → resolved, author nothing.** Registry says it may be authored ungated;
  it is in fact gilded-gated and already quested as a task item in `g5_empire_of_iron` node
  `4D4F011000000142`. No action, no 08 entry.

---

## 6. Flight slot — DEAD

`createpropulsion` and `aeronautics` are **excluded** (Registry Policy 2 rows + Policy 3 flight
ruling: flight stays unquested and ungated on purpose; many installed the pack for free flight).
The 02d flight g-slot and its dependency-link reservation are void. Author no chapter, no node, no
dep for flight. Do not reference `08_CREATE_GAPS_AND_QA` flight content for Gilded.

---

## 7. Task list (coordinator view)

| Task | Scope | File(s) | Wave / sequencing | Status of prompt item |
|---|---|---|---|---|
| **T-02d-1** | Author Neo Vitae orb ladder (3 required + 1 optional node) | `chapters/g7_chartered_arcana.snbt` + sidecar `phase0/stubs/T-02d-1_stubs.txt` | Independent; no dep on 02c (does not touch g4). Any wave. | P1 — the only real work |
| ~~T-02d-2 (IF)~~ | — | — | — | dropped: already done in g2 |
| ~~T-02d-3 (extrastorage)~~ | — | — | — | dropped: done at4, atomic-gated |
| ~~T-02d-4 (appmek)~~ | — | — | — | dropped: done at3, atomic-gated |
| ~~T-02d-5 (g4 seq)~~ | — | — | — | moot: 02d never touches g4 |
| **handoff → 02c** | enderio fluid_tank + pressurized_fluid_tank (IR-gated, 0 quests) | (02c owns) | 02c wave | P3 reassigned out of age |
| **[CANON] closeouts** | mekanismadditions SKIP; powered_spawner done | (none) | — | P3 resolved, no queue |

**Disjoint-file guarantee:** T-02d-1 touches only `g7_chartered_arcana.snbt` + a new stub sidecar.
It does not touch g2, g4, g5, ow6, or any kubejs/astages file. It is safe to run in any wave with no
sequencing constraint (the earlier "sequence after 02c g4 re-wire" constraint is moot because 02d no
longer authors into g4).

## 8. Ledger delta (for LEDGER.md after implementation)
- g7_chartered_arcana: before = 6 nodes / 6 (2 optional). after = 10 nodes / +3 required +1 optional.
- Net new required quests in Gilded: 3 (magician, master, archmage orbs). Magic spine continuity
  hole closed (Ren apprentice → Gilded magician/master/archmage → Atomic transcendent).
- No gate changes. No dupes introduced (verified: three orb ids first-placed in g7).
