from utils.test_driver import test_driver_main


# from collections import Counter
# from collections import deque
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sorted_heights=sorted(heights)
        n =len (heights)
        res=0
        for i in range(n):
            if sorted_heights[i]!=heights[i]:res+=1
        return res
        
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [
            [[1,1,4,2,1,3]], 
            3
        ],
    ]

    test_driver_main(sol.heightChecker, tests, index)
