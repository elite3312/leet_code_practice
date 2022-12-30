class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=dict()#dp[_left,_right]=true if s[_left,_right+1] is palindrome
        n=len(s)
        res=s[0]
        for i in range(n):
            dp[(i,i)]=(True,True,s[i])#(is_palinedrome, contains only one type of character), the only char
        for left in range(0,n):
            for right in range(0,n):
                
                _candidate=dp.get((left,right))
                if _candidate:
                    if _candidate[0]==True:continue
                    
                else:
                    _candidate_0=dp.get((left+1,right-1))
                    
                    if _candidate_0:#left+1,right-1
                        if dp[(left+1,right-1)][1]:#all same
                            _that_char= dp[(left+1,right-1)][2]
                            if s[left]==s[right]==_that_char:
                                dp[(left,right)]=(True,True,_that_char)
                                if right-left+1>len(res):res=s[left:right+1]
                            elif (s[left]==s[right])and (s[right]!=_that_char):
                                dp[(left,right)]=(True,False,None)
                                if right-left+1>len(res):res=s[left:right+1]
                            
                        else:#not all same
                            if s[left]==s[right]:
                                dp[(left,right)]=(True,False,None)
                                if right-left+1>len(res):res=s[left:right+1]
                    #############
                    _candidate_1=dp.get((left,right-1))
                    if _candidate_1:#left,right-1 
                        if dp[(left,right-1)][1]:#all same      
                            _that_char= dp[(left,right-1)][2]
                            if s[right]==_that_char:
                                dp[(left,right)]=(True,True,_that_char)
                                if right-left+1>len(res):res=s[left:right+1]
                    ##########
                    _candidate_2=dp.get((left+1,right))
                    if _candidate_2:#left+1,right
                        if dp[(left+1,right)][1]:#all same   
                            _that_char= dp[(left+1,right)][2]
                            if s[left]==_that_char:
                                dp[(left,right)]=(True,True,_that_char)
                                if right-left+1>len(res):res=s[left:right+1]
                    if not _candidate_0 and not _candidate_1 and not _candidate_2:
                        dp[(left,right)]=(False,False,None)
                        
        
                
        return res
if __name__ == "__main__":
    s=Solution()
    #a="babad"#bab
    #a="cbbd"#bb
    #a='bb'#bb
    a="abcba"#"abcba"
    print(s.longestPalindrome(a))
    
    