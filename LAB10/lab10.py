import sys
from collections import deque

class CoinChange:
    def __init__(self, values, amount):
        self.values = sorted(values)
        self.amount = amount

    def run(self):
        print("=" * 50)
        print("Greedy Results")
        g = self.cChangeGreedy(self.values, self.amount)
        print('Minimum Coins: {}'.format(g['total_coins']))
        print('Coin Combinations: {}'.format(g['combination']))

        print("=" * 50)
        print("Dynamic Programming Results")
        dp = self.cChangeDP(self.values, self.amount)
        print('Minimum Coins: {}'.format(dp['min_coins']))
        print('Coin Combinations: {}'.format(dp['combination']))

        print("=" * 50)
        print("Backtracking Results")
        bt = self.cChangeBackTracking(self.values, self.amount, 0)
        print('Ways: {}'.format(bt['solutions']))
        print('Minimum Coins: {}'.format(bt['minCoins']))
        print('Coin Combinations: {}'.format(bt['Coin Combinations']))
        print('Explored Nodes: {}'.format(bt['Node Explored']))

        print("=" * 50)
        print("Branch and Bound Results")
        bnb = self.cBnB(self.amount, self.values, len(self.values))
        print('Minimum Coins: {}'.format(bnb['min_coins']))
        print('Coin Combinations: {}'.format(bnb['Coin Combinations']))
        print('Explored Nodes: {}'.format(bnb['Node Explored']))

    def cChangeGreedy(self, values, amount):
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
            return {'coins_used': coins_used, 'total_coins': total_used, 'combination': combination}
        return {'total_coins': -1, 'combination': []}

    def cChangeDP(self, coins, amount):
        dp = [sys.maxsize] * (amount + 1)
        parent = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != sys.maxsize:
                    if dp[i] > dp[i - coin] + 1:
                        dp[i] = dp[i - coin] + 1
                        parent[i] = coin
        if dp[amount] == sys.maxsize:
            return {'min_coins': -1, 'combination': []}
        combination = []
        curr = amount
        while curr > 0:
            combination.append(parent[curr])
            curr -= parent[curr]
        return {'min_coins': dp[amount], 'combination': combination}

    def cChangeBackTracking(self, values, amount, idx):
        self.bt_nodes = 0
        self.bt_paths = []
        self.bt_minCoins = sys.maxsize
        self._backtrack(values, amount, idx, [], 0)
        return {
            'solutions': len(self.bt_paths),
            'minCoins': self.bt_minCoins,
            'Coin Combinations': self.bt_paths,
            'Node Explored': self.bt_nodes
        }

    def _backtrack(self, values, amount, idx, path, coin_used):
        self.bt_nodes += 1
        if amount < 0:
            return
        if amount == 0:
            self.bt_paths.append(path[:])
            self.bt_minCoins = min(self.bt_minCoins, coin_used)
            return
        for i in range(idx, len(values)):
            path.append(values[i])
            self._backtrack(values, amount - values[i], i, path, coin_used + 1)
            path.pop()

    def cBnB(self, amount, coins, n):
        self.bnb_nodes = 0
        q = deque([(amount, [])])
        visited = {}
        while q:
            self.bnb_nodes += 1
            curr_amount, curr_paths = q.popleft()
            if curr_amount == 0:
                return {
                    'min_coins': len(curr_paths),
                    'Coin Combinations': curr_paths,
                    'Node Explored': self.bnb_nodes
                }
            if curr_amount < 0:
                continue
            if curr_amount in visited and visited[curr_amount] <= len(curr_paths):
                continue
            visited[curr_amount] = len(curr_paths)
            for i in range(n):
                q.append((curr_amount - coins[i], curr_paths + [coins[i]]))
        return {
            'min_coins': -1,
            'Coin Combinations': [],
            'Node Explored': self.bnb_nodes
        }

# if __name__ == "__main__":
#     values = [1, 5, 10, 25]
#     amount = 10
#     cc = CoinChange(values, amount)
#     cc.run()