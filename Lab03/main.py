from lab03 import MSSP

def tst_mssp():
    l3=MSSP()
    A= [2,-3,5,-9,6,7,-4,5,-2,1,-3,8]
    print("Brute force {}",format(l3.mssp_bf(A)))
    print("DC {}",format(l3.mssp_dc(A)))
    print("Dp {}",format(l3.mssp_bf(A)))

def main():
    tst_mssp()
    
    
    
if __name__ =="main":
    main()