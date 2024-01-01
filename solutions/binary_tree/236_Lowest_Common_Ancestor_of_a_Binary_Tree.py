from utils.test_driver import test_driver



class Solution:
    def placedCoins(self, edges: list[list[int]], cost: list[int]) -> list[int]:
        n=len(edges)
        res=[1 for _ in range(n)]

        parent=[[i for i in range(n)]]
        
        def find(x):
            if parent[x]==x:return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            a=find(a)
            b=find(b)
            if a!=b:
                parent[b]=a    
                #parent[a]=b
        

                    
        

if __name__ == "__main__":
    s = Solution()

    tests = [
            [
            # input
            [
                [[0,1],[0,2],[0,3],[0,4],[0,5]],
                [1,2,3,4,5,6]
            ],
            #res
            [120,1,1,1,1,1]
            ],
        ]
    for input, res in tests:
        test_driver(s.placedCoins, input[0],input[1], expected=res)
