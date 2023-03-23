from sys import stdin
# Carlos Felipe Palacio Lozano

# Implementacion de disjointset union basada en la del profesor Carlos Alberto Ramirez.
# operaciones disjoint set union
# **************************************

def makeSet(v, p, rango):
    p[v], rango[v] = v, 0

def findSet(v, p, rango):
    ans = None
    if v == p[v]: 
        ans = v
    else:
        temp = findSet(p[v], p, rango)
        rango[v] += rango[p[v]]
        p[v] = temp
        ans = temp
    return ans

def unionSet(u, v, p, rango):
    p[u] = v
    rango[u] = abs(v - u) % (1000)

# ****************************************

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        numOfEnterprises = int(stdin.readline())
        p, rango = [0 for _ in range(numOfEnterprises + 1)], [0 for _ in range(numOfEnterprises + 1)]
        for y in range(1, numOfEnterprises + 1):
            makeSet(y, p, rango)
        testCase = stdin.readline().split()
        while(testCase != ["O"]):
            if(testCase[0] == "E"):
                rango[findSet(int(testCase[1]), p, rango)]
                print(rango[int(testCase[1])])
            elif(testCase[0] == "I"):
                unionSet(int(testCase[1]), int(testCase[2]), p, rango)
            testCase = stdin.readline().split()
            
main()