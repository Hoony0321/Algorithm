#baekjoon_1092_배

# === import module ===#

# === variable declare ===#
N = None; #크레인 개수
M = None; #박스 개수

WeightBound = []; #크레인 무게 제한 배열
BoxWeight = []; #박스 무게 정보
# === Function define ===#

# === main function ===#
N = int(input());
WeightBound = list(map(int,input().split()));
M = int(input());
BoxWeight = list(map(int,input().split()));

WeightBound.sort(reverse=True);
BoxWeight.sort(reverse=True);

action = 0;
while(len(BoxWeight) > 0):

    #제일 무거운 박스를 옮길 수 있는 크레인 없음.
    if BoxWeight[0] > WeightBound[0]:
        break;

    # 크레인으로 박스 옮기기
    for selected in range(N):
        for idx in range(len(BoxWeight)):
            if WeightBound[selected] >= BoxWeight[idx]:
                del BoxWeight[idx];
                break;

    action += 1;

if len(BoxWeight) != 0:
    print(-1);
else:
    print(action);





