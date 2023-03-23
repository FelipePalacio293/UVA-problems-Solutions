from sys import stdin

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        n = int(stdin.readline())
        heights = stdin.readline().split()
        lista = []
        for x in range(n):
            lista.append(int(heights[x]))

main()