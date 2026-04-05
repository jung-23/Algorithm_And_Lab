from lab04 import inversion, sorting

def tst_inversion():
    inv = inversion()
    A = [11,2,31,4,5,6,17,8]
    print("count BF : ",inv.inversion_bf(A))
    print("count DC : ",inv.inversion_dc(A,0,len(A)-1))

def tst_sorting():
    s = sorting()
    A = [3,4,7,7,9,1,2,1]
    A2 = [777,123,456,111,134]
    A3 = [3,7,12,9,5,2,1]
    print(A)
    B = s.countion_sort(A,max(A)+1)
    print(B)

    print(A2)
    s.radix_sort(A2)
    print(A2)
    s.quick_sort(A2,0,len(A2)-1)
    print(A2)
    print(A3)
    S= [0]*len(A3)
    s.merg_sort(A3,)


def main():
    tst_inversion()
    tst_sorting()

if __name__=="__main__":
    main()
