// AoA KubeJS: magic_spine_bridges.js
// Batch 9 verified bridge recipes only. Keep broad material policy and tech
// bridge rollout in their own batches.

ServerEvents.recipes(event => {
  // Oritech Core 5 stays an Oritech advanced-computing milestone, but now
  // requires explicit Forbidden Arcanus, Theurgy, and Malum proof.
  event.remove({ id: 'oritech:crafting/core5' })

  event.shaped('oritech:machine_core_5', [
    'DAD',
    'HCM',
    'DAD'
  ], {
    A: 'oritech:adamant_ingot',
    C: 'oritech:advanced_computing_engine',
    D: '#aoa:magic_feedstock',
    H: 'malum:hallowed_gold_ingot',
    M: 'theurgy:mercury_catalyst'
  }).id('aoa:magic_spine/oritech_machine_core_5')
})
