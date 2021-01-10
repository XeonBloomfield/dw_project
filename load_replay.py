import sc2reader

filepath = 'dataset/Replays/00a34632e38a7547e98bbcd50d9928b6c238ffc8db2dd9502955c07600baf713.SC2Replay'

replay = sc2reader.load_replay(filepath)

print(replay)
