a,b = map(int,input().split());

while(b > 0):
    print(a,b);
    tmp = b;
    b = a % b;
    a = tmp;

print(a);10