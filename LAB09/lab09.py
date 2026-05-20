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
    
class SumSS:
    def __init__(self,s,W):
        self.nn=0
        self.pn=1
        
        remainingTotal = sum(s)
        runningWeight = 0
        n = len(s)
        subset=[]
        index = 0
        self.sumss(s,subset,index,runningWeight,n,W,remainingTotal)



    def sumss(self,s,subset,index,runningWeight,n,W,remainingTotal):
        self.nn += 1
        if runningWeight == W :
            print("subset =",subset,"sum of subset",sum(subset))
            return
        elif index == n:
            return
        elif runningWeight > W and remainingTotal< W:
            return
        else:
            self.pn += 1
            # if we do not pick the element (right subtree)
            remainingTotal -= s[index]
            self.sumss(s,subset,index+1,runningWeight,n,W,remainingTotal)

            # if we pick the element (left subtree)
            remainingTotal -= s[index]
            runningWeight += s[index]
            subset += [s[index]]
            self.sumss(s,subset,index-1,runningWeight,n,W,remainingTotal)


class Sdoku:
    def __init__(self,g):
        self.grid = g
        self.non = 0

    def print_grid(self):
        for row in self.grid:
            print(''.join(['{:2d}'.format(item) for item in row]))

    def empthyCell(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0 :
                    return(i,j)
        return None
    def isPromissing(self,num,pos):
        for i in range(len(self.grid)):
            if self.grid[pos[0]][i] == num and pos[1] != i:
                return False
        for i in range(len(self.grid)):
            if self.grid[i][pos[1]] == num and pos[0] != i:
                return False
            
        box_x = pos[1]//3
        box_y = pos[0]//3
        for i in range(box_y*3, box_y *3+3):
            for j in range(box_x*3,box_x *3 +3):
                if self.grid[i][j] == num and (i,j) != pos:
                    return False
        return True
    
    def solve(self):
        # self.tn += 1
        find = self.empthyCell()
        if not find :
            return True
        else:
            row, col = find

        for i in range( 1, 10 ):
            if self.isPromissing(i,(row,col)):
                self.non += 1
                self.grid[row][col] = i
                # print(f"\nTrying {i} at ( {row}, {col}) - promising nodes : {self.non}")
                # self.print_grid(self.grid)
                # time.sleep(0.1) # slow down for visualization

                if self.solve():
                    return True
                
                #Backtrack
                # print(f"Backtracking from( {row}, {col})"")

                self.grid[row][col]=0

                # self.print_grid(self.grid)
                # time.sleep(0.1)
        return False
    
    def run(self):
        print("Start State:")
        self.print_grid()
        if self.solve():
            print("Goal State: ")
            self.print_grid()
            print("Number of promising nodes:", self.non)
        else:
            print("No solution exists")



class GraphColoring:
    def __init__(self,g,m):
        N =len(g)
        Color = [0]*N
        self.colors = [ "","Red","Green","Blue","Black","pink","Aqua","Brown"]
        if not self.graghColor(N,g,m,Color,0):
            print("No solution")
        else:
            self.printsoulution(Color)

    def printsoulution(self,solution):
        print( 'Assighned colors : ')
        for vix in range(len(solution)):
            print("The certex {} is assigned {} color".format(vix,self.colors[solution[vix]]))

    def ispromising(self, n ,gragh, vertex,color,c):
        for i in range(n):
            if gragh[vertex][i] == 1 and color[i] == c:
                return False
        return True
    
    def graghColor(self, n, gragh, m, color, vertex):
        if vertex == n:
            return True
        for c in range(1,m+1):
            if self.ispromising(n,gragh,vertex,color,c):
                color[vertex] = c
                if self.graghColor(n,gragh,m,color,vertex+1):
                    return True
                color[vertex] = 0
        return False