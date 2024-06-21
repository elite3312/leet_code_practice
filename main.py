from utils.test_driver import test_driver_main

# from collections import Counter
# from collections import deque
import bisect
class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        n = len(position)
        position.sort()

        if m == 2:
            return position[-1]-position[0]
        
        def inner(left_index, right_index, balls):
            if (right_index-left_index)==1:return position[right_index]- position[left_index]

            balls += 1
            mid = (position[left_index]+position[right_index])//2

            mid_index = bisect.bisect_left(position[left_index:right_index], mid)+left_index# this finds the first index i such that everything in positions starting from i is greater than or equal to mid
            if mid_index==right_index:
                mid_index-=1
            elif mid_index==left_index:
                mid_index+=1
            
            if balls == m:
                return max(position[mid_index]-position[left_index], position[right_index]-position[mid_index])
            else:
                return max(inner(left_index, mid_index,balls), inner(mid_index, right_index,balls))
        return inner(0, n-1, 2)


if __name__ == "__main__":
    sol = Solution()

    index =0

    tests = [
        [
            [[1, 2, 3, 4, 7], 3],
            3
        ],
        [
            [[5, 4, 3, 2, 1, 1000000000], 2], 999999999
        ],
        [
            [[ 1,2,3, 100], 3], 97
        ],
        [
            [[ 1,2,3,7,17, 100], 4], 83
        ],
        [
            [[79,74,57,22], 4], 5
        ]
    ]

    test_driver_main(sol.maxDistance, tests, index)
