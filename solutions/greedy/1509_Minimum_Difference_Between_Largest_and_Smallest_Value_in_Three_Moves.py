from utils.test_driver import test_driver_main
from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def minDifference_0(self, nums: list[int]) -> int:
        n=len(nums)
        if n<=4:return 0

        nums.sort()

        # The minimum difference possible is obtained by removing three elements between the three smallest and three largest values in the array.
        # 0 1 2 ... -3 -2 -1
        indexes=[
            0, 1, 2,n-3, n-2, n-1
        ]
        
        diffs=[]
        for comb in combinations(indexes,3):
            l=[]
            for i in range(n):
                if i not in comb:
                    l.append(nums[i])
            diffs.append(abs(l[0]-l[-1]))
        return  min(diffs)
    def minDifference_1(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        ans = nums[-1] - nums[0]
        '''
        0 1 2 , -3 -2 -1
        |     |
          |      |
            |       |
              |        |  
        '''
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        return ans
    def minDifference(self, nums: list[int]) -> int:
        def shift(arr:list,left_index:int):
            n=len(arr)
            for i in range(n-1,left_index,-1):
                arr[i]=arr[i-1]
        
        if len(nums) <= 4:
            return 0
        
        min4 = [float('inf')] * 4
        max4 = [float('-inf')] * 4

        for num in nums:
            added = False
            for j in range(4):
                if num < min4[j]:
                    shift(min4, j)
                    min4[j] = num
                    added = True
                    break
            if not added and min4[-1] == float('inf'):
                min4[-1] = num
        for num in nums:
            added = False
            for j in range(4):
                if num > max4[j]:
                    shift(max4, j)
                    max4[j] = num
                    added = True
                    break
            if not added and max4[-1] == float('-inf'):
                max4[-1] = num
        
        ans = max4[0] - min4[0]
        for i in range(4):
            ans = min(ans, max4[3 - i] - min4[i])
        
        return ans
if __name__ == "__main__":
    sol = Solution()

    index =1

    tests = [
        [
            [[5,3,2,4]],
            0
        ],
        [
            [[1,5,0,10,14]],
            1
            # 0 1 5 10 14
            # 
        ],
        [
            [[3,100,20]],
            0
        ]
    ]

    test_driver_main(sol.minDifference, tests, index)
