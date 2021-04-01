#include<cstdio>
#include<stack>

using namespace std;

int main(){
  stack<int> stack_obj;
  int K;

  scanf("%d", &K);
  for(int i = 0; i < K; i++){
    int num;
    scanf("%d", &num);
    if(num != 0){
      stack_obj.push(num);
    }
    else{
      if(!stack_obj.empty()) stack_obj.pop();
    }
  }

  int sum = 0;
  while(!stack_obj.empty()){
    sum += stack_obj.top();
    stack_obj.pop();
  }

  printf("%d\n" , sum);
}