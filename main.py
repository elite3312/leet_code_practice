from utils.test_driver import test_driver

from cmath import sqrt
from collections import Counter
class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:return 1

   
        ctr=Counter()
        for num in nums:
            ctr[num] +=1
            
        res=0
        for k in ctr.keys():
            if k ==1 :continue# number 1 cannot be center
            #prev=k
            _res=1
            k=sqrt(k)

            while (ctr[k]>=2):
                _res+=2
                k=sqrt(k)
            res=max(res,_res)
        return res






        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                [1,3,2,4]
            ],
            # res
            1

        ],
        [
            # inputs
            [
              [5,4,1,2,2]
            ],
            # res
            3

        ],
        




    ]
    for input, res in tests:
        test_driver(s.maximumLength, input[0],  expected=res)
