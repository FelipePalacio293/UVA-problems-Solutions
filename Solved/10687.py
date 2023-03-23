import math
from sys import stdin

stations = list()
visited = list()
n = int()

def getDistance(u):
    global stations
    distanceList = [[None, None, None, None] for _ in range(n)]
    
    for x in range(n):
        distanceList[x][0] = math.sqrt(math.pow(stations[x][0] - stations[u][0], 2) + math.pow(stations[x][1] - stations[u][1], 2))
        distanceList[x][1] = stations[x][0]
        distanceList[x][2] = stations[x][1]
        distanceList[x][3] = x
    return distanceList

def getTwoClosest(u):
    distanceList = getDistance(u)
    distanceList.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
    return distanceList

def dfs(u):
    global visited
    visited[u] = 1
    distance = list(getTwoClosest(u))
    for x in range(2):
        if(visited[distance[1][3]] == 0):
            dfs(distance[1][3])
        if(visited[distance[2][3]] == 0):
            dfs(distance[2][3])

def main():
    global stations
    global visited
    global n
    n = int(stdin.readline())
    while(n):
        data = list(map(int, stdin.readline().split()))
        stations = []
        visited = [0 for _ in range(n)]
        for x in range(1, n * 2, 2):
            stations.append([data[x - 1], data[x]])
        if(n > 2):
            dfs(0)
        w = bool()
        w = True
        for x in range(n):
            if(visited[x] == 0):
                w = False
        if(w == False and n > 2):
            print("There are stations that are unreachable.")
        else:
            print("All stations are reachable.")

        n = int(stdin.readline())

main()