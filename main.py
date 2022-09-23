
class Solution:
    def minimumLength(self, s: str) -> int:
        while True:
            if len(s)==1:break
            #check if we can still remove some chars from both ends
            if(s[-1]==s[0]):#at least one char from both ends are identical
                current_char=s[-1]
                start_ptr=0
                while True:
                    if s[start_ptr]!=current_char:break
                    else:
                        start_ptr+=1
                        if start_ptr==len(s):break
                s=s[start_ptr:]
                if s=='':break
                end_ptr=len(s)-1
                while True:
                    if s[end_ptr]!=current_char:break
                    else:
                        end_ptr-=1
                        if end_ptr==-1:break
                s=s[:end_ptr+1]
                if s=='':break
            else:break
            
        return len(s)


if __name__ == "__main__":

    s = Solution()
    #i = "cabaabac"
    #i="ca"
    i = "aabccabba"
    ans = s.minimumLength(i)
    print(ans)
