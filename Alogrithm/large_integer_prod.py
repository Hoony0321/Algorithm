#큰 정수 곱셈 알고리즘
import math
from math import pow


def prod(u,v):
    global threshold;
    n = max(len(str(u)), len(str(v))); #u,v의 최대 자릿수

    if(u == 0 or v == 0): #둘 중 하나라도 0이 있으면 곱셈 = 0
        return 0;
    elif(n <= threshold): #임계값
        return u * v;
    else:
        m = math.floor(n/2);
        x = u // pow(10,m);
        w = v // pow(10,m);
        y = u % pow(10,m);
        z = v % pow(10,m);
        x,y,z,w = map(int,[x,y,z,w]);
        return prod(x,w) * pow(10,2*m) + (prod(x,z) + prod(w,y)) * pow(10,m) + prod(y,z);

threshold = 2; #threshold = 2로 설정

u,v = map(int,input().split());

print(prod(u,v));