// AoA Atomic Age cross-mod weaves (2026-06-10).
// A1 "Yellowcake Interchange" — the nuclear-ladder bridge pinned by
// 22_CANON_nuclear_ladder.md: Mekanism's enrichment line feeds Nuclear
// Science's Nuclear Boiler by joining mekanism:yellow_cake_uranium to the
// c:yellow_cake_uranium tag (stock tag holds only nuclearscience:yellowcake).
// One tag line, no recipe ids touched, no CT collision (CT is greenfield).
// Taught in prose at at3 "Chemical Extractor" / "Nuclear Boiler" and in the
// Atomic Modonomicon book.

ServerEvents.tags('item', event => {
  event.add('c:yellow_cake_uranium', 'mekanism:yellow_cake_uranium')
})
