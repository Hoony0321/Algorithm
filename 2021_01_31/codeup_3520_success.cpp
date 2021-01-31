#include<iostream>
#include<vector>

using namespace std;

int mapSize;
vector<int> currentMap;

int number_of_availableCase = 0;
int number_of_answer = 3;

bool CheckingAvailablity(int row ,vector<int> currentMap){
  //일차원 배열을 사용해서 이미 행은 검사할 필요 X
  //avaiableNum 배열 사용해서 열 또한 검사할 필요 X

  int currentInput = currentMap[row];
  for(int i = 0; i < row; i++){ 
      if(row - i == abs(currentInput - currentMap[i])) return false; //대각선 검사
  }

  return true;
}

void FindingCase(int row,  vector<bool> availableNum, vector<int> currentMap){
  if(row == mapSize) { // 완료 - 가능한 경우
    number_of_availableCase++;   
    if(number_of_answer > 0){
      for(auto elem : currentMap)
      { cout << elem + 1 << " ";}
      cout << endl;
    }
    number_of_answer--;
    return;
  }

  for(int i = 0; i < mapSize; i++){
    if(availableNum[i] == true){ 
      availableNum[i] = false; 
      currentMap[row] = i;
      if(CheckingAvailablity(int row, currentMap)){
        FindingCase(++row, availableNum, currentMap);
      } 
      availableNum[i] = false;
    }
  }
}



int main(){
  cin >> mapSize;

  currentMap.resize(mapSize, -1);
  vector<bool> availableNum(mapSize, true);

  FindingCase(0,availableNum,currentMap);

  cout << number_of_availableCase << endl;


}