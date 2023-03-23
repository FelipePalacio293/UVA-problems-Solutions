from sys import stdin

def main():
    line = stdin.readline().split()
    while(line != []):
        m, n, t = int(line[0]), int(line[1]), int(line[2])
        tmp = [0 for _ in range(t + 1)]
        if(n > t and m > t):
            print("0", t)
        else:
            if(m == t and n == t):
                print("1")
            elif(m == 1):
                print(t)
            elif(n == 1):
                print(t)
            elif(n == t and t % m != 0):
                print(1)
            elif(m == t and t % n != 0):
                print(1)
            else:
                if(m < t):
                    tmp[m] = 1
                if(n < t):
                    tmp[n] = 1
                for x in range(min(m, n), t + 1):
                    if(tmp[x - n] != 0 and tmp[x - m] != 0 and x >= m and x >= n):
                        tmp[x] = max(tmp[x - m] + 1, tmp[x - n] + 1)
                    elif(tmp[x - m] != 0 and x >= m):
                        tmp[x] = tmp[x - m] + 1
                    elif(tmp[x - n] != 0 and x >= n):
                        tmp[x] = tmp[x - n] + 1
                if(tmp[t] != 0):
                    print(tmp[t])
                else:
                    x = t
                    cont = 0
                    while(tmp[x] == 0 and x > 0):
                        cont += 1
                        x -= 1
                    print(tmp[x], cont)
        line = stdin.readline().split()

main()