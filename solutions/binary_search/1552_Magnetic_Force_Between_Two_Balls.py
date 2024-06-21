from utils.test_driver import test_driver_main

# from collections import Counter
# from collections import deque
class Solution(object):
    def maxDistance(self, position:list, m:int):
        position.sort()
        lo, hi = 1, (position[-1] - position[0]) // (m - 1)
        res = 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.canPlace(position, mid, m):
                # go to the right block, higher
                res = mid
                lo = mid + 1
            else:
                # go to the left block, lower
                hi = mid - 1
        
        return res
    
    def canPlace(self, arr, dist, balls):
        # place the first ball at the left
        countBalls = 1
        lastPlaced = arr[0]

        # go to the right by dist each time
        for i in range(1, len(arr)):
            if arr[i] - lastPlaced >= dist:
                countBalls += 1
                lastPlaced = arr[i]
            else:pass# go to the next position
            if countBalls >= balls:
                return True
        return False
        


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
            [[ 1,2,3, 100], 3], 2
        ],
        [
            [[ 1,2,3,7,17, 100], 4], 6
        ],
        [
            [[79,74,57,22], 4], 5
        ]
    ]

    test_driver_main(sol.maxDistance, tests, index)
