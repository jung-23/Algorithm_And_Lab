import random,math


class linearsearch:
    def simple_search(self,A,key):
        for i in range(len(A)):
            if A[i] == key:
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
            


    def binary_search_recursive(self,A,left,right,key):
        pass

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
    
    def ternary_search_ietrative(self,A,left,right,key):
        pass
    def ternary_search_recursive(self,A,left,right,key):
        pass

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
        return (abs(p1[0-p2[0]])+abs(p1[1]-p2[1]))
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
            mdist1 += self.distance1(ax,P[i])
            print("average point {}, total distance{}".format(ap,mdist1))
        
        mdist2 =0 
        for i in range(len(P)):
            mdist2 += self.distance2(ax,P[i])
            print("average point {}, total distance{}".format(ap,mdist2))


class fakecoin:
    def __init__(self,n=100):
        self.coins=self.random_coins(n)
        
    def fake_coins(self):
        pile = list(self.coins)
        while len(pile)>1:
            r = len(pile)//3
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