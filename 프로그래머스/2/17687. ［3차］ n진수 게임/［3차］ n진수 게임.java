import java.util.*;

class Solution {
    HashMap<Integer,String> digitMap = new HashMap<>();
    
    public String convertNumberToDigit(int n, int number){
        if(number == 0) return "0";
        String numDigit = "";
        
        while(number > 0){
            int rest = number % n;
            numDigit = digitMap.get(rest) + numDigit;
            number /= n;   
        }
        
        return numDigit;
    }
    
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        
        
        for(int i = 0; i < 10; i++){
            digitMap.put(i,Integer.toString(i));
        }
        digitMap.put(10,"A");
        digitMap.put(11,"B");
        digitMap.put(12,"C");
        digitMap.put(13,"D");
        digitMap.put(14,"E");
        digitMap.put(15,"F");
        
        int num = 0;
        int turn = 0;
        while(answer.length() < t){
            String numDigit = convertNumberToDigit(n, num);
            
            for(int i = 0; i < numDigit.length(); i++){
                if(turn == p-1){
                    answer += numDigit.charAt(i);
                }
                turn = (turn + 1) % m;
            }
            
            num++;
        }
        
        
        return answer.substring(0,t);
    }
}