//baekjoon_19843_수면 패턴
#include<iostream>
#include<vector>

using namespace std;

int T;
int N;

vector<vector<int>> list;

constexpr unsigned int HashCode(const char* str)
{
    return str[0] ? static_cast<unsigned int>(str[0]) + 0xEDB8832Full * HashCode(str + 1) : 8603;
}

int ChangeDaytoInt(string day){
  int returnVal;
  switch(HashCode(day.c_str())){
    case HashCode("Mon"):
      returnVal = 1;
      break;
    case HashCode("Tue"):
      returnVal = 2;
      break;
    case HashCode("Wed"):
      returnVal = 3;
      break;
    case HashCode("Thu"):
      returnVal = 4;
      break;
    case HashCode("Fri"):
      returnVal = 5;
      break;
  }
  return returnVal;
}

int CalculatingSleepTime(vector<int> input){
  int time;
  if(input[0] == input[2]){
    time = input[3] - input[1];
  }
  else{
    time = input[3] + 24 - input[1];
    time += (input[2] - input[0] - 1)*24;
  }

  return time;
}

int main(){
  cin >> T >> N;
  list.resize(N);
  for(int i = 0; i < N; i++){
    list[i].resize(4);
    string day;
    cin >> day;
    list[i][0] = ChangeDaytoInt(day);
    cin >>list[i][1];
    cin >> day;
    list[i][2] = ChangeDaytoInt(day);
    cin >>list[i][3];
  }

  int totalSleep = 0;
  for(int i = 0 ; i < N; i++){
    totalSleep += CalculatingSleepTime(list[i]);
  }


  if(T - totalSleep > 48 ) cout << -1 << endl;
  else if(T - totalSleep < 0) cout << 0 << endl;
  else cout << T - totalSleep << endl;
  


}
