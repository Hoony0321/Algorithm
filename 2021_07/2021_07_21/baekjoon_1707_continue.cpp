//baekjoon_1707
#include<iostream>
#include<deque>
#include<vector>
using namespace std;

struct point{
  int y; int x;
  point(int _y, int _x){y = _y; x = _x;};
};

int RED = 1;
int BLACK = -1;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int K; //testcase
  cin >> K;

  for(int testcase = 0 ; testcase < K; testcase++){
    int vertex,edge;
    cin >> vertex >> edge;

    vector<vector<int>> map(vertex+1,vector<int>(vertex+1,-1));
    for(int i = 0; i < edge; i++){
      int v1,v2;
      cin >> v1 >> v2;
      map[v1][v2] = 0; map[v2][v1] = 0;
    }

    
    bool isBipartite = true;
    for(int i = 1; i <= vertex; i++){
      if(!isBipartite) return;

      deque<int> bfsQueue;
      bfsQueue.push_back(i);
      while(!bfsQueue.empty()){
        int from = bfsQueue.front();
        bfsQueue.pop_front();

        for(int to = 1; to <= vertex; to++){
          if(map[from][to] != 0)
        }

      }
    }


  }
}