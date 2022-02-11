#파이썬 정규형 연습
import re

def RepresentObject(obj):
  if obj:
    print("Match found : ", obj.group()); #group이란? -> 정규 표현식을 여러가지 그룹으로 나눌 수 있음. 이때 group(number) 매개변수 number에 따라 해당 그룹만 표현되게 할 수 있음.             예를 들어 group(1)이라고 하면 첫번째 그룹에 해당되는 객체들만 반환되게 됨.
    
  else:
    print("Not match");

#match - 문자열의 처음부터 정규식과 매치되는 지 조사 return -> match 객체 or None
p = re.compile('[a-z]+') #소문자 알파벳이 적어도 하나 이상

m = p.match("pythoN");
print(m); #match 객체 리턴

_m = p.match("3 python");
print(_m); #None 객체 리턴

p = re.compile('[a-z]+\d') #소문자 알파벳이 적어도 하나 이상 + 숫자 한 개
m = p.match("python");
RepresentObject(m); # Not match

p = re.compile('([a-z]+)(\d)') #소문자 알파벳이 적어도 하나 이상 + 숫자 한 개
m = p.match("python3");
RepresentObject(m); # match

#search - 문자열의 처음부터가 아닌 계속 검색하여 해당하는 객체있으면 반환.
p = re.compile('[a-z]+') #소문자 알파벳이 적어도 하나 이상
m = p.search("pythoN");
RepresentObject(m);

m = p.search("pythoN123pyth334dvs");
RepresentObject(m);

#findall - search 함수를 계속 for문 돌려 결과를 리스트 형태로 반환하는 것.
p = re.compile('[a-z]+') #소문자 알파벳이 적어도 하나 이상
m = p.findall("pythoN");
print(m);

m = p.findall("pythoN123pyth334dvs");
print(m);

#finditer - findall결과를 반복가능한 iteration 객체로 반환하는 거.
p = re.compile('[a-z]+') #소문자 알파벳이 적어도 하나 이상
m = p.finditer("pythoN123pyth334dvs");

for item in m:
  RepresentObject(item);

#start, end, span 함수 -> 각 찾은 객체의 시작 index, 끝 index 등을 알려주는 함수다.
#이때 match는 항상 처음부터 확인하므로 start 반환 값은 항상 0이다. search는 다름.
#이때 match객체의 매소드이므로 findall에선 사용하긴 힘들다.

p = re.compile('[a-z]+') #소문자 알파벳이 적어도 하나 이상
m = p.match("pythoN123pyth334dvs");
print(m.span());

m = p.search("pythoN123pyth334dvs");
print(m.span());

# m = p.findall("pythoN123pyth334dvs");
# for item in m:
#   print(item.span());
# ==> findall은 list 안의 string 형태의 객체를 반환하므로 오류 발생

m = p.finditer("pythoN123pyth334dvs");
for item in m:
  print(item.span());

#축약된 방법으로 사용하기 => re.method(정규식, string 객체)
m = re.match("[a-z]+", "pythoN123pyth334dvs");
RepresentObject(m);

#compile 옵션 - 가로 안에 축양형 사용해도 됨.
#DOTALL(S) - '.'이 \n 포함해서 카운팅 가능
p = re.compile("a.b", re.DOTALL); 
m = p.match("a\nb");
print(m); #\n 인식함.

#IGNORECASE(I) - 대소문자 구분 X
p = re.compile("[a-z]+", re.IGNORECASE);
m1 = p.match("python");
m2 = p.match("PYTHON");
print(m1);
print(m2);

#MULTILINE(M) - 여러 줄 가능
p = re.compile("^python \w+", re.M);
data = """python one
life is too short
python two
you need python
python three"""
m = p.findall(data);
print(m);

#VERBOSE(X) - 정규식을 보게 편하게 만들어 준다.
p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);');

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
#이때 compile 앞에 있는 r은 뒤의 string이 raw string임을 의미한다.
p = re.compile('\\\\nclass') 
p = re.compile(r'\\nclass')  #둘 다 같은 결과를 보여줌.
data = '\\nclass';
print(data);
print(p.findall(data));