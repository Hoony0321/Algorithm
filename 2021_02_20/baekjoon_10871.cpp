#include<cstdio>

int main(){
  int N,X;
  scanf("%d %d",&N,&X);

  int* numList = new int[N];

  for(int i = 0; i <  N; i++){
    scanf("%d", &numList[i]);
  }

  for(int i = 0; i < N; i++){
    if(numList[i] < X) printf("%d ",numList[i]);
  }

  delete[] numList;
}