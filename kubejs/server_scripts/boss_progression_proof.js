// AoA KubeJS: boss_progression_proof.js
// Batch 5 - P1 Boss Proof and Combat Cheese Hardening.
//
// Boss proof authority is quest-proof first where a wrapper exists.
// Stage grants live in FTB Quests AStages command rewards, not here.
// Non-player deaths lose capstone proof drops and capture output.

const AOA_BOSS_PROOF = {
  // ============================================================================
  // REQUIRED SPINE BOSSES (Route 2: guaranteed proof drop on real-player kill)
  // ============================================================================

  // Renaissance capstone proof.
  'cataclysm:maledictus': {
    proof: 'cataclysm:cursium_ingot',
    guaranteeProofDrop: true,
    strip: [
      'cataclysm:cursium_ingot',
      'cataclysm:music_disc_maledictus',
      'cataclysm:maledictus_spawn_egg'
    ]
  },

  // Industrial Revolution capstone proof.
  'bosses_of_mass_destruction:obsidilith': {
    proof: 'bosses_of_mass_destruction:obsidian_heart',
    guaranteeProofDrop: true,
    strip: [
      'bosses_of_mass_destruction:obsidian_heart',
      'bosses_of_mass_destruction:obsidilith_spawn_egg'
    ]
  },

  // Industrial Revolution co-required Qliphoth exam (boss-ladder BL1, 2026-07-02).
  // Core is a guaranteed single-roll drop; guarantee it on real-player kills and
  // strip the proof/trophy on non-player kills so the IR capstone fan-in is not bypassable.
  'fdbosses:chesed': {
    proof: 'fdbosses:lightning_core',
    guaranteeProofDrop: true,
    strip: [
      'fdbosses:lightning_core',
      'fdbosses:phase_sphere',
      'fdbosses:chesed_trophy',
      'fdbosses:chesed_spawn_egg'
    ]
  },

  // Gilded Age co-required Qliphoth exam (boss-ladder BL1, 2026-07-02).
  'fdbosses:malkuth': {
    proof: 'fdbosses:fire_and_ice_core',
    guaranteeProofDrop: true,
    strip: [
      'fdbosses:fire_and_ice_core',
      'fdbosses:malkuth_fist',
      'fdbosses:malkuth_trophy',
      'fdbosses:malkuth_spawn_egg'
    ]
  },

  // Atomic judgment and consequence exam.
  'fdbosses:geburah': {
    proof: 'fdbosses:justice_core',
    guaranteeProofDrop: true,
    strip: [
      'fdbosses:justice_core',
      'fdbosses:divine_gear',
      'fdbosses:geburah_trophy',
      'fdbosses:polished_justicestone',
      'fdbosses:geburah_spawn_egg'
    ]
  },

  // Gilded -> Atomic Astral proof component.
  'astral_dimension:void_titan': {
    proof: 'astral_dimension:void_boots_helmet',
    guaranteeProofDrop: true,
    strip: [
      'astral_dimension:void_boots_helmet',
      'astral_dimension:titan_helmet_upgrade_template',
      'astral_dimension:astral_amulet',
      'astral_dimension:void_titan_present',
      'astral_dimension:void_titan_spawn_egg'
    ]
  },

  // Atomic horror-biotech containment spine.
  'macabre:valamon': {
    proof: 'macabre:valamon_heart',
    guaranteeProofDrop: true,
    strip: [
      'macabre:valamon_heart',
      'macabre:valamon_pack',
      'macabre:valamon_spawn_egg'
    ]
  },
  'macabre:gomoria': {
    proof: 'macabre:gomoria_heart',
    guaranteeProofDrop: true,
    strip: [
      'macabre:gomoria_heart',
      'macabre:gomoria_pack',
      'macabre:gomoria_spawn_egg'
    ]
  },
  'macabre:gargamaw': {
    proof: 'macabre:gargamaw_heart',
    guaranteeProofDrop: true,
    strip: [
      'macabre:gargamaw_heart',
      'macabre:gargamaw_pack',
      'macabre:gargamaw_spawn_egg'
    ]
  },
  'macabre:baal': {
    proof: 'macabre:baal_heart',
    guaranteeProofDrop: true,
    strip: [
      'macabre:baal_heart',
      'macabre:baal_pack',
      'macabre:baal_spawn_egg'
    ]
  },

  // ============================================================================
  // QUESTED OPTIONAL SIDE BOSSES (Route 5: strip non-player/capture outputs)
  // ============================================================================
  // Future optional candidates belong here only after canon assigns an FTBQ
  // optional task: Cataclysm Harbinger/Ignis/Ender Guardian/Netherite
  // Monstrosity/Ancient Remnant/Revenant/Clawdian/Ender Golem, BFB roster,
  // BOMD Lich/Void Blossom/Gauntlet, and fdbosses Malkuth/Chesed.
  'cataclysm:scylla': {
    proof: 'cataclysm:essence_of_the_storm',
    guaranteeProofDrop: false,
    strip: [
      'cataclysm:essence_of_the_storm',
      'cataclysm:astrape',
      'cataclysm:lacrima',
      'cataclysm:storm_eye',
      'cataclysm:ceraunus',
      'cataclysm:music_disc_scylla',
      'cataclysm:scylla_spawn_egg'
    ]
  },

  // ============================================================================
  // DEMOTED - RENAISSANCE REALM LITERACY OPTIONAL DEPTH (Route 5)
  // ============================================================================
  // Eternal Starlight remains side-depth proof-only content unless later promoted.
  'eternal_starlight:the_gatekeeper': {
    proof: 'eternal_starlight:orb_of_prophecy',
    guaranteeProofDrop: false,
    strip: [
      'eternal_starlight:orb_of_prophecy',
      'eternal_starlight:book',
      'eternal_starlight:music_disc_optimized_option',
      'eternal_starlight:the_gatekeeper_spawn_egg'
    ]
  },
  'eternal_starlight:starlight_golem': {
    proof: 'eternal_starlight:oxidized_alloy_furnace',
    guaranteeProofDrop: false,
    strip: [
      'eternal_starlight:oxidized_alloy_furnace',
      'eternal_starlight:oxidized_golem_steel_ingot',
      'eternal_starlight:forge_armor_trim_smithing_template',
      'eternal_starlight:energy_sword',
      'eternal_starlight:music_disc_mechanical_fossil',
      'eternal_starlight:starlight_golem_spawn_egg'
    ]
  },
  'eternal_starlight:permafrost': {
    proof: 'eternal_starlight:coldsnap',
    guaranteeProofDrop: false,
    strip: [
      'eternal_starlight:coldsnap',
      'eternal_starlight:frozen_tube',
      'eternal_starlight:oxidized_golem_steel_nugget',
      'eternal_starlight:permafrost_spawn_egg'
    ]
  },
  'eternal_starlight:lunar_monstrosity': {
    proof: 'eternal_starlight:soul_dew',
    guaranteeProofDrop: false,
    strip: [
      'eternal_starlight:soul_dew',
      'eternal_starlight:moonring_bow',
      'eternal_starlight:tenacious_petal',
      'eternal_starlight:tenacious_vine',
      'eternal_starlight:lunar_monstrosity_spawn_egg'
    ]
  },

  // ============================================================================
  // REQUIRED - Otherworldly -> Ascension boss proof, owned by OW6 planning.
  // ============================================================================
  // The staged FTBQ plan checks both the kill and tidal_claws. Guarantee the
  // proof on real-player kills so the required OW gate is not RNG-blocked.
  'cataclysm:the_leviathan': {
    proof: 'cataclysm:tidal_claws',
    guaranteeProofDrop: true,
    strip: [
      'cataclysm:tidal_claws',
      'cataclysm:abyssal_egg',
      'cataclysm:music_disc_the_leviathan',
      'cataclysm:the_leviathan_spawn_egg'
    ]
  },

  // ============================================================================
  // REQUIRED - RENAISSANCE DIMENSION/EXPLORATION BOSSES (boss-ladder BL2, 2026-07-02)
  // ============================================================================
  // Nine Renaissance required bosses feed their own dimension chapter's proof-grant
  // quest (which already fans into the Renaissance age grant 0B0310A0000000F0).
  // Each item-proof drop is a guaranteed single-roll entity drop, so guarantee it on
  // real-player kills and strip proof/utility drops on non-player kills to keep the
  // chapter fan-in un-bypassable. Kill-only bosses (starlight_golem, gatekeeper) use an
  // MQT kill task as their proof; no LootJS guarantee is needed there.

  // Nether threshold: Ignis (ignitium_ingot).
  'cataclysm:ignis': {
    proof: 'cataclysm:ignitium_ingot',
    guaranteeProofDrop: true,
    strip: [
      'cataclysm:ignitium_ingot',
      'cataclysm:music_disc_ignis',
      'cataclysm:ignis_spawn_egg'
    ]
  },
  // Nether threshold: The Harbinger (witherite_block).
  'cataclysm:the_harbinger': {
    proof: 'cataclysm:witherite_block',
    guaranteeProofDrop: true,
    strip: [
      'cataclysm:witherite_block',
      'cataclysm:music_disc_the_harbinger',
      'cataclysm:the_harbinger_spawn_egg'
    ]
  },
  // Nether threshold: Nether Gauntlet. Native blazing_eye drops from a death-spawned
  // chest table, not the entity table, so move it onto the real-player kill path (see
  // the addTableModifier below) exactly like Obsidilith's heart.
  'bosses_of_mass_destruction:gauntlet': {
    proof: 'bosses_of_mass_destruction:blazing_eye',
    guaranteeProofDrop: true,
    strip: [
      'bosses_of_mass_destruction:blazing_eye',
      'bosses_of_mass_destruction:gauntlet_spawn_egg'
    ]
  },
  // Aether literacy: Valkyrie Queen (silver_dungeon_key).
  'aether:valkyrie_queen': {
    proof: 'aether:silver_dungeon_key',
    guaranteeProofDrop: true,
    strip: [
      'aether:silver_dungeon_key',
      'aether:valkyrie_queen_spawn_egg'
    ]
  },
  // Undergarden descent: Forgotten Guardian (forgotten_nugget).
  'undergarden:forgotten_guardian': {
    proof: 'undergarden:forgotten_nugget',
    guaranteeProofDrop: true,
    strip: [
      'undergarden:forgotten_nugget',
      'undergarden:forgotten_guardian_spawn_egg'
    ]
  }

  // ============================================================================
  // DEFERRED
  // ============================================================================
  // Future required bosses belong above only after live FTBQ or canon assigns
  // them a Route 2 proof role. Draconic Guardian is intentionally absent:
  // live FTBQ uses the More Quest Types kill task as the proof.
  // Bosses never grant age stages here.
}

function aoaEventSource(event) {
  if (!event) return null
  try {
    if (event.source) return event.source
  } catch (ignored) {}
  try {
    if (event.getSource) return event.getSource()
  } catch (ignored) {}
  return null
}

function aoaSourceEntity(source) {
  if (!source) return null
  try {
    if (source.entity) return source.entity
  } catch (ignored) {}
  try {
    if (source.getEntity) return source.getEntity()
  } catch (ignored) {}
  return null
}

function aoaEntityTypeId(entity) {
  if (!entity) return ''
  try {
    if (entity.type) return String(entity.type)
  } catch (ignored) {}
  try {
    if (entity.getType) return String(entity.getType())
  } catch (ignored) {}
  try {
    if (entity.isPlayer && entity.isPlayer()) return 'minecraft:player'
  } catch (ignored) {}
  try {
    const className = String(entity.getClass().getName())
    if (className.indexOf('ServerPlayer') !== -1 || className.indexOf('.Player') !== -1) {
      return 'minecraft:player'
    }
  } catch (ignored) {}
  return ''
}

function aoaIsRealPlayerKill(event) {
  return aoaEntityTypeId(aoaSourceEntity(aoaEventSource(event))) === 'minecraft:player'
}

function aoaSourcePlayer(event) {
  const entity = aoaSourceEntity(aoaEventSource(event))
  return aoaEntityTypeId(entity) === 'minecraft:player' ? entity : null
}

function aoaDropItemId(drop) {
  if (!drop) return ''

  let stack = null
  try {
    if (drop.item) stack = drop.item
  } catch (ignored) {}
  if (!stack) {
    try {
      if (drop.getItem) stack = drop.getItem()
    } catch (ignored) {}
  }
  if (!stack) return ''

  try {
    if (stack.id) return String(stack.id)
  } catch (ignored) {}
  try {
    if (stack.item && stack.item.id) return String(stack.item.id)
  } catch (ignored) {}
  try {
    if (stack.getId) return String(stack.getId())
  } catch (ignored) {}
  try {
    if (stack.getItem && stack.getItem().id) return String(stack.getItem().id)
  } catch (ignored) {}

  return ''
}

function aoaShouldStripDrop(id, bossProof) {
  if (!id) return false
  return bossProof.strip.indexOf(id) !== -1 || id.endsWith('_spawn_egg') || id === 'minecraft:spawn_egg'
}

function aoaStripDrops(event, bossProof, includeProofDrops) {
  let drops = null
  try {
    if (event.getDrops) drops = event.getDrops()
  } catch (ignored) {}
  if (!drops) {
    try {
      if (event.drops) drops = event.drops
    } catch (ignored) {}
  }
  if (!drops || !drops.size || !drops.get || !drops.remove) return

  for (let i = drops.size() - 1; i >= 0; i--) {
    const drop = drops.get(i)
    const id = aoaDropItemId(drop)
    const isCaptureOutput = id.endsWith('_spawn_egg') || id === 'minecraft:spawn_egg'
    if ((includeProofDrops && aoaShouldStripDrop(id, bossProof)) || isCaptureOutput) {
      drops.remove(i)
    }
  }
}

Object.keys(AOA_BOSS_PROOF).forEach(entityId => {
  EntityEvents.drops(entityId, event => {
    const bossProof = AOA_BOSS_PROOF[entityId]
    const realPlayerKill = aoaIsRealPlayerKill(event)
    aoaStripDrops(event, bossProof, !realPlayerKill)
  })
})

LootJS.modifiers(event => {
  Object.keys(AOA_BOSS_PROOF).forEach(entityId => {
    const bossProof = AOA_BOSS_PROOF[entityId]
    if (!bossProof.guaranteeProofDrop) return

    const modifier = event.addEntityModifier(entityId)
    modifier.removeLoot(bossProof.proof)
    modifier.addLoot(
      LootEntry.of(Item.of(bossProof.proof, 1))
        .when(condition => condition.killedByPlayer())
    )
  })

  // Obsidilith's native proof is a structure/arena chest table. Move the heart
  // to the real-player kill path above so opening an arena chest is never proof.
  event.addTableModifier('bosses_of_mass_destruction:chests/obsidilith')
    .removeLoot('bosses_of_mass_destruction:obsidian_heart')

  // Nether Gauntlet's native proof (blazing_eye) is a death-spawned arena chest table.
  // Move it onto the real-player kill path above so opening the chest is never proof.
  event.addTableModifier('bosses_of_mass_destruction:chests/gauntlet')
    .removeLoot('bosses_of_mass_destruction:blazing_eye')
})

