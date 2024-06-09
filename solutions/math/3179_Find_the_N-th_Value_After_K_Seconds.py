from utils.test_driver import test_driver_main

# from collections import Counter
# from collections import deque 
import math

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        '''
        binomial sequence
                1
               1 1
              1 2 1 
             1 3 3 1 
            1 4 6 4 1
          1 5 10 10 5 1
         1 6 15 20 15 6 1
        binomial(x,y) gets you the yth col in the xth row

        example 1
        n=5, k=3
        (second : state)
        0: 1 1 1 1 1
        0: 1 2 3 4 5
        0: 1 3 6 10 15
        0: 1 4 10 20 35
        '''
        
        return math.comb(k+n-1, k)%int(1e9+7)# binomial(k+n-1,k)

if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [4,5],
            56
        ],
        [
            [5,3],
            35
        ],
        
    ]

    test_driver_main(sol.valueAfterKSeconds,tests,index)
