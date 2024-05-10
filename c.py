try:from utils.test_driver import test_driver
except:pass
'''
* for wall
. for space
'''
class Solution:
    def venue_cleaning(self, n,m,map) -> int:
        if map[0][0]=='*':return [-1,[]] 
        cur=(0,0)

        adjacent_cells=[(-1,0),#up
                        (0,-1),#left
                        (1,0),#down
                        (0,1)]#right
    
                     
        def is_valid(r,c):
            if  r<0 or c<0 or r>=n or c>=m:return False
            elif map[r][c]=='*':return False
            else :return True
        
        stk=[cur]
        visited=[[False for _ in range(m)]for _ in range(n)]
        res_path=[]

      
        while 1:
            # visit current cell
            cur=stk[-1]
            
            visited[cur[0]][cur[1]]=True
            res_path.append((cur[0]+1,cur[1]+1))
            if len(res_path)>2*n*m:return [-1,[]]

            if cur==(n-1,m-1):
                res=(cur[0]+1,cur[1]+1)
                break
            
            # push 1st occurence of the valid and unvisited adjacent cell onto stk
            next=None
            found_valid_next=False
            for adjcell_r,adjcell_c in adjacent_cells:
                next=(cur[0]+adjcell_r,cur[1]+adjcell_c)
                if is_valid(next[0],next[1]) and not visited[next[0]][next[1]]:
                    found_valid_next=True
                    break
            if found_valid_next:
                stk.append(next)

            # no such cell is found, look at stack top
            else:
                if len(stk)<2:return [-1,[]]
                stk.append(stk[-2])

        # case where a portion of the map is unreachable
        for r in range(n):
            for c in range(m) :
                if visited[r][c]==False and map[r][c]=='.':return [-1,[]]
        pass
        return [len(res_path), res_path]

        
if __name__ == "__main__":
    s = Solution()

    submit=True
    index=0
    
    if submit:
        n,m=str(input()).strip().split(' ')
        n,m=int(n),int(m)
        map=[]
        for _ in range(n):
            cur=str(input()).strip()
            map.append(cur)
        
        res,res_path=s.venue_cleaning(n,m,map)
        if res==-1:
            res,res_path=s.venue_cleaning(n,m,map)
        print(res)
        if len(res_path)>0:
            for _ in res_path:
                print("%d %d"%(_[0],_[1]))
    else:

        tests = []
        
        # 0
        n,m=3,4
        map=["...*",
             "*..." ,
             "...."
            ]
        tests.append(
            [
                # inputs
                [
                    n,m,map
                ],
                # res
                [12,[
                    (1, 1),
                    (1, 2),
                    (2, 2),
                    (3, 2),
                    (3, 1),
                    (3, 2),
                    (3, 3),
                    (2, 3),
                    (1, 3),
                    (2, 3),
                    (2, 4),
                    (3, 4),
                ]]

            ],
        )
        # 1
        n,m=3,4
        map=["....",
             ".*..",
             "...."
            ]
        tests.append(
            [
                # inputs
                [
                    n,m,map
                ],
                # res
                [14,[
                    (1 ,1),
                    (1 ,2),
                    (1 ,3),
                    (2 ,3),
                    (3 ,3),
                    (3 ,2),
                    (3 ,1),
                    (2 ,1),
                    (1 ,1),
                    (1 ,2),
                    (1 ,3),
                    (1 ,4),
                    (2 ,4),
                    (3 ,4),
                ]]

            ],
        )
        # 2
        n,m=3,3
        map=["...",
             "*..",
             ".*."
            ]
        tests.append(
            [
                # inputs
                [
                    n,m,map
                ],
                # res
                [-1,[
                    
                ]]

            ],
        )

        # 3
        n,m=1 ,1
        map=[".",
            
            ]
        tests.append(
            [
                # inputs
                [
                    n,m,map
                ],
                # res
                [1,[(1,1)
                    
                ]]

            ],
        )
        
        # 4
        n,m=1 ,1
        map=["*",
            
            ]
        tests.append(
            [
                # inputs
                [
                    n,m,map
                ],
                # res
                [-1,[
                    
                ]]

            ],
        )
        # 5
        n,m=1 ,2
        map=[".*",
            
            ]
        tests.append(
            [
                # inputs
                [
                    n,m,map
                ],
                # res
                [-1,[
                    
                ]]

            ],
        )
        
        for input, res in tests[index:]:
            if not  test_driver(s.venue_cleaning, input[0],input[1],input[2],False , expected=res):
                print("attempting alternative")
                test_driver(s.venue_cleaning, input[0],input[1],input[2],True,  expected=res)
