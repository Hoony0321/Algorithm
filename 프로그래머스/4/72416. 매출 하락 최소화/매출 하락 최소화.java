import java.util.*;

class Solution {
    Stack<Integer> leaders = new Stack<>();
    Map<Integer, List<Integer>> members = new HashMap<>();
    int[][] dp = new int[][]{};
    
    private int convertBooleanArrayToBinaryInt(boolean[] array){
        int result = 0;
        for(int i = 0; i < array.length; i++){
            result <<= 1;
            if(array[i]){
                result |= 1;
            }
        }
        return result;
    }
    
    public int solution(int[] sales, int[][] links) {
        // members 설정
        for(int[] link : links){
            int leader = link[0];
            int member = link[1];
            
            if(!members.containsKey(leader)){
                members.put(leader, new ArrayList<>());
            }
                    
            members.get(leader).add(member);
        }
        
        // leaders 설정
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        
        while(!queue.isEmpty()){
            int leader = queue.poll();
            leaders.add(leader);
            
            for(int member : members.get(leader)){
                if(members.containsKey(member)){
                    queue.add(member);
                }
            }
        }
        
        
        
        // dp 설정
        dp = new int[sales.length+1][2];
        for(int i = 1; i <= sales.length; i++){
            dp[i][0] = 0;
            dp[i][1] = sales[i-1];
        }
        
        // total min sum sales 찾기
        while(!leaders.isEmpty()){
            int leader = leaders.pop();
            // leader가 포함되는 경우
            int minSumSalesIncludeLeader = dp[leader][1];
            for(int member : members.get(leader)){
                minSumSalesIncludeLeader += Math.min(dp[member][0], dp[member][1]);
            }
            dp[leader][1] = minSumSalesIncludeLeader;
            
            // leader가 포함되지 않는 경우
            int minSumSalesNotIncludeLeader = 0;
            int selectZeroCount = 0;
            for(int member : members.get(leader)){
                minSumSalesNotIncludeLeader += Math.min(dp[member][0], dp[member][1]);
                selectZeroCount += dp[member][0] < dp[member][1] ? 1 : 0;
            }
            
            // 모든 멤버를 포함하지 않는 경우 (예외 경우)
            if(selectZeroCount == members.get(leader).size()){
                int minTotalSales = Integer.MAX_VALUE;
                
                for(int includeMember : members.get(leader)){
                    int totalSales = 0;
                    for(int member : members.get(leader)){
                        if(member == includeMember) totalSales += dp[member][1];
                        else totalSales += dp[member][0];
                    }
                    
                    minTotalSales = Math.min(minTotalSales, totalSales);
                }
                
                minSumSalesNotIncludeLeader = minTotalSales;
            }
            
            dp[leader][0] = minSumSalesNotIncludeLeader;
        }
        
        return Math.min(dp[1][0], dp[1][1]);
    }
}