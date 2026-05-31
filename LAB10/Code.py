import sys
from collections import deque
import copy
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue
import itertools
import numpy as np
# from scipy.optimize import linear_sum_assignment
# GLOBALS
n = 3
directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
class State:
    def __init__(self, parent=None, puzzle=None):
        self.parent = parent
        self.puzzle = puzzle
        # f = g + h
        self.g = 0
        self.h = 0
        self.f = 0
    def __lt__(self, other):
        return self.f < other.f
    def __hash__(self):
        return hash(tuple(tuple(row)for row in self.puzzle))
 
# EIGHT PUZZLE CLASS
class EightPuzzle():
    def __init__(self, iPuzzle, fPuzzle):
        self.iPuzzle = iPuzzle
        self.fPuzzle = fPuzzle
        if not self.isSolvable():
            print("The instance is not solvable...")
            return
        self.solveDFS()
        self.solveBFS()
        self.solveBnB()
    # DFS
    def solveDFS(self):
        print("\nRunning Depth-First Search...")
        iState = State(None, self.iPuzzle)
        expandedNodes = 0
        generatedNodes = 0
        stack = LifoQueue()
        visited = set()
        stack.put(iState)
        visited.add(self.puzzleToTuple(iState.puzzle))
        while not stack.empty():
            cState = stack.get()
 
            expandedNodes += 1
            # Goal found
            if cState.puzzle == self.fPuzzle:
                self.printPath(cState)
                print("DFS expanded nodes: {}, generated nodes: {}".format(
                        expandedNodes,generatedNodes ))
                return
            # Depth limit
            if cState.g > 15:
                continue
            cRow, cCol = self.indexBTile(cState)
            # Generate children
            for i in range(len(directions)):
                child = self.newState(cState,cRow,cCol,i)
                if child is None:
                    continue
                child.g = cState.g + 1
                child_tuple = self.puzzleToTuple(child.puzzle)
                if child_tuple not in visited:
                    visited.add(child_tuple)
                    stack.put(child)
                    generatedNodes += 1
    # BFS
 
    def solveBFS(self):
        print("\nRunning Breadth-First Search...")
        iState = State(None,self.iPuzzle)
        expandedNodes = 0
        generatedNodes = 0
        queue = Queue()
        visited = set()
        queue.put(iState)
        visited.add(self.puzzleToTuple(iState.puzzle))
        while not queue.empty():
            cState = queue.get()
            expandedNodes += 1
            # Goal found
            if cState.puzzle == self.fPuzzle:
                self.printPath(cState)
                print("BFS expanded nodes: {}, generated nodes: {}".format(
                        expandedNodes,generatedNodes))
                return
            # Depth limit
            if cState.g > 30:
                continue
            cRow, cCol = self.indexBTile(cState)
            # Generate children
            for i in range(len(directions)):
 
                child = self.newState(cState,cRow, cCol, i)
                if child is None:
                    continue
                child.g = cState.g + 1
                child_tuple = self.puzzleToTuple(child.puzzle)
                if child_tuple not in visited:
                    visited.add(child_tuple)
                    queue.put(child)
                    generatedNodes += 1
    # BRANCH AND BOUND (A*)
    def solveBnB(self):
        print("\nRunning Branch and Bound (A*)...")
        iState = State(None, self.iPuzzle)
        expandedNodes = 0
        generatedNodes = 0
        PQ = PriorityQueue()
        visited = set()
        iState.g = 0
        iState.h = self.costManhattan( iState.puzzle,self.fPuzzle )
        iState.f = iState.g + iState.h
        PQ.put(iState)
        visited.add( self.puzzleToTuple(iState.puzzle)  )
        while not PQ.empty():
 
            cState = PQ.get()
            expandedNodes += 1
            # Goal found
            if cState.puzzle == self.fPuzzle:
                self.printPath(cState)
                print("BnB expanded nodes: {}, generated nodes: {}".format(
                        expandedNodes, generatedNodes))
                return
            # Depth limit
            if cState.g > 30:
                continue
            cRow, cCol = self.indexBTile(cState)
            # Generate children
            for i in range(len(directions)):
                child = self.newState(cState,cRow,cCol,i)
                if child is None:
                    continue
                child.g = cState.g + 1
                child.h = self.costManhattan(child.puzzle,self.fPuzzle)
                child.f = child.g + child.h
                child_tuple = self.puzzleToTuple(child.puzzle)
                if child_tuple not in visited:
                    visited.add(child_tuple)
 
                    PQ.put(child)
                    generatedNodes += 1
    # CREATE NEW STATE
    def newState( self,cState,cRow,cCol,i):
        nRow = cRow + directions[i][0]
        nCol = cCol + directions[i][1]
        if not self.isSafe(nRow, nCol):
            return None
        nState = State()
        nState.parent = cState
        nState.puzzle = copy.deepcopy(cState.puzzle)
        nState.g = cState.g
        # Swap tiles
        nState.puzzle[cRow][cCol], nState.puzzle[nRow][nCol] = \
            nState.puzzle[nRow][nCol], nState.puzzle[cRow][cCol]
        return nState
    # SAFETY CHECK
    def isSafe(self, x, y):
        return (x >= 0 and x < n and y >= 0 and y < n )
    # CONVERT PUZZLE TO HASHABLE TUPLE
    def puzzleToTuple(self, puzzle):
        return tuple(tuple(row)for row in puzzle )
 
    # PRINT SOLUTION PATH
    def printPath(self, root):
        if root is None:
            return
        self.printPath(root.parent)
        print("g = {}, h = {}, f = {}".format(root.g, root.h,root.f))
        print('\n'.join([' '.join(['{:3d}'.format(item)for item in row])for row in root.puzzle]))
        print()
    # HAMMING DISTANCE
    def costHamming(self, this, target):
        count = 0
        for i in range(n):
            for j in range(n):
                if ( this[i][j] != 0 and this[i][j] != target[i][j]):
                    count += 1
        return count
    # MANHATTAN DISTANCE
    def costManhattan(self, this, target):
        count = 0
        for num in range(1, n * n):
            x1 = y1 = x2 = y2 = 0
            for i in range(n):
                for j in range(n):
 
                    if this[i][j] == num:
                        x1, y1 = i, j
                    if target[i][j] == num:
                        x2, y2 = i, j
            count += abs(x1 - x2) + abs(y1 - y2)
        return count
    # FIND BLANK TILE
    def indexBTile(self, cState):
        for i in range(n):
            for j in range(n):
                if cState.puzzle[i][j] == 0:
                    return i, j
    # SOLVABILITY CHECK
    def isSolvable(self):
        inversions = 0
        arr = []
        for i in range(n):
            for j in range(n):
                arr.append(self.iPuzzle[i][j])
        for i in range(n * n - 1):
            for j in range(i + 1, n * n):
                if ( arr[i] != 0 and
                    arr[j] != 0 and
                    arr[i] > arr[j] ):
 
                    inversions += 1
        print("Number of inversions = {}".format( inversions ))
        return inversions % 2 == 0
