# MergeSort in Python

cont = 0
tmp = []
def mergesort(A, low, hi):
    if low + 1 < hi:
        mid = low + ((hi - low) >> 1) # mid = (low+hi)//2
        mergesort(A, low, mid) # induction hypothesis on the first half
        mergesort(A, mid, hi) # induction hypothesis on the second half
        merge(A, low, mid, hi) # combine the two halves preserving the order

def merge(A, low, mid, hi):
    global tmp # a global array at least the size of A
    global cont
    for i in range(low, hi): 
        tmp[i] = A[i] # copy A[low..hi) to tmp[low..hi)
    l, r = low, mid
    for n in range(low, hi):
        if l == mid: 
            A[n], r = tmp[r], r + 1 # only process the right half
        elif r == hi: 
            A[n], l = tmp[l], l + 1 # only process the left half
        else:
        # the first pending element of each half needs to be compared
            if tmp[l] <= tmp[r]: 
                A[n], l = tmp[l], l + 1 # choose the one on the left
            else: 
                A[n], r = tmp[r], r + 1 # choose the one on the right
                cont += 1
            
def numerosMayoritarios(A, x):
    N, ans = len(A), False
    if N != 0:
        low, hi, mid= 0, N, 0
        # C0 ∧ C1
        while low + 1 != hi:
            mid = low + ((hi - low) >> 1) # mid = (low+hi)//2
            
            if A[mid] <= x: 
                
                low = mid
            else: 
                
                hi = mid
            ans = A[low]==x
        if(ans):
            primeraPos = low + 1
            low, hi = 0, primeraPos
            while low + 1 != hi:
                
                mid = low+((hi-low)>>1) # mid = (low+hi)//2
                print(A[low:mid], A[mid:hi], mid, low, hi, A[mid - 1], A[mid])
                if(x > A[mid - 1]) and A[mid] <= x: 
                    low = mid
                else: 
                    hi = mid
                ans = A[low]==x
        else:
            return False
    if(ans):
        print(primeraPos - low) > N / 2
    else:
        print(1 > N / 2)

def main():
    global tmp
    global cont
    array2 = [3, 1, 2]
    tmp = [None for _ in range(len(array2))]
    print(*array2)
    cont = 0
    mergesort(array2, 0, len(array2))
    print(*array2)
    l = [1, ]
    print(binsearch(array2, 3))
    print(cont)
main()