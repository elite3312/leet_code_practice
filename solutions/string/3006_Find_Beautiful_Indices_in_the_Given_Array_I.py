from utils.test_driver import test_driver


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        a_substrs_indexes=[i for i in range(len(s)) if s.startswith(a, i)]
        b_substrs_indexes=[i for i in range(len(s)) if s.startswith(b, i)]
        
        res=[]
        for a in a_substrs_indexes:
            for b in b_substrs_indexes:
                if abs(a-b)<=k:
                    res.append(a)
                    break

        return res         
        

if __name__ == "__main__":
    sol = Solution()
    s="isawsquirrelnearmysquirrelhouseohmy"
    a="my"
    b="squirrel"
    k=15
    res=sol.beautifulIndices(s,a,b,k)
    print (res)#[16,33]

   
