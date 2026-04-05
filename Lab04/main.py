from lab04 import inversion, sorting, merge_sort_3way

def tst_inversion():
    inv = inversion()
    A = [11,2,31,4,5,6,17,8]
    
    print("\n"+"% Inversion test >>>")
    print("count BF : ",inv.inversion_bf(A.copy()))
    print("count DC : ",inv.inversion_dc(A.copy(),0,len(A)-1))
    print("count ST : ",inv.inversion_st(A.copy()))

def tst_sorting():
    s = sorting()
    arr = [11,2,31,4,5,6,17,8]
    
    print("% Sorting test >>>")

    print("Original array:", arr)
    print("Counting Sort:", s.countion_sort(arr.copy(), max(arr) + 1))

    print("Radix Sort:", s.radix_sort(arr.copy()))

    print("Quick Sort:", s.quick_sort(arr.copy(), 0, len(arr) - 1))

    print("Merge Sort:", s.merg_sort(arr.copy(), [0] * len(arr), 0, len(arr) - 1))

    print("Heap Sort:", s.heap_sort(arr.copy()))

def tst_merge_sort_3way():
    m = merge_sort_3way()
    arr = [11,2,31,4,5,6,17,8]

    print("\n"+"% 3-Way Merge Sort test >>>")
    print("Original array:", arr)
    print("3-Way Merge Sort:", m.merge_sort_3way(arr.copy(), 0, len(arr) - 1))

def main():
    tst_sorting()
    tst_inversion()
    tst_merge_sort_3way()
    print()

if __name__=="__main__":
    main()
