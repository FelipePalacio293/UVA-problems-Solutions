from sys import stdin

graph = []
visitado = []
weights = []
sum = 0
nodosVisitados = list()

def dfs(u):
    global graph
    global visitado
    global sum
    global nodosVisitados

    visitado[u] = 1
    mayor = float('-inf')
    node = None
    for v in graph[u]:
        if weights[v] > mayor and visitado[v] == 0:
            mayor = weights[v]
            node = v
    if(node):
        nodosVisitados.append(node)
        sum += mayor
        visitado[node] = 1
        dfs(node)
    
def main():
    global graph
    global visitado
    global weights
    global sum
    global nodosVisitados
    cases = int(stdin.readline())
    cont = 1
    while cases:
        stdin.readline()
        n, m = list(map(int, stdin.readline().split()))
        graph = [[] for _ in range(n)]
        visitado = [0 for _ in range(n)]
        nodosVisitados = []
        sum = 0
        weights = list(map(int, stdin.readline().split()))
        for _ in range(m):
            v, w = list(map(int, stdin.readline().split()))
            graph[v].append(w)
        dfs(0)
        print(f'Case {cont}: {sum} {nodosVisitados[len(nodosVisitados) - 1]}')
        cases -= 1
        cont += 1

main()