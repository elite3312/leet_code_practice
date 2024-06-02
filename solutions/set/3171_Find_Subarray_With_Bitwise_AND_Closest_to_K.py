from utils.test_driver import test_driver
#from collections import deque
#from collections import defaultdict
#import heapq
class Solution:
    def minimumDifference_naive(self, nums: list[int], k: int) -> int:
    
        n = len(nums)
        min_diff = float('inf')
        
        for start in range(n):
            current_and = nums[start]
            for end in range(start, n):
                if end > start:
                    current_and &= nums[end]
                min_diff = min(min_diff, abs(k - current_and))
                if min_diff == 0:
                    return 0  # Early exit if the minimum possible difference is found

        return min_diff

    def minimumDifference(self, nums: list[int], k: int) -> int:
        '''
        idea: use a set to maintain the distinct bitwise and of subarrays
        '''
        cur = nums[0]
        res = abs(k - cur)
        s = set([nums[0]])
        for i in nums[1:]:
            res = min(res, abs(k-i))
            cur_s = set()
            cur_s.add(i)
            for j in s:
                cur = j&i
                res = min(res, abs(k-cur))
                cur_s.add(cur)
            s = cur_s
        return res
if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
              [1,2,4,5], 3
            ],
           1#4-3
        ],
        [
            [[1,2,1,2] ,2]
            ,
           0
        ],
        [
            [[1],10]
            ,
           9
        ],
      
        
        
       
        
    ]

    fail_cnt=0
    for input, res in tests[index:]:
        if not test_driver(sol.minimumDifference, input[0], input[1],expected=res):
            fail_cnt+=1
    if fail_cnt>0:
        print("%d tests failed"%fail_cnt)

