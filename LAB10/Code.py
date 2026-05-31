import sys
from collections import deque
from queue import PriorityQueue, Queue, LifoQueue
import itertools
import copy

# GLOBALS
n = 3
directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

# ─────────────────────────────────────────
# STATE CLASS (for 8-Puzzle)
# ─────────────────────────────────────────
class State:
    def __init__(self, parent=None, puzzle=None):
        self.parent = parent
        self.puzzle = puzzle
        self.g = 0
        self.h = 0
        self.f = 0
    def __lt__(self, other):
        return self.f < other.f
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.puzzle))

# ─────────────────────────────────────────
# EIGHT PUZZLE CLASS
# ─────────────────────────────────────────
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

    # A. DEPTH FIRST SEARCH
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
            if cState.puzzle == self.fPuzzle:
                self.printPath(cState)
                print("DFS expanded nodes: {}, generated nodes: {}".format(
                    expandedNodes, generatedNodes))
                return
            if cState.g > 15:
                continue
            cRow, cCol = self.indexBTile(cState)
            for i in range(len(directions)):
                child = self.newState(cState, cRow, cCol, i)
                if child is None:
                    continue
                child.g = cState.g + 1
                child_tuple = self.puzzleToTuple(child.puzzle)
                if child_tuple not in visited:
                    visited.add(child_tuple)
                    stack.put(child)
                    generatedNodes += 1

    # B. BREADTH FIRST SEARCH
    def solveBFS(self):
        print("\nRunning Breadth-First Search...")
        iState = State(None, self.iPuzzle)
        expandedNodes = 0
        generatedNodes = 0
        queue = Queue()
        visited = set()
        queue.put(iState)
        visited.add(self.puzzleToTuple(iState.puzzle))
        while not queue.empty():
            cState = queue.get()
            expandedNodes += 1
            if cState.puzzle == self.fPuzzle:
                self.printPath(cState)
                print("BFS expanded nodes: {}, generated nodes: {}".format(
                    expandedNodes, generatedNodes))
                return
            if cState.g > 30:
                continue
            cRow, cCol = self.indexBTile(cState)
            for i in range(len(directions)):
                child = self.newState(cState, cRow, cCol, i)
                if child is None:
                    continue
                child.g = cState.g + 1
                child_tuple = self.puzzleToTuple(child.puzzle)
                if child_tuple not in visited:
                    visited.add(child_tuple)
                    queue.put(child)
                    generatedNodes += 1

    # C. BRANCH AND BOUND (Best First Search / A*)
    def solveBnB(self):
        print("\nRunning Branch and Bound (A*)...")
        iState = State(None, self.iPuzzle)
        expandedNodes = 0
        generatedNodes = 0
        PQ = PriorityQueue()
        visited = set()
        iState.g = 0
        iState.h = self.costManhattan(iState.puzzle, self.fPuzzle)
        iState.f = iState.g + iState.h
        PQ.put(iState)
        visited.add(self.puzzleToTuple(iState.puzzle))
        while not PQ.empty():
            cState = PQ.get()
            expandedNodes += 1
            if cState.puzzle == self.fPuzzle:
                self.printPath(cState)
                print("BnB expanded nodes: {}, generated nodes: {}".format(
                    expandedNodes, generatedNodes))
                return
            if cState.g > 30:
                continue
            cRow, cCol = self.indexBTile(cState)
            for i in range(len(directions)):
                child = self.newState(cState, cRow, cCol, i)
                if child is None:
                    continue
                child.g = cState.g + 1
                child.h = self.costManhattan(child.puzzle, self.fPuzzle)
                child.f = child.g + child.h
                child_tuple = self.puzzleToTuple(child.puzzle)
                if child_tuple not in visited:
                    visited.add(child_tuple)
                    PQ.put(child)
                    generatedNodes += 1

    def newState(self, cState, cRow, cCol, i):
        nRow = cRow + directions[i][0]
        nCol = cCol + directions[i][1]
        if not self.isSafe(nRow, nCol):
            return None
        nState = State()
        nState.parent = cState
        nState.puzzle = copy.deepcopy(cState.puzzle)
        nState.g = cState.g
        nState.puzzle[cRow][cCol], nState.puzzle[nRow][nCol] = \
            nState.puzzle[nRow][nCol], nState.puzzle[cRow][cCol]
        return nState

    def isSafe(self, x, y):
        return (x >= 0 and x < n and y >= 0 and y < n)

    def puzzleToTuple(self, puzzle):
        return tuple(tuple(row) for row in puzzle)

    def printPath(self, root):
        if root is None:
            return
        self.printPath(root.parent)
        print("g = {}, h = {}, f = {}".format(root.g, root.h, root.f))
        print('\n'.join([' '.join(['{:3d}'.format(item) for item in row]) for row in root.puzzle]))
        print()

    def costHamming(self, this, target):
        count = 0
        for i in range(n):
            for j in range(n):
                if this[i][j] != 0 and this[i][j] != target[i][j]:
                    count += 1
        return count

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

    def indexBTile(self, cState):
        for i in range(n):
            for j in range(n):
                if cState.puzzle[i][j] == 0:
                    return i, j

    def isSolvable(self):
        inversions = 0
        arr = []
        for i in range(n):
            for j in range(n):
                arr.append(self.iPuzzle[i][j])
        for i in range(n * n - 1):
            for j in range(i + 1, n * n):
                if arr[i] != 0 and arr[j] != 0 and arr[i] > arr[j]:
                    inversions += 1
        print("Number of inversions = {}".format(inversions))
        return inversions % 2 == 0

