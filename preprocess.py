from matplotlib import pyplot as plt
import numpy as np
import json
import os
from mpl_toolkits.mplot3d import Axes3D
import os

os.environ["OMP_NUM_THREADS"] = "1"

import traceback
import json
import glob
import os
import re
import subprocess
from multiprocessing.pool import Pool
# from tqdm import tqdm
# import pandas as pd

g2p = None
COLLATED_DATA_DIR = "data/collated_data/trajectory"




# def preprocess(raw_data_dir):   # 'data/raw_data/trajectory'
#
#     # games = os.listdir(raw_data_dir)
#     # # for g in games:
#     # #     round = os.listdir(raw_data_dir+"/"+g)
#     # #     for r in round:
#     #         fn = os.listdir(raw_data_dir+"/"+g+"/"+r)
#     p = Pool(os.cpu_count())
#     fn = glob.glob(raw_data_dir+"/*/*/metadata_*")
#     #print(fn)
#     for f in fn:
#         # if(f[:8]=='metadata'):
#         with open(f, 'r') as load_f:
#             metadata = json.load(load_f)
#         gameid = metadata['gameid']
#         movement = f[-7:-5]
#         print(movement)
#         for team in ["home", "visitor"]:
#             players = metadata[team]['players']
#             movement_path = f.replace("metadata", "movement")
#             gen_dir = COLLATED_DATA_DIR + "/" + gameid + "/" + movement + "/" + team
#             os.makedirs(gen_dir, exist_ok=True)
#             for player in players:
#                 p.apply_async(player2trajectory, args=[movement_path, gen_dir, player['playerid']])
#     p.close()



# def player2trajectory(path, target_dir,  player_id):  #  ->[x,y]
#     '''
#     return : x, y and [x, y] trajectory for the player in certain round
#     '''
#     # load data
#     # data_dir = os.listdir("data/test/")
#     # for dir in data_dir:
#     player = {}
#     with open(path, 'r') as load_f:
#         data = json.load(load_f)
#     #print(len(data))
#
#     data.sort(key=lambda x: x['game_clock'], reverse=True)
#     # player_position = data['player_position']  #list
#     px = []
#     py = []
#     pxy = []
#     for d in data:
#         for p in d['player_position']:
#             # print(p[1])
#             if p[1] == player_id:
#                 px.append(p[2])
#                 py.append(p[3])
#                 pxy.append([p[2], p[3]])
#     dict = {'px':px, "py":py, "pxy":pxy}
#     with open(target_dir +"/"+ "p_" + player_id, 'w') as  f:
#         json.dump(dict, f)
#     return px, py, pxy
    # print((pxy))
    # # data.sort(key=lambda x: x['game_clock'], reverse=True)
    # for d in data:
    #     print("rest_time:",d['game_clock'])
    #     for p in d['player_position']:
    #         player[p[1]].append(p['player_position'])  #p[1] : player id
    # print(player)

# def _get

def preprocess(raw_data_dir):  # 'data/raw_data/trajectory'

    # games = os.listdir(raw_data_dir)
    # # for g in games:
    # #     round = os.listdir(raw_data_dir+"/"+g)
    # #     for r in round:
    #         fn = os.listdir(raw_data_dir+"/"+g+"/"+r)
    #p = Pool(os.cpu_count())
    fn = glob.glob(raw_data_dir + "/*/*/metadata_*")
    for f in fn:
        # if(f[:8]=='metadata'):
        with open(f, 'r') as load_f:
            metadata = json.load(load_f)
        gameid = metadata['gameid']
        movement = f[-7:-5]
        movement = movement.replace("_", "0")
        for team in ["home", "visitor"]:
            players = metadata[team]['players']
            movement_path = f.replace("metadata", "movement")
            gen_dir = COLLATED_DATA_DIR + "/" + gameid + "/" + movement + "/" + team
            os.makedirs(gen_dir, exist_ok=True)
            for player in players:
                #p.apply_async(player2trajectory, args=[movement_path, gen_dir, player['playerid']])
                player2trajectory(movement_path, gen_dir, player['playerid'])
    #p.close()


def player2trajectory(path, target_dir, player_id):  # ->[x,y]
    '''
    return : x, y and [x, y] trajectory for the player in certain round
    '''
    # load data
    # data_dir = os.listdir("data/test/")
    # for dir in data_dir:
    player = {}

    if not os.path.exists(path):
        return
    with open(path, 'r') as load_f:
        data = json.load(load_f)
    # print(len(data))

    data.sort(key=lambda x: x['game_clock'], reverse=True)
    # player_position = data['player_position']  #list
    px = []
    py = []
    pxy = []
    #print(data[0])
    for d in data:
        for p in d['player_position']:
            if p[1] == player_id:
                print(p[1])
                px.append(p[2])
                py.append(p[3])
                pxy.append([p[2], p[3]])
    dict = {'px': px, "py": py, "pxy": pxy}
    #print(len(px))
    #print(target_dir + "/" + "p_" + player_id)
    if len(px) == 0  or len(py) == 0 or len(pxy) == 0 :
        return
    with open(target_dir + "/" + "p_" + str(player_id), 'a+') as  f:
        json.dump(dict, f)
    return px, py, pxy




if __name__ == '__main__':
    #player2trajectory("data/test/31/movement_31.json", 203138)
    preprocess('data')