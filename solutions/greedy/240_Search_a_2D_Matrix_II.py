'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        len_r=len(matrix)
        len_c=len(matrix[0])
        r=len_r-1
        c=0
        while 1:
            # check matching condition
            curr=matrix[r][c]
            if curr==target:return True

            # get upper cell value if possible
            upper=None
            if r>=1:upper=matrix[r-1][c]
            
            # get right cell value if possible
            right=None
            if c<=len_c-2:right=matrix[r][c+1]

            if upper:
                # if target is less than or equal to upper cell value, go up
                if target<=upper:r-=1
                else:
                    # if right cell exists, go left
                    if right:
                        c+=1
                    # right cell is none, upper is bigger than target, thus stop
                    else:break
            # can't go up
            else:
                # if right cell exists, go right
                if right:
                    c+=1
                # can't go up or right, thus stop
                else:break
            
        return False

def test_driver(s: Solution, *inputs, expected: str):
    # change this line
    ans = s.searchMatrix(*inputs)

    for i in range(len(inputs)):
        print('input_%d : %s'%(i,str(inputs[i])))
    print("ans: ", ans)
    print('expected:', expected)
if __name__ == "__main__":
    s = Solution()
    matrix = [[1,  4, 7,11,15],
              [2,  5, 8,12,19],
              [3,  6, 9,16,22],
              [10,13,14,17,24],
              [18,21,23,26,30]]
    target = 5
    test_driver(s, matrix,target, expected=True)

    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    test_driver(s, matrix,target, expected=False)

# o(m)
# idea : start from bottomo left, go up or go left until reaching border