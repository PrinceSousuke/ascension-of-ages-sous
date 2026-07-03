# Ascension of Ages — Quest Scope Registry

**Authoritative, standing reference. Read this before any coverage census, "not-fully-done"
audit, gap report, or gating proposal.** It records mods that are deliberately OUT of quest
scope and the pack's standing gating policy, so these decisions stop getting re-litigated every
pass. If a census or audit flags anything listed here as "unquested / not done / needs a gate,"
that census is wrong — reconcile against this file, do not re-raise it.

Maintained by Andrew. Agents: do not delete rows. Add new rulings with a date. When in doubt,
ask for a ruling rather than assuming a mod is in scope.

Referenced from `AOA_AGENT_CANON.md` §9.

---

## Policy 1 — Gating (STANDING, 2026-07-02)
**No coverage-driven gating.** Ungated mods do not need AStages gates. Do not propose, add, or
flag gates for mods just because they are "ungated." Nothing currently ungated is required to be
gated. (Intentional existing gates on progression tech stay as they are — that is a separate,
already-settled contract in `aoa_astages_*.js`. This policy is specifically about NOT inventing
new gates for coverage/age-discipline reasons.)

Consequence: any report section titled like "139 ungated mods need gating" is void. Drop it.

---

## Policy 2 — Excluded from questing (STANDING)
These mods are **out of quest scope**. Do not author quests for them, do not list them as
"not fully done," do not treat their items as missing coverage. They are content the pack
includes for players to use freely, not to be gated behind or taught by the questbook.

| modId | Common name | Category | Ruling |
|---|---|---|---|
| `botanypots` | Botany Pots | farming/QoL | excluded 2026-07-02 |
| `archers` | Archers | RPG class | excluded 2026-07-02 |
| `paladins` | Paladins | RPG class | excluded 2026-07-02 |
| `rogues` | Rogues | RPG class | excluded 2026-07-02 |
| `wizards` | Wizards | RPG class | excluded 2026-07-02 |
| `armory_rpgs` | Armory RPGs | RPG gear | excluded 2026-07-02 |
| `skill_tree` | Skill Tree | RPG skill system | excluded 2026-07-02 ("skill tree rpgs") |
| `puffish_skills` | Puffish's Skills | RPG skill backbone | excluded 2026-07-02 (companion to the RPG class series — confirm) |
| `spell_engine` | Spell Engine | RPG spellcasting | excluded 2026-07-02 |
| `spell_power` | Spell Power | spell attribute lib | excluded 2026-07-02 (companion to spell_engine — confirm) |
| `runes` | Runes | magic/utility | excluded 2026-07-02 |
| `relics` | Relics | trinkets | excluded 2026-07-02 |
| `supplementaries` | Supplementaries | decor/QoL | excluded 2026-07-02 |
| `bellsandwhistles` | Bells & Whistles | decor | excluded 2026-07-02 |
| `waystones` | Waystones | travel/QoL | excluded 2026-07-02 |
| `alltheores` | All The Ores | ore unification | excluded 2026-07-02 |
| `zoniex` | ZoNiEx | content | excluded 2026-07-02 |
| `create_dragons_plus` | Create Dragons Plus | content | excluded 2026-07-02 |
| `immersive_aircraft` | Immersive Aircraft | transport | excluded 2026-07-02 |
| `createpropulsion` | Create Propulsion | flight | excluded 2026-07-02 (see flight ruling below) |
| `aeronautics` | Create: Aeronautics | flight | excluded (flight stays free/ungated) |
| `alexscaves` | Alex's Caves | worldgen/content | excluded 2026-07-02 |
| `the_afterdark` | The Afterdark | dimension | excluded 2026-07-02 |

Two rows tagged "(confirm)" are the skill/attribute backbones of the excluded RPG/spell mods
(`puffish_skills` powers the archers/paladins/rogues/wizards skill trees; `spell_power` is the
attribute library for `spell_engine`). They are excluded on the same rationale; remove them here
if that inference is wrong.

Also previously ruled excluded (kept for continuity): `artifacts`.

---

## Policy 3 — Standing scope rulings (in scope, but special handling)
Not excluded, but do not treat as ordinary "fill it out" targets:

- **Flight** (`aeronautics`, `createpropulsion`) — stays **unquested and ungated** on purpose.
  Many players installed the pack for free-flight. Do not gate it, do not build a chapter for it.
- **`railways`** (Steam 'n' Rails) — **minimal only**: a couple of quests at most, never a chapter.
- **`psi`** — **optional-only, never required.** May appear as an optional side beat; never on any
  spine or as a dependency of a capstone.
- **`avaritia`, `stellaris`, `modern_industrialization`, `extendedcrafting`** — **thorough
  endgame treatment.** These get deep, complete coverage (they are the tentpole endgame trees).
- **`createnuclear`, `createoreexcavation`, `powergrid`** — **leave alone.** Already placed; no
  rework.
- **`ftboceanmobs`** — **being dropped** from the pack. Author no coverage for it.

---

## How future passes must use this
1. Load this file at the start of any coverage/census/gap/gating task.
2. Subtract every Policy-2 mod from the "content mods" denominator and from any not-done list.
3. Never emit a gating recommendation (Policy 1).
4. Apply Policy-3 handling verbatim.
5. If you believe something here is wrong or stale, flag it to Andrew for a ruling. Do not
   silently re-scope.

## Changelog
- **2026-07-02** — Registry created. Policy 1 (no coverage-driven gating) set. 23 mods excluded
  (Policy 2). Policy-3 rulings consolidated from the 02a backlog rulings + this session.
