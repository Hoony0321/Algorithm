#include<iostream>
#include<queue>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  queue<int> queue;
  int queue_size;
  cin >> queue_size;
  for(int i = 1; i <= queue_size; i++){
    queue.push(i);
  }

  while(queue.size() != 1){
    queue.pop();
    int num = queue.front();
    queue.pop();
    queue.push(num);
  }

  cout << queue.front() << "\n";
}