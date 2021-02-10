//baekjoon_14890 - 경사로
#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;

#define Matrix vector<vector<int>>

int map_size;
int slope;
Matrix map;

int result = 0;

void SettingMap(int map_size){
  map.resize(map_size);
  for(auto& elem : map){
    elem.resize(map_size);
  }


  for(auto& elem1 : map)
    for(auto& elem2 : elem1) cin >> elem2;
}

void FindingPath(vector<int>& map_row){
  int step = 0;
  vector<bool> IsSlope(map_size, false);



  while(step < map_size - 1){
    int diff = abs(map_row[step] - map_row[step+1]);
    if(diff == 0){ //경사로가 같을 경우
      step += 1;
    }

    else if(diff == 1){ //경사로 차이가 1인 경우
      if(map_row[step] < map_row[step+1]){ // 앞 칸이 높을 경우
        if(step - slope + 1 < 0){ return; } // 길이 부족
        if(IsSlope[step] == true) return;
        IsSlope[step] = true;
        for(int i = 1; i < slope; i++){
          if(map_row[step - i] == map_row[step] && IsSlope[step - i] == false){
            IsSlope[step - i] = true;
          }
          else{ return; }
        }
        step += 1;
      }
      else{ // 뒷 칸이 높을 경우
        if(step + slope > map_size - 1){ return; } // 길이 부족
          for(int i = 1; i <= slope; i++){
            if(map_row[step + i] == map_row[step] - 1 && IsSlope[step + i] == false){
              IsSlope[step + i] = true;
            }
            else{ return; }
          }
        step += slope;
      }
    }


    else{ // 경사로 차이가 2 이상인 경우
      return;
    }
  }



  result += 1;
}

int main(){
  cin >> map_size >> slope;
  SettingMap(map_size);

  for(int i = 0; i < map_size; i++){
    vector<int> map_row;
    for(int j = 0; j < map_size; j++){
      map_row.push_back(map[i][j]);
    }
    FindingPath(map_row);
  }

  for(int i = 0; i < map_size; i++){
    vector<int> map_row;
    for(int j = 0; j < map_size; j++){
      map_row.push_back(map[j][i]);
    }
    FindingPath(map_row);
  }

  cout << result << endl;

}