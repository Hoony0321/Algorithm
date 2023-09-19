import java.util.*;

class Solution {
    public int solution(int storey) {
        int answer = 0;
        
        int n = 0;
        while(storey > 0){
            int rest =  storey % (int)Math.pow(10,n+1) / (int) Math.pow(10,n);
            
            if(rest < 5){ // 내려가기
                answer += rest;
                storey -= rest * (int) Math.pow(10, n);
            }
            else if(rest == 5){
                if(storey % (int)Math.pow(10,n+2) / (int)Math.pow(10,n+1) < 5){
                    answer += rest;
                    storey -= rest * (int) Math.pow(10, n);
                }
                else{
                    answer += 10-rest;
                    storey += (10-rest) * (int) Math.pow(10,n);
                }
                
            }
            else{ // 올라가기
                answer += 10-rest;
                storey += (10-rest) * (int) Math.pow(10,n);
            }
            
            n++;
        }
        
        
        return answer;
    }
}