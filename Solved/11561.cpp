#include <vector>
#include <map>
#include <cstdio>
#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int deltaX[] = {-1, 0, 1, 0};
int deltaY[] = {0, -1, 0, 1};
char table[55][55] = {};
int visited[55][55] = {};
int w, h;
int suma;

int isValid(int i, int j){
    if(table[i][j] != '#'){
        return 1;
    }
    
    return 0;
}

int isSecure(int i, int j){
    if(table[i][j] == 'T'){
        return 1;
    }
    return 0;
}

void dfs(int i, int j){
    int newX, newY, x;
    visited[i][j] = 1;

    if(table[i][j] == 'G')
        suma += 1;
    
    for(x = 0; x < 4; x++){
        newX = i + deltaX[x];
        newY = j + deltaY[x];
        if(isValid(newX, newY) == 1 && visited[newX][newY] == 0){
            if(isSecure(newX, newY) == 1){
                return;             
            }
        }
    }
    for(x = 0; x < 4; x++){
        newX = i + deltaX[x];
        newY = j + deltaY[x];
        if(isValid(newX, newY) == 1 && visited[newX][newY] == 0){
            dfs(newX, newY);
        }
    }
}

int main(){
    char val;
    int x, y;
    while(scanf("%d %d", &w, &h) == 2){
        for(x = 0; x < h; x++)
            scanf("%s", table[x]);
        
        memset(visited, 0, sizeof(visited));

        for(x = 0; x < h; x++){
            for(y = 0; y < w; y++){
                if(table[x][y] == 'P'){
                    dfs(x, y);
                    break;
                }
            }
        }
        cout << suma << endl;
        suma = 0;
    }   
}