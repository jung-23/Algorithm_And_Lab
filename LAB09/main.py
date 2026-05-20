from lab09 import permutaltions,NQueens,SumSS,Sdoku,GraphColoring,pathMaze

def tstPermutation():
    st = "ABC"
    per = permutaltions(st)

def tstnQueens():
    nq=NQueens(4)

def tstsumss():
    S = [1,3,7]
    W = 8

    ss = SumSS(S,W)

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

def tstgraphColoring():
    graph = [[0,1,0,0,1],
             [1,0,1,0,0],
             [0,1,0,1,0],
             [0,0,1,0,1],
             [1,0,0,1,0]]
    m = 3
    gc = GraphColoring(graph,m)

def tstPathMaze():
    maze =[[1,0,1,1,0],
           [1,0,1,1,1],
           [1,1,1,0,1],
           [0,1,1,1,1],
           [0,1,1,1,1]]
    
    mp = pathMaze(maze)

def main():
    tests = {
        "1": ("tstPermutation",  tstPermutation),
        "2": ("tstnQueens",      tstnQueens),
        "3": ("tstsumss",        tstsumss),
        "4": ("tstSudoku",       tstSudoku),
        "5": ("tstgraphColoring",tstgraphColoring),
        "6": ("tstPathMaze",     tstPathMaze),
    }

    while True:
        print("\n" + "=" * 40)
        for key, (name, _) in tests.items():
            print(f"  [{key}] {name}")
        print("  [0] 종료")
        print("=" * 40)

        choice = input("번호 입력 → ").strip()

        if choice == "0":
            print("종료합니다.")
            break
        elif choice in tests:
            name, fn = tests[choice]
            print(f"\n--- {name} ---")
            fn()
            print("\n[m] 메뉴로  [0] 종료")
            after = input("→ ").strip()
            if after == "0":
                print("종료합니다.")
                break
        else:
            print("없는 번호입니다.")

if __name__=="__main__":
    main()
