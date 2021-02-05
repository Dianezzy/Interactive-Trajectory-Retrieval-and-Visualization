
import sys
import os
import numpy as np
from frechetdist import frdist
from preprocess import player2trajectory
from dtw_dist import *
from LCSS import LCSS
from edit_dist import edit_dist

from frechetdist import frdist

TEST_CASES = [

    {
        'P': [[1, 1], [2, 1], [2, 2]],
        'Q': [[2, 2], [0, 1], [2, 4]],
        'expected': 2.0
    },

    {
        'P': np.array((np.linspace(0.0, 1.0, 100), np.ones(100))).T,
        'Q': np.array((np.linspace(0.0, 1.0, 100), np.ones(100))).T,
        'expected': 0
    },

    {
        'P': [[-1, 0], [0, 1], [1, 0], [0, -1]],
        'Q': [[-2, 0], [0, 2], [2, 0], [0, -2]],
        'expected': 1.0
    },

    {
        'P': np.array((np.linspace(0.0, 1.0, 100), np.ones(100)*2)).T,
        'Q': np.array((np.linspace(0.0, 1.0, 100), np.ones(100))).T,
        'expected': 1.0
    }

]


def test_main():

    # # test frechet dist
    # for test_case in TEST_CASES:
    #     P = test_case['P']
    #     Q = test_case['Q']
    #     # assert frdist(P, Q) == eo
    #     dtwdist(P, Q)


    # # test dtw dist
    # p = [[0,1,1], [1,2,1], [2,2,2], [3,3,3]]
    # q = [[0, 1, 2], [1, 2, 2], [2, 2, 3], [3, 3, 4]]
    # dist, _, _ = my_dtw(p, q)
    # print(dist)

    # test LCSS & edit distance
    px, py, pxy = player2trajectory("data/test/31/movement_31.json", 203138)
    qx, qy, qxy = player2trajectory("data/test/31/movement_31.json", 203477)
    #similarity1 = LCSS(px, py, qx, qy)
    similarity1 = edit_dist(px, py, qx, qy)
    print(similarity1)

    # similarity2 = LCSS_v2(pxy, qxy)
    # print("res:",similarity2)






#
# def test_errors():
#
#     P = [[1, 1], [2, 1]]
#     Q = [[2, 2], [0, 1], [2, 4]]
#
#     with pytest.raises(ValueError):
#         assert frdist(P, Q) == 2.0
#
#     P = []
#     Q = [[2, 2], [0, 1], [2, 4]]
#
#     with pytest.raises(ValueError):
#         assert frdist(P, Q) == 2.0


if __name__ == '__main__':
        test_main()