class JobAssignment:
    def __init__(self, C):
        self.cost_matrix = C
        self.n = len(C)
        self.optimal_cost = sys.maxsize
        self.optimal_solution = None
        # Counters
        self.dfs_nodes = 0
        self.dfs_complete_solutions = 0
        self.bt_nodes = 0
        self.bt_complete_solutions = 0
        self.bnb_deq = 0
    # BRUTE FORCE
    def bf_ja(self):
        n = self.n
        min_cost = sys.maxsize
        best_assignment = []
        all_permutations = list(itertools.permutations(range(n)))
        print("Total permutations to check: {}".format(len(all_permutations)))
        for idx, perm in enumerate(all_permutations):
 
            total_cost = 0
            for worker in range(n):
                total_cost += self.cost_matrix[worker][perm[worker]]
            print("Permutation #{}: Assignment = {}, Cost = {}".format(
                idx + 1, perm, total_cost))
            if total_cost < min_cost:
                min_cost = total_cost
                best_assignment = perm
        return min_cost, best_assignment
    # HUNGARIAN ALGORITHM
    def hungarian_ja(self):
        n = self.n
        cost = [row[:] for row in self.cost_matrix]
        print("\n--- Hungarian Algorithm ---")
        print("\nOriginal Cost Matrix:")
        for row in cost:
            print(row)
        # Row Reduction
        for i in range(n):
            row_min = min(cost[i])
            for j in range(n):
                cost[i][j] -= row_min
        print("\nAfter Row Reduction:")
 
        for row in cost:
            print(row)
        # Column Reduction
        for j in range(n):
            col_min = min(cost[i][j] for i in range(n))
            for i in range(n):
                cost[i][j] -= col_min
        print("\nAfter Column Reduction:")
        for row in cost:
            print(row)
        # Assignment
        assigned_jobs = [-1] * n
        used_cols = [False] * n
        for i in range(n):
            for j in range(n):
                if cost[i][j] == 0 and not used_cols[j]:
                    assigned_jobs[i] = j
                    used_cols[j] = True
                    break
        print("\nAssignments:")
        total_cost = 0
        for worker in range(n):
            job = assigned_jobs[worker]
            if job != -1:
 
                actual_cost = self.cost_matrix[worker][job]
                total_cost += actual_cost
                print("Worker {} -> Job {} : Cost = {}".format(
                    worker, job, actual_cost))
        print("\nHungarian Minimal Cost = {}".format(total_cost))
        return total_cost, assigned_jobs
    def hungarian_ja2(self):
        cost_matrix = np.array(self.cost_matrix)
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        total_cost = 0
        solution = [-1] * self.n
        print("\nAssignments:")
        for r, c in zip(row_ind, col_ind):
            cost = self.cost_matrix[r][c]
            solution[r] = c
            total_cost += cost
        return total_cost, solution
    # DFS
    def dfs_ja(self, i, current_solution, current_cost, visited):
        self.dfs_nodes += 1
        # Complete assignment
        if i == self.n:
            self.dfs_complete_solutions += 1
 
            print("DFS Solution #{}: {}, Cost = {}".format(
                self.dfs_complete_solutions, current_solution, current_cost))
            if current_cost < self.optimal_cost:
                self.optimal_cost = current_cost
                self.optimal_solution = current_solution[:]
            return
        # Try assigning jobs
        for j in range(self.n):
            if not visited[j]:
                visited[j] = True
                current_solution[i] = j
                self.dfs_ja(i + 1, current_solution, current_cost + self.cost_matrix[i][j], visited)
                # Backtrack
                visited[j] = False
                current_solution[i] = -1
    # BOUND FUNCTION
    def calc_bound(self, level, visited):
        bound = 0
        for i in range(level, self.n):
            min_cost = sys.maxsize
            for j in range(self.n):
                if not visited[j]:
                    min_cost = min(min_cost, self.cost_matrix[i][j])
            bound += min_cost
 
        return bound
    # BACKTRACKING WITH PRUNING
    def bt_ja(self, i, current_solution, current_cost, visited):
        self.bt_nodes += 1
        # Complete assignment
        if i == self.n:
            self.bt_complete_solutions += 1
            print("BT Solution #{}: {}, Cost = {}".format(
                self.bt_complete_solutions, current_solution, current_cost))
            if current_cost < self.optimal_cost:
                self.optimal_cost = current_cost
                self.optimal_solution = current_solution[:]
            return
        # Prune
        if current_cost >= self.optimal_cost:
            return
        # Try jobs
        for j in range(self.n):
            if not visited[j]:
                visited[j] = True
                current_solution[i] = j
                new_cost = (current_cost + self.cost_matrix[i][j])
                bound = self.calc_bound(i + 1, visited)
 
                # Bounding condition
                if new_cost + bound < self.optimal_cost:
                    self.bt_ja(i + 1, current_solution, new_cost, visited)
                # Backtrack
                visited[j] = False
                current_solution[i] = -1
    # BRANCH AND BOUND (ITERATIVE)
    def bnb_ja(self):
        N = self.n
        PQ = PriorityQueue()
        best_cost = sys.maxsize
        best_solution = None
        counter = 0
        root_visited = [False] * N
        root_bound = self.calc_bound(0, root_visited)
        PQ.put((root_bound, counter, (0, root_bound, [], root_visited)))
        while not PQ.empty():
            total, _, data = PQ.get()
            cost, bound, jobs, visited = data
            level = len(jobs)
            self.bnb_deq += 1
            print("[Node #{}] Level = {}, Cost = {}, Bound = {}, Total = {}, Jobs = {}".format(
                self.bnb_deq, level, cost, bound, total, jobs))
 
            # Complete solution
            if level == N:
                if cost < best_cost:
                    best_cost = cost
                    best_solution = jobs
                    print("Found new best solution: Cost = {}, Jobs = {}".format(
                        best_cost, best_solution))
                continue
            # Expand children
            for j in range(N):
                if not visited[j]:
                    new_jobs = jobs + [j]
                    new_visited = visited[:]
                    new_visited[j] = True
                    new_cost = (cost + self.cost_matrix[level][j])
                    new_bound = self.calc_bound(level + 1, new_visited)
                    new_total = (new_cost + new_bound)
                    # Bounding condition
                    if new_total < best_cost:
                        counter += 1
                        PQ.put((new_total, counter, (new_cost, new_bound, new_jobs, new_visited)))
                        print("Promising Node: Job {}, Cost = {}, Bound = {}, Total = {}, Jobs = {}".format(
                            j, new_cost, new_bound, new_total, new_jobs))
                    else:
 
                        print("Pruned: Job {}, Total = {} >= Best Cost = {}".format(
                            j, new_total, best_cost))
        return best_cost, best_solution
