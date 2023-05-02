board=[[1,2],
       [3,4]]
r=len(board)
c=len(board[0])
transpose_board=[[0]*r]*c
for row in range (r):
    for col in range(c):
        transpose_board[col][row]=board[row][col]

print(board)
print(transpose_board)

board=[[1,2],
       [3,4]]
r=len(board)
c=len(board[0])
#transpose_board=[[0]*r]*c
transpose_board=[[0 for _ in range(r)] for _ in range(c)]
for row in range (r):
    for col in range(c):
        transpose_board[col][row]=board[row][col]

print(board)
print(transpose_board)
