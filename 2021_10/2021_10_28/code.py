#baekjoon_16637_괄호추가하기

def calculate(formula):
  result = int(formula[0]); # 첫 수는 무조건 정수

  operation = None;
  isinbracket = False;
  subResult = 0;
  subOperation = None;
  for i in range(1,len(formula)):
    if not formula[i].isdigit(): # +,-,*,() 일 경우
      operation = formula[i];
    else:
      if operation = '+':
        result += int(formula[i]);
      elif operation = '-':
        result -= int(formula[i]);
      elif operation = '*':
        result *= int(formula[i]);
      elif operation = '(':
        isinbracket = True;
      elif operation = ')':



length = int(input());

formula = input();

for item in formula:
  print(item.isdigit());

#max_result = calculate(formula);