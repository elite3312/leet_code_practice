from utils.test_driver import test_driver_main
# import functools
# from utils.linked_list import print_list
# from itertools import combinations
# from collections import Counter
# from collections import deque
# import math
# import heapq

class set_with_max_min:
    _s:set
    _max:int
    _min:int
    def __init__(self,first_item:int) -> None:
        self._s=set()
        self._s.add(first_item)
        self._max=first_item
        self._min=first_item

    def add(self,item:int):
        self._s.add(item)
        if item>self._max:
            self._max=item
        elif item<self._min:
            self._min=item
    def get_max(self):
        return self._max
    def get_min(self):
        return self._min    
    def get_set(self):
        return self._s

class Solution_tle:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:

        #preprocess the input array:
        #group them into sets according to the rule regarding maxDiff

        sets_with_max_min=[set_with_max_min(nums[0])]

        for i in range(1,len(nums)):
            added_to_one_of_the_sets=False
            for _set_with_max_min in sets_with_max_min:
                can_be_added_to_this_set:bool=True
                if nums[i]>_set_with_max_min.get_max():
                    if (nums[i]-_set_with_max_min.get_max())>maxDiff:
                        can_be_added_to_this_set=False
                        continue
                if can_be_added_to_this_set and nums[i]<_set_with_max_min.get_min():
                    if (_set_with_max_min.get_min()-nums[i])>maxDiff:
                        can_be_added_to_this_set=False
                        continue
                if can_be_added_to_this_set:
                    _set_with_max_min.add(nums[i])
                    added_to_one_of_the_sets=True
                    break
            if not added_to_one_of_the_sets:
                sets_with_max_min.append(set_with_max_min(nums[i]))
            
        # query each set, check if the pair fall into the same set

        res = []
        for q in queries:
            ans=False
            for _set_with_max_min in sets_with_max_min:
                _s=_set_with_max_min.get_set()
                if nums[q[0]] in _s  and nums[q[1]] in _s:
                    ans=True
                    break
            res.append(ans)

        return res

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        comps=[-1]*n# connected components

        comps[0]=nums[0]

        for i in range(1,n):
            # since the list is sorted
            # if the next number satisfies constraint, put it into the current comp
            if (nums[i]-nums[i-1])<=maxDiff:
                comps[i]=comps[i-1]
            else:
                comps[i]=nums[i]
        return [comps[i]==comps[j]for i,j in queries]#use the comp id to check if two elems are in the same comp
'''
"Component" here is short for connected component — a graph theory term.

In this problem, nums and maxDiff implicitly define a graph: nodes are indices 0..n-1, and an edge connects i and j if |nums[i]-nums[j]| <= maxDiff. A connected component is a maximal group of nodes that are all reachable from each other via some chain of edges (not necessarily a direct edge — a path through other nodes counts).

Two nodes have "a path between them" (what the query asks) exactly when they belong to the same connected component. So instead of checking reachability per query, you precompute which component every index belongs to, then a query is just "are these two indices' components equal?"
'''

'''
You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], determine whether there exists a path between nodes ui and vi.

Return a boolean array answer, where answer[i] is true if there exists a path between ui and vi in the ith query and false otherwise.
'''
if __name__ == "__main__":
    sol = Solution()

    index = 0

    tests = [
        [[2,[1,3],1,[[0,0],[0,1]]],[True,False]],
        [[4,[2,5,6,8],2,[[0,1],[0,2],[1,3],[2,3]]],[False,False,True,True]],
        [[6,[2,5,6,8,9,27],2,[[0,1],[0,2],[1,3],[2,3],[0,4]]],[False,False,True,True,False]],
    ]

    test_driver_main(sol.pathExistenceQueries   , tests, index)
