from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_base import base



class Replay(base):
    __tablename__ = "Replay"
    replay_id = Column(Integer, primary_key=True)
    category = Column(String)
    battle_net = Column(Boolean)
    competetive = Column(Boolean)
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
    tournament_id = Column(Integer, ForeignKey("Tournament.tournament_id"))
    tournament = relationship("Tournament", back_populates="replays")
    game_objects = relationship("GameObject", back_populates="replay")
    player_games = relationship("PlayerGame", back_populates="replay")
    to_copy = ["category", "battleNet", "competetive", "cooperative", "date", "unix_timestamp",
               "gameType", "expansion", "frames", "game_fps", "lenght", "map_hash", "map_name",
               "region", "speed"]
