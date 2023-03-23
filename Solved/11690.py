from sys import stdin

# Carlos Felipe Palacio

def tarjanAux(nodo, grafo):
    global t
    global visitado
    global low
    global enPila
    global pila
    global numGrupos
    global grupos
    t += 1
    visitado[nodo] = t
    low[nodo] = t
    pila.append(nodo)
    enPila[nodo] = True
    for i in range(1,len(grafo[nodo])):
        nodoVisitado = grafo[nodo][i][1]
        if visitado[nodoVisitado] == -1:
            tarjanAux(nodoVisitado, grafo)
            low[nodo] = min(low[nodo], low[nodoVisitado])
        elif enPila[nodoVisitado]:
            low[nodo] = min(low[nodo], visitado[nodoVisitado])
    if low[nodo] == visitado[nodo]:
        grupos.append([])
        numGrupos += 1
        while pila[-1] != nodo:
            a = pila.pop()
            enPila[a] = False
            grupos[numGrupos - 1].append(a)
        a = pila.pop()
        enPila[a] = False
        grupos[numGrupos - 1].append(a)

def tarjan(grafo, n, m):
    global t
    global visitado
    global low
    global enPila
    global pila
    global numGrupos
    global grupos
    numGrupos = 0
    grupos = []
    t = 0
    visitado = []
    low = []
    enPila = []
    pila = []
    for i in range(n):
        visitado.append(-1)
        low.append(-1)
        enPila.append(False)
    for i in range(n):
        if visitado[i] == -1:
            tarjanAux(i, grafo)
    return grupos

def comprobarPosible(grupos, grafo):
    acum = 0
    for i in range(len(grupos)):
        for j in range(len(grupos[i])):
            acum += grafo[grupos[i][j]][0]
        if(acum != 0):
            return 0
    return 1
        
def main():
    cases = int(input())
    for i in range(cases):
        n, m = list(map(int, stdin.readline().split()))
        grafo = []
        for j in range(n):
            numNodo = int(input())
            grafo.append([numNodo])
        for j in range(m):
            inicioArista, finalArista = list(map(int, stdin.readline().split()))
            grafo[inicioArista].append((inicioArista, finalArista))
            grafo[finalArista].append((finalArista, inicioArista))
        grupos = tarjan(grafo, n, m)
        posibilidad = comprobarPosible(grupos, grafo)
        if(posibilidad == 1):
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")

main()