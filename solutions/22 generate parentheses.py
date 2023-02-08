class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        #check all combinations with brute force
        res=[]
        N=2*n
    
        def inner(s):#s is a list
            if len(s)==N:
                if valid_s(s):
                    res.append("".join(s))
            else:
                s.append('(')
                inner(s)
                s.pop(-1)
                s.append(')')
                inner(s)
                s.pop(-1)

        def valid_s(s):
            _stack=[]
            for c in s:
                if c =='(':
                    _stack.append(c)
                else:
                    if len(_stack)==0:return False
                    _stack.pop()
            if len(_stack)>0:return False
            else: return True
        s=[]
        inner(s)
        return res


if __name__ == "__main__":
    
        #catalan(n+1)=for k in [0,n]:sum+=catalan(k)*catalan(n-k)
    s=Solution()
    
    n=3
    
    ans=s.generateParenthesis(n)
    print(ans)