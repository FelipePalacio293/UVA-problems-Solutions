from sys import stdin
from collections import deque

adj = {}
m = int()
visitados = {}
dist = {}

def bfsAux(u, l):
    global visitados
    global adj
    global m
    global dist
    cola = deque()
    cola.append((u, 0))
    dist[u] = 0
    visitados[u] = True
    flag = True

    while flag and len(cola) != 0:
        w, c = cola.popleft()
        # print(w)
        if w == l:
            flag = False
        else:
            for v in adj[w]:
                if not visitados[v]:
                    cola.append((v, c + 1))
                    dist[v] = c + 1
                    visitados[v] = True
    return dist[l]

def main():
    global visitados
    global adj
    global m
    global dist
    c = int(stdin.readline())
    acum = 1
    print("SHIPPING ROUTES OUTPUT\n")
    while(c):
        m, n, p = map(int, stdin.readline().split())
        adj = {}
        nodes = stdin.readline().split()
        
        for x in nodes:
            adj[x] = []
        for x in range(n):
            fnode, snode = map(str, stdin.readline().split())
            adj[fnode].append(snode)
            adj[snode].append(fnode)
        print(f"DATA SET  {acum}\n")
        for x in range(p):
            dist = {x : float("-inf") for x in nodes}
            visitados = {x : False for x in nodes}
            value, origen, destine = map(str, stdin.readline().split())
            distance = bfsAux(origen, destine)
            if(distance == float("-inf")):
                print("NO SHIPMENT POSSIBLE")
            else:
                cost = int(value) * distance  * 100
                print(f"${cost}")
        print("")
        acum += 1
        c -= 1
    print("END OF OUTPUT")
main()