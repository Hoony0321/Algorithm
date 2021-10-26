#baekjoon_3052 나머지
numList = [];

for i in range(10):
  inputVal = int(input());
  numList.append(inputVal);

for i in range(10):
  numList[i] %= 42;

numList = set(numList);

print(len(numList));