import math
class SolutionTLE:
    def minOperations(self, n: int) -> int:
        self.pows_of_two=dict()
        self.max_pow=14#14
        
        self.res=1000000

        
        self.inner(n,0,0)
        return self.res
    def inner(self, curr_num=39,curr_pow=0,pows_taken=0):
        if self.pows_of_two.get(curr_num):
            self.res=min(self.res,pows_taken+1)
            return
        elif curr_pow>self.max_pow:
            return False
        self.inner(curr_num+math.pow(2,curr_pow),curr_pow+1,pows_taken+1)
        
        self.inner(curr_num-math.pow(2,curr_pow),curr_pow+1,pows_taken+1)
        
        self.inner(curr_num,curr_pow+1,pows_taken)
class Solution:
    def minOperations(self, n: int) -> int:
        # greedy, always jump to the closet pows of 2
        pows_of_two=[]
        max_pow=20
        for i in range(max_pow):
            pows_of_two.append(math.pow(2,i))
        curr=n
        res=0
        while curr:
            _diff=float('inf')
            _closet_pow=None
            for p in pows_of_two:
                if abs(curr-p)<_diff:
                    _diff=abs(curr-p)
                    _closet_pow=p
            curr=abs(curr-_closet_pow)
            res+=1
        return res
if __name__ == "__main__":
    s=Solution()
    
    input=54
    expected=3
    print(s.minOperations(input),' ans=',expected) 
    
    input=9
    expected=2
    print(s.minOperations(input),' ans=',expected) 

    input=39
    expected=3
    print(s.minOperations(input),' ans=',expected) 
    
    



