//21964 - 제5회 천하제일 코딩대회 예선  - 선린인터넷고등학교 교가
#include<iostream>
#include<string>
using namespace std;

int length;

int main(){
  cin >> length;
  string inputData;
  cin >> inputData;

  cout << inputData.substr(length - 5) << "\n";

}
