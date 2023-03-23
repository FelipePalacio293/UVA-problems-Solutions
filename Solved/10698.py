# Carlos Felipe Palacio 11/08/2021
from sys import stdin

def calcularDiferenciaDeGoles(datos):
    for x in range(len(datos)): 
        datos[x][6] = datos[x][4] - datos[x][5]

def calcularPorcentajeDePuntos(datos):
    for x in range(len(datos)):
        if(datos[x][3] > 0):
            datos[x][7] = datos[x][2] * 100 / (3 * datos[x][3])
        elif(datos[x][3] == 0):
            datos[x][7] = "N/A"

def main():
    nE, nP = list(map(int, stdin.readline().split()))
    
    while nE != 0 or nP != 0:
        datos = []
        equipos, resultadoPartidos = [0 for _ in range(nE)], [0 for _ in range(nP)]
        for i in range(nE):
            equipos[i] = str(stdin.readline().strip())
        for i in range(nP): 
            resultadoPartidos[i] = str(stdin.readline().strip())
        for j in equipos:
            datos.append([j, 0, 0, 0, 0, 0, 0, 0.0])
        for x in resultadoPartidos:
            w = x.split()
            for y in range(len(datos)): # Se agregan a la matriz los datos
                if(datos[y][0] == w[0]):
                    datos[y][3] += 1
                    datos[y][4] += int(w[1])
                    datos[y][5] += int(w[3])
                    if(int(w[1]) > int(w[3])):
                        datos[y][2] += 3
                    elif(int(w[1]) == int(w[3])):
                        datos[y][2] += 1
                if(datos[y][0] == w[4]):
                    datos[y][3] += 1
                    datos[y][4] += int(w[3])
                    datos[y][5] += int(w[1])
                    if(int(w[3]) > int(w[1])):
                        datos[y][2] += 3
                    elif(int(w[3]) == int(w[1])):
                        datos[y][2] += 1
        calcularDiferenciaDeGoles(datos)
        calcularPorcentajeDePuntos(datos)
        datos.sort(key = lambda x: (-x[2], -x[6], -x[4], x[0].lower())) # Se acomodan los elementos de tal forma que queden de mayor a menor segun cada campo
        num = 1
        for x in range(len(datos)):
            if(x == 0 or datos[x][2] < datos[x - 1][2] or datos[x][6] < datos[x - 1][6] or datos[x][4] < datos[x - 1][4]): # Se verifican las posiciones y se imprimen en orden
                print("%2d. " % num, end = "")
                num += 1
            else:
                num += 1
                print("    ", end = "" )
            print("%15s %3d %3d %3d %3d%4d " % (datos[x][0], datos[x][2], datos[x][3], datos[x][4], datos[x][5], datos[x][6]), end = "")
            if datos[x][3] == 0:
                datos[x][7] = "N/A"
                print("%6s" % datos[x][7])
            else:
                print("%6.2f" % datos[x][7])
        
        nE, nP = list(map(int, stdin.readline().split()))
        if nE != 0:
            print("")

main()