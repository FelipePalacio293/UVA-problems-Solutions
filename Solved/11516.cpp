/* Carlos Felipe Palacio 31/08/2021 */
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

int buscarCobertura(int casas[100000], int mid, int m){
    int cont = 1, x;
    float cobertura = casas[0] + mid;
    for(x = 0; x < m; x++){
        if(casas[x] > cobertura){
            cobertura = casas[x] + mid;
            cont++;
        }
    }
    return cont;
}

int main(){
    int casos, n, m, x;
    cin >> casos;
    while(casos){
        int casas[100000];
        cin >> n;
        cin >> m;
        if(n >= m){
            cout << "0.0" << endl;
            for(x = 0; x < m; x++){
                cin >> casas[x];
            }
        }
        else{
            for(x = 0; x < m; x++){
                cin >> casas[x];
            }
            sort(casas, casas + m);
            int low = 0;
            int hi = casas[m - 1];
            int mid;
            while(abs(low - hi) > 1){
                mid = (low + hi) / 2;
                if(buscarCobertura(casas, mid, m) > n){
                    low = mid;
                }
                else{
                    hi = mid;
                }
            }
            float resultado = (float)hi / 2;
            printf("%.1f\n", resultado);
        }
        casos--;
    }
    return 0;
}