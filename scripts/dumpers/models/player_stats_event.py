from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.sqlalchemy_base import base, copy_fields


class PlayerStatsEvent(base):
    __tablename__ = "PlayerStatsEvent"
    player_stats_event_id = Column(Integer, primary_key=True)
    ff_minerals_lost_army = Column(Integer)
    ff_minerals_lost_economy = Column(Integer)
    ff_minerals_lost_technology = Column(Integer)
    ff_vespene_lost_army = Column(Integer)
    ff_vespene_lost_economy = Column(Integer)
    ff_vespene_lost_technology = Column(Integer)
    food_made = Column(Float)
    food_used = Column(Float)
    frame = Column(Integer)
    minerals_collection_rate = Column(Integer)
    minerals_current = Column(Integer)
    minerals_killed = Column(Integer)
    minerals_killed_army = Column(Integer)
    minerals_killed_economy = Column(Integer)
    minerals_killed_technology = Column(Integer)
    minerals_lost = Column(Integer)
    minerals_lost_army = Column(Integer)
    minerals_lost_economy = Column(Integer)
    minerals_lost_technology = Column(Integer)
    minerals_used_active_forces = Column(Integer)
    minerals_used_current = Column(Integer)
    minerals_used_current_army = Column(Integer)
    minerals_used_current_economy = Column(Integer)
    minerals_used_current_technology = Column(Integer)
    minerals_used_in_progress = Column(Integer)
    minerals_used_in_progress_army = Column(Integer)
    minerals_used_in_progress_economy = Column(Integer)
    minerals_used_in_progress_technology = Column(Integer)
    pid = Column(Integer)
    resources_killed = Column(Integer)
    resources_lost = Column(Integer)
    resources_used_current = Column(Integer)
    resources_used_in_progress = Column(Integer)
    second = Column(Integer)
    vespene_collection_rate = Column(Integer)
    vespene_current = Column(Integer)
    vespene_killed = Column(Integer)
    vespene_killed_army = Column(Integer)
    vespene_killed_economy = Column(Integer)
    vespene_killed_technology = Column(Integer)
    vespene_lost = Column(Integer)
    vespene_lost_army = Column(Integer)
    vespene_lost_economy = Column(Integer)
    vespene_lost_technology = Column(Integer)
    vespene_used_active_forces = Column(Integer)
    vespene_used_current = Column(Integer)
    vespene_used_current_army = Column(Integer)
    vespene_used_current_economy = Column(Integer)
    vespene_used_current_technology = Column(Integer)
    vespene_used_in_progress = Column(Integer)
    vespene_used_in_progress_army = Column(Integer)
    vespene_used_in_progress_economy = Column(Integer)
    vespene_used_in_progress_technology = Column(Integer)
    workers_active_count = Column(Integer)
    player_game_id = Column(Integer, ForeignKey("PlayerGame.player_game_id"))
    player_game = relationship(
        "PlayerGame", back_populates="player_stats_events")
    to_copy = ["ff_minerals_lost_army", "ff_minerals_lost_economy", "ff_minerals_lost_technology",
               "ff_vespene_lost_army", "ff_vespene_lost_economy", "ff_vespene_lost_technology",
               "food_made", "food_used", "frame", "minerals_collection_rate",
               "minerals_current", "minerals_killed", "minerals_killed_army", "minerals_killed_economy",
               "minerals_killed_technology", "minerals_lost", "minerals_lost_army",
               "minerals_lost_economy", "minerals_lost_technology", "minerals_used_active_forces",
               "minerals_used_current", "minerals_used_current_army", "minerals_used_current_economy",
               "minerals_used_current_technology", "minerals_used_in_progress",
               "minerals_used_in_progress_army", "minerals_used_in_progress_economy",
               "minerals_used_in_progress_technology", "pid", "resources_killed", "resources_lost",
               "resources_used_current", "resources_used_in_progress", "second",
               "vespene_collection_rate", "vespene_current", "vespene_killed", "vespene_killed_army",
               "vespene_killed_economy", "vespene_killed_technology", "vespene_lost", "vespene_lost_army",
               "vespene_lost_economy", "vespene_lost_technology", "vespene_used_active_forces",
               "vespene_used_current", "vespene_used_current_army", "vespene_used_current_economy",
               "vespene_used_current_technology", "vespene_used_in_progress",
               "vespene_used_in_progress_army", "vespene_used_in_progress_economy",
               "vespene_used_in_progress_technology", "workers_active_count"]

    def load_raw_data(self, raw_object):
        copy_fields(raw_object, self, self.to_copy)
