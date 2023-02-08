# 39
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Constraints:
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # prepare a hashmap for shorter lookup time
        candidate_hashmap = [False]*41
        for i in candidates:
            candidate_hashmap[i] = True

        # dp[i]=possible combinationSums for i
        dp =[]

        # initialize dp
        for i in range(0,target+1):
            dp.append(set())

        # fill up dp in a bottom-up fashion
        for anchor in range(2,target+1):
            if candidate_hashmap[anchor]:
                _list_to_add_to_dp_anchor=[]
                _list_to_add_to_dp_anchor.append(anchor)
                dp[anchor].add(tuple(_list_to_add_to_dp_anchor))
            i=anchor-2
            while i>=anchor//2:
                remainder=anchor-i
                if len(dp[remainder])>0:
                    _tuples_from_remainder=dp[remainder]
                    _tuples_from_i=dp[i]
                    for _tuple_from_remainder in _tuples_from_remainder:
                        for _tuple_from_i in _tuples_from_i:
                            _list_from_remainder=list(_tuple_from_remainder)
                            _list_from_i=list(_tuple_from_i)
                            _list_to_add_to_dp_anchor=_list_from_i+_list_from_remainder
                            _list_to_add_to_dp_anchor.sort()
                            _tuple_to_add_to_dp_anchor=tuple(_list_to_add_to_dp_anchor)
                            dp[anchor].add(_tuple_to_add_to_dp_anchor)
                i-=1
        res=[]
        for t in dp[target]:
            res.append(list(t))
        return res


if __name__ == "__main__":
    sol = Solution()
    #---------start writing-------------#
    candidates = [2, 3, 6, 7]
    target = 7
    ans = "ans=[[2,2,3],[7]]\n"
    print(sol.combinationSum(candidates, target),ans)
#
    candidates =[2,3,5]
    target = 8
    ans = "ans=[[2,2,2,2],[2,3,3],[3,5]]\n"
    print(sol.combinationSum(candidates, target),ans)

    candidates =[2]
    target = 3
    ans = "ans=[]\n"
    print(sol.combinationSum(candidates, target),ans)