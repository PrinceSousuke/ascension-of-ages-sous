// AoA KubeJS: aoa_astages_migration_shim.js
// One-shot first-login migration from legacy PS state to AStages-only
// authority. Gated on persistentData flag; flag is set only on the success
// path so an API-name mismatch produces one error per login (recoverable)
// rather than a permanent half-migration.
//
// KubeJS NeoForge 1.21.1 / AStages 2.0.3.
// Inventory access uses player.inventory.containerSize + getItem(i) per
// KubeJS NeoForge 1.21.1; if the runtime exposes player.inventory.items
// instead, swap the scan accordingly (verify against the running KubeJS
// version before shipping).
// AStages JS-bridge method name (hasStage vs playerHasStage) needs to be
// verified against the astages-2.0.3-1.21.1.jar before shipping; the
// runCommandSilent path is idempotent so a duplicate grant is harmless.

const MIGRATION_FLAG = 'aoa_ps_to_astages_migrated'
const LEGACY_INDUSTRIAL_INDICATOR = 'cataclysm:cursium_ingot'
const LATE_STAGES = [
  'industrial_revolution', 'gilded_age', 'atomic', 'otherworldly', 'ascension'
]

function hasStage(player, stage) {
  return typeof AStages !== 'undefined' && AStages.hasStage(player, stage)
}

function grantStage(player, stage) {
  player.server.runCommandSilent(`astages add ${player.username} ${stage} true true`)
}

function hasLegacyCursiumInInventory(player) {
  for (let i = 0; i < player.inventory.containerSize; i++) {
    const stack = player.inventory.getItem(i)
    if (stack && !stack.isEmpty() && String(stack.getItem().id || stack.id) === LEGACY_INDUSTRIAL_INDICATOR) {
      return true
    }
  }
  return false
}

function indicatesIndustrialOrBeyond(player) {
  // Priority 1: existing stage state from a prior migration. Cheap and
  // authoritative -- short-circuits before any inventory scan.
  for (const s of LATE_STAGES) {
    if (hasStage(player, s)) return true
  }
  // Priority 2: legacy heuristic for save-converted players who came across
  // with no AStages state at all.
  return hasLegacyCursiumInInventory(player)
}

PlayerEvents.loggedIn(event => {
  const player = event.player
  const pData = player.persistentData
  if (pData.getBoolean(MIGRATION_FLAG)) return

  let migrationCompleted = false
  try {
    if (indicatesIndustrialOrBeyond(player)) {
      // Public-age backfill: if a prior migration handled the_renaissance,
      // hasStage returns true and the grant is skipped.
      if (!hasStage(player, 'the_renaissance'))           grantStage(player, 'the_renaissance')
      // Renaissance faculty proofs imply industrial entry.
      if (!hasStage(player, 'ren_seal_obtained'))         grantStage(player, 'ren_seal_obtained')
      if (!hasStage(player, 'ren_dragon_proof_obtained')) grantStage(player, 'ren_dragon_proof_obtained')
      if (!hasStage(player, 'ren_maledictus_defeated'))   grantStage(player, 'ren_maledictus_defeated')
      if (!hasStage(player, 'industrial_revolution'))     grantStage(player, 'industrial_revolution')
    }
    migrationCompleted = true
  } catch (e) {
    console.error('[aoa] migration shim failed for ' + player.username + ': ' + e)
    // Do NOT set the flag -- let the player retry on next login after a fix.
  }
  if (migrationCompleted) {
    pData.putBoolean(MIGRATION_FLAG, true)
  }
})
