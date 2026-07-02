// AoA KubeJS: aoa_astages_team_grant.js
//
// FTB Quests stores completion per FTB Team, but SNBT `/astages add {p}` command
// rewards only grant the completing player. This hook mirrors every quest stage
// grant to all FTB team members (online and offline).
//
// SNBT command rewards are kept for advancement co-grants and as a fallback for
// solo players. Grants here are idempotent.
//
// Regenerate QUEST_STAGE_GRANTS after SNBT reward edits:
//   python tools/gen_quest_stage_grants_js.py
//
// AStages API (astages-2.0.4-1.21.1):
//   AStages.playerHasStage(String stage, Player player) -> boolean
//   AStages.addStageToPlayer(String stage, Player player) -> void

;(function () {
  if (typeof AStages === 'undefined') return

  const ObjectCompletedEvent = loadClassOrNull('dev.ftb.mods.ftbquests.events.ObjectCompletedEvent')
  const EventResult = loadClassOrNull('dev.architectury.event.EventResult')
  const FTBTeamsAPI = loadClassOrNull('dev.ftb.mods.ftbteams.api.FTBTeamsAPI')
  const TeamData = loadClassOrNull('dev.ftb.mods.ftbquests.quest.TeamData')
  const QuestObjectBase = loadClassOrNull('dev.ftb.mods.ftbquests.quest.QuestObjectBase')
  const ServerQuestFile = loadClassOrNull('dev.ftb.mods.ftbquests.quest.ServerQuestFile')

  if (!ObjectCompletedEvent || !EventResult || !FTBTeamsAPI || !TeamData || !QuestObjectBase) {
    console.warn('[AoA AStages Team Grant] Missing FTB Quests / Teams / Architectury classes; hook disabled')
    return
  }

  const QUEST_STAGE_GRANTS = {
    '5350010000010000': ['dark_ages'],
    '097AED7C91033D5E': ['medieval_times'],
    '0B03101000000039': ['ren_magic_foundations_complete'],
    '0B03102000000062': ['ren_nether_threshold_complete'],
    '0B03103000000031': ['ren_aether_literacy_complete'],
    '0B03104000000050': ['ren_starlight_observation_complete'],
    '0B03105000000050': ['ren_undergarden_descent_complete'],
    '0B03106000000050': ['ren_deeper_darker_otherside_complete'],
    '0B03107000000050': ['ren_archive_recordkeeping_complete'],
    '0B031080000000F2': ['ren_observation_experimentation_complete'],
    '0B03109000000060': ['ren_end_threshold_complete'],
    '0B0310A000000014': ['ren_maledictus_defeated', 'ren_maledictus_vigil_complete'],
    '0B0310A0000000F0': ['industrial_revolution', 'ren_seal_obtained'],
    '4153010000010001': ['asc_archive_of_ages_complete'],
    '4153010000010002': ['asc_capstone_complete', 'aoa_complete'],
    '425201000001000B': ['asc_final_boss_convergence_complete', 'draconic_guardian_defeated'],
    '4256010000010004': ['leviathan_defeated'],
    '4256010000010005': ['ow_beyond_the_veil_theme_complete'],
    '4256010000010006': ['ow_capstone_complete', 'ascension'],
    '4341011000000004': ['g_magic_authorization_complete'],
    '4348010000010004': ['at_nuclear_engineering_complete'],
    '4358010000010001': ['tremorzilla_defeated'],
    '4358010000010002': ['geburah_defeated'],
    '4358010000010003': ['at_capstone_complete', 'otherworldly'],
    '4443010000010006': ['ow_interdimensional_infrastructure_complete'],
    '4448010000010005': ['asc_draconic_apex_complete'],
    '4454010000010005': ['ow_draconic_technology_complete'],
    '4646010000010000': ['macabre_valamon_defeated'],
    '4646010000010001': ['macabre_gomoria_defeated'],
    '4646010000010002': ['macabre_gargamaw_defeated'],
    '4646010000010003': ['macabre_baal_defeated'],
    '4954021000000016': ['ir_factory_discipline_complete'],
    '4954051000000011': ['ir_power_motion_complete'],
    '495406100000001D': ['ir_pressure_chemistry_entry_complete'],
    '49540A100000000F': ['ir_digital_logistics_complete'],
    '49540B1000000015': ['ir_magic_feedstock_complete'],
    '49540C1000000006': ['obsidilith_defeated'],
    '4954631000000000': ['ir_capstone_complete', 'gilded_age'],
    '4C57010000010004': ['ow_launch_offworld_logistics_complete'],
    '4C58010000010005': ['ow_strange_dimension_operations_complete'],
    '4C59010000010004': ['ow_dyson_project_complete'],
    '4D4E011000000006': ['g_scaled_logistics_computation_complete'],
    '4D4F011000000005': ['g_advanced_applied_industry_complete'],
    '4D50011000000003': ['g_nautec_oceanic_industry_complete'],
    '4D53010000010003': ['at_reactor_control_complete', 'at_neural_industry_complete'],
    '4E44010000010004': ['at_radiological_materials_complete', 'at_create_nuclear_mainline_complete'],
    '4F47011000000002': ['g_atomic_license_complete'],
    '5044010000010006': ['asc_avaritia_singularity_pressure_complete'],
    '5057011000000003': ['void_titan_defeated', 'g_temporal_authorization_complete'],
    '5057011000000004': ['atomic'],
    '5246011000000007': ['g_biotech_hazard_readiness_complete'],
    '5347010000010002': ['asc_oritech_apex_complete'],
    '5449010000010006': ['asc_final_crafting_surface_complete'],
    '5457010000010003': ['at_mff_containment_complete', 'at_ballistix_policy_complete'],
    '6D7E8F901A2B1054': ['the_renaissance']
  }

  function loadClassOrNull(className) {
    try {
      return Java.loadClass(className)
    } catch (e) {
      console.warn('[AoA AStages Team Grant] Missing optional class ' + className + ': ' + e)
      return null
    }
  }

  function resolveTeamData(event) {
    try {
      var m = event.getOnlineMembers()
      if (m && m.size && m.size() > 0) return TeamData.get(m.get(0))
    } catch (e) {
      console.warn('[AoA AStages Team Grant] resolveTeamData failed: ' + e)
    }
    return null
  }

  function normalizeQuestId(rawId) {
    return String(rawId || '').trim().replace(/^#/, '').toUpperCase()
  }

  function playerName(player) {
    return String(player.username || player.name || 'unknown')
  }

  function commandTargetFromName(name) {
    var target = String(name || '')
    if (!/^[A-Za-z0-9_]{1,16}$/.test(target)) return null
    return target
  }

  function commandTarget(player) {
    return commandTargetFromName(playerName(player))
  }

  function hasStage(player, stage) {
    try {
      return AStages.playerHasStage(stage, player)
    } catch (e) {
      console.warn('[AoA AStages Team Grant] Stage check failed for ' + stage + ': ' + e)
      return false
    }
  }

  function addStageViaCommand(server, target, stage) {
    server.runCommandSilent('astages add ' + target + ' ' + stage + ' true true')
  }

  function addStageToOnlinePlayer(player, stage) {
    if (!player || hasStage(player, stage)) return false
    try {
      AStages.addStageToPlayer(stage, player)
      return true
    } catch (e) {
      console.warn('[AoA AStages Team Grant] addStageToPlayer failed for ' + stage + ': ' + e)
      return false
    }
  }

  function teamsManager(server) {
    try {
      return FTBTeamsAPI.api().getManager()
    } catch (e) {
      console.warn('[AoA AStages Team Grant] FTB Teams manager unavailable: ' + e)
      return null
    }
  }

  function teamFromTeamData(server, teamData) {
    if (!teamData || !server) return null
    var manager = teamsManager(server)
    if (!manager) return null

    try {
      var teamId = teamData.getTeamId()
      var optionalTeam = manager.getTeamByID(teamId)
      if (optionalTeam && optionalTeam.isPresent()) return optionalTeam.get()
    } catch (e) {
      console.warn('[AoA AStages Team Grant] Team lookup failed: ' + e)
    }
    return null
  }

  function teamFromPlayer(server, player) {
    if (!player || !server) return null
    var manager = teamsManager(server)
    if (!manager) return null

    try {
      var optionalTeam = manager.getTeamForPlayer(player)
      if (optionalTeam && optionalTeam.isPresent()) return optionalTeam.get()
    } catch (e) {
      console.warn('[AoA AStages Team Grant] Player team lookup failed: ' + e)
    }
    return null
  }

  function componentToPlainName(value) {
    if (!value) return null
    try {
      if (typeof value.getString === 'function') return String(value.getString())
    } catch (e) {
      // Fall through to String().
    }
    return String(value)
  }

  function resolveMemberUsername(server, manager, team, memberUuid) {
    if (!server || !memberUuid) return null

    try {
      var online = server.getPlayerList().getPlayer(memberUuid)
      if (online) return commandTarget(online)
    } catch (e) {
      // Continue to offline resolution.
    }

    if (manager) {
      try {
        var knownTeams = manager.getKnownPlayerTeams()
        if (knownTeams && typeof knownTeams.get === 'function') {
          var playerTeam = knownTeams.get(memberUuid)
          if (playerTeam && typeof playerTeam.getPlayerName === 'function') {
            var knownName = commandTargetFromName(playerTeam.getPlayerName())
            if (knownName) return knownName
          }
        }
      } catch (e) {
        // Continue to other lookups.
      }
    }

    if (team && typeof team.getPlayerName === 'function') {
      try {
        var teamName = commandTargetFromName(componentToPlainName(team.getPlayerName(memberUuid)))
        if (teamName) return teamName
      } catch (e) {
        // Continue to profile cache.
      }
    }

    try {
      var cache = server.getProfileCache()
      if (cache) {
        var profile = cache.get(memberUuid)
        if (profile && profile.isPresent()) {
          return commandTargetFromName(profile.get().getName())
        }
      }
    } catch (e) {
      console.warn('[AoA AStages Team Grant] Profile cache lookup failed: ' + e)
    }

    return null
  }

  function forEachMemberUuid(team, callback) {
    if (!team || typeof team.getMembers !== 'function') return
    var members = team.getMembers()
    if (!members || typeof members.iterator !== 'function') return

    var iterator = members.iterator()
    while (iterator.hasNext()) {
      callback(iterator.next())
    }
  }

  function dedupeStages(stages) {
    var seen = {}
    var out = []
    for (var i = 0; i < stages.length; i++) {
      var stage = stages[i]
      if (!stage || seen[stage]) continue
      seen[stage] = true
      out.push(stage)
    }
    return out
  }

  function grantStagesToOnlineMembers(server, members, stages, contextLabel) {
    if (!server || !members || !stages || stages.length === 0) return 0

    var uniqueStages = dedupeStages(stages)
    var grantedCount = 0

    for (var i = 0; i < members.size(); i++) {
      var player = members.get(i)
      if (!player) continue
      for (var j = 0; j < uniqueStages.length; j++) {
        if (addStageToOnlinePlayer(player, uniqueStages[j])) grantedCount++
      }
    }

    if (grantedCount > 0) {
      console.info('[AoA AStages Team Grant] ' + contextLabel + ' granted ' + grantedCount + ' stage(s) to online member(s)')
    }
    return grantedCount
  }

  function grantStagesToTeam(server, team, stages, contextLabel) {
    if (!server || !team || !stages || stages.length === 0) return

    var manager = teamsManager(server)
    var uniqueStages = dedupeStages(stages)
    var grantedCount = 0

    forEachMemberUuid(team, function (memberUuid) {
      var username = resolveMemberUsername(server, manager, team, memberUuid)
      if (!username) {
        console.warn('[AoA AStages Team Grant] Could not resolve username for member ' + memberUuid + ' (' + contextLabel + ')')
        return
      }

      var online = server.getPlayerList().getPlayer(memberUuid)
      for (var i = 0; i < uniqueStages.length; i++) {
        var stage = uniqueStages[i]
        if (online) {
          if (addStageToOnlinePlayer(online, stage)) grantedCount++
        } else {
          // Offline grants use the AStages command so username-targeted data persists.
          addStageViaCommand(server, username, stage)
          grantedCount++
        }
      }
    })

    if (grantedCount > 0) {
      console.info('[AoA AStages Team Grant] ' + contextLabel + ' granted ' + grantedCount + ' stage(s) to team members')
    }
  }

  function parseQuestId(questId) {
    try {
      return QuestObjectBase.parseCodeString(questId)
    } catch (e) {
      console.warn('[AoA AStages Team Grant] Invalid quest id ' + questId + ': ' + e)
      return null
    }
  }

  function isTeamQuestComplete(teamData, questId) {
    if (!teamData) return false

    var parsedId = parseQuestId(questId)
    if (parsedId === null || parsedId === undefined) return false

    try {
      var completedTime = teamData.getCompletedTime(parsedId)
      if (completedTime && typeof completedTime.isPresent === 'function' && completedTime.isPresent()) {
        return true
      }

      if (ServerQuestFile && ServerQuestFile.INSTANCE) {
        var quest = ServerQuestFile.INSTANCE.getQuest(parsedId)
        if (quest) return teamData.isCompleted(quest)
      }
    } catch (e) {
      console.warn('[AoA AStages Team Grant] Quest completion check failed for ' + questId + ': ' + e)
    }

    return false
  }

  function stagesForQuest(questId) {
    return QUEST_STAGE_GRANTS[normalizeQuestId(questId)] || null
  }

  function resolveServerFromQuestEvent(event) {
    var onlineMembers = event.getOnlineMembers()
    if (onlineMembers && onlineMembers.size && onlineMembers.size() > 0) {
      return onlineMembers.get(0).getServer()
    }

    var teamData = resolveTeamData(event)
    if (teamData) {
      var fallbackOnline = teamData.getOnlineMembers()
      if (fallbackOnline && fallbackOnline.size && fallbackOnline.size() > 0) {
        return fallbackOnline.get(0).getServer()
      }
    }

    return null
  }

  ObjectCompletedEvent.QUEST.register(function (event) {
    try {
      var quest = event.getObject()
      if (!quest) return EventResult.pass()

      var questId = normalizeQuestId(quest.getCodeString ? quest.getCodeString() : quest.getId())
      var stages = stagesForQuest(questId)
      if (!stages) return EventResult.pass()

      var server = resolveServerFromQuestEvent(event)
      var team = teamFromTeamData(server, resolveTeamData(event))
      var onlineMembers = event.getOnlineMembers()

      if (server && team) {
        grantStagesToTeam(server, team, stages, 'quest ' + questId)
      } else if (server && onlineMembers && onlineMembers.size && onlineMembers.size() > 0) {
        grantStagesToOnlineMembers(server, onlineMembers, stages, 'quest ' + questId + ' (online fallback)')
      } else {
        console.warn('[AoA AStages Team Grant] Quest ' + questId + ' completed but team/server could not be resolved')
      }

    } catch (e) {
      console.warn('[AoA AStages Team Grant] Quest completion hook failed: ' + e)
    }

    return EventResult.pass()
  })

  function reconcilePlayerTeamStages(event) {
    var player = event.player
    var server = event.server
    if (!player || !server) return

    var teamData = TeamData.get(player)
    if (!teamData) return

    var missingStages = []
    for (var questId in QUEST_STAGE_GRANTS) {
      if (!Object.prototype.hasOwnProperty.call(QUEST_STAGE_GRANTS, questId)) continue
      if (!isTeamQuestComplete(teamData, questId)) continue

      var stages = QUEST_STAGE_GRANTS[questId]
      for (var i = 0; i < stages.length; i++) {
        var stage = stages[i]
        if (!hasStage(player, stage)) missingStages.push(stage)
      }
    }

    var uniqueMissing = dedupeStages(missingStages)
    if (uniqueMissing.length === 0) return

    var target = commandTarget(player)
    if (!target) {
      console.warn('[AoA AStages Team Grant] Login reconcile skipped for unsafe command target')
      return
    }

    for (var j = 0; j < uniqueMissing.length; j++) {
      var missingStage = uniqueMissing[j]
      if (addStageToOnlinePlayer(player, missingStage)) continue
      addStageViaCommand(server, target, missingStage)
    }

    console.info('[AoA AStages Team Grant] Login reconcile for ' + target + ' granted ' + uniqueMissing.join(', '))
  }

  PlayerEvents.loggedIn(reconcilePlayerTeamStages)

  console.info('[AoA AStages Team Grant] Hook registered for ' + Object.keys(QUEST_STAGE_GRANTS).length + ' quest grant(s)')
})()
