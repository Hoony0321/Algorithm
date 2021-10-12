#baekjoon_1032_명령프롬프트

def FindCommand(results):
  length = len(results[0]);
  array_size = len(results);
  common_part = [];
  
  for index in range(length):
    isCommonPart = True;
    criteria = results[0][index];
    for i in range(1,array_size):
      if criteria != results[i][index]:
        isCommonPart = False;
        break;
    if isCommonPart: common_part.append(criteria);
    else: common_part.append('?');
  
  return common_part;


testCase = int(input());
results = [[] for i in range(testCase)];

for test in range(testCase):
  result = input();
  for i in range(len(result)):
    results[test].append(result[i]);

command = FindCommand(results);
for char in command:
  print(char,end='');
