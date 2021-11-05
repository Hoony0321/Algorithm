#baekjoon_1043_거짓말

#사람 수, 파티 수 입력
peoples, parties = map(int,(input().split()));

#아는 사람 수, 아는 사람 번호 입력
tmpList = list(map(int,input().split()));
num_knowing = tmpList[0];
knowingPeoples = tmpList[1:];


graph = [[0 for i in range(peoples)+1] for j in range(peoples)+1]
partyMembers = [];

for party in range(parties):
  #파티에 오는 사람 수, 파티에 오는 사람 번호 입력
  tmpList = list(map(int,input().split()));
  num_coming = tmpList[0];
  comingPeople = tmpList[1:];
  
  #partyInfo에 추가
  partyMembers.append(comingPeople);
  
  #graph에 추가
  for i in range(len(comingPeople)):
    for j in range(len(comingPeople)):
      graph[i+1][j+1] += 1;
      graph[j+1][i+1] += 1;

#처음 newKnowingPeoples설정
newKnowingPeoples = [];

for people in knowingPeoples:
  for i in range(peoples):
    if graph[people-1][i] != 0: 
      if i+1 not in knowingPeoples:
        newKnowingPeoples.append(i+1);

knowingPeoples += newKnowingPeoples;

#반복
while(len(newKnowingPeoples) != 0):
  tempList = [];

  for people in newKnowingPeoples:
    for i in range(peoples):
      if graph[people-1][i] != 0:
        if i+1 not in knowingPeoples:
          tempList.append(i+1);
  
  newKnowingPeoples = tempList;
  knowingPeoples += newKnowingPeoples;

availableParty = 0;

for party in partyMembers:
  print("knowing member : {}".format(knowingPeoples));
  isAvailable = True;
  for member in party:
    if member in knowingPeoples:
      isAvailable = False;
      break;
  
  if isAvailable:
    availableParty += 1;

print(availableParty);
  


  





