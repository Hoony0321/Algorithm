#baekjoon_1002_터렛

class Circle:
  def __init__(self,x,y,r):
    self.x = x;
    self.y = y;
    self.r = r;

def ReturnNum_ContactNum(circle1, circle2):
  a = circle1.x - circle2.x;
  b = circle1.y - circle2.y;

  distance = ((a**2) + (b**2))**(1/2);
  radius_diff = abs(circle1.r - circle2.r);
  radius_sum = circle1.r + circle2.r;

  if distance == 0: #원의 중심이 같을 때
    if circle1.r == circle2.r: return -1;
    else: return 0;
  else: #원의 중심이 다를 때
    if distance == radius_sum: return 1; #외접할 때
    elif distance == radius_diff: return 1; #내접할 때
    elif distance < radius_diff: return 0; #내부에 있으나 만나지 않음.
    elif distance < radius_sum: return 2; #두 점에서 만날 때
    elif distance > radius_sum: return 0; # 만나지 않을 때
    

  


testCase = int(input());
for case in range(testCase):
  arr = list(map(int,input().split()));

  circle1 = Circle(arr[0],arr[1],arr[2]);
  circle2 = Circle(arr[3],arr[4],arr[5]);

  num_contactPoint = ReturnNum_ContactNum(circle1,circle2);
  print(num_contactPoint);


