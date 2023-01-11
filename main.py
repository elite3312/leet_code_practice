class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        return 0
    def inner(self,n:int,index:int,nums:int,target:int):
        if index==0 :
            if target<nums[index]:return-1
        if index==n-1:
            if target>nums[index]:return-1
        if target== nums[index]:
            return index
        else:
            if target< nums[index]: 
                _lower_bound=0
                _upper_bound=n-1
                while True:
                    if nums[(_upper_bound-_lower_bound)//2]
                    
                return self.inner(index//2,nums,target)
            
            elif target>nums[index]: 
                return self.inner(n-index)//2+1,nums,target)
if __name__ == "__main__":
    sol=Solution()
    nums=[4,5,6,7,0,1,2]


    print(sol.search(nums))
    