#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N,M,max_area;
vector<vector<int>> map(10,vector<int>(10,1));

void spreading(vector<vector<int>>& map, int y, int x){
  //왼쪽
  if(map[y][x-1] == 0){
    map[y][x-1] = 2;
    spreading(map,y,x-1);
  }
  //오른쪽
  if(map[y][x+1] == 0){
    map[y][x+1] = 2;
    spreading(map,y,x+1);
  }
  //위쪽
  if(map[y-1][x] == 0){
    map[y-1][x] = 2;
    spreading(map,y-1,x);
  }
  //아래쪽
  if(map[y+1][x] == 0){
    map[y+1][x] = 2;
    spreading(map,y+1,x);
  }
}

int spreadingVirus(vector<vector<int>>& map, vector<pair<int,int>>& virus){
  for(int i = 0; i < virus.size(); i++){
    spreading(map,virus[i].first,virus[i].second);
  }

  int safeArea = 0;
  for(auto elem1 : map){
    for(auto elem2 : elem1){
      if(elem2 == 0) safeArea += 1;
    }
  }

  return safeArea;
}

void calculatingSafeArea(vector<vector<int>> map){
  vector<pair<int,int>> virus;
  for(int i = 1; i <= N; i++){
    for(int j = 1; j <= M; j++){
      if(map[i][j] == 2){
        virus.push_back(make_pair(i,j));
      }
    }
  }
  int safeArea = spreadingVirus(map,virus);
  if(safeArea > max_area) {
    max_area = safeArea;
  }
}

void DFS(int index, vector<vector<int>> map, int prev){
  if(index == 3){
    calculatingSafeArea(map);
    return;
  }
  for(int i= 1; i <= N; i++){
    for(int j=1; j <= M; j++){
      if(map[i][j] == 0 && prev < M*i + j){
        map[i][j] = 1; //변형
        DFS(index+1,map,M*i + j); //DFS진행
        map[i][j] = 0; //원복
      }
    }
  }
}

int main(){
  cin >> N >> M;
  for(int i = 1; i<= N; i++){
    for(int j = 1; j<= M; j++){
      cin >> map[i][j];
    }
  }


  DFS(0,map,-1);

  cout << max_area << "\n";


}

