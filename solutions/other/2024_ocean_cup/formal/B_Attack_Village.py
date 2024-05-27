# b
import bisect
class Solution:
    '''
    Each player takes a turn to perform exactly once the following operation:
    Choose any one of the sites x:
    1. If this site x is unoccupied, the player will occupy the longest
    unoccupied range centered on the site x. In other words, starting from the site x, the player keeps
    expanding the same length to the left and right until the site is occupied or until it reaches the
    border. 
    2. If other players already occupy the site x, he will take all the sites from the player who
    originally occupied it.

    example 1:
    5 10
    3 4 6 9 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] → [1, 1, 1, 1, 1, 0, 0, 0, 0, 0] → [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]
    → [2, 2, 2, 2, 2, 3, 0, 0, 0, 0] → [2, 2, 2, 2, 2, 3, 0, 4, 4, 4] → [2, 2, 2, 2, 2, 3, 0, 5, 5, 5]

    - init
        add (0,0,0) and (11,11,11) for initial turn
        [(0,0,0),(11,11,11)]
    - player 1 picks pos 3
        the first "start" less than 3 is 0
        its end is also less than 3
        so we conclude player 1 has picked an unoccupied pos
        so dist_left=3-0-1=2

        the first "start" greater than 3 is 11
        so dist_right=11-3-1=7

        min_dist=2, so we set 
        ->[(0,5,1),(11,11,11)]
    - player 2 picks pos 4
        the first "start" less than 4 is 0
        and its "end"(5) is greater than 4 as well
        so we conclude that player 2 has picked a pos already occupied
        so we set the interval's to 2
        ->[(0,5,2),(11,11,11)]
    - player 3 picks pos 6
        the first "start" less than 6 is 1
        but its "end" is less than 6 as well
        so we conclude that player 3 has picked a pos not occupied
        dist_left=6-5-1=0

        the first start greater than 6 is 11
        so dist_right=11-3-1=7
        ->[(0,5,2),(6,6,3)(11,11,11)]
    - etc
    '''
    def solve(self,n:int,m:int,arr:list):
        # n: number of players
        # m number of villages
        def my_key(a):
            return a[0]
        arr.insert(0,None)
        l=[[0,0,0],[m+1,m+1,0]]#(start,end, owner)
        i=1
        for x in arr[1:]:
            first_start_less_than_x=bisect.bisect_right(l,x,key=my_key)-1

            if l[first_start_less_than_x][1]<x:
                # then x is unoccupied
                dist_left=x- l[first_start_less_than_x][1]-1
                #we should find the first start greater than x
                first_start_greater_than_x=first_start_less_than_x+1
                dist_right=l[first_start_greater_than_x][0]-x-1

                # add a new interval
                dist=min(dist_left,dist_right)
                l.insert(first_start_greater_than_x,[x-dist,x+dist,i])
            else:
                # x is occupied, change owner
                l[first_start_less_than_x][2]=i
            i+=1
        res=[0 for _ in range(m+1)]
        
        for e in l[1:len(l)-1]:
            for i in range(e[0],e[1]+1):
                res[i]=e[2]

                
                

        

        return res[1:]
        

        

if __name__ == "__main__":
    s = Solution()

    n,m=input().strip().split(' ')
    n,m=int(n),int(m)
    arr=input().strip().split(' ')
    arr=[int (x) for x in arr]
    
    res=s.solve(n,m,arr)
    for i in range(len(res)-1):
        print("%d"%res[i],end=" ")
    print("%d"%res[-1],end="\n")
'''
void solve(){
    map<int, pair<int, int> > mp; // start, {end, id}
    mp[-1] ={-1, 0}; -> l
    mp[n] = {n, 0}; -> r
    r = upper_bound(x) -> >x的第一個start point
    l = r-1 -> <=x
    if( x<=l->end) = mp[] = id
    // mp.upper_bound(x);
    lower_bouhnd(),  
    // -1 0 0 0 0 0 -1
        l           r
    mp[0] = {n-1, id}
}
'''