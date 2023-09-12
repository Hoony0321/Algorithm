import java.util.ArrayList;
import java.util.List;
import java.util.HashSet;
import java.util.Set;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        Map<Integer, Integer> toppingA = new HashMap<>();
        
        for(int i : topping){
            if(toppingA.containsKey(i)){
                toppingA.put(i, toppingA.get(i)+1);
            }
            else{
                toppingA.put(i,1);
            }
        }
        
        Set<Integer> toppingB = new HashSet<>();
        
        for(int i : topping){
            toppingB.add(i);
            toppingA.put(i, toppingA.get(i)-1);
            
            if(toppingA.get(i) == 0) toppingA.remove(i);
            
            if(toppingB.size() == toppingA.size()) answer += 1;
        }
        
        return answer;
    }
}