import json
import glob
import os
fn = glob.glob("clean_data/*/*/metadata.json")
for f in fn:
    move = f.replace("metadata", "movement_refined_shot_clock")
    with open(f, 'r') as load_f:
        metadata = json.load(load_f)
    s = metadata['possession_start_index']
    e = metadata['possession_end_index']
    with open(move, 'r') as load_move:
        movement = json.load(load_move)

    event = movement[s:e + 1]
    import numpy as np
    target_path = f.replace("metadata", "vector")
    for e in event:
        element = []
        element.append(e['shot_clock'])
        for i in range(3):
            element.append(e['ball_position'][i])
        for p in e['player_position']:
            element.append(p[2])
            element.append(p[3])
        # element = nparray(element,dtype = np.float32)

        with open(target_path, 'a+') as  f:
            json.dump(element, f)
