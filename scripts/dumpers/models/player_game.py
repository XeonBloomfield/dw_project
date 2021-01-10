from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from models.sqlalchemy_base import base, copy_fields


class PlayerGame(base):
    __tablename__ = "PlayerGame"
    player_game_id = Column(Integer, primary_key=True)
    result = Column(String)
    pick_race = Column(String)
    team_id = Column(Integer)
    is_human = Column(Boolean)
    commander_level = Column(Integer)
    combined_race_levels = Column(BigInteger)
    color = Column(String)
    player_id = Column(Integer, ForeignKey("Player.player_id"))
    player = relationship("Player", back_populates="player_games")
    replay_id = Column(Integer, ForeignKey("Replay.replay_id"))
    replay = relationship("Replay", back_populates="player_games")
    tracker_events = relationship("TrackerEvent", back_populates="player_game")
    game_events = relationship("GameEvent", back_populates="player_game")
    player_stats_events = relationship(
        "PlayerStatsEvent", back_populates="player_game")
    to_copy = ["result", "pick_race", "team_id", "is_human",
               "commander_level", "combined_race_levels", "color"]

    def load_raw_data(self, raw_object):
        copy_fields(raw_object, self, self.to_copy)
        self.color = raw_object.color.hex
