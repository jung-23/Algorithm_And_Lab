from lab06 import chainmatries

def tstCMM():
    cm=chainmatries()

    n =10
    # dims = cm.getDims(n)
    dims = [5,2,3,4,6,7,8]
    n=len(dims)-1
    print(dims)
    P,M = cm.cmmDP(dims)
    print('matrix M')
    for r in M:
        print(r)
    print('matrix P')
    for r in P:
        print(r)
    
    cm.printOrder(P,0,n-1)


def main():
    tstCMM()

if __name__=="__main__":
    main()