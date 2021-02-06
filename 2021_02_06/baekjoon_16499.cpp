//baekjoon_16499_동일한 단어 그룹화하기
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

vector<bool> groupIn;
vector<string> inputString;
int n;
int group = 0;

int main(){
  cin >> n;
  groupIn.resize(n,false);
  for(int i = 0; i < n; i++){
    string str;
    cin >> str;
    sort(begin(str),end(str));
    
    inputString.push_back(str);
  }


  for(int i = 0; i < n-1; i++){
    if(groupIn[i] == false){
      group += 1;
        for(int j = i+1; j < n; j++){
          if(groupIn[j] == false){
            if(inputString[i].compare(inputString[j]) == 0){
              groupIn[j] = true;
            }
          }
        }
    }
    
  }
  if(groupIn[n-1] == false) group += 1;
  cout << group << endl;
  
}