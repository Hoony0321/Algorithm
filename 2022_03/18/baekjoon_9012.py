#baekjoon_9012_괄호

T = int(input());

for _ in range(T):
    inputData = list(input());

    if len(inputData) == 1:
        print("NO"); continue;


    countF = 0;
    possible = True;
    for data in inputData:
        if data == '(':
            countF += 1;
        else: #입력된 문자가 ( 인 경우
            if countF == 0:
                possible = False; break;
            else:
                countF -= 1;

    if possible and countF == 0:
        print("YES");
    else:
        print("NO");


