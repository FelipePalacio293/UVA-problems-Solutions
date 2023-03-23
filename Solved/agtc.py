from sys import stdin

# Codigo tomado del profesor Camilo Rocha en la clase del 09/01 sobre programacion dinamica

def msedtab(A, B):
    M, N = len(A), len(B)
    tab = [ [ None for _ in range(N + 1) ] for _ in range(M + 1) ]
    for n in range(N + 1): tab[0][n] = n
    for m in range(M + 1): tab[m][0] = m
    m, n = 1, 1
    while m != M + 1:
        if n == N + 1:
            m, n = m + 1,1
        else:
            if A[m - 1]== B[n - 1]:
                tab[m][n] = tab[m - 1][n - 1]
            else:
                tab[m][n] = 1 + min(tab[m - 1][n - 1], min(tab[m - 1][n], tab[m][n - 1]))
            n += 1
    return tab[M][N]

def main():
    cadenaUno = list(map(str, stdin.readline().split()))
    cadenaDos = list(map(str, stdin.readline().split()))
    while cadenaUno != []:
        cadenaUno = cadenaUno[1]
        cadenaDos = cadenaDos[1]
        print(msedtab(cadenaUno, cadenaDos))
        cadenaUno = list(map(str, stdin.readline().split()))
        cadenaDos = list(map(str, stdin.readline().split()))
main()