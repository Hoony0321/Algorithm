//codeup_4016 : 세 수의 최대공약수 구하기 - 정올1번문제집
#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int gcd(int a, int b){
    int tmp, n;
 
//a에 큰 값을 위치시키기 위한 조건문입니다.
    if(a<b){
        tmp = a;
        a = b;
        b = tmp;
    }
    
//유클리드 알고리즘 부분입니다.
//b가 0이 될때까지(a%b), 반복문을 돌게되고, b가 0인 순간의 a를 GCD로 판단하고 리턴합니다.
    while(b!=0){
        n = a%b;
        a = b;
        b = n;
    }
    return a;
}



int main(){
  vector<int> vec(3,0);
  for(int i = 0; i < 3; i++){
    cin >> vec[i];
  }
  
  sort(begin(vec), end(vec));
  
  int num = gcd(vec[0], vec[1]);


  if(num > vec[2]){
    cout << gcd(num,vec[2]) << endl;
  }
  else{
    cout << gcd(vec[2],num) << endl;
  }
}


