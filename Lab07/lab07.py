import heapq
from collections import Counter


class Horspool:
    def shift_table(self, P):
        m = len(P)
        table = {}
        for i in range(m):
            table[P[i]] = m
        for j in range(m - 1):
            table[P[j]] = m - j - 1
        return table

    def match(self, T, P):
        n, m = len(T), len(P)
        if m == 0 or m > n:
            return -1
        table = self.shift_table(P)
        results = []
        i = m - 1
        while i <= n - 1:
            k = 0
            while k <= m - 1 and P[m - 1 - k] == T[i - k]:
                k += 1
            if k == m:
                results.append(i - m + 1)
                i += 1
            else:
                i += table.get(T[i], m)
        return results if results else -1


class KMP:
    def lps(self, P):
        m = len(P)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and P[k] != P[q]:
                k = pi[k - 1]
            if P[k] == P[q]:
                k += 1
            pi[q] = k
        return pi

    def match(self, T, P):
        n, m = len(T), len(P)
        if m == 0 or m > n:
            return -1
        pi = self.lps(P)
        results = []
        q = 0
        for i in range(n):
            while q > 0 and P[q] != T[i]:
                q = pi[q - 1]
            if P[q] == T[i]:
                q += 1
            if q == m:
                results.append(i - m + 1)
                q = pi[q - 1]
        return results if results else -1


class EditDistance:
    def compute(self, S, T):
        m, n = len(S), len(T)
        F = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            F[i][0] = i
        for j in range(n + 1):
            F[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if S[i-1] == T[j-1] else 1
                F[i][j] = min(F[i-1][j] + 1, F[i][j-1] + 1, F[i-1][j-1] + cost)
        return F[m][n]


class LCS:
    def lcs_dc(self, X, Y, m=None, n=None):
        if m is None: m = len(X)
        if n is None: n = len(Y)
        if m == 0 or n == 0:
            return 0
        if X[m-1] == Y[n-1]:
            return 1 + self.lcs_dc(X, Y, m-1, n-1)
        return max(self.lcs_dc(X, Y, m, n-1), self.lcs_dc(X, Y, m-1, n))

    def lcsdp(self, X, Y):
        m, n = len(X), len(Y)
        L = [[0] * (n + 1) for _ in range(m + 1)]
        B = [[' '] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j-1] + 1
                    B[i][j] = 'D'
                elif L[i-1][j] >= L[i][j-1]:
                    L[i][j] = L[i-1][j]
                    B[i][j] = 'U'
                else:
                    L[i][j] = L[i][j-1]
                    B[i][j] = 'L'
        return L, B

    def print_lcs(self, B, X, i, j, result=None):
        if result is None:
            result = []
        if i == 0 or j == 0:
            return
        if B[i][j] == 'D':
            self.print_lcs(B, X, i-1, j-1, result)
            result.append(X[i-1])
        elif B[i][j] == 'U':
            self.print_lcs(B, X, i-1, j, result)
        else:
            self.print_lcs(B, X, i, j-1, result)
        return ''.join(result)

    def solve(self, X, Y):
        L, B = self.lcsdp(X, Y)
        return L[len(X)][len(Y)], self.print_lcs(B, X, len(X), len(Y)) or ''


class HuffmanCoding:
    class Node:
        def __init__(self, char=None, frequency=0):
            self.char = char
            self.frequency = frequency
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.frequency < other.frequency

    def build_tree(self, text):
        if not text:
            return None
        pq = []
        for char, count in Counter(text).items():
            heapq.heappush(pq, self.Node(char, count))
        n = len(pq)
        for i in range(n - 1):
            p = heapq.heappop(pq)
            q = heapq.heappop(pq)
            r = self.Node()
            r.left = p
            r.right = q
            r.frequency = p.frequency + q.frequency
            heapq.heappush(pq, r)
        return heapq.heappop(pq)

    def generate_codes(self, root):
        codes = {}
        def traverse(node, prefix=''):
            if node is None:
                return
            if node.char is not None:
                codes[node.char] = prefix if prefix else '0'
                return
            traverse(node.left,  prefix + '0')
            traverse(node.right, prefix + '1')
        traverse(root)
        return codes

    def encode(self, text):
        root = self.build_tree(text)
        codes = self.generate_codes(root)
        return ''.join(codes[ch] for ch in text), root

    def decode(self, encoded, root):
        if root is None:
            return ''
        if root.char is not None:
            return root.char * len(encoded)
        result = []
        node = root
        for bit in encoded:
            node = node.left if bit == '0' else node.right
            if node.char is not None:
                result.append(node.char)
                node = root
        return ''.join(result)