#include<iostream>
#include<vector>
#include<math.h>

using namespace std;

//맨 위 부터 시계방향으로

int number_digital[10][7] = {{1,1,1,1,1,1,0},{0,1,1,0,0,0,0},{1,1,0,1,1,0,1},{1,1,1,1,0,0,1},{0,1,1,0,0,1,1},{1,0,1,1,0,1,1},{1,0,1,1,1,1,1},{1,1,1,0,0,0,0},{1,1,1,1,1,1,1},{1,1,1,1,0,1,1}};

vector<vector<int>> reverse_map(10,vector<int>(10,-1));


int max_floor, digit, reverse, current;
int result = 0;

void solution(vector<int> number, int times, vector<bool> changed){
  int currentNum = 0;
  for(int i = 0; i < digit; i++){
    currentNum += number[i] * pow(10,i);
  }
  if(currentNum > max_floor) return;
  if(times > reverse) return;
  else{
    result++;}

  for(int i = 0; i < digit; i++){
    if(!changed[i]){ //아직 바꾸지 않음.
      changed[i] = true;
      for(int j = 0; j < 10; j++){ //0 ~ 9까지 수로 바꾸기
        if(reverse_map[number[i]][j] != 0){
          int origin = number[i];
          number[i] = j;
          solution(number,times + reverse_map[origin][j],changed);
          number[i] = origin;
        }
      }
    }
  }

}

int main(){
  cin >> max_floor >> digit >> reverse >> current;

  //reverse_map 채우기
  for(int i = 0; i <= 9; i++){
    int* fromNum = number_digital[i];
    for(int j = 0; j <= 9; j++){
      int* toNum = number_digital[j];
      if(reverse_map[i][j] == -1){ //아직 채워지지 않음.
        if(i == j) reverse_map[i][j] = 0;
        else{
          int diffrence = 0;
          for(int k = 0; k < 7; k++){diffrence += fromNum[k] != toNum[k] ? 1 : 0;}
          reverse_map[i][j] = diffrence; reverse_map[j][i] = diffrence;
        }
      }
    }
  }

  vector<int> number(digit,0);
  string str = to_string(current);
  for(int i = str.size()-1; i >= 0; i--){
    number[i] = str[str.size() - 1 - i] - '0';
  }
  vector<bool> changed(digit,false);
  solution(number,0,changed);

  cout << result - 1 << "\n";

  
}