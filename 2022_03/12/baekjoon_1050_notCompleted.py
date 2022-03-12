# baekjoon_1050_물약

# === import module ===#

# === variable declare ===#
N = None; #재료 개수
M = None; #물약식 개수
ingredient_info = {}; #재료 정보
medicine_info = {}; #물약식 정보

availableItem = (); #현재 사용가능한 재료/물약

# === Function define ===#

# === main function ===#
N , M = map(int,input().split());

#시장에서 파는 재료 정보 입력
for _ in range(N):
    name, cost = input().split();
    ingredient_info[name] = int(cost);
    availableItem.add(name); #재료는 당장 사용가능하므로 추가.

#물약식 정보 입력
for _ in range(M):
    medicine , recipe = input().split("=");
    recipe = list(recipe.split("+"));

    medicine_info[medicine] = [];
    for ingredient in recipe:
        dose = (ingredient[1:], ingredient[0]);
        medicine_info[medicine].append(dose);

ChangeValue = 1;
while(ChangeValue > 0): #변한 게 없으면 종료

    for medicine in medicine_info.keys():
        if medicine in availableItem: #이미 만든
            pass;









