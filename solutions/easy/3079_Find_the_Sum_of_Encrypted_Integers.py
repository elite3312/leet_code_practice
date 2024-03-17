from utils.test_driver import test_driver

class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        
        res=0
        for num in nums:
            num_s=str(num)
            max_digit=0
            for d in num_s:
                _=int(d)
                if max_digit<_:max_digit=_
            sum_=0
            for d in num_s:
                sum_+=max_digit
                sum_*=10
            res+=sum_/10
        return int(res)



        
if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
                [10,21,31]
            ],
            # res
            66

        ],

    ]
    for input, res in tests:
        test_driver(s.sumOfEncryptedInt, input[0],  expected=res)
