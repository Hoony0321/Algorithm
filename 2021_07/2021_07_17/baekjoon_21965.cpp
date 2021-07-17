//21965 - 제5회 천하제일 코딩대회 예선  - 선린인터넷고등학교 교가
#include<iostream>

using namespace std;


int main(){
  int N;
  int preNum = 0;
  int curNum = 0;
  bool increase = true;
  bool isMountain = true;
  cin >> N;
  for(int i = 1; i <= N; i++){
    cin >> curNum;
    if(increase){
      if(preNum == curNum){isMountain = false; break;}
      else  if(preNum > curNum){increase = false;}
    }
    else{
      if(preNum <= curNum){isMountain = false; break;}
    }
    preNum = curNum;
  }

  if(isMountain) cout << "YES" << "\n";
  else{cout << "NO" << "\n";}
  
  
}