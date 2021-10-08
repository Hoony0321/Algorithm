#baekjoon_2309_일곱 난쟁이

heights = [];

for i in range(9):
  inputVal = int(input());
  heights.append(inputVal);

totalHeight = 0
for item in heights:
  totalHeight = totalHeight + item;

extraHeight = totalHeight - 100;
extraIndex = []
for i in range(9):
  sumHeight = heights[i];
  find = False;
  for j in range(8):
    j = i+1;
    if j > 8: break;
    sumHeight = sumHeight + heights[j];
    if sumHeight == extraHeight:
      extraIndex.append(i);
      extraIndex.append(j);
      find = True;
      break;
    sumHeight = sumHeight - heights[j];
  
  if find: break;


if i > j :
  temp = i;
  i = j;
  j = i;

heights.pop(j);
heights.pop(i);
heights.sort()
print(heights);