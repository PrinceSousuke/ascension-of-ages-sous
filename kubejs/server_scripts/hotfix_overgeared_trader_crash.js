// AoA hotfix: prevent Overgeared wandering-trader blueprint crash
// Crash observed: NPE in overgeared BlueprintData.withQuality during wandering trader tick.
// Temporary mitigation until Overgeared-side fix: disable wandering trader lifecycle.

function purgeWanderingTraders(server) {
  server.runCommandSilent('kill @e[type=minecraft:wandering_trader]')
  server.runCommandSilent('kill @e[type=minecraft:trader_llama]')
}

ServerEvents.loaded(event => {
  // Stop new trader spawns in this world.
  event.server.runCommandSilent('gamerule doTraderSpawning false')

  // Remove any already loaded trader entities (including the crashing one).
  purgeWanderingTraders(event.server)

  // Run a couple delayed passes to catch entities that appear right after load.
  event.server.scheduleInTicks(20, () => purgeWanderingTraders(event.server))
  event.server.scheduleInTicks(200, () => purgeWanderingTraders(event.server))
})

EntityEvents.spawned(event => {
  const type = `${event.entity.type}`
  if (type === 'minecraft:wandering_trader' || type === 'minecraft:trader_llama') {
    event.entity.discard()
  }
})
