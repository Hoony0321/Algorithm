#programmers_완전탐색_모의고사

#=== import module ===#

#=== variable declare ===#
person_solve = [[],[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]];

#=== Function define ===#
def solve(answers,person):
  collect = 0;
  iter = 0;
  for answer in answers:
    if person_solve[person][iter] == answer:
      collect += 1;
    iter += 1;

    if iter == len(person_solve[person]): #끝 지점 도달-> 첫 지점으로 돌아감
      iter = 0;

  return collect;
    

    
    


def solution(answers):
  collects = [];
  collects.append(solve(answers,1));
  collects.append(solve(answers,2));
  collects.append(solve(answers,3));

  max_collects = -1;
  answer = [];
  for i in range(3):
    if max_collects < collects[i]:
      max_collects = collects[i];
      answer = [];
    elif max_collects == collects[i]:
      answer.append(i);
    else:
      pass;

  return answer;

  
#=== main function ===#

print(solution([1,2,3,4,5]));


