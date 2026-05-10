// AoA M1 — Stage emitters for The First Mill capstones.
// E-28 is the hard capstone: emits aoa:medieval_kinetics_mastered (gates M2 entry).
// F-23 is the soft capstone (Brass Horizon completion): emits aoa:medieval_kinetics_fully_mastered.

FTBQuestsEvents.completed(event => {
  const questId = event.getObject().getCodeString()
  const player = event.getPlayer()
  if (!player) return

  const playerName = player.name.string

  if (questId === '7A1F05000000001C') {
    player.runCommandSilent(`astages add ${playerName} aoa:medieval_kinetics_mastered`)
  }

  if (questId === '7A1F060000000017') {
    player.runCommandSilent(`astages add ${playerName} aoa:medieval_kinetics_fully_mastered`)
  }
})
