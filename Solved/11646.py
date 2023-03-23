# Carlos Felipe Palacio 31/08/2021 

from sys import stdin
import math

EPS = 1e-12

def encontrarArco(mid, r):
    return (math.acos(mid / (2 * r))) * 2 * r 

def encontrarRadio(mid, a, b):
    return math.sqrt((((mid ** 2) / 4) + ((b ** 2) * (mid ** 2)) / (4 * (a ** 2))))

def main():
    datos = stdin.readline()
    caso = 1
    while datos != "":
        a = int(datos[0])
        b = int(datos[2])
        low = 0
        hi = 200
        while hi - low > EPS:
            mid = (low + hi) / 2
            lado = encontrarRadio(mid, a, b)
            arco = encontrarArco(mid, lado)
            if ((2 * mid) + (2 * arco)) > 400:
                hi = mid
            else:
                low = mid
        print("Case %d: %.10f %.10f" % (caso, mid, (b * mid) / a))
        datos = stdin.readline()
        caso += 1
main()