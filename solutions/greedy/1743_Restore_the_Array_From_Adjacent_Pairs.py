'''
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.
'''
'''
{4: {(...)}, -2: {}}
'''
class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        d={}
        for elem in adjacentPairs:
            t=(elem[0],elem[1])
            if d.get(elem[0])==None:
                d[elem[0]]=set()
            d[elem[0]].add(t)
            if d.get(elem[1])==None:
                d[elem[1]]=set()
            d[elem[1]].add(t)
        
  
        def inner(res:list,last:list,curr:list):
            while 1:
                res.append(last)
                if last==curr[1]:
                    last=curr[0]
                    # use left to get nexts
                    nexts=d[curr[0]]
                    if len(nexts)==1:
                        res.append(curr[0])
                        break
                    else:
                        for n in nexts:
                            if n==(curr[0],curr[1]):continue
                            else:
                                curr=n
                                break
                elif last==curr[0]:
                    last=curr[1]
                    # use right to get nexts
                    nexts=d[curr[1]]
                    if len(nexts)==1:
                        res.append(curr[1])
                        break
                    else:
                        for n in nexts:
                            if n==(curr[0],curr[1]):continue
                            else:
                                curr=n
                                break
        res0=[]
        last=adjacentPairs[0][0]
        curr=adjacentPairs[0]
        inner(res0,last,curr)

        res1=[]
        last=adjacentPairs[0][1]
        curr=adjacentPairs[0]
        inner(res1,last,curr)

        res0.reverse()

        index=-1
        hold=res0[-1]
        for i in range(len(res1)):
            if res1[i]==hold:
                index=i
                break
        return res0+res1[index+1:]
        

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
    