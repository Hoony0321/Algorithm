import java.util.*;

class Solution {
    public int[] solution(int n) {
        
        List<Integer> resultList = new ArrayList<>();
        int divideNum = 1;
        while(divideNum <= n){
            if(n % divideNum == 0){
                resultList.add(divideNum);
            }
            divideNum++;
        }
        
        int[] result = new int[resultList.size()];
        for(int i = 0; i < resultList.size(); i++){
            result[i] = resultList.get(i);
        }
        
        return result;
    }
}