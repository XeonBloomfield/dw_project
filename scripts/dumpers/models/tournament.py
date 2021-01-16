from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from models.sqlalchemy_base import base


class Tournament(base):
    __tablename__ = "Tournament"
    tournament_id = Column(Integer, primary_key=True)
    name = Column(String)
    year = Column(Integer)
    replays = relationship("Replay", back_populates="tournament")
    to_copy = ['name', 'year']
