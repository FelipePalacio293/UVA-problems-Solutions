#include<bits/stdc++.h>
#define go(i,a,b) for(int i=a;i<=b;i++)
#define inf 1000000000
using namespace std;
string a, b;
map<string, int> S;
int _, T, n, m, q, u[1002], v[1002], p[1002], d[102][102];

void bellmanFord(){
    for(int x = 1; x <= n; x++){
        for(int y = 1; y <= n; y++){
            d[y][x] = d[y][x - 1];
            
        }
        for(int y = 1; y <= m; y++){
            d[v[y]][x] = min(d[v[y]][x], d[u[y]][x - 1] + p[y]);
        }

    } 
    scanf("%d", &q);
    if(_ - T - 1) puts("");
    printf("Scenario #%d\n", _ - T);
    while(q--){
        int t;
        scanf("%d", &t);
        d[n][t = min(++t, n)] == inf ? puts("No satisfactory flights"):
        printf("Total cost of flight(s) is $%d\n",d[n][t]);
    }
}


int main(){
    scanf("%d", &T);
    _ = T;
    while(scanf("%d", &n), T--){
        go(i,1,n)
        cin >> a, S[a] = i, d[i][0] = inf;
        scanf("%d", &m);
        d[1][0] = 0;
        go(i,1,m) cin >> a >> b >> p[i], u[i] = S[a], v[i] = S[b];

        bellmanFord();
    }
    return 0;
}
//Paul_Guderian