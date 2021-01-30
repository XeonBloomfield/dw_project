from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from speed_layer_game_stats import get_active_games, get_replay_stats
from wrappers.replay import ReplayWrapper
from wrappers.playerStat import PlayerStat

origins = [
    "http://localhost",
    "http://localhost:4200"
]

ReplayWrappers = List[ReplayWrapper]
PlayerStats = List[PlayerStat]

class Server:
    app = FastAPI()
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    @app.get("/currState/{replayId}/{frame}", response_model=PlayerStats)
    def read_root(replayId: int, frame: int):
        return get_replay_stats(replayId, frame)

    @app.get("/game/active", response_model=ReplayWrappers)
    def read_root():
        return get_active_games()

    @app.get("/game/finished", response_model=ReplayWrappers)
    def read_root():
        return []


if __name__ == "__main__":
    server = Server()
    try:
        uvicorn.run(server.app, host="0.0.0.0", port=8000, log_level="info")
    except ValueError as er:
        print("[ERROR] %s" % er)
