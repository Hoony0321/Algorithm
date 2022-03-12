#=== import module ===#
from collections import deque
#=== variable declare ===#

#=== Function define ===#
def solution(numbers,target):
  arr = deque()
  arr.append(0);
  for num in numbers:
    for i in range(len(arr)):
      elem = arr.popleft();
      arr.append(elem + num);
      arr.append(elem - num);

  return arr.count(target);