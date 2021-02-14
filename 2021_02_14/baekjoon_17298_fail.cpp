#include<iostream>
#include<vector>
#include<stack>

using namespace std;

vector<int> vec;

int FindingNGE(int index, int stack_size, stack<int> numStack){
  int result = -1;
  for(int i = stack_size; i > index+1; i--){
    if(vec[index] < numStack.top()){
      result = numStack.top();
    }
    numStack.pop();
  }
  return result;
}

int main(){
  int n;
  cin >> n;
  stack<int> numStack;
  for(int i = 0 ; i < n; i++){
    int num;
    cin >> num;
    vec.push_back(num);
    numStack.push(num);
  }

  vector<int> result;
  for(int i = 0; i < n; i++){
    result.push_back(FindingNGE(i,n,numStack));
  }
  for(auto elem : result) cout << elem << " ";
  cout << endl;

}