# 03 — CREATE ADD-ONS: CLOSE ALL GAPS + QA

**Owner:** Fable (structure + gates + weaves) → Opus (prose) → CC (age-discipline review).
**Prepend:** `01_MASTER_PREAMBLE.md`. **Depends on:** `LEDGER.md` (from 02) signed off.
**Read first:** every file in `AoA redo/40_create_addons/` (INDEX.md + create_base.md +
each add-on doc). They are the machine-level research. Treat their "0 quested" verdicts as
STALE where the ledger says otherwise.

The Create questline rollout is mid-flight: Phase 1 (Ren "Second Mill"), Phase 2 (IR entry
rungs), Phase 4 (Medieval alloyed + sliceanddice) shipped. **Phase 3 was never started.**
This prompt finishes the job.

---

## Priority 1 — Phase 3: the Gilded flight & propulsion line (THE missing phase)

Two installed add-ons have **zero quests and no AStages gate** — a real age-discipline hole
(craftable from world start):
- `create-aeronautics-bundled` (namespaces `aeronautics` / `simulated` / `offroad`):
  Physics Assembler, Portable Engines, Envelopes + Burners, Propellers, Levitite, Wheel
  Mount + Tires. Full physics-contraption flight + ground-vehicle system.
- `create-stuff-additions` (`create_sa`): Copper/Andesite/Brass/Netherite jetpacks +
  exoskeletons, tanks, Brass Drone, grappling hook, slime gear. (Only `drone_controller` is
  currently gated.)

Tasks:
1. **Gate them first** (Fable/CC, KubeJS in `aoa_astages_01g_create_family.js` or a new
   `aoa_astages_01q_create_flight.js`): Aeronautics → `gilded_age` (matches the INDEX.md
   placement table + the 8-age ladder). Stuff & Additions: split by tier — copper/andesite
   jetpack tier → `the_renaissance` "mobility" per the doc, brass/netherite tier →
   `industrial_revolution`/`gilded_age`. Verify each id against the jar before gating.
   Note copper tier is recipe-removed pack-side (`early_overgeared_progression_cleanup.js`)
   — confirm what's actually craftable before questing it.
2. **Author the Gilded flight chapter** (Fable, `.snbt`). Candidate file
   `g3_flight_and_propulsion.snbt` (note: `g3` slot is currently empty — the g-series skips
   3; verify). Teach the arc: Physics Assembler → portable engine → envelope + burner →
   propeller lift → levitite/altitude → wheel-mount ground variant → a capstone airship or
   rover contraption. Crossing-free layout. Bundle the multiblock assembler into one node.
3. **Fold in Create Propulsion** (`createpropulsion`, ~97% unquested, mostly ungated):
   turpentine fuel → first thruster → mount-on-contraption → Stirling branch → Coral/Ion
   tier → vectored capstone. Gate the tiers appropriately (thrusters read as Gilded).
4. **Stuff & Additions mobility branch** — jetpack/exoskeleton/grapple/drone as a Renaissance
   "gadgets" mini-line (or fold into an existing Ren chapter if layout allows without
   crossings). Drone ties to the already-gated `drone_controller`.

## Priority 2 — the thin/partial extensions (base Create + electric)

5. **Create 6.0 Factory Logistics** (base `create:`, still ~untaught after Phase 1):
   `packager` → `stock_link` → `stock_ticker` → `factory_gauge` → `redstone_requester` →
   frogport. This is a Renaissance/IR tail — extend `ren_second_mill_steam_rail_logistics`
   or the IR Create chapter. This is Create's flagship new system; it deserves a real
   teaching sub-line, not a single acquire node.
6. **Create: New Age entry rung** (`create_new_age`): the FIRST electricity node is missing.
   Teach coil + magnets → brushes → wire → basic motor BEFORE the existing reinforced-tier
   quests. Add it upstream in `ir_create_industrial_addons` / `ir_power_motion_and_grid`.
7. **Crafts & Additions supply chain** (`createaddition`): the machine spine is quested but
   the wire/rod/sheet/spool chain + biomass→bioethanol fuel loop (~75% of the mod) is open.
   Add a compact supply-chain node cluster + an explicit **low-current vs high-current wire**
   teaching node (the doc flags this as the #1 new-player confusion point).
8. **Metalwork alloy-by-pour** (`createmetalwork`): entry (molten_iron) + capstone
   (molten_netherite) exist; teach the signature trick — andesite-alloy doubling via a
   12 mB iron/zinc pinch, and the brass 4-ingot pour.
9. **Aquatic Ambitions mechanics** (`create_aquatic_ambitions`): 4/7 items quested in `g6`
   but the two actual MECHANICS (Channeling setup, fluid-effect Conduit Cage) aren't taught.
   Add dedicated nodes. (Also closes 2 of g6's 4 missing-desc defects: `Conduit Cage`
   `A818144300D946A8` and `Alloy From the Reef` `051AB096CA0848B4`.)

## Priority 3 — QA read over already-quested Create

10. **Pedagogy QA** (Opus reads, Fable/CC fix structure if needed): read the prose for every
    already-quested Create machine across `m1_first_mill`, `ren_second_mill_*`,
    `ir_create_industrial_addons`, `ir_power_motion_and_grid`, and the g-series. Flag any
    node where the description does not actually teach the machine, names the wrong item, or
    assumes a mechanic taught later. `m1_first_mill` (55 base-Create nodes) is the tutorial —
    confirm the teaching order is still monotonic after Phase 4 folded Alloyed's
    Forge+Steel+Bronze beat (8 nodes) into it.

## Explicitly DEFER (do not quest — record why in the ledger)
- `create_ultimate_factory` — no ownable items (all outputs vanilla or `create:` intermediates;
  empty lang). At most 2–4 optional "this shortcut exists" prose notes.
- `create_cold_sweat` — registers zero items (behavioral temperature hooks only). Unquestable
  by design; at most a prose tip on an existing IR/Gilded heat node.
- Decor/compat jars (createdeco, createframed, createbetterfps, kubejs-create, emi_create_
  schematics, createoritechcompat, create-otbwg-compat, createaddoncompatibility) — no
  player-facing gating content.

---

## Deliverables from this prompt
- New/edited `.snbt` chapters (crossing-free) + AStages gate entries for the two ungated
  add-ons — with a full VERIFICATION LOG per §2 of the preamble.
- Stub lang keys with teaching briefs for every new node (Opus fills later via prompt 07).
- New/edited `aoa_recipes_gilded_weaves.js` entries for any cross-mod recipe the flight line
  needs (see prompt 06). `node --check` PASS pasted.
- A short "Create coverage: before/after" table appended to `LEDGER.md`.
