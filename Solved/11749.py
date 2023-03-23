from sys import stdin

# Carlos Felipe Palacio Lozano
# Basado en el código de Carlos Ramírez

MAX = 505
caminos = [[ ] for _ in range(MAX)]
visitados = [False for _ in range(MAX)]
cantCiudades = 0
n = 0
maxNumCiudad = 0

def dfsAux(v):
    global cantCiudades
    visitados[v] = True
    cantCiudades += 1
    for u in caminos[v]:
        if not visitados[u]:
            dfsAux(u)

def dfs():
    global cantCiudades, maxNumCiudad, n
    for i in range(n + 1):
        visitados[i] = False
    for i in range(n):
        if not visitados[i]:
            cantCiudades = 0
            dfsAux(i)
            maxNumCiudad = max(maxNumCiudad, cantCiudades)

def main():
    global n, maxNumCiudad
    n, m = list(map(int, stdin.readline().split()))
    while(n != 0 and m != 0):
        dic = {}
        mayorPPA = float("-inf")
        maxNumCiudad = 0
        for i in range(n + 1):
            caminos[i].clear()
        for i in range(m):
            u, v, PPA = list(map(int, stdin.readline().split()))
            dic[f'u{i}'] = u
            dic[f'v{i}'] = v
            dic[f'PPA{i}'] = PPA
            mayorPPA = max(mayorPPA, PPA)
            if(dic[f'PPA{i}'] == mayorPPA):
                caminos[dic[f'u{i}']].append(dic[f'v{i}'])
                caminos[dic[f'v{i}']].append(dic[f'u{i}'])
        dfs()
        print(maxNumCiudad)
        n, m = list(map(int, stdin.readline().split()))

main()