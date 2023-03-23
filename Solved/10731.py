from sys import stdin

MAX = 10000
adj = {}
visitado = {}
sccInd = {}
n, t, numSCC = int(), 0, 0
sccNodos, pilaS, pilaP = [], [], []

def gabow():
    global sccInd, visitado, n, t, numSCC, sccNodos, pilaS, pilaP
    n, t, numSCC = int(), 0, 0
    sccNodos, pilaS, pilaP = [], [], []
    visitado = {}
    sccInd = {}
    for i in adj.keys():
        sccInd[i], visitado[i] = -1, -1
        for y in range(len(adj[i])):
            sccInd[adj[i][y]], visitado[adj[i][y]] = -1, -1
            
    for i in adj.keys():
        if visitado[i] == -1:
            gabowAux(i)

def gabowAux(v):
    global t, numSCC
    t += 1
    visitado[v] = t
    pilaS.append(v)
    pilaP.append(v)

    for i in range(len(adj[v])):
        w = adj[v][i]
        if visitado[w] == -1:
            gabowAux(w)
        elif sccInd[w] == -1:
            while visitado[pilaP[-1]] > visitado[w]:
                pilaP.pop()

    if v == pilaP[-1]:
        numSCC += 1
        sccNodos.append([])
        while pilaS[-1] != v:
            a = pilaS.pop()
            sccInd[a] = numSCC - 1
            sccNodos[numSCC - 1].append(a)

        a = pilaS.pop()
        sccInd[a] = numSCC - 1
        sccNodos[numSCC - 1].append(a)
        pilaP.pop()

def sort_list(x):
    if type(x) == list:
        x.sort()
        return (1, x)
    else:
        return (0, x)


def main():
    global sccNodos
    global adj
    n = int(stdin.readline())
    while(n != 0):
        adj = {}
        for x in range(n):
            line = list(map(str, stdin.readline().split()))
            if(line[0] not in adj.keys()):
                adj[line[0]] = []
            if(line[1] not in adj.keys()):
                adj[line[1]] = []
            if(line[2] not in adj.keys()):
                adj[line[2]] = []
            if(line[3] not in adj.keys()):
                adj[line[3]] = []
            if(line[4] not in adj.keys()):
                adj[line[4]] = []
            if line[5] not in adj.keys():
                adj[line[5]] = line[0: 5]
            else:
                adj[line[5]] = list(set(adj[line[5]] + line[0: 5]))
        gabow()
        sccNodos = sorted(sccNodos, key=sort_list)
        for x in sccNodos:
            print(*x)

        n = int(stdin.readline())
        if n != 0:
            print()
main()