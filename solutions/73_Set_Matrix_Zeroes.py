class Solution:
    # o(1), t(m*n)
    def setZeroes(self, matrix) -> None:
        '''
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
        '''
        m = len(matrix)
        n = len(matrix[0])

        flag = None
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    # iterate thru all cols in this row, and set any non_zeroes to flag
                    for iterate_c in range(n):
                        if matrix[r][iterate_c] != 0:
                            matrix[r][iterate_c] = flag
                    # iterate thru all rows in this rol, and set any non_zeroes to flag
                    for iterate_r in range(m):
                        if matrix[iterate_r][c] != 0:
                            matrix[iterate_r][c] = flag

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == flag:
                    matrix[r][c] = 0


if __name__ == "__main__":

    s = Solution()

    input1 = [[0, 1, 1, 1],
              [1, 1, 0, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1]]

    excepted = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 1, 0, 1],
                [0, 1, 0, 1]]
    ans = s.setZeroes(input1)
    print('input1__:', input1)
    print('expected:', excepted)

    input1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    excepted = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    ans = s.setZeroes(input1)
    print('input1__:', input1)
    print('expected:', excepted)
