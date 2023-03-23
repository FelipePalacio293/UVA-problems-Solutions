from sys import stdin

class Arbol:
  def __init__(self, first):
    self.first = first

class Hoja:
  def __init__(self):
    self.hijos = []
    self.palos = 0
  
  def agregarHijo(self, hijo):
    self.hijos.append(hijo)

def phi(hoja, n):
  if len(hoja.hijos) > 0:
    cantPalos = 0
    tamano = 0
    for i in hoja.hijos:
      ans = phi(i, n)
      cantPalos += i.palos
      tamano = max(tamano, ans)
    tamano += 1
    if tamano > n:
      cantPalos += 1
      tamano = 0
    hoja.palos = cantPalos
    return tamano
  else:
    return 1

def main():
  linea = stdin.readline()
  while len(linea) > 0:
    nodos, lineas, n = [int(_) for _ in linea.split()]
    listaNodos = [Hoja() for _ in range(nodos)]
    for i in range(lineas):
      linea = input().split()
      for j in linea[1:]:
        listaNodos[int(linea[0])].agregarHijo(listaNodos[int(j)])
    phi(listaNodos[0], n)
    print(listaNodos[0].palos)
    linea = stdin.readline()

main()