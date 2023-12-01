import java.util.*;

class Solution {
    List<User> userList = new ArrayList<>();
    List<Emoticon> emoticonList = new ArrayList<>();
    int maxTotalPurchasePrice = 0;
    int maxCountPurchaseEmoticonPlus = 0;
    
    class User {
        int targetDiscountRatio;
        int targetPrice;
        
        public User(int targetDiscountRatio, int targetPrice){
            this.targetDiscountRatio = targetDiscountRatio;
            this.targetPrice = targetPrice;
        }
        
        // 만약 targetPrice를 넘으면 -1 반환 (이모티콘 플러스 구매)
        public int getEmoticonPurchasePrice(List<Integer> discountList){
            int purchasePrice = 0;
            for(int i = 0; i < discountList.size(); i++){
                if(discountList.get(i) >= targetDiscountRatio){ // 목표 할인 비율 넘을때만 구매
                    int price = emoticonList.get(i).getPriceByDiscount(discountList.get(i));
                    purchasePrice += price;    
                }
            }
            
            return purchasePrice >= targetPrice ? -1 : purchasePrice;
        }
    }
    
    class Emoticon {
        int price;
        
        public Emoticon(int price){
            this.price = price;
        }
        
        public int getPriceByDiscount(int discountRatio){
            return price * (100 - discountRatio) / 100;
        }
    }
    
    public void dfs(int index, List<Integer> discountList){
        if(index == emoticonList.size()){ // 종료 조건
            int totalPurchasePrice = 0;
            int countPurchaseEmoticonPlus = 0;

            // get totalPurchasePrice & countPurchaseEmoticonPlus in current discount
            for(User user : userList){
                int purchasePrice = user.getEmoticonPurchasePrice(discountList);
                if(purchasePrice == -1){
                    countPurchaseEmoticonPlus++;
                }

                if(purchasePrice != -1){
                    totalPurchasePrice += purchasePrice;
                }
            }

            // update maxTotalPurchasePrice & maxTotalPurchasePrice
            if(maxCountPurchaseEmoticonPlus < countPurchaseEmoticonPlus){
                maxCountPurchaseEmoticonPlus = countPurchaseEmoticonPlus;
                maxTotalPurchasePrice = totalPurchasePrice;
            }
            
            if(maxCountPurchaseEmoticonPlus == countPurchaseEmoticonPlus){
                if(maxTotalPurchasePrice < totalPurchasePrice) maxTotalPurchasePrice = totalPurchasePrice;      
            }
            
            return;
        }
     
        // progress next step
        for(int addDiscount = 0; addDiscount < 50; addDiscount+=10){
            discountList.set(index, discountList.get(index) + addDiscount);
            dfs(index+1, discountList);
            discountList.set(index, discountList.get(index) - addDiscount);
        }
    }
    
    public int[] solution(int[][] users, int[] emoticons) {
        // set user list
        for(int[] user : users){
            userList.add(new User(user[0], user[1]));
        }
        
        // set emoticon list
        for(int emoticon : emoticons){
            emoticonList.add(new Emoticon(emoticon));
        }
        
        // set discount list
        List<Integer> discountList = new ArrayList<>();
        for(int i = 0; i < emoticons.length; i++){
            discountList.add(0);
        }
        
        dfs(0, discountList);
        
        return new int[]{maxCountPurchaseEmoticonPlus, maxTotalPurchasePrice};
    }
}