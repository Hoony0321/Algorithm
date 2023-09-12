import java.util.Map;
import java.util.HashMap;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;


class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 1;
        int totalWeight = 0;
        Map<Integer, Integer> bridge = new HashMap<>();
        
        
        for(int i = 0; i < truck_weights.length; i++){
            bridge.put(i, 1);
            totalWeight += truck_weights[i];
            
            while(i != truck_weights.length-1){
                answer += 1;
                
                // 다리에 있는 트럭들 한칸씩 전진
                List<Integer> removeList = new ArrayList<>();
                for(int truck : bridge.keySet()){
                    int position = bridge.get(truck);
                    if(position == bridge_length){
                        removeList.add(truck);
                    }
                    else{
                        bridge.put(truck, position+1);
                    }
                }
                
                // 다 건너 트럭 제거
                for(int removeKey : removeList){
                    totalWeight -= truck_weights[removeKey];
                    bridge.remove(removeKey);
                }
                
                // 다음 트럭 추가될 수 있는지 확인
                if(totalWeight + truck_weights[i+1] <= weight) break;
            }
            
        }
        
        return answer + bridge_length;
    }
}