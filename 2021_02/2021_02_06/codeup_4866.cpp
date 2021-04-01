//codeup_4866 : 방 배정 (중등) - 2019정올1차
#include<iostream>
#include<vector>

using namespace std;

int N,K;
vector<vector<int>> std_info;
int result = 0;
vector<vector<int>> classifyList(3,vector<int>(2,0));

int CalculatingRooms(int num){
  if(num % K == 0){
    return num / K;
  }
  else return num / K + 1;
}

void ClassifingStd(){
  for(int i = 0 ; i < N; i++){
    int num = std_info[i][1];
    switch(num){
      case 1:
      case 2:
        if(std_info[i][0] == 0) classifyList[0][0] += 1;
        else classifyList[0][1] += 1;
        break;
      case 3:
      case 4:
        if(std_info[i][0] == 0) classifyList[1][0] += 1;
        else classifyList[1][1] += 1;
        break;
      case 5:
      case 6:
        if(std_info[i][0] == 0) classifyList[2][0] += 1;
        else classifyList[2][1] += 1;
        break;
    }
  }
}

int main(){
  cin >> N >> K;
  for(int i = 0; i < N; i++){
    int a,b;
    cin >> a >> b;
    std_info.push_back({a,b});
  }

  ClassifingStd();
  //1학년~2학년
  int std = classifyList[0][0] + classifyList[0][1];
  result += CalculatingRooms(std);

  //3~4
  result += CalculatingRooms(classifyList[1][0]);
  result += CalculatingRooms(classifyList[1][1]);

  //5~6
  result += CalculatingRooms(classifyList[2][0]);
  result += CalculatingRooms(classifyList[2][1]);

  cout << result << endl; 
}