from lab09 import permutaltions,NQueens,SumSS,Sdoku

def tstPermutation():
    st = "ABC"
    per = permutaltions(st)
    print("Total permutation",per.np)

def tstnQueens():
    nq=NQueens(10)

def tstsumss():
    S = [4,3,6,1,6]
    W = 13

    ss = SumSS(S,W)
    print("Total nodes", ss.nn, " promissing nodes : ", ss.pn)

def tstSudoku():
    g = [[3,0,6,5,0,8,4,0,0],
         [5,2,0,0,0,0,0,0,0],
         [0,8,7,0,0,0,0,3,1],
         [0,0,3,0,1,0,0,8,0],
         [9,0,0,8,0,3,0,0,5],
         [0,5,0,0,9,0,6,0,0],
         [1,3,0,0,0,0,2,5,0],
         [0,9,0,0,0,0,0,7,4],
         [0,0,5,2,0,6,3,0,0]]
    
    sk = Sdoku(g)
    sk.run()

def main():
    tstSudoku()





if __name__=="__main__":
    main()
