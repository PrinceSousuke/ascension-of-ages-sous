// AoA KubeJS: remove_starting_items.js
// NeoForge 1.21.1 / KubeJS 2101.x
//
// FIX (2026-05): The previous version ran clearStubbornItems() every 10 ticks
// forever via PlayerEvents.tick. Each call fires runCommandSilent('/clear ...')
// which triggers InventoryChangeTrigger → full FTBQuests criterion scan →
// ~1.15ms per call × multiple items × all online players. This was the primary
// cause of the 1-2 second delay on container open observed in Spark profiles.
//
// Fix: one-shot scrub window on login (ticks 5→200), then a short post-login
// confirmation window (ticks 200→1200, every 40t), then permanently stop via
// persistentData flag. The tick loop is gone entirely for players who have
// already been scrubbed.
//
// UPDATE (2026-05-02): Added Theurgy + Occultism guidebook entries.
//   - Theurgy uses Modonomicon's standard generated item with the
//     `modonomicon:book_id` data component (verified via book.json:
//     `generate_book_item: True`, book id `theurgy:the_hermetica`).
//     Component name verified via Modonomicon DataComponentRegistry bytecode.
//   - Occultism uses a custom registered item `occultism:dictionary_of_spirits`
//     (verified via book.json: `generate_book_item: False`,
//     `custom_book_item: "occultism:dictionary_of_spirits"`).

const EXACT_STARTING_ITEMS = [
  'patchouli:guide_book[patchouli:book="jtl:jtl_essentia"]',
  'patchouli:guide_book[patchouli:book="jtl:essentia"]',
  'patchouli:guide_book[patchouli:book="jtl:essentia_bible"]',
  'patchouli:guide_book[patchouli:book="divinerpg:divine"]',
  'patchouli:guide_book[patchouli:book="kubejs:first_days_field_guide"]',
  'industrialupgrade:book/guide_book[industrialupgrade:container={listItem:[],open:0b,slot_inventory:-1,uid:0}]',
  // Theurgy "The Hermetica" — Modonomicon-generated, identified by book_id component
  'modonomicon:modonomicon[modonomicon:book_id="theurgy:the_hermetica"]'
]

const BASE_STARTING_ITEMS = [
  'industrialupgrade:book/guide_book',
  'jtl:essentia_bible',
  'ars_nouveau:worn_notebook',
  'alexsmobs:animal_dictionary',
  'modern_industrialization:guidebook',
  'alchemists_garden:overgrown_letter',
  'cosmos_infinia:infinity_opus',
  'industrialupgrade:sensor/sensor',
  'nautec:nautec_guide',
  // Occultism "Dictionary of Spirits" — custom registered item, plain ID
  'occultism:dictionary_of_spirits'
]

const STUBBORN_ITEMS = [
  'integrateddynamics:on_the_dynamics_of_integration',
  'patchouli:guide_book[patchouli:book="jtl:jtl_essentia"]',
  'patchouli:guide_book[patchouli:book="jtl:essentia"]',
  'patchouli:guide_book[patchouli:book="jtl:essentia_bible"]',
  'cosmos_infinia:infinity_opus',
  'jtl:essentia_bible',
  // Re-grant defenders for the new entries — both mods may re-give the book
  // if it's missing from a player's inventory on login. The base/exact lists
  // catch the on-login give; STUBBORN covers any deferred re-give within the
  // 60s confirmation window.
  'modonomicon:modonomicon[modonomicon:book_id="theurgy:the_hermetica"]',
  'occultism:dictionary_of_spirits'
]

// Persistent data keys
const FLAG_FIRST_JOIN_SCRUB   = 'starterBooksScrubbed'
const FLAG_STUBBORN_CLEARED   = 'aoa_stubborn_items_cleared'

// How long (ticks) to keep trying stubborn items after login before giving up.
// 1200t = 60s. Generous enough for slow world loads.
const STUBBORN_CLEAR_WINDOW   = 1200
// Interval (ticks) for stubborn re-checks within the window
const STUBBORN_RECHECK_EVERY  = 40

const SCRUB_ALL_PATCHOULI_ON_FIRST_JOIN = false
const ALLOW_STUBBORN_ITEMS_STAGE = 'starting_books_unlocked'

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function clearItem(player, item) {
  const itemId = item.split('[')[0]
  if (!Item.exists(itemId)) return
  player.server.runCommandSilent(`clear "${player.username}" ${item}`)
}

function clearNormalStartingItems(player) {
  for (const item of EXACT_STARTING_ITEMS) clearItem(player, item)
  for (const item of BASE_STARTING_ITEMS)  clearItem(player, item)
}

function clearAllPatchouliBooks(player) {
  clearItem(player, 'patchouli:guide_book')
}

function clearStubbornItems(player) {
  if (player.stages && player.stages.has(ALLOW_STUBBORN_ITEMS_STAGE)) return
  for (const item of STUBBORN_ITEMS) clearItem(player, item)
}

// ---------------------------------------------------------------------------
// Login — burst scrub window
// ---------------------------------------------------------------------------

PlayerEvents.loggedIn(event => {
  const player  = event.player
  const pData   = player.persistentData
  const server  = event.server
  const isFirst = !pData.getBoolean(FLAG_FIRST_JOIN_SCRUB)

  if (isFirst) {
    pData.putBoolean(FLAG_FIRST_JOIN_SCRUB, true)
  }

  // Normal starting items: fire-and-forget burst on login
  clearNormalStartingItems(player)
  if (isFirst && SCRUB_ALL_PATCHOULI_ON_FIRST_JOIN) clearAllPatchouliBooks(player)

  for (const delay of [5, 20, 40, 100, 200]) {
    server.scheduleInTicks(delay, () => {
      clearNormalStartingItems(player)
      if (isFirst && SCRUB_ALL_PATCHOULI_ON_FIRST_JOIN) clearAllPatchouliBooks(player)
    })
  }

  // Stubborn items: scrub now, then hand off to tick loop for STUBBORN_CLEAR_WINDOW
  // Only if not already confirmed cleared in a previous session
  if (!pData.getBoolean(FLAG_STUBBORN_CLEARED)) {
    clearStubbornItems(player)
  }
})

// ---------------------------------------------------------------------------
// Respawn — re-run normal scrub burst only (stubborn items don't respawn)
// ---------------------------------------------------------------------------

PlayerEvents.respawned(event => {
  const player = event.player
  const server = event.server

  clearNormalStartingItems(player)
  for (const delay of [5, 20, 40, 100, 200]) {
    server.scheduleInTicks(delay, () => clearNormalStartingItems(player))
  }
})

// ---------------------------------------------------------------------------
// Tick — stubborn item confirmation window ONLY
//
// Runs every STUBBORN_RECHECK_EVERY ticks for up to STUBBORN_CLEAR_WINDOW
// ticks after login, then sets the cleared flag and never runs again for
// this player. Zero cost once the flag is set.
// ---------------------------------------------------------------------------

PlayerEvents.tick(event => {
  const player = event.player
  const pData  = player.persistentData

  // Fast-exit: already confirmed cleared
  if (pData.getBoolean(FLAG_STUBBORN_CLEARED)) return

  // Fast-exit: not our interval
  if (player.tickCount % STUBBORN_RECHECK_EVERY !== 0) return

  // Within window: keep clearing
  if (player.tickCount <= STUBBORN_CLEAR_WINDOW) {
    clearStubbornItems(player)
    return
  }

  // Window expired: set flag and stop forever
  pData.putBoolean(FLAG_STUBBORN_CLEARED, true)
})
