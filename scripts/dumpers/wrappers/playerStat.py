from pydantic import BaseModel
from datetime import date
from typing import List

class PlayerStat(BaseModel):
    ff_minerals_lost_army : int
    ff_minerals_lost_economy : int
    ff_minerals_lost_technology : int
    ff_vespene_lost_army : int
    ff_vespene_lost_economy : int
    ff_vespene_lost_technology : int
    food_made : float
    food_used : float
    frame : int
    minerals_collection_rate : int
    minerals_current : int
    minerals_killed : int
    minerals_killed_army : int
    minerals_killed_economy : int
    minerals_killed_technology : int
    minerals_lost : int
    minerals_lost_army : int
    minerals_lost_economy : int
    minerals_lost_technology : int
    minerals_used_active_forces : int
    minerals_used_current : int
    minerals_used_current_army : int
    minerals_used_current_economy : int
    minerals_used_current_technology : int
    minerals_used_in_progress : int
    minerals_used_in_progress_army : int
    minerals_used_in_progress_economy : int
    minerals_used_in_progress_technology : int
    pid : int
    resources_killed : int
    resources_lost : int
    resources_used_current : int
    resources_used_in_progress : int
    second : int
    vespene_collection_rate : int
    vespene_current : int
    vespene_killed : int
    vespene_killed_army : int
    vespene_killed_economy : int
    vespene_killed_technology : int
    vespene_lost : int
    vespene_lost_army : int
    vespene_lost_economy : int
    vespene_lost_technology : int
    vespene_used_active_forces : int
    vespene_used_current : int
    vespene_used_current_army : int
    vespene_used_current_economy : int
    vespene_used_current_technology : int
    vespene_used_in_progress : int
    vespene_used_in_progress_army : int
    vespene_used_in_progress_economy : int
    vespene_used_in_progress_technology : int
    workers_active_count : int
    player_game_id: int