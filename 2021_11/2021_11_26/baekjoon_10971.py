#baekjoon_10971_외판원 순회 2
#도시가 10개 이하 -> 그냥 완전탐색으로 가능

#=== import module ===#
import copy

#=== Function define ===#
def TSP(current, visited, cost):
  global result, city, w;
  #visited = copy.deepcopy(_visited);
  if 0 not in visited: #모든 도시를 방문한 경우
    if w[current][0] != 0:
      cost += w[current][0];
      result.append(cost);
  else: #모든 도시를 아직 방문하지 않은 경우
    for _city in range(city):
      if w[current][_city] == 0: continue; #현재 도시에서 갈 수 없는 도시
      if visited[_city] == 1: continue; #이미 방문한 도시인 경우
      visited[_city] = 1; #방문 표시
      TSP(_city,visited,cost + w[current][_city]);
      visited[_city] = 0; #방문 원상복귀



#=== variable declare ===#
city = 0; w = []; result = [];
#=== main function ===#
city = int(input());

for _ in range(city):
  w.append(list(map(int,input().split())));

visited = [0 for i in range(city)];
visited[0] = 1;

TSP(0,visited,0);

print(min(result));