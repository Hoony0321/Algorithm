#baekjoon_11653_소인수분해
N = int(input());

factor = 2;
while(N > 1):
  if N % factor == 0:
    print(factor);
    N /= factor;
    factor = 2;
  else:
    factor += 1;