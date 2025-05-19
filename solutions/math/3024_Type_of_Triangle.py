from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq
class Solution:
    def triangleType(self, nums: list[int]) -> str:
        """
        Given a list of integers, return the type of triangle that can be formed with the given sides.
        """
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if nums[0] == nums[1]and nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"
        elif nums[0]!= nums[1] and nums[1] != nums[2]:
            return "scalene"
        return "none"
        
        
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[[3,3,3]],"equilateral"],
        [[[3,4,5]],"scalene"],
        [[[2,2,3]],"isosceles"],
    ]

    test_driver_main(sol.triangleType   , tests, index)
