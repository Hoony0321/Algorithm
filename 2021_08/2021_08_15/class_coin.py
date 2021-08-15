#코인 가상화폐 앱을 만들 때 코인 클래스 만들어보기

class currency:

  #가상화폐 정보를 가져오는 함수
  def __load(self,currencyName):
    close = 50
  
  #__init__ 초기화 함수
  def __init__(self,currencyName):
    self.__currencyName = currencyName
    self.__load(currencyName)

    self.__close = None

  #property 정의
  @property
  def close(self):
    return self.__close

  #setter 정의
  @close.setter
  def close(self,close):
    self.__close = close

  def __repr__(self):
    return "{} 의 정보\n".format(self.__currencyName) + "종가 : {}".format(self.__close)



XRP = currency("XRP")
print(XRP)
    
  