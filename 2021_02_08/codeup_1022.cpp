//codeup_1022 : [기초-입출력] 문장 1개 입력받아 그대로 출력하기(설명)


#include<stdio.h>
 
int main(void)
{
    char data[2001]="";
    fgets(data,2000,stdin);
    printf("%s", data);
 
    return 0;
}