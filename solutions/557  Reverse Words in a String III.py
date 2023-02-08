class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(' ')
        res=""
        for word in words:
            for i in range(len(word)):
                res+=word[-(i+1)]
            res+=' '
        
        res=res[:len(res)-1]
        return res

        
if __name__ == "__main__":
    
    s = Solution()
    i = "Let's take LeetCode contest"
    #i="God Ding"
    ans=s.reverseWords(i)
    print(ans)
    