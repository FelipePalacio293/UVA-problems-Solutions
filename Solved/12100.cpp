#include <iostream>
#include <list>

using namespace std;

int verificarSiPuedeImprimir(list<int> colaDePrioridades){
    int elementoMayor = colaDePrioridades.front();
    for(list<int>::iterator it = colaDePrioridades.begin(); it !=  colaDePrioridades.end(); it++){
        if(elementoMayor < *it){ // Si hay algun elemento mayor al que esta en la primera posicion retorna 0, de lo contrario retorna 1
            return 0;
        }
    }
    return 1; 
}

void calcularMinutos(int cantidadDeColas){
    list<int> colaDePrioridades;
    int x, y, z, w, trabajosEnCola, trabajoRequerido, prioridadTrabajo, tiempo = 0, primerElemento, trabajoImpreso = 0;
    list<int>::iterator itPrimerIterador;
    for(x = 0; x < cantidadDeColas; x++){
        cin >> trabajosEnCola >> trabajoRequerido;
        for(y = 0; y < trabajosEnCola; y++){
            cin >> prioridadTrabajo;
            colaDePrioridades.push_back(prioridadTrabajo);
        }
        list<int>::iterator itTrabajoRequerido; 

        itTrabajoRequerido = colaDePrioridades.begin(); // Se guarda un iterador que siempre apunta al elemento deseado.
        for(z = 0; z < trabajoRequerido; z++){
        	itTrabajoRequerido++;
		}
        tiempo = 0;
        trabajoImpreso = 0;
        while(!colaDePrioridades.empty() && !trabajoImpreso){
            if(verificarSiPuedeImprimir(colaDePrioridades)){
                if(itTrabajoRequerido == colaDePrioridades.begin()){
                    trabajoImpreso = 1;
                }
                colaDePrioridades.pop_front();
                tiempo++;
            }
            else if(itTrabajoRequerido == colaDePrioridades.begin()){
                primerElemento = colaDePrioridades.front();
                colaDePrioridades.push_back(primerElemento);
                colaDePrioridades.pop_front();
                itTrabajoRequerido = colaDePrioridades.begin();
                for(w = 0; w < colaDePrioridades.size() - 1; w++){
        			itTrabajoRequerido++;
				}
            }
            else{
            	primerElemento = colaDePrioridades.front();
                colaDePrioridades.push_back(primerElemento);
                colaDePrioridades.pop_front();
			}
        }
        cout << tiempo << endl;
        colaDePrioridades.clear();
    }
}

int main(){
    int cantidadDeColas;
    cin >> cantidadDeColas;
    calcularMinutos(cantidadDeColas);
    return 0;
}