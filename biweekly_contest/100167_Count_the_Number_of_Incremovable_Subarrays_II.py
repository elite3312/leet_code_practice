from utils.test_driver import test_driver


class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        pass

if __name__ == "__main__":
    s = Solution()

    tests = [
            [[1,2,3,4],10],
            [[6,5,7,8],7],
            [[8,7,6,6],3],
        ]
    for input, res in tests:
        test_driver(s.incremovableSubarrayCount, input, expected=res)
