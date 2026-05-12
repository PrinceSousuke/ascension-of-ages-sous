// AoA KubeJS: aoa_astages_00_register_stages.js
// Marker-restriction pattern: registers each AoA stage with AStages by
// attaching a no-op restriction on minecraft:barrier. Barrier is unobtainable
// in survival, so the restriction is invisible to players. This silences the
// astages-common.toml "Enable Warning" for any stage with no real item lock --
// notably the ren_* milestone flags, which are pure progression markers.
// If a future admin task involves real barrier-block restrictions, switch the
// marker item to a different unobtainable id (e.g. minecraft:structure_void).

;(function () {
  if (typeof AStages === 'undefined') return

  function markerRestriction(stage) {
    const id = 'aoa/marker/' + stage
    AStages.addRestrictionForItem(id, stage, 'minecraft:barrier')
  }

  const stages = [
    // Public ages -- already referenced by aoa_astages_01..09; listed here for
    // completeness and to make the registry self-documenting.
    'dark_ages', 'medieval_times', 'the_renaissance',
    'industrial_revolution', 'gilded_age', 'atomic',
    'otherworldly', 'ascension',
    // Renaissance prologue + faculty progression (new -- Phase 1 will grant)
    'ren_matriculated',
    'ren_traditions_partial', 'ren_traditions_complete',
    'ren_worlds_partial', 'ren_worlds_complete',
    'ren_void_studies_unlocked',
    'ren_instruments_partial', 'ren_instruments_complete',
    // Renaissance milestone proofs (new)
    'ren_seal_obtained',
    'ren_dragon_proof_obtained',
    'ren_maledictus_defeated'
  ]
  // 19 stages total, 11 new.

  stages.forEach(markerRestriction)
})()