class CoinChange:
    def __init__(self, values, amount):
        self.values = sorted(values)
        self.amount = amount
    def cBackTracking(self, values, amount, idx):
        self.bt_nodes = 0
        self.bt_paths = []
        self.bt_min_coins = sys.maxsize
        self._backtrack(values, amount, idx,[],0)
        return {
            "ways": len(self.bt_paths),
            "min_coins": self.bt_min_coins
            if self.bt_min_coins != sys.maxsize
            else -1,
            "coin_combinations": self.bt_paths,
            "nodes_explored": self.bt_nodes
        }
    def _backtrack(self,values,amount,idx, path,coins_used):
        self.bt_nodes += 1
        # Invalid path
 
        if amount < 0:
            return
        # Solution found
        if amount == 0:
            self.bt_paths.append(path[:])
            self.bt_min_coins = min(self.bt_min_coins,coins_used)
            return
        # Explore
        for i in range(idx, len(values)):
            path.append(values[i])
            self._backtrack(values,amount - values[i],i,path,coins_used + 1 )
            path.pop()
    # DYNAMIC PROGRAMMING
    def cDynamicProgramming(self, coins, amount):
        dp = [sys.maxsize] * (amount + 1)
        parent = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if (i >= coin and dp[i - coin] != sys.maxsize):
                    if dp[i] > dp[i - coin] + 1:
                        dp[i] = dp[i - coin] + 1
                        parent[i] = coin
 
        # No solution
        if dp[amount] == sys.maxsize:
            return {
                "min_coins": -1,
                "combination": []
            }
        # Reconstruct solution
        combination = []
        curr = amount
        while curr > 0:
            combination.append(parent[curr])
            curr -= parent[curr]
        return {
            "min_coins": dp[amount],
            "combination": combination
        }
    # BRANCH AND BOUND (BFS STYLE)
    def cBranchAndBound(self, amount, coins, n):
        self.bnb_nodes = 0
        q = deque([(amount, [])])
        visited = {}
        while q:
            curr_amount, curr_path = q.popleft()
            self.bnb_nodes += 1
 
            # Solution found
            if curr_amount == 0:
                return {
                    "min_coins": len(curr_path),
                    "coin_combination": curr_path,
                    "nodes_explored": self.bnb_nodes
                }
            # Invalid path
            if curr_amount < 0:
                continue
            # Better pruning
            if (curr_amount in visited and visited[curr_amount] <= len(curr_path)):
                continue
            visited[curr_amount] = len(curr_path)
            # Expand nodes
            for i in range(n):
                q.append((curr_amount - coins[i],curr_path + [coins[i]]))
        return {
            "min_coins": -1,
            "coin_combination": [],
            "nodes_explored": self.bnb_nodes
        }
    # GREEDY
    def cGreedy(self, values, amount):
 
        coins_used = [0] * len(values)
        combination = []
        total_used = 0
        remaining = amount
        for i in range(len(values) - 1, -1, -1):
            while remaining >= values[i]:
                remaining -= values[i]
                coins_used[i] += 1
                combination.append(values[i])
                total_used += 1
        if remaining == 0:
            return {
                "coins_used": coins_used,
                "total_coins": total_used,
                "combination": combination
            }
        return "Not possible with greedy"