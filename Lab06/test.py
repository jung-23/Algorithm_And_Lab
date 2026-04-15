import matplotlib.pyplot as plt

import random

import math

import copy


# ===================== POINT CLASS =====================

class Point:

    def __init__(self, x=0, y=0):

        self.x = x

        self.y = y


    def __repr__(self):

        return f"({self.x},{self.y})"


    def __eq__(self, other):

        return self.x == other.x and self.y == other.y


    def __lt__(self, other):   # FIXED

        if self.x < other.x:

            return True

        elif self.x == other.x:

            return self.y < other.y

        return False


    def __hash__(self):   # FIXED (very important)

        return hash((self.x, self.y))



# ===================== CLOSEST PAIR =====================

class ClosestPair:

 

    def getPoints(self, n):

        points = set()

        while len(points) < n:

            points.add(Point(random.randint(1, 200), random.randint(1, 200)))

        return list(points)


    def distance(self, p1, p2):

        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


    # -------- Brute Force --------

    def closest_pair_bf(self, P):

        n = len(P)

        mindist = float("inf")

        cp = None


        for i in range(n - 1):

            for j in range(i + 1, n):

                dist = self.distance(P[i], P[j])

                if dist < mindist:

                    mindist = dist

                    cp = (P[i], P[j])


        return mindist, cp


    # -------- Strip Check --------

    def stripClosest(self, strip, d):

        min_val = d

        cp = None

 
        strip.sort(key=lambda p: p.y)


        for i in range(len(strip)):

            j = i + 1

            while j < len(strip) and (strip[j].y - strip[i].y) < min_val:

                dist = self.distance(strip[i], strip[j])

                if dist < min_val:   # FIXED

                    min_val = dist

                    cp = (strip[i], strip[j])

                j += 1


        return min_val, cp


    # -------- Divide & Conquer --------

    def closest_pair_dc(self, P):

        P.sort(key=lambda p: p.x)

        return self._closest_pair_dc(P)


    def _closest_pair_dc(self, P):

        n = len(P)


        if n <= 3:

            return self.closest_pair_bf(P)


        mid = n // 2

        midPoint = P[mid]


        dl, cp_l = self._closest_pair_dc(P[:mid])

        dr, cp_r = self._closest_pair_dc(P[mid:])


 
        if dl < dr:

            d = dl

            cp = cp_l

        else:

            d = dr

            cp = cp_r


        strip = [p for p in P if abs(p.x - midPoint.x) < d]


        d_strip, cp_strip = self.stripClosest(strip, d)


        if cp_strip and d_strip < d:

            return d_strip, cp_strip


        return d, cp


    # -------- Display --------

    def display(self, P, cp):

        x = [p.x for p in P]

        y = [p.y for p in P]

        plt.scatter(x, y)


        if cp:

            cx = [p.x for p in cp]

            cy = [p.y for p in cp]

            plt.plot(cx, cy, 'r-', linewidth=2)


        plt.title("Closest Pair")

        plt.show()



 
# ===================== CONVEX HULL =====================

class ConvexHull:


    def getPoints(self, n):

        points = set()

        while len(points) < n:

            points.add(Point(random.randint(-200, 200), random.randint(-200, 200)))

        return list(points)


    def _det(self, a, b, c):

        return (a.x * b.y + b.x * c.y + c.x * a.y) - \
               (a.y * b.x + b.y * c.x + c.y * a.x)


    # -------- Brute Force --------

    def convex_hull_bf(self, points):

        n = len(points)

        hull = set()


        for i in range(n):

            for j in range(i + 1, n):

                left = right = False


                for k in range(n):

                    if k != i and k != j:

                        val = self._det(points[i], points[j], points[k])

                        if val > 0:

                            left = True

                        elif val < 0:

 
                            right = True


                    if left and right:

                        break


                if not (left and right):

                    hull.add(points[i])

                    hull.add(points[j])


        return list(hull)


    # -------- QuickHull (Divide & Conquer) --------

    def convex_hull_dc(self, points):

        points.sort()

        left = points[0]

        right = points[-1]


        upper = []

        lower = []


        for p in points:

            val = self._det(left, right, p)

            if val > 0:

                upper.append(p)

            elif val < 0:

                lower.append(p)


        hull = {left, right}

        self._build_hull(upper, left, right, hull)

        self._build_hull(lower, right, left, hull)

 

        return list(hull)


    def _build_hull(self, points, a, b, hull):

        if not points:

            return


        farthest = max(points, key=lambda p: abs(self._det(a, b, p)))

        hull.add(farthest)


        left_set = []

        right_set = []


        for p in points:

            if self._det(a, farthest, p) > 0:

                left_set.append(p)

            elif self._det(farthest, b, p) > 0:

                right_set.append(p)


        self._build_hull(left_set, a, farthest, hull)

        self._build_hull(right_set, farthest, b, hull)


    # -------- Display --------

    def display(self, points, hull):

        x = [p.x for p in points]

        y = [p.y for p in points]


        hx = [p.x for p in hull]

        hy = [p.y for p in hull]


        plt.scatter(x, y)

 
        plt.scatter(hx, hy, color='red')


        plt.title("Convex Hull")

        plt.show()



if __name__ == "__main__":


    # -------- Closest Pair --------

    cp = ClosestPair()

    points = cp.getPoints(20)


    print("Points:", points)


    # Brute Force

    d_bf, pair_bf = cp.closest_pair_bf(points)

    print("\nBrute Force:")

    print("Distance:", d_bf)

    print("Pair:", pair_bf)


    # Divide & Conquer

    d_dc, pair_dc = cp.closest_pair_dc(points)

    print("\nDivide & Conquer:")

    print("Distance:", d_dc)

    print("Pair:", pair_dc)


    # Visualization (using DC result)

    cp.display(points, pair_dc)



    # -------- Convex Hull --------

 
    ch = ConvexHull()

    points = ch.getPoints(20)


    print("\nPoints:", points)


    # Brute Force Hull

    hull_bf = ch.convex_hull_bf(points)

    print("\nConvex Hull (Brute Force):")

    print(hull_bf)


    # Divide & Conquer Hull

    hull_dc = ch.convex_hull_dc(points)

    print("\nConvex Hull (Divide & Conquer):")

    print(hull_dc)


    # Visualization (DC hull)

    ch.display(points, hull_dc)