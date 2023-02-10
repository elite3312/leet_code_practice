class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        side_len=n
        for leftmost_row in range(n//2):
            
            for c_offset in range(side_len-1):

                r=leftmost_row
                c=leftmost_row+c_offset

                val=matrix[r][c]
                c+=side_len-1
                # 0
                if c_offset>0:
                    r=leftmost_row+c_offset
                    c=leftmost_row+(side_len-1)
                temp=matrix[r][c]
                matrix[r][c]=val
                val=temp
                
                r+=side_len-1
                # 1  
                if c_offset>0:
                    c=leftmost_row+(side_len-1)-c_offset
                    r=leftmost_row+(side_len-1)
                temp=matrix[r][c]
                matrix[r][c]=val
                val=temp

                # 2
                c-=side_len-1
                if c<leftmost_row:
                    r=leftmost_row+(side_len-1)-c_offset
                    c=leftmost_row
                temp=matrix[r][c]
                matrix[r][c]=val
                val=temp

                # 3
                r-=side_len-1
                if r<leftmost_row:
                    c=leftmost_row+c_offset
                    r=leftmost_row
                matrix[r][c]=val
                    
            side_len-=2

if __name__ == "__main__":
    sol = Solution()
    #matrix=[[1,2,3],[4,5,6],[7,8,9]]
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    #matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    sol.rotate(matrix)
    print(matrix)