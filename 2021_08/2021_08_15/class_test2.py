#https://mungto.tistory.com/106 44차시 연습문제 1

#문제 내용
# name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진
# GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를
# 다음과 같이 문자열로 출력하는 코드를 작성하십시오.

class Student:

  def __init__(self,name):
    self.__name = name
  
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self,name):
    self.__name = name

  def __repr__(self):
    return "이름 : {}".format(self.__name)


class GraduateStudent(Student):

  def __init__(self,name,major):
    super().__init__(name)
    self.__major = major

  @property
  def major(self):
    self.__major

  @major.setter
  def major(self,major):
    self.__major = major

  def __repr__(self):
    return "전공 : {}\n".format(self.__major) + super().__repr__()


print("="*5 + " Student " + "="*5)
stu = Student("대훈")
print(stu)

print("="*5 + " GraduateStudent " + "="*5)
graduateStu = GraduateStudent("대훈", "컴공")
print(graduateStu)