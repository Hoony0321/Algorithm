#include<iostream>

using namespace std;

char map[105][105];

int minCordinate[2] = {50,50};
int maxCordinate[2] = {50,50};
int direciontList[4][2] = {{+1,0},{0,-1},{-1,0},{0,+1}}; // 남 서 북 동

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int N;
  cin >> N;

  int direction = 0;
  int y = 50;
  int x = 50;
  map[y][x] = '.';
  
  
  for(int i = 0; i < N; i++){
    char move;
    cin >> move;
    
    switch(move){
      case 'R':
        direction = (direction+1)%4;
        break;
      case 'L':
        direction = (direction-1)%4;
        if(direction < 0) direction = 3;
        break;
      case 'F':
        y += direciontList[direction][0];
        x += direciontList[direction][1];
        if(y < minCordinate[0]) minCordinate[0] = y;
        else if(y > maxCordinate[0]) maxCordinate[0] = y;
        if(x < minCordinate[1]) minCordinate[1] = x;
        else if(x > maxCordinate[1]) maxCordinate[1] = x;
        map[y][x] = '.';
        break;
    }
  }


  for(int i = minCordinate[0]; i <= maxCordinate[0]; i++){
    for(int j = minCordinate[1]; j <= maxCordinate[1]; j++){
      if(!map[i][j]){map[i][j] = '#';} 
      cout << map[i][j];
    }
    cout << "\n";
  }
  
}