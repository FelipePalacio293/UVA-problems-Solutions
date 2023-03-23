from sys import stdin 

def main():
    c = int(stdin.readline())
    while c != 0:
        n, t, m = map(int, stdin.readline().split())
        l = []
        r = []
        final = []
        for x in range(m):
            number, petition = map(str, stdin.readline().split())
            if(petition == "right"):
                r.append(x)
            elif(petition == "left"):
                l.append(x)
            final.append(int(number))
        side = 0 # 0: izquierda 1: derecha
        time = 0
        data = [0 for x in range(10050)]
        while len(r) != 0 or len(l) != 0:
            if len(r) == 0:
                nextTime = final[l[0]]
            elif len(l) == 0:
                nextTime = final[r[0]]
            else:
                nextTime = min(final[l[0]], final[r[0]])
            time = max(nextTime, time)
            cars = 0
            if(side == 0):

                while len(l) > 0 and cars < n and final[l[0]] <= time:
                    data[l[0]] = time + t
                    l.pop(0)
                    cars += 1
                side = 1
            else:
                while len(r) > 0 and cars < n and final[r[0]] <= time:
                    data[r[0]] = time + t
                    r.pop(0)
                    cars += 1
                side = 0

            time += t
        for x in range(m):
            print(data[x])
        c -= 1
        if(c != 0):
            print()

main()