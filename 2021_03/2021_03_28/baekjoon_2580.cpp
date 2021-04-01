#include<iostream>
#include<vector>
using namespace std;
using matrix = vector<vector<int>>;

matrix map(9,vector<int>(9,0));
vector<pair<int,int>> blankList;

bool CheckingPossiblity(int& y, int& x){
  //가로줄 체크
  for(int i = 0; i < 9; i++){
    if(x != i){
      if(map[y][x] == map[y][i]) return false;
    }
  }
  //세로줄 체크
  for(int i = 0; i < 9; i++){
    if(y != i){
      if(map[y][x] == map[i][x]) return false;
    }
  }
  //3*3 박스 체크
  int box_y;
  int box_x;
  //box_y찾기
  if(y < 3){
    box_y = 0;
  }
  else if(y < 6){
    box_y = 3;
  }
  else{box_y = 6;}
  //box_x찾기
  if(x < 3){
    box_x = 0;
  }
  else if(x < 6){
    box_x = 3;
  }
  else{box_x = 6;}  

  for(int i = box_y; i < box_y +3; i++){
    for(int j = box_x; j < box_x+3; j++){
      if(y != i && x != j){
        if(map[y][x] == map[i][j]) return false;
      }
    }
  }

  return true;
}

void BackTracking(int step){
  if(step == blankList.size()){ //종료 조건
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
          cout << map[i][j] << " ";
        }
        cout << "\n";
      }
    exit(0);
  }
  int x,y;
  y = blankList[step].first;
  x = blankList[step].second;
  for(int i = 1; i <= 9; i++){
    map[y][x] = i;
    //체크 시작
    if(CheckingPossiblity(y,x) == true){BackTracking(step+1);}
    map[y][x] = 0;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);



  for(int i = 0; i < 9; i++){
    for(int j = 0; j < 9; j++){
      int input_val;
      cin >> input_val;
      if(input_val == 0){blankList.push_back(make_pair(i,j));}
      map[i][j] = input_val;
    }
  }

  BackTracking(0);


}