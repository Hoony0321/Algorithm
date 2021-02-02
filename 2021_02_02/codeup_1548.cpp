#include <stdio.h>

int n;

//codeup_1548 : [기초-함수작성] 함수로 학점 리턴하기

// 이 부분에 들어가야 될 코드를 작성하여 제출

char grade(int n){
  char grade_char = ' ';
  if(n >= 90){
    grade_char = 'A';
  }
  else if(n >=80){
    grade_char = 'B';
  }
  else if(n >=70){
    grade_char = 'C';
  }
  else if(n >=60){
    grade_char = 'D';
  }
  else{
    grade_char = 'F';
  }

  return grade_char;
}

int main()
{
  scanf("%d", &n);
  printf("%c", grade(n));
  return 0;
}