# Carlos Felipe Palacio Lozano 8956397

"""
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali, los valores éticos y la integridad son tan importantes como la excelencia académica. En este curso se espera que los estudiantes se comporten ética y honestamente, con los más altos niveles de integridad escolar. En particular, se asume que cada estudiante adopta el siguiente código de honor:
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo a seguir los más altos estándares de integridad académica.
Integridad académica se refiere a ser honesto, dar crédito a quien se lo merece y respetar el trabajo de los demás. Por eso es importante evitar plagiar, engañar, “hacer trampa”, etc. En particular, el acto de entregar un programa de computador ajeno como propio constituye un acto de plagio; cambiar el nombre de las variables, agregar o eliminar comentarios y reorganizar los comandos no cambia el hecho de que se está copiando el programa de alguien más. Para más detalles consultar el Reglamento de Estudiantes, Sección VI.
"""
"""
Entrada:
    g(int) : grupo actual
    n(int) : cantidad máxima de grupos
Funcionamiento: Si el grupo actual (g) es mayor que la cantidad máxima de grupos (n), entonces, debe reiniciar el grupo actual de tal forma que quede en la posicion correcta.
Salida: 
    g(int) : grupo actual sin el offset de n
"""
def resetNextGroup(g, n):
    if(g >= n):
        g = g - n
    return g

"""
Entrada: 
    l(int) : cantidad de plazas que hay en la montaña rusa
    c(int) : cantidad de veces que se puede usar la montaña rusa por día
    n(int) : cantidad de grupos 
    pi(list) : cada posicion corresponde el tamaño de un grupo
Funcionamiento: Se cálcula la mayor cantidad de ganancias que se puede obtener con las entradas recibidas. De tal forma que se itera con base a la cantidad de veces que funciona la montaña rusa por día, y luego, se itera hasta que el numero de plazas de la montaña rusa esté llena o sea lo máximo posible.
Salida: earns(int) : Mayor cantidad de ganancias para el parque de atracciones
"""
def calculateEarnings(l, c, n, pi):
    x = 0
    earns = 0
    mem = {}
    for x in range(n):
        actualGroup = pi[x]
        totalSize = actualGroup
        ans = True
        numOfGroups = 0
        nextGroup = x + 1
        nextGroup = resetNextGroup(nextGroup, n)
        while ans:
            if(totalSize + pi[nextGroup] <= l and numOfGroups < n - 1):
                element = pi[nextGroup]
                totalSize += element
                nextGroup += 1
                nextGroup = resetNextGroup(nextGroup, n)
            else:
                ans = False
            numOfGroups += 1
        mem[(actualGroup, x)] = (totalSize, (pi[nextGroup], nextGroup))
    
    element = mem[(pi[0], 0)]
    earns += element[0]
    next = element[1]
    
    for x in range(c - 1):
        element = mem[(next)]
        earns += element[0]
        next = element[1]
    return earns

"""
Funcionamiento: La función main únicamente lee las entradas del problema.
"""      
def main():
    l, c, n = [int(i) for i in input().split()]
    pi = list()
    for i in range(n):
        pi.append(int(input()))
    print(calculateEarnings(l, c, n, pi))

main()