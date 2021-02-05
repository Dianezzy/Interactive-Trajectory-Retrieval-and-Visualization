from SAX import *
s = SAX(18, 10)
SECONDS = 2
FRAME_PER_SECOND = 25
WINDOW_SIZE = SECONDS * FRAME_PER_SECOND # 24min  1440  # data[len]/2 : second_half
from utils import largestK
import numpy as np
from utils import *
import json
lcss2tag = {}
import subprocess
from multiprocessing.pool import Pool


def LCSS(query, dataset, chosen_index):
    global lcss2tag
    p = Pool(os.cpu_count())
    with open(query, 'r') as load_f:
        data = json.load(load_f)
    px, py= data['px'], data['py']
    px_list, px_index = s.sliding_window(px, WINDOW_SIZE)
    py_list, py_index = s.sliding_window(py, WINDOW_SIZE)
    trg_x = px_list[chosen_index]
    trg_y = py_list[chosen_index]
    candiadates=[]
    for f in dataset:
        #res = (p.apply_async(_LCSS, args=[trg_x, trg_y, f]))
        lcss, tag = (p.apply_async(_LCSS, args=[trg_x, trg_y, f])).get()
        for l, t in zip(lcss, tag):
            if (l not in lcss2tag):
                lcss2tag[l] = []
            lcss2tag[l].append(t)
        #res = _LCSS(trg_x, trg_y, f)
        # candiadates = candiadates + res
    # candiadates = largestK(candiadates, 10)
    p.close()
    p.join()

    return candiadates



    # for px in px_str:

    # lcs_x = LCS(px_str, qx_str)
    # lcs_y = LCS(py_str, qt_str)
    # lcs = lcs_x * lcs_x + lcs_y * lcs_y
    # return lcs
    # qx_list, qx_index = s.sliding_window(qx, WINDOW_SIZE)
    # qy_list, qy_index = s.sliding_window(qy, WINDOW_SIZE)
    # simi_x = LCSS()
    #
    # for f in fn:
    #     trajectories = []
    #
    #     for f in fn:
    #
    #
    # with open(f, 'r') as nf:
    #     ndata = json.load(nf)
    #     qx, qy, qxy = ndata['px'], ndata['py'], ndata['pxy']
    # assert (len(py) == len(px) and len(qy) == len(qx)), "Unmatched trajectory size!"

def _LCSS(trg_x, trg_y, f):
    #global lcss2tag
    with open(f, 'r') as fl:
        ndata = json.load(fl)
    qx, qy = ndata['px'], ndata['py']
    qx_list, qx_index = s.sliding_window(qx, WINDOW_SIZE)
    qy_list, qy_index = s.sliding_window(qy, WINDOW_SIZE)
    lst = []
    tag = []
    for i in range(len(qx_list)):
        str_x = qx_list[i]
        str_y = qy_list[i]
        simi_x = LCS(trg_x, str_x)
        simi_y = LCS(trg_y, str_y)
        start = str(qx_index[i][0])
        end = str(qx_index[i][1])
        simi = simi_x * simi_x + simi_y * simi_y
        tag.append(f.split("/")[-1]+"_"+start+"_"+end)
        # lcss2tag.update({simi:tag})

        lst.append(simi)
    # res = largestK(lst, min(8,int(2*len(qx_list)/3)))
    return lst, tag
# def LCS(str1, str2) :
#     print(str1, str2)
#     m, n = len(str1), len(str2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = 1 + dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
#     return dp[-1][-1]

def LCS(text1, text2):
    if not text1 or not text2:
        return 0
    m, n = len(text1), len(text2)
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 if text1[0] == text2[0] else 0
    for i in range(1, m):
        dp[i][0] = 1 if text1[i] == text2[0] else dp[i - 1][0]
    for j in range(1, n):
        dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j - 1]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            if text1[i] == text2[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    return dp[m - 1][n - 1]


# def LCSS_v2(pxy, qxy):
#     pxy = np.array(pxy)
#     qxy = np.array(qxy)
#     print(pxy.shape)
#     pxy_str = sax_via_window(pxy, win_size=SECOND_HALF, paa_size=18, alphabet_size=10, nr_strategy='independent')
#     qxy_str = sax_via_window(qxy, win_size=SECOND_HALF, paa_size=18, alphabet_size=10, nr_strategy='independent')
#     print(pxy_str)
#     print(qxy_str)
#     similarity = LCS(pxy_str, qxy_str)
#     return similarity





