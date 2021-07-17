//21967 - 제5회 천하제일 코딩대회 예선  - 세워라 반석 위에
#include<iostream>
#include<vector>

using namespace std;

struct point{
  int cnt;
  int min_element;
  int max_element;
  int startPoint;
  point(int _cnt, int _min_element, int _max_element, int _startPoint){
    cnt = _cnt; min_element = _min_element; max_element = _max_element; startPoint = _startPoint;
  };

  point(){
    cnt = 1; min_element = 10; max_element = 1; startPoint = 1;
  };
};

int N;
int numList[1000001];
struct point dp[1000001];




int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);
  cin >> N;
  
  for(int i = 1; i <= N; i++){
    cin >> numList[i];
  }

  if(N == 1){cout << 1 << "\n"; exit(0);}


  dp[1] = (point(1,numList[1],numList[1],1));  //처음 원소

  for(int i = 2; i <= N; i++){
    if(abs(dp[i-1].min_element - numList[i]) > 2 || abs(dp[i-1].max_element - numList[i]) > 2){
      //차이가 2 초과 => 반석 깨짐
      for(int startPoint = dp[i-1].startPoint + 1; startPoint < i; startPoint++){
        int min = 10;
        int max = 1;
        for(int s = startPoint; s < i; s++){
          min = min > numList[s] ? numList[s] : min;
          max = max < numList[s] ? numList[s] : max;
        }
        if(max - min <= 2){
          //반석 성공
          dp[i] = point(i - startPoint + 1, min, max, startPoint);
          break;
        }
      }
    }
    else{
      //차이 2 이하 => 반석 유지
      point newPoint = dp[i-1];
      newPoint.cnt += 1;
      if(dp[i-1].min_element > numList[i]){ //min_element 갱신
        newPoint.min_element = numList[i];
      }
      else if(dp[i-1].max_element < numList[i]){
        newPoint.max_element = numList[i];
      }
      dp[i] = newPoint;
    }
  }

  int max = 1;
  for(int i = 1; i <= N; i++){
    if(max < dp[i].cnt) max = dp[i].cnt;
  }
  cout << max << "\n";


}