#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N;
vector<int> A;
vector<int> B;  

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  A.resize(N); B.resize(N);
  for(int i = 0; i < 2; i++){
    for(int j = 0; j < N; j++){
      switch(i){
        case 0:
          cin >> A[j];
          break;
        case 1:
          cin >> B[j];
          break;
      }
    }
  }

  
  sort(A.begin(), A.end());
  sort(B.begin(), B.end(),greater<int>());
  int sum = 0;
  for(int i = 0; i < N; i++){
    sum += A[i] * B[i];
  }

  cout << sum << "\n";

}