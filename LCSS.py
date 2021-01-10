
from utils import _num2str, _get_list

def LCSS( pt, px, py, qt, qx, qy):
    px_str, py_str = _num2str(pt, px, py)
    qx_str, qt_str = _num2str(qt, qx, qy)
    lcs_x = LCS(px_str, qx_str)
    lcs_y = LCS(py_str, qt_str)
    lcs = lcs_x * lcs_x + lcs_y * lcs_y
    return lcs


def LCS(str1, str2) :
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]



