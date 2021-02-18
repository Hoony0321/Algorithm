#include<iostream>

using namespace std;

int FindingMaximum(int* numList, int N, int M){
  int max = 0;
  for(int i = 0; i < N-2; i++){
    for(int j = i+1; j < N -1; j++){
      for(int k = j+1; k < N; k++){
        int sum = numList[i] + numList[j] + numList[k];
        if(max < sum && sum <= M) max = sum;
      }
    }
  }
  return max;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  int N,M;
  cin >> N >> M;

  int* numList = new int[N];
  for(int i = 0; i < N; i++){
    cin >> numList[i];
  }

  int result = FindingMaximum(numList,N, M);
  cout << result << "\n";
  delete[] numList;
}