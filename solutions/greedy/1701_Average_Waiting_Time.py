from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        '''
        customers[i]: (arrival time, cost)
        case 0
        time     0 1 2 3 4 5 6 7 8 9 10
        customer   0 0  
                     x 1 1 1 1 1
                         x x x x 2 2 2   
        case 1 
        time     0 1 2 3 4 5 6 7 8 9 1011121314151617181920
        customer           0 0
                           x x 1 1 1 1
                                     x 2 2 2
                                                         3
        '''
        cur_avail_time=-1
        wait_sum=0
        for arrival, cost in customers:
            if arrival>=cur_avail_time:
                cur_avail_time=arrival
            else:
                wait_sum+=cur_avail_time-arrival# x
            cur_avail_time+=cost
            wait_sum+=cost

        return wait_sum /len(customers)

if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[
            [[1, 2], [2, 5], [4, 3]]
        ],
            5.00000
        ],
        [[
            [[5, 2], [5, 4], [10, 3], [20, 1]]
        ],
            3.25000
        ],


    ]

    test_driver_main(sol.averageWaitingTime, tests, index)
