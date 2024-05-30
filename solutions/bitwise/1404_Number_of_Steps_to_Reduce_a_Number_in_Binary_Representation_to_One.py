from collections import deque
from utils.test_driver import test_driver
class Solution:
    '''
    If the current number is even, you have to divide it by 2.
    If the current number is odd, you have to add 1 to it.
    '''
    def add_one(self,s:deque):
        '''
        100100
        '''
       
        n=len(s)
        carry=1
        cur=n-1
        while cur >=0:
            if s[cur]=='1' and carry:
                s[cur]='0'
            else:
                s[cur]='1'
                carry=0
                break
            cur-=1
        if carry:
            s.appendleft('1')
        return s
    def numSteps(self, s: str) -> int:
        l=deque(s)
        res=0
        while not (len(l)==1 and l[0]=='1'):
            res+=1
            if l[-1]=='1':
                self.add_one(l)
            else:
                l.pop()
           
        return res


if __name__ == "__main__":
    sol = Solution()

    index = 0


    tests = [
        [
            [
                "1101"
            ],
            6
        ],
        [
            [
                "10"
            ],
            1
        ],
        
        
        [
            [
                "1"
            ],
            0
        ],
       
        
    ]

    fail_cnt=0
    for input, res in tests[index:]:
        if not test_driver(sol.numSteps, input[0], expected=res):
            fail_cnt+=1
    if fail_cnt>0:
        print("%d tests failed"%fail_cnt)

