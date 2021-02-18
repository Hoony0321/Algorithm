#include<iostream>
#include<deque>

using namespace std;


deque<int> Check_front(deque<int> Deque, int& count, int target){
  while(target != Deque.front()){
      count += 1;
      int num = Deque.front();
      Deque.pop_front();
      Deque.push_back(num);
    }
    Deque.pop_front();
    return Deque;
}
deque<int> Check_back(deque<int> Deque, int& count, int target){
  while(target != Deque.front()){
      count += 1;
      int num = Deque.back();
      Deque.pop_back();
      Deque.push_front(num);
    }
    Deque.pop_front();
    return Deque;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);

  int N,M;
  cin >> N >> M;

  deque<int> Deque;
  for(int i = 0 ; i < N; i++){
    Deque.push_back(i+1);
  }

  
  int sum =0;
  //뽑기 시작
  for(int i = 0; i < M; i++){
    int target;
    cin >> target;

    int count_front = 0;
    int count_back = 0;

    deque<int> Deque_front = Check_front(Deque,count_front,target);
    deque<int> Deque_back = Check_back(Deque,count_back,target);

    if(count_front > count_back){sum += count_back; Deque = Deque_front;} 
    else {sum += count_front; Deque = Deque_back;}

    

  }

  cout << sum << "\n";


}