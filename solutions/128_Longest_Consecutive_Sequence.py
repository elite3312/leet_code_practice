class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:# starting point, e.g. the lowest number
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.longestConsecutive(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)

if __name__ == "__main__":
    '''
    0 <= nums.length <= 105
    1e-9 <= nums[i] <= 1e9
    '''
    s = Solution()

    # 1234
    test_driver(s,[100,4,200,1,3,2],None,4)

    test_driver(s,[0,3,7,2,5,8,4,6,0,1],None,9)
    
    
