from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.sqlalchemy_base import base, copy_fields


class GameEventGameObject(base):
    __tablename__ = "GameEventGameObject"
    game_event_game_object_id = Column(Integer, primary_key=True)
    role = Column(String)
    game_event_id = Column(Integer, ForeignKey("GameEvent.game_event_id"))
    game_event = relationship(
        "GameEvent", back_populates="game_event_game_objects")
    game_object_id = Column(Integer, ForeignKey("GameObject.game_object_id"))
    game_object = relationship(
        "GameObject", back_populates="game_event_game_objects")

    def load_raw_data(self, raw_object):
        copy_fields(raw_object, self, self.to_copy)
