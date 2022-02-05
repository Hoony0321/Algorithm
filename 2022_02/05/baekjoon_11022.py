#baekjoon_11022_A+B - 8

t = int(input());

for i in range(1,t+1):
  a,b = map(int,input().split());
  print("Case #{}: {} + {} = {}".format(i,a,b,a+b));