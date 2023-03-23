from sys import stdin

def wedding(A, m, i, j, mem):
    if (i, j) in mem:
        ans = mem[(i, j)]
    else:
        if(i == len(A[j]) or j == len(A)):
            ans = 0
        else:
            mayor = float("-inf")
            for x in range(len(A[j])): 
                if(mayor < A[x]):
                    mayor = A[x]
        ans[(i, j)] = ans

def main():
    cases = int(stdin.readline())
    while(cases):
        line = stdin.readline().split()
        m, c = int(line[0]), int(line[1])
        
        lista = []
        for y in range(c):
            line = stdin.readline().split()
            lista.append([])
            for x in range(len(1, line)):
                lista[y].append(int(line[x]))
        print(lista)
        cases -= 1
main()