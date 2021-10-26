#baekjoon_4344 평균은 넘겠지

def solve():
  stu_record = list(map(int,input().split()));
  stu_num = stu_record[0];
  stu_scores = [];

  for i in range(1,stu_num+1):
    stu_scores.append(stu_record[i]);
  sum_score = sum(stu_scores);
  avarge = sum_score/stu_num;
  cnt = 0;
  for score in stu_scores:
    if score > avarge:
      cnt += 1;
  
  result = '{:.3f}%'.format(round(cnt/stu_num*100,3));
  print(result);

test_case = int(input());

for i in range(test_case):
  solve();