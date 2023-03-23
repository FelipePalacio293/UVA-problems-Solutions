import heapq
from sys import stdin

def minsum():
    cases = int(stdin.readline())
    lista = []
    sum = 0
    sumas = []
    while(cases != ""):
        cases = int(cases)
        for x in range(cases):
            lista.append([])
            num = input().split()
            for w in range(cases):
                lista[x].append(int(num[w]))
                # sum += lista[0]
        for y in range(cases):
            heapq.heapify(lista[y])
        for x in range(cases):
            sum += lista[x][0]
        sumas.append(sum)
        for x in range(cases - 1):
            mayor = float("-inf")
            encontrado = -1
            sum = 0
            for y in range(cases):
                if(lista[y][0] > mayor and lista[y][0] != 0 and lista[y][0] != 1):
                    mayor = lista[y][0]
                    encontrado = y
            if(encontrado != -1):
                heapq.heappop(lista[encontrado])
            for y in range(cases):
                if(len(lista[y]) != 0):
                    print(lista[y])
                    sum += lista[y][0]
            sumas.append(sum)
            print("sumas ", sumas)
        
        sum = 0
        sumas = []
        lista = []
        cases = stdin.readline()
minsum()