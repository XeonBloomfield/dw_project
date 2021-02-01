from pydantic import BaseModel
from datetime import date
from typing import List, Dict

class ReplayWrapper(BaseModel):
    date: date
    game_type: str
    map_name: str
    replay_id: int
    players: List[str]
    # aggr
    apm: List[float]
    spm: List[float]
    units: List[Dict[str, int]]
    structures: List[Dict[str, int]]
    favourite_unit: List[str]
    structure_heatmap: str
    kills_heatmap: str
