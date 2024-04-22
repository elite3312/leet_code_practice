from utils.test_driver import test_driver

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        # use a sliding window
        pass
        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                [1,3,2,3,3],2
            ],
            # res
            6

        ],
        [
            # inputs
            [
                [1,4,2,1],  3
            ],
            # res
            0

        ],
    
    ]
    for input, res in tests:
        test_driver(s.countSubarrays, input[0],input[1],  expected=res)
