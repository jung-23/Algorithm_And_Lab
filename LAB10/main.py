from Code import *
from lab10 import *

C = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
ja = JobAssignment(C)

def run_ja_DFS():
    print("DFS algorithm")
    cSolution = [-1] * ja.n
    visited = [False] * ja.n
    ja.dfs_ja(0, cSolution,0,visited)
    print("Best Cost:", ja.optimal_cost)
    print("Best Assignment:", ja.optimal_solution)

def run_ja_bf():
    print("Brute Force algorithm")
    min_cost, best_assignment = ja.bf_ja()
    print("Best Cost:", min_cost)
    print("Best Assignment:", best_assignment)

def run_ja():
    run_ja_DFS()
    #run_ja_bf()

def run_ep():

    iState = [[1,2,3], [4,0,6], [7,5,8]]
    fState=[[1,2,3], [4,5,6], [7,8,0]]
    ep = EightPuzzle(iState, fState)

def tstCC():
    values = [1, 5, 10, 25]
    amount = 10
    cc = CoinChange(values, amount)
    cc.run()

def main():
    #run_ja()
    #run_ja_DFS()
    #run_ep()
    tstCC()

if __name__ == "__main__":
    main()