#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <iostream>
#include <string.h>
#include <queue>

using namespace std;

vector<vector<int> > adj(10001);
// vector<vector<int> > lines(10001);
int importantes[10001];

int n;
int freq[10001];
int dist[10001];
bool visitados[10001];

int bfsAux(int u){
    int v, i, w, c, x, distances = 0;
    pair<int, int> parents;
    queue< pair<int, int> > cola;
    for(x = 0; x < n + 1; x++){
        dist[x] = -99999;
        visitados[x] = false;
    }

    visitados[u] = true;
    cola.push(make_pair(u, 0));
    dist[u] = 0;

    while(!cola.empty()){
        parents = cola.front();
        w = parents.first;
        c = parents.second;
        cola.pop();
        // cout << w << endl;
        for(i = 0; i < adj[w].size(); ++i){
            v = adj[w][i];
            if(!visitados[v]){
                cola.push(make_pair(v, c + 1));
                dist[v] = c + 1;
                visitados[v] = true;
            }
        }    
    }

    for(x = 1; x < n + 1; x++){
        if(freq[x] > 1){
            distances += dist[x];
        }
    }

    return distances;
}

int main(){
    int c, s, x, y, w, stationTwo, stationOne, size, alreadyOnList[10000], bestDistance = 9999999, totalDistance, tempDistance, bestNode;
    bool hit;
    cin >> c;
    while(c--){
        cin >> n >> s;
        for(x = 0; x < s; x++){
            cin >> stationOne;
            freq[stationOne]++;
            while(scanf("%d", &stationTwo) != 0){
                if(stationTwo == 0){
                    break;
                }
                
                adj[stationOne].push_back(stationTwo);
                adj[stationTwo].push_back(stationOne);
                
                stationOne = stationTwo;
                freq[stationOne]++;
            }
        }

        for(x = 0; x < n + 1; x++){
            if(freq[x] > 1){
                tempDistance = bfsAux(x);
                if(tempDistance < bestDistance){
                    bestDistance = tempDistance;
                    bestNode = x;
                }
            }    
        }

        cout << "Krochanska is in: " << bestNode << endl;

        for(x = 0; x < n + 1; x++){
            freq[x] = 0;
            adj[x].clear();
        }    
        bestDistance = 9999999;
    }
    return 0;
}