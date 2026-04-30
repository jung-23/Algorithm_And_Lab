import random,sys

class chainmatries:
    def Getdims ( self, n):
        dims =[]
        for i in range(n+1):
            dims.append(random.randint(1,9))

        for i in range(n):
            print("M_{} ({} x {})",format(i+1,dims[i],dims[i+1]))

        return dims
    
    def cmmRec(self,dims,i,j):
        if j <= i+1:
            return 0
        
        mm = sys.maxsize

        for k in range (i+1,j):
            cost = self.cmmRec(dims,i,k)
            cost += self.cmmRec(dims,k,j)
            cost += dims[i]*dims[k]*dims[j]

        if cost < mm:
            mm =cost
        
        return mm
    
    def cmmDP(self, dims):
        n=len(dims)-1
        m=[[0 for i in range(0,n)] for i in range(0,n)]
        P = [[0 for i in range(0,n)]for j in range(0,n)]

        for d in range(2, n+1):
            for i in range(0,n-d+1):
                j=i+d-1
                if i < j :
                    cost = [m[i][k]+m[k+1][j] + dims[i]*dims[k+1]*dims[j+1] for k in range(i,j)]
                    (P[i][j],m[i][j]) = min(enumerate(cost),key=lambda x:x[1])

                    P[i][j] = P[i][j]+i+1
        return P,m
    
    def printOrder(self,P,i,j):

        if i == j:
            print( "A_{}",format(i+1),end = '')
        else:
            print("(",end= "")
            self.printOrder(P,i,P[i][j]-1)
            self.printOrder(P,P[i][j],j)
            print(")",end="")