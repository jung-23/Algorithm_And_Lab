
class xpowern:
    def power1(self,x,n):
        result=1
        for _ in range(n):
            result*=x
        return result
    'n=10 -> 10번 연산'

    def power2(self,x,n):
        if n ==0:
            return 1
        return x*self.power2(x,n-1)
    'n=10 -> 10번 연삭'

    '교수님은 둘이 같다라는데 왤까요 ->'

    def power3(self, x, n):
        if n==0:
            return 1
        half = self.power3(x,n//2)
        if n%2==0:
            return half*half
        else:
            return x*half*half
    'n=10 -> 4번 연산'
    '#로그함수? log2'

    def power4(self,x,n):
        result=1
        while n>0:
            if n%w2==1:
                result *=x
            x *=x
            n=n//2
        return result



class Fibonacci:
    def fib1(self,n):
        if n<=1:
            return n
        return self.fib1(n-1)+self.fib1(n-2)

    def fib2(self,n):
        if n<=1:
            return n
        a,b=0,1
        for _ in range(2,n+1):
            a,b = b, a+b
        return b
    "n=10 9번?"
    'fib2가 fib1보다 연산속도가 빠른데 왜일까 ->'

    def fib3(self,n):
        'Matrix Exponentiation Method for Fibonacci'
        if n==0:
            return(0,1)
        a,b = self.fib3(n//2)
        c=a*(2*b-a)
        d=a*a + b*b
        if n%2==0:
            return (c,d)
            '투플리턴'
        else:
            return (d,c+d)


        'T1(n) = 2^(n) -> 시간이 급격하게 증가  ex) n!' \
        'T2(n) = n -> 시간이 선형으로 증가  ex) n^(2), n^(3)' \
        'T3(n) = log2 n -> 시간이 매우 작게 증가' \
        '시간증가하는 정도 T3 < T2 < T1'

class Search:
    def sequential_search(self,S,x):
        location = 0
        while location < len(S):
            if S[location]== x:
                return location
            location += 1
        return -1 #n+1

    def element_uniqueness(self,A):
        n = len(A)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if A[i] == A[j]:
                    return False
        return True #(n(n-1))/2

    def Guassian_elemention(self,A):
        n = len(A)
        for i in range(0,n-1):
            for j in range(i+1,n):
                for k in range(i,n+1):
                    A[j][k] = A[j][k] - A[i][k]*A[j][i]/A[i][i]
        return A

class Hanoi:
    def hanoi(self,disks,source,auxiliary,target):
        if disks > 0:
            self.hanoi(disks-1,source,target,auxiliary)
            print("move disk",disks,"from",source,"-->",target)
            self.hanoi(disks-1,auxiliary,source,target)
    # 2^(n)-1