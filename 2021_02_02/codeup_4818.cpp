#include<iostream>
#include<vector>

using namespace std;

//codeup_4818 : 격자상의 경로 - 메모제이션 기법 + 자료형 범위

int row;
int column;
int point; // 무조건 지나갸아 하는 점
vector<__int64_t> memory;

//===함수선언===//
__int64_t Factorial(int num);
__int64_t FindingCase(int row, int column);

__int64_t FindingAllCase();

__int64_t CalculatingMeduimLevel(int num1, int num2){
  __int64_t result = 1;
  for(int i = num1; i > num2; i--){
    result *= i;
  }
  return result;
}


//==main==//
int main(){
  cin >> row >> column >> point;
  memory.resize(row + column, 0);
  
  cout << FindingAllCase() << endl;;

}


//===함수정의===//
__int64_t Factorial(int num){
  if(memory[num] != 0) return memory[num]; //전에 이미 계산된 적 있음.

  if(num == 1 || num == 0) return 1;
  
  memory[num] = Factorial(num - 1) * num;
  return memory[num];

}

__int64_t FindingCase(int row, int column){
  if(row > column) return CalculatingMeduimLevel(row+column, row) / Factorial(column);
  else return CalculatingMeduimLevel(row+column, column) / Factorial(row);
}

__int64_t FindingAllCase(){
  if(point == 0){
    return FindingCase(row-1,column-1);
  }

  int point_row = (point - 1) / column;
  int point_column = (point - 1) % column;
  __int64_t result1= FindingCase(point_row,point_column);
  __int64_t result2= FindingCase(row - point_row - 1, column - point_column - 1);

  return result1 * result2;

}
