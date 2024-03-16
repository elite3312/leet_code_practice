from utils.test_driver import test_driver
import heapq
class Solution:
    def minimizeStringValue(self, s: str) -> str:

        h=[]#count,char as key
    
        for i in range(0,26):
            cur=ord('a')+i
            h.append([0,cur])
        

        for c in s:
            if c=='?':
                pass
                        
            else:
                for i in range(0,26):
                    if h[i][1]==ord(c):
                         h[i][0]+=1
                         break
        heapq.heapify(h)

        temp=[]
        for c in s:
            if c=='?':
                temp.append(h[0][1])
                h[0][0]+=1
                heapq.heapify(h)
                
        res=[]
        i=0
        for c in s:
            if c=='?':
                res.append(chr(temp[i]))
                i+=1    
            else:
                res.append(c)

        return "".join(str(element) for element in res)




        
if __name__ == "__main__":
    s = Solution()
    
    tests = [
        [
            # inputs
            [
                "abcdefghijklmnopqrstuvwxy??"
            ],
            # res
             "abcdefghijklmnopqrstuvwxyaz"

        ],
        [
            # inputs
            [
                 "???" 
            ],
            # res
             "abc"

        ],
        [
            # inputs
            [
                 "a?a?"
            ],
            # res
             "abac"

        ],
        [
            # inputs
            [
                "aa?ab"
            ],
            # res
             "aacab"

        ],
    ]
    for input, res in tests:
        test_driver(s.minimizeStringValue, input[0],  expected=res)
