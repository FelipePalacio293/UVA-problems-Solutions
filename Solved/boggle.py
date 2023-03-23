# Carlos Felipe Palacio 8956397

from sys import stdin

offsetX = [-1, -1, 0, 1, 1, 1, 0, -1]
offsetY = [0, 1, 1, 1, 0, -1, -1, -1]
words = []

def find(boggle, word, posX, posY):
    if(len(word) >= 3):
        words.append(word)
    for i in range(8):
        char = boggle[posX + offsetX[i]][posY + offsetY[i]]
        if(char > word[-1] and char != "0"):
            find(boggle, word + char, posX + offsetX[i], posY + offsetY[i])
    
def findWords(boggle, N):
    global words
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            find(boggle, boggle[i][j], i, j)
    words = list(set(words))
    words = sorted(words)
    words = sorted(words, key = len)
    print('\n'.join(words))
    words = []

def main():
    cases = int(stdin.readline())
    ignore = stdin.readline()
    while(cases):
        boggle = []
        N = int(stdin.readline())
        ceros = "0" * (N + 2)
        ceros = list(ceros)
        boggle.append(ceros)
        for _ in range(N):
            linea = stdin.readline().strip()
            linea = "0" + linea + "0"
            linea = list(linea)
            boggle.append(linea)
        boggle.append(ceros)
        findWords(boggle, N)
        ignore = stdin.readline()
        cases -= 1
main()