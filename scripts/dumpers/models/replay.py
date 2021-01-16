from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.sqlalchemy_base import base, copy_fields


class Replay(base):
    __tablename__ = "Replay"
    replay_id = Column(Integer, primary_key=True)
    category = Column(String)
    battle_net = Column(Boolean)
    competitive = Column(Boolean)
    cooperative = Column(Boolean)
    date = Column(DateTime)
    unix_timestamp = Column(Integer)
    game_type = Column(String)
    expansion = Column(String)
    frames = Column(Integer)
    game_fps = Column(Integer)
    lenght = Column(Integer)
    map_hash = Column(String)
    map_name = Column(String)
    region = Column(String)
    speed = Column(String)
    filehash = Column(String)
    tournament_id = Column(Integer, ForeignKey("Tournament.tournament_id"))
    tournament = relationship("Tournament", back_populates="replays")
    game_objects = relationship("GameObject", back_populates="replay")
    player_games = relationship("PlayerGame", back_populates="replay")
    tracker_events = relationship("TrackerEvent", back_populates="replay")
    game_events = relationship("GameEvent", back_populates="replay")
    player_stats_events = relationship(
        "PlayerStatsEvent", back_populates="replay")
    to_copy = ["category", "battle_net", "competitive", "cooperative", "date", "unix_timestamp",
               "game_type", "expansion", "frames", "game_fps", "lenght", "map_hash", "map_name",
               "region", "speed", "filehash"]

    def load_raw_data(self, raw_object):
        copy_fields(raw_object, self, self.to_copy)
        self.battle_net = raw_object.battle_net > 0
        self.competitive = raw_object.competitive > 0
        self.cooperative = raw_object.cooperative > 0
        self.lenght = raw_object.length.seconds
