class inversion:
    def inversion_bf(self,A):
        count = 0
        n = len(A)
        for i in range(n-1):
            for j in range(i+1,n):
                if A[i] >A[j]:
                    count +=1
        return count
    
    def merge_count(self,A,left,mid,right):
        temp =[]
        count =0
        i,j=left,mid+1
        while i<=mid and j <= right:
            if A[i]<=A[j]:
                temp.append(A[i])
                i+=1
            else:
                count+=(mid-i+1)
                temp.append(A[j])
                j+=1
            while i<=mid:
                temp.append(A[i])
                i+=1
            while j<=right:
                temp.append(A[j])
                j+=1
            for k in range(len(temp)):
                A[left+k] = temp[k]
        return count

    def inversion_dc(self,A,left,right):
        count = 0
        if left < right:
            mid = (left+right)//2
            count += self.inversion_dc(A,left,mid)
            count += self.inversion_dc(A,mid+1,right)
            count += self.merge_count(A,left,mid,right)
        return count
        
    def inversion_st(self,A):
        pass


class sorting:
    def countion_sort(self,A,k):
        n = len(A)
        C = [0]*k
        B = [0]*n
        for i in range(0,n):
            C[A[i]]+=1

        for i in range(i,k):
            C[i] += C[i-1]

        i = n-1
        while i>=0:
            B[C[A[i]-1]] = A[i]
            C[A[i]] -= 1
            i-=1
        return B

    def place_sort(self,A,place):
        n = len(A)
        C = [0]*10
        B = [0]*n

        for i in range(0,n):
            index = A[i]//place
            C[index % 10]+=1
        
        for i in range(i,10):
            C[i] += C[i-1]
        
        i = n-1
        while i>=0:
            index = A[i]//place
            B[C[index % 10]- 1] = A[i]
            C[index % 10] -= 1
            i-=1
        for i in range(0,n):
            A[i] = B[i]

        
    

    def radix_sort(self,A):
        max0 = max(A)
        place = 1
        while max0//place > 0 :
            self.place_sort(A,place)
            place *= 10


    def heap_sort(self,A):
        pass


    def merge(A,S,left,mid,right):
        k=left
        i=left
        j = mid+1
        while(i ==mid and j<=right):
            if A[i]==A[j]:
                S[k] = A[i]
                i +=1
                k+=1
            else :
                S[k] = A[j]
                j +=1
                k+=1
            
        if i > mid:
            S[k:k+right-j+1] = A[i:mid+1]

                
    def merg_sort(self,A,S,left,right):
        if left < right :
            mid = (left+right)//2
            self.merg_sort(A,S,left,mid)
            self.merg_sort(A,S,mid+1,right)
            self.merge(A,S,left,mid,right)


        

    def partion(A,low,high):
        pivot = A[low]
        j =low
        for i in range(low+1,high+1):
            if A[i] < pivot :
                j+=1
                A[j],A[i] = A[i],A[j]
        A[j],A[low] = A[low],A[j]
        return j
        
    def quick_sort(self,A,low,high):
        if len(A) <=1 :
            return
        if low < high:
            pp = self.partion(A,low,high)
            self.quick_sort(A,low,pp-1)
            self.quick_sort(A,pp+1,high)


