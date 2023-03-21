class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        res=0
        n=len(nums)
        curr_consecutize_zeroes=0

        for i in range(0,n):
            
            if nums[i]==0:
                # increment consecutize_zeroes
                curr_consecutize_zeroes+=1
                # for subarrays of len 1,2...consecutize_zeroes, increment by 1
                res+=curr_consecutize_zeroes
            else:
                # consecutize_zeroes is broken, set it to 0
                curr_consecutize_zeroes=0
            

        return res
if __name__ == "__main__":

    s = Solution()
    input1= [1,3,0,0,2,0,0,4]
    excepted=6
    ans = s.zeroFilledSubarray(input1)
    print("%d"%ans+' expected:%d'%excepted)

    input1= [0,0,0,2,0,0]
    excepted=9
    ans = s.zeroFilledSubarray(input1)
    print("%d"%ans+' expected:%d'%excepted)

    input1=  [2,10,2019]
    excepted=0
    ans = s.zeroFilledSubarray(input1)
    print("%d"%ans+' expected:%d'%excepted)
