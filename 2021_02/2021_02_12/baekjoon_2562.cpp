#include<stdio.h>



int main(){
  int array[9] = {0};

  int max = 1;
  int index;
  for(int i = 0; i < 9; i++){
    scanf("%d" , &array[i]);
    if(max < array[i]){
      max = array[i];
      index = i+1;
    }
  }

  printf("%d\n%d\n",max,index);
}