from lab05 import linearsearch,fakecoin,intervalsearch,ranksearch,postoffice_location
import random

def tst_fakecoin():
    n=20
    fc=fakecoin(n)
    print(fc.fake_coins())

def tst_intervalsearch():
    ints = intervalsearch()
    A = random.sample(range(1,30),20)
    B = sorted(A)
    print(B)
    key = 15
    print('binarysearch',ints.binary_search_ietrative(B,0,len(B)-1,key))
    print('Exponential search',ints.exponential_search(B,key))
    print('Fibonacci search',ints.fibonacci_search(B,key))
    print('interpolation search',ints.interpolation_search(B,key))

def tst_linearsearch():
    l = linearsearch()
    A = random.sample(range(1,30),20)
    print(A)
    key=15
    print("simplesearch",l.simple_search(A,key))
    print("self organizing search",l.self_organizing_search(A,key))

def tst_ranksearch():
    r= ranksearch()
    A = random.sample(range(1,30),20)
    print(A)
    k = int(round(1+len(A)//2))
    print('element {} rank {}'.format(r.rank_search(A,0,len(A)-1,k),k))
    

def tst_postofficelocation():
    pos = postoffice_location()
    P = [(1,1),(4,5),(2,4),(11,21),(42,56),(12,49)]
    pos.pol(P)

def main():
    #tst_fakecoin()
    tst_intervalsearch()
    tst_linearsearch()
    tst_ranksearch()
    tst_postofficelocation()

if __name__=="__main__":
    print('시작')
    main()
