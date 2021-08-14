#https://mungto.tistory.com/106 44차시 연습문제 1

#문제 내용
# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

class Student:
  def __init__(self,kor,mat,eng):
    self.__kor = kor
    self.__mat = mat
    self.__eng = eng

  @property
  def kor(self):
    return self.__kor

  @kor.setter
  def kor(self, kor):
    self.__kor = kor

  @property
  def mat(self):
    return self.__mat

  @mat.setter
  def mat(self,mat):
    self.__mat == mat

  @property
  def eng(self):
    return self.__eng

  @eng.setter
  def eng(self, eng):
    self.__eng = eng

  def gettingAll(self):
    sum = self.__kor + self.__mat + self.__eng
    return sum

scores = input("국어,수학,영어 순으로 점수를 입력하시오 : ").split(' ')
stu = Student(int(scores[0]), int(scores[1]), int(scores[2]))

print("학생의 총점은" , stu.gettingAll() , "입니다.")
