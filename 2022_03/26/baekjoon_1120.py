#baekjoon_1120_문자열
N = int(input());
strList = [input() for _ in range(N)];

sortList = {};

max_len = 0;
for word in strList:
    length = len(word);
    max_len = max(max_len,length);
    if length in sortList.keys():
        if word in sortList[length]: continue;
        sortList[length].append(word);
    else:
        sortList[length] = [word];


for i in range(1, max_len+1):
    if i in sortList.keys():
        sortList[i].sort();
        for elem in sortList[i]:
            print(elem);

