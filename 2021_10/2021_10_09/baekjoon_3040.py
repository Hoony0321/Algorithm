#baekjoon_3040_백설공주와일곱난쟁이

heights = [];

for i in range(9):
  inputVal = int(input());
  heights.append(inputVal);

totalHeight = 0
for item in heights:
  totalHeight = totalHeight + item;

extraHeight = totalHeight - 100;
extraIndex = []
for i in range(8):
  temp_height = extraHeight - heights[i];
  find = False;
  for j in range(i+1,9):
    if temp_height == heights[j]:
      extraIndex.append(i);
      extraIndex.append(j);
      find = True;
      break;
  
  if find: break;



if i > j :
  temp = i;
  i = j;
  j = i;

heights.pop(j);
heights.pop(i);
for i in range(7):
  print(heights[i]);