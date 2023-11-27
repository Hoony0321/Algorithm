import java.util.*;

class Solution {    
    class Problem {
        int reqAlp;
        int reqCop;
        int rwdAlp;
        int rwdCop;
        int cost;
        
        public Problem(int[] array){
            this.reqAlp = array[0];
            this.reqCop = array[1];
            this.rwdAlp = array[2];
            this.rwdCop = array[3];
            this.cost = array[4];
        }
        
        public boolean isCanSolve(int alp, int cop){
            if(this.reqAlp <= alp && this.reqCop <= cop){
                return true;
            }
            
            return false;
        }
    }
    
    private int[] getMaxReqAlpAndCop(List<Problem> problemList){
        int maxReqAlp = 0;
        int maxReqCop = 0;
        for(Problem problem : problemList){
            maxReqAlp = Math.max(maxReqAlp, problem.reqAlp);
            maxReqCop = Math.max(maxReqCop, problem.reqCop);
        }
        
        return new int[]{maxReqAlp, maxReqCop};
    }
    
    private void setDpByBasicProblems(int[][] dp, int alp, int cop){
        for(int i = alp; i < dp.length-1; i++){
            for(int j = cop; j < dp[i].length-1; j++){
                dp[i+1][j] = dp[i][j] + 1;
                dp[i][j+1] = dp[i][j] + 1;
            }
        }
    }
    
    private void setDpByGivenProblems(int[][] dp, List<Problem> problemList, int alp, int cop, int maxReqAlp, int maxReqCop){
      for(int calp = alp; calp < dp.length; calp++){
            for(int ccop = cop; ccop < dp[0].length; ccop++){
                for(Problem problem : problemList){
                    if(!problem.isCanSolve(calp,ccop)) continue; // 요구되는 수치에 못 미치는 경우
                    if(calp + problem.rwdAlp >= dp.length-1 || ccop + problem.rwdCop >= dp[0].length-1) continue; // 범위를 벗어나는 경우
                    dp[calp + problem.rwdAlp][ccop + problem.rwdCop] = Math.min(
                        dp[calp + problem.rwdAlp][ccop + problem.rwdCop],
                        dp[calp][ccop] + problem.cost
                    );
                }
            }
        }
    }
    
    private int getMinTime(int[][] dp, int maxReqAlp, int maxReqCop){
        int minTime = Integer.MAX_VALUE;
        for(int alp = maxReqAlp; alp < dp.length; alp++){
            for(int cop = maxReqCop; cop < dp[0].length; cop++){
                minTime = Math.min(minTime, dp[alp][cop]);
            }
        }
        
        return minTime;
    }
    
    public int solution(int alp, int cop, int[][] problems) {
        // set problemList 
        List<Problem> problemList = new ArrayList<>();
        for(int[] problem : problems){
            problemList.add(new Problem(problem));
        }
        
        // set maxReqAlp & maxReqCop
        int[] maxReqAlpAndCopArray = getMaxReqAlpAndCop(problemList);
        int maxReqAlp = maxReqAlpAndCopArray[0];
        int maxReqCop = maxReqAlpAndCopArray[1];
        
        // set dp by basic problem
        int[][] dp = new int[451][451];
        for(int i = 0; i < dp.length; i++){
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }
        dp[alp][cop] = 0;
        setDpByBasicProblems(dp, alp, cop);

        // set dp by given problem
        setDpByGivenProblems(dp, problemList, alp, cop, maxReqAlp, maxReqCop);
        
        // get min time by dp
        int minTime = getMinTime(dp, maxReqAlp, maxReqCop);
        return minTime;
    }
}