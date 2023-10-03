import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        List<int[]> jobList = new ArrayList<>();
        for(int[] job : jobs){
            jobList.add(new int[]{job[0], job[1]});
        }
        
        // 요청 시간대로 정렬
        Collections.sort(jobList, new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[0] - o2[0];
            }
        });
        
        int initSize = jobList.size();
        int current = 0;
        int sumWaitingTime = 0;
        while(!jobList.isEmpty()){
            int shortestUseTime = 1001;
            int shortestJobIdx = -1;
            for(int i = 0; i < jobList.size(); i++){
                int requestTime = jobList.get(i)[0];
                int useTime = jobList.get(i)[1];
                
                // 아직 요청되지 않음 -> 이후 작업들도 다 요청되지 않으므로 break
                if(requestTime > current) break;
                
                if(shortestUseTime > useTime){
                    shortestJobIdx = i;
                    shortestUseTime = useTime;
                }
            }
            
            if(shortestJobIdx == -1){ // 현재 처리할 수 있는 작업이 없는 경우 -> 시간 증가
                current++;
            }
            else{
                int requestTime = jobList.get(shortestJobIdx)[0];
                int useTime = jobList.get(shortestJobIdx)[1];
                
                sumWaitingTime += current - requestTime + useTime; // 대기 시간 추가
                jobList.remove(shortestJobIdx); // 완료된 작업 제거
                current += useTime; // 시간 증가
            }
            
        }
        
        return sumWaitingTime / initSize;
    }
}