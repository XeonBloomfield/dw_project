import sc2reader

filepath = 'dataset/Replays/0000e057beefc9b1e9da959ed921b24b9f0a31c63fedb8d94a1db78b58cf92c5.SC2Replay'

replay = sc2reader.load_replay(filepath)

print(replay)
