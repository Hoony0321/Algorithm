#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N,M,max_area;


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

void DFS(vector<vector<int>> map){
  vector<int> availableCase;
  availableCase.resize(N*M);
  availableCase[0] = 1; availableCase[1] = 1; availableCase[2] = 1;
  do{
    vector<vector<int>> map_temp(10,vector<int>(10));
    copy(map.begin(),map.end(),map_temp.begin());

    vector<int> choiceArea;
    for(int i = 0; i < N*M; i++){
      if(availableCase[i] == 1){choiceArea.push_back(i);}
    }

    bool available = true;
    for(int i = 0; i < 3; i++){
      if(map_temp[choiceArea[i]/M+1][choiceArea[i]%M+1] != 0){available = false; break;} 
      map_temp[choiceArea[i]/M+1][choiceArea[i]%M+1] = 1;
    }

    if(available){calculatingSafeArea(map_temp);}

  }while(prev_permutation(availableCase.begin(),availableCase.end()));

}

int main(){
  vector<vector<int>> map(10,vector<int>(10,1));
  cin >> N >> M;
  for(int i = 1; i<= N; i++){
    for(int j = 1; j<= M; j++){
      cin >> map[i][j];
    }
  }


  DFS(map);

  cout << max_area << "\n";


}

