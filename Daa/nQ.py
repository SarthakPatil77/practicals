n=int(input("enter the n*n board n="))
def safe(r,c,board):
    for i in range(r):
        if board[i][c]==1:
            return False
    for i,j in zip(range(r-1,-1,-1),range(c-1,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(r-1,-1,-1),range(c+1,n)):
        if board[i][j]==1:
            return False
    return True 
    
    
def solve(board,r):
    if r==n:
        return True
    else:
        for c in range(n):
            if safe(r,c,board):
                board[r][c]=1
                if solve(board,r+1):
                    return True
                board[r][c]=0
    return False
        
board=[[0 for i in range(n)] for i in range(n)]
col=int(input(f"enter the col from 0-{n-1} where you want to put queen in row[0]["))
board[0][col]=1
solve(board,1)
for i in board:
    print(" ".join(str(a)for a in i))