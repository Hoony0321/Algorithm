#codeup 6079 : [기초-종합] 언제까지 더해야 할까?(py)

limit = int(input())
sum = 0
delta = 0
while(sum < limit):
  delta += 1
  sum += delta
  

print(delta)