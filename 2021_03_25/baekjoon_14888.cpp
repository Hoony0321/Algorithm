#include<iostream>
#include<vector>

using namespace std;

long min_val = 1000000000;
long max_val = -1000000000;
int N;

void DFS(int index, long val,vector<int>& num_array, const vector<int> oper_array){
  if(index == N-1){ //종료
    if(val < min_val) min_val = val;
    if(val > max_val) max_val = val;
    return;
  }

  index += 1;

  for(int i = 0; i < 4; i++){
    vector<int> temp_array;
    temp_array.resize(4);
    copy(oper_array.begin(), oper_array.end(), temp_array.begin());
    if(oper_array[i] != 0){
      temp_array[i] -= 1;
      switch(i){
        case 0:
          DFS(index, val + num_array[index], num_array ,temp_array);
          break;
        case 1:
          DFS(index, val - num_array[index], num_array ,temp_array);
          break;
        case 2:
          DFS(index, val * num_array[index], num_array ,temp_array);
          break;
        case 3:
          DFS(index, val / num_array[index], num_array ,temp_array);
          break;
      }
    }
  }

}


int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  vector<int> num_array;
  vector<int> oper_array(4);
  num_array.resize(N);

  
  for(int i = 0; i < N; i++){
    cin >> num_array[i];
  }
  for(int i = 0; i < 4; i ++){
    cin >> oper_array[i];
  }

  DFS(0,long(num_array[0]),num_array, oper_array);

  cout << max_val << "\n";
  cout << min_val << "\n";


}