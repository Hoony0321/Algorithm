class Solution {
    public boolean judgeNewCity(int canMoveSilver, int canMoveGold, int canMoveTotal, int needSilver, int needGold){
        if(needSilver > canMoveSilver) return false;
        if(needGold > canMoveGold) return false;
        if(needSilver + needGold > canMoveTotal) return false;
        return true;
    }
    
    public long solution(int a, int b, int[] g, int[] s, int[] w, int[] t) {
        long answer = 4 * (long) Math.pow(10,14) + (long) Math.pow(10,15) + 5;
        int cityNum = g.length;
        long maxTime =  4 * (long) Math.pow(10,14) + (long) Math.pow(10,15) + 5;
        long minTime = 1;
        
        
        while(maxTime >= minTime){
            long midTime = (maxTime + minTime)/2;
            
            // midTime 동안 모든 금,은을 옮길 수 있는지 판단.
            int canMoveSilver = 0;
            int canMoveGold = 0;
            int canMoveTotal = 0;
            
            for(int i = 0; i < cityNum; i++){
                long moveCnt = midTime / (2 * t[i]);
                if(midTime % (2 * t[i]) >= t[i]) moveCnt++;
                
                canMoveGold += Math.min(g[i], moveCnt * w[i]);
                canMoveSilver += Math.min(s[i], moveCnt * w[i]);
                canMoveTotal += Math.min(g[i] + s[i], moveCnt * w[i]);
            }
            
            boolean canNewCity = judgeNewCity(canMoveSilver, canMoveGold, canMoveTotal, b, a);
            
            if(canNewCity){ // 새로운 도시 건설 가능
                answer = Math.min(midTime, answer);
                maxTime = midTime - 1;
            }
            
            if(!canNewCity){ // 새로운 도시 건설 불가능
                minTime = midTime + 1;
            }
        }
        
        return answer;
    }
}