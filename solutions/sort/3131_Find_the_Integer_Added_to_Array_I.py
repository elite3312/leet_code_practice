from utils.test_driver import test_driver

class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()
        return nums2[0]-nums1[0]
        
        

if __name__ == "__main__":
    s = Solution()

    nums1 = [2,6,4]
    nums2 = [9,7,5]
    res=3
    tests = [
        [
            # inputs
            [
              nums1,nums2
            ],
            # res
            3
        ],
       
        
    ]
    for input, res in tests:
        test_driver(s.addedInteger, input[0],input[1],   expected=res)
