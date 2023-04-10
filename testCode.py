# 문제 정보

# 5 4
# 1 3
# 1 2
# 2 3
# 2 4

# 4
# 4
# 3
# 4
# 1

# === import module ===#

# === variable declare ===#
n = 0;
k = 0;
switchs = [];
stdArray = [];
stdSwitch = [];

# === Function define ===#

# === main function ===#

n,k = map(int, input().split())

stdArray = [0 for _ in range(n)]
stdSwitch = [i for i in range(n)]

for i in range(k):
    switchs.append(list(map(int, input().split())));

for i in range(k):
    for item in switchs:
        sit1, sit2 = item[0], item[1];
        stdSwitch[stdArray[sit1]] += 1;
        stdSwitch[stdArray[sit2]] += 1;

        stdArray[]

        stdArray[item[1]], stdArray[[item[0]]] = stdArray[[item[0]]], stdArray[[item[1]]]

print(stdSwitch);




