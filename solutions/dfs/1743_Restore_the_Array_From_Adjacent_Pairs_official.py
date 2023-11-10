'''
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.
'''
'''
{4: {(...)}, -2: {}}
'''
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break
        
        def dfs(node, prev, ans):
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node, ans)

        ans = []
        dfs(root, None, ans)
        return ans
        

def test_driver(s: Solution, *inputs, expected: str):
    # change this line
    ans = s.restoreArray(*inputs)

    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
if __name__ == "__main__":
    s = Solution()

    # change below
    input = [[4,-2],[1,4],[-3,1]]
    ans=[-2,4,1,-3]
    test_driver(s,input,expected=ans)

    input = [[5,1],[5,3],[3,7],[9,7],[10,9]]
    ans=[1,5,3,7,9,10]
    test_driver(s,input,expected=ans)

    input = [[5,3],[5,1],[3,7],[9,7],[10,9]]
    ans=[1,5,3,7,9,10]
    test_driver(s,input,expected=ans)
    