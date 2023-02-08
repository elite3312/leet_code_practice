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
        dp = dict()
        for anchor in range(2, target+1):
            is_first = True
            i = anchor
            while i > 0:
                remainder = anchor - i

                if candidate_hashmap[i] and i == anchor:
                    s = set()
                    s.add((i))
                    dp[anchor] = s
                elif candidate_hashmap[i] and dp.get(remainder) != None:
                    s = set()
                    set_from_remainder: set = dp.get(remainder)
                    list_from_remainder = list(set_from_remainder)
                    l = [0]+list_from_remainder
                    l.sort()
                    
                    dp[anchor] . add(tuple(l))
                if is_first:
                    i -= 2
                    is_first = False
                else:
                    i -= 1
        return dp.get(target)


if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = "[[2,2,3],[7]]"
    print(sol.combinationSum(candidates, target),)
