#include<iostream>
#include<stack>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  int array_size;
  cin >> array_size;
  int* array = new int[array_size]; // 배열 동적 할당
  int* answer = new int[array_size]; //배열 동적 할당 및 초기화

  for(int i = 0; i < array_size; i++){
    cin >> array[i];
  }

  stack<int> stack;
  //탐색 시작 - stack 비어있으면 현재 index stack에 push 아니면 탐색 후 push -> 위에 있는 스택일수록 작은거!
  for(int i = 0; i < array_size; i++){ //마지막 원소는 탐색할 필요 x
    if(!stack.empty()){
      int stack_size = stack.size();
      for(int j = 0; j < stack_size; j++){
        if(array[stack.top()] >= array[i]) break;
        else{
          answer[stack.top()] = array[i];
          stack.pop();
        }
      }
    }
    stack.push(i);
  }

  while(!stack.empty()){
    answer[stack.top()] = -1;
    stack.pop();
  }

  for(int i = 0; i < array_size; i++){
    cout << answer[i] << " ";
  }
  cout << "\n";

  delete[] answer;//배열 동적 메모리 delete
  delete[] array;//배열 동적 메모리 delete

}