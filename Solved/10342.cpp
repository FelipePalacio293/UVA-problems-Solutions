#include <climits>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int n; 
vector<int> p(500);
vector<vector<int>> d(500);
vector<vector<pair<int, int> > > adj(50000);

void inicializar(){
    for(int i = 0; i < n; ++i){
        d[i].push_back(INT_MAX);
        d[i].push_back(INT_MAX);
        p[i] = -1;
    }
}

void dijkstra(int x, int y){
    int i, j, k, u, v, peso, costo;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > cola;

    inicializar();

    cola.push(make_pair(0, x));
    while(!cola.empty() ){
        costo = cola.top().first;
        u = cola.top().second;
        cola.pop();
        if(costo != d[u][0]){
            if( costo < d[u][0]){
                d[u][0] = costo;
            }
            else if( costo < d[u][1]){
                d[u][1] = costo;
            }
            for(j = 0; j < adj[u].size(); ++j){
                v = adj[u][j].first;
                peso = adj[u][j].second;
                if( d[v][0] > costo + peso || d[v][1] > costo + peso){
                    cola.push(make_pair(costo + peso, v));
                }
            }
        }
    }
}

int main(){
    int r, u, v, w, index = 1, q, x, y, D;
    cin >> n >> r;
    while(n != EOF && r != EOF){
        for(int i = 0; i < n; i++){
            adj[i].clear();
            d[i].clear();
        }
        for(int i = 0; i < r; i++){
            cin >> u >> v >> w; 
            adj[u].push_back(make_pair(v, w));
            adj[v].push_back(make_pair(u, w));
        }
        cout << "Set #" << index++ << "\n";
        cin >> q;
        for(int i = 0; i < q; i++){
            cin >> x >> y;
            dijkstra( x, y );
            if( d[y][1] != INT_MAX){
                printf("%d\n", d[y][1]);
            }
            else{
                printf("?\n");
            }
        }
        cin >> n >> r; 
    }
}