class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d={}
        for num in nums:
            if d.get(num)==None:d[num]=True
            else:return True
        return False
        

                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    nums = [2,2,4,3,2,5]
    output=True
    test_driver(s.containsDuplicate,nums,expected=output)
