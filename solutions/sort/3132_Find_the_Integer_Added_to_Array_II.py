from utils.test_driver import test_driver
from itertools import combinations
# semi brute force: check all c(n,n-2) combinations for arr1, then look for consistent diff between arr1 and arr2
debug=False
class Solution:
    def minimumAddedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()
        n=len(nums1)
        # c(200 ,20)
        res=1e6
        for comb in list(combinations(range(n), 2)):
            cur=[]
            i=0
            check_failed=False

            is_first=True
            diff=None
            for j in range(n):
                if j not in comb:
                    cur.append(nums1[j])

                    if is_first:
                        diff=nums2[0]-cur[0]
                        is_first=False

                    elif nums2[i]-cur[i]!=diff:
                        check_failed=True
                        break
                    i+=1
            if check_failed:continue

            if debug:
                print(cur)
                print(nums2)
                print('\n')
      
            res=min(nums2[0]-cur[0],res)
 
        return res
        
        

if __name__ == "__main__":
    s = Solution()
    index=0
    nums1 = [4,20,16,12,8]
    nums2 = [14,18,10]
    res=-2
    tests = [
        [
            # inputs
            [
              nums1,nums2
            ],
            # res
            res
            
        ],
       
        [
            # inputs
            [
              [4,6,3,1,4,2,10,9,5],[5,10,3,2,6,1,9]
            ],
            # res
            0
        ],
        [
            # inputs
            [
              [4,7,5],[5]
            ],
            # res
            -2
        ]
    ]
    for input, res in tests[index:]:
        test_driver(s.minimumAddedInteger, input[0],input[1],   expected=res)
