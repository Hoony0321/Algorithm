#include<iostream>

using namespace std;

int list[52][52][52];

int DP(int a, int b, int c){
  if(a <= 0 || b <= 0 || c <= 0) return 1;
  
  if(list[a][b][c] != 0) return list[a][b][c]; //배열에 값 존재 시 바로  출력

  if(a > 20 || b > 20 || c > 20){
    list[a][b][c] = DP(20,20,20);
    return list[a][b][c];
  } 
  
  if(a < b && b < c){
    list[a][b][c] = DP(a,b,c-1) + DP(a,b-1,c-1) - DP(a,b-1,c);
    return list[a][b][c];
  }
  else{
    list[a][b][c] = DP(a-1,b,c) + DP(a-1,b-1,c) + DP(a-1,b,c-1) - DP(a-1,b-1,c-1);
    return list[a][b][c];
  }
}

int main(){

  int a,b,c;

  while(true){
    cin >> a >> b >> c;
    if(a == -1 && b == -1 && c == -1){
      break;
    }

    printf("w(%d, %d, %d) = %d\n", a,b,c,DP(a,b,c));

  }
}