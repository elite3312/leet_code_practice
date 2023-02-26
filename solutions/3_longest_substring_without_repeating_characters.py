from collections import Counter

#Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _counter=Counter()#a counter works similar to a dictionary. It returns 0 instead of keyerror during a miss. 

        rightmost_index=0
        leftmost_index=0
        res=0
        while rightmost_index<len(s):
            
            rightmost_char=s[rightmost_index]
            _counter[rightmost_char]+=1#this might cause the _counter to have duplicates
            #thus we need to fix it. We remove char(s) from the left until the no duplicates property is restored
            while _counter[rightmost_char]>=2:
                leftmost_char=s[leftmost_index]
                _counter[leftmost_char]-=1
                leftmost_index+=1
            res=max(res,rightmost_index-leftmost_index+1)
            rightmost_index+=1
        return res




if __name__ == "__main__":
    
       
    s=Solution()
    
    