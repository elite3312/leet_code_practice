# disjoint set
from collections import Counter


def find(parents,x):
    if parents[x]==x:return x
    else:
        # path compression
        parents[x]=find(parents,parents[x])
        return parents[x]
def union(parents, u, v):
    u = find(parents,u)
    v = find(parents,v)
    if u != v:
        if u>=v:# make smaller index parent
            parents[u] = v
        else:
            parents[v] = u
class Solution:
    
    def solve(self,n:int,colors:list,edges:list):
        '''
        Conditions:
        1. If there exists at least one simple path in the tree that starts and ends with different red nodes without
        any yellow nodes on the path
        2. If the path starts and ends with different yellow nodes without any red nodes on the path

        e.g.
            1G
        /  |  \\
        3R  2Y  4R
        |   |   |
        6G  5G  7G

        134 is a path that meets condition 1
        
        1. build 2 disjoint sets
        the 1st disjoint set contains no yellow nodes
        the 2nd disjoint set contains no red nodes

        2. count the number of red nodes in the 1st disjoint set
        and the number of yellow nodes in the 2nd disjoint set.
        3. If any of the counts are greater than 2, the tree is ugly.
        (For condition 1, this means a simple path between 2 red nodes exist and the path contains no yellow nodes)
        '''

        colors.insert(0,None)# for 1 indexed access

        parents_no_yellow=[i for i in range (n+1)]# at first each node is seperate
        parents_no_red=[i for i in range (n+1)]# at first each node is seperate

        # we process one edge at a time
        for e in edges:
            u,v=e[0],e[1]
            if not(colors[u]=='Y'or colors[v]=='Y'):
                union(parents_no_yellow,u,v)
            if not(colors[u]=='R'or colors[v]=='R'):
                union(parents_no_red,u,v)
        for i in range(n+1):
            find(parents_no_yellow,i)
            find(parents_no_red,i)
        
        # check counts
        cnter_no_yellow=Counter(parents_no_yellow[1:])
        cnter_no_red=Counter(parents_no_red[1:])
        for k in cnter_no_yellow:
            if cnter_no_yellow[k]>1:
                red_cnt=0
                for i in range(1,n+1):
                    if colors[i]=='R':red_cnt+=1
                    if red_cnt>1:return False
        for k in cnter_no_red:
            if cnter_no_red[k]>1:
                yellow_cnt=0
                for i in range(1,n+1):
                    if colors[i]=='Y':yellow_cnt+=1
                    if yellow_cnt>1:return False

        return True


        

if __name__ == "__main__":
    s = Solution()

    n=int(input())
    colors=input().strip().split(' ')
    
    edges=[]
    for i in range(n-1):
        line=input().strip().split(' ')
        for i in range(2):line[i]=int(line[i])
        edges.append(line.copy())
    res=s.solve(n,colors,edges)
    if res:print("It is a Christmas tree!")
    else:print("What an ugly tree!")
    