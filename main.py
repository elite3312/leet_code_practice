class Solution_tle:
    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        self.grid = dict()
        for row in range(m):
            for col in range(n):
                self.grid[(row, col)] = True

        self.res = 0
        self.path_2_bottom_right(0, 0)
        return self.res

    def path_2_bottom_right(self, curr_r, curr_c):
        if self.grid.get((curr_r, curr_c)) == None:
            return
        elif curr_r == self.m-1 and curr_c == self.n-1:
            self.res += 1
        # go down
        self.path_2_bottom_right(curr_r+1, curr_c)
        self.path_2_bottom_right(curr_r, curr_c+1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[(r,c)]:when robot is at r,c, the number of unique paths for it to reach m-1,n-1
        self.dp = dict()
        self.m=m
        self.n=n
        self.dp[(m-1, n-1)] = 1
        self.inner(m-1, n-1)

        return self.dp[(0,0)]
    def inner(self,r,c ):
        if r<0 or c<0 :return
        if r==self.m-1 and c==self.n-1 :
            pass
        else:
            if self.dp.get((r,c)):return

            portion_from_right=self.dp.get(r,c+1)
            if  portion_from_right == None:
                portion_from_right=0

            portion_from_bottom=self.dp.get(r+1,c)
            if  portion_from_bottom == None:
                portion_from_bottom=0

            self.dp[(r,c)]=portion_from_right+portion_from_bottom
            if r==0 and c==0:return
        # go left 
        self.inner(r,c-1)
        # go up 
        self.inner(r-1,c)

if __name__ == "__main__":

    s = Solution()
    input1 = 3
    input2 = 7
    excepted = 28
    ans = s.uniquePaths(input1, input2)
    print("%d" % ans+' expected:%d' % excepted)

    input1 = 3
    input2 = 2
    excepted = 3
    ans = s.uniquePaths(input1, input2)
    print("%d" % ans+' expected:%d' % excepted)

    input1 = 1
    input2 = 100
    excepted = 1
    ans = s.uniquePaths(input1, input2)
    print("%d" % ans+' expected:%d' % excepted)

    input1 = 3
    input2 = 3
    excepted = 6
    ans = s.uniquePaths(input1, input2)
    print("%d" % ans+' expected:%d' % excepted)
