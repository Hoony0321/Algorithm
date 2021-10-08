#baekjoon_2609_최대공약수와 최소공배수
numA, numB = input().split();

numA = int(numA);
numB = int(numB);

def ReturnLCM(numA, numB):
  gcd = ReturnGCD(numA, numB);
  lcm = numA * numB / gcd;
  return int(lcm);

def ReturnGCD(numA, numB):
  while(numB != 0):
    numC  = numA % numB;
    numA = numB;
    numB = numC;
  
  return numA;

if numA < numB:
  temp = numA;
  numA = numB;
  numB = temp;

print(ReturnGCD(numA,numB));
print(ReturnLCM(numA,numB));