#include<iostream>

using namespace std;

int** room_ptr;
int N,M;
int number_of_cleanRoom = 0;
int left_direction[4][2] = {{0,-1},{-1,0},{0,+1},{+1,0}};
int behind_direction[4][2] = {{+1,0},{0,-1},{-1,0},{0,+1}};

void CleaningRoom(int index, int* coordinate,int direction){
  if(index == 4){
    int behind_y = coordinate[0] + behind_direction[direction][0];
    int behind_x = coordinate[1] + behind_direction[direction][1];
    if(room_ptr[behind_y][behind_x] == 1){ return; }
    else{
      coordinate[0] = behind_y;
      coordinate[1] = behind_x;
      CleaningRoom(0,coordinate,direction);
      return;
    }
  }

  if(room_ptr[coordinate[0]][coordinate[1]] == 0){ //현재 자리 청소
    room_ptr[coordinate[0]][coordinate[1]] = 2;
    number_of_cleanRoom += 1;
  }
  int left_y = coordinate[0] + left_direction[direction][0];
  int left_x = coordinate[1] + left_direction[direction][1];
  
  //STEP 2
  if(room_ptr[left_y][left_x] == 0){ //왼쪽에 공간할 장소가 있을 경우
    coordinate[0] = left_y;
    coordinate[1] = left_x;
    direction = (direction + 3) % 4;
    CleaningRoom(0,coordinate,direction);
  }
  else{ // 없을 경우
    direction = (direction + 3) % 4;
    CleaningRoom(index+1, coordinate, direction);
  }

}

int main(void){
  //생성자
  cin >> N >> M;
  int** room = new int*[N];
  for(int i = 0; i < N; i ++){
    room[i] = new int[M];
  }

  //map ptr 할당
  room_ptr = room;

  //입력
  int coordinate[2];
  int direction;
  cin >> coordinate[0] >> coordinate[1] >> direction;
  for(int i = 0; i<N; i++ ){
    for(int j = 0; j<M; j++){
      cin >> room[i][j];
    }
  }

  CleaningRoom(0, coordinate, direction);


  cout << number_of_cleanRoom << "\n";



  /*
  //소멸자
  for(int i = 0; i < M; i ++){
    delete[] room[i];
  }
  delete[] room;
  room_ptr = nullptr;
  */
}