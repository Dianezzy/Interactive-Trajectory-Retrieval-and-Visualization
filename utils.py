import numpy as np
import matplotlib.pyplot as plt
from SAX import *
s = SAX(18, 10)
SECOND_HALF = 325 # 24min  1440  # data[len]/2 : second_half

def num2str(px, py):
    assert (len(py) == len(px)), "Unmatched trajectory size!"
    px_list, px_index = s.sliding_window(px, SECOND_HALF)
    py_list, py_index = s.sliding_window(py, SECOND_HALF)
    px_str = ''
    px_str = px_str.join(px_list)
    py_str = ''
    py_str = py_str.join(py_list)
    return px_str, py_str





#
# def _get_list(x, y, len):
#     l = np.polyfit(x, y, 3)
#     res = []
#     for i in range(len):
#         ele = np.polyval(l, i)
#         res.append(ele)
#
#     # draw
#     plt.plot(x, y, 'b^', label='f(x)')
#     plt.plot(x, res, 'r.', label='regression')
#
#     return res


