#include <vector>
#include <map>
#include <string>
#include <cstdio>
#include <iostream>

using namespace std;

int MAX = 10000;
int n, t = 0, ti;
vector<vector<int> > adj(MAX);
vector<int> visitado(MAX), pred(MAX), f(MAX), d(MAX);
vector<int> topo(10000);

// 0 = no visitado, 1 = visitado pero no completado, 2 = completado
void topoSort(int u){
    int v, i;
    visitado[u] = 1;
    //printf("%d\n", v);
    for(i = 0; i < adj[u].size(); ++i){
        v = adj[u][i];
        if(!visitado[v]){
            topoSort(v);
        }
    }
    topo[ti++] = u;
}

void dfs(int u){
    int v, i;
    //d[v] = ++t;
    visitado[u] = 1;
    // printf("%d\n", u);

    for(i = 0; i < adj[u].size(); ++i){
        v = adj[u][i];
        if(!visitado[v]){
            dfs(v);
        }
    }

    //visitado[v] = 2;
    //f[v] = ++t;
}

int main(){
    int i, n, m, x, a, b, u;
    while(scanf("%d %d", &n, &m)){
        for(x = 0; x < m; x++){
            scanf("%d %d", &a, &b);
            adj[a].push_back(b);
        }
        for(i = 0; i <= n; ++i){
            visitado[i] = 0;
            topo[i] = 0;
        }
        ti = 0;
        for (i = 0 ; i <= n; i++) {
            if (!visitado[i]) topoSort(i);
        }
        for(i = 0; i <= n; ++i){
            visitado[i] = 0;
        }
        int ans = 0;

        for (i = ti - 1; i >= 0; i--) {
            u = topo[i];
            if (visitado[u]) {
                continue;
            }
            if (u != 0) 
                ans++;
            dfs(u);
        }

        for(i = 0; i <= n; ++i){
            adj[i].clear();
        }
        cout << ans << endl;
    }
    
    return 0;
}