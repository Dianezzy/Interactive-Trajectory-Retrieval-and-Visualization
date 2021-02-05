import numpy as np
import matplotlib.pyplot as plt
from SAX import *
s = SAX(18, 10)
SECONDS = 2
FRAME_PER_SECOND = 25
WINDOW_SIZE = SECONDS * FRAME_PER_SECOND # 24min  1440  # data[len]/2 : second_half
import heapq


# def num2str(px, py):
#     assert (len(py) == len(px)), "Unmatched trajectory size!"
#     px_list, px_index = s.sliding_window(px, WINDOW_SIZE)
#     py_list, py_index = s.sliding_window(py, WINDOW_SIZE)
#     print("px_list:",px_list)
#     print("px_index:",px_index)
#     px_str = ''
#     px_str = px_str.join(px_list)
#     py_str = ''
#     py_str = py_str.join(py_list)
#     return px_str, py_str

def sliding_window_num(x, windowSize = WINDOW_SIZE):
    overlap = windowSize - STEP
    moveSize = int(windowSize - overlap)
    if moveSize < 1:
        raise OverlapSpecifiedIsNotSmallerThanWindowSize()
    ptr = 0
    n = len(x)
    windowIndices = []
    Rep = []
    while ptr < n - windowSize + 1:
        thisSubRange = x[ptr:ptr + windowSize]
        Rep.append(thisSubRange)
        windowIndices.append((ptr, ptr + windowSize))
        ptr += moveSize
    return (Rep, windowIndices)


def smallestK(arr, k):
    if k > len(arr) or k == 0:
        return []
    heap = []
    for i in arr[:k]:
        heapq.heappush(heap, -i)
    for i in arr[k:]:
        if i < -heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, -i)
    result = []
    for i in range(k):
        result.append(-heapq.heappop(heap))
    return result[::-1]

def largestK(arr, k):
    if k > len(arr) or k == 0:
        return []
    heap = []
    for i in arr[:k]:
        heapq.heappush(heap, i)
    for i in arr[k:]:
        if i > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, i)
    result = []
    for i in range(k):
        result.append(heapq.heappop(heap))
    return result[::-1]



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

# def write_sliding_window(raw_data_dir)


if __name__ == '__main__':
    lst = [1,5,3,2,4,7]
    l, id = sliding_window_num(lst, 3)
    print(l)
    print(id)