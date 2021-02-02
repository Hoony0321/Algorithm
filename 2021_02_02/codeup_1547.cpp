#include <stdio.h>

int n;

//coudeup_1547 : [기초-함수작성] 함수로 prime/composite 판별하기

// 이 부분에 들어가야 될 코드를 작성하여 제출
bool prime(int n){
  for(int i = 2; i <= n/2; i++){
    if(n % i == 0) return false;
  }

  return true;
}

int main()
{
  scanf("%d", &n);
  if(prime(n)) printf("prime");
  else printf("composite");
  return 0;
}