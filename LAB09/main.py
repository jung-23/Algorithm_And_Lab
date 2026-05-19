from lab09 import permutaltions,NQueens

def tstPermutation():
    st = "ABC"
    per = permutaltions(st)
    print("Total permutation",per.np)

def tstnQueens():
    nq=NQueens(10)



def main():
    tstPermutation()
    tstnQueens()



if __name__=="__main__":
    main()
