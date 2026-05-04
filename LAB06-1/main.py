from lab06 import chainmatries

def tstCMM():
    print("<<< Chain Matrix Multiplication >>>")
    cm=chainmatries()

    n =10
    # dims = cm.getDims(n)
    dims = [5,2,3,4,6,7,8]
    n=len(dims)-1
    print(dims)
    P,M = cm.cmmDP(dims)
    print('matrix M')
    for r in M:
        print(r)
    print('matrix P')
    for r in P:
        print(r)
    
    cm.printOrder(P,0,n-1)

def tstBC():
    from lab06 import Binomial_Coefficients
    print("<<< Binomial Coefficients >>>")
    bc = Binomial_Coefficients()

    n = 5
    k = 2

    print("Binomial Coefficient >>> C({}, {}) = {}".format(n, k, bc.BC(n, k)))

def tstPaths():
    from lab06 import Path_Counting_Problem
    print("<<< Path Counting Problem >>>")
    P = Path_Counting_Problem()

    n = 3
    m = 4

    print("Number of Paths DC >>> C({}, {}) = {}".format(n, m, P.count_path_dc(n, m)))
    print("Number of Paths DP >>> C({}, {}) = {}".format(n, m, P.count_path_dp(n, m)))
    print("Number of Paths CMN >>> C({}, {}) = {}".format(n, m, P.count_path_cmn(n, m)))

def tstCoin():
    from lab06 import Coin_collecting_problem
    print("<<< Coin Collecting Problem >>>")
    C = Coin_collecting_problem()

    coins = [[0, 0, 1, 0],
             [0, 1, 0, 1],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]

    max_coins, path = C.coin_collection(coins)

    print(f"Maximum Coins: {max_coins}")
    print(f"Path (0-indexed): {path}")

    # 경로 시각화
    print("\nMap (★=Path, ●=Coins, ·=Empty):")
    path_set = set(path)
    for i in range(len(coins)):
        row = ""
        for j in range(len(coins[0])):
            if (i, j) in path_set:
                row += "★ "
            elif coins[i][j] == 1:
                row += "● "
            else:
                row += "· "
        print(row)

def tstOBST():
    from lab06 import Optimal_Binary_Search_Tree
    print("<<< Optimal Binary Search Tree >>>")
    obst = Optimal_Binary_Search_Tree()
    keys = [0, 10, 20, 30, 40, 50, 60]
    p    = [0, 0.15, 0.10, 0.05, 0.35, 0.20, 0.15]

    minavg, A, R, n = obst.opt_search_tree(p)
    print(f"minavg: {minavg:.4f}")

    root = obst.tree(R, keys, 1, n)

    print("\n탐색 테스트:")
    for key in [10, 40, 99]:
        result = obst.search(root, key)
        print(f"  {key} → {'found' if result else 'not found'}")

def main():
    print()
    #tstBC()
    #tstPaths()
    #tstCoin()
    #tstCMM()
    tstOBST()
    print()

if __name__=="__main__":
    main()