import numpy as np


def calu_second_order(second_order):
    N = second_order.shape[0]
    res = np.zeros(N)
    for i in range(N):
        res_pre = 1
        res_post = 1
        for j in range(N):
            res_pre *= second_order[j][i+j-N]
            res_post *= second_order[j][N-1-i-j]
        res[i] = res_pre - res_post
    return res, np.sum(res)


if __name__ == '__main__':
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 2, 3, 4, 5], [2, 4, 8, 16, 32], [1, 1, 1, 1, 1], [1, 10, 100, 1000, 10000]])
    print(calu_second_order(b))
