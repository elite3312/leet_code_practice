from utils.test_driver import test_driver
'''
010
001
011
100
res=1+1=2
(make the number of 1 bits in the 0th bit odd, and the number of 1 bits in the 2nd bit even)
'''
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        

        ones_cnt=[0 for _ in range(32)]# cnt 1s, lower bits to higher bits

        for num in nums:
            bin_num=bin(num)[2:]
            n=len(bin_num)
            for i in range(n):
                if bin_num[-(i+1)]=='1':
                    ones_cnt[i]+=1

        bin_k=list(bin(k)[2:])
        remain=32-len(bin_k)
        bin_k=['0' for _ in range(remain)]+bin_k
        res=0
        for i in range(32):
            if bin_k[-(i+1)]=='1':
                if ones_cnt[i]%2==0:res+=1
            else:
                if ones_cnt[i]%2==1:res+=1
        return res

            


if __name__ == "__main__":
    s = Solution()

    nums = [2,1,3,4]
    k = 1
    tests = [
        [
            # inputs
            [
               nums,k
            ],
            # res
            2
        ],
        [
            # inputs
            [
               [2],1
            ],
            # res
            2
        ],
        
    ]
    for input, res in tests:
        test_driver(s.minOperations, input[0], input[1],  expected=res)
