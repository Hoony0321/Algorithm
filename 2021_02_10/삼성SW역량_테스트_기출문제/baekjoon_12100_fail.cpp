//baekjoon_12100 - 2048 (Easy)
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int map_size; // 1 <=  N <= 20
int max_result = 0;

void Setting_map(int map_size, vector<vector<int>>& map){
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

// 배열에서 최대 원소의 값을 반환
int getMaxVar(vector<vector<int> >& board){
    int maxNum=0;
    for(int i=0;i<map_size;++i)
        for(int j=0;j<map_size;++j)
            maxNum=max(maxNum,board[i][j]);
    return maxNum;
}


void SwappingBlock(int direction,int y, int x , 
vector<vector<int>>& map, vector<vector<bool>>& IsCalculate){
  switch(direction){
    //-----위-----//
    case 1:
      if(y-1 >= 0){ //맨 위에 있는 경우가 아닌 경우
        if(map[y-1][x] == 0){ // 빈 공간일 경우
          map[y-1][x] = map[y][x];
          map[y][x] = 0;
          SwappingBlock(1,y-1,x,map,IsCalculate); //위에 또 빈 공간일수도 있으므로 실행
        }
        else{ //빈 공간일 아닐 경우
          if(map[y-1][x] == map[y][x] && IsCalculate[y-1][x] == false){ //같을 경우
            IsCalculate[y-1][x] = true;
            map[y-1][x] *= 2;
            map[y][x] = 0;
          }
        }
      }
      break;
    //-----아래-----//
    case 2:
      if(y+1 < map_size){ //맨 아래에 있는 경우가 아닌 경우
        if(map[y+1][x] == 0){ // 빈 공간일 경우
          map[y+1][x] = map[y][x];
          map[y][x] = 0;
          SwappingBlock(2,y+1,x,map,IsCalculate); //아래에 또 빈 공간일수도 있으므로 실행
        }
        else{ //빈 공간일 아닐 경우
          if(map[y+1][x] == map[y][x] && IsCalculate[y+1][x] == false){ //같을 경우
            IsCalculate[y+1][x] = true;
            map[y+1][x] *= 2;
            map[y][x] = 0;
          }
        }
      }
      break;
    //-----왼쪽-----//
    case 3:
      if(x-1 >= 0){ //맨 왼쪽에 있는 경우가 아닌 경우
        if(map[y][x-1] == 0){ // 빈 공간일 경우
          map[y][x-1] = map[y][x];
          map[y][x] = 0;
          SwappingBlock(3,y,x-1,map,IsCalculate); //위에 또 빈 공간일수도 있으므로 실행
        }
        else{ //빈 공간일 아닐 경우
          if(map[y][x-1] == map[y][x] && IsCalculate[y][x-1] == false){ //같을 경우
            IsCalculate[y][x-1] = true;
            map[y][x-1] *= 2;
            map[y][x] = 0;
          }
        }
      }
      break;

    //-----오른쪽-----//
    case 4:
      if(x+1 < map_size){ //맨 오른쪽에 있는 경우가 아닌 경우
        if(map[y][x+1] == 0){ // 빈 공간일 경우
          map[y][x+1] = map[y][x];
          map[y][x] = 0;
          SwappingBlock(4,y,x+1,map,IsCalculate); //위에 또 빈 공간일수도 있으므로 실행
        }
        else{ //빈 공간일 아닐 경우
          if(map[y][x+1] == map[y][x] && IsCalculate[y][x+1] == false){ //같을 경우
            IsCalculate[y][x+1] = true;
            map[y][x+1] *= 2;
            map[y][x] = 0;
          }
        }
      }
      break;
  }
}

void SwappingMap(int direction, vector<vector<int>>& map){
  //맵 블럭 하나씩 스와이핑 - 이때 값이 있는 블럭들만 SwappingBlock
  vector<vector<bool>> IsCalculate(map_size,vector<bool>(map_size,false));
  switch(direction){
    //-----위-----//
    case 1:
      for(int i = 0; i < map_size; i++){
        for(int j = 0; j < map_size; j++){
          if(map[j][i] != 0){
            SwappingBlock(direction, j, i,map, IsCalculate);
          }
        }
      }
      break;
    //-----아래-----//
    case 2:
      for(int i = 0; i < map_size; i++){
        for(int j = map_size - 1; j >= 0; j--){
          if(map[j][i] != 0){
            SwappingBlock(direction, j, i,map, IsCalculate);
          }
        }
      }
      break;
    //-----왼쪽-----//
    case 3:
      for(int i = 0; i < map_size; i++){
        for(int j = 0; j < map_size; j++){
          if(map[i][j] != 0){
            SwappingBlock(direction, i, j,map, IsCalculate);
          }
        }
      }
      break;
    //-----오른쪽-----//
    case 4:
      for(int i = 0; i < map_size; i++){
        for(int j = map_size-1; j >= 0; j--){
          if(map[i][j] != 0){
            SwappingBlock(direction, i, j,map, IsCalculate);
          }
        }
      }
      break;
 
  }
}

void FindingMaxBlock(int index, vector<vector<int>> map){
  if(index == 6){
    int max_elem = getMaxVar(map);
    if(max_elem > max_result) max_result = max_elem;

    return;
  }

  
  for(int i = 1; i < 5; i++){
    vector<vector<int>> map_next(map);
    SwappingMap(i,map_next);
    FindingMaxBlock(index+1, map_next);
  }

  
}


int main(){
  //map size 입력
  cin >> map_size;

  vector<vector<int>> map;

  //map setting
  Setting_map(map_size, map);
  
  FindingMaxBlock(0,map);
  cout << max_result << endl;

  


}