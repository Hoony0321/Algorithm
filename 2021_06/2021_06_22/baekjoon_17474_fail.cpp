//트리문제? 이 방식으로는 시간초과로 안 됨.
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int vec_size,query_size;
vector<int> numList;

void function_1(int L,int R,int X){
  for(int i = L; i <= R; i++){
    numList[i] = min(numList[i],X);
  }
}

void function_2(int L,int R){
  int max_num = *max_element(numList.begin(),numList.end());
  cout << max_num << "\n";
}

void function_3(int L,int R){
  int sum = 0;
  for(int i = L; i <= R; i++){
    sum += numList[i];
  }
  cout << sum << "\n";
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  cin >> vec_size;

  for(int i = 0; i < vec_size; i++){
    int num;
    cin >> num;
    numList.push_back(num);
  }

  cin >> query_size;
  int function_case,L,R,X;
  for(int i = 0; i < query_size; i++){
    cin >> function_case >> L >> R;
    switch(function_case){
      case 1:
        cin >> X;
        function_1(L-1,R-1,X);
        break;
      case 2:
        function_2(L-1,R-1);
        break;
      case 3:
        function_3(L-1,R-1);
        break;
    }
  }
}