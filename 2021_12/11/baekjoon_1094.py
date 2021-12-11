#baekjoon_1094_막대기

#=== import module ===#

#=== variable declare ===#

#=== Function define ===#

#=== main function ===#
X = int(input());

cnt = 0;
for i in range(8):
  if X & (1 << i) != 0 : cnt += 1;

print(cnt);

