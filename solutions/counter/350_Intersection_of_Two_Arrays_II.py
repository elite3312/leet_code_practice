from utils.test_driver import test_driver_main

from collections import Counter
# from collections import deque
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        cnter=Counter()
        for e in nums2:
            cnter[e]+=1
        res=[]
        for e in nums1:
            if cnter[e]>0:
                res.append(e)
                cnter[e]-=1
        return res
if __name__ == "__main__":
    sol = Solution()

    index =0

    tests = [
        [
            [[1,2,2,1],[2,2]],
            [2,2]
        ],
        [
            [[4,9,5],[9,4,9,8,4]],
            [4,9]
        ]
    ]

    test_driver_main(sol.intersect, tests, index)
