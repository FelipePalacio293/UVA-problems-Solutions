# Carlos Felipe Palacio 11/08/2021 

from heapq import heappush, heappop
from sys import stdin
def main():
    casos = int(stdin.readline())
    for x in range(casos):
        cantidadMedicamentos, cantidadMostrar = list(map(int, stdin.readline().split()))
        lista = []
        for y in range(cantidadMedicamentos):
            med = stdin.readline().split()
            heappush(lista, [int(med[1]), y , med[0], int(med[1])]) # Se agregan los datos al heap. Posicion 0: minutos iniciales
            # posicion 1: prioridad por orden de llegada. posicion 2: nombre. posicion 3: minutos no variantes.
        for w in range(cantidadMostrar):            
            print(f"{lista[0][0]} {lista[0][2]}")
            heappush(lista, [lista[0][0] + lista[0][3], lista[0][1], lista[0][2], lista[0][3]]) # Se agrega a la heap los mismos datos, pero aumentando los minutos.
            heappop(lista)
main()