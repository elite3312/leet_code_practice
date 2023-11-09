class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res=0
        while n>0 : 
            if n & 1:res+=1
            n>>=1
        return res

def test_driver(s: Solution, *inputs, expected: str):
    # change this line
    ans = s.hammingWeight(*inputs)

    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
if __name__ == "__main__":
    s = Solution()
    test_driver(s,13,expected=3)
    