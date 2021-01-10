import sc2reader
from sqlalchemy.orm import sessionmaker
from models.sqlalchemy_base import base, db
from models.game_event import GameEvent
from models.game_object import GameObject
from models.player_game import PlayerGame
from models.player_stats_event import PlayerStatsEvent
from models.player import Player
from models.replay import Replay
from models.tournament import Tournament
from models.tracker_event_game_object import TrackerEventGameObject
from models.tracker_event import TrackerEvent


def copy_fields(source, desitnation, fields):
    for field in fields:
        if hasattr(source, field):
            setattr(desitnation, field, getattr(source, field))


if __name__ == "__main__":
    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)
    replays = sc2reader.load_replays("dataset/Replays")
