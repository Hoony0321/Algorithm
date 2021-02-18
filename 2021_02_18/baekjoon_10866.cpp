#include<iostream>
#include<deque>
#include<string>

using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);
  
  deque<int> Deque;
  string inputOrder;

  int N;
  cin >> N;

  for(int i = 0; i < N; i++){
    cin >> inputOrder;
    if(inputOrder == "push_front"){
      int num;
      cin >> num;
      Deque.push_front(num);
    }
    else if(inputOrder == "push_back"){
      int num;
      cin >> num;
      Deque.push_back(num);
    }
    else if(inputOrder == "pop_front"){
      if(Deque.empty()) cout << -1 << "\n";
      else{
        int num =   Deque.front();
        cout << num << "\n";
        Deque.pop_front();
      }
    }
    else if(inputOrder == "pop_back"){
      if(Deque.empty()) cout << -1 << "\n";
      else{
        int num =   Deque.back();
        cout << num << "\n";
        Deque.pop_back();
      }
      
    }
    else if(inputOrder == "size"){
      cout << Deque.size() << "\n";
    }
    else if(inputOrder == "empty"){
      if(Deque.empty()) cout << 1 << "\n";
      else cout << 0 << endl;
    }
    else if(inputOrder == "front"){
      if(Deque.empty()) cout << -1 << "\n";
      else cout << Deque.front() << endl;
    }
    else if(inputOrder == "back"){
      if(Deque.empty()) cout << -1 << "\n";
      else cout << Deque.back() << endl;
    }


  }
}