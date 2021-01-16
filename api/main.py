from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:4200"
]

time = 0

class GameObject(BaseModel):
    name: str
    startedAt: int
    finishedAt: int
    unitResValue: int
    diedAt: int
    isArmy: bool
    isBuilding: bool
    isWorker: bool
    x: int
    y: int

GameObjects = List[GameObject]

states = [
    [GameObject(name='Krzysio', startedAt=0, unitResValue=20, finishedAt=0, diedAt=10, isArmy=True, isBuilding=False, isWorker=False, x=10, y=10),
    GameObject(name='Zbysio', startedAt=0, unitResValue=30,finishedAt=0, diedAt=10, isArmy=True, isBuilding=False, isWorker=False, x=30, y=10)]
]

class Server:
    app = FastAPI()
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    @app.get("/currState", response_model=GameObjects)
    def read_root():
        global time
        curr_state = states[0]
        curr_state[0].unitResValue += 4*time
        curr_state[1].unitResValue += 4*time
        print(curr_state)
        time += 1
        return curr_state


if __name__ == "__main__":
    server = Server()
    try:
        uvicorn.run(server.app, host="0.0.0.0", port=8000, log_level="info")
    except ValueError as er:
        print("[ERROR] %s" % er)
