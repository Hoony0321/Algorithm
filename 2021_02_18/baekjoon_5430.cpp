#include<deque>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

void SettingInput(string& order, deque<int>& numList, int& numArray){
  cin  >> order >> numArray;

  char inputNumlist[400001];
  cin >> inputNumlist;

  char* ptr = strtok(inputNumlist, "[,]");
  while(ptr != NULL){
    numList.push_back(stoi(ptr));
    ptr = strtok(NULL,"[,]");
  }

}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  int numTestCase;
  cin >> numTestCase;

  
  //각 테스트케이스 실행
  for(int i = 0; i < numTestCase; i++){
    int num_Array, num_temp;
    deque<int> numList;
    string inputOrder;
    SettingInput(inputOrder,numList,num_Array);


    bool reverse = false;
    bool isError = false;
    string answer = "";
    for(int k = 0; k < inputOrder.size(); k++){
      if(inputOrder[k] == 'R'){
        reverse = !reverse;
      }
      else{
        if(numList.empty()){isError = true; break;}
        else{
          if(!reverse){
            numList.pop_front();
          }
          else{
            numList.pop_back();
          }
        }
      }
    }

    if(isError){cout << "error" << "\n";}
    else{
      if(numList.empty()){
        cout << "[]" <<'\n';
      }
      else{
        answer += "[";
        while(!numList.empty()){
          if(!reverse){
            answer += to_string(numList.front());
            answer += ",";
            numList.pop_front();
          }
          else{
            answer += to_string(numList.back());
            answer += ",";
            numList.pop_back();
          }
          
        }
        answer[answer.size()-1] = ']';
        cout << answer << "\n";
      }
      
    }
  
  }


}