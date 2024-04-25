from utils.test_driver import test_driver

class Solution:
    def __init__(self) -> None:
        d={}
        d[0]=0
        d[1]=1
        d[2]=1
        for i in range(3,38):
            d[i]=d[i-1]+d[i-2]+d[i-3]
        self.mem=d

    def tribonacci_tle(self, n: int) -> int:
        if n==0:return 0
        elif n==1:return 1 
        elif n==2:return 1
        else :return self.tribonacci_tle(n-1)+self.tribonacci_tle(n-2)+self.tribonacci_tle(n-3)

    def tribonacci(self, n: int) -> int:
        return self.mem[n]
        

if __name__ == "__main__":
    s = Solution()

    
    tests = [
        [
            # inputs
            [
               4
            ],
            # res
            4
        ],
       
        
    ]
    for input, res in tests:
        test_driver(s.tribonacci, input[0],   expected=res)
