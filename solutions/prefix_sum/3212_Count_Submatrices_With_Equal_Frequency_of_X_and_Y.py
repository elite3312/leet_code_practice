from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque


class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:

        m, n = len(grid), len(grid[0])

        pref_sum = {}
        for val in ['X', "Y", "."]:
            # X_pref_sum[i][j]=sum of x for matrix[0:i][0:j]
            pref_sum[val] = [[0 for j in range(n+1)]for i in range(m+1)]

        a = grid[0][0]
        res = 0
        for i in range(m):
            for j in range(n):
                for val in ['X', "Y", "."]:
                    pref_sum[val][i+1][j+1] = pref_sum[val][i+1][j] +\
                        pref_sum[val][i][j+1]-pref_sum[val][i][j] +\
                        int(grid[i][j] == val)

                if pref_sum["X"][i+1][j+1] == pref_sum["Y"][i+1][j+1] \
                        and pref_sum[a][i+1][j+1] > 0 \
                        and pref_sum['X'][i+1][j+1] > 0:
                    res += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    index = 2

    tests = [
        [[[["X", "Y", "."],
           ["Y", ".", "."]]],
         3
         ],
        [[[[".", "Y", "."],
           ["Y", "X", "."]]],
         1
         ],
        [[[[".", "."], [".", "."]]],
         0

         ]

    ]

    test_driver_main(sol.numberOfSubmatrices, tests, index)
