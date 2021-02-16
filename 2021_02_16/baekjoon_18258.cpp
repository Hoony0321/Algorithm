#include<iostream>
#include<queue>
#include<string>

using namespace std;


constexpr unsigned int HashCode(const char* str)
{
    return str[0] ? static_cast<unsigned int>(str[0]) + 0xEDB8832Full * HashCode(str + 1) : 8603;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int num;
  string inputOrder;
  cin >> num;

  queue<int> queue;

  for(int i =0; i < num; i++){
    cin >> inputOrder;
    switch(HashCode(inputOrder.c_str())){
      case HashCode("push"):
        int X;
        cin >> X;
        queue.push(X);
        break;
      case HashCode("pop"):
        if(queue.empty()) cout << -1 << "\n";
        else{cout << queue.front() << "\n"; queue.pop();} 
        break;
      case HashCode("size"):
        cout << queue.size() << "\n";
        break;
      case HashCode("empty"):
        if(queue.empty()) cout << 1 << "\n";
        else cout << 0 << "\n";
        break;
      case HashCode("front"):
        if(!queue.empty()) cout << queue.front() << "\n";
        else cout << -1 << "\n";
        break;
      case HashCode("back"):
        if(!queue.empty()) cout << queue.back() << "\n";
        else cout << -1 << "\n";
        break;
    }
  }
}