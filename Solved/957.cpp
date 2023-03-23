#include <iostream>

using namespace std;

int main(){
    int periodo, numPapas, x, aniosPapas[100000];
    while(cin >> periodo){
        cin >> numPapas;
        while(x != numPapas){
            cin >> aniosPapas[x];
            x++;
        }
        int inicio = 0, final = 0, contadorPapas = 0, mejorNum = 0;
        int j;
        for(x = 0; x < numPapas; x++){
            j = x;
            contadorPapas = 0;
            while(j < numPapas && aniosPapas[j] < aniosPapas[x] + periodo){
                j++;
                contadorPapas++;
            }
            if(contadorPapas > mejorNum){
                mejorNum = contadorPapas;
                inicio = aniosPapas[x];
                final = aniosPapas[j - 1];
            }
        }
        cout << mejorNum << ' ' << inicio << ' ' << final << endl;
    }
    return 0;
}