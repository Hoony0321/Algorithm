#baekjoon_1495_기타리스트

N , S, M = map(int,input().split());

tuneList= list(map(int,input().split()));

VolumeList = [[] for _ in range(N+1)];
VolumeList[0].append(S);


for i in range(1,N+1):
    tuneAvailable = False;
    for preVol in VolumeList[i-1]:
        #P - V[i]
        nxtVol = preVol - tuneList[i-1];
        if 0 <= nxtVol <= M:
            if nxtVol not in VolumeList[i]:
                VolumeList[i].append(nxtVol);
                tuneAvailable = True;
        #P + V[i]
        nxtVol = preVol + tuneList[i-1];
        if 0 <= nxtVol <= M:
            if nxtVol not in VolumeList[i]:
                VolumeList[i].append(nxtVol);
                tuneAvailable = True;

    if not tuneAvailable:
        print(-1); exit(0);

print(max(VolumeList[N]));


