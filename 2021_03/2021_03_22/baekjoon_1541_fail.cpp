#include<iostream>
#include<string.h>
#include<string>
#include<vector>

using namespace std;


int main(){
  char inputFormula[52];
  cin >> inputFormula;

  vector<int> pos;
  char *ptr = strtok(inputFormula,"-");

  
  while(ptr != NULL){
    pos.push_back(strlen(ptr) + 1);
    ptr = strtok(NULL,"-");
  }

  int sum = 0;
  if(pos.empty()){
    char *ptr = strtok(inputFormula,"+");
    while(ptr != NULL){
      sum += stoi(ptr);
    }
  }
  else{
    bool first = true;
    int pre_pos = 0;
    for(int i = 0; i < pos.size(); i++){
      cout << pos[i] << "\n";
      string temp = string(inputFormula).substr(pre_pos,pos[i] - pre_pos-1);
      pre_pos = pos[i];
      cout << temp << "\n";
    } 
  }

  cout << sum << "\n";
}