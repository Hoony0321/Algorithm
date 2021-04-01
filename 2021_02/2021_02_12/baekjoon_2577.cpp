#include<stdio.h>
#include<cmath>

int main(){
  int A,B,C;
  int array[10] = {0};
  scanf("%d %d %d",&A,&B,&C);

  int multiple = A * B * C;
  while(multiple > 0){
    array[multiple%10]++;
    multiple /= 10;
  }
  for(int i = 0; i <= 9; i++){
    printf("%d\n", array[i]);
  }
}