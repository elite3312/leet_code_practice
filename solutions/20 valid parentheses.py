class Solution:
    def isValid(self, s: str) -> bool:
        _stack=[]
        for c in s:
            if len(_stack)>0:
                
                if c==')' and _stack[-1]=='(':_stack.pop(-1)
                elif c==']' and _stack[-1]=='[':_stack.pop(-1)
                elif c=='}' and _stack[-1]=='{':_stack.pop(-1)
                else:
                    _stack.append(c)
            else:_stack.append(c)
        if len(_stack)==0:return True
        return False
            

if __name__ == "__main__":
    sol=Solution()
    
    s = "[])"#false
    s = "()"#true
    s="()[]{}"#true
    s="[()]s{}"#true
    print(sol.isValid(s))
    