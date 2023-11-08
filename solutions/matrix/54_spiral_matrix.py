class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        r=len(matrix)
        c=len(matrix[0])
        total=r*c
        curr_upperleft_r=0
        curr_upperleft_c=0
        curr_r_size=r
        curr_c_size=c
        res=[]
        while True:
            

            for i in range(curr_c_size):
                res.append(matrix[curr_upperleft_r][curr_upperleft_c+i])
            if len(res)>=total:break
            for i in range(1,curr_r_size):
                res.append(matrix[curr_upperleft_r+i][curr_upperleft_c+curr_c_size-1])
            if len(res)>=total:break
            for i in range(curr_c_size-2,-1,-1):
                res.append(matrix[curr_upperleft_r+curr_r_size-1][curr_upperleft_c+i])
            if len(res)>=total:break
            for i in range(curr_r_size-2,0,-1):
                res.append(matrix[curr_upperleft_r+i][curr_upperleft_c])
            if len(res)>=total:break
            curr_r_size-=2
            curr_c_size-=2
            curr_upperleft_c+=1
            curr_upperleft_r+=1
        return res
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3]
             ,[4,5,6]
             ,[7,8,9]]
    Output=[1,2,3,6,9,8,7,4,5]
    res=sol.spiralOrder(matrix)
    print(res," expected: ", Output)

    matrix = [[1,2,3, 4, 5, 6]
             ,[7,8,9,10,11,12]
             ,[13,14,15,16,17,18]
             ,[19,20,21,22,23,24]
             ,[25,26,27,28,29,30]
             ,[31,32,33,34,35,36]
             
             ]
    Output=[1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 35, 34, 33, 32, 31, 25, 19, 13, 7, 8, 9, 10, 11, 17, 23, 29, 28, 27, 26, 20, 14, 15, 16, 22, 21]
    res=sol.spiralOrder(matrix)
    print(res," expected: ", Output)