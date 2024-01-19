from utils.test_driver import test_driver




class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:pass
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
       

    ]
    for input, res in tests:
        test_driver(s.minFallingPathSum, input[0], expected=res)
