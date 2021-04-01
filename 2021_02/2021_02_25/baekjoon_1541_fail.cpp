#include<iostream>
#include<string.h>
#include<string>

using namespace std;

bool checkOperation(char* inputFormula, int pos){
  if(inputFormula[pos] == '-'){
      return true;
    }
    else{
      return false;
    }
}

int main(){
  char inputFormula[52];
  cin >> inputFormula;

  char *ptr = strtok(inputFormula,"-");

  bool first = true;
  int sum = 0;
  int pos = strlen(ptr) + 1; 
  while(ptr != NULL){
    cout << "ptr : " <<ptr << "\n";
    char *ptr2 = strtok(ptr,"+");
    int preSum = 0;
    while(ptr2 != NULL){
      if(first){
        cout << sum << " + " << stoi(ptr2) << "\n"; 
        sum += stoi(ptr2);
        
      }
      else{
        cout << "preSum : "<< preSum << " + " << stoi(ptr2) << "\n";
        preSum += stoi(ptr2);
      }
      ptr2 = strtok(NULL,"+");
    }
    if(first) first = false;

    cout << "sum - preSum : " << sum << "-" << preSum << "\n";
    sum -= preSum;

    string temp;
    for(int i = pos; i < strlen(inputFormula); i++){
      temp += inputFormula[i];
    }
    ptr = strtok(temp.c_str(),"-");
  }

  cout << sum << "\n";
}