//baekjoon_12100 - 2048 (Easy)
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int map_size; // 1 <=  N <= 20
int vector<vector<int>> map;
int max_result = 0;

void Setting_map(int map_size){
  //map 크기 초기화
  map.resize(map_size);
  for(auto& elem : map){
    elem.resize(map_size,0);
  }

  //map 입력
  for(auto& elem1 : map){
    for(auto& elem2 : elem1){
      cin >> elem2;
    }
  }
}

void SwappingValue(int& val1, int& val2){
  int temp = val1;
  val1 = val2;
  val2 = temp;
}



void SwappingBlock(int direction,int y, int x){
  switch(direction){
    //-----위-----//
    case 1:
      if(y-1 >= 0){ //맨 위에 있는 경우가 아닌 경우
        if(map[y-1][x] == 0){ // 빈 공간일 경우
          SwappingValue(map[y][x], map[y-1][x]);
          SwappingBlock(1,y-1,x); //위에 또 빈 공간일수도 있으므로 실행
        }
        else{ //빈 공간일 아닐 경우
          if(map[y-1][x] == map[y][x]){ //같을 경우
            SwappingValue(map[y-1][x], map[y-1][x] * 2);
            SwappingValue(map[y][x],0);
          }
        }
      }
      break;
    //-----아래-----//
    case 2:
      if(y+1 < map_size){ //맨 아래에 있는 경우가 아닌 경우
        if(map[y+1][x] == 0){ // 빈 공간일 경우
          SwappingValue(map[y][x], map[y+1][x]);
          SwappingBlock(2,y+1,x); //위에 또 빈 공간일수도 있으므로 실행
        }
        else{ //빈 공간일 아닐 경우
          if(map[y+1][x] == map[y][x]){ //같을 경우
            SwappingValue(map[y+1][x], map[y+1][x] * 2);
            SwappingValue(map[y][x],0);
          }
        }
      }
      break;
    //-----왼쪽-----//
    case 3:
      if(x-1 >= 0){ //맨 왼쪽에 있는 경우가 아닌 경우
        if(map[y][x-1] == 0){ // 빈 공간일 경우
          SwappingValue(map[y][x], map[y][x-1]);
          SwappingBlock(3,y,x-1); //위에 또 빈 공간일수도 있으므로 실행
        }
        else{ //빈 공간일 아닐 경우
          if(map[y][x-1] == map[y][x]){ //같을 경우
            SwappingValue(map[y][x-1], map[y][x-1] * 2);
            SwappingValue(map[y][x],0);
          }
        }
      }
      break;

    //-----오른쪽-----//
    case 4:
      if(x+1 < map_size){ //맨 오른쪽에 있는 경우가 아닌 경우
        if(map[y][x+1] == 0){ // 빈 공간일 경우
          SwappingValue(map[y][x], map[y][x+1]);
          SwappingBlock(4,y,x+1); //위에 또 빈 공간일수도 있으므로 실행
        }
        else{ //빈 공간일 아닐 경우
          if(map[y][x+1] == map[y][x]){ //같을 경우
            SwappingValue(map[y][x+1], map[y][x+1] * 2);
            SwappingValue(map[y][x],0);
          }
        }
      }
      break;
  }
}

void SwappingMap(int direction){
  //맵 블럭 하나씩 스와이핑 - 이때 값이 있는 블럭들만 SwappingBlock
}

void FindingMaxBlock(int index, int max_elem){

}


int main(){
  //map size 입력
  cin >> map_size;

  //map setting
  Setting_map(map_size);


  


}