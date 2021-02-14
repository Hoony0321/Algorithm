#include<cstdio>
#include<cstring>
#include<stack>

using namespace std;

void CheckingIsValid(char* sentence, stack<char>& stack_obj){
  for(int i = 0; i < strlen(sentence); i++){
    if(sentence[i] == '(' || sentence[i] == '['){
      stack_obj.push(sentence[i]);
    }
    else if(sentence[i] == ')'){
      if(stack_obj.empty()){
        printf("no\n");
        return;
      }
      if(stack_obj.top() == '(') stack_obj.pop();
      else stack_obj.push(sentence[i]);
    }
    else if(sentence[i] == ']'){
      if(stack_obj.empty()){
        printf("no\n");
        return;
      }
      if(stack_obj.top() == '[') stack_obj.pop();
      else stack_obj.push(sentence[i]);
    }
  }

  if(stack_obj.empty()) printf("yes\n");
  else printf("no\n");
}

int main(){
  char inputStr[102];
  stack<char> stack_obj;

  while(1){
    fgets(inputStr, 101, stdin);
    inputStr[strlen(inputStr) -1] = '\0';
    if(strcmp(inputStr,".\0") == 0 ){
      break;
    }
    else{ //판단 시작
      CheckingIsValid(inputStr, stack_obj);
      while(!stack_obj.empty()) stack_obj.pop(); // clear stack
    }
  }

}