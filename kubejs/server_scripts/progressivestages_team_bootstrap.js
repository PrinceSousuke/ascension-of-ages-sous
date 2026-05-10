// AoA KubeJS: progressivestages_team_bootstrap.js
// NeoForge 1.21.1 / KubeJS 2101.x
//
// Purpose: Keeps FTB Teams party UUID changes from hiding the starting
// questbook by ensuring dark_ages stage is always granted on join/party events.
//
// FIX (2026-05): The previous version ran aoaBootstrapStage() every 200 ticks
// forever via PlayerEvents.tick. aoaBootstrapStage() calls
// runCommandSilent('stage grant ...') which fires stage-change event hooks on
// every call even when the stage is already present. This added constant
// overhead to the server thread for every online player indefinitely.
//
// Fix: stage grant fires on the correct discrete events (login, party join/leave)
// plus a short post-login confirmation window to catch race conditions with
// FTB Teams UUID reassignment. Once the window expires the tick loop stops
// via persistentData flag. Stage grant is idempotent so duplicate calls
// during the window are harmless.

const AOA_BOOTSTRAP_STAGE    = 'dark_ages'
const FLAG_BOOTSTRAP_STABLE  = 'aoa_bootstrap_stage_stable'
const BOOTSTRAP_WINDOW       = 600   // ticks — 30s, enough for any Teams UUID race
const BOOTSTRAP_RECHECK_EVERY = 200

// ---------------------------------------------------------------------------
// Helper
// ---------------------------------------------------------------------------

function aoaBootstrapStage(player) {
  player.server.runCommandSilent(
    `stage grant ${player.username} ${AOA_BOOTSTRAP_STAGE}`
  )
}

// ---------------------------------------------------------------------------
// Login
// ---------------------------------------------------------------------------

PlayerEvents.loggedIn(event => {
  const player = event.player

  // Reset window flag — Teams UUID may reassign after this event
  player.persistentData.putBoolean(FLAG_BOOTSTRAP_STABLE, false)

  aoaBootstrapStage(player)
})

// ---------------------------------------------------------------------------
// Party events — fire immediately, reset window in case of UUID churn
// ---------------------------------------------------------------------------

FTBTeamsEvents.playerJoinedParty(event => {
  const player = event.getEntity()
  player.persistentData.putBoolean(FLAG_BOOTSTRAP_STABLE, false)
  aoaBootstrapStage(player)
})

FTBTeamsEvents.playerLeftParty(event => {
  const player = event.getEntity()
  player.persistentData.putBoolean(FLAG_BOOTSTRAP_STABLE, false)
  aoaBootstrapStage(player)
})

// ---------------------------------------------------------------------------
// Tick — short confirmation window only, not infinite
// ---------------------------------------------------------------------------

PlayerEvents.tick(event => {
  const player = event.player
  const pData  = player.persistentData

  // Fast-exit: already confirmed stable this session
  if (pData.getBoolean(FLAG_BOOTSTRAP_STABLE)) return

  // Fast-exit: not our interval
  if (player.tickCount % BOOTSTRAP_RECHECK_EVERY !== 0) return

  // Within window: re-grant to handle any delayed Teams UUID flip
  if (player.tickCount <= BOOTSTRAP_WINDOW) {
    aoaBootstrapStage(player)
    return
  }

  // Window expired: mark stable and stop
  pData.putBoolean(FLAG_BOOTSTRAP_STABLE, true)
})
