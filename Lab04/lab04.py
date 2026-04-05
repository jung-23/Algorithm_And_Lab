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
            
        max_val = max(A) + 1
        bit = [0]*(max_val+1)

        def update(i):
            while i <= max_val:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        count = 0

        for i in range(len(A)-1, -1, -1):
            count += query(A[i]-1)
            update(A[i])

        return count


class sorting:
    def countion_sort(self,A,k):
        n = len(A)
        C = [0]*k
        B = [0]*n
        for i in range(0,n):
            C[A[i]]+=1

        for i in range(1,k):
            C[i] += C[i-1]

        i = n-1
        while i>=0:
            B[C[A[i]]-1] = A[i]
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
        
        for i in range(1,10):
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
        return A

    def heapify(self, A, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and A[left] > A[largest]:
            largest = left

        if right < n and A[right] > A[largest]:
            largest = right

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(A, n, largest)

    def heap_sort(self,A):
        n = len(A)

        for i in range(n//2 - 1, -1, -1):
            self.heapify(A, n, i)

        for i in range(n-1, 0, -1):
            A[0], A[i] = A[i], A[0]  
            self.heapify(A, i, 0)

        return A


    def merge(self,A,S,left,mid,right):
        k=left
        i=left
        j = mid+1
        while(i <=mid and j<=right):
            if A[i]<=A[j]:
                S[k] = A[i]
                i +=1
                k+=1
            else :
                S[k] = A[j]
                j +=1
                k+=1
            
        if i > mid:
            S[k:k+right-j+1] = A[j:right+1]
        else:
            S[k:k+mid-i+1] = A[i:mid+1]
        
        A[left:right+1] = S[left:right+1]
                
    def merg_sort(self,A,S,left,right):
        if left < right :
            mid = (left+right)//2
            self.merg_sort(A,S,left,mid)
            self.merg_sort(A,S,mid+1,right)
            self.merge(A,S,left,mid,right)
        return A


        

    def partion(self,A,low,high):
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
        return A


class merge_sort_3way:

    def merge_3way(self, A, left, mid1, mid2, right):
        i = left
        j = mid1 + 1
        k = mid2 + 1

        temp = []

        while i <= mid1 or j <= mid2 or k <= right:

            values = []

            if i <= mid1:
                values.append((A[i], 'i'))
            if j <= mid2:
                values.append((A[j], 'j'))
            if k <= right:
                values.append((A[k], 'k'))

            val, idx = min(values)
            temp.append(val)

            if idx == 'i':
                i += 1
            elif idx == 'j':
                j += 1
            else:
                k += 1

        for t in range(len(temp)):
            A[left + t] = temp[t]


    def merge_sort_3way(self, A, left, right):

        if left < right:

            third = (right - left) // 3

            mid1 = left + third
            mid2 = mid1 + third + 1

            self.merge_sort_3way(A, left, mid1)
            self.merge_sort_3way(A, mid1 + 1, mid2)
            self.merge_sort_3way(A, mid2 + 1, right)

            self.merge_3way(A, left, mid1, mid2, right)
        return A