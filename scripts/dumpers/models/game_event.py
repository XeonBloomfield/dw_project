from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.sqlalchemy_base import base, copy_fields


class GameEvent(base):
    __tablename__ = "GameEvent"
    game_event_id = Column(Integer, primary_key=True)
    frmae = Column(Integer)
    game_event_type = Column(String)
    player_game_id = Column(Integer, ForeignKey("PlayerGame.player_game_id"))
    player_game = relationship("PlayerGame", back_populates="game_events")
    to_copy = ["frame", "game_event_type"]
    game_event_game_objects = relationship(
        "GameEventGameObject", back_populates="game_event")

    def load_raw_data(self, raw_object):
        copy_fields(raw_object, self, self.to_copy)
