
class ChangeMaking:
    def cmDP(self, coins, amount):
        F = [float('inf')] * (amount + 1)
        F[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    F[i] = min(F[i], F[i - coin] + 1)
        
    def cmGA(self, coins, amount):
        coins.sort(reverse=True)
        S =[]
        tCoins = 0
        for coin in coins:
            count = amount // coin
            if count > 0:
                S.append((coin, count))
                tCoins += count
                amount = amount % coin
        if amount != 0:
            print("Exact change cannot be made...")
        return S, tCoins
    
class Scheduling:
    def sTotalTime(self,jobs):
        #jobs = [('J1',6), ('J2',65), ('J3',16), ('J4',26)]
        jobs.sort(key=lambda x: x[1])
        cTime = 0
        tTime = 0
        S= []
        for job,t in jobs:
            cTime += t
            S.append((job, cTime))
            tTime += cTime
        return S, tTime
    
    def sJobsDeadLines(self,jobs):
        #jobs = [('J1',2, 20), ('J2',1, 25), ('J3',3, 40), ('J4',2, 10), ('J5',1, 40)]
        jobs.sort(key=lambda x: x[2], reverse=True)
        maxDeadline = max(job[1] for job in jobs)
        slots = [False] * ( maxDeadline + 1 )
        S = [None] * ( maxDeadline + 1 )
        tprofit = 0
        for job,dl,p in jobs:
            for j in range(dl,0,-1):
                if not slots[j]:
                    slots[j] = True
                    S[j] = job
                    tprofit += p
                    break
            sjobs = [job for job in S if job is not None]
        return sjobs, S, tprofit
      