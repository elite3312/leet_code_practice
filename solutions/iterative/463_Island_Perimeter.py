from utils.test_driver import test_driver


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        for row in grid:
            print(row)
        m = len(grid)
        n = len(grid[0])
        overlap_edges = 0
        island_tiles = 0

        def is_valid(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            return True
        # find overlaps
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                else:
                    island_tiles += 1

                # check right
                if is_valid(i, j+1):
                    if grid[i][j+1] == 1:
                        overlap_edges += 1
                # check down
                if is_valid(i+1, j):
                    if grid[i+1][j] == 1:
                        overlap_edges += 1

        res = island_tiles*4-overlap_edges*2
        return res


if __name__ == "__main__":
    s = Solution()

    tests = [
        [[[
            [0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]
           ]
          ],
              16],

        [[[
            [1]
            ]
            ],
              4],
        [[[
            [0]
            ]
            ],
              0]
    ]
    for input, res in tests:
        test_driver(s.islandPerimeter, input[0], expected=res)
