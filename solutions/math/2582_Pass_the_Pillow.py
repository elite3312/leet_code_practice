from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        '''
        case 0
        4 5 ->2

        0 1 2 3
        x x x x

        case 1
        3 2 ->3
        x x x
        '''
        # it takes n-1 times for the pillow to go from the first person to the last person
        laps=time//(n-1)
        pos=time % (n-1)

        if laps%2==1:
            # reverse dir
            res=n-1-pos
        else:
            res=pos
        return res+1
if __name__ == "__main__":
    sol = Solution()

    index =0

   
    tests=[
        [[4,5],
        2],
        [[3,2],
        3],
        [[2,1000],
        1]
    ]

    test_driver_main(sol.passThePillow, tests, index)
