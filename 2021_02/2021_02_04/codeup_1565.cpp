//codeup_1565 : [기초-함수작성] 함수로 최소공배수 리턴하기
#include <stdio.h>

int gcd(int p, int q){ if(p==0) return q; return gcd(q%p, p);}
long long int lcm(int a, int b){ return (long long int)a* (long long int)b / (long long int)gcd(a,b);}
// 이 부분에 들어가야 될 코드를 작성하여 제출
int main()
{
  int a, b;
  scanf("%d%d", &a, &b);
  printf("%lld\n", lcm(a, b));
}   

