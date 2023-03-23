# Carlos Felipe Palacio

from sys import stdin

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        line  = stdin.readline().split()
        n, m = int(line[0]), int(line[1])
        casas = []
        for _ in range(m):
            casas.append(int(stdin.readline()))
        casas.sort()
        low, hi = 0, casas[len(casas) - 1]
        while(hi - low > 1):
            mid = (hi + low) / 2
            distancia = casas[0] + mid
            cantidad = 0
            for x in range(m):
                if(casas[x] > distancia):
                    distancia = casas[x] + mid
                    cantidad += 1
            if(cantidad >= n):
                low = mid
            else:
                hi = mid
        
        print("%.1f" % (int(hi) / 2))
main()