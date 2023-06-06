class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove non alpha-numeric
        new_s=str()
        for c in s:
            if ord('a')<=ord(c)<=ord('z') or \
                ord('A')<=ord(c)<=ord('Z')or \
                    ord('0')<=ord(c)<=ord('9'):new_s+=c
        
        # the rest
        new_s=new_s.lower()
        ptr=0
        n=len(new_s)
        if n in [0,1]:return True
        terminate_index=n/2 

        while 1:
            if new_s[ptr]!=new_s[-1-ptr]:return False
            if ptr>=terminate_index:break
            ptr+=1
        return True
def test_driver(s: Solution, input1: any, input2: any, expected: str):
    # change this line
    ans = s.isPalindrome(input1)

    print('\ninput1__:', input1)
    print('input2__:', input2)
    print("ans: ", ans)
    print('expected:', expected)



if __name__ == "__main__":

    s = Solution()
    test_driver(s,'A man, a plan, a canal: Panama',None,True)
    
