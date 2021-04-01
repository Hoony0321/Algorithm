#include<iostream>

using namespace std;

int N,M,number_of_cleaningRoom;

void TurnLeft(int* condition){
  switch(condition[2]){
    case 0: //북쪽
      condition[2] += 3;
      break;
    case 1: //동쪽
      condition[2] += 0;
      break;
    case 2: //남쪽
      condition[2] -= 1;
      break;
    case 3: //서쪽
      condition[2] -= 2;
      break;
  }
}

void Move(int* condition){
  switch(condition[2]){
    case 0: //북쪽
      condition[0] -= 1;
      break;
    case 1: //동쪽
      condition[1] += 1;
      break;
    case 2: //남쪽
      condition[0] += 1;
      break;
    case 3: //서쪽
      condition[1] -= 1;
      break;
  }
}

void CleaningRoom(int** map, int* condition){
  //현재 자리 청소
  number_of_cleaningRoom += 1;
  map[condition[0]][condition[1]] = 2;

  //탐색
  if(condition[1] != 0 && map[condition[1] - 1] == 0){ //왼쪽 청소 안 한 빈방 존재
    TurnLeft(condition);
    Move(condition);
  }
  else if(condition[1] == 0 || map[condition[1] - 1] == 1){ //왼쪽 청소할 공간 존재 X
    TurnLeft(condition);
  }
  else if((map[condition[1] + 1] == 1 || map[condition[1] + 1] == 2) &&
   (map[condition[0] + 1] == 1 || map[condition[0] + 1] == 2) &&
   (map[condition[0] - 1] == 1 || map[condition[0] - 1] == 2) 

  ){

  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;

  int** map = new int*[N];
  for(int i = 0; i < N; i++){
    map[i] = new int[M];
    for(int j= 0; j < M; j++){
      cin >> map[j];
    }
  }

  int condition[3];
  cin >> condition[0] >> condition[1] >> condition[2];
  CleaningRoom(map,condition);

  cout << number_of_cleaningRoom;


  


  for(int i = 0; i < N; i++){
    delete[] map[i];
  }
  delete[] map;

}