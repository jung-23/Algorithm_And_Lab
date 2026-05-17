
class ChangeMaking:
    def cmDP(self, coins, amount):
        F = [float('inf')] * (amount + 1)
        F[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    F[i] = min(F[i], F[i - coin] + 1)
        
    def cmGA(self, coins, amount):
        coins.sort(reverse=True)
        S =[]
        tCoins = 0
        for coin in coins:
            count = amount // coin
            if count > 0:
                S.append((coin, count))
                tCoins += count
                amount = amount % coin
        if amount != 0:
            print("Exact change cannot be made...")
        return S, tCoins
    
class Scheduling:
    def sTotalTime(self,jobs):
        #jobs = [('J1',6), ('J2',65), ('J3',16), ('J4',26)]
        jobs.sort(key=lambda x: x[1])
        cTime = 0
        tTime = 0
        S= []
        for job,t in jobs:
            cTime += t
            S.append((job, cTime))
            tTime += cTime
        return S, tTime
    
    def sJobsDeadLines(self,jobs):
        #jobs = [('J1',2, 20), ('J2',1, 25), ('J3',3, 40), ('J4',2, 10), ('J5',1, 40)]
        jobs.sort(key=lambda x: x[2], reverse=True)
        maxDeadline = max(job[1] for job in jobs)
        slots = [False] * ( maxDeadline + 1 )
        S = [None] * ( maxDeadline + 1 )
        tprofit = 0
        for job,dl,p in jobs:
            for j in range(dl,0,-1):
                if not slots[j]:
                    slots[j] = True
                    S[j] = job
                    tprofit += p
                    break
            sjobs = [job for job in S if job is not None]
        return sjobs, S, tprofit
    

from queue import PriorityQueue

class MST:
    def Kruskal(self, G):
        edges = []
        for u in G:
            for v, w in G[u]:
                edges.append((w, u, v))
        edges.sort()
        
        parent = {u: u for u in G}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        T = []
        for w, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                T.append((u, v, w))
        return T

    def Prim(self, G, r):
        key = {u: float('inf') for u in G}
        p = {u: None for u in G}
        key[r] = 0
        PQ = PriorityQueue()
        for u in G:
            PQ.put((key[u], u))
        inMST = set()
        T = []
        while not PQ.empty():
            _, u = PQ.get()
            if u in inMST:
                continue
            inMST.add(u)
            if p[u] is not None:
                T.append((p[u], u, key[u]))
            for v, w in G[u]:
                if v not in inMST and w < key[v]:
                    key[v] = w
                    p[v] = u
                    PQ.put((key[v], v))
        return T


class SSSP:
    def Dijkstra(self, G, S):
        D ={}
        P ={}
        for v in G:
            D[v] = float('inf')
            P[v] = None
        D[S] = 0
        PQ = PriorityQueue()
        PQ.put((0, S))
        while not PQ.empty():
            d, u = PQ.get()
            if d > D[u]:
                continue
            for v, w in G[u]:
                if D[u] + w < D[v]:
                    D[v] = D[u] + w
                    P[v] = u
                    PQ.put((D[v], v))
        return D, P
    
    def Bellman(self, G, S):
        D ={}
        P ={}
        for v in G:
            D[v] = float('inf')
            P[v] = None
        D[S] = 0
        n=len(G)
        for i in range(n-1):
            for u in G:
                for v, w in G[u]:
                    if D[u] != float('inf') and D[u] + w < D[v]:
                        D[v] = D[u] + w
                        P[v] = u
            
        for u in G :
            for v, w in G[u]:
                if D[u] != float('inf') and D[u] + w < D[v]:
                    print("negative cycle,...")
                    return None, None
                
        return D, P
      

class APSP:
    def usingDigikstra(self, G):
        ss = SSSP()
        paths = {}
        for s in G:
            paths[s] = ss.Dijkstra(G, s)
        return paths
    
    def repeatSquaring(self, W):
        n = len(W)
        D = [row[:] for row in W]
        m = 1
        while m < n - 1:
            D = self.SMM(D, D)
            m = 2 * m
        return D

    def SMM(self,A,B):
        n = len(A)
        D = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if A[i][k] + B[k][j] < D[i][j]:
                        D[i][j] = A[i][k] + B[k][j]
        return D

    def Floyd(self,W):
        n = len(W)
        D = [row[:] for row in W]
        P = [[0] * n for _ in range(n)]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if D[i][k] + D[k][j] < D[i][j]:
                        D[i][j] = D[i][k] + D[k][j]
                        P[i][j] = k + 1  # 1-based
        return D, P