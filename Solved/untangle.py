from sys import stdin

# La funcion lis y find_idx fueron tomadas de la clase del 09/22 dada por Camilo Rocha. 

def find_idx(a, low, hi, x):
    while low + 1 != hi:
        mid = low + ((hi - low) >> 1)
        if(a[mid] > x): hi = mid
        else: low = mid
    return hi

def lis(a):
    ans = [a[0][1]]
    for n in range(1, len(a)):
        if ans[-1] <= a[n][1]: ans.append(a[n][1])
        else: ans[find_idx(ans, -1, len(ans) - 1, a[n][1])] = a[n][1]
    return len(ans)

def main():
    N = int(stdin.readline())
    while(N != 0):
        matrix = []
        hRopes = list(map(int, stdin.readline().split()))
        bRopes = list(map(int, stdin.readline().split()))
        [matrix.append((hRopes[x], bRopes[x])) for x in range(N)]
        matrix.sort()
        print(lis(matrix), end=' ')
        matrix.sort(reverse = True)
        print(lis(matrix))
        N = int(stdin.readline())
main()