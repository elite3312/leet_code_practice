
from utils.test_driver import test_driver

import heapq
class Solution:
    def maximumEnergy_dp(self, energy: list[int], k: int) -> int:
        n=len(energy)
        
        dp=[[-1 for _ in range (n)]for _ in range (n)]
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        
        n=len(energy)
        
        h=[(-energy[i],i) for i in range(n)]#(priority,index),priority is the cur sum
        heapq.heapify(h)
        max_gained=-1e9

        trees_cnt=0
        while h:
            cur=heapq.heappop(h)

            cur_en=-cur[0]
            cur_index=cur[1]
            # append the child nodes of cur
            if cur_index+k<n:
                next_index=cur_index+k
                next_en=cur_en+energy[cur_index+k]
                heapq.heappush(h,(-next_en,next_index))
            else:
                max_gained=max(max_gained,cur_en)
                trees_cnt+=1
                if trees_cnt>(n*3/4):return max_gained
                
        return max_gained
    def maximumEnergy_naive(self, energy: list[int], k: int) -> int:
        n=len(energy)

        max_gained=-1e9
        for i in range(n):
            cur=i
            cur_energy=0
            while cur<n:
                cur_energy+=energy[cur]
                cur+=k
            max_gained=max(max_gained,cur_energy)
        return max_gained
              


if __name__ == "__main__":
    sol = Solution()

    index = 0

    energy = [5,2,-10,-5,1]
    k = 3
    res = 3
    tests = [
        [#0
            [
            energy,k
            ],
            res
        ],
        [#0
            [
             [-2,-3,-1], 2
            ],
            -1
        ],
        [#0
            [
             [-9,-2,-6,-5,-8,3,0], 1
            ],
            3
        ],
    ]

    for input, res in tests[index:]:
        test_driver(sol.maximumEnergy, input[0],input[1], expected=res)
