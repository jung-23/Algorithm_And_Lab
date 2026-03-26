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
        left_sum=0
        for i in range(mid,low-1,-1):
            sm+=A[i]
            left_sum = max(left_sum,sm)
            
        sm=0
        right_sum =0
        for i in range(mid+1,high+1):
            sm+=A[i]
            right_sum=max(right_sum,sm)
        return left_sum+right_sum

    def mssp_dc(self,A,low,high):
        if low == high:
            return A[low]
        else:
            mid = (low+high)//2
            return max(self.mssp_dc(A,low,mid),
                       self.mssp_dc(A,mid+1,high),
                       self.crossMax(A,low,mid,high))
        
    def mssp_dp(self,n,A):
        smax = A[0]
        cmax = A[0]
        for i in range(2,n):
            cmax = max(cmax + A[i], A[i])
            smax = max(smax, cmax)
        return smax
class LZSS:
    def LZSS_bf(self,A):
        n = len(A)
        max_len = 0
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += A[j]
                if curr_sum == 0:
                    max_len = max(max_len, j - i + 1)
        return max_len

    def LZSS_dc(self,A,low,high):
        if low >high:
            return 0
        if(low==high):
            if A[low]==0:
                return 1
            else:
                return 0
        mid = (low + high) // 2
        left_len = self.LZSS_dc(A, low, mid)
        right_len = self.LZSS_dc(A, mid + 1, high)
        
        maxcross = 0
        for i in range(mid, low - 1, -1):
            sum = 0
            for j in range(i, high + 1):
                sum += A[j]
                if sum == 0:
                    maxcross = max(maxcross,j-i+1)
        return max(left_len, right_len, maxcross)

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
        n,m = len(M),len(M[0])
        marea =0
        for r1 in range(n):
            for c1 in range(m):
                for r2 in range(r1,n):
                    for c2 in range(c1,m):
                        total =0
                        for i in range(r1,r2+1):
                            for k in range(c1,c2+1):
                                total +=M[i][k]
                            if total ==0 :
                                area = (r2-r1)*(c2-c1)
                                marea=max(marea,area)
        return marea
    
    def compute_prefix_matrix(self,M):
        n,m = len(M),len(M[0])
        p =[[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(1, m+1):
                p[i][j] = (M[i-1][j-1] + p[i-1][j] + p[i][j-1] - p[i-1][j-1])
        return p
    
    def LZSSM_Prefix(self,M):
        P=self.compute_prefix_matrix(M)
        n,m = len(M),len(M[0])
        marea =0
        for r1 in range(n):
            for c1 in range(m):
                for r2 in range(r1,n):
                    for c2 in range(c1,m):
                        total = P[r2][c2] - P[r1-1][c2] - P[r2][c1-1] + P[r1-1][c1-1]
                        if total ==0 :
                            area = (r2-r1)*(c2-c1)
                            marea=max(marea,area)
        return marea

    def LZSSM_RC(self, M):
        if not M or not M[0]:
            return 0
        
        n, m = len(M), len(M[0])
        max_area = 0

        for r1 in range(n):
            column_sums = [0] * m
            
            for r2 in range(r1, n):
                for c in range(m):
                    column_sums[c] += M[r2][c]
                
                hash_map = {0: -1}
                current_sum = 0
                
                for i in range(m):
                    current_sum += column_sums[i]
                    
                    if current_sum in hash_map:
                        length = i - hash_map[current_sum]
                        area = (r2 - r1 + 1) * length
                        if area > max_area:
                            max_area = area
                    else:
                        hash_map[current_sum] = i

        return max_area
