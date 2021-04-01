#include<cstdio>
#include<stack>

using namespace std;
int n;
int array[100000];
char answer[100000];
bool IsValid = true;
int index = 0;

void FindRequiredOperate(stack<int>& stack, int target_index, int stage){
  int target = array[target_index];
  if(stage < target){
    stack.push(stage+1);
    answer[index] = '+';
    index += 1;
    FindRequiredOperate(stack,target_index,stage+1);
    return;
  }

  while(!stack.empty()){
    if(stack.top() == target){
      answer[index] = '-';
      index += 1;
      stack.pop();
      if(target_index+1 == n) return;
      else{FindRequiredOperate(stack,target_index+1, stage); return;}
    }
    else{
      answer[index] = '-';
      index += 1;
      stack.pop();
    }
  }

  IsValid =false;
  return;
}

int main(){
  
  stack<int> stack;
  scanf("%d",&n);
  for(int i = 0; i < n; i++){
    int num;
    scanf("%d",&num);
    array[i] = num;
  }

  FindRequiredOperate(stack,0,0);
  
  if(IsValid == false) printf("NO\n");
  else{
    for(int i = 0; i <= index-1; i++){
      printf("%c\n",answer[i]);
    }
  }
}