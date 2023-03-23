/* Carlos Felipe Palacio 31/08/2021 */
#include <iostream>

using namespace std;

int binarySearchMayor(int A[], int x, int tam){
    int ans = -1, N = tam - 1;
    if(N != 0){
        int low = 0, hi = tam;
        while(low <= hi){
            int mid = (hi + low) / 2;
            if(A[mid] <= x){
                low = mid + 1;
            }
            else if(A[mid] > x){
                hi = mid - 1;
            }
        }
        if(low >= tam) return -1;
        return low;
    }
}

int binarySearchMenor(int A[], int x, int tam){
    int ans = -1, N = tam - 1;
    if(N != 0){
        int low = 0, hi = tam;
        while(low <= hi){
            int mid = (hi + low) / 2;
            if(A[mid] < x){
                low = mid + 1;
            }
            else if(A[mid] >= x){
                hi = mid - 1;
            }
        }
        if(hi < 0) return -1;
        return hi;
    }
}

int main(){
    int cantidadChimpancesHembras, arreglosHembras[50000], edadesBuscadas, arregloEdades[25000], x;
    cin >> cantidadChimpancesHembras;
    for(x = 0; x < cantidadChimpancesHembras; x++){
        cin >> arreglosHembras[x];
    }
    cin >> edadesBuscadas;
    for(x = 0; x < edadesBuscadas; x++){
        cin >> arregloEdades[x];
    }
    for(x = 0; x < edadesBuscadas; x++){
        int edadArriba = binarySearchMayor(arreglosHembras, arregloEdades[x], cantidadChimpancesHembras);
        int edadAbajo = binarySearchMenor(arreglosHembras, arregloEdades[x], cantidadChimpancesHembras);
        if(edadAbajo != -1 && edadArriba != -1){
            cout << arreglosHembras[edadAbajo] << " " << arreglosHembras[edadArriba] << endl;
        }
        else if(edadAbajo == -1){
            cout << "X " << arreglosHembras[edadArriba] << endl;
        }
        else if(edadArriba == -1){
            cout << arreglosHembras[edadAbajo] << " X" << endl;
        }
        else{
            cout << "X X" << endl;
        }
    }
    return 0;
}