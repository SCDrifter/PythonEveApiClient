# coding: utf-8

# flake8: noqa
"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.8.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from eve_api.models.bad_request import BadRequest
from eve_api.models.delete_characters_character_id_mail_labels_label_id_unprocessable_entity import DeleteCharactersCharacterIdMailLabelsLabelIdUnprocessableEntity
from eve_api.models.delete_fleets_fleet_id_members_member_id_not_found import DeleteFleetsFleetIdMembersMemberIdNotFound
from eve_api.models.delete_fleets_fleet_id_squads_squad_id_not_found import DeleteFleetsFleetIdSquadsSquadIdNotFound
from eve_api.models.delete_fleets_fleet_id_wings_wing_id_not_found import DeleteFleetsFleetIdWingsWingIdNotFound
from eve_api.models.error_limited import ErrorLimited
from eve_api.models.forbidden import Forbidden
from eve_api.models.gateway_timeout import GatewayTimeout
from eve_api.models.get_alliances_alliance_id_contacts200_ok import GetAlliancesAllianceIdContacts200Ok
from eve_api.models.get_alliances_alliance_id_contacts_labels200_ok import GetAlliancesAllianceIdContactsLabels200Ok
from eve_api.models.get_alliances_alliance_id_icons_not_found import GetAlliancesAllianceIdIconsNotFound
from eve_api.models.get_alliances_alliance_id_icons_ok import GetAlliancesAllianceIdIconsOk
from eve_api.models.get_alliances_alliance_id_not_found import GetAlliancesAllianceIdNotFound
from eve_api.models.get_alliances_alliance_id_ok import GetAlliancesAllianceIdOk
from eve_api.models.get_characters_character_id_agents_research200_ok import GetCharactersCharacterIdAgentsResearch200Ok
from eve_api.models.get_characters_character_id_assets200_ok import GetCharactersCharacterIdAssets200Ok
from eve_api.models.get_characters_character_id_assets_not_found import GetCharactersCharacterIdAssetsNotFound
from eve_api.models.get_characters_character_id_attributes_ok import GetCharactersCharacterIdAttributesOk
from eve_api.models.get_characters_character_id_blueprints200_ok import GetCharactersCharacterIdBlueprints200Ok
from eve_api.models.get_characters_character_id_bookmarks200_ok import GetCharactersCharacterIdBookmarks200Ok
from eve_api.models.get_characters_character_id_bookmarks_coordinates import GetCharactersCharacterIdBookmarksCoordinates
from eve_api.models.get_characters_character_id_bookmarks_folders200_ok import GetCharactersCharacterIdBookmarksFolders200Ok
from eve_api.models.get_characters_character_id_bookmarks_item import GetCharactersCharacterIdBookmarksItem
from eve_api.models.get_characters_character_id_calendar200_ok import GetCharactersCharacterIdCalendar200Ok
from eve_api.models.get_characters_character_id_calendar_event_id_attendees200_ok import GetCharactersCharacterIdCalendarEventIdAttendees200Ok
from eve_api.models.get_characters_character_id_calendar_event_id_attendees_not_found import GetCharactersCharacterIdCalendarEventIdAttendeesNotFound
from eve_api.models.get_characters_character_id_calendar_event_id_not_found import GetCharactersCharacterIdCalendarEventIdNotFound
from eve_api.models.get_characters_character_id_calendar_event_id_ok import GetCharactersCharacterIdCalendarEventIdOk
from eve_api.models.get_characters_character_id_clones_home_location import GetCharactersCharacterIdClonesHomeLocation
from eve_api.models.get_characters_character_id_clones_jump_clone import GetCharactersCharacterIdClonesJumpClone
from eve_api.models.get_characters_character_id_clones_ok import GetCharactersCharacterIdClonesOk
from eve_api.models.get_characters_character_id_contacts200_ok import GetCharactersCharacterIdContacts200Ok
from eve_api.models.get_characters_character_id_contacts_labels200_ok import GetCharactersCharacterIdContactsLabels200Ok
from eve_api.models.get_characters_character_id_contracts200_ok import GetCharactersCharacterIdContracts200Ok
from eve_api.models.get_characters_character_id_contracts_contract_id_bids200_ok import GetCharactersCharacterIdContractsContractIdBids200Ok
from eve_api.models.get_characters_character_id_contracts_contract_id_bids_not_found import GetCharactersCharacterIdContractsContractIdBidsNotFound
from eve_api.models.get_characters_character_id_contracts_contract_id_items200_ok import GetCharactersCharacterIdContractsContractIdItems200Ok
from eve_api.models.get_characters_character_id_contracts_contract_id_items_not_found import GetCharactersCharacterIdContractsContractIdItemsNotFound
from eve_api.models.get_characters_character_id_corporationhistory200_ok import GetCharactersCharacterIdCorporationhistory200Ok
from eve_api.models.get_characters_character_id_fatigue_ok import GetCharactersCharacterIdFatigueOk
from eve_api.models.get_characters_character_id_fittings200_ok import GetCharactersCharacterIdFittings200Ok
from eve_api.models.get_characters_character_id_fittings_item import GetCharactersCharacterIdFittingsItem
from eve_api.models.get_characters_character_id_fleet_not_found import GetCharactersCharacterIdFleetNotFound
from eve_api.models.get_characters_character_id_fleet_ok import GetCharactersCharacterIdFleetOk
from eve_api.models.get_characters_character_id_fw_stats_kills import GetCharactersCharacterIdFwStatsKills
from eve_api.models.get_characters_character_id_fw_stats_ok import GetCharactersCharacterIdFwStatsOk
from eve_api.models.get_characters_character_id_fw_stats_victory_points import GetCharactersCharacterIdFwStatsVictoryPoints
from eve_api.models.get_characters_character_id_industry_jobs200_ok import GetCharactersCharacterIdIndustryJobs200Ok
from eve_api.models.get_characters_character_id_killmails_recent200_ok import GetCharactersCharacterIdKillmailsRecent200Ok
from eve_api.models.get_characters_character_id_location_ok import GetCharactersCharacterIdLocationOk
from eve_api.models.get_characters_character_id_loyalty_points200_ok import GetCharactersCharacterIdLoyaltyPoints200Ok
from eve_api.models.get_characters_character_id_mail200_ok import GetCharactersCharacterIdMail200Ok
from eve_api.models.get_characters_character_id_mail_labels_label import GetCharactersCharacterIdMailLabelsLabel
from eve_api.models.get_characters_character_id_mail_labels_ok import GetCharactersCharacterIdMailLabelsOk
from eve_api.models.get_characters_character_id_mail_lists200_ok import GetCharactersCharacterIdMailLists200Ok
from eve_api.models.get_characters_character_id_mail_mail_id_not_found import GetCharactersCharacterIdMailMailIdNotFound
from eve_api.models.get_characters_character_id_mail_mail_id_ok import GetCharactersCharacterIdMailMailIdOk
from eve_api.models.get_characters_character_id_mail_mail_id_recipient import GetCharactersCharacterIdMailMailIdRecipient
from eve_api.models.get_characters_character_id_mail_recipient import GetCharactersCharacterIdMailRecipient
from eve_api.models.get_characters_character_id_medals200_ok import GetCharactersCharacterIdMedals200Ok
from eve_api.models.get_characters_character_id_medals_graphic import GetCharactersCharacterIdMedalsGraphic
from eve_api.models.get_characters_character_id_mining200_ok import GetCharactersCharacterIdMining200Ok
from eve_api.models.get_characters_character_id_not_found import GetCharactersCharacterIdNotFound
from eve_api.models.get_characters_character_id_notifications200_ok import GetCharactersCharacterIdNotifications200Ok
from eve_api.models.get_characters_character_id_notifications_contacts200_ok import GetCharactersCharacterIdNotificationsContacts200Ok
from eve_api.models.get_characters_character_id_ok import GetCharactersCharacterIdOk
from eve_api.models.get_characters_character_id_online_ok import GetCharactersCharacterIdOnlineOk
from eve_api.models.get_characters_character_id_opportunities200_ok import GetCharactersCharacterIdOpportunities200Ok
from eve_api.models.get_characters_character_id_orders200_ok import GetCharactersCharacterIdOrders200Ok
from eve_api.models.get_characters_character_id_orders_history200_ok import GetCharactersCharacterIdOrdersHistory200Ok
from eve_api.models.get_characters_character_id_planets200_ok import GetCharactersCharacterIdPlanets200Ok
from eve_api.models.get_characters_character_id_planets_planet_id_content import GetCharactersCharacterIdPlanetsPlanetIdContent
from eve_api.models.get_characters_character_id_planets_planet_id_extractor_details import GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails
from eve_api.models.get_characters_character_id_planets_planet_id_factory_details import GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails
from eve_api.models.get_characters_character_id_planets_planet_id_head import GetCharactersCharacterIdPlanetsPlanetIdHead
from eve_api.models.get_characters_character_id_planets_planet_id_link import GetCharactersCharacterIdPlanetsPlanetIdLink
from eve_api.models.get_characters_character_id_planets_planet_id_not_found import GetCharactersCharacterIdPlanetsPlanetIdNotFound
from eve_api.models.get_characters_character_id_planets_planet_id_ok import GetCharactersCharacterIdPlanetsPlanetIdOk
from eve_api.models.get_characters_character_id_planets_planet_id_pin import GetCharactersCharacterIdPlanetsPlanetIdPin
from eve_api.models.get_characters_character_id_planets_planet_id_route import GetCharactersCharacterIdPlanetsPlanetIdRoute
from eve_api.models.get_characters_character_id_portrait_not_found import GetCharactersCharacterIdPortraitNotFound
from eve_api.models.get_characters_character_id_portrait_ok import GetCharactersCharacterIdPortraitOk
from eve_api.models.get_characters_character_id_roles_ok import GetCharactersCharacterIdRolesOk
from eve_api.models.get_characters_character_id_search_ok import GetCharactersCharacterIdSearchOk
from eve_api.models.get_characters_character_id_ship_ok import GetCharactersCharacterIdShipOk
from eve_api.models.get_characters_character_id_skillqueue200_ok import GetCharactersCharacterIdSkillqueue200Ok
from eve_api.models.get_characters_character_id_skills_ok import GetCharactersCharacterIdSkillsOk
from eve_api.models.get_characters_character_id_skills_skill import GetCharactersCharacterIdSkillsSkill
from eve_api.models.get_characters_character_id_standings200_ok import GetCharactersCharacterIdStandings200Ok
from eve_api.models.get_characters_character_id_titles200_ok import GetCharactersCharacterIdTitles200Ok
from eve_api.models.get_characters_character_id_wallet_journal200_ok import GetCharactersCharacterIdWalletJournal200Ok
from eve_api.models.get_characters_character_id_wallet_transactions200_ok import GetCharactersCharacterIdWalletTransactions200Ok
from eve_api.models.get_contracts_public_bids_contract_id200_ok import GetContractsPublicBidsContractId200Ok
from eve_api.models.get_contracts_public_bids_contract_id_forbidden import GetContractsPublicBidsContractIdForbidden
from eve_api.models.get_contracts_public_bids_contract_id_not_found import GetContractsPublicBidsContractIdNotFound
from eve_api.models.get_contracts_public_items_contract_id200_ok import GetContractsPublicItemsContractId200Ok
from eve_api.models.get_contracts_public_items_contract_id_forbidden import GetContractsPublicItemsContractIdForbidden
from eve_api.models.get_contracts_public_items_contract_id_not_found import GetContractsPublicItemsContractIdNotFound
from eve_api.models.get_contracts_public_region_id200_ok import GetContractsPublicRegionId200Ok
from eve_api.models.get_contracts_public_region_id_not_found import GetContractsPublicRegionIdNotFound
from eve_api.models.get_corporation_corporation_id_mining_extractions200_ok import GetCorporationCorporationIdMiningExtractions200Ok
from eve_api.models.get_corporation_corporation_id_mining_observers200_ok import GetCorporationCorporationIdMiningObservers200Ok
from eve_api.models.get_corporation_corporation_id_mining_observers_observer_id200_ok import GetCorporationCorporationIdMiningObserversObserverId200Ok
from eve_api.models.get_corporations_corporation_id_alliancehistory200_ok import GetCorporationsCorporationIdAlliancehistory200Ok
from eve_api.models.get_corporations_corporation_id_assets200_ok import GetCorporationsCorporationIdAssets200Ok
from eve_api.models.get_corporations_corporation_id_blueprints200_ok import GetCorporationsCorporationIdBlueprints200Ok
from eve_api.models.get_corporations_corporation_id_bookmarks200_ok import GetCorporationsCorporationIdBookmarks200Ok
from eve_api.models.get_corporations_corporation_id_bookmarks_coordinates import GetCorporationsCorporationIdBookmarksCoordinates
from eve_api.models.get_corporations_corporation_id_bookmarks_folders200_ok import GetCorporationsCorporationIdBookmarksFolders200Ok
from eve_api.models.get_corporations_corporation_id_bookmarks_item import GetCorporationsCorporationIdBookmarksItem
from eve_api.models.get_corporations_corporation_id_contacts200_ok import GetCorporationsCorporationIdContacts200Ok
from eve_api.models.get_corporations_corporation_id_contacts_labels200_ok import GetCorporationsCorporationIdContactsLabels200Ok
from eve_api.models.get_corporations_corporation_id_containers_logs200_ok import GetCorporationsCorporationIdContainersLogs200Ok
from eve_api.models.get_corporations_corporation_id_contracts200_ok import GetCorporationsCorporationIdContracts200Ok
from eve_api.models.get_corporations_corporation_id_contracts_contract_id_bids200_ok import GetCorporationsCorporationIdContractsContractIdBids200Ok
from eve_api.models.get_corporations_corporation_id_contracts_contract_id_bids_not_found import GetCorporationsCorporationIdContractsContractIdBidsNotFound
from eve_api.models.get_corporations_corporation_id_contracts_contract_id_items200_ok import GetCorporationsCorporationIdContractsContractIdItems200Ok
from eve_api.models.get_corporations_corporation_id_contracts_contract_id_items_error520 import GetCorporationsCorporationIdContractsContractIdItemsError520
from eve_api.models.get_corporations_corporation_id_contracts_contract_id_items_not_found import GetCorporationsCorporationIdContractsContractIdItemsNotFound
from eve_api.models.get_corporations_corporation_id_customs_offices200_ok import GetCorporationsCorporationIdCustomsOffices200Ok
from eve_api.models.get_corporations_corporation_id_divisions_hangar_hangar import GetCorporationsCorporationIdDivisionsHangarHangar
from eve_api.models.get_corporations_corporation_id_divisions_ok import GetCorporationsCorporationIdDivisionsOk
from eve_api.models.get_corporations_corporation_id_divisions_wallet_wallet import GetCorporationsCorporationIdDivisionsWalletWallet
from eve_api.models.get_corporations_corporation_id_facilities200_ok import GetCorporationsCorporationIdFacilities200Ok
from eve_api.models.get_corporations_corporation_id_fw_stats_kills import GetCorporationsCorporationIdFwStatsKills
from eve_api.models.get_corporations_corporation_id_fw_stats_ok import GetCorporationsCorporationIdFwStatsOk
from eve_api.models.get_corporations_corporation_id_fw_stats_victory_points import GetCorporationsCorporationIdFwStatsVictoryPoints
from eve_api.models.get_corporations_corporation_id_icons_not_found import GetCorporationsCorporationIdIconsNotFound
from eve_api.models.get_corporations_corporation_id_icons_ok import GetCorporationsCorporationIdIconsOk
from eve_api.models.get_corporations_corporation_id_industry_jobs200_ok import GetCorporationsCorporationIdIndustryJobs200Ok
from eve_api.models.get_corporations_corporation_id_killmails_recent200_ok import GetCorporationsCorporationIdKillmailsRecent200Ok
from eve_api.models.get_corporations_corporation_id_medals200_ok import GetCorporationsCorporationIdMedals200Ok
from eve_api.models.get_corporations_corporation_id_medals_issued200_ok import GetCorporationsCorporationIdMedalsIssued200Ok
from eve_api.models.get_corporations_corporation_id_members_titles200_ok import GetCorporationsCorporationIdMembersTitles200Ok
from eve_api.models.get_corporations_corporation_id_membertracking200_ok import GetCorporationsCorporationIdMembertracking200Ok
from eve_api.models.get_corporations_corporation_id_not_found import GetCorporationsCorporationIdNotFound
from eve_api.models.get_corporations_corporation_id_ok import GetCorporationsCorporationIdOk
from eve_api.models.get_corporations_corporation_id_orders200_ok import GetCorporationsCorporationIdOrders200Ok
from eve_api.models.get_corporations_corporation_id_orders_history200_ok import GetCorporationsCorporationIdOrdersHistory200Ok
from eve_api.models.get_corporations_corporation_id_roles200_ok import GetCorporationsCorporationIdRoles200Ok
from eve_api.models.get_corporations_corporation_id_roles_history200_ok import GetCorporationsCorporationIdRolesHistory200Ok
from eve_api.models.get_corporations_corporation_id_shareholders200_ok import GetCorporationsCorporationIdShareholders200Ok
from eve_api.models.get_corporations_corporation_id_standings200_ok import GetCorporationsCorporationIdStandings200Ok
from eve_api.models.get_corporations_corporation_id_starbases200_ok import GetCorporationsCorporationIdStarbases200Ok
from eve_api.models.get_corporations_corporation_id_starbases_starbase_id_fuel import GetCorporationsCorporationIdStarbasesStarbaseIdFuel
from eve_api.models.get_corporations_corporation_id_starbases_starbase_id_ok import GetCorporationsCorporationIdStarbasesStarbaseIdOk
from eve_api.models.get_corporations_corporation_id_structures200_ok import GetCorporationsCorporationIdStructures200Ok
from eve_api.models.get_corporations_corporation_id_structures_service import GetCorporationsCorporationIdStructuresService
from eve_api.models.get_corporations_corporation_id_titles200_ok import GetCorporationsCorporationIdTitles200Ok
from eve_api.models.get_corporations_corporation_id_wallets200_ok import GetCorporationsCorporationIdWallets200Ok
from eve_api.models.get_corporations_corporation_id_wallets_division_journal200_ok import GetCorporationsCorporationIdWalletsDivisionJournal200Ok
from eve_api.models.get_corporations_corporation_id_wallets_division_transactions200_ok import GetCorporationsCorporationIdWalletsDivisionTransactions200Ok
from eve_api.models.get_dogma_attributes_attribute_id_not_found import GetDogmaAttributesAttributeIdNotFound
from eve_api.models.get_dogma_attributes_attribute_id_ok import GetDogmaAttributesAttributeIdOk
from eve_api.models.get_dogma_dynamic_items_type_id_item_id_dogma_attribute import GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute
from eve_api.models.get_dogma_dynamic_items_type_id_item_id_dogma_effect import GetDogmaDynamicItemsTypeIdItemIdDogmaEffect
from eve_api.models.get_dogma_dynamic_items_type_id_item_id_not_found import GetDogmaDynamicItemsTypeIdItemIdNotFound
from eve_api.models.get_dogma_dynamic_items_type_id_item_id_ok import GetDogmaDynamicItemsTypeIdItemIdOk
from eve_api.models.get_dogma_effects_effect_id_modifier import GetDogmaEffectsEffectIdModifier
from eve_api.models.get_dogma_effects_effect_id_not_found import GetDogmaEffectsEffectIdNotFound
from eve_api.models.get_dogma_effects_effect_id_ok import GetDogmaEffectsEffectIdOk
from eve_api.models.get_fleets_fleet_id_members200_ok import GetFleetsFleetIdMembers200Ok
from eve_api.models.get_fleets_fleet_id_members_not_found import GetFleetsFleetIdMembersNotFound
from eve_api.models.get_fleets_fleet_id_not_found import GetFleetsFleetIdNotFound
from eve_api.models.get_fleets_fleet_id_ok import GetFleetsFleetIdOk
from eve_api.models.get_fleets_fleet_id_wings200_ok import GetFleetsFleetIdWings200Ok
from eve_api.models.get_fleets_fleet_id_wings_not_found import GetFleetsFleetIdWingsNotFound
from eve_api.models.get_fleets_fleet_id_wings_squad import GetFleetsFleetIdWingsSquad
from eve_api.models.get_fw_leaderboards_active_total_active_total import GetFwLeaderboardsActiveTotalActiveTotal
from eve_api.models.get_fw_leaderboards_active_total_active_total1 import GetFwLeaderboardsActiveTotalActiveTotal1
from eve_api.models.get_fw_leaderboards_characters_active_total_active_total import GetFwLeaderboardsCharactersActiveTotalActiveTotal
from eve_api.models.get_fw_leaderboards_characters_active_total_active_total1 import GetFwLeaderboardsCharactersActiveTotalActiveTotal1
from eve_api.models.get_fw_leaderboards_characters_kills import GetFwLeaderboardsCharactersKills
from eve_api.models.get_fw_leaderboards_characters_last_week_last_week import GetFwLeaderboardsCharactersLastWeekLastWeek
from eve_api.models.get_fw_leaderboards_characters_last_week_last_week1 import GetFwLeaderboardsCharactersLastWeekLastWeek1
from eve_api.models.get_fw_leaderboards_characters_ok import GetFwLeaderboardsCharactersOk
from eve_api.models.get_fw_leaderboards_characters_victory_points import GetFwLeaderboardsCharactersVictoryPoints
from eve_api.models.get_fw_leaderboards_characters_yesterday_yesterday import GetFwLeaderboardsCharactersYesterdayYesterday
from eve_api.models.get_fw_leaderboards_characters_yesterday_yesterday1 import GetFwLeaderboardsCharactersYesterdayYesterday1
from eve_api.models.get_fw_leaderboards_corporations_active_total_active_total import GetFwLeaderboardsCorporationsActiveTotalActiveTotal
from eve_api.models.get_fw_leaderboards_corporations_active_total_active_total1 import GetFwLeaderboardsCorporationsActiveTotalActiveTotal1
from eve_api.models.get_fw_leaderboards_corporations_kills import GetFwLeaderboardsCorporationsKills
from eve_api.models.get_fw_leaderboards_corporations_last_week_last_week import GetFwLeaderboardsCorporationsLastWeekLastWeek
from eve_api.models.get_fw_leaderboards_corporations_last_week_last_week1 import GetFwLeaderboardsCorporationsLastWeekLastWeek1
from eve_api.models.get_fw_leaderboards_corporations_ok import GetFwLeaderboardsCorporationsOk
from eve_api.models.get_fw_leaderboards_corporations_victory_points import GetFwLeaderboardsCorporationsVictoryPoints
from eve_api.models.get_fw_leaderboards_corporations_yesterday_yesterday import GetFwLeaderboardsCorporationsYesterdayYesterday
from eve_api.models.get_fw_leaderboards_corporations_yesterday_yesterday1 import GetFwLeaderboardsCorporationsYesterdayYesterday1
from eve_api.models.get_fw_leaderboards_kills import GetFwLeaderboardsKills
from eve_api.models.get_fw_leaderboards_last_week_last_week import GetFwLeaderboardsLastWeekLastWeek
from eve_api.models.get_fw_leaderboards_last_week_last_week1 import GetFwLeaderboardsLastWeekLastWeek1
from eve_api.models.get_fw_leaderboards_ok import GetFwLeaderboardsOk
from eve_api.models.get_fw_leaderboards_victory_points import GetFwLeaderboardsVictoryPoints
from eve_api.models.get_fw_leaderboards_yesterday_yesterday import GetFwLeaderboardsYesterdayYesterday
from eve_api.models.get_fw_leaderboards_yesterday_yesterday1 import GetFwLeaderboardsYesterdayYesterday1
from eve_api.models.get_fw_stats200_ok import GetFwStats200Ok
from eve_api.models.get_fw_stats_kills import GetFwStatsKills
from eve_api.models.get_fw_stats_victory_points import GetFwStatsVictoryPoints
from eve_api.models.get_fw_systems200_ok import GetFwSystems200Ok
from eve_api.models.get_fw_wars200_ok import GetFwWars200Ok
from eve_api.models.get_incursions200_ok import GetIncursions200Ok
from eve_api.models.get_industry_facilities200_ok import GetIndustryFacilities200Ok
from eve_api.models.get_industry_systems200_ok import GetIndustrySystems200Ok
from eve_api.models.get_industry_systems_cost_indice import GetIndustrySystemsCostIndice
from eve_api.models.get_insurance_prices200_ok import GetInsurancePrices200Ok
from eve_api.models.get_insurance_prices_level import GetInsurancePricesLevel
from eve_api.models.get_killmails_killmail_id_killmail_hash_attacker import GetKillmailsKillmailIdKillmailHashAttacker
from eve_api.models.get_killmails_killmail_id_killmail_hash_item import GetKillmailsKillmailIdKillmailHashItem
from eve_api.models.get_killmails_killmail_id_killmail_hash_items_item import GetKillmailsKillmailIdKillmailHashItemsItem
from eve_api.models.get_killmails_killmail_id_killmail_hash_ok import GetKillmailsKillmailIdKillmailHashOk
from eve_api.models.get_killmails_killmail_id_killmail_hash_position import GetKillmailsKillmailIdKillmailHashPosition
from eve_api.models.get_killmails_killmail_id_killmail_hash_unprocessable_entity import GetKillmailsKillmailIdKillmailHashUnprocessableEntity
from eve_api.models.get_killmails_killmail_id_killmail_hash_victim import GetKillmailsKillmailIdKillmailHashVictim
from eve_api.models.get_loyalty_stores_corporation_id_offers200_ok import GetLoyaltyStoresCorporationIdOffers200Ok
from eve_api.models.get_loyalty_stores_corporation_id_offers_not_found import GetLoyaltyStoresCorporationIdOffersNotFound
from eve_api.models.get_loyalty_stores_corporation_id_offers_required_item import GetLoyaltyStoresCorporationIdOffersRequiredItem
from eve_api.models.get_markets_groups_market_group_id_not_found import GetMarketsGroupsMarketGroupIdNotFound
from eve_api.models.get_markets_groups_market_group_id_ok import GetMarketsGroupsMarketGroupIdOk
from eve_api.models.get_markets_prices200_ok import GetMarketsPrices200Ok
from eve_api.models.get_markets_region_id_history200_ok import GetMarketsRegionIdHistory200Ok
from eve_api.models.get_markets_region_id_history_error520 import GetMarketsRegionIdHistoryError520
from eve_api.models.get_markets_region_id_history_not_found import GetMarketsRegionIdHistoryNotFound
from eve_api.models.get_markets_region_id_history_unprocessable_entity import GetMarketsRegionIdHistoryUnprocessableEntity
from eve_api.models.get_markets_region_id_orders200_ok import GetMarketsRegionIdOrders200Ok
from eve_api.models.get_markets_region_id_orders_not_found import GetMarketsRegionIdOrdersNotFound
from eve_api.models.get_markets_region_id_orders_unprocessable_entity import GetMarketsRegionIdOrdersUnprocessableEntity
from eve_api.models.get_markets_structures_structure_id200_ok import GetMarketsStructuresStructureId200Ok
from eve_api.models.get_opportunities_groups_group_id_ok import GetOpportunitiesGroupsGroupIdOk
from eve_api.models.get_opportunities_tasks_task_id_ok import GetOpportunitiesTasksTaskIdOk
from eve_api.models.get_route_origin_destination_not_found import GetRouteOriginDestinationNotFound
from eve_api.models.get_search_ok import GetSearchOk
from eve_api.models.get_sovereignty_campaigns200_ok import GetSovereigntyCampaigns200Ok
from eve_api.models.get_sovereignty_campaigns_participant import GetSovereigntyCampaignsParticipant
from eve_api.models.get_sovereignty_map200_ok import GetSovereigntyMap200Ok
from eve_api.models.get_sovereignty_structures200_ok import GetSovereigntyStructures200Ok
from eve_api.models.get_status_ok import GetStatusOk
from eve_api.models.get_universe_ancestries200_ok import GetUniverseAncestries200Ok
from eve_api.models.get_universe_asteroid_belts_asteroid_belt_id_not_found import GetUniverseAsteroidBeltsAsteroidBeltIdNotFound
from eve_api.models.get_universe_asteroid_belts_asteroid_belt_id_ok import GetUniverseAsteroidBeltsAsteroidBeltIdOk
from eve_api.models.get_universe_asteroid_belts_asteroid_belt_id_position import GetUniverseAsteroidBeltsAsteroidBeltIdPosition
from eve_api.models.get_universe_bloodlines200_ok import GetUniverseBloodlines200Ok
from eve_api.models.get_universe_categories_category_id_not_found import GetUniverseCategoriesCategoryIdNotFound
from eve_api.models.get_universe_categories_category_id_ok import GetUniverseCategoriesCategoryIdOk
from eve_api.models.get_universe_constellations_constellation_id_not_found import GetUniverseConstellationsConstellationIdNotFound
from eve_api.models.get_universe_constellations_constellation_id_ok import GetUniverseConstellationsConstellationIdOk
from eve_api.models.get_universe_constellations_constellation_id_position import GetUniverseConstellationsConstellationIdPosition
from eve_api.models.get_universe_factions200_ok import GetUniverseFactions200Ok
from eve_api.models.get_universe_graphics_graphic_id_not_found import GetUniverseGraphicsGraphicIdNotFound
from eve_api.models.get_universe_graphics_graphic_id_ok import GetUniverseGraphicsGraphicIdOk
from eve_api.models.get_universe_groups_group_id_not_found import GetUniverseGroupsGroupIdNotFound
from eve_api.models.get_universe_groups_group_id_ok import GetUniverseGroupsGroupIdOk
from eve_api.models.get_universe_moons_moon_id_not_found import GetUniverseMoonsMoonIdNotFound
from eve_api.models.get_universe_moons_moon_id_ok import GetUniverseMoonsMoonIdOk
from eve_api.models.get_universe_moons_moon_id_position import GetUniverseMoonsMoonIdPosition
from eve_api.models.get_universe_planets_planet_id_not_found import GetUniversePlanetsPlanetIdNotFound
from eve_api.models.get_universe_planets_planet_id_ok import GetUniversePlanetsPlanetIdOk
from eve_api.models.get_universe_planets_planet_id_position import GetUniversePlanetsPlanetIdPosition
from eve_api.models.get_universe_races200_ok import GetUniverseRaces200Ok
from eve_api.models.get_universe_regions_region_id_not_found import GetUniverseRegionsRegionIdNotFound
from eve_api.models.get_universe_regions_region_id_ok import GetUniverseRegionsRegionIdOk
from eve_api.models.get_universe_schematics_schematic_id_not_found import GetUniverseSchematicsSchematicIdNotFound
from eve_api.models.get_universe_schematics_schematic_id_ok import GetUniverseSchematicsSchematicIdOk
from eve_api.models.get_universe_stargates_stargate_id_destination import GetUniverseStargatesStargateIdDestination
from eve_api.models.get_universe_stargates_stargate_id_not_found import GetUniverseStargatesStargateIdNotFound
from eve_api.models.get_universe_stargates_stargate_id_ok import GetUniverseStargatesStargateIdOk
from eve_api.models.get_universe_stargates_stargate_id_position import GetUniverseStargatesStargateIdPosition
from eve_api.models.get_universe_stars_star_id_ok import GetUniverseStarsStarIdOk
from eve_api.models.get_universe_stations_station_id_not_found import GetUniverseStationsStationIdNotFound
from eve_api.models.get_universe_stations_station_id_ok import GetUniverseStationsStationIdOk
from eve_api.models.get_universe_stations_station_id_position import GetUniverseStationsStationIdPosition
from eve_api.models.get_universe_structures_structure_id_not_found import GetUniverseStructuresStructureIdNotFound
from eve_api.models.get_universe_structures_structure_id_ok import GetUniverseStructuresStructureIdOk
from eve_api.models.get_universe_structures_structure_id_position import GetUniverseStructuresStructureIdPosition
from eve_api.models.get_universe_system_jumps200_ok import GetUniverseSystemJumps200Ok
from eve_api.models.get_universe_system_kills200_ok import GetUniverseSystemKills200Ok
from eve_api.models.get_universe_systems_system_id_not_found import GetUniverseSystemsSystemIdNotFound
from eve_api.models.get_universe_systems_system_id_ok import GetUniverseSystemsSystemIdOk
from eve_api.models.get_universe_systems_system_id_planet import GetUniverseSystemsSystemIdPlanet
from eve_api.models.get_universe_systems_system_id_position import GetUniverseSystemsSystemIdPosition
from eve_api.models.get_universe_types_type_id_dogma_attribute import GetUniverseTypesTypeIdDogmaAttribute
from eve_api.models.get_universe_types_type_id_dogma_effect import GetUniverseTypesTypeIdDogmaEffect
from eve_api.models.get_universe_types_type_id_not_found import GetUniverseTypesTypeIdNotFound
from eve_api.models.get_universe_types_type_id_ok import GetUniverseTypesTypeIdOk
from eve_api.models.get_wars_war_id_aggressor import GetWarsWarIdAggressor
from eve_api.models.get_wars_war_id_ally import GetWarsWarIdAlly
from eve_api.models.get_wars_war_id_defender import GetWarsWarIdDefender
from eve_api.models.get_wars_war_id_killmails200_ok import GetWarsWarIdKillmails200Ok
from eve_api.models.get_wars_war_id_killmails_unprocessable_entity import GetWarsWarIdKillmailsUnprocessableEntity
from eve_api.models.get_wars_war_id_ok import GetWarsWarIdOk
from eve_api.models.get_wars_war_id_unprocessable_entity import GetWarsWarIdUnprocessableEntity
from eve_api.models.internal_server_error import InternalServerError
from eve_api.models.post_characters_affiliation200_ok import PostCharactersAffiliation200Ok
from eve_api.models.post_characters_character_id_assets_locations200_ok import PostCharactersCharacterIdAssetsLocations200Ok
from eve_api.models.post_characters_character_id_assets_locations_position import PostCharactersCharacterIdAssetsLocationsPosition
from eve_api.models.post_characters_character_id_assets_names200_ok import PostCharactersCharacterIdAssetsNames200Ok
from eve_api.models.post_characters_character_id_contacts_error520 import PostCharactersCharacterIdContactsError520
from eve_api.models.post_characters_character_id_fittings_created import PostCharactersCharacterIdFittingsCreated
from eve_api.models.post_characters_character_id_fittings_fitting import PostCharactersCharacterIdFittingsFitting
from eve_api.models.post_characters_character_id_fittings_item import PostCharactersCharacterIdFittingsItem
from eve_api.models.post_characters_character_id_mail_error520 import PostCharactersCharacterIdMailError520
from eve_api.models.post_characters_character_id_mail_labels_label import PostCharactersCharacterIdMailLabelsLabel
from eve_api.models.post_characters_character_id_mail_mail import PostCharactersCharacterIdMailMail
from eve_api.models.post_characters_character_id_mail_recipient import PostCharactersCharacterIdMailRecipient
from eve_api.models.post_corporations_corporation_id_assets_locations200_ok import PostCorporationsCorporationIdAssetsLocations200Ok
from eve_api.models.post_corporations_corporation_id_assets_locations_not_found import PostCorporationsCorporationIdAssetsLocationsNotFound
from eve_api.models.post_corporations_corporation_id_assets_locations_position import PostCorporationsCorporationIdAssetsLocationsPosition
from eve_api.models.post_corporations_corporation_id_assets_names200_ok import PostCorporationsCorporationIdAssetsNames200Ok
from eve_api.models.post_corporations_corporation_id_assets_names_not_found import PostCorporationsCorporationIdAssetsNamesNotFound
from eve_api.models.post_fleets_fleet_id_members_invitation import PostFleetsFleetIdMembersInvitation
from eve_api.models.post_fleets_fleet_id_members_not_found import PostFleetsFleetIdMembersNotFound
from eve_api.models.post_fleets_fleet_id_members_unprocessable_entity import PostFleetsFleetIdMembersUnprocessableEntity
from eve_api.models.post_fleets_fleet_id_wings_created import PostFleetsFleetIdWingsCreated
from eve_api.models.post_fleets_fleet_id_wings_not_found import PostFleetsFleetIdWingsNotFound
from eve_api.models.post_fleets_fleet_id_wings_wing_id_squads_created import PostFleetsFleetIdWingsWingIdSquadsCreated
from eve_api.models.post_fleets_fleet_id_wings_wing_id_squads_not_found import PostFleetsFleetIdWingsWingIdSquadsNotFound
from eve_api.models.post_ui_openwindow_newmail_new_mail import PostUiOpenwindowNewmailNewMail
from eve_api.models.post_ui_openwindow_newmail_unprocessable_entity import PostUiOpenwindowNewmailUnprocessableEntity
from eve_api.models.post_universe_ids_agent import PostUniverseIdsAgent
from eve_api.models.post_universe_ids_alliance import PostUniverseIdsAlliance
from eve_api.models.post_universe_ids_character import PostUniverseIdsCharacter
from eve_api.models.post_universe_ids_constellation import PostUniverseIdsConstellation
from eve_api.models.post_universe_ids_corporation import PostUniverseIdsCorporation
from eve_api.models.post_universe_ids_faction import PostUniverseIdsFaction
from eve_api.models.post_universe_ids_inventory_type import PostUniverseIdsInventoryType
from eve_api.models.post_universe_ids_ok import PostUniverseIdsOk
from eve_api.models.post_universe_ids_region import PostUniverseIdsRegion
from eve_api.models.post_universe_ids_station import PostUniverseIdsStation
from eve_api.models.post_universe_ids_system import PostUniverseIdsSystem
from eve_api.models.post_universe_names200_ok import PostUniverseNames200Ok
from eve_api.models.post_universe_names_not_found import PostUniverseNamesNotFound
from eve_api.models.put_characters_character_id_calendar_event_id_response import PutCharactersCharacterIdCalendarEventIdResponse
from eve_api.models.put_characters_character_id_mail_mail_id_contents import PutCharactersCharacterIdMailMailIdContents
from eve_api.models.put_fleets_fleet_id_members_member_id_movement import PutFleetsFleetIdMembersMemberIdMovement
from eve_api.models.put_fleets_fleet_id_members_member_id_not_found import PutFleetsFleetIdMembersMemberIdNotFound
from eve_api.models.put_fleets_fleet_id_members_member_id_unprocessable_entity import PutFleetsFleetIdMembersMemberIdUnprocessableEntity
from eve_api.models.put_fleets_fleet_id_new_settings import PutFleetsFleetIdNewSettings
from eve_api.models.put_fleets_fleet_id_not_found import PutFleetsFleetIdNotFound
from eve_api.models.put_fleets_fleet_id_squads_squad_id_naming import PutFleetsFleetIdSquadsSquadIdNaming
from eve_api.models.put_fleets_fleet_id_squads_squad_id_not_found import PutFleetsFleetIdSquadsSquadIdNotFound
from eve_api.models.put_fleets_fleet_id_wings_wing_id_naming import PutFleetsFleetIdWingsWingIdNaming
from eve_api.models.put_fleets_fleet_id_wings_wing_id_not_found import PutFleetsFleetIdWingsWingIdNotFound
from eve_api.models.service_unavailable import ServiceUnavailable
from eve_api.models.unauthorized import Unauthorized
