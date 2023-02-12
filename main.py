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

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output=[1,2,3,4,8,12,11,10,9,5,6,7]
    res=sol.spiralOrder(matrix)
    print(res," expected: ", Output)