from matplotlib import pyplot as plt
import numpy as np
import json
import os
from mpl_toolkits.mplot3d import Axes3D
def preprocess(path, player_id):  #  ->[x,y]
    '''
    return : x, y and [x, y] trajectory for the player in certain round
    '''
    # load data
    # data_dir = os.listdir("data/test/")
    # for dir in data_dir:
    player = {}
    with open(path, 'r') as load_f:
        data = json.load(load_f)
    #print(len(data))

    data.sort(key=lambda x: x['game_clock'], reverse=True)
    # player_position = data['player_position']  #list
    px = []
    py = []
    pxy = []
    for d in data:
        for p in d['player_position']:
            # print(p[1])
            if p[1] == player_id:
                px.append(p[2])
                py.append(p[3])
                pxy.append([p[2], p[3]])

    return px, py, pxy
    # print((pxy))
    # # data.sort(key=lambda x: x['game_clock'], reverse=True)
    # for d in data:
    #     print("rest_time:",d['game_clock'])
    #     for p in d['player_position']:
    #         player[p[1]].append(p['player_position'])  #p[1] : player id
    # print(player)

# def _get





if __name__ == '__main__':
    preprocess("data/test/31/movement_31.json", 203138)