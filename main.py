from utils.test_driver import test_driver

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n=len(nums)
        cur_max=-1
        cur_max_cnt=0
        for i in range(n):
            cur_max=max(cur_max,nums[i])
            
        
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
