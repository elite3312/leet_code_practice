
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:return True
        mid=num//2
        for i in range(mid,num):
            a=i
            b=num-i
            if b==self.rev(a):return True
        return False

    def rev(self,num):
        n=num
        temp=n
        rev=0
        while(n>0):
            dig=n%10
            rev=rev*10+dig
            n=n//10
        return rev


if __name__ == "__main__":
    s=Solution()
    #n=443#true
    n=63#false
    #n=181#true
    
    ans=s.sumOfNumberAndReverse(n)
    print(ans)