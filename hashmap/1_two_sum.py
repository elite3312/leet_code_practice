class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d=dict()
        for i,elem in enumerate( nums):
            d[elem]=i
        for i,elem in enumerate( nums):
            try:
                _candidate=d[target-elem]
                if _candidate>=0 and _candidate!=i:
                    return [i,_candidate]
            except:
                pass#couldn't find an index that satifies constraint, key error

if __name__ == "__main__":
    
       
    s=Solution()
    
    