class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        my_dict={}
        for elem in nums:
            my_dict[elem]=0
        for elem in nums:
            my_dict[elem]+=1
           
        for k in my_dict.keys():
            if my_dict[k]%2!=0:return False
        return True
if __name__ == "__main__":
    accounts = [1,2,3,3,2,1]
    s=Solution()

    print(s.divideArray(accounts))