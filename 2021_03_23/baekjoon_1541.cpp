#include<iostream>
#include<string.h>
#include<string>
#include<vector>

using namespace std;

/* 내가 짠 코드...
int main(){
  char inputFormula[52];
  cin >> inputFormula;
  char originInput[52];
  strcpy(originInput, inputFormula);
  vector<int> pos;
  char *ptr = strtok(inputFormula,"-");

  int offset = -1;
  while(ptr != NULL){
    if(offset != -1){
      pos.push_back(pos[offset] + strlen(ptr)+1);
    }
    else pos.push_back(strlen(ptr));
    offset++;
    ptr = strtok(NULL,"-");
  }



  
  int sum = 0;
  if(pos.size() == 1){ // '-' 존재 X
    char *ptr = strtok(originInput,"+");
    while(ptr != NULL){
      sum += stoi(ptr);
      ptr = strtok(NULL,"+");
    }
  }
  else{ // '-' 존재 O
    bool first = true;
    int pre_pos = 0;
    for(int i = 0; i < pos.size(); i++){
      string temp = string(originInput).substr(pre_pos,pos[i] - pre_pos);
      pre_pos = pos[i]+1;
      char* temp2 = new char[temp.size() + 1];
      copy(temp.begin(),temp.end(),temp2);
      temp2[temp.size()] = '\0';
      char *ptr = strtok(temp2,"+");

      int sub_sum = 0;
      while(ptr != NULL){
        sub_sum += stoi(ptr);
        ptr = strtok(NULL,"+");
      }
      if(first){sum += sub_sum; first = false;}
      else sum -= sub_sum; 

      delete[] temp2;
    } 
  }

  cout << sum << "\n";
  
}
*/


int main(void){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  char operation;
  int answer , num;
  bool minus = false;
  int sub_sum = 0;

  cin >> answer; //처음에는 숫자가 입력되므로 바로 answer에 더해줌.

  while(cin >> operation){ //그 다음 끝날대까지 operation 받아주면서 계산 시작
    if(operation == '-'){ //-가 나온 경우
      minus = true;
    }
    cin >> num;
    if(minus) answer -= num;
    else answer += num;
    
  }
  cout << answer << "\n";
}


