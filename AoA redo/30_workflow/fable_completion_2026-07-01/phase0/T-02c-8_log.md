# T-02c-8 log — Deeper & Darker gear-tail MOVE (ledger row 8)

Task: MOVE two smithing-template quests + the duplicate `sonorous_staff` quest out of
`ren_deeper_darker_otherside` and INTO `ir_netherite_citadel_obsidilith`, re-parenting onto
the citadel's existing `resonarium_helmet` node. `warden_carapace` STAYS in Ren (coordinator
adjudication F.2). Quest ids travel unchanged in spirit (fresh citadel-scheme ids assigned;
lang precedent = Neo Vitae move).

## Files edited (contract file set)
- `config/ftbquests/quests/chapters/ren_deeper_darker_otherside.snbt` (source: 3 leaves deleted)
- `config/ftbquests/quests/chapters/ir_netherite_citadel_obsidilith.snbt` (destination: 3 nodes added)
- `AoA redo/30_workflow/fable_completion_2026-07-01/phase0/stubs/T-02c-8_stubs.txt` (sidecar, created)

No `en_us.snbt` edit (forbidden). Orphaned old Ren lang keys (9 lines:
`quest.0B0310600000008D/8F/91.{title,quest_subtitle,quest_desc}`) left in place for the
Codex normalization sweep per plan section C / T-02c-8 "Lang" note.

## Nodes MOVED

| old Ren id (DELETED) | item | -> new citadel id (ADDED) | citadel coords | dep |
|---|---|---|---|---|
| `0B0310600000008F` | `deeperdarker:warden_upgrade_smithing_template` | `49540C1000000030` | x-3.0 y-3.0 | `["49540C1000000029"]` |
| `0B0310600000008D` | `deeperdarker:resonarium_upgrade_smithing_template` | `49540C1000000031` | x-3.0 y-4.5 | `["49540C1000000029"]` |
| `0B03106000000091` | `deeperdarker:sonorous_staff` (DUPLICATE) | `49540C1000000032` | x-3.0 y-6.0 | `["49540C1000000029"]` |

New nodes: `hide_until_deps_visible: true`, `optional: true`, xp:10 reward, icon = task item
(default). `SkillsLevel`/`PlayerSpells` blocks copied byte-for-byte from the sibling
`49540C1000000029` task shape (never hand-typed/stripped). Fresh reward ids
`49540C300000003{0,1,2}` and task ids `49540C200000003{0,1,2}` (all proven unique pack-wide,
occurrences == 1 each).

### Coordinate deviation from plan (documented)
Plan C/T-02c-8 assigned the moved trio to (-1.5,-4.5)/(0.0,-4.5)/(1.5,-4.5). Cell (-1.5,-4.5)
is ALREADY OCCUPIED in the live citadel by `49540C100000002C` (aether:valkyrie_queen kill),
so the planned row would collide and risk clipping the root->valkyrie edge. Re-laid the trio
into the fully-empty x=-3.0 column (y -3.0/-4.5/-6.0), hanging LEFT off the host helmet node
at (-1.5,-3.0). This preserves "small DD sub-lane off the resonarium_helmet node", stays clear
of the root fan-out (all root children sit at x>=-1.5), and is crossing-free (verified below).

## Re-wire (Ren side)
DELETED the three leaf nodes. All three proved to be pure LEAVES:
`dependencies:` arrays in the entire Ren chapter reference each moved id 0 times (script check).
Nothing dangles. Load-bearing hubs kept in Ren and verified present after edit:
`0B0310600000008E` warden_carapace, `0B03106000000034` resonarium, `0B03106000000033`
reinforced_echo_shard, `0B03106000000045` sonorous_staff (external-gated original), and
`0B03106000000090` deeperdarker:lite (which sat between the deleted blocks and stays).

warden_carapace `0B0310600000008E` STAYS in Ren per F.2 (it is not a leaf: depends on the
load-bearing reinforced_echo_shard hub; moving it would invert a dependency across ages).
The moved warden template is therefore re-parented onto the citadel `resonarium_helmet`
(`49540C1000000029`), NOT onto carapace.

## Proof-stage integrity
Neither the Ren chapter capstone nor the `ren_deeper_darker_otherside_complete` grant depends
on any of the three moved leaves (they have zero dependents). No AStages grant altered. DD gear
legal in an IR citadel chapter: deeperdarker family floor is at/before IR; the citadel already
hosts betterend/undergarden/deeperdarker post-Ren gear as its reward tail (established role).

## Verification (outputs)

### Item-id proofs (jar)
`mods/deeperdarker-neoforge-1.21.1-1.4.1.jar` en_us.json — all three FOUND:
`warden_upgrade_smithing_template`, `resonarium_upgrade_smithing_template`, `sonorous_staff`.
(Also pre-existing tasks in Ren, already jar-proven in PLAN section E.)

### AStages legality (gating CLOSED, cited from plan E)
deeperdarker family is Renaissance-tier deep-dark content; no lock later than IR applies.
tier_audit reports all three citadel nodes as **OK** at `industrial_revolution`.

### tier_audit.py
`0 SOFTLOCK` in regenerated `A_tier_softlock_table.md` (grep -c SOFTLOCK = 0). My three nodes
listed as **OK** (industrial_revolution). Surviving Ren sonorous_staff `0B03106000000045` = OK.

### ef_audit.py
- DUP ids: {} (0)
- DANGLING dep sources: 0 / total dangling edges: 0
- BACKWARD-age deps: 0
- ORPHANS: 1 (`3400000000009000` in stone_water_weather_and_wounds — pre-existing, not mine)
- MISSING quest_desc: 166 (includes my 3 new nodes pending Opus prose — expected; stubs filed)

### Byte / structure discipline
- ren_deeper_darker_otherside.snbt: CRLF 1124, lone_lf 0; braces 200/200; brackets 134/134.
- ir_netherite_citadel_obsidilith.snbt: CRLF 2506, lone_lf 0; braces 439/439; brackets 207/207.
- Both files pure CRLF (matched pre-edit line-ending profile). Tabs preserved.

### Anchored id-dup scan
`^\s+id: "49540C100000003[012]"` across all chapters: only the 3 new definitions (unique).
Reward/task ids (`...2/300000003X`) each occur exactly once pack-wide.

### Duplicate-item scan
`deeperdarker:sonorous_staff` now appears in Ren (`0B03106000000045`) and citadel
(`49540C1000000032`) — distinct quests, no single-chapter dup; the redundant Ren duplicate
`0B03106000000091` was removed by the move (de-dupe). Templates appear once each pack-wide.

### Crossing statement
- CITADEL: baseline crossings at HEAD = 5; post-edit = 5; NEW crossings introduced by this edit
  = 0. Crossings involving my new nodes (30/31/32) = 0. (The 5 are all pre-existing among other
  nodes and outside this task's file-set scope.) My three left-hanging edges from
  (-1.5,-3.0) into the empty x=-3.0 column intersect no existing edge (segment-intersection
  test, shared-endpoints excluded). PASS for this task's contribution.
- REN: 0 crossings total after deletion (deletion cannot add crossings).

### KubeJS
No KubeJS file touched — `node --check` N/A.
