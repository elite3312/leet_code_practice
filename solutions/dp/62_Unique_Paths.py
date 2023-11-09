
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dp[(r,c)] : when robot is at r,c, the number of unique paths for it to reach m-1,n-1
        m,n=4,3
        dp:
            0,  1,  2
            __  __  __
        0 | 10, 4,  1   
        1 |  6, 3,  1 
        2 |  3, 2,  1
        3 |  1, 1,  1

        '''
        dp = [[False]*n]*m
        dp[m-1][n-1] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c == n-1:
                    continue
                if r+1>m-1:
                    portion_from_bottom = 0
                else:
                    portion_from_bottom = dp[r+1][ c]
                if  c+1>n-1:
                    portion_from_right =0
                else:
                    portion_from_right = dp[r][ c+1]
                dp[r][c] = portion_from_bottom+portion_from_right

        return dp[0][ 0]
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

    input1 = 3
    input2 = 4
    excepted =10
    ans = s.uniquePaths(input1, input2)
    print("%d" % ans+' expected:%d' % excepted)

    input1 = 23
    input2 = 14
    excepted =1476337800
    ans = s.uniquePaths(input1, input2)
    print("%d" % ans+' expected:%d' % excepted)

class Solution_dict:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = dict()
        dp[(m-1, n-1)] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c == n-1:
                    continue

                portion_from_bottom = dp.get((r+1, c))
                if portion_from_bottom == None:
                    portion_from_bottom = 0

                portion_from_right = dp.get((r, c+1))
                if portion_from_right == None:
                    portion_from_right = 0
                dp[(r, c)] = portion_from_bottom+portion_from_right

        return dp[(0, 0)]

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
