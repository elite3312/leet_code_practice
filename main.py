class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_substring=dict()#dp[_left,_right]=str[_left:_right+1] is palindrome or not
        n=len(s)
        res=s[0]
        for i in range(n):
            is_substring[(i,i)]=True
        for _left in range(0,n):
            for _right in range(_left,n):
                
                try:
                    if is_substring[(_left,_right)]==True:
                        pass
                except:
                    try :
                        if is_substring[(_left+1,_right-1)]:
                            _set=set(s[_left+1,_right-1+1])
                            if s[_left]==s[_right]:
                                is_substring[(_left,_right)]=True
                                if _right-_left+1>len(res):
                                    res=s[_left:_right+1]
                            else:
                                is_substring[(_left,_right)]=False
                            if len(_set)==1:
                                _only_char=_set[0]
                                if s[_left]==_only_char:
                                    is_substring[(_left,_right-1)]=True
                                if s[_right]==_only_char:
                                    is_substring[(_left+1,_right)]=True

                            
                        else:
                            is_substring[(_left,_right)]=False
                        
                    except:
                        pass
                
        return res
if __name__ == "__main__":
    s=Solution()
    #a="babad"
    a="cbbd"
    print(s.longestPalindrome(a))
    
    