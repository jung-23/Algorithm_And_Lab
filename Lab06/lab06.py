class Tromino:
    def __init__(self,n=3,x=0,y=0):
        self.tno=0
        self.size = 2**n
        self.map=[['x' if i==x and j ==y else '0' for j in range(self.size)] for i in range(self.size)]
        if not self.isValid(x,y,0,0,self.size-1,self.size-1):
            print("InValid input tile")
        else:
            self.printMap()
            self.solve(n,0,self.size-1,0,self.size-1,x,y)
            self.printMap()

    def solve(self, n ,startX,startY,endX,endY,x,y):
        cx,cy = self.getCenter(startX,startY,endX,endY)
        x1,y1 = cx,cy
        x2,y2 = cx+1,cy
        x3,y3 = cx,cy+1
        x4,y4 = cx+1,cy+1

        if x <=cx:
            if y <=cy:
                self.placeTiles(cx,cy+1,cx+1,cy+1,cx+1,cy)
                x1,y1=x,y
            else:
                self.placeTiles(cx,cy,cx+1,cy,cx+1,cy+1)
                x2,y2 =x,y
        else:
            if y <=cy:
                self.placeTiles(cx,cy,cx,cy+1,cx+1,cy+1)
                x3,y3=x,y
            else:
                self.placeTiles(cx,cy,cx+1,cy,cx,cy+1)
                x4,y4 =x,y

        if n ==1:
            return
        else:
            self.solve(n-1,startX,cx,startY,cy,x1,y1)
            self.solve(n-1,startX,cx,cy,endY,x2,y2)
            self.solve(n-1,cx,endX,startY,cy,x3,y3)
            self.solve(n-1,cx,cy,endX,endY,x4,y4)
            
                
        
    
    def placeTiles(self,x1,y1,x2,y2,x3,y3):
        self.tno +=1
        self.map[x1][y1] = self.tno
        self.map[x2][y2] = self.tno
        self.map[x3][y3] = self.tno

    def getCenter(self,startX,endX,startY,endY):
        return ((startX+endX)//2,(startY+endY)//2)
    
    def printMap(self):
        print()
        for i in range(self.size):
            for j in range(self.size):
                print("{:<3}".format(self.map[i][j]),end='')
            print()
        print()

        
    def isValid(self,x,y,startX,startY,endX,endY):
        return(startX <=x <= endX) and (startY <= y <= endY)