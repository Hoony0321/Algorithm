#programmers_단어 변환

#=== import module ===#
from collections import deque
#=== variable declare ===#

#=== Function define ===#
def solution(begin, target, words):
  if target not in words: return 0; #불가능한 경우
    
  queue = deque();
  queue.append([begin,0]); #current, visited
  level = 0;
  succeed = False;
  while queue and not succeed:
    level += 1;
    for i in range(len(queue)):
      current,visited = queue.popleft();
      for idx in range(len(words)):
        if visited & (1 << idx) != 0: continue; #이미 방문한 단어
        nextWord = words[idx];
        diff = 0;
        for i in range(len(current)):
          if current[i] != nextWord[i]: diff += 1;
        if diff != 1: continue; #다른 것이 2개 이상이라서 한번에 변환 불가능
        if nextWord == target: #성공 조건
          succeed = True; break;
        queue.append([nextWord,visited | (1 << idx)]);

  if succeed: return level;
  else: return 0;
              
#=== main function ===#
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]));


