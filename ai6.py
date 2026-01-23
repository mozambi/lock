N=4
id=[0]*(2*N-1)
rd=[0]*(2*N-1)
cl=[0]*N

def printsolution(board):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".",end="")
        print()
def solveNQUtil(board,col):
    if col>=N:
        return True
    for i in range(N):
        if id[i-col+N-1]!=1 and rd[i+col]!=1 and cl[i]!=1:
            board[i][col]=1
            id[i-col+N-1]=rd[i+col]=cl[i]=1
            if solveNQUtil(board,col+1):
                return True
            board[i][col]=0
            id[i-col+N-1]=rd[i+col]=cl[i]=0
    return False
def solveNQ():
   board = [[0 for _ in range(N)] for _ in range(N)]
   if not solveNQUtil(board,0):
        print("solution does not exist")
        return False
   printsolution(board)
   return True

solveNQ()
