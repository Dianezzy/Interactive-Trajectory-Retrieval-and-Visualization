import numpy as np
import matplotlib.pyplot as plt
from SAX import *
s = SAX(18, 18)


def _num2str(pt, px, py):
    assert (len(pt) == len(px) and len(pt) == len(py)), "Unmatched trajectory size!"
    ptx = _get_list(pt, px, len(pt))
    pty = _get_list(pt, py, len(pt))
    px_str, px_index = s.to_letter_rep(ptx)
    py_str, py_index = s.to_letter_rep(pty)
    print("pxstr:",px_str)
    print("pxindex:",px_index)
    print("pystr:",py_str)
    print("pyindex:",py_index)
    return px_str, py_str




def _get_list(x, y, len):
    l = np.polyfit(x, y, 3)
    res = []
    for i in range(len):
        ele = np.polyval(l, i)
        res.append(ele)

    # draw
    plt.plot(x, y, 'b^', label='f(x)')
    plt.plot(x, res, 'r.', label='regression')

    return res


