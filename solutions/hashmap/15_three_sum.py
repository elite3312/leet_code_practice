class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        d=dict()
        res=set()
        pos_start=0# index of 1st non-zero element
        _found_index=False
        zero_count=0# count zeroes in nums
        for i,elem in enumerate(nums):
            if elem >=0 and not _found_index:
                pos_start=i
                _found_index=True
            if elem==0:
                zero_count+=1
            d[elem]=i
        if zero_count==n:return [[0]*3]# nums is all zero
        elif zero_count>=3:
            res.add((0,0,0))
        for i in range(pos_start):
            for j in range(pos_start,n):
                if nums[j]>-nums[i]:break
                query_result=d.get(-(nums[i]+nums[j]))
                if query_result!=None and query_result!=j:
                    _l=[nums[i],nums[j],-(nums[i]+nums[j])]
                    _l.sort()
                    res.add((_l[0],_l[1],_l[2]))
        for i in range(n-1,pos_start-1,-1):
            for j in range(pos_start-1,-1,-1):
                if -nums[j]>nums[i]:break
                query_result=d.get(-(nums[i]+nums[j]))
                if query_result!=None and query_result!=j:
                    _l=[nums[i],nums[j],-(nums[i]+nums[j])]
                    _l.sort()
                    res.add((_l[0],_l[1],_l[2]))
        _res=[]
        for t in res:
            _l=[t[0],t[1],t[2]]
            _res.append(_l)
        return _res
if __name__ == "__main__":
    s=Solution()
    nums = [-1,0,1,2,-1,-4]# [[-1,-1,2],[-1,0,1]]
    print(s.threeSum(nums))
    #for i in range(5,2,-1):print(i)


    
    nums = [0,1,1]# []
    print(s.threeSum(nums))

    nums = [0,0,0]# []
    print(s.threeSum(nums))
    
    nums=[-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]#[[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]
    print(s.threeSum(nums))