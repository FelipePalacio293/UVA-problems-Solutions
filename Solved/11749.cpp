#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <iostream>
#include <string.h>
#include <queue>

using namespace std;

int visited[1000], n, cont;
long long int maxN;
vector<vector<pair<int, long long int> > > adj(10001);
vector<vector<int> > comps;
bool visitado[50000];

void ccDFSAux(int v){
    int w, peso;
    visitado[v] = true;
    // comps[comps.size() - 1].push_back(v);
    
    for(int i = 0; i < adj[v].size(); i++){
        w = adj[v][i].first;
        peso = adj[v][i].second;
        if(!visitado[w] && peso == maxN){
            cont++;
            ccDFSAux(w);
        }
    }
}

void ccDFS(){
    int i, ans = -1;
    
    for(i = 1; i < n; i++)
        visitado[i] = false;

    for(i = 1; i < n; i++){
        if(!visitado[i]){
            cont = 0;
            // comps.push_back(vector<int>());
            ccDFSAux(i);
            ans = max(cont, ans);
        }
    }
    cout << ans + 1 << endl;
}

int main(){
    int m, x, c, d, j ;
    long long int w;
    int i;
    while(scanf("%d %d", &n, &m)){
        if(n == 0 && m == 0){
            break;
        }
        maxN = -99999999999999999;
        for(x = 0; x < m; x++){
            scanf("%d %d %lld", &c, &d, &w);
            adj[c].push_back(make_pair(d, w));
            adj[d].push_back(make_pair(c, w));
            maxN = max(maxN, w);
        }
        n++;
        ccDFS();
        for(i = 1; i < n; i++)
            adj[i].clear();
    }

    /*
    ccDFS();
    
    cout << "Total Componentes: " << comps.size() << endl;
    for(i = 0; i < comps.size(); i++){
        cout << "Componente " << i << ":";
        for(j = 0; j < comps[i].size(); j++)
            cout << " " << comps[i][j];
        cout << endl;
    }
    */
    return 0;
}