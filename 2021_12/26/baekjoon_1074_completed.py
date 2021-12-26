#baekjoon_1074_Z
#찾고자 하는 좌표가 어느 사분면에 속하는 지 찾으면 됨
#점점 사분면을 좁혀가서 결국 2 * 2 사각형 크기에서 사분면 어디 속하는 지까지 가면 됨.
#1사분면에 있을 경우 - skip 0 / 2사분면에 있을 경우 skip 1 / 3사분면에 있을 경우 skip 2 이런 식으로

#=== import module ===#

#=== variable declare ===#
answer = 0;
#=== Function define ===#
def Z(y,x,size,skip):
  global r,c,answer;

  

  if(r < y + size and r >= y and c < x + size and c >= x):
    answer += size * size * skip;
    nSize = size//2;

    if(r == y and c == x): return;

    Z(y,x, nSize,0); #1사분면
    Z(y,x + nSize, nSize, 1 ); #2사분면
    Z(y + nSize, x, nSize, 2); #3사분면
    Z(y + nSize, x + nSize, nSize, 3); #4사분면
  


#=== main function ===#
N, r, c = map(int,input().split());

Z(0,0,(1<<N),0);
print(answer);