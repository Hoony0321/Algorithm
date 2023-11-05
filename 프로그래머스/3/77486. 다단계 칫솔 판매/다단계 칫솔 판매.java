import java.util.*;

class Solution {
    
    public void distributeProfit(){
        
    }
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int size = enroll.length;
        Map<String,String> referralMap = new HashMap<>();
        Map<String,Integer> profitMap = new HashMap<>();
        
        for(int i = 0; i < size; i++){
            referralMap.put(enroll[i], referral[i]);
            profitMap.put(enroll[i], 0);
        }
        
        // 이익금 분배
        for(int i = 0; i < seller.length; i++){
            String current = seller[i];
            int profit = amount[i] * 100;
            
            while(profit > 0){
                String recommender = referralMap.get(current);
                if(recommender.equals("-")){ // 추천인이 없는 경우 -> center로 분배
                    int referralFee = (int) (profit * 0.1);
                    profitMap.put(current, profitMap.get(current) + profit - referralFee);
                    profit = 0;
                }
                else{ // 추천인이 있는 경우
                    int referralFee = (int) (profit * 0.1);
                    profitMap.put(current, profitMap.get(current) + profit - referralFee);
                    profit = referralFee;
                    current = recommender;
                }
            }
        }
        
        int[] answer = new int[size];
        for(int i = 0; i < size; i++){
            // System.out.println(String.format("%s : %d", enroll[i], profitMap.get(enroll[i])));
            answer[i] = profitMap.get(enroll[i]);
        }
        
        return answer;
    }
}