from lab05 import linearsearch,fakecoin,intervalsearch,ranksearch,postoffice_location,MinMaxSearch
import random

def tst_fakecoin():
    print("\n>>> FAKE COIN >>>")
    n=20
    fc=fakecoin(n)
    print(fc.fake_coins())

def tst_intervalsearch():
    print("\n>>> INTERVALSEARCH >>>")
    ints = intervalsearch()
    A = random.sample(range(1,30),20)
    B = sorted(A)
    print(B)
    key = 15
    print('binarysearch',ints.binary_search_ietrative(B,0,len(B)-1,key))
    print('binarysearch recursive',ints.binary_search_recursive(B,0,len(B)-1,key))
    
    print('ternary search iterative',ints.ternary_search_ietrative(B,0,len(B)-1,key))
    print('ternary search recursive',ints.ternary_search_recursive(B,0,len(B)-1,key))

    print('interpolation search',ints.interpolation_search(B,key))

    print('Fibonacci search',ints.fibonacci_search(B,key))

    print('Exponential search',ints.exponential_search(B,key))
    

def tst_linearsearch():
    print("\n>>> LINEARSEARCH >>>")
    l = linearsearch()
    A = random.sample(range(1,30),20)
    print("A:", A)
    B = sorted(A)
    print("B:", B)
    key=15
    print("simplesearch",l.simple_search(A.copy(),key))

    print("two way search",l.two_way_search(A.copy(),key))

    print("ordered search",l.ordered_search(B,key))

    print("sentinel search",l.sentinel_search(A.copy(),key))

    print("self organizing search",l.self_organizing_search(A.copy(),key))


def tst_ranksearch():
    print("\n>>> RANKSEARCH >>>")
    r= ranksearch()
    A = random.sample(range(1,30),20)
    print(A)
    k = int(round(1+len(A)//2))
    print('element {} rank {}'.format(r.rank_search(A,0,len(A)-1,k),k))
    

def tst_postofficelocation():
    print("\n>>> POSTOFFICE LOCATION >>>")
    pos = postoffice_location()
    P = [(1,1),(4,5),(2,4),(11,21),(42,56),(12,49)]
    pos.pol(P)

def tst_minmaxsearch():
    print("\n>>> MINMAXSEARCH >>>")
    mms = MinMaxSearch()
    A = random.sample(range(1,30),20)
    print(A)
    min_val, max_val = mms.pairing_keys(A)
    print("pairing keys - Min:", min_val, "Max:", max_val)
    print("tournament selection - Max:", mms.tournament_selection(A))

def main():
    #tst_linearsearch()
    #tst_intervalsearch()
    #tst_minmaxsearch()
    # tst_ranksearch()
    tst_postofficelocation()
    tst_fakecoin()



if __name__=="__main__":
    main()
