#baekjoon_1546 평균
num_subjects = int(input());

score_list = list(map(int,input().split()));

max_score = max(score_list);

for i in range(num_subjects):
  score_list[i] = score_list[i]/max_score*100;

sum_score = sum(score_list);
average = sum_score/num_subjects;

print(average);



 