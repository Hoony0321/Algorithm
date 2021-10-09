#baekjoon_1004_어린왕자
class Planet:
  startPoint = [];
  endPoint = []
  def __init__(self,_x,_y,_r):
    self.y = _y;
    self.x = _x;
    self.r = _r;
    self.num_innerPoint = 0;
  
  def setPoint(self,_startPoint, _endPoint):
    Planet.startPoint = _startPoint;
    Planet.endPoint = _endPoint;

  def isPass(self):
    if isinnerPoint(self,self.startPoint): self.num_innerPoint+=1;
    if isinnerPoint(self,self.endPoint): self.num_innerPoint+=1;

    if self.num_innerPoint == 1:
      return True;
    else:
      return False;
  
def isinnerPoint(planet, point):
  tempNum = (point[0] - planet.x)**2 + (point[1] - planet.y)**2
  radius_square = planet.r**2;
  return tempNum - radius_square < 0

def solve(planets):
  num_passPlanet = 0;
  for item in planets:
    if item.isPass(): num_passPlanet+=1;
  
  return num_passPlanet;

  


testCase = int(input());

for count in range(testCase):
  Point = list(map(int,input().split()));
  startPoint = Point[0:2];
  endPoint = Point[2:4];
  num_planet = int(input());

  planets = [];
  for i in range(num_planet):
    basic_info = list(map(int,input().split()));
    new_planet = Planet(basic_info[0], basic_info[1], basic_info[2]);
    planets.append(new_planet);
  
  planets[0].setPoint(startPoint,endPoint);
  print(solve(planets));
    


