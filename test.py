def gcd(a, b):  # 최대공약수 구하기

    tmpB = 0;
    while (b != 0):
        tmpB = b;
        b = a % b;
        a = tmpB

    return tmpB;

print(gcd(84,32));