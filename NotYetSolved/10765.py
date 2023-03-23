from sys import stdin

# Carlos Felipe Palacio Lozano
# Basado en el código de Carlos Ramírez

low = [-1 for _ in range(10005)]
padre = [-1 for _ in range(10005)]
numHijos = [-1 for _ in range(10005)]
adj = [[ ] for _ in range(10005)]
visitado = [False for _ in range(10005)]
n = 0
t = 0

def apAux(v):
    global numHijos, n, padre, adj, t
    t += 1
    visitado[v] = t
    low[v] = t
    for w in adj[v]:
        if visitado[w] == -1:
            padre[w] = v
            apAux(w)
            low[v] = min(low[v],low[w])
            if(low[w] >= visitado[v]):
                numHijos[v] += 1
        elif w != padre[v]:
            low[v] = min(low[v], visitado[w])

def ap():
    for i in range(n):
        low[i] = -1
        visitado[i] = -1
        padre[i] = -1
    for i in range(n):
        if visitado[i] == -1:
            apAux(i)

def comparar( a, b ):
    if a[1] == b[1]:
        return a[0] < b[0]
    else:
        return a[1] > b[1]

def main():
    global numHijos, n, padre, adj
    n, m = list(map(int, stdin.readline().split()))
    while(n != 0 and m != 0):
        for i in range(n):
            adj[i].clear()
        u, v = list(map(int, stdin.readline().split()))
        while(u + v != -2):
            adj[u].append(v)
            adj[v].append(u)
            u, v = list(map(int, stdin.readline().split()))
        ap()
        apNodos = []
        numHijos[0] -= 1
        for i in range(n):
            apNodos.append([i, numHijos[i]])
        #apNodos.sort(key=comparar(apNodos, apNodos)) No supe hacer el tema del sort, pero intenté hacer el resto
        #como me lo imaginaba. 
        i = 0
        j = 0
        while i != len(apNodos) and m > j:
            print( apNodos[i][0], apNodos[i][1])
            i += 1
            j += 1

main()