//16234
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int map[52][52];
vector<vector<pair<int,int>>> union_vec;
int N,L,R;


void DFS(int y,int x, bool visited[52][52], bool is_start, int prev){
  if(y == 0 || x == 0 || y == N+1 || x == N+1) return; //영역 벗어난 곳
  if(visited[y][x]) return;

  visited[y][x] = true;

  if(is_start){ //새로 탐색 시작한 곳 => 국경 열리는 곳 스타트 지점.
    union_vec.push_back({make_pair(y,x)});
    is_start =false;
  }
  else{ //연합에 포함 시키기
    int diff = abs(prev - map[y][x]);
    if(diff >= L && diff <= R){ //차이가 조건에 부합할 경우
      union_vec[union_vec.size()-1].push_back(make_pair(y,x));
    }
    else{return;} //차이가 조건에 부합하지 않음 => 종료
  }

  //위 방문
  DFS(y-1,x,visited,is_start,map[y][x]);
  //아래 방문
  DFS(y+1,x,visited,is_start,map[y][x]);
  //왼쪽 방문
  DFS(y,x-1,visited,is_start,map[y][x]);
  //오른쪽 방문
  DFS(y,x+1,visited,is_start,map[y][x]);
  return;
}



void OpenBorder(){
  bool visited[52][52];

  for(int i = 1; i <= N; i++){
    for(int j = 1; j <=N; j++){
      DFS(i,j,visited,true,0);
    }
  }
}

int main(){
  cin >> N >> L >> R;
  for(int i = 1; i <= N; i++){
    for(int j = 1; j <=N; j++){
      cin >> map[i][j];
    }
  }

  OpenBorder();

  for(auto elem : union_vec){
    for(auto elem2: elem){
      cout << "(" << elem2.first << " , " << elem2.second << ")   ";
    }
    cout << "\n"; 
  }


}