class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=set()
        for c in sentence:
            s.add(c)
        if len(s)==26:return True
        else: return False


if __name__ == "__main__":
    s=Solution()
    
    n=['a','b','c']
    
    ans=s.checkIfPangram(n)
    print(ans)