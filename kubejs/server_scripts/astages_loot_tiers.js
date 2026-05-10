;(function () {
  if (typeof AStages === 'undefined') {
    // ProgressiveStages is active; skip legacy AStages hooks safely.
    return
  }

  function configureLootRestriction(restriction) {
    // Keep AStages restrictions focused on generated/container loot only.
    // Normal block drops like ore mining should be handled by ProgressiveStages, not AStages.
    return restriction.applyForEveryLootTableAndDrop(false)
  }

  // Before medieval: keep early treasure from handing out major gem skips.
  // Do NOT gate normal ore drops, low-tier metals, or broad progression here.
  configureLootRestriction(AStages.addRestrictionForLoot('pack/loot/requires_medieval_times', 'medieval_times'))
    .restrictTags(
      'c:gems'
    )
    .ignoredItems(
      'minecraft:coal',
      'minecraft:charcoal',
      'minecraft:flint',
      'minecraft:quartz',
      'minecraft:amethyst_shard',
      'minecraft:redstone',
      'minecraft:lapis_lazuli'
    )

  // Before renaissance: no diamond/emerald jackpot gem spikes.
  configureLootRestriction(AStages.addRestrictionForLoot('pack/loot/requires_the_renaissance', 'the_renaissance'))
    .restrictTags('c:gems')
    .ignoredItems(
      'minecraft:lapis_lazuli',
      'minecraft:quartz',
      'minecraft:amethyst_shard',
      'minecraft:redstone'
    )

  // Before renaissance: no advanced tech materials/components.
  configureLootRestriction(AStages.addRestrictionForLoot('pack/loot/requires_the_renaissance_advanced', 'the_renaissance'))
    .restrictTags(
      'c:alloys',
      'c:circuits'
    )

  // Before renaissance: no huge endgame chest spikes.
  configureLootRestriction(AStages.addRestrictionForLoot('pack/loot/requires_the_renaissance_endgame', 'the_renaissance'))
    .restrictTags(
      'c:storage_blocks',
      'c:foods/golden'
    )
})()
