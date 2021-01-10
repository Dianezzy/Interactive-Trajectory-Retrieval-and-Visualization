
from utils import num2str
import numpy as np
from saxpy.sax import sax_via_window
from utils import SECOND_HALF

def LCSS(px, py, qx, qy):
    px_str, py_str = num2str(px, py)
    qx_str, qt_str = num2str(qx, qy)
    # for px in px_str:

    lcs_x = LCS(px_str, qx_str)
    lcs_y = LCS(py_str, qt_str)
    lcs = lcs_x * lcs_x + lcs_y * lcs_y
    return lcs


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





