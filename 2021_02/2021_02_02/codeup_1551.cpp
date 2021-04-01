#include <stdio.h>

int n, d[100010], k;

//codeup_1551 : [기초-함수작성] 함수로 원하는 값의 위치 리턴하기 1

// 이 부분에 들어가야 될 코드를 작성하여 제출
int f(int k){
  for(int i = 0; i <=n; i++){
    if(d[i] == k){
      return i;
    }
  }
  return -1;
}

int main()
{
  scanf("%d", &n);

  for(int i=1; i<=n; i++)
    scanf("%d", &d[i]);

  scanf("%d", &k);
  printf("%d\n", f(k));
}