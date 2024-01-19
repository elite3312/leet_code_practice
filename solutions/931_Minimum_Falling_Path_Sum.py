from utils.test_driver import test_driver

import heapq


class Solution:
    def minFallingPathSum_dfs(self, matrix: list[list[int]]) -> int:
        '''this will probrably tle'''

        n = len(matrix)
        costs = []

        def inner(row: int, cost: int, last_col):
            next_col = self.get_next_cols(row-1, last_col,  n)
            if next_col == None:
                costs.append(cost)
                return

            for col in next_col:
                inner(row+1,
                      cost+matrix[row][col], col)
        for col in range(n):
            inner(0, 0, col)
        return min(costs)

    def get_next_cols(self, row, col,  n):
        if row >= n-1:
            return None
        elif col == 0:
            if n > 1:
                return [0, 1]
            else:
                return [0]
        elif col == n-1:
            if n > 1:
                return [n-1, n-2]
            else:
                return [n-1]
        else:
            return [col-1, col, col+1]

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        res=1e7
        q = []
        if n<3:num=n
        else :num=n//2

        for col, cost in enumerate(matrix[0]):
            heapq.heappush(q, (cost, (0, col)))
        while len(q) > 0:
            accum_cost, (r, c) = heapq.heappop(q)

            children_cols = self.get_next_cols(r, c, n)
            if children_cols == None:
                # reached last row
                if num>0:
                    res=min(res,accum_cost)
                    num-=1
            else:
                child_row = r+1
                for child_col in children_cols:
                    heapq.heappush(
                        q, (accum_cost+matrix[child_row][child_col], (child_row, child_col)))
        return res

if __name__ == "__main__":
    s = Solution()

    tests = [
            [  # case 1
                # inputs
                [
                    [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
                ],
                # res
                13

            ],
        [  # case 2
                # inputs
                [
                    [[-19, 57], [- 40, -5]]
                ],
                # res
                -59

            ],
        [  # case 3
                # inputs
                [
                    [[-51,-35,74],[-62,14,-53],[94,61,-10]]
                ],
                # res
                -59

            ],

    ]
    for input, res in tests:
        test_driver(s.minFallingPathSum, input[0], expected=res)
