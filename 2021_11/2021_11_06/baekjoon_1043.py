#baekjoon_1043_거짓말

#사람 수, 파티 수 입력
peoples, parties = map(int,(input().split()));

#아는 사람 수, 아는 사람 번호 입력
tmpList = list(map(int,input().split()));
num_knowing = tmpList[0];
knowingPeoples = tmpList[1:];


graph = [[0 for i in range(peoples+1)] for j in range(peoples+1)]
partyMembers = [];

for party in range(parties):
  #파티에 오는 사람 수, 파티에 오는 사람 번호 입력
  tmpList = list(map(int,input().split()));
  num_coming = tmpList[0];
  comingPeople = tmpList[1:];
  
  #partyInfo에 추가
  partyMembers.append(comingPeople);
  
  #graph에 추가
  for people in comingPeople:
    for other in comingPeople:
      graph[people][other] +=1;
      graph[other][people] += 1;
  

#처음 newKnowingPeoples설정
newKnowingPeoples = [];

for people in knowingPeoples:
  for i in range(1,peoples+1):
    if graph[people][i] != 0: 
      if i not in knowingPeoples:
        newKnowingPeoples.append(i);

knowingPeoples += newKnowingPeoples;

#반복
while(len(newKnowingPeoples) != 0):
  tempList = [];

  for people in newKnowingPeoples:
    for i in range(1,peoples+1):
      if graph[people][i] != 0:
        if i not in knowingPeoples:
          tempList.append(i);
  
  newKnowingPeoples = tempList;
  knowingPeoples += newKnowingPeoples;

availableParty = 0;

for party in partyMembers:
  isAvailable = True;
  for member in party:
    if member in knowingPeoples:
      isAvailable = False;
      break;
  
  if isAvailable:
    availableParty += 1;

print(availableParty);
  


  





