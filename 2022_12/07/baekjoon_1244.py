# 문제 정보 baekjoon_1244 스위치 키고 끄기 (실버)

# === import module ===#

# === variable declare ===#
num_of_switches = 0
state_switches = []
num_of_std = 0
state_of_std = []

# === Function define ===#
def flatten(array): #2차원 배열 -> 1차원 배열
    result = []
    for row in array:
        for item in row:
            result.append(item)

    return result

def action(std):
    sex, num = std

    if sex == 1: #남학생
        for idx in range(num, num_of_switches+1, num):
            state_switches[idx-1] = int(not state_switches[idx-1])
    elif sex == 2: #여학생
        symmetry_step = 0
        while(True):
            left_idx = num - symmetry_step -1
            right_idx = num + symmetry_step -1
            if left_idx < 0 or right_idx >= num_of_switches:
                break
            if state_switches[left_idx] != state_switches[right_idx]:
                break
            symmetry_step += 1
        symmetry_step -= 1

        for idx in range(num - symmetry_step - 1, num + symmetry_step):
            state_switches[idx] = int(not state_switches[idx])

    else:
        raise Exception("정상적인 입력 형태가 아닙니다.")

# === main function ===#

num_of_switches = int(input())
# for _ in range(int(num_of_switches / 20) + 1):
#     state_switches.append(map(int, input().split()))
# state_switches = flatten(state_switches)
state_switches = list(map(int,input().split()))

num_of_std = int(input())
for _ in range(num_of_std):
    state_of_std.append(map(int, input().split()))

for std in state_of_std:
    action(std)

for idx in range(num_of_switches):
    if idx != 0 and (idx+1) % 20 == 0:
        print(state_switches[idx], end='\n')
    else:
        print(state_switches[idx], end=' ')