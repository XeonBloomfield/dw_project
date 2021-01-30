from pydantic import BaseModel
from datetime import date
from typing import List

class ReplayWrapper(BaseModel):
    date: date
    game_type: str
    map_name: str
    replay_id: int
    players: List[str]
    # aggr