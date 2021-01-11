from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.sqlalchemy_base import base, copy_fields


class TrackerEvent(base):
    __tablename__ = "TrackerEvent"
    tracker_event_id = Column(Integer, primary_key=True)
    name = Column(String)
    tracker_event_game_objects = relationship(
        "TrackerEventGameObject", back_populates="tracker_event")
    frame = Column(Integer)
    replay_id = Column(Integer, ForeignKey("Replay.replay_id"))
    replay = relationship("Replay", back_populates="tracker_events")
    to_copy = ["name", "frame"]

    def load_raw_data(self, raw_object):
        copy_fields(raw_object, self, self.to_copy)
