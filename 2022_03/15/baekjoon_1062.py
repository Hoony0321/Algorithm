#baekjoon_1062_가르침
import copy
import itertools

N,K = map(int,input().split());
alphaList = set(); #단어에 나오는 알파벳들 저장 집합(중복 방지)
basicAlpha = ['a','c','i','n','t']; #기본 알파벳들(필수)
wordList = []; #각 단어마다 필요한 알파벳들 저장
for _ in range(N):
    word = list(set(input()));

    tmpList = set();
    for elem in word:
        if elem in basicAlpha: continue; #기본 알파벳에 포함되면 패스.
        else:
            tmpList.add(elem); alphaList.add(elem);

    wordList.append(tmpList); #wordList 안에 각 단어의 필요한 알파벳들이 집합 형태로 들어감.
if K < 5: #불가능한 경우
    print(0); exit(0);

if K-5 > len(alphaList):
    choiceList = list(itertools.combinations(alphaList, len(alphaList)));
else:
    choiceList = list(itertools.combinations(alphaList, K - 5));


max_result = 0;
for choice in choiceList:
    available = 0;
    choice = set(choice);

    for word in wordList:
        #print("choiceAlpah : {}, word : {}".format(choiceAlpha,word));

        if word.issubset(choice):
            available += 1;

    max_result = max(max_result,available);

print(max_result)