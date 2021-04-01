#include<stdio.h>

int main(){
  int n;
  scanf("%d", &n);
  int* array = new int[n];
  for(int i = 0; i < n; i++){
    scanf("%d",&array[i]);
  }

  int min = 1000000;
  int max = -1000000;

  for(int i = 0; i < n; i++){
    if(min > array[i]) min = array[i];
    if(max < array[i]) max = array[i];
  }

  printf("%d %d" , min, max);

  delete[] array;
}