from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sc2reader

db_string = "postgresql://postgres:user@localhost:5432/speed"
db = create_engine(db_string)
base = declarative_base()
replays = sc2reader.load_replays("dataset/Replays")


class Tournament(base):
    __tablename__ = "Tournament"
    tournament_id = Column(Integer, primary_key=True)
    name = Column(String)
    replays = relationship("Replay", back_populates="tournament")


class Replay(base):
    __tablename__ = "Replay"
    replay_id = Column(Integer, primary_key=True)
    category = Column(String)
    battleNet = Column(Boolean)
    competetive = Column(Boolean)
    cooperative = Column(Boolean)
    date = Column(DateTime)
    unix_timestamp = Column(Integer)
    gameType = Column(String)
    expansion = Column(String)
    frames = Column(Integer)
    game_fps = Column(Integer)
    lenght = Column(Integer)
    map_hash = Column(String)
    map_name = Column(String)
    region = Column(String)
    speed = Column(String)
    tournament_id = Column(Integer, ForeignKey("Tournament.tournament_id"))
    tournament = relationship("Tournament", back_populates="replays")
    events = relationship("Event", back_populates="replay")
    game_objects = relationship("GameObject", back_populates="replay")
    player_games = relationship("PlayerGame", back_populates="replay")


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
    replay_id = Column(Integer, ForeignKey("Replay.replay_id"))
    replay = relationship("Replay", back_populates="game_objects")
    killed = relationship("GameObject", back_populates="killed_by")
    killed_by_id = Column(Integer, ForeignKey("GameObject.game_object_id"))
    killed_by = relationship("GameObject", back_populates="killed_by_id")
    tracker_event_game_objects = relationship(
        "TrackerEventGameObject", back_populates="game_object")


class TrackerEventGameObject(base):
    __tablename__ = "TrackerEventGameObject"
    tracker_event_game_object_id = Column(Integer, primary_key=True)
    role = Column(String)
    tracker_event_id = Column(Integer, ForeignKey(
        "TrackerEvent.tracker_event_id"))
    tracker_event = relationship(
        "TrackerEvent", back_populates="tracker_event_game_objects")
    game_object_id = Column(Integer, ForeignKey("GameObject.game_object_id"))
    game_object = relationship(
        "GameObject", back_populates="tracker_event_game_objects")


class TrackerEvent(base):
    __tablename__ = "TrackerEvent"
    tracker_event_id = Column(Integer, primary_key=True)
    tracker_type = Column(String)
    tracker_event_game_objects = relationship(
        "TrackerEventGameObject", back_populates="tracker_event")
    player_game_id = Column(Integer, ForeignKey("PlayerGame.player_game_id"))
    player_game = relationship("PlayerGame", back_populates="tracker_events")


class Player(base):
    __tablename__ = "Player"
    player_id = Column(Integer, primary_key=True)
    url = Column(String)
    player_games = relationship("PlayerGame", back_populates="player_id")


class PlayerGame(base):
    __tablename__ = "PlayerGame"
    player_game_id = Column(Integer, primary_key=True)
    result = Column(String)
    pick_race = Column(String)
    team_id = Column(Integer)
    is_human = Column(Boolean)
    commander_level = Column(Integer)
    combined_race_levels = Column(Integer)
    color = Column(String)
    player_id = Column(Integer, ForeignKey("Player.player_id"))
    player = relationship("Player", back_populates="player_games")
    replay_id = Column(Integer, ForeignKey("Replay.replay_id"))
    replay = relationship("Replay", back_populates="player_games")
    tracker_events = relationship("TrackerEvent", back_populates="player_game")
    game_events = relationship("GameEvent", back_populates="player_game")
    player_stats_events = relationship(
        "PlayerStatsEvent", back_populates="player_game")


class GameEvent(base):
    __tablename__ = "GameEvent"
    game_event_id = Column(Integer, primary_key=True)
    frmae = Column(Integer)
    game_event_type = Column(String)
    player_game_id = Column(Integer, ForeignKey("PlayerGame.player_game_id"))
    player_game = relationship("PlayerGame", back_populates="game_events")


class PlayerStatsEvent(base):
    __tablename__ = "PlayerStatsEvent"
    player_stats_event_id = Column(Integer, primary_key=True)
    player_game_id = Column(Integer, ForeignKey("PlayerGame.player_game_id"))
    player_game = relationship(
        "PlayerGame", back_populates="player_stats_events")


if __name__ == "__main__":
    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)

    for replay in replays:
        replay_obj = Replay(frames=replay.frames, date=replay.date)
        session.add(replay_obj)
        for event in replay.events:
            event_obj = Event(frame=event.frame, replay=replay_obj)
            session.add(event_obj)
        session.commit()
