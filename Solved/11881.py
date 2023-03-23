# Carlos Felipe Palacio 31/08/2021 
from sys import stdin

EPS = 1e-6

def calcularFormula(numEcuaciones, listaEcuaciones, valorCalculado):
    nvm = 0
    for i in range(numEcuaciones + 1):
        nvm += listaEcuaciones[i] / (1 + valorCalculado) ** i
    return nvm

def main():
    numEcuaciones = int(input())
    while(numEcuaciones != 0):
        listaEcuaciones = list(map(int, stdin.readline().split()))
        hi = 10000
        low = -1
        while(hi - low > EPS):
            mid = (hi + low) / 2
            nvm = calcularFormula(numEcuaciones, listaEcuaciones, mid)
            if(nvm > 0):
                low = mid
            else:
                hi = mid
        print("%.2f" %mid)
        numEcuaciones = int(input())

main()