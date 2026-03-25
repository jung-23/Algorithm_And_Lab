class MSSP:
    def mssp_bf(self,A):
        n =len(A)
        mx=0
        for i in range(n):
            sm=0
            for j in range(i,n):
                sm+=A[j]
                mx=max(mx,sm)
        return mx
    
    def crossMax(self,A,low,mid,high):
        sm=0
        left_sum=1000
        right_sum =1000
        for i in range(mid,low-1,-1):
            sm+=A[i]
            left_sum = max(left_sum,sum)
            
        sm=0
        for i in range(mid,high+1):
            sm+=A[i]
            right_sum=max(right_sum,sum)
        return left_sum+right_sum

    def mssp_dc(self,A,low,high):
        if low == high:
            return A[low]
        else:
            mid = (low+high)//2
            return max[self.mssp_dc(A,low,mid),
                       self.mssp_dc(A,mid+1,high),
                       self.crossMax(A,low,mid,high)]

class LZSS:
    def LZSS_bf(self,A):
        pass

    def LZSS_dc(self,A,low,high):
        pass
    def LZSS_Prefix(self,A):
        map={}
        sm=0
        mlen=0
        for i in range(len(A)):
            sm+=A[i]
            if sm==0:
                mlen=i+1
            if sm in map:
                mlen=max(mlen,i-map[sm])
            else:
                map[sm]=i
        return mlen

class LZSSM:
    def LZSSM_BF(self,M):
        n,m = len(M),len(m[0])
        marea =0
        for r1 in range(n):
            for c1 in range(m):
                for r2 in range(r1,n):
                    for c2 in range(c1,m):



                        total =0
                        for i in range(r1,r2+1):
                            for k in rnage(c1,c2+1):
                                total +=M[i][j]

                    
                        if total ==0 :
                            area = (r2-r1+1)*(c2-21+1)
                            marea=max(marea,area)
        return marea
    
    def compute_prefix_matrix(self,M):
        n,m = len(M),len(M[0])
        p =[[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(1, m+1):
                p[i][j] = (M[i][j] + p[i-1][j] + p[i][j-1] - p[i-1][j-1])
        return p
    
    def LZSSM_Prefix(self,M):
        pass
