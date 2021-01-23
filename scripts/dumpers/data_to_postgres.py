import sc2reader
from sqlalchemy.orm import sessionmaker
from models.sqlalchemy_base import base, db
from models.game_event_game_object import GameEventGameObject
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

    # Load replays
    replays_raw = sc2reader.load_replays("dataset/Replays")
    tournaments = []
    for replay in replays_raw:
        replays = []
        players = []
        player_games = []
        player_stats_events = []
        game_objects = []
        tracker_events = []
        game_events = []
        tracker_event_game_objects = []
        game_event_game_objects = []

        # Tournament
        filename_split = replay.filename.split("\\")
        tournament_db = session.query(
            Tournament).filter_by(name=filename_split[2]).first()
        if tournament_db is None:
            tournament_db = Tournament(
                name=filename_split[2], year=filename_split[1])
            tournaments.append(tournament_db)

        # Replay
        replay_db = session.query(Replay).filter_by(
            filehash=replay.filehash).first()
        if replay_db is None:
            replay_db = Replay()
            replay_db.load_raw_data(replay)
        else:
            continue  # !If the replay exist in DB we skip it
        replay_db.tournament = tournament_db
        replays.append(replay_db)

        # Players
        for player in replay.players:
            player_db = session.query(Player).filter_by(
                toon_id=player.toon_id).first()
            if player_db is None:
                player_db = Player()
                player_db.load_raw_data(player)
            players.append(player_db)

            # PlayerGame
            player_game_db = PlayerGame()
            player_game_db.load_raw_data(player)
            player_game_db.player = player_db
            player_game_db.replay = replay_db
            player_games.append(player_game_db)

        # GameObjects
        for game_object in replay.objects.values():
            game_object_db = GameObject()
            game_object_db.load_raw_data(game_object)
            game_object_db.replay = replay_db
            if hasattr(game_object.owner, "toon_id") and game_object.owner.toon_id is not None:
                owner_toon_id = game_object.owner.toon_id
                player_game = next(
                    (x for x in player_games if x.player.toon_id == owner_toon_id), None)
                game_object_db.player_game = player_game
            game_objects.append(game_object_db)

        # GameObject.killed_by
        for game_object in replay.objects.values():
            if game_object.killed_by is not None and game_object.killing_unit is not None:
                killer_go_db = next(
                    (x for x in game_objects if x.internal_id == game_object.killing_unit.id), None)
                killed_go_db = next(
                    (x for x in game_objects if x.internal_id == game_object.id), None)
                killed_go_db.killed_by = killed_go_db

        for tracker_event in replay.tracker_events:
            # PlayerStatsEvent
            if isinstance(tracker_event, sc2reader.events.tracker.PlayerStatsEvent):
                player_stats_event_db = PlayerStatsEvent()
                player_stats_event_db.replay = replay_db
                player_stats_event_db.load_raw_data(tracker_event)
                player_stats_event_db.player_game = next(
                    (x for x in player_games if x.player.toon_id == tracker_event.player.toon_id), None)
                player_stats_events.append(player_stats_event_db)
            # TrackerEvent
            elif hasattr(tracker_event, "unit"):
                tracker_event_db = TrackerEvent()
                tracker_event_db.replay = replay_db
                tracker_event_db.load_raw_data(tracker_event)
                unit_db = next(
                    (x for x in game_objects if x.internal_id == tracker_event.unit.id), None)
                tracker_event_game_object_db = TrackerEventGameObject()
                tracker_event_game_object_db.game_object = unit_db
                tracker_event_game_object_db.tracker_event = tracker_event_db
                tracker_event_game_object_db.role = "subject"
                tracker_events.append(tracker_event_db)
                tracker_event_game_objects.append(tracker_event_game_object_db)

        # GameEvents
        for game_event in replay.game_events:
            game_event_db = GameEvent()
            game_event_db.load_raw_data(game_event)
            player_game = next(
                (x for x in player_games if x.player.toon_id == game_event.player.toon_id), None)
            if player_game is None:
                continue
            game_event_db.player_game = player_game
            game_event_db.replay = replay_db
            if hasattr(game_event, "objects"):
                for obj in game_event.objects:
                    game_obj = next(
                        (x for x in game_objects if x.internal_id == obj.id), None)
                    game_event_game_object_db = GameEventGameObject()
                    game_event_game_object_db.role = "Subject"
                    game_event_game_object_db.game_object = game_obj
                    game_event_game_object_db.game_event = game_event_db
                    game_event_game_objects.append(game_event_game_object_db)
            if hasattr(game_event, "target"):
                target_obj = next(
                    (x for x in game_objects if x.internal_id == game_event.target.id), None)
                game_event_game_object_db = GameEventGameObject()
                game_event_game_object_db.role = "Target"
                game_event_game_object_db.game_object = target_obj
                game_event_game_object_db.game_event = game_event_db
                game_event_game_objects.append(game_event_game_object_db)
            game_events.append(game_event_db)

        session.add_all(tournaments)
        session.add_all(replays)
        session.add_all(players)
        session.add_all(player_games)
        session.add_all(player_stats_events)
        session.add_all(game_objects)
        session.add_all(tracker_events)
        session.add_all(game_events)
        session.add_all(tracker_event_game_objects)
        session.add_all(game_event_game_objects)
        session.commit()
        print("Replay loaded")
