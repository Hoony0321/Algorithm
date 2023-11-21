import java.util.*;

class Solution {
    String targetString;
    int count = -1;
    boolean isFind = false;
    List<String> alphabets = List.of("A", "E", "I", "O", "U");
    
    public int solution(String word) {
        targetString = word;
        
        dfs("");
        
        return count;
    }
    
    public void dfs(String current){
        if(isFind) return;
        count++;
        
        if(current.equals(targetString)){
            isFind = true;
            return;
        }
        
        if(current.length() == 5){
            return;
        }
        
        for(String alphabet : alphabets){
            dfs(current + alphabet);
        }
    }
}