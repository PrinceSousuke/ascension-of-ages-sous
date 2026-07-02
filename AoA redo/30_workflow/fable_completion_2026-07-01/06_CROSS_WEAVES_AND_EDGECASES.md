# 06 — CROSS-WEAVES + EDGE CASES (KubeJS recipe integration)

**Owner:** Fable (authors weaves) → CC (verifies no softlock / no bad id) → Codex (`node --check` sweep).
**Prepend:** `01_MASTER_PREAMBLE.md`.
**This is the "recipes cross-weaved and edge cases accounted for" work.** It runs alongside
the buildouts (03/04/05), because a chapter that requires a cross-mod item is only safe if
the recipe path to that item is legal at its age.

---

## The established pattern (match it — do not invent a new one)
Cross-mod recipe bridges live in `kubejs/server_scripts/` as per-age weave files:
`aoa_recipes_renaissance_weaves.js`, `aoa_recipes_ir_weaves.js`, `aoa_recipes_gilded_weaves.js`,
`aoa_recipes_atomic_weaves.js`, plus targeted bridges (`magic_spine_bridges.js`,
`ir_magic_feedstock_bridges.js`, `ir_native_capstone_recipes.js`,
`aoa_recipes_capstone_convergence.js`, `aoa_oil_spine_weaves.js`,
`aoa_recipes_neovitae_weaves.js`, `aoa_recipes_oritech_weaves.js`). Read 2–3 of these to
learn the house style (event hooks, id conventions, output policy) before writing new ones.
`zz_aoa_recipe_output_policy.js` is the dedupe/override policy — respect its ordering.

New files this pack needs: `aoa_recipes_otherworldly_weaves.js`,
`aoa_recipes_ascension_weaves.js`, and Gilded-flight additions to
`aoa_recipes_gilded_weaves.js`.

---

## What a weave is FOR (the four edge-case classes)
1. **Cross-age softlock:** an item legal at age N has a recipe requiring an item only legal
   at age N+1. Fix: weave an alternate recipe using only ≤N materials, OR re-gate (canon
   call). The machine-graph audit (prompt 02.A) surfaces these.
2. **Missing bridge:** two mods that SHOULD interoperate don't share a recipe (e.g. Draconic
   energy core needs an intermediate only sold by Mekanism, but no recipe connects them).
   Weave the intermediate.
3. **Recipe collision / dupe:** two mods add the same conceptual item or clash on a tag
   (almostunified territory). Resolve via output policy, don't let both fire.
4. **Amount/throughput trap:** a quest requires N of an item whose only source is a
   slow/locked machine — impossible in practice. Fix the recipe yield or the quest amount.

## Required edge-case checks for THIS pack (verify each; weave or flag)
- **`ae2:singularity` at Otherworldly** — advanced_ae quantum tier needs it. Confirm it's
  obtainable at OW; if the only route is Ascension-tier, weave an OW-legal path or re-gate.
- **Draconic ↔ MI/Mekanism power interop** at OW (RF/FE bridge blocks exist? or needed?).
- **Stellaris fuel path** — legal OW-tier recipe, or does it need atomic/petrochem outputs
  that aren't reachable? Weave the fuel loop.
- **Avaritia infinity chain** — every input legal at Ascension, collectors not required in
  amounts that assume an un-unlocked machine.
- **Extended Crafting table tier order** — elite table must exist before elite recipes;
  no recipe may require a higher-tier table than the quest that grants it.
- **Chaos crystal circularity** — the Draconic Guardian is the FINAL boss; NOTHING pre-final
  may require a chaos crystal / Guardian drop. Scan for it explicitly.
- **Neo Vitae anchor A1** (from the ledger) — if the buildout touches Renaissance magic, the
  `ren_magic_foundations` F&A dep (`0B03101000000039`→`0B0310100000CAFE`) should be repointed
  to the Ara Vitae T1 equivalent. Only do this with a canon sign-off; otherwise leave + flag.

## Method
- Every recipe you weave: log input ids + output id + the grep proving each exists + the age
  each is legal at. A weave that references a non-existent id is a silent break (prompt 02.D
  hunts these — don't create new ones).
- `node --check` every file. Paste PASS lines.
- After weaving, re-run the tier audit (02.A) on the affected chapters to confirm you closed
  the softlock without opening a new one (fixes can cascade — a re-sourced recipe can pull in
  a new too-late material). Iterate until clean.

## Deliverables
- New/edited weave scripts, each `node --check` PASS.
- A "weaves added" table in `LEDGER.md`: `file | recipe | inputs→output | age | why`.
- Confirmation that the post-weave tier audit is clean for OW + Ascension + Gilded-flight.
