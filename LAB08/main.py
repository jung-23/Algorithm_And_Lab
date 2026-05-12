from lab08 import ChangeMaking, Scheduling

def tstCm():
    cm = ChangeMaking()
    coins = [1,5,10,25]
    amount = 69
    S, tCoins = cm.cmGA(coins, amount)
    print(S)
    print( "Total coins :", tCoins)

    print("Total coins by DP :", cm.cmDP(coins, amount))

def tstScheduling():
    s = Scheduling()
    jobs = [('J1',6), ('J2',65), ('J3',16), ('J4',26)]
    S, tTime = s.sTotalTime(jobs)
    print("Total time in System:", tTime)
    print(S)

    jobs = [('J1',2, 20), ('J2',1, 25), ('J3',3, 40), ('J4',2, 10), ('J5',1, 40)]
    sjobs, S, tprofit = s.sJobsDeadLines(jobs)
    print("Total profit:", tprofit)
    print(S)
    print(sjobs)


def main():
    tstCm()
    tstScheduling()


if __name__ == "__main__":    
    main()