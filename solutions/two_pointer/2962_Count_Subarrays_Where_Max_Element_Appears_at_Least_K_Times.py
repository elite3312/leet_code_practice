from utils.test_driver import test_driver
class Solution:
    def countSubarrays(self, nums, k):
        m = {}
        n = len(nums)
        a = max(nums)
        i = j = 0
        res = 0
        while j < n:
            m[nums[j]] = m.get(nums[j], 0) + 1#increment entry in dict
            while m.get(a, 0) >= k:
                res += n - j
                m[nums[i]] -= 1
                i += 1
            j += 1
        return res

            
        
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
