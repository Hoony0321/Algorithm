#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
  int num_testCase;
  cin >> num_testCase;
  for(int l = 0; l < num_testCase; l++){
    int N,M;
    int order = 0;
    queue<pair<int,int>> printQueue;
    cin >> N >> M;

    vector<int> importance_Vec;
    for(int i = 0; i < N; i++){
      int doc_importance;
      cin >> doc_importance;
      importance_Vec.push_back(doc_importance);
      printQueue.push(make_pair(doc_importance,i));
    }

    while(1){
      sort(importance_Vec.begin(),importance_Vec.end());
      int max = *(importance_Vec.end() - 1);

      while(max != printQueue.front().first){
        pair<int,int> elem_first = printQueue.front();
        printQueue.pop();
        printQueue.push(elem_first);
      }

      order += 1;
      if(printQueue.front().second == M){break;}
      printQueue.pop();
      importance_Vec.erase(importance_Vec.end()-1);

    }

    cout <<order << "\n";



  }
}
