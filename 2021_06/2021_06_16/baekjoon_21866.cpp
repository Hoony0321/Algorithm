#include<iostream>

using namespace std;

int main(){
  int max_score[9] = {100,100,200,200,300,300,400,400,500};
  int list[9];
  bool isNone = true;
  bool isHacker = false;

  for(int i = 0; i < 9; i++){
    cin >> list[i];
  }
  
  int sum = 0;
  for(int i = 0; i < 9; i++){
    sum += list[i];
    if(list[i] > max_score[i]) {isHacker = true; break;}
  }
  if(sum >= 100) isNone = false;
  if(isNone){cout << "none" << "\n";}
  else if(isHacker){cout << "hacker" << "\n";}
  else{cout << "draw" << "\n";}



}