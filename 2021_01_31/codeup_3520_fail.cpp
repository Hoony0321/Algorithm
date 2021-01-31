#include<iostream>
#include<vector>

using namespace std;

int mapSize;
vector<int> currentMap;

int number_of_availableCase = 0;
int number_of_answer = 3;

bool CheckingAvailablity(int row, vector<int> currentMap){


  int currentInput = currentMap[row];
  for(int i = 0; i < row; i++){ 
      if(currentInput == currentMap[i]) return false; //행 검사
      if(row - i == abs(currentInput - currentMap[i])) return false; //대각선 검사
  }

  return true;
}

void FindingCase(int row, vector<int> currentMap){
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
    currentMap[row] = i;
    if(CheckingAvailablity(row, currentMap) == true){
        FindingCase(row+1, currentMap);
    }
  }
}



int main(){
  cin >> mapSize;

  currentMap.resize(mapSize, -1);

  FindingCase(0,currentMap);

  cout << number_of_availableCase << endl;


}