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
            _res=1
            center=k
            center=sqrt(center)

            while (ctr[center]>=2):
                _res+=2
                center=sqrt(center)
            res=max(res,_res)
            pass
        res_=ctr[1]
        if res_%2==0:res_-=1
        return max(res,res_)






        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                [64,25,121,81,49,100,49,36,81,64,25,81,36,36,4,49,81,9,49,100,49,36,100,36,4,49,25,100,25,25,64,4,100,25,16,16,64,144,4,16,25,144,121,9,49,4,100,144,64,36,100,81,4,16,64,64,4,64,25,121,49,49,16,144,36,144,144,25,64,25,100,100,4,16,81,49,4,121,16,100,100,144,9,144,25,9,64,16,36,36,25,64,36,121,64,49,25,81,121,64]
                ],
            # res
            3

        ],
        [
            # inputs
            [
                [48841,358801,28561,18974736,4356,221,358801,599,13,4356,66,48841,28561,815730721,13,815730721,18974736,66,169,599,169,221]
            ],
            # res
            7

        ],
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
'''
1 use counter to count occurences
2 iterate thru the key of the counter
  while counter[key]>=2
    res+=2
    key=sqrt(key)
'''