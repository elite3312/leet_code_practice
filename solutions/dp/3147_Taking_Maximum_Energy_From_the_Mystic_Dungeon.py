
from utils.test_driver import test_driver

import heapq
class Solution:
    def maximumEnergy_dp(self, energy: list[int], k: int) -> int:
        n=len(energy)
        
        '''dp approach
        we partition enery into subsets using modular k
        e.g. 
                9-2-6-5-8 3 2
        index : 0 1 2 3 4 5 6, k=3
        subset: 0 1 2 0 1 2 0
        
        maintain dp entries for each subset 
                 0  1 2
            dp: 6 -2 3
        '''

        max_en_by_mod_k={}
        for i in range(k):max_en_by_mod_k[i]=energy[i]
        for i in range(k,n):
            #dp[i%k]    =        max(previous sum + current cell enery,discard previous sums and only retain current cell energy)
            # remember that the sums must be consecutive! This is why we can simply discard the previous sums as well as add up energy to the previous sums.
            max_en_by_mod_k[i%k]=max(max_en_by_mod_k[i%k]+energy[i],energy[i])
        # return the maximum entry in the dictionary
        return max([x[1] for x in max_en_by_mod_k.items()])
    def maximumEnergy_best_first_search(self, energy: list[int], k: int) -> int:
        
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
        [#1
            [
             [-2,-3,-1], 2
            ],
            -1
        ],
        [#2
            [
             [-9,-2,-6,-5,-8,3,0], 1
            ],
            3
        ],
    ]

    for input, res in tests[index:]:
        test_driver(sol.maximumEnergy_dp, input[0],input[1], expected=res)
