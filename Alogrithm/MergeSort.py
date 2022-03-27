#Merge Sort
import random

def Merge(h,m,U,V,S):

    i = 0; j =0; k = 0;
    while(i < h and j < m):

        if U[i] < V[j]: #U[i]가 S[i]에 들어감.
            S[k] = U[i];
            i += 1;
        else: #V[i]가 S[i]에 들어감.
            S[k] = V[j];
            j += 1;
        k += 1;

    if (i > h-1): #V배열에 남은 수 넣기 j ~ m-1
        S[k:] = V[j:];
    else: #U배열에 남은 수 넣기 i ~ h-1
        S[k:] = U[i:];





def MergeSort(n,S):
    global  requireVolume, max_volume;
    h = n//2; m = n - h;




    if n>1:
        # 추가 저장 공간 발생
        U = S[0:h];
        V = S[h:];
        requireVolume += (h + m);  # h,m만큼 volume 추가 발생
        max_volume = max(max_volume, requireVolume);


        MergeSort(h,U);
        MergeSort(m,V);

        Merge(h,m,U,V,S);
        #Merge 후 U와 V에 할당한 Volume 삭제
        requireVolume -= (h+m);



#n = int(input()); #테스트 할 데이터 크기
#S = [random.randrange(1,101) for _ in range(n)]; #1~100사이의 랜덤 난수 n번 발생

S = [8,3,15,2,9,1,5,7,4,16,10,11,12,13,6,14];
n = 16;

requireVolume = 0;
max_volume = 0;
MergeSort(n,S);
print(S);
print("추가 저장 공간 : {}".format(max_volume));

