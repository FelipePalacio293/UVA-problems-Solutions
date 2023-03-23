from sys import stdin

# Algoritmo de busqueda binaria tomado de el libro de notas de clase del curso de analisis y disenio de algoritmos

def binsearch(A, x):
    N, ans = len(A),False
    if N != 0:
        low, hi = 0,N
        # C0 ∧ C1
        while low + 1 != hi:
            mid = low+((hi-low)>>1) # mid = (low+hi)//2
            if A[mid] <= x: 
                low = mid
            else: 
                hi = mid
    if(A[low] < x):
        return hi
    else:
        return low
        
def smallfactors():
    cases = int(stdin.readline())
    temp = []
    for x in range(70):
        for y in range(70):
            temp.append((2 ** x) * (3 ** y))
    while(cases):
        temp.sort()
        print(temp[binsearch(temp, cases)])
        cases = int(stdin.readline())
smallfactors()