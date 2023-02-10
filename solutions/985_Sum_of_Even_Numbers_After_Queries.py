class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even_value_map=dict()
        sum_even_values=0
        for i in range(len(nums)):
            if nums[i] %2==0:
                even_value_map[i]=True
                sum_even_values+=nums[i]
            else:even_value_map[i]=False
        res=[]
        for q in queries:
            val=q[0]
            index=q[1]
            original_value=nums[index]
            if even_value_map[index]:
                sum_even_values-=original_value
            nums[index]+=val
            updated_val=nums[index]
            if updated_val%2==1:
                even_value_map[index]=False
            else:
                even_value_map[index]=True
                sum_even_values+=updated_val
            res.append(sum_even_values)
        return res
        
if __name__ == "__main__":
    
    s = Solution()
    #nums=[1,2,3,4]
    #queries = [[1,0],[-3,1],[-4,0],[2,3]]
    nums=[1]
    queries = [[4,0]]
    
    ans=s.sumEvenAfterQueries(nums,queries)
    print(ans)
    