from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_base import base


class Player(base):
    __tablename__ = "Player"
    player_id = Column(Integer, primary_key=True)
    url = Column(String)
    toon_id = Column(Integer)
    player_games = relationship("PlayerGame", back_populates="player")
    to_copy = ["url", "toon_id"]
