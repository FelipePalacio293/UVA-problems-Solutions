from sys import stdin

visitados = [0 for _ in range(25)]

def solve(paths, graph, vertex, path, longitud):
    print(path)
    if longitud == paths:
        print(path)
        return path
    visitados[vertex] = 1
    for x in range(1, 5):
        if(vertex != x and graph[vertex][x] == 1 and visitados[vertex] == 0):
            solve(paths, graph, x, path + str(x), longitud + 1)
    visitados[vertex] = 0

def main():
    line = " "
    while(line != ''):
        n, k = map(int, stdin.readline().split())
        matriz = []
        line = list(map(int, stdin.readline().split()))
        matriz.append(line.copy())
        while(line != [-9999]):
            matriz.append(line.copy())
            solve(k, matriz, 1, '', 0)
            line = list(map(int, stdin.readline().split()))

main()