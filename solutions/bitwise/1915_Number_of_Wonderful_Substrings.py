from utils.test_driver import test_driver

'''
A wonderful string is a string where at most one letter appears an odd number of times.
Hint 1
For each prefix of the string, check which characters are of even frequency and which are not and represent it by a bitmask.
Hint 2
Find the other prefixes whose masks differs from the current prefix mask by at most one bit.

aba-a=ab
01 xor 10 =11, which is a valid substr
'''

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cur_bit_mask=0
        cnter={}
        cnter[0]=1#to account for mask 0000000000, it exists by default
        res=0
        for c in word:
            bit_index=ord(c)-ord('a')# 0 for a, 1 for b, etc
            cur_bit_mask^=(1<<bit_index)
            
            # case 0 : for each char, smaller prefix and larger prefix has same parity, which matches the target description: all chars appear even times
            if cur_bit_mask in cnter :
                substr=cur_bit_mask^0
                res+=cnter[substr]
                cnter[cur_bit_mask]+=1
            else :cnter[cur_bit_mask]=1

            # case 1 : exactly one char has odd parity
            for i in range(10):
                substr=cur_bit_mask^(1<<i)# let curmask differ by exactly one char in terms of parity
                if substr in cnter:
                    res+=cnter[substr]
                    # if for any char, the parity is 1, we have to find a existing record that has a parity 0 for said char, to create a odd substr
                    # if for any char, the parity is 0, we have to find a existing record that has a parity 1 for said char, to create a odd substr
        return res
if __name__ == "__main__":
    s = Solution()
    index=0

    word = "aba"
    res=4
    tests = [
        [
            # inputs
            [
               word
            ],
            # res
            4
        ],
       
        
    ]
    for input, res in tests[index:]:
        test_driver(s.wonderfulSubstrings, input[0],   expected=res)
