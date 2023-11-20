class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
                                
from utils.test_driver import test_driver
if __name__ == "__main__":
    s=Solution()
    inp1='rat'
    inp2='tar'
    out=True
    test_driver(s.isAnagram,inp1,inp2,expected=out)
# idea: res[i]=prefix_product[i-1]*suffix_product[i+1]