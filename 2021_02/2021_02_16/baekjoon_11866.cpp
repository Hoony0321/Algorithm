#include<iostream>
#include<queue>
#include<vector>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);

  int N,K;
  queue<int> queue;
  vector<int> answer;
  cin >> N >> K;

  for(int i = 1; i <= N; i++){
    queue.push(i);
  }

  while(queue.size() != 1){
    int num;
    for(int i = 0; i <K-1; i++){
      //앞으로 한칸씩 이동
      num = queue.front();
      queue.pop();
      queue.push(num);
    }
    

    //answer배열에 첫번째 원소 넣기
    answer.push_back(queue.front());
    queue.pop();
  }
  answer.push_back(queue.front());

  cout << "<";
  for(int i = 0; i < answer.size()-1; i++){
    cout << answer[i] << ", ";
  }
  cout << *(answer.end()-1) << ">" << "\n";

}