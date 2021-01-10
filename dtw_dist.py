import numpy as np
import matplotlib.pyplot as plt
from dtw import dtw
# ref: https://github.com/DynamicTimeWarping/dtw-python/tree/master/dtw

# def dtwdist(p, q):
#     alignment = dtw(p, q, keep_internals=True)
#     #plt.plot(p);
#     plt.plot(q);
#     #plt.plot(alignment.index1, alignment.index2)
#     #alignment.plot(type="threeway")
#     #plt.show()
#     print(alignment.distance)


def _trackeback(D):
    i, j = np.array(D.shape) - 1
    p, q = [i], [j]
    while (i > 0 and j > 0):
        tb = np.argmin((D[i - 1, j - 1], D[i - 1, j], D[i, j - 1]))

        if (tb == 0):
            i = i - 1
            j = j - 1
        elif (tb == 1):
            i = i - 1
        elif (tb == 2):
            j = j - 1

        p.insert(0, i)
        q.insert(0, j)
    p.insert(0, 0)
    q.insert(0, 0)
    return (np.array(p), np.array(q))


def my_dtw(class1_sample, class2_sample, plot=False, dist=lambda x, y: np.linalg.norm(x - y, ord=1)):
    """
    dwt (Dynamic Time Wraping) function computes the distance between unequal trajectories.
    It finds  a time warping that minimize the total distance between matching points
    @class1_sample: user1 matrix representinx a trajectory
    @class2_sample: user2 matrix representinx a trajectory
    """
    x = np.array(class1_sample)
    y = np.array(class2_sample)

    r, c = len(x), len(y)

    D = np.zeros((r + 1, c + 1))
    D[0, 1:] = np.inf
    D[1:, 0] = np.inf

    for i in range(r):
        for j in range(c):
            D[i + 1, j + 1] = dist(x[i], y[j])

    for i in range(r):
        for j in range(c):
            D[i + 1, j + 1] += min(D[i, j], D[i, j + 1],
                                   D[i + 1, j])

    D = D[1:, 1:]
    dist = D[-1, -1] / sum(D.shape)
    cost = D
    path = _trackeback(D)

    if plot:
        plt.imshow(cost.T, origin='lower', cmap='gray', interpolation='nearest')
        plt.plot(path[0], path[1], 'w')
        plt.xlim((-0.5, cost.shape[0] - 0.5))
        plt.ylim((-0.5, cost.shape[1] - 0.5))
        plt.show()

    return dist, cost, path

