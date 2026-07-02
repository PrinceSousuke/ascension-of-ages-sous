# T1 — Neo Vitae tier fix: VERIFICATION LOG

Implements `J_neovitae_curve.md`. Working-tree only; NO git run. Executed 2026-07-02.

Status: **DONE_WITH_CONCERNS** (two documented canon calls on de-duplication; see §7).

---

## 1. Part 1 — AStages lock down-tier (`kubejs/server_scripts/aoa_astages_01m_magic.js`)

Down-tiered 4 sentient-armor locks Gilded -> IR (jar-justified per J §1f: sentient armor
is Alchemy-Array-made from a Common gem + iron armour, reachable once the IR-locked
Hellfire Forge is built):

| item | old | new |
|---|---|---|
| `neovitae:sentient_helmet`  | gilded_age | industrial_revolution |
| `neovitae:sentient_plate`   | gilded_age | industrial_revolution |
| `neovitae:sentient_leggings`| gilded_age | industrial_revolution |
| `neovitae:sentient_boots`   | gilded_age | industrial_revolution |

**Sentient TOOLS left at gilded_age** (`sentient_sword/pickaxe/axe`). Verified no IR node
quests them: `grep sentient_sword|pickaxe|axe ir_magic_feedstock_and_spectrum_network.snbt`
= NONE. They are only used by OW6 (optional depth), which is >= gilded, so still legal.

`node --check` result:
```
NODE_CHECK_PASS: kubejs/server_scripts/aoa_astages_01m_magic.js
```

---

## 2. Part 2 — node moves into `ir_magic_feedstock_and_spectrum_network.snbt`

The IR chapter already teaches the Hellfire Forge (`49540B1000000004`, use_block) and
already has a `neovitae:hellforged_block` item node (`49540B1000000018`). The 8 listed
nodes were integrated as two vertical sub-branches hanging off the forge node `04`.

Two of the 8 are DUPLICATE item tasks of content already present in the target and were
DE-DUPLICATED instead of moved (canon: "no near-duplicate variants", "first-placement-wins"):

- `0B03102000000047` (hellforged_block) — DROPPED. Duplicate of existing `49540B1000000018`.
- `0B03101000000038` (spiritus_gem_petty) — DROPPED. Duplicate of the moved `0B03102000000081`
  (also petty). J §4 row 5 explicitly says "dedupe with #6".

6 nodes physically relocated into the IR chapter (ids/task-ids/xp-reward-ids UNCHANGED so
their existing lang keys stay valid). New rewards are xp-only (matching the source Ren
nodes); no loot-table id fabricated.

Hellforged column (x = -3.0), rooted at forge `49540B1000000004`:
| id | item | dep | x,y |
|---|---|---|---|
| `0B03102000000041` | hellforged_dust  | `49540B1000000004` | -3.0, -6.5 |
| `0B03102000000042` | ingot_hellforged | `0B03102000000041` | -3.0, -8.0 |
| `0B03102000000046` | hellforged_parts | `0B03102000000042` | -3.0, -9.5 |

Spiritus-gem column (x = -2.0), rooted at forge `49540B1000000004`:
| id | item | dep | x,y |
|---|---|---|---|
| `0B03102000000081` | spiritus_gem_petty  | `49540B1000000004` | -2.0, -6.5 |
| `0B03101000000070` | spiritus_gem_lesser | `0B03102000000081` | -2.0, -8.0 |
| `0B03101000000075` | spiritus_gem_common | `0B03101000000070` | -2.0, -9.5 |

The existing block node `49540B1000000018` was LEFT UNCHANGED (still dep `04`); the
dust->ingot->parts chain and the existing block node are parallel children of the forge.
Rewiring `18` to sit downstream of `parts` was TESTED and rejected: it forced the
parts->block line across the sentient-armor fan and the `06->22` vertical (+4 crossings).
Keeping `18` parallel keeps the chapter crossing-clean (see §5).

Column placement chosen in the empty far-left region (x = -3.0/-2.0), which held no nodes
or edges. Verified 0 new crossings.

---

## 3. Renaissance rewiring — `ren_nether_threshold.snbt`

Removed 5 quest objects: `0B03102000000041, 42, 46, 47, 81`.

Orphaned dependent rewired:
- `0B03102000000080` (neovitae:blood_pearl, STAYS — Ren-legal, was `dep 0B03102000000042`)
  -> re-pointed to closest surviving Ren ancestor `0B03102000000040` (neovitae:rune_speed),
  and RELOCATED into the vacated hellforged space at **x 1.5,10.5 -> 6.0,0.0**. 0 new crossings.
- `0B03102000000081` was `80`'s only child; it moved to IR, so `80` now has no child.

Chapter-icon retarget (was `neovitae:ingot_hellforged`, now IR-only):
- **file-level `icon`** (header) : `neovitae:ingot_hellforged` -> `neovitae:blood_pearl`.
- **root quest `0B03102000000001` icon** (dimension task; decorative) : `ingot_hellforged`
  -> `neovitae:blood_pearl`.
- **capstone reward icon** on `0B03302000000060` (the `ren_nether_threshold_complete` grant):
  `ingot_hellforged` -> `neovitae:blood_pearl`.
`neovitae:blood_pearl` is Ren-locked (`aoa_astages_01m_magic.js:121`) and remains tasked in
the chapter (node `0B03102000000080`). After retarget, 0 remaining `ingot_hellforged` refs.

Capstone chain unaffected: `0B03102000000062` (grant) deps `0B03102000000061`
(create:empty_blaze_burner) -> `0B03102000000021` (fortress). No moved node fed the grant.

---

## 4. Renaissance rewiring — `ren_magic_foundations.snbt`

Removed 3 quest objects: `0B03101000000038, 70, 75`.

Orphaned dependents rewired to closest surviving Ren ancestor:
- `0B03101000000071` (neovitae:raw_spiritus, was `dep 0B03101000000070`) -> `0B03101000000001`
  (chapter root, malum:spirit_altar / overworld — the NV spine origin), and repositioned to
  the vacated column-head slot **y 1.5 -> 0.0** (x stays 18.0) so the x=18 column stays contiguous.
- `0B03101000000076` (neovitae:blood_pearl, was `dep 0B03101000000075`) -> `0B03101000000074`
  (neovitae:spiritus_ruina_shard). Adjacent in-column, 0 new crossings.
- `0B03101000000038` was a leaf (no children); removed cleanly (deduped, see §2).

Capstone unaffected: `ren_magic_foundations_complete` grant chain does not depend on any moved
node.

---

## 5. Crossing check (hard constraint)

Segment-intersection test (shared endpoints excluded), computed directly on the final files
and, for the IR chapter, against the HEAD version:

| chapter | crossings HEAD/pre | crossings final | involving moved/rewired nodes | new introduced |
|---|---|---|---|---|
| `ir_magic_feedstock_and_spectrum_network` | 14 (37 nodes) | 14 (43 nodes) | **0** | **0** |
| `ren_nether_threshold` | 19 | 13 | **0** | **0** (removed 6) |
| `ren_magic_foundations` | 4 | 4 | 1 (`01->71` x `30->31`) | **0 net** |

Statements:
- **IR new branch is fully crossing-free** — the chapter had 14 crossings at HEAD and still
  has exactly 14 after adding the 6 nodes; none of the 14 touch a moved/new node. The
  pre-existing 14 are in the chapter's dense convergence hub (unrelated to this task).
- **ren_nether_threshold**: moving the hellforged branch out REMOVED 6 pre-existing crossings
  (19 -> 13); the `80` re-parent/relocation adds none.
- **ren_magic_foundations**: the single crossing that touches a rewired node (`01->71` vs the
  long `30->31` vertical) is NOT new — it structurally REPLACES the removed `01->70` crossing
  (identical geometry: `71` now sits at `70`'s old (18,0) slot). `30->31` was already crossed
  3x by node `01`'s pre-existing fan (`01->51`, `01->60`, `01->70`); this is a pre-existing
  layout defect in that chapter, outside this task's scope. Net crossing count unchanged (4->4).
  No NEW crossing pattern was introduced by the fix.

---

## 6. Tier audit (proof)

`python "AoA redo/30_workflow/fable_completion_2026-07-01/phase0/tier_audit.py"`

| run | SOFTLOCK | ILLEGAL | CANON |
|---|---|---|---|
| before any edit (from J audit) | 12 | 0 | 21 |
| after Part 1 lock down-tier only | 8 | 0 | 21 |
| **after full fix (final)** | **0** | 0 | 21 |

All 12 tier mismatches resolved. The 21 CANON rows are pre-existing family-floor advisories
(immersiveengineering items in `metallurgy` @ medieval; modern_industrialization bronze in
`ren_observation_experimentation`) — untouched by and unrelated to this task.

Integrity: all three chapters brace-balanced, no duplicate quest ids
(ren_nether 40 quests, ren_magic_foundations 62, ir_magic_feedstock 43). All 6 moved-node
lang keys (`quest.<id>.title`) still resolve in `lang/en_us.snbt`. All three files remain
pure CRLF. `en_us.snbt` was NOT touched.

---

## 7. Concerns / canon calls (why DONE_WITH_CONCERNS)

1. **Two de-dups vs the literal "move 8" instruction.** The prompt listed 8 nodes to move,
   but `0B03102000000047` (hellforged_block) and `0B03101000000038` (petty gem) are exact
   duplicates of content already in the IR target (`49540B1000000018` block; and the other
   moved petty `81`). Canon forbids duplicate item tasks, so these two were DROPPED, not
   duplicated. 6 nodes physically relocated. J §4 already anticipated the petty dedupe;
   the block dedupe follows the same rule. Their orphaned lang keys were left in place
   (instruction: do not touch lang).

2. **`ren_magic_foundations` pre-existing crossings.** Node `01`'s fan crosses the `30->31`
   vertical 3x independent of this task. The fix is crossing-neutral there but does not clean
   up that pre-existing defect (out of scope). Flag for a later layout pass if desired.

3. **Latent (not in scope):** `ren_magic_foundations` node `0B03101000000037` is a
   `use_block` task on `neovitae:hellfire_forge` (an IR-locked block) sitting in a Renaissance
   chapter. The tier audit only scans `type:"item"` tasks, so it is not flagged, and `37` was
   not on the move list. It is a real Ren-page reference to an IR block (its child `38` was the
   petty gem now removed). Recommend a follow-up canon call on whether `37` should also move to
   IR. Left untouched here.