# ─────────────────────────────────────────
# JOB ASSIGNMENT CLASS
# ─────────────────────────────────────────
class JobAssignment:
    def __init__(self, C):
        self.cost_matrix = C
        self.n = len(C)
        self.optimal_cost = sys.maxsize
        self.optimal_solution = None
        self.bf_nodes = 0
        self.bfs_nodes = 0
        self.bnb_nodes = 0

    # A. BRUTE FORCE
    def bf_ja(self):
        min_cost = sys.maxsize
        best_assignment = []
        all_permutations = list(itertools.permutations(range(self.n)))
        nodes = 0
        print("Total permutations: {}".format(len(all_permutations)))
        for perm in all_permutations:
            nodes += 1
            total_cost = sum(self.cost_matrix[w][perm[w]] for w in range(self.n))
            print("  Permutation {}: Assignment={}, Cost={}".format(nodes, list(perm), total_cost))
            if total_cost < min_cost:
                min_cost = total_cost
                best_assignment = list(perm)
        self.bf_nodes = nodes
        return min_cost, best_assignment, nodes

    # BOUND FUNCTION (for BnB)
    def calc_bound(self, level, visited):
        bound = 0
        for i in range(level, self.n):
            min_cost = sys.maxsize
            for j in range(self.n):
                if not visited[j]:
                    min_cost = min(min_cost, self.cost_matrix[i][j])
            bound += min_cost
        return bound

    # B. BRANCH AND BOUND WITH BFS
    def bnb_bfs_ja(self):
        q = Queue()
        best_cost = sys.maxsize
        best_solution = None
        nodes = 0
        q.put((0, 0, [], [False] * self.n))
        while not q.empty():
            cost, level, jobs, visited = q.get()
            nodes += 1
            if level == self.n:
                if cost < best_cost:
                    best_cost = cost
                    best_solution = jobs
                continue
            for j in range(self.n):
                if not visited[j]:
                    new_cost = cost + self.cost_matrix[level][j]
                    # Promising condition
                    if new_cost < best_cost:
                        new_visited = visited[:]
                        new_visited[j] = True
                        q.put((new_cost, level + 1, jobs + [j], new_visited))
        self.bfs_nodes = nodes
        return best_cost, best_solution, nodes

    # C. BRANCH AND BOUND WITH BEST FIRST SEARCH
    def bnb_bfs_best_ja(self):
        PQ = PriorityQueue()
        best_cost = sys.maxsize
        best_solution = None
        counter = 0
        nodes = 0
        root_visited = [False] * self.n
        root_bound = self.calc_bound(0, root_visited)
        PQ.put((root_bound, counter, (0, [], root_visited)))
        while not PQ.empty():
            total, _, data = PQ.get()
            cost, jobs, visited = data
            level = len(jobs)
            nodes += 1
            if total >= best_cost:
                continue
            if level == self.n:
                if cost < best_cost:
                    best_cost = cost
                    best_solution = jobs
                continue
            for j in range(self.n):
                if not visited[j]:
                    new_jobs = jobs + [j]
                    new_visited = visited[:]
                    new_visited[j] = True
                    new_cost = cost + self.cost_matrix[level][j]
                    new_bound = self.calc_bound(level + 1, new_visited)
                    new_total = new_cost + new_bound
                    if new_total < best_cost:
                        counter += 1
                        PQ.put((new_total, counter, (new_cost, new_jobs, new_visited)))
        self.bnb_nodes = nodes
        return best_cost, best_solution, nodes


if __name__ == "__main__":
    # ── Assignment Problem ──
    print("=" * 50)
    print("Assignment Problem")
    C = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
    ja = JobAssignment(C)

    print("\nA. Brute Force")
    cost, assign, nodes = ja.bf_ja()
    print("Best Cost: {}, Assignment: {}, Nodes: {}".format(cost, assign, nodes))

    print("\nB. Branch and Bound with BFS")
    cost, assign, nodes = ja.bnb_bfs_ja()
    print("Best Cost: {}, Assignment: {}, Nodes: {}".format(cost, assign, nodes))

    print("\nC. Branch and Bound with Best First Search")
    cost, assign, nodes = ja.bnb_bfs_best_ja()
    print("Best Cost: {}, Assignment: {}, Nodes: {}".format(cost, assign, nodes))

    # ── 8-Puzzle ──
    print("\n" + "=" * 50)
    print("8-Puzzle Problem")
    iState = [[1,2,3],[4,0,6],[7,5,8]]
    fState = [[1,2,3],[4,5,6],[7,8,0]]
    ep = EightPuzzle(iState, fState)