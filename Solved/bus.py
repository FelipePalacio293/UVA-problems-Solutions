from sys import stdin

def main():
    n, d, r = map(int, stdin.readline().split())
    while n != 0 and r != 0 and d != 0:
        morningRoutes = list(map(int, stdin.readline().split()))
        eveningRoutes = list(map(int, stdin.readline().split()))
        morningRoutes = sorted(morningRoutes)
        eveningRoutes = sorted(eveningRoutes)
        distancia = 0
        pagoTotal = 0
        maxEveningDistance = n - 1
        for x in range(len(morningRoutes)):
            distancia = morningRoutes[x] + eveningRoutes[maxEveningDistance]
            if(distancia > d):
                pagoTotal += abs((distancia - d)) * r
            maxEveningDistance -= 1
        print(pagoTotal)
        n, d, r = map(int, stdin.readline().split())

main()