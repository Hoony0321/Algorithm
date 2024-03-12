def solution(k, room_numbers):
    
    answer = []
    allocatedRoomDict = {}
    
    for roomNumber in room_numbers:
        tmpList = []
        while roomNumber in allocatedRoomDict:
            tmpList.append(roomNumber)
            roomNumber = allocatedRoomDict[roomNumber]
            
        
        for tmpRoomNumber in tmpList:
            allocatedRoomDict[tmpRoomNumber] = roomNumber+1
        
        allocatedRoomDict[roomNumber] = roomNumber+1
        answer.append(roomNumber)
        
    return answer