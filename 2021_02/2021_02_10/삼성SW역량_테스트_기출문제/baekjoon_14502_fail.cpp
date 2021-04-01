//baekjoon_14502 - 연구소 
#include<iostream>
#include<vector>

using namespace std;

vector<vector<int>> map
int map_row;
int map_column;

void SettingMap(){
  cin >> map_row >> map_column;
  map.resize(map_row);
  for(auto& elem1 : map){
    for(auto& elem2 : elem1){
      elem2.resize(map_column,0);
    }
  }

  for(auto& elem1 : map){
    for(auto& elem2 : elem1){
      cin >> elem2;
    }
  }
}

void PuttingWall(vector<vector<int>>& map, int count){
  if(count == 3) return;

  for(int i = 0; i < map_row; i++){
    for(int j = 0; j <map_column; j++){
      if(map[i][j] == 0){map[i][j]}
    }
  }
}

void SpreadingVirous()

void SolveProblem(){

}

int main(){
  SettingMap();

  for(int i = 0; i < 3; i++){
    for(int j = 0; j < row; j++){

    }
  }

}