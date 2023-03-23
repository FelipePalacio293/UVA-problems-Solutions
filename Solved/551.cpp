/* Carlos Felipe Palacio 11/08/2021   */

#include <iostream>
#include <stack>
#include <string>

using namespace std;

const int CHAR_TO_STRING = 1;

void encontrarErrores(){
    string expresion;
    int x, error = 0, huboError = 0;
    string specialChar = "$";
    while( getline( cin, expresion ) ){
        stack< string > pila;
        huboError = 0;
        error = 0;
        for(x = 0; x < expresion.length() && !huboError; x++){
            error++;
            if(expresion[x] == '(' || expresion[x] == '[' || expresion[x] == '{' || expresion[x] == '<'){
                if(expresion[x + 1] == '*'  && expresion[x] == '('){
                    pila.push("$");
                    x++;
                }
                else{
                    string caracter(CHAR_TO_STRING, expresion[x]);
                    pila.push(caracter);
                }
            }
            else if(expresion[x] == ')' || expresion[x] == ']' || expresion[x] == '}' || expresion[x] == '>' || (expresion[x] == '*' && expresion[x + 1] == ')' )){
                if(pila.empty()){
                    huboError = 1;
                }
                else if(expresion[x] == ')'){
                    if(pila.top() != "("){

                        huboError = 1;
                    }
                    else{
                        pila.pop();
                    }
                }
                else if(expresion[x] == ']'){
                    if(pila.top() != "["){

                        huboError = 1;
                    }
                    else{
                        pila.pop();
                    }
                }
                else if(expresion[x] == '}'){
                    if(pila.top() != "{"){

                        huboError = 1;
                    }
                    else{
                        pila.pop();
                    }
                }
                else if(expresion[x] == '>'){
                    if(pila.top() != "<"){

                        huboError = 1;
                    }
                    else{
                        pila.pop();
                    }
                }
                else if(expresion[x] == '*' && expresion[x + 1] == ')'){
                    x++;
                    if(pila.top() != "$"){
                        huboError = 1;
                    }
                    else{

                        pila.pop();
                    }
                }
            }
        }
        if(!pila.empty() && !huboError){
            huboError = 1;
            error++;
        }
        if(huboError){
            cout << "NO " << error << endl;
        }
        else{
            cout << "YES" << endl;
        }
    }
}

int main(){
    encontrarErrores();
    return 0;
}