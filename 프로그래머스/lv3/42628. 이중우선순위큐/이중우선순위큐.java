import java.util.*;

class Solution {
    TreeSet<Integer> treeSet = new TreeSet<>();
    
    public void operate(String operation, Integer number){
        if(operation.equals("I")){
            treeSet.add(number);
        }
        else if(operation.equals("D")){
            if(!treeSet.isEmpty()){
                if(number == 1){
                    treeSet.pollLast();
                }
                else if(number == -1){
                    treeSet.pollFirst();
                }
            }
        }
    }
    
    public int[] solution(String[] operations) {
        
        for(String operation : operations){
            String[] _operation = operation.split(" ");
            String operator = _operation[0];
            Integer number = Integer.parseInt(_operation[1]);
            
            operate(operator, number);
        }
        
        
        
        
        
        return treeSet.isEmpty() ? new int[]{0,0} : new int[]{treeSet.last(), treeSet.first()};
    }
}