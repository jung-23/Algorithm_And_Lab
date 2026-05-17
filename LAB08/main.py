from lab08 import ChangeMaking, Scheduling, SSSP, APSP, MST

def tstCm():
    cm = ChangeMaking()
    coins = [1,5,10,25]
    amount = 69
    S, tCoins = cm.cmGA(coins, amount)
    print(S)
    print( "Total coins :", tCoins)

    print("Total coins by DP :", cm.cmDP(coins, amount))

def tstScheduling():
    s = Scheduling()
    jobs = [('J1',6), ('J2',65), ('J3',16), ('J4',26)]
    S, tTime = s.sTotalTime(jobs)
    print("Total time in System:", tTime)
    print(S)

    print()

    jobs = [('J1',2, 20), ('J2',1, 25), ('J3',3, 40), ('J4',2, 10), ('J5',1, 40)]
    sjobs, S, tprofit = s.sJobsDeadLines(jobs)
    print("Total profit:", tprofit)
    print(S)
    print(sjobs)


def tstMST():
    mst = MST()
    ss = SSSP()

    G = {
        'A': [('B', 4), ('C', 1), ('D', 5)],
        'B': [('A', 4), ('C', 2), ('E', 6)],
        'C': [('A', 1), ('B', 2), ('D', 3), ('E', 7)],
        'D': [('A', 5), ('C', 3), ('E', 8)],
        'E': [('B', 6), ('C', 7), ('D', 8)]
    }

    print("=== Kruskal ===")
    T = mst.Kruskal(G)
    for u, v, w in T:
        print(f"{u} - {v} : {w}")

    print("\n=== Prim ===")
    T = mst.Prim(G, 'A')
    for u, v, w in T:
        print(f"{u} - {v} : {w}")

    print("\n=== Dijkstra ===")
    D, P = ss.Dijkstra(G, 'A')
    for v in D:
        print(v, "=", D[v], " ", P[v])

def tstSSSP():
    ss = SSSP()
    G = {'A':[('B',3),('C',5)],
         'B':[('C',2),('D',7),('E',4),('A',6)],
         'C':[('D',7),('E',4),('A',6)],
         'D':[('E',7),('A',4),('B',6)],
         'E':[]
         }
    
    print("=== Dijkstra ===")
    D, P = ss.Dijkstra(G, 'A')
    for v in D:
        print(v, "=", D[v], " ", P[v])

    print("\n=== Bellman-Ford ===")
    d, p = ss.Bellman(G, 'A')
    for v in d:
        print(v, "=", d[v], " ", p[v])

def tstAPSP():
    apsp = APSP()
    
    INF = float('inf')
    W = [
        [0,   3,   8, INF,  -4],
        [INF, 0, INF,   1,   7],
        [INF, 4,   0, INF, INF],
        [2, INF, -5,   0, INF],
        [INF, INF, INF,   6,   0]
    ]

    print("=== Matrix Multiplication (SMM) ===")
    D2 = apsp.SMM(W, W)       # D^2
    print("D^2:")
    for row in D2:
        print(row)
    D4 = apsp.SMM(D2, D2)     # D^4
    print("D^4:")
    for row in D4:
        print(row)

    print("\n=== Floyd ===")
    D, P = apsp.Floyd(W)
    for row in D:
        print(row)


def main():
    # tstCm()
    # tstScheduling()
    # tstSSSP()
    # tstAPSP()
    tstMST()


if __name__ == "__main__":    
    main()