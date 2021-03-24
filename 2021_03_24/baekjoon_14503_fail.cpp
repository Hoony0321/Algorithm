#include<iostream>

using namespace std;

int N,M,number_of_cleaningRoom;
//북 0, 동 1, 남 2, 서 3
void TurnLeft(int* condition){
  switch(condition[2]){
    case 0: //북쪽
      condition[2] = 3;
      break;
    case 1: //동쪽
      condition[2] = 0;
      break;
    case 2: //남쪽
      condition[2] = 1;
      break;
    case 3: //서쪽
      condition[2] = 2;
      break;
  }
}

bool SeeLeft(int** map, int* condition){
    switch(condition[2]){
    case 0: //북쪽
      if(map[condition[0]][condition[1]-1] == 0) return true;
      else return false;
      break;
    case 1: //동쪽
      if(map[condition[0]-1][condition[1]] == 0) return true;
      else return false;
      break;
    case 2: //남쪽
      if(map[condition[0]][condition[1]+1] == 0) return true;
      else return false;
      break;
    case 3: //서쪽
      if(map[condition[0]+1][condition[1]] == 0) return true;
      else return false;
      break;
  }
}

bool SeeBack(int** map, int* condition){
    switch(condition[2]){
    case 0: //북쪽
      if(map[condition[0]+1][condition[1]] != 1) return true;
      else return false;
      break;
    case 1: //동쪽
      if(map[condition[0]][condition[1]-1] != 1) return true;
      else return false;
      break;
    case 2: //남쪽
      if(map[condition[0]-1][condition[1]] != 1) return true;
      else return false;
      break;
    case 3: //서쪽
      if(map[condition[0]][condition[1]+1] != 1) return true;
      else return false;
      break;
  }
}

void Move_front(int* condition){
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

void Move_back(int* condition){
  switch(condition[2]){
    case 0: //북쪽
      condition[0] += 1;
      break;
    case 1: //동쪽
      condition[1] -= 1;
      break;
    case 2: //남쪽
      condition[0] -= 1;
      break;
    case 3: //서쪽
      condition[1] += 1;
      break;
  }
}

void CleaningRoom(int** map, int* condition){
  
  cout << "y : " << condition[0] << " x : " << condition[1] << " direction : " << condition[2] << "\n";
  //현재 자리 청소
  if(map[condition[0]][condition[1]] == 0){
    number_of_cleaningRoom += 1;
    map[condition[0]][condition[1]] = 2;
  }


  //탐색
  int count = 0;
  while(count < 4){
    if(SeeLeft(map, condition)){
      TurnLeft(condition);
      Move_front(condition);
      count = 0;
    }
    else{
      TurnLeft(condition);
      count += 1;
    }
  }
  
  if(SeeBack(map,condition)){
    Move_back(condition);
    CleaningRoom(map,condition);
  }
  else{
    //종료
  }

}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  cin >> N >> M;
  int condition[3];
  cin >> condition[0] >> condition[1] >> condition[2];
  
  
  int** map = new int*[N];
  for(int i = 0; i < N; i++){
    map[i] = new int[M];
    for(int j= 0; j < M; j++){
      cin >> map[i][j];
    }
  }

  
  CleaningRoom(map,condition);

  cout << number_of_cleaningRoom << "\n";


  


  for(int i = 0; i < N; i++){
    delete[] map[i];
  }
  delete[] map;

}