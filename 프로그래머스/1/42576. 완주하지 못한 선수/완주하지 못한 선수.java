import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        Map<String,Integer> completionMap = new HashMap<>();
        
        for(String c : completion){
            completionMap.put(c, completionMap.getOrDefault(c,0) + 1);
        }
        
        for(String p : participant){
            if(completionMap.getOrDefault(p,0) <= 0){
                answer = p;
                break;
            }
            
            completionMap.put(p, completionMap.get(p) - 1);
        }
        
        return answer;
    }
}