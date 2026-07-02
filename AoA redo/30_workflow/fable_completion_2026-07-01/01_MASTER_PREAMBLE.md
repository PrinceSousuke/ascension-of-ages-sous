# 01 — MASTER PREAMBLE (prepend to EVERY delegation prompt in this pack)

You are working on **Ascension of Ages**, a NeoForge 1.21.1 CurseForge modpack. The
quest layer is **FTB Quests**. This preamble is the shared contract. Do not violate it.
If any instruction below conflicts with a task-specific prompt, STOP and ask for a canon
call rather than guessing.

---

## 0. Who does what (model lanes — do not cross them)

- **Fable** — STRUCTURAL AUTHOR. Builds quest-node graphs (`.snbt`), cross-weave recipe
  scripts (KubeJS), AStages gate entries, and handles mod fleshing-out + edge cases.
  Authors from a census it verifies itself. Emits structure with **stub lang keys only**
  (see §5). Fable does NOT write player-facing prose.
- **Opus** — PROSE AUTHOR. Writes `en_us.snbt` values (title / subtitle / description) for
  the nodes Fable scaffolds. Never edits structure.
- **Codex** — deterministic bulk + validation at scale: mass find/replace, byte-format
  normalization, `node --check` sweeps, dependency-crossing computation, gate-audit runs.
- **Claude Code (CC)** — reasoning-heavy verification, canon-call judgment, age-discipline
  review of Fable output, final merge review.

**Handshake:** Fable authors structure → Opus fills prose → Codex normalizes/validates
mechanically → CC does the independent age-discipline + softlock review before merge.

---

## 1. The 8 ages (ordered) — VERIFIED live stage IDs

```
dark_ages → medieval_times → the_renaissance → industrial_revolution
→ gilded_age → atomic → otherworldly → ascension
```

Exact IDs (do not typo): `the_renaissance` has the `the_` prefix; `atomic` has **no**
`_age` suffix; `dark_ages` is plural. Registered in
`kubejs/server_scripts/aoa_astages_00_register_stages.js`.

**Age-tier discipline (HARD RULE):** a quest may only require items/mods/mechanics legal
at or before its chapter's age. Later-tier tech in an earlier chapter is a hard defect and
usually a real softlock. Confirm every item's unlock stage against the AStages scripts
BEFORE placing it.

---

## 2. VERIFY-FIRST PROTOCOL (non-negotiable — this is how Fable is allowed to author structure safely)

Fable is fast but ID-hallucination-prone. The ONLY safe way to let it author structure is
to force verification and make it show its work. Every structural deliverable MUST ship
with a **VERIFICATION LOG**. No log = the work is rejected unmerged.

For every item / block / fluid / tag ID you place, the log must contain:
- the exact `grep`/registry command you ran, AND
- the file or jar path that confirms the ID exists (e.g. a recipe json, a lang entry, the
  jar's `data/<namespace>/` tree), AND
- the AStages line proving it's legal at (or before) the target age.

For every KubeJS file you create or edit: paste the `node --check <file>` PASS line.

If you cannot verify an ID, you may NOT use it. Write `UNVERIFIED: <what/why>` and stop on
that node. Never invent an item ID. Never assume a recipe exists.

**Tooling truth:** the file mount can misreport truncation/corruption. Use `wc -l`,
`grep -c`, `sed`, `node --check`, or Desktop Commander as ground truth. Never "repair" a
file on a single truncation report — that has caused real damage before.

---

## 3. Per-age legal tech (VERIFIED 2026-07-01 from `aoa_astages_01*.js`) — the census baseline

This is the baseline; re-verify against the live scripts at author time (gates move).

| Mod family | Starts at | Notes |
|---|---|---|
| **Mekanism** (base) | industrial_revolution | processing spine (infuser/enrichment/crusher/PRC/chem). Uranium chain + digital_miner + hazmat → **atomic**. (VERIFIED override: Mek starts IR, not later.) |
| **AE2** | industrial_revolution | ME spine (controller/drive/cells 1k–256k). megacells/expandedae → gilded; spatial → atomic; advanced_ae quantum → otherworldly |
| **Refined Storage** | industrial_revolution | controller/grid/disk_drive. extrastorage netherite + INFINITE tier → atomic |
| **Oritech** | industrial_revolution | basic processing. machine_core_4/assembler → gilded; atomic_forge/core_5-7/duratium → atomic |
| **Modern Industrialization** | industrial_revolution | LV bronze/steel. aluminum/stainless + petrochem → gilded; titanium/nuclear → atomic; iridium/quantum/plasma/superconductor (fusion) → **otherworldly** |
| **Create family** | Medieval/Renaissance base | createaddition/new_age electric/dieselgen/oreexcavation → IR; aquatic_ambitions → gilded; new_age nuclear (thorium) → atomic |
| **PneumaticCraft / Applied Pneumatics** | industrial_revolution | pressure spine (compressed_iron/PCB = IR ceiling); drone programming → gilded |
| **Immersive Engineering / Petroleum** | industrial_revolution | full multiblock fleet; radio_tower/auto_lubricator → gilded |
| **Industrial Foregoing** | gilded_age | whole fleet (user call 2026-05-28); black-hole advanced → atomic; supreme → otherworldly |
| **Nuclear/power cluster** (createnuclear, nuclearscience, electrodynamics, ballistix, powergrid) | powergrid=IR (analog) | reactor/fuel-cycle spine → atomic; ballistix antimatter/darkmatter → otherworldly |
| **EnderIO** | industrial_revolution | void_chassis/AssemblyLine; ensouled/soul_stained_steel → gilded |
| **Draconic Evolution** | **otherworldly** (base+wyvern) | awakened/chaotic/reactor tier → **ascension** |
| **Re:Avaritia** | **ascension** | all prestige tier |
| **Extended Crafting** | basic=IR | advanced/ender/flux → gilded; elite/ultimate/crystaltine → **ascension** |
| **Stellaris (space)** | **otherworldly** | rocket/cables/tanks/banks space-infra family |
| **Astral Dimension** | gilded_age | supreme_altar/astranite_cauldron |

**Dimension gates** (`aoa_astages_03_dimension_restrictions.js`): Nether/End/Otherside/
Starlight/Aether/Undergarden → the_renaissance. Astral → gilded_age. Spectrum Deeper Down
→ atomic. NeoVitae dungeon → industrial_revolution. Stellaris planets + the_afterdark →
otherworldly. Macabre's Pit → atomic.

---

## 4. Capstone boss chain (VERIFIED from `boss_progression_proof.js` + `aoa_astages_08_*`)

| Age gate | Required capstone boss | Proof item |
|---|---|---|
| Renaissance → IR | `cataclysm:maledictus` | `cataclysm:cursium_ingot` |
| IR → Gilded | `bosses_of_mass_destruction:obsidilith` | `bosses_of_mass_destruction:obsidian_heart` |
| Gilded → Atomic | `astral_dimension:void_titan` | `astral_dimension:void_boots_helmet` |
| Atomic (required spine) | `macabre:valamon` + `gomoria` + `gargamaw` + `baal` + `fdbosses:geburah` (exam) | respective `_heart` / `fdbosses:justice_core` |
| Otherworldly → Ascension | `cataclysm:the_leviathan` | `cataclysm:tidal_claws` |
| Ascension final | `draconicevolution:draconic_guardian` (Chaos/Draconic Guardian) | MQT `kill_entity` task (not a proof-item drop) |

Age-boundary stage grants fire from FTBQ command rewards inside the `.snbt` (KubeJS does
NOT grant stages — it only registers restrictions + mirrors to the team). Canonical capstone
grant is `/aoa reward grant_team` + `/advancement grant`, NOT a bare `/astages add`.

---

## 5. Prose lives SEPARATELY from structure — this is why Fable is safe here

- **Structure** = `config/ftbquests/quests/chapters/*.snbt` — coordinates, `dependencies:`,
  `tasks:`, `rewards:`, `icon:`. NO player-facing text here.
- **Prose** = `config/ftbquests/quests/lang/en_us.snbt`, keyed by quest id:
  `quest.<id>.title`, `quest.<id>.quest_subtitle`, `quest.<id>.quest_desc` (array-of-strings
  form — the pack standard; 1857/1864 use arrays, normalize any new ones to arrays too).

**Fable's stub-key rule:** when you author a new quest node, add its three lang keys with a
short machine-readable placeholder that encodes the TEACHING BRIEF for Opus, e.g.:

```
quest.4C57010000010042.title: "[STUB] title"
quest.4C57010000010042.quest_subtitle: "[STUB] subtitle"
quest.4C57010000010042.quest_desc: ["[BRIEF] teaches: Stellaris rocket assembly; requires stellaris:rocket_engine (gated otherworldly); prior node = launch_pad; edge case: needs fuel loop from ow2. Opus: write 2-4 para instruction-first."]
```

Opus later replaces every `[STUB]`/`[BRIEF]` value with real prose. This keeps Fable out of
the language entirely while still handing Opus everything it needs.

---

## 6. Hard authoring rules

1. **Layout:** dependency lines must NOT cross (hard constraint). Flow direction is
   negotiable (vertical/backward OK). 0.5 grid. Pool same-mod quests. First-placement-wins.
   Bundle multiblocks into one node. No filler / duplicate / vanilla-recipe / checkmark
   quests. Quality over density — never pad to a number.
2. **`.snbt` byte discipline:** preserve CRLF + tab structure; coordinate-only edits for
   layout. Do NOT strip the `SkillsLevel` block (inert More Quest Types mixin artifact;
   `check:0b`; regenerates on save — stripping it is a known mistake).
3. **Task types — use only PROVEN types** (verified in live use): `item`, `xp`, `loot`,
   `random`, `command`, `advancement`, `kill`, `check_quest`, `choice`, `dimension`,
   `xp_levels`, `structure`, `place_block`, `use_block`, `biome`, `custom`, `timer`. Use the
   More Quest Types extended types (`random`, `choice`, `structure`, `kill`, etc.) for
   variety, but verify any type ID you haven't personally seen in a live chapter before use.
   Never invent a task-type ID.
4. **Duplicate-id scans:** use anchored `grep -P '^\s+id: "'` — a loose `id:` grep
   false-positives on `autofocus_id:`.
5. **Icons:** `icon = task item`; for non-item quests use a verified distinct mod icon
   (check the jar's item models, never guess an id).
6. **Teach foundations, not just capstones.** The pack's dominant defect is big tech mods with
   dense endgame chapters but ZERO onboarding (AE2 controller, Mekanism enrichment chamber,
   Oritech machine core — all currently unquested). When completing a mod, author its entry
   rungs FIRST, then re-point the existing endgame quests to depend on them. A player must be
   able to path from the foundation to the taught endgame by following quests alone.
7. **Coverage source of truth:** `02a_COMPLETION_BACKLOG.md` (per-age, from the verified census
   at `AoA redo/30_workflow/mod_quest_coverage_census_2026-07-02.md`). 216 of 303 content mods
   are not fully quested — work the backlog, do not re-derive scope from scratch.

---

## 7. Current canon state (mixed — verify per-anchor, do NOT assume "shipped")

- **Magic spine = Neo Vitae** (Forbidden & Arcanus demoted to optional/decor). Neo Vitae is
  STAGED live (Ren→Atomic). BUT: capstone **anchor A1 is NOT done** —
  `ren_magic_foundations.snbt` still deps F&A node `0B03101000000039` (arcane_bone_meal) into
  capstone aggregator `0B0310100000CAFE`. Oritech tag-swap anchors A2/A3 ARE done
  (`#aoa:magic_feedstock` holds neovitae + deorum alternates).
- **Hephaestus Forge tier gating is non-monotonic** (T4/T5 lock back to `the_renaissance`) —
  likely a leftover bug; flag for a canon call, don't cite as intentional.
- **Renaissance Redistribution + Apotheosis tier moves = NOT executed** (still a runbook).
- **Removed mods:** phantasm, luminous_nether, gardens_of_the_dead. **Alloy Forgery does not
  exist on 1.21.1** — do not suggest it. "Alloyed" is a separate installed mod (Alloy Forge).

---

## 8. Prose voice (for Opus; Fable only needs to know it exists)

Instruction-first. Teach the mechanic. 2–4 short paragraphs. Short declarative sentences.
**No em dashes anywhere.** No AI-isms, no "the X is the lesson" aphorisms. Reference live
AoA Modonomicon prose for voice. Player-facing text must tell the player what to build/do
and why it matters mechanically.

---

**END PREAMBLE. The task-specific prompt follows below when you paste it.**
