from utils import num2str
import numpy as np
from utils import WINDOW_SIZE

def edit_dist(px, py, qx, qy):
    px_str, py_str = num2str(px, py)
    qx_str, qt_str = num2str(qx, qy)
    # for px in px_str:

    edit_x = _edit_dist(px_str, qx_str)
    edit_y = _edit_dist(py_str, qt_str)
    edit = edit_x * edit_x + edit_y * edit_y
    return edit


def _edit_dist(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    n = len(word1)
    m = len(word2)
    if n * m == 0:
        return n + m

    D = [ [0] * (m + 1) for _ in range(n + 1)]

    # initialize
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j

    # dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left = D[i - 1][j] + 1
            down = D[i][j - 1] + 1
            left_down = D[i - 1][j - 1]
            if word1[i - 1] != word2[j - 1]:
                left_down += 1
            D[i][j] = min(left, down, left_down)

    return D[n][m]
