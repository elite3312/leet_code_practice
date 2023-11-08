class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs)==1:
            return [strs]
        d=dict()
        for s in strs:
            _list=list(s)
            _list.sort()
            key=str(_list)
            query_result=d.get(key)
            if query_result==None:
                d[key]=list()
            d[key].append(s)
        res=[]
        for k in d:
            res.append(d[k])
        return res
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    res=sol.groupAnagrams(strs)
    expected="expected: [[\"bat\"],[\"nat\",\"tan\"],[\"ate\",\"eat\",\"tea\"]]"
    print(res,expected)