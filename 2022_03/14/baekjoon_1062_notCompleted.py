#baekjoon_1062_가르침
import copy
import itertools

N,K = map(int,input().split());
alphaList = set();
choiceAlpha = set(['a','c','i','n','t']);
wordInfo = []
for _ in range(N):
    word = list(set(input()));

    tmpList = set();
    for elem in word:
        if elem in choiceAlpha: continue;
        else:
            tmpList.add(elem); alphaList.add(elem);

    wordInfo.append(tmpList);
if K < 5: #불가능한 경우
    print(0); exit(0);

choiceList = list(itertools.combinations(alphaList,K -5));

max_result = 0;
for choice in choiceList:
    available = 0;
    choiceAlpha = set(choice);

    for word in wordInfo:
        #print("choiceAlpah : {}, word : {}".format(choiceAlpha,word));

        if word.issubset(choiceAlpha):
            available += 1;

    max_result = max(max_result,available);

print(max_result)