#baekjoon_1037_약수 (수학문제)

#=== import module ===#

#=== Function define ===#

#=== variable declare ===#

#=== main function ===#
num_aliquot = int(input());
aliquots = list(map(int,input().split()));

aliquots.sort();
result = 0;
if num_aliquot == 1:
  result = aliquots[0] ** 2;
else:
  result = aliquots[0] * aliquots[num_aliquot-1];

print(result);