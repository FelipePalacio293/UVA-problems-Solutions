# Carlos Felipe Palacio 11/08/2021
# Entrada: 
# Salida: 
from sys import stdin

def encontrarCandidatoGanador(partidos):
    mayor = 0
    partidoGanador = ""
    candidatoGanador = ""
    for i in partidos:
        if partidos[i][1] > mayor:
            mayor = partidos[i][1]
            partidoGanador = partidos[i][0]
            candidatoGanador = i
    return mayor, partidoGanador, candidatoGanador

def verificarEmpate(datosElecciones, mayor, candidatoGanador, partidoGanador):
    for candidato in datosElecciones:
        if datosElecciones[candidato][1] == mayor and candidato != candidatoGanador:
            partidoGanador = "tie"
    return partidoGanador

def main():
    listaImprimir = []
    reps = int(stdin.readline())
    while reps != 0:
        if stdin.readline() != "":
            cantCandidatos = int(stdin.readline())
            datosElecciones = {}
            for i in range(cantCandidatos):
               candidato = stdin.readline().strip()
               nombrePartido = stdin.readline().strip()
               datosElecciones[candidato] = [nombrePartido, 0]
            numeroVotos = int(stdin.readline())
            nombresCandidatos = datosElecciones.keys()
            for i in range(numeroVotos):
                temp = stdin.readline().strip()
                if temp in nombresCandidatos:
                    datosElecciones[temp][1] += 1
            partidoGanador = ""
            mayor, partidoGanador, candidatoGanador = encontrarCandidatoGanador(datosElecciones)
            listaImprimir.append(verificarEmpate(datosElecciones, mayor, candidatoGanador, partidoGanador))
            reps -= 1
    w = 0
    while w < len(listaImprimir) - 1:
        print(str(listaImprimir[w]) + "\n")
        w += 1
    print(listaImprimir[w])
main()
