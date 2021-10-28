#baekjoon_16637_괄호추가하기

def operationProcess(operation,num1,num2):
    if operation == '+':
      num1 += num2;
    elif operation == '-':
      num1 -= num2;
    elif operation == '*':
      num1 *= num2;
    return num1;

def calculate(formula):
  result = int(formula[0]); # 첫 수는 무조건 정수

  operation = None;
  isinbracket = False;
  subResult = 0;
  subOperation = None;
  for i in range(1,len(formula)):
    if isinbracket: #괄호 O
      if not formula[i].isdigit(): #,+,-,*,() 일 경우
        subOperation = formula[i];
        if subOperation == ')':
          result = operationProcess(operation,result,subResult);
          subOperation = None;
          isinbracket = False;
      else: # 숫자일 경우
        if subOperation is None:
          subResult = int(formula[i]);
        else:
          subResult = operationProcess(subOperation,subResult,int(formula[i]));
    else: #괄호 X
      if not formula[i].isdigit(): # +,-,*,() 일 경우
        if formula[i] == '(':
          isinbracket = True;
        else:
          operation = formula[i];
      else: #숫자일 경우
        result = operationProcess(operation,result,int(formula[i]));
  return result;

def FindFormula(starIdx, formula):
  global maxResult;

  if len(formula)-1 - starIdx < 2: #더 이상 bracket 들갈 자리 없음
    calc_result = calculate(formula);
    if maxResult < calc_result:
      maxResult = calc_result;
      print(formula);
  else: #bracket 더 가능함.
    #bracket 추가 X
    FindFormula(starIdx+3,formula);
    #bracket 추가
    formula.insert(starIdx,'(');
    formula.insert(starIdx+4,')');
    FindFormula(starIdx+6,formula);
    




length = int(input());

formula = list(input());

maxResult = calculate(formula); #괄호 없는 결과값

FindFormula(2,formula);

print(maxResult);


