#정규표현식 실전 연습문제
import re

#1. 날짜 표현 탐지하기 - DD/MM/YYYY형태 탐지하기

#p = re.compile("([0-2]\d|3[01])/(0[1-9]|1[0-2])/([12]\d{3})");
# p = re.compile("""
# ([0-2]\d|3[01]) #DD표현
# /(0[1-9]|1[0-2]) #MM포현
# /([12]\d{3}) ##YYYY포현
# """, re.X);
# inputData = input("날짜를 DD/MM/YYYY 형태로 입력해주세요 : ");
# m = p.match(inputData);

# if m:
#   print(m.group());
# else:
#   print("잘못된 입력입니다.");

#2.비밀번호 탐지기
#최소 길이 8자, 대문자 소문자 포함, 적어도 하나의 숫자 포함

inputData = input("비밀번호를 입력해주세요 : ");
isVaild = True;

 #최소 길이 8자 확인
p = re.compile(".{8,}");
m = p.match(inputData);
if not m : isVaild = False;

#대문자 포함 확인
p = re.compile("[A-Z]");
m = p.search(inputData);
if not m : isVaild = False;

#소문자 포함 확인
p = re.compile("[a-z]");
m = p.search(inputData);
if not m : isVaild = False;

#숫자 포함 확인
p = re.compile("\d");
m = p.search(inputData);
if not m : isVaild = False;

if isVaild:
  print("유효한 비밀번호입니다.")
else:
  print("유효하지 않은 비밀번호입니다.")



