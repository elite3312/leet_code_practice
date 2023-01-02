class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        pos_elems=[]
        d=dict()
        for elem in nums:
            d[elem]=True
            if elem >0 :
                pos_elems.append(elem)
        if len(pos_elems)==0 or len(pos_elems)==len(nums):return -1
        pos_elems.sort(reverse=True)
        for pos_elem in pos_elems:
            has_negative_counter_part=False
            try:
                if d[-pos_elem]:
                    has_negative_counter_part=True
            except:
                pass
            if has_negative_counter_part:
                return pos_elem

        return -1
        
                
        
            


if __name__ == "__main__":
    nums = [-1,10,6,7,-7,1]
    s=Solution()
    ans=Solution(nums)
    print(ans)