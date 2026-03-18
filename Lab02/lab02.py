class part02:
    
    #input : A= [[1,2,3],
    #            [2,4,5],
    #            [3,5,6]]
    def enigma(self,A):
        n=len(A)
        for i in range(0,n-1):
            for j in range(i+1, n):
                if A[i][j] != A[j][i]:
                    return False
        return True
    
    #input : B=[2,6,8,3,9,0,11,45,67,90,1]
    def riddle(self,A,n):
        if n==1:
            return A[0]
        else:
            temp = self.riddle(A,n-1)
            if temp <=A[n-1]:
                return temp
            else:
                return A[n-1]
    
    #input : G=[[0,1,1,1,1],
    #           [1,0,1,1,1],
    #           [1,1,0,1,1],
    #           [1,1,1,0,1],
    #           [1,1,1,1,0]]
    def grapgh_complete(self, A,n):
        if n==1:
            return 1
        if not self.grapg_complete(A,n-1):
            return 0
        for j in range(0,n-1):
            if A[n-1][j] == 0:
                return 0
        return 1
    
class part03:
    def Stair_recursive(self,n):
        if n <=1:
            return 1
        return self.Stair_recursive(n-1)+self.Stair_recursive(n-2)
    
    def Stair_itrative(self,n):
        S = [0]*(n+1)
        S[0]=1
        S[1]=1
        for i in range(2,n+1):
            S[i] = S[i-1]+S[i-2]
        return S[n]
    
    def multiply(self,A,B):
        return [[A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]],
                [A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

    def power(self,M,n):
        if n ==1 :
            return M
        half=self.power(M,n//2)
        result = self.multiply(half, half)
        if n%2 == 1:
            result = self.multiply(result,M)
        return result

    def Stair_matrix_power(self,n):
        if n <=1:
            return 1
        M=[[1,1],[1,0]]
        R = self.power(M,n-1)
        return R[0][0] + R[0][1]
