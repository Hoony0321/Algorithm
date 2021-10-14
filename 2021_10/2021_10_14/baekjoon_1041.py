#baekjoon_1041_주사위

def FindOnlyOneSide(size):
    sum = 0;
    sum += (size-2) * (size-2) * 5;
    #밑에가 바닥이라서 맨 밑 가운데 블럭들도 한면만 보임
    sum += (size-2)*4;

    return sum;



size = int(input());
#A,B,C,D,E,F 순
dice = list(map(int,input().split()));

#2개씩 인접한 것으로 묶은 쌍
#(a,b),(a,c),(a,d),(a,e),(b,c),(b,d),(b,f),(c,e),(c,f),(d,e),(d,f),(e,f)
#(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)
pair2 = ((0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5));
num2_list = [];  #세쌍씩 묶은 값들의 합 리스트
for i in range(len(pair2)):
    sum = 0;
    for val in pair2[i]:
        sum += dice[val];
    num2_list.append(sum);


#3개씩 인접한 것으로 묶은 쌍
#(a,b,c),(a,b,d),(a,d,e),(a,c,e),(f,b,c),(f,b,d),(f,d,e),(f,c,e)
#(0,1,2),(0,1,3),(0,3,4),(0,2,4),(5,1,2),(5,1,3),(5,3,4),(5,2,4)
pair3 = ((0,1,2),(0,1,3),(0,3,4),(0,2,4),(5,1,2),(5,1,3),(5,3,4),(5,2,4));
num3_list = [];  #세쌍씩 묶은 값들의 합 리스트
for i in range(len(pair3)):
    sum = 0;
    for val in pair3[i]:
        sum += dice[val];
    num3_list.append(sum);



min_num_dice = min(dice);
min_num_pair2 = min(num2_list);
min_num_pair3 = min(num3_list);

num_display_dice = (size**3 - (size-2)**3) - ((size-2)**2);
num_side1 = FindOnlyOneSide(size);
num_side3 = 4;
num_side2 = num_display_dice - num_side1 - num_side3;

if(size==1):
    maxVal = max(dice);
    sum = 0;
    for val in dice:
        sum += val;
    print(sum - maxVal);
else:
    print(num_side1*min_num_dice + num_side2*min_num_pair2 + num_side3*min_num_pair3);





