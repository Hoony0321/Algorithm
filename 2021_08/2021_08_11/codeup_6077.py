#codeup 6077 : [기초-종합] 짝수 합 구하기(설명)(py)

num = 2
sum = 0
target = int(input())
while(num <= target):
  sum += num
  num += 2
  

print(sum)