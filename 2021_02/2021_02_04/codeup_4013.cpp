//codeup_4013 : 진법 변환 - 정올1번문제

#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

string str_16 = "0123456789ABCDEF";

void PrintingBinary(int num){
  vector<int> answer;
  int share, remain;
  while(num != 0){
    share = num / 2;
    remain = num % 2;
    num = share;
    answer.push_back(remain);
  }
  reverse(answer.begin(), answer.end());
  cout << "2 ";
  for(auto elem : answer){
    cout << elem;
  }
  cout << endl;
}

void PrintingEight(int num){
  vector<int> answer;
  int share, remain;
  while(num != 0){
    share = num / 8;
    remain = num % 8;
    num = share;
    answer.push_back(remain);
  }
  reverse(answer.begin(), answer.end());
  cout << "8 ";
  for(auto elem : answer){
    cout << elem;
  }
  cout << endl;
}

void PrintingSixteen(int num){
  vector<char> answer;
  int share, remain;
  while(num != 0){
    share = num / 16;
    remain = num % 16;
    num = share;
    answer.push_back(str_16[remain]);
  }
  reverse(answer.begin(), answer.end());
  cout << "16 ";
  for(auto elem : answer){
    cout << elem;
  }
  cout << endl;
}



int main(){
  int num;
  cin >> num;
  PrintingBinary(num);
  PrintingEight(num);
  PrintingSixteen(num);

}