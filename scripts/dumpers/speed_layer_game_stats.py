from sqlalchemy.orm import sessionmaker
from models.sqlalchemy_base import base, db
from models.tournament import Tournament
from models.sqlalchemy_base import base, db
from models.game_event_game_object import GameEventGameObject
from models.game_event import GameEvent
from models.game_object import GameObject
from models.player_game import PlayerGame
from models.player_stats_event import PlayerStatsEvent
from models.player import Player
from models.replay import Replay
from models.tracker_event_game_object import TrackerEventGameObject
from models.tracker_event import TrackerEvent
from wrappers.replay import ReplayWrapper
from wrappers.playerStat import PlayerStat
from sqlalchemy.sql import select
from sqlalchemy import distinct


def get_active_games():
    Session = sessionmaker(db)
    session = Session()
    replay_db = session.query( Replay.date, Replay.game_type, PlayerGame.player_game_id,
     Replay.map_name, PlayerGame.color, PlayerGame.player, Player.url, Replay.replay_id).join(Player).limit(20)
    result = session.execute(replay_db)
    replays = {}
    for row in result:
        if row.Replay_replay_id in replays:
            replays[row.Replay_replay_id].players.append(row.Player_url)
        else:
            replays[row.Replay_replay_id] = ReplayWrapper(date=row.Replay_date, players=[row.Player_url],
            game_type=row.Replay_game_type, map_name=row.Replay_map_name, replay_id=row.Replay_replay_id)
    out = []
    for key in replays:
        replays[key].players = list(set(replays[key].players))
        out.append(replays[key])
    return out

def get_replay_stats(replay_id, frame):
    Session = sessionmaker(db)
    session = Session()
    replay_db = session.query(Replay.replay_id, PlayerStatsEvent, PlayerStatsEvent.player_game_id).filter(Replay.replay_id == replay_id).join(PlayerStatsEvent).filter(PlayerStatsEvent.frame > frame)

    result = session.execute(replay_db)
    stats = []
    for row in result:
        stats.append(PlayerStat(
    ff_minerals_lost_army = row[2],
    ff_minerals_lost_economy = row[3],
    ff_minerals_lost_technology = row[4],
    ff_vespene_lost_army = row[5],
    ff_vespene_lost_economy = row[6],
    ff_vespene_lost_technology = row[7],
    food_made = row[8],
    food_used = row[9],
    frame = row[10],
    minerals_collection_rate = row[11],
    minerals_current = row[12],
    minerals_killed = row[13],
    minerals_killed_army = row[14],
    minerals_killed_economy = row[15],
    minerals_killed_technology = row[16],
    minerals_lost = row[17],
    minerals_lost_army = row[18],
    minerals_lost_economy = row[19],
    minerals_lost_technology = row[20],
    minerals_used_active_forces = row[21],
    minerals_used_current = row[22],
    minerals_used_current_army = row[23],
    minerals_used_current_economy = row[24],
    minerals_used_current_technology = row[25],
    minerals_used_in_progress = row[26],
    minerals_used_in_progress_army = row[27],
    minerals_used_in_progress_economy = row[28],
    minerals_used_in_progress_technology = row[29],
    pid = row[30],
    resources_killed = row[31],
    resources_lost = row[32],
    resources_used_current = row[33],
    resources_used_in_progress = row[34],
    second = row[35],
    vespene_collection_rate = row[36],
    vespene_current = row[37],
    vespene_killed = row[38],
    vespene_killed_army = row[39],
    vespene_killed_economy = row[40],
    vespene_killed_technology = row[41],
    vespene_lost = row[42],
    vespene_lost_army = row[43],
    vespene_lost_economy = row[44],
    vespene_lost_technology = row[45],
    vespene_used_active_forces = row[46],
    vespene_used_current = row[47],
    vespene_used_current_army = row[48],
    vespene_used_current_economy = row[49],
    vespene_used_current_technology = row[50],
    vespene_used_in_progress = row[51],
    vespene_used_in_progress_army = row[52],
    vespene_used_in_progress_economy = row[53],
    vespene_used_in_progress_technology = row[54],
    workers_active_count = row[55],
    player_game_id=row[56]
    ))
    return stats