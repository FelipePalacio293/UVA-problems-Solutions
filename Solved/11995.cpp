/* Carlos Felipe Palacio 31/08/2021 */

#include <iostream>
#include <cstdio>
#include <stack>
#include <queue>
using namespace std;

int main(){
    int cases, x, operacion, dato;
    while(cin >> cases){
        queue<int> cola; // Se declaran una pila, una cola y una cola de prioridad
        stack<int> pila;
        priority_queue<int> pCola;
        int esCola = 1, esPila = 1, esColaP = 1; // Se declaran banderas para cada una de las estructuras de datos declaradas
        for(x = 0; x < cases; x++){
            cin >> operacion;
            cin >> dato;
            if(operacion == 1){
                if(esCola) cola.push(dato); // Si ninguna operacion ha fallado, se pushea el dato dentro de la estructura
                if(esPila) pila.push(dato);
                if(esColaP) pCola.push(dato);
            }
            else{
                if(esCola){ // En caso de que alguna operacion haya fallado, ya no se debe comprobar mas
                    if(cola.empty() || cola.front() != dato){ // Si la estructura esta vacia, o su ultimo elemento guardado es diferente al que se quiere eliminar, podemos confirmar que no es ese tipo de estructura. 
                        esCola = 0;
                    } 
                    else{
                        cola.pop(); // En caso de que lo anterior no se cumpla, si puede borrar
                    }
                }
                if(esPila){ // La explicacion anterior es igual con las demas estructuras.
                    if(pila.empty() || pila.top() != dato){ 
                        esPila = 0;
                    } 
                    else{
                        pila.pop();
                    } 
                }
                if(esColaP){
                    if(pCola.empty() || pCola.top() != dato){
                        esColaP = 0; 
                    } 
                    else{
                        pCola.pop();
                    } 
                }
            }
        }
        if(esPila && !esColaP && !esCola){ // Se decide que tipo de estructura es la que se analizo
            cout << "stack" << endl;
        }
        else if(!esPila && esColaP && !esCola){
            cout << "priority queue" << endl;
        }
        else if(!esPila && !esColaP && esCola){
            cout << "queue" << endl;
        }
        else if(!esPila && !esCola && !esColaP){
            cout << "impossible" << endl;
        }
        else{
            cout << "not sure" << endl;
        }
    }
    return 0;
}