from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    playDict = defaultdict(list)
    for i in range(len(plays)):
        playDict[genres[i]].append([plays[i],i])
    
    # 가장 많이 재생된 장르 순으로 정렬
    genrePlayList = []
    for key,value in playDict.items():
        genrePlayList.append([sum(x[0] for x in playDict[key]),key])
    
    genrePlayList.sort(key = lambda x : x[0], reverse=True)
    
    for _, genre in genrePlayList:
        playDict[genre].sort(key = lambda x : x[0], reverse=True)
        answer.append(playDict[genre][0][1])
        if len(playDict[genre]) > 1:
            answer.append(playDict[genre][1][1])
    
    return answer