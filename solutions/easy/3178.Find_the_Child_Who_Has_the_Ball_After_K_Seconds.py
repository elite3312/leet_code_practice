from utils.test_driver import test_driver_main


# from collections import Counter
# from collections import deque 
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        to_add=1
        cur_pos=0
        for i in range(k):
            cur_pos+=to_add
            if cur_pos==n-1:to_add=-1
            elif cur_pos==0:to_add=1
        return cur_pos
if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [3,5],
            1
        ],
        [
            [5,6],
            2
        ],
        
    ]

    test_driver_main(sol.numberOfChild,tests,index)
