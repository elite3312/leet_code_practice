from utils.test_driver import test_driver



import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count={}
        for n in nums:
            if count.get(n)==None:count[n]=0
            count[n]+=1
        pairs=[]
        for key in count:
            heapq.heappush(pairs,(-count[key],key))
        res=[]
        for _ in range(k):res.append(heapq.heappop(pairs)[1])
        return res


if __name__ == "__main__":
    s = Solution()

    tests = [
        [
            # inputs
            [
              [-1,-1],1
            ],
            # res
            [-1]

        ],
        [
            # inputs
            [
              [1,1,1,2,2,3],2
            ],
            # res
            [1,2]

        ],
        [
            # inputs
            [
              [1],1
            ],
            # res
            [1]

        ],




    ]
    for input, res in tests:
        test_driver(s.topKFrequent, input[0], input[1],  expected=res)
'''
1 use counter for unique elems
2 push all (count, k) onto a maxheap
'''