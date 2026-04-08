import random,math

class linearsearch:
    def simple_search(self,A,key):
        for i in range(len(A)):
            if A[i] == key:
                return i
        return -1
    
    def two_way_search(self,A, key):
        low = 0
        high = len(A) - 1
        
        while low <= high:
            if A[low] == key:
                return low
            if A[high] == key:
                return high
            low += 1
            high -= 1
        return -1
    
    def ordered_search(self,A, key):
        for i in range(len(A)):
            if A[i] == key:
                return i
            elif A[i] > key:
                break
        return -1
    
    def sentinel_search(self,A, key):
        n = len(A)
        if n == 0: return -1
        
        last = A[n-1]
        A[n-1] = key
        
        i = 0
        while A[i] != key:
            i += 1
            
        A[n-1] = last
        
        if i < n - 1 or A[n-1] == key:
            return i
        return -1

    def self_organizing_search(self,A,key):
        for i in range(len(A)):
            if A[i] == key:
                A[0],A[i]=A[i],A[0]
                return i
        return -1
        
class intervalsearch:
    def interpolation_search(self,A,key):
        low, high = 0,len(A)-1
        while low <=high and key <= A[high] and key >= A[low]:
            pos = low + ((key-A[low])*(high-low)//(A[high]-A[low]))
            if A[pos] == key:
                return pos
            elif A[pos] < key:
                low = pos+1
            else:
                high = pos -1
        return -1

    def fibonacci_search(self,A,key):
        n=len(A)
        fib2,fib1,=0,1
        fib= fib1+fib2 
        while fib < n:
            fib2,fib1=fib1,fib
            fib = fib1+fib2
        offset = -1
        while fib > 1:
            i = min(offset+fib2,n-1)
            if A[i] < key:
                fib = fib1
                fib1=fib2
                fib2=fib-fib1
                offset = i
            elif A[i] > key:
                fib = fib2
                fib1 -= fib2
                fib2 = fib-fib1
            else:
                return i
        if fib1 and offset+1 < n and A[offset] == key:
            offset + 1
        return -1

    def binary_search_recursive(self, A, left, right, key):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            return self.binary_search_recursive(A, mid + 1, right, key)
        else:
            return self.binary_search_recursive(A, left, mid - 1, key)

    def binary_search_ietrative(self,A,left,right,key):
        while left <= right:
            mid = (left+right)//2
            if A[mid] == key:
                return mid
            elif A[mid] < key:
                left = mid + 1
            else:
                right = mid- 1

    def exponential_search(self,A,key):
        n=len(A)
        if A[0] == key:
            return 0
        i=1
        while i <n and A[i] <= key:
            i *= 2
        return self.binary_search_ietrative(A, i//2, min(i,n-1),key)
    
    def ternary_search_ietrative(self, A, left, right, key):
        while left <= right:
            # 범위를 3등분하기 위한 두 개의 지점(m1, m2) 계산
            m1 = left + (right - left) // 3
            m2 = right - (right - left) // 3
            
            if A[m1] == key:
                return m1
            if A[m2] == key:
                return m2
                
            # 검색 범위를 1/3로 좁힘
            if key < A[m1]:
                right = m1 - 1
            elif key > A[m2]:
                left = m2 + 1
            else:
                left = m1 + 1
                right = m2 - 1
        return -1
    
    def ternary_search_recursive(self, A, left, right, key):
        if left > right:
            return -1
            
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3
        
        if A[m1] == key:
            return m1
        if A[m2] == key:
            return m2
            
        if key < A[m1]:
            return self.ternary_search_recursive(A, left, m1 - 1, key)
        elif key > A[m2]:
            return self.ternary_search_recursive(A, m2 + 1, right, key)
        else:
            return self.ternary_search_recursive(A, m1 + 1, m2 - 1, key)

class ranksearch:
    def partion(self, A, low, high):
        pivot = A[low]
        j = low
        for i in range(low+1,high+1):
            if A[i] < pivot:
                j+=1
                A[j],A[i] = A[i],A[j]
        A[j],A[low] = A[low],A[j]
        return j
    
    def rank_search(self,A,low,high,k):
        pos = self.partion(A,low,high)
        if pos+1 == low+k:
            return A[pos]
        elif pos+1 > low+k:
            return self.rank_search(A,low,pos-1,k)
        else:
            return self.rank_search(A,pos+1,high,k-(pos+1-low))

class postoffice_location:
    def distance1(self,p1,p2):
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    def distance2(self,p1,p2):
        return (abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))
    def pol(self,P):
        Xs,Ys=zip(*P)
        Xs = list(Xs)
        Ys=list(Ys)
        print(Xs)
        print(Ys)

        ax=sum(Xs)//len(Xs) #average X
        ay=sum(Ys)//len(Ys) #average Y
        ap = (ax,ay) #average point
        mdist1=0
        for i in range(len(P)):
            mdist1 += self.distance1(ap,P[i])
            print("average point {}, total distance{}".format(ap,mdist1))
        
        mdist2 =0 
        for i in range(len(P)):
            mdist2 += self.distance2(ap,P[i])
            print("average point {}, total distance{}".format(ap,mdist2))

class fakecoin:
    
    def __init__(self,n=100):
        self.coins=self.random_coins(n)
        
    def fake_coins(self):
        pile = list(self.coins)
        while len(pile)>1:
            n = len(pile)
            if n == 2:
                return pile[0] if pile[0] < pile[1] else pile[1]
            r = n//3
            g1=pile[:r]
            g2=pile[r:2*r]
            g3=pile[2*r:]
            cr=self.compare(g1,g2)
            if cr == 0:
                pile=g3
            elif cr == 1:
                pile = g2
            else:
                pile = g1
        return pile[0]


    def compare(self,group1,group2):
        if sum(group1) > sum(group2):
            return 1
        elif sum(group1) < sum(group2):
            return -1
        else:
            return 0

    def random_coins(self,n):
        coins=[2]*(n-1)+[1]
        random.shuffle(coins)
        print(coins)
        return coins
    
class MinMaxSearch:
    def pairing_keys(self, A):
        n = len(A)
        if n == 0: return None, None
        if n == 1: return A[0], A[0]

        if n % 2 == 0:
            if A[0] < A[1]:
                min_val, max_val = A[0], A[1]
            else:
                min_val, max_val = A[1], A[0]
            start_idx = 2
        else:
            min_val = max_val = A[0]
            start_idx = 1

        for i in range(start_idx, n - 1,2):
            if A[i] < A[i+1]:
                if A[i] < min_val: min_val = A[i]
                if A[i+1] > max_val: max_val = A[i+1]
            else:
                if A[i+1] < min_val: min_val = A[i+1]
                if A[i] > max_val: max_val = A[i]
        
        return min_val, max_val
    
    def tournament_selection(self, A):
        def get_max(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            
            next_round = []
            for i in range(0, n, 2):
                if i + 1 < n:
                    next_round.append(max(arr[i], arr[i+1]))
                else:
                    next_round.append(arr[i])
            return get_max(next_round)

        if not A: return None
        return get_max(A)

class MedianOfNArrays:
    def find_median(self, arrays):

        if not arrays: return None
        
        all_elements = []
        for arr in arrays:
            all_elements.extend(arr)
        
        n = len(all_elements)
        if n == 0: return None
        
        all_elements.sort()
        
        if n % 2 == 1:
            return all_elements[n // 2]
        else:
            return (all_elements[n // 2 - 1] + all_elements[n // 2]) / 2

    def find_median_efficient(self, arrays):
        import bisect
        
        all_elements_count = sum(len(arr) for arr in arrays)
        if all_elements_count == 0: return None
        
        def count_less_equal(mid):
            return sum(bisect.bisect_right(arr, mid) for arr in arrays)

        def get_kth(k):
            low = min(arr[0] for arr in arrays if arr)
            high = max(arr[-1] for arr in arrays if arr)
            
            ans = low
            while low <= high:
                mid = (low + high) // 2
                if count_less_equal(mid) >= k:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        if all_elements_count % 2 == 1:
            return get_kth(all_elements_count // 2 + 1)
        else:
            mid1 = get_kth(all_elements_count // 2)
            mid2 = get_kth(all_elements_count // 2 + 1)
            return (mid1 + mid2) / 2