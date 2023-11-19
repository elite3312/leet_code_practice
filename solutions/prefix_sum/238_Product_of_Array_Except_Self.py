class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zero_index=[]#store index of elems with 0 as values
        p=1#product
        n=len(nums)

        for i in range(n):
            if nums[i]==0:zero_index.append(i)
            else:p*=nums[i]

        if len(zero_index)>1:return [0 for _ in range(n)]
        elif len(zero_index)==1:
            res= [0 for _ in range(n)]
            res[zero_index[0]]=p
            return res
        
        else:# has no 0 elems
            prefix_product=[0 for _ in range(n)]
            prefix_product[0]=nums[0]
            for i in range(1,n):
                prefix_product[i]=prefix_product[i-1]*nums[i]
            suffix_product=[0 for _ in range(n)]
            suffix_product[-1]=nums[-1]
            for i in range(1,n):
                suffix_product[-i-1]=suffix_product[-i]*nums[-i-1]
            res=[0 for _ in range(n)]
            res[0]=suffix_product[1]
            res[-1]=prefix_product[-2]
            for i in range(1,n-1):
                res[i]=prefix_product[i-1]*suffix_product[i+1]
            return res

                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    inp=[1,2,3,4]
    out=[24,12,8,6]
    test_driver(s.productExceptSelf,inp,expected=out)
# idea: res[i]=prefix_product[i-1]*suffix_product[i+1]