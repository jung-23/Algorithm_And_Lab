from Code import *
from lab10 import *

C = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
ja = JobAssignment(C)

def run_ja():
    print("=" * 50)
    print("Assignment Problem")

    print("\nA. Brute Force")
    cost, assign, nodes = ja.bf_ja()
    print("Best Cost: {}, Assignment: {}, Nodes: {}".format(cost, assign, nodes))

    print("\nB. Branch and Bound with BFS")
    cost, assign, nodes = ja.bnb_bfs_ja()
    print("Best Cost: {}, Assignment: {}, Nodes: {}".format(cost, assign, nodes))

    print("\nC. Branch and Bound with Best First Search")
    cost, assign, nodes = ja.bnb_bfs_best_ja()
    print("Best Cost: {}, Assignment: {}, Nodes: {}".format(cost, assign, nodes))

def run_ep():
    print("=" * 50)
    print("8-Puzzle Problem")
    iState = [[1,2,3], [4,0,6], [7,5,8]]
    fState = [[1,2,3], [4,5,6], [7,8,0]]
    ep = EightPuzzle(iState, fState)

def run_cc():
    print("=" * 50)
    print("Coin Change Problem")
    values = [1, 5, 10, 25]
    amount = 10
    cc = CoinChange(values, amount)
    cc.run()

def main():
    run_cc()
    run_ja()
    run_ep()

if __name__ == "__main__":
    main()