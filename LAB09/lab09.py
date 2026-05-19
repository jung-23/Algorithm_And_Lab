class permutaltions:
    def __init__(self,st):
        aList = list(st)
        self.np =0
        self.permute(aList,0,len(aList)-1)

    def permute(self, st, start,end):
        if start == end:
            self.np += 1
            print("".join(st))

        else:
            for i in range(start,end+1):
                st[start],st[i] = st[i],st[start]
                self.permute(st,start+1,end)
                st[start],st[i] = st[i], st[start]

class NQueens:
    def __init__(self,N):
        self.N = N
        self.solutions = 0
        self.solve()

    def solve(self):
        board = [-1]*self.N
        self.nQueenDFS(board,0)
        print("Found ",self.solutions,"Solutions")

    def nQueenDFS(self,board,row):
        if row == self.N:
            print(board)
            self.solutions += 1
        else:
            for col in range(self.N):
                if self.isPromising(board,row,col):
                    board[row] = col
                    self.nQueenDFS(board,row+1)
    
    def isPromising(self,board,row,col):
        for i in range(row):
            if board[i] == col or board[i]-i == col-row or board[i]+i == col+row :
                return False
        return True