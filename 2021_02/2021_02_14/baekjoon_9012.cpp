#include<iostream>
#include<stack>
#include<cstring>

using namespace std;

int main(){
  int n;
  std::stack<char> stack_obj;
  scanf("%d", &n);
  
  for(int i = 0; i < n; i++){
    char temp[50];
    scanf("%s", temp);

    for(int i = 0; i < strlen(temp); i++){
      
      //연산시작
      if(stack_obj.empty()) stack_obj.push(temp[i]);
      else{
        if(temp[i] == ')'){
          if(stack_obj.top() == '(') stack_obj.pop();
          else stack_obj.push(temp[i]);
        }
        else{
          stack_obj.push(temp[i]);
        }
      }
    }
    if(!stack_obj.empty()) printf("NO\n");
    else printf("YES\n");

    while(!stack_obj.empty()) stack_obj.pop();
  }

}