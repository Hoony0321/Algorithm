#include<iostream>

using namespace std;

int N,M,number_of_cleaningRoom;

void CleaningRoom(int** map, int* condition){
  //현재 자리 청소
  number_of_cleaningRoom += 1;
  map[condition[0]][condition[1]] = 2;

  //탐색
  if(condition[1] - 1 >= 0 ** condition[1] - 1 == 0){ //왼쪽 빈 방

  }
  else if(condition[1] - 1 < 0){ //왼쪽 벽

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