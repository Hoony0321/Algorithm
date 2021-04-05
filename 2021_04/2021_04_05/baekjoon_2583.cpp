#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int map[102][102] = {0,};
bool visited[102][102] = {false,};
int M,N,K;
vector<int> area;

void FindArea(int step, int y, int x){
  if(visited[y][x] == true) return; //이미 방문한 경우 종료

  visited[y][x] = true;
  if(map[y][x] == 1) return; //벽인 경우 종료
  
  //벽이 아닌 경우
  area[step] += 1;

  //왼쪽
  if(x-1>=1){
    FindArea(step,y,x-1);
  }

  //오른쪽
  if(x+1<=N){
    FindArea(step,y,x+1);
  }

  //위쪽
  if(y-1>=1){
    FindArea(step,y-1,x);
  }

  //아래쪽
  if(y+1<=M){
    FindArea(step,y+1,x);
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> M >> N >> K;
  
  //직사각형 입력 받기
  for(int a = 0; a < K; a++){
    int left_x,bottom_y,right_x,top_y;
    cin >> left_x >> bottom_y >> right_x >> top_y;
    //직사각형 채우기
    for(int i = bottom_y+1; i <= top_y; i++){
      for(int j = left_x+1; j <= right_x; j++){
        map[i][j] = 1;
      }
    }
  }

  int step = -1;
  for(int i = 1; i <= M; i++){
    for(int j = 1; j <= N; j++){
      if(map[i][j] == 0 && visited[i][j] == false){
        area.push_back(0);
        step += 1;
        FindArea(step,i,j);
      }
    }
  }

  cout << area.size() << "\n";
  sort(area.begin(), area.end());
  for(auto elem : area){cout << elem << " ";}
  cout << "\n";


}