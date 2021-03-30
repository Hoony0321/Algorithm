#include<iostream>
#include<vector>

using namespace std;

int N,M;
int max_area = 0;
  vector<vector<int>> map;
  
//방향 {북 0 동 1 남 2 서 3}

int FindArea(vector<int> map, vector<int>& camera){
  int area = 0;
  
}

void DFS(int index, vector<int> camera){
  if(index == camera.size()){ //종료 조건

    return;
  }

  //카메라 방향 설정
  //북
  DFS(index+1, camera); 
  //동
  camera[index][4] += 1;
  DFS(index+1, camera);
  //남
  camera[index][4] += 1;
  DFS(index+1, camera);
  //서
  camera[index][4] += 1;
  DFS(index+1, camera);

}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  vector<vector<int>> camera; 
  cin >> N >> M;
  map.resize(N);
  for(int i = 0; i < N; i++){map[i].resize(M);}


  for(int i = 0; i < N; i++){
    for(int j = 0; j < M; j++){
      int num;
      cin >> num;
      if(0 < num && num <6){
        camera.push_back({i,j,num,0}); //위치, 카메라 번호, 방향
      }
      map[i][j] = num;
    }
  }

  DFS(0,camera);


}