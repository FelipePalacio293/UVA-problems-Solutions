#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <stdio.h>
#include <string.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <iterator>

using namespace std;

int stations[1000][2];
int visited[1000];
int n;

struct VectorComparator {
    bool operator()(const std::vector<double>& a, const std::vector<double>& b) const {
        if (a[0] == b[0]) {
            if (a[1] == b[1]) {
                return a[2] < b[2];
            }
            return a[1] < b[1];
        }
        return a[0] < b[0];
    }
};

void getTwoClosest(int u){
    vector < vector < double > > dis(1000);
    static double distanceList[1000][4];
    int x;
    for(x = 0; x < n; x++){
        distanceList[x][0] = (double) sqrt(pow(stations[x][0] - stations[u][0], 2) + pow(stations[x][1] - stations[u][1], 2));
        distanceList[x][1] = stations[x][0];
        distanceList[x][2] = stations[x][1];
        distanceList[x][3] = x;
        dis[x].push_back(distanceList[x][0]);
        dis[x].push_back(distanceList[x][1]);
        dis[x].push_back(distanceList[x][2]);
        dis[x].push_back(distanceList[x][3]);
    }
    
    sort(dis.begin(), dis.end(),  [](const auto& a, const auto& b) {
        if (a[0] == b[0]) {
        if (a[1] == b[1]) {
            return a[2] < b[2];
        }
        return a[1] < b[1];
        }
        return a[0] < b[0];
    });
}

void dfs(int u){
    int x, y, pos, beforePost = -55555, tempPos;
    visited[u] = 1;
    getTwoClosest(u);
    
    for(x = 0; x < 2; ++x){
        
        if(visited[pos] == 0)
            dfs(pos);
        
    }
}

int main(){
    int x;
    bool w;
    while(scanf("%d", &n) != 0){
        if(n == 0){
            break;
        }
        memset(stations, 0, sizeof(stations));
        memset(visited, 0, sizeof(visited));
        for(x = 0; x < n; x++)
            scanf("%d %d", &stations[x][0], &stations[x][1]);
        dfs(0);
        w = true;
        for(x = 0; x < n; x++){
            if(visited[x] == 0){
                w = false;
                cout << x << endl;
            }
        }
        if(w){
            cout << "All stations are reachable." << endl;
        }
        else{
            cout << "There are stations that are unreachable." << endl;
        }
        // cout << "Ya" << endl;
    }
    return 0;
}