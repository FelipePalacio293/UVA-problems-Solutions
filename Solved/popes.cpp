/* Carlos Felipe Palacio 31/08/2021 */
#include <iostream>

using namespace std;

int busquedaBinaria(int a[100000], int x, int tam){
    int resp = 0;
    int N = tam;
    int mid = 0;
    int low = 0;
    if(N != 0){
        int hi = tam;
        while(low + 1 != hi){
            mid = low + ((hi - low) / 2);
            if(a[mid] <= x){
                low = mid;
            }
            else{
                hi = mid;
            }
        }
    }
    return low;   
}

int main(){
    int periodo, numPapas, x, aniosPapas[100000];
    int inicio = 0, final = 0, respuesta = 0;
    while(cin >> periodo){
        cin >> numPapas;
        x = 0;
        while(x != numPapas){
            cin >> aniosPapas[x];
            x++;
        }
        inicio = 0; 
        final = 0; 
        respuesta = 0;
        for(x = 0; x < numPapas; x++){
            int posicion = busquedaBinaria(aniosPapas, aniosPapas[x] + periodo - 1, numPapas);
            if(posicion - x > respuesta){
                respuesta = posicion - x;
                inicio = aniosPapas[x];
                final = aniosPapas[posicion];
            }
        }
        cout << respuesta + 1 << " " << inicio << " " << final << endl; 
    }
}