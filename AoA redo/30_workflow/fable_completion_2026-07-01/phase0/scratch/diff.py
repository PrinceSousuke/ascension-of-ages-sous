import zipfile, glob, re, os, collections

chdir="config/ftbquests/quests/chapters"
ns_counter=collections.Counter()
pats=[re.compile(r'item:\s*"([a-z0-9_]+):'),re.compile(r'entity:\s*"([a-z0-9_]+):'),
      re.compile(r'advancement:\s*"([a-z0-9_]+):'),re.compile(r'block:\s*"([a-z0-9_]+):'),
      re.compile(r'id:\s*"([a-z0-9_]+):')]
for f in glob.glob(os.path.join(chdir,"*.snbt")):
    raw=open(f,encoding='utf-8',errors='replace').read()
    for p in pats:
        for m in p.finditer(raw):
            if m.group(1)!='minecraft': ns_counter[m.group(1)]+=1

modids=set()
for jar in glob.glob("mods/*.jar"):
    try: z=zipfile.ZipFile(jar)
    except: continue
    toml=None
    for name in ("META-INF/neoforge.mods.toml","META-INF/mods.toml"):
        if name in z.namelist(): toml=z.read(name).decode('utf-8','replace'); break
    if toml:
        in_mods=False
        for ln in toml.splitlines():
            s=ln.strip()
            if s.startswith('[['): in_mods=(s=='[[mods]]'); continue
            if s.startswith('[') and not s.startswith('[['): in_mods=False; continue
            if in_mods:
                m=re.match(r'modId\s*=\s*"([^"]+)"',s)
                if m: modids.add(m.group(1))
    z.close()

noncontent={
 'architectury','balm','bcc','bookshelf','cloth_config','codechickenlib','collective','commoncapabilities',
 'corgilib','creativecore','cucumber','cyclopscore','fabric_api','forgified_fabric_api','framework','fzzy_config',
 'geckolib','glitchcore','glodium','hammerlib','iceberg','kotlinforforge','lodestone','midnightlib','moonlight',
 'octolib','owo','platform','prickle','puzzleslib','resourcefulconfig','resourcefullib','rhino','searchables',
 'shield_api','smartbrainlib','structure_pool_api','txnilib','yungsapi','zeta','zerocore','azurelib','azurelibarmor',
 'brandonscore','dragonlib','edivadlib','exclusions_lib','experiencelib','extralib','libraryferret','ldlib2','morejs',
 'particle_core','playeranimator','productivelib','ranged_weapon_api','ritchiesprojectilelib','runelic','sable',
 'tesseract_api','wunderlib','yet_another_config_lib_v3','cerbons_api','clavis','cryonicconfig','bundleapi',
 'almanac','athena','biolith','blueprint','bclib','wover','aeroblender','necronomicon','nyctography','pigpen',
 'jupiter','uranus','taxov','hopo','lmft','mifa','nerb','beb','civil','potentials',
 'skill_tree_rpgs','spell_power','combat_roll',
 'kubejs','kubejs_create','kubejs_mekanism','crafttweaker','lootjs','aoacore','config_manager','configureddefaults',
 'wabbanodecompanion','questinstaller','defaultoptions','starterkit',
 'sodium','lithium','c2me','ferritecore','entityculling','immediatelyfast','badoptimizations','fastboot','servercore',
 'spark','noisium','packetfixer','clumps','letmedespawn','netherportalfix','borderlesswindow','iris','irisflw',
 'emi','jei','jade','journeymap','controlling','mousetweaks','trashslot','emi_create_schematics','emi_enchanting',
 'emi_loot','emi_ores','emiffect','emixx','toomanyrecipeviewers','distraction_free_recipes','obscure_tooltips',
 'enchdesc','equipmentcompare','overflowingbars','betterf3','ambientsounds','sound_physics_remastered','particlerain',
 'notenoughanimations','visualworkbench','craftingtweaks','polymorph','clienttweaks','revelationary',
 'obsidianui','blockui','guideme','extraquests','more_quest_types','ftbquestsentityvis','certain_questing_additions',
 'loot_journal','yeetusexperimentus','travelerstitles','explorerscompass','naturescompass','waystones',
 'ftblibrary','ftbteams','ftbchunks','ftbchunks_modded','ftbessentials','ftbxmodcompat','ftbpc','ftbqopt','ftbfiltersystem',
 'crafting_on_a_stick','item_obliterator','trimmed','runes','patchouli','modonomicon',
 'tectonic','terrablender','terralith','lithostitched','structurify','atistructures','moogs_structures','incendium',
 'fragmentum','stonycliffs','regions_unexplored','ohthetreesyoullgrow','snowundertrees','biomeswevegone',
 'betterdeserttemples','betterfortresses','betterjungletemples','bettermineshafts','betterwitchhuts','cataclysmfortresses',
 'ocean_lily_pad_village','underwater_village','aether_villages','explore_ruins_aether','hellish_trials','moa_decor_electronics',
 'yungsbridges','create_otbwg_compat',
 'chipped','chisel','copycats','handcrafted','furniture','factory_blocks','refurbished_furniture','immersive_furniture',
 'mcwbridges','mcwdoors','mcwfences','mcwfurnitures','mcwlights','mcwpaintings','mcwpaths','mcwroofs','mcwstairs',
 'mcwtrpdoors','mcwwindows','diagonalfences','diagonalwalls','diagonalwindows','doubledoors','fastitemframes',
 'fastpaintings','supplementaries','amendments','quark','quarkoddities','quarkengineering','darkutils',
 'abyssal_decor','create_furnitures','create_confectionery','treechop','corail_woodcutter','constructionwand',
 'cubes_without_borders','cb_microblock','cb_multipart','cb_multipart_minecraft',
 'bettercombat','critical_strike','archers','rogues','paladins','wizards','armory_rpgs','mahou_tsukai_combat',
 'attributefix','puffish_skills','curios','accessories','sophisticatedcore','extendedterminal',
 'revamped_phantoms','creeperoverhaul','livingthings','endermanoverhaul','monsterplus',
 'bwncr','incontrol','lootr','tombstone','comforts','thirst','cold_sweat','eclipticseasons','appleskin',
 'smallships','immersive_aircraft','immersive_machinery','createpropulsion',
 'createnuclear','createoreexcavation','powergrid',
 'euphoria_patcher','prism','vanillabackport',
 'hearth_and_timber',
 'ftboceanmobs',
 # confirmed non-content stragglers (verified via jar lang inspection)
 'advancement_portals','aether_emissivity','allthecompatibility','configured',
 'create_ultimate_factory', # recipe-only pack, registers zero items
 'the_afterdark', # dimension gate but only teleport block/catalyst in this build
 'variantsandventures', # 4 ordinary mob variants only
}
# hybrid_aquatic asset namespace is 'hybrid-aquatic' (hyphen) and IS covered (m3+g6)
HYPHEN_COVERED={'hybrid_aquatic'}
integration={'refinedstorage_mekanism_integration','refinedstorage_curios_integration','refinedstorage_emi_integration',
 'refinedstorage_quartz_arsenal','integrateddynamicscompat','integratedterminalscompat','integratedtunnelscompat',
 'projectred_transmission','projectred_illumination','projectred_integration','createaddoncompatibility',
 'almostunified','almostunified_ie','create_cold_sweat','mi_sound_addon','industrialization_overdrive',
 'kubejs_create','kubejs_mekanism'}

content=[m for m in sorted(modids) if m not in noncontent and m not in integration and m not in HYPHEN_COVERED]
zero=[]; under=[]; ok=[]
for m in content:
    c=ns_counter.get(m,0)
    if c==0: zero.append(m)
    elif c<=5: under.append((m,c))
    else: ok.append((m,c))
print("CONTENT_MODS_TOTAL",len(content))
print("\n--- ZERO coverage (%d) ---"%len(zero))
for m in zero: print("  0\t"+m)
print("\n--- UNDER 1-5 (%d) ---"%len(under))
for m,c in sorted(under,key=lambda x:x[1]): print("  %d\t%s"%(c,m))
print("\n--- OK >5 (%d) ---"%len(ok))
for m,c in sorted(ok,key=lambda x:-x[1]): print("  %d\t%s"%(c,m))
