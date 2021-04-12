#include<iostream>
#include<vector>


using namespace std;

int N,M;
vector<vector<int>> map;
vector<vector<int>> cameraList;
int array_direction = {{-1,0},{0,+1},{+1,0},{0,-1}}; //북 동 남 서

class camera{
private:
  int x;
  int y;
  int direction;
public :
  camera(int _direction,int _y, int _x){
    direction = _direction
    y = _y;
    x = _x;
  }

  void getLocation(int& _y, int& _x){_y = y; _x = x;}
  int getDirection(){return direction;}
  void ChangeDirection(){direction = (direction+1)%4;}
}

class camera_No1 : camera{
public :
  void CheckingArea(vector<int> sight){
    //좌표 설정
    int ahead_y = sight[0] + array_direction[direction][0];
    int ahead_x = sight[1] + array_direction[direction][1];

    //좌표 검사
    if(ahead_y < 1 || ahead_y > N){ return; }
    else if(ahead_x < 1 || ahead_x > M){ return;}

    //감시 시작
    if(map[ahead_y][ahead_x] == 6){ return; }
    else if(map[ahead_y][ahead_x] == 0) map[ahead_y][ahead_x] = 7;

    CheckingArea({ahead_y,ahead_x});
  }

}

void duplicatePermutation(int depth){
    if(depth == cameraList.size()){
        FindArea(direction_result);
        return;
    }

    for(int i = 0; i < 4; i++){
        direction_temp[depth] = i;
        duplicatePermutation(depth + 1);
    }
}

void FindArea(int* direction_result){
  for(int i = 0; i < cameraList.size(); i++){
    switch(cameraList[i][0]){
      case 1:
        camera_No1 camera_no1(direction_result[0],cameraList[i][1],cameraList[i][2]);
        camera_no1.CheckingArea(camera_no1.);
        break;
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N >> M;
  map.resize(N+1);
  for(int i = 0; i < N; i++){
    map[i].resize(M+1);
  }
  for(int i = 1; i <= N; i++){
    for(int j = 1; j <= M; j++){
      int temp;
      cin >> temp;
      if(temp >= 1 && temp <= 5){
        cameraList.push_back({temp,i,j});
      }
      map[i][j] = temp;
    }
  }

  int direction_temp = {0,};
  duplicatePermutation(int depth);

  


}