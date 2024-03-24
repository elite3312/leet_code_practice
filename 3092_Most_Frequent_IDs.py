from utils.test_driver import test_driver

import heapq


class CustomItem:
    def __init__(self, priority:list, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        return self.priority[0] >= other.priority[0]
    
class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        cnter=dict()
        l=[]#(obj(cnt),val)
        n=len(nums)

        res=[]
        
        for i in range(n):
            is_first_time_2_add=False
            if cnter.get(nums[i])==None:
                cnter[nums[i]]=[0]
                is_first_time_2_add=True

            cnter[nums[i]][0]+=freq[i]
            if cnter[nums[i]][0]<0:cnter[nums[i]][0]=0
            
            if is_first_time_2_add:
                heapq.heappush(l,CustomItem(cnter[nums[i]],nums[i]))
      
            else:heapq.heapify(l)

            res.append(l[0].priority[0])
        return res

        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                [5,5,3],[2,-2,1]
            ],
            # res
            [2,0,1]

        ],
        [
            # inputs
            [
                [2,3,2,1],[3,2,-3,1]
            ],
            # res
            [3,3,2,2]

        ],
    
    ]
    for input, res in tests:
        test_driver(s.mostFrequentIDs, input[0],input[1],  expected=res)
