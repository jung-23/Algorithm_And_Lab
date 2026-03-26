from lab03 import MSSP,LZSS,LZSSM

def tst_mssp():
    l3=MSSP()
    A= [2,-3,5,-9,6,7,-4,5,-2,1,-3,8]
    print("\n>>> MSSP"+"-"*20)
    print("Brute force {}",format(l3.mssp_bf(A)))
    print("DC {}",format(l3.mssp_dc(A,0,len(A)-1)))
    print("Dp {}",format(l3.mssp_dp(len(A),A)))

def tst_LZSS():
    l3=LZSS()
    A= [2,-3,5,-9,6,7,-4,5,-2,1,-3,8]
    print("\n>>> LZSS"+"-"*20)
    print("Brute force {}",format(l3.LZSS_bf(A)))
    print("DC {}",format(l3.LZSS_dc(A,0,len(A)-1)))
    print("Prefix {}",format(l3.LZSS_Prefix(A)))

def tst_LZSSM():
    l3=LZSSM()
    A = [[1,2,-3],[3,-3,3],[1,-1,0]]
    print("\n>>> LZSSM"+"-"*20)
    print("Brute force {}",format(l3.LZSSM_BF(A)))
    print("Prefix {}",format(l3.LZSSM_Prefix(A)))
    print("RC {}",format(l3.LZSSM_RC(A)))


def main():
    tst_mssp()
    tst_LZSS()
    tst_LZSSM()
    
    
if __name__ == "__main__":
    main()