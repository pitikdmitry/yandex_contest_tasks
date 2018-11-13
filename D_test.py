import unittest
from collections import Counter

from D import c_n_k_func, check_division_5


class TestStringMethods(unittest.TestCase):

    def test_5_on_end(self):
        N = "125"
        K = 1
        # counter = Counter()
        #
        # c_n_k = c_n_k_func(len(N), 2)
        # if len(N) <= 2:
        #     c_n_k_len_minus_one = -1
        # else:
        #     c_n_k_len_minus_one = c_n_k_func(len(N) - 1, 2)
        #
        # for c in N:
        #     num = int(c)
        #     counter[num] += 1
        #
        # res = check_division_5(N, K, counter, c_n_k, c_n_k_len_minus_one)
        # print(res)


if __name__ == '__main__':
    unittest.main()
