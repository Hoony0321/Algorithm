#programmers_체육복

#=== import module ===#

#=== variable declare ===#

#=== Function define ===#
def solution(n, lost, reserve):
  lost.sort();
  reserve.sort();
  #lost,reserve에 둘 다 속한 index 삭제
  deleteArr = [];
  for elem in lost:
    if elem in reserve:
      deleteArr.append(elem);

  for elem in deleteArr:
    lost.remove(elem);
    reserve.remove(elem);

  answer = n - len(lost);
  for elem in reserve:
    prev = elem - 1; next = elem + 1;
    if prev > 0:
      if prev in lost:
        lost.remove(prev);
        answer += 1;
        continue;

    if next <= n:
      if next in lost:
        lost.remove(next);
        answer += 1;

  return answer;
        
    
#=== main function ===#
print(solution(3,[3],[1]));


