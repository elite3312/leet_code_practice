from utils.test_driver import test_driver_main
# from utils.linked_list import print_list
#from itertools import combinations
# from collections import Counter
# from collections import deque
class Solution:
    def maxEnergyBoost_tle(self, energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        #O(3^n)
        n=len(energyDrinkA)
        
        def inner(i,cur,drinkA):
            if i>n-1:
                return cur
            drink_from=energyDrinkB[i]
            if drinkA:
                drink_from=energyDrinkA[i]
                
            
                

            return max(inner(i+1,cur+drink_from,drinkA),
                       inner(i+1,cur,not drinkA))

        return max(inner(1,energyDrinkA[0],True),inner(1,energyDrinkB[0],False))
    def maxEnergyBoost(self,energyDrinkA: list[int], energyDrinkB: list[int]) -> int:
        #O(n)
        n=len(energyDrinkA)

        fromA = [energyDrinkA[0]]+[0 for i in range(n-1)]# dpA[i]=what you can gain at max by drinking from A at index i
        fromB = [energyDrinkB[0]]+[0 for i in range(n-1)]#dpB
        
        for i in range(1, n):
            from_prev_b=0
            if i>1:
                from_prev_b=fromB[i-2]
            fromA[i] = energyDrinkA[i] + max(fromA[i-1], from_prev_b )
            
            from_prev_a=0
            if i>1:
                from_prev_a=fromA[i-2]
            fromB[i] = energyDrinkB[i] + max(fromB[i-1], from_prev_a)
        
        return max(fromA[-1], fromB[-1])
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [
          [[1,3,1],[3,1,1]]  ,5
        ],
        [
            [[4,1,1],[1,1,3]],7
        ]
    ]

    test_driver_main(sol.maxEnergyBoost, tests, index)
