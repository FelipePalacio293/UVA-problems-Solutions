from sys import stdin
from tokenize import group

def listAlphabet():
    abc = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    dicc = {}
    for x in range(len(abc)):
        dicc[abc[x]] = x
    return dicc

def main():
    alphabet = listAlphabet()
    r, c = map(int, stdin.readline().split())
    while r != 0 and c != 0:
        p = int(stdin.readline())
        cine = [[0 for _ in range(c + 1)] for _ in range(r)]
        for x in range(p):
            silla, vaso = map(str, stdin.readline().split())
            posLetra = alphabet[silla[0]]
            postNum = int(silla[1:])
            cine[posLetra][postNum] = vaso
        p = int(stdin.readline())
        group = []
        for x in range(p):
            group.append(stdin.readline())
        r, c = map(int, stdin.readline().split())
main()