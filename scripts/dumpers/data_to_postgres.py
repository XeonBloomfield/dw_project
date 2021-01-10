import sc2reader
from sqlalchemy.orm import sessionmaker
from models.sqlalchemy_base import base, db
from models import game_event, game_object, player_game, player_stats_event,\
    player, replay, tournament, tracker_event_game_object, tracker_event


def copy_fields(source, desitnation, fields):
    for field in fields:
        if hasattr(source, field):
            setattr(desitnation, field, getattr(source, field))


if __name__ == "__main__":
    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)
    replays = sc2reader.load_replays("dataset/Replays")
