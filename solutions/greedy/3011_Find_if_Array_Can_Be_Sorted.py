from utils.test_driver import test_driver




class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        n=len(nums)
        # base case
        is_sorted=True
        for i in range (n-1):
            if nums[i]>nums[i+1]:is_sorted=False
        if is_sorted:return True

        partitions=[]
        last_set_bit_count=-1
        cur_partition=None
        for num in nums:
            set_bit_count=self.get_set_bit_count(num)
            if set_bit_count!=last_set_bit_count:
                cur_partition=[]
                partitions.append(cur_partition)
            cur_partition.append(num)
            last_set_bit_count=set_bit_count
        
        
        
        last_max=-1
        for partition in partitions:
            _min=1<<9
            _max=-1
            for num in partition:
                if _min>num:_min=num
                if _max<num:_max=num
            if last_max>_min:return False
            last_max=_max
        return True
            
    def get_set_bit_count(self,num):
        res=0
        while num>0:
            if num%2==1:res+=1
            num>>=1
        return res



        

        
if __name__ == "__main__":
    s = Solution()

    tests = [
            [  # case 1
                # inputs
                [
                   [8,4,2,30,15]
                ],
                # res
                True

            ],
            [  # case 2
                # inputs
                [
                   [1,2,3]
                ],
                # res
                True

            ],
            [  # case 3
                # inputs
                [
                   [3,16,8,4,2]
                ],
                # res
                False

            ],
       

    ]
    for input, res in tests:
        test_driver(s.canSortArray, input[0], expected=res)
'''
idea
partition array according to number of set bits
then check if the max of partitions[i] is less than the min of partitions[i+1] 
'''