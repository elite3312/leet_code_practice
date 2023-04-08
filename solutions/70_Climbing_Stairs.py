class Solution:
    def __init__(self) -> None:
        dp=[0]*46
        dp[1]=1
        dp[2]=2

        for i in range(3,46):
            dp[i]=dp[i-1]+dp[i-2]
        self.dp=dp
    def climbStairs(self, n: int) -> int:
        # dp[n]: ways of climbing n stairs, using steps 1 or 2 wide
        
        '''
        dp[1]= ["1"]
        dp[2]= ["2",
                "1,1"]
        dp[3]= ["1,1,1",
                "1,2",
                "2,1]
        dp[4]= dp[3]+dp[2]=5

        '''
        return self.dp [n]
if __name__ == "__main__":

    s = Solution()
    input1 = 2
    excepted = 2
    ans = s.climbStairs(input1)
    print("%d" % ans+' expected:%d' % excepted)
    input1 =3
    excepted = 3
    ans = s.climbStairs(input1)
    print("%d" % ans+' expected:%d' % excepted)
    input1 =45
    excepted = 1836311903
    ans = s.climbStairs(input1)
    print("%d" % ans+' expected:%d' % excepted)
class Solution_tle:
    def climbStairs(self, n: int) -> int:
        self.n=n
        self.res=0
        self.inner(0)
        return self.res
    def inner(self,curr_sum):
        if curr_sum==self.n:
            self.res+=1
            return
        elif curr_sum>self.n:
            return None
        
        else:
            self.inner(curr_sum+1)
            self.inner(curr_sum+2)