#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;


vector<vector<char>> map(5, vector<char>(5));
vector<int> numList;

void DFS(int step,int y, int x, string num){
  if(step == 6){ //종료 조건
    int result = stoi(num.c_str());
    vector<int>::iterator iter = find(numList.begin(), numList.end(), result);
    if(iter == numList.end()){
      numList.push_back(result);
    }
    return;
  }

  //왼쪽
  if(x-1>=0){
    DFS(step+1,y,x-1,num + map[y][x-1]);
  }

  //오른쪽
  if(x+1<5){
    DFS(step+1,y,x+1,num + map[y][x+1]);
  }

  //위쪽
  if(y-1>=0){
    DFS(step+1,y-1,x,num + map[y-1][x]);
  }

  //아래쪽
  if(y+1<5){
    DFS(step+1,y+1,x,num + map[y+1][x]);
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  for(auto& elem : map){
    for(auto& elem2 : elem){
      cin >> elem2;
    }
  }

  for(int i = 0; i < 5; i++){
    for(int j = 0; j < 5; j++){
      string temp = "";
      DFS(1,i,j,temp + map[i][j]);
    }
  }

  cout << numList.size() << "\n";
}





