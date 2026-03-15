from lab01 import xpowern, Fibonacci, Search, Hanoi

def test_power():
    p=xpowern()
    print(p.power1(2, 10))
    print(p.power2(2, 10))
    print(p.power3(2, 10))

def test_fibonacci():
    f=Fibonacci()
    print(f.fib1(10))
    print(f.fib2(10))
    print(f.fib3(10)[0])

def test_SS():
    lab=Search()
    S=[3,7,22,45,9,8,34,12]
    loc = lab.sequential_search(S,11)
    if loc==-1:
        print("Elemet Not found...")
    else:
        print("element found at index{}".format(loc))

def test_EU():
    lab = Search()
    S = [3, 7, 22, 45, 9, 22, 34, 12]
    print(lab.element_uniqueness(S))

def test_BE():
    lab = Search()
    A = [
        [4,6,1,4],
        [3,2,1,1],
        [14,16,1,14]
    ]
    for r in A:
        print(r)
    R = lab.Guassian_elemention(A)
    for r in R:
        print(r)

def test_hanoi():
    lab = Hanoi()
    N = 5
    lab.hanoi(N,1,2,3)


def main():
    test_power()
    test_fibonacci()
    test_SS()
    test_EU()
    test_BE()
    test_hanoi()


if __name__=="__main__":
    main()
