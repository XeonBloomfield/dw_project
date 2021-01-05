from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sc2reader

db_string = "postgresql://postgres:user@localhost:5432/speed"
db = create_engine(db_string)
base = declarative_base()
replays = sc2reader.load_replays("dataset/Replays")


class Replay(base):
    __tablename__ = "Replay"
    replay_id = Column(Integer, primary_key=True)
    frames = Column(Integer)
    date = Column(DateTime)
    events = relationship("Event", back_populates="replay")


class Event(base):
    __tablename__ = "Event"
    event_id = Column(Integer, primary_key=True)
    frame = Column(Integer)
    replay_id = Column(Integer, ForeignKey("Replay.replay_id"))
    replay = relationship("Replay", back_populates="events")


if __name__ == "__main__":
    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)

    for replay in replays:
        replay_obj = Replay(frames=replay.frames, date=replay.date)
        session.add(replay_obj)
        for event in replay.events:
            event_obj = Event(frame=event.frame, replay = replay_obj)
            session.add(event_obj)
        session.commit()
