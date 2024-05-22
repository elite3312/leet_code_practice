
from utils.test_driver import test_driver
#prefix sum
class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n=len(nums)

        arr=[0 for _ in range (n)]
        arr[0]=1
        for i in range(1,n):
            if nums[i]%2!=nums[i-1]%2:arr[i]=1# arr[i]=1 iff nums[i]%2 != nums[i-1]%2

        #now that we have this arr, we can create a prefix_sum_arr for fast query of valid intervals

        prefix_sum=[arr[0]]
        for v in arr[1:]:prefix_sum.append(v+prefix_sum[-1])

        res=[]
        for q in queries:
            i,j=q
            if (j-i)==(prefix_sum[j]-prefix_sum[i]):res.append(True)
            else:res.append(False)
        return res
        




        
              


if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
                [3,7,8],[[0,2]]
            ],
            [False]
        ],
        [
            [
                [2,7,2],[[0,0],[1,2]]
            ],
            [True,True]
        ],
        [
            [
                [1,1,2,3,2,1],[[0,1]]
            ],
            [False]
        ],
        [
            [
            [4,3,1,6],[[0,2],[2,3]]
            ],
            [False,True]
        ],
      
        
    ]

    fail_cnt=0
    for input, res in tests[index:]:
        if not test_driver(sol.isArraySpecial, input[0],input[1], expected=res):
            fail_cnt+=1
    if fail_cnt>0:
        print("%d tests failed"%fail_cnt)

