//21966 - 제5회 천하제일 코딩대회 예선  - 선린인터넷고등학교 교가
#include<iostream>
#include<string>
#include<vector>

using namespace std;


int main(){
  int N;
  cin >> N;
  string inputData;
  cin >> inputData;

  vector<string> sentences;

  int startPoint = 0;
  int nextPoint = 0;
  while(inputData.find('.',startPoint) != string::npos){
    nextPoint = inputData.find('.',startPoint) + 1;
    sentences.push_back(inputData.substr(startPoint, nextPoint - startPoint - 1));
    startPoint = nextPoint;
  }

  if(N <= 25){
    cout << inputData  << "\n";
  }
  else{
    startPoint = 11;
    nextPoint = N - 12;
    string frontStr = inputData.substr(0,9);
    string endStr = inputData.substr(N - 10);
    string str = inputData.substr(startPoint, nextPoint - startPoint + 1);
    bool oneSentence = false;
    for(auto elem : sentences){
      string tempStr = elem + ".";
      if(tempStr.find(str) != string::npos){ //한 문장 안에 있음.
        frontStr = inputData.substr(0,startPoint - 0);
        endStr = inputData.substr(nextPoint+1);
        oneSentence = true; break;
      }
      else{ //한 문장 안에 없음
        //Nothing
      }
    }
    cout << frontStr;
    if(oneSentence) cout << "...";
    else cout << "......";
    cout << endStr << "\n";
  }
}