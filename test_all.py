
import sys
import os
import numpy as np
from frechetdist import frdist
from dtw_dist import *
from LCSS import LCSS

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

    # test LCSS
    p_t = [1.87, 2.83, 3.44, 4.56]
    p_x = [0.87, 2.87, 10.44, 2.56]
    p_y = [2.87, 0.83, 13.44, 7.56]
    q_t = [1.87, 2.83, 3.44, 4.56]
    q_x = [0.87, 2.87, 10.44, 2.56]
    q_y = [3.87, 1.83, 44.44, 8.56]
    dist = LCSS(p_t, p_x, p_y, q_t, q_x, q_y)
    print(dist) #very wrong






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
