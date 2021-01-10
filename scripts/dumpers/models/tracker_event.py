from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_base import base


class TrackerEvent(base):
    __tablename__ = "TrackerEvent"
    tracker_event_id = Column(Integer, primary_key=True)
    tracker_type = Column(String)
    tracker_event_game_objects = relationship(
        "TrackerEventGameObject", back_populates="tracker_event")
    player_game_id = Column(Integer, ForeignKey("PlayerGame.player_game_id"))
    player_game = relationship("PlayerGame", back_populates="tracker_events")
