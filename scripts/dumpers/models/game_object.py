from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from models.sqlalchemy_base import base, copy_fields


class GameObject(base):
    __tablename__ = "GameObject"
    game_object_id = Column(Integer, primary_key=True)
    name = Column(String)
    finished_at = Column(Integer)
    started_at = Column(Integer)
    died_at = Column(Integer)
    is_army = Column(Boolean)
    is_building = Column(Boolean)
    is_worker = Column(Boolean)
    minerals = Column(Integer)
    vespene = Column(Integer)
    supply = Column(Integer)
    internal_id = Column(Integer)
    replay_id = Column(Integer, ForeignKey("Replay.replay_id"))
    replay = relationship("Replay", back_populates="game_objects")
    killed_by_id = Column(Integer, ForeignKey("GameObject.game_object_id"))
    killed = relationship(
        "GameObject", backref=backref("killed_by", remote_side=[game_object_id]), post_update=True)
    tracker_event_game_objects = relationship(
        "TrackerEventGameObject", back_populates="game_object")
    to_copy = ["name", "finished_at", "started_at", "died_at", "is_army",
               "is_building", "is_worker", "minerals", "vespene", "supply"]
    game_event_game_objects = relationship(
        "GameEventGameObject", back_populates="game_object")

    def load_raw_data(self, raw_object):
        copy_fields(raw_object, self, self.to_copy)
        self.internal_id = raw_object.id
