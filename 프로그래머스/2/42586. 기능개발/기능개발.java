import java.util.*;

class Feature {
    int progress;
    int speed;
    
    public Feature(int progress, int speed){
        this.progress = progress;
        this.speed = speed;
    }
    
    public void develop(){
        progress += speed;
    }
    
    public boolean isDone(){
        return progress >= 100 ? true : false;
    }
}

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        Deque<Feature> featDeque = new ArrayDeque<>();
        for(int i=0; i < progresses.length; i++){
            featDeque.addLast(new Feature(progresses[i], speeds[i]));
        }
        
        while(!featDeque.isEmpty()){
            // 배포 가능한 게 있는지 체크
            int deployNum = 0;
            while(!featDeque.isEmpty() && featDeque.peek().isDone()){
                featDeque.removeFirst();
                deployNum += 1;
            }
        
            if(deployNum > 0) answer.add(deployNum);
            
            // 개발 진행
            for(Feature feat : featDeque){
                feat.develop();
            }
            
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}