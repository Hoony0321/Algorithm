#include<iostream>
#include<stack>
#include<cstring>


using namespace std;

int main(){
  stack<int> stack_object;
  int n;
  scanf("%d", &n);
  getchar(); //버퍼지우기
  for(int i = 0; i < n; ++i){
    char num[10];
    scanf("%s", num);
    if(strcmp(num,"push") == 0){ //push 인 경우
      int temp;
      scanf("%d", &temp);
      stack_object.push(temp);
    }
    else if(strcmp(num,"top") == 0){
      if(!stack_object.empty()) cout << stack_object.top() <<"\n";
      else printf("-1\n");
    }
    else if(strcmp(num,"pop") == 0){
      if(!stack_object.empty()) {cout << stack_object.top() << "\n"; stack_object.pop();}
      else printf("-1\n");
      
    }
    else if(strcmp(num,"size") == 0){
      printf("%ld\n", stack_object.size());
    }
    else if(strcmp(num,"empty") == 0){
      if(stack_object.empty()) printf("1\n");
      else printf("0\n");
    }
  }
  getchar();



}