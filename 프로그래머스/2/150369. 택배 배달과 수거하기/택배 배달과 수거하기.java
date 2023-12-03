import java.util.*;

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        // pickUpStack & deliveryStack 초기화
        Stack<int[]> pickUpStack = new Stack<>();
        for(int i = 0; i < pickups.length; i++){
            if(pickups[i] == 0) continue;
            pickUpStack.add(new int[]{i+1, pickups[i]});
        }
        
        Stack<int[]> deliveryStack = new Stack<>();
        for(int i = 0; i < deliveries.length; i++){
            if(deliveries[i] == 0) continue;
            deliveryStack.add(new int[]{i+1, deliveries[i]});
        }
        
        long moveDistance = 0;
        while(!deliveryStack.isEmpty() || !pickUpStack.isEmpty()){
            int maxDistanceHouse = 0;
            
            // 택배 박스 배달
            int deliveryBoxNum = 0;
            while(!deliveryStack.isEmpty()){ // 배달할 곳이 있으면
                if(deliveryBoxNum >= cap) break;
                
                int[] stackElem = deliveryStack.pop();
                deliveryBoxNum += stackElem[1];
                maxDistanceHouse = Math.max(maxDistanceHouse, stackElem[0]);
                
                if(deliveryBoxNum > cap){ // 용량 초과인 경우 -> 넘치는 박스는 다시 추가
                    deliveryStack.add(new int[]{stackElem[0], deliveryBoxNum - cap});
                }
            }
            
            // 택배 박스 수거
            int pickUpBoxNum = 0;
            while(!pickUpStack.isEmpty()){ // 픽업할 곳이 있으면
                if(pickUpBoxNum >= cap) break;
                
                int[] stackElem = pickUpStack.pop();
                pickUpBoxNum += stackElem[1];
                maxDistanceHouse = Math.max(maxDistanceHouse, stackElem[0]);
                
                if(pickUpBoxNum > cap){ // 용량 초과인 경우 -> 넘치는 박스는 다시 추가
                    pickUpStack.add(new int[]{stackElem[0], pickUpBoxNum - cap});
                }
            }
            
            // 이동거리 계산
            moveDistance += 2 * maxDistanceHouse;
        }
        
        
        return moveDistance;
    }
}