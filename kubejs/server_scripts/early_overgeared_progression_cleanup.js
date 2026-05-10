// ============================================================================
//  Early Overgeared progression cleanup
// ============================================================================
//
//  Intent:
//    - Overgeared is the canonical early tool and armor path.
//    - Copper gear must come from Overgeared, not side-mod grid recipes.
//    - Vanilla iron/gold/diamond tools and iron armor must not be shortcut by
//      Apotheosis smithing upgrades before players work through heated ingots,
//      forged heads, and the Overgeared tier ladder.
//
//  Keep:
//    - Overgeared copper tools, copper armor, heated iron, and forged tool heads.
//    - Mod-specific later hammers such as the MI forge hammer; those are not
//      vanilla-tier tool replacements and are quested in their own chapters.
// ============================================================================

const NON_OVERGEARED_COPPER_GEAR_RECIPES = [
  'alltheores:copper_ore_hammer',
  'butchery:copperhammerrecipe',
  'create:crafting/appliances/copper_diving_boots',
  'create:crafting/appliances/copper_diving_helmet',
  'create_sa:copper_axe_recipe',
  'create_sa:copper_boots_recipe',
  'create_sa:copper_chestplate_recipe',
  'create_sa:copper_exoskeleton_recipe',
  'create_sa:copper_helmet_recipe',
  'create_sa:copper_hoe_recipe',
  'create_sa:copper_leggings_recipe',
  'create_sa:copper_pickaxe_recipe',
  'create_sa:copper_propeler_recipe',
  'create_sa:copper_shovel_recipe',
  'create_sa:copper_sword_recipe',
  'iceandfire:armor_copper_boots',
  'iceandfire:armor_copper_chestplate',
  'iceandfire:armor_copper_helmet',
  'iceandfire:armor_copper_leggings',
  'iceandfire:armor_copper_metal_boots',
  'iceandfire:armor_copper_metal_chestplate',
  'iceandfire:armor_copper_metal_helmet',
  'iceandfire:armor_copper_metal_leggings',
  'iceandfire:copper_axe',
  'iceandfire:copper_hoe',
  'iceandfire:copper_pickaxe',
  'iceandfire:copper_shovel',
  'iceandfire:copper_sword'
]

const NON_OVERGEARED_VANILLA_TIER_UPGRADES = [
  'apotheosis:smithing/upgrade_chainmail_boots_to_iron_boots',
  'apotheosis:smithing/upgrade_chainmail_chestplate_to_iron_chestplate',
  'apotheosis:smithing/upgrade_chainmail_helmet_to_iron_helmet',
  'apotheosis:smithing/upgrade_chainmail_leggings_to_iron_leggings',
  'apotheosis:smithing/upgrade_golden_axe_to_diamond_axe',
  'apotheosis:smithing/upgrade_golden_hoe_to_diamond_hoe',
  'apotheosis:smithing/upgrade_golden_pickaxe_to_diamond_pickaxe',
  'apotheosis:smithing/upgrade_golden_shovel_to_diamond_shovel',
  'apotheosis:smithing/upgrade_golden_sword_to_diamond_sword',
  'apotheosis:smithing/upgrade_iron_axe_to_golden_axe',
  'apotheosis:smithing/upgrade_iron_hoe_to_golden_hoe',
  'apotheosis:smithing/upgrade_iron_pickaxe_to_golden_pickaxe',
  'apotheosis:smithing/upgrade_iron_shovel_to_golden_shovel',
  'apotheosis:smithing/upgrade_iron_sword_to_golden_sword',
  'apotheosis:smithing/upgrade_stone_axe_to_iron_axe',
  'apotheosis:smithing/upgrade_stone_hoe_to_iron_hoe',
  'apotheosis:smithing/upgrade_stone_pickaxe_to_iron_pickaxe',
  'apotheosis:smithing/upgrade_stone_shovel_to_iron_shovel',
  'apotheosis:smithing/upgrade_stone_sword_to_iron_sword',
  'titanium:test_serializer/dirt_to_used'
]

ServerEvents.recipes(event => {
  NON_OVERGEARED_COPPER_GEAR_RECIPES.forEach(id => event.remove({ id: id }))
  NON_OVERGEARED_VANILLA_TIER_UPGRADES.forEach(id => event.remove({ id: id }))
})
