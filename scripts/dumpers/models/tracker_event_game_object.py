from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.sqlalchemy_base import base


class TrackerEventGameObject(base):
    __tablename__ = "TrackerEventGameObject"
    tracker_event_game_object_id = Column(Integer, primary_key=True)
    role = Column(String)
    tracker_event_id = Column(Integer, ForeignKey(
        "TrackerEvent.tracker_event_id"))
    tracker_event = relationship(
        "TrackerEvent", back_populates="tracker_event_game_objects")
    game_object_id = Column(Integer, ForeignKey("GameObject.game_object_id"))
    game_object = relationship(
        "GameObject", back_populates="tracker_event_game_objects")
