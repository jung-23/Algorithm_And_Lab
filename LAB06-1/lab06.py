import random,sys

# 이항 계수 문제---------------------------------------------------------------
class  Binomial_Coefficients:
    def BC(self,n, k):
        B = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):                  # i = 0 to n
            for j in range(min(i, k) + 1):      # j = 0 to min(i, k)
                if j == 0 or j == i:            # 양 끝은 항상 1
                    B[i][j] = 1
                else:                           # 파스칼의 삼각형
                    B[i][j] = B[i-1][j-1] + B[i-1][j]

        return B[n][k]




# 경로 계산 문제---------------------------------------------------------------

class Path_Counting_Problem:
    def count_path_dc(self, n, m):
        if n == 1 or m == 1:        # 한 줄/열이면 경로는 1개
            return 1
        else:
            return self.count_path_dc(n-1, m) + self.count_path_dc(n, m-1)
        
    def count_path_dp(self,n, m):
        T = [[0] * m for _ in range(n)]

        for i in range(n):          # 첫 번째 열 = 모두 1
            T[i][0] = 1
        for j in range(m):          # 첫 번째 행 = 모두 1
            T[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                T[i][j] = T[i-1][j] + T[i][j-1]   # 위 + 왼쪽

        return T[n-1][m-1]
    
    def count_path_cmn(self, n, m):
        paths = 1
        for i in range(n, m + n - 1):          # i = n, n+1, ..., m+n-2
            paths = paths * i // (i - n + 1)   # C(n+m-2, n-1) 점화식
        return paths
        



# 동전 수집 문제---------------------------------------------------------------
class Coin_collecting_problem:
    def coin_collection(self, C):
        n = len(C)
        m = len(C[0])

        # F[i][j] : (1,1) → (i,j) 까지 모을 수 있는 최대 동전 수
        F = [[0] * m for _ in range(n)]

        # ── 초기화 ──────────────────────────────
        F[0][0] = C[0][0]

        for j in range(1, m):               # 첫 번째 행: 오른쪽으로만 이동 가능
            F[0][j] = F[0][j-1] + C[0][j]

        for i in range(1, n):               # 첫 번째 열: 아래로만 이동 가능
            F[i][0] = F[i-1][0] + C[i][0]

        # ── DP 테이블 채우기 ─────────────────────
        for i in range(1, n):
            for j in range(1, m):
                F[i][j] = max(F[i-1][j], F[i][j-1]) + C[i][j]
                #              ↑ 위에서 내려옴    ↑ 왼쪽에서 옴

        # ── 경로 역추적 (print path) ─────────────
        path = []
        i, j = n - 1, m - 1

        while i > 0 or j > 0:
            path.append((i, j))
            if i == 0:                      # 첫 행 → 왼쪽에서 온 것
                j -= 1
            elif j == 0:                    # 첫 열 → 위에서 온 것
                i -= 1
            elif F[i-1][j] > F[i][j-1]:    # 위가 더 크면 → 위에서 온 것
                i -= 1
            else:                           # 왼쪽이 크거나 같으면 → 왼쪽에서 온 것
                j -= 1

        path.append((0, 0))
        path.reverse()

        return F[n-1][m-1], path

class Optimal_Binary_Search_Tree:
    class Node:
        def __init__(self, key):
            self.key   = key
            self.left  = None
            self.right = None
    
    def opt_search_tree(self,p):
        """
        p : 탐색 확률 리스트 (1-indexed 사용, p[0] 미사용)
            예) p = [0, 0.15, 0.10, 0.05, 0.35, 0.20, 0.15]
                → 키 1~6 에 대한 확률
        """
        n = len(p) - 1  # 키 개수 (p[1]..p[n])

        # (n+2) x (n+2) 크기로 생성 (1-indexed, 0행/열 미사용)
        A = [[0.0] * (n + 2) for _ in range(n + 2)]
        R = [[0]   * (n + 2) for _ in range(n + 2)]

        # 빈 구간 초기화
        for i in range(1, n + 2):
            A[i][i - 1] = 0.0
            R[i][i - 1] = 0
        A[n + 1][n] = 0.0
        R[n + 1][n] = 0

        # diagonal = 1 → n  (구간 길이)
        for diagonal in range(1, n + 1):
            for i in range(1, n - diagonal + 2):    # i = 1 .. n-diagonal+1
                j = i + diagonal - 1                 # j = i + diagonal - 1

                # i..j 구간의 확률 합
                prob_sum = sum(p[m] for m in range(i, j + 1))

                # k = i..j 중 A[i][k-1] + A[k+1][j] 최솟값 탐색
                best_cost = float('inf')
                best_k    = i
                for k in range(i, j + 1):
                    cost = A[i][k - 1] + A[k + 1][j]
                    if cost < best_cost:
                        best_cost = cost
                        best_k    = k

                A[i][j] = best_cost + prob_sum
                R[i][j] = best_k

        minavg = A[1][n]
        return minavg, A, R, n
    
    def tree(self,R, keys, i, j):
        """
        R     : 루트 인덱스 테이블
        keys  : 키 리스트 (1-indexed, keys[0] 미사용)
        i, j  : 현재 구간
        """
        k = R[i][j]
        if k == 0:
            return None

        node        = self.Node(keys[k])
        node.left   = self.tree(R, keys, i,     k - 1)
        node.right  = self.tree(R, keys, k + 1, j    )
        return node
    
    def search(self,root, keyin):
        p     = root
        found = False
        while not found:
            if p is None:
                return None
            if p.key == keyin:
                found = True
            else:
                if keyin < p.key:
                    p = p.left
                else:
                    p = p.right
        return p
    
    def print_tree(self,node, prefix="", is_left=True):
        if node is None:
            return
        connector = "├── " if is_left else "└── "
        print(prefix + connector + str(node.key))
        new_prefix = prefix + ("│   " if is_left else "    ")
        self.print_tree(node.left,  new_prefix, True )
        self.print_tree(node.right, new_prefix, False)


# 행렬 곱셈 문제---------------------------------------------------------------

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
                mm = cost
        
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
            print( "A_{}".format(i+1),end = '')
        else:
            print("(",end= "")
            self.printOrder(P,i,P[i][j]-1)
            self.printOrder(P,P[i][j],j)
            print(")",end="")