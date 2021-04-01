#include <iostream>
#include<vector>
#include<math.h>

using namespace std;

//codeup_3540 : 0 만들기 게임 - breadth first search(BFS)

int number_of_num;
bool isPlus = true;
int sum = 0;


void Calculating(int prevNum){
  if(isPlus) sum += prevNum;
  else sum -= prevNum;
}

bool CheckingIsZero(vector<char>currentCase){
  sum = 0;
  int prevNum = currentCase[0] - '0';
  isPlus = true;
  for(int i = 0; i < number_of_num; i++){
    switch(currentCase[i*2+1]){
      case' ':
        prevNum = prevNum * 10 + currentCase[i*2+2] - '0';
        break;
      case'+':
        Calculating(prevNum);
        prevNum = currentCase[i*2+2] - '0';
        isPlus = true;
        break;
      case'-':
        Calculating(prevNum);
        prevNum = currentCase[i*2+2] - '0';
        isPlus = false;
        break;
    }
  } 
  Calculating(prevNum);

  if(sum == 0) return true;
  return false;
}

int count = 3;
void BackTracking(int index, vector<char> currentCase){
  
  if(index == number_of_num){
    if(CheckingIsZero(currentCase) == true){
      count--;
      if(count == 0){
             for(auto elem : currentCase){
          cout << elem;
        }
        cout << endl;
        count = 3;
      }

    }
    
    return;
  }

  //=====push operation=====//

  currentCase[index*2 + 1] = ' ';  //blank operation push
  BackTracking(index+1, currentCase);

  currentCase[index*2 + 1] = '+';  //plus operation push
  BackTracking(index+1, currentCase);

  currentCase[index*2 + 1] = '-';  //minus operation push
  BackTracking(index+1, currentCase);




}

int main(){
  cin >> number_of_num;
  vector<char> currentCase(number_of_num*2 - 1, 'X');
  for(int i = 0; i < number_of_num; i++){
    currentCase[i*2] = *to_string(i+1).c_str();
  }


  BackTracking(0,currentCase);
}