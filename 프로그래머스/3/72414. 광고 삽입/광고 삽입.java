import java.util.*;

class Solution {
    public int convertTimeStringToInt(String time){
        String[] splited = time.split(":");
        return Integer.parseInt(splited[0]) * 3600 + Integer.parseInt(splited[1]) * 60 + Integer.parseInt(splited[2]);
    }
    
    public String convertTimeIntToString(int time){
        int hour = time / 3600;
        int min = (time - hour * 3600)  / 60;
        int second = time - hour * 3600 - min * 60;
        return String.format("%02d:%02d:%02d",hour,min,second);
    }
    
    public String solution(String play_time, String adv_time, String[] logs) {
        int totalPlayTime = convertTimeStringToInt(play_time);
        long[] times = new long[totalPlayTime + 2];
        
        // 누적합 세팅
        for(String log : logs){
            String[] logTimes = log.split("-");
            int startTime = convertTimeStringToInt(logTimes[0]);
            int endTime = convertTimeStringToInt(logTimes[1]);
            
            times[startTime] += 1;
            times[endTime] += -1;
        }
        
        // 누적합 진행
        for(int i = 0; i < totalPlayTime; i++){
            times[i+1] += times[i];
        }
        
        // 최장 시청 구간 구하기
        int advTime = convertTimeStringToInt(adv_time);
        int maxWatchingTimeIdx = 0;
        long maxWatchingTime = 0;
        for(int i = 0; i < advTime; i++){
            maxWatchingTime += times[i];
        }
        
        long sumWatchingTime = maxWatchingTime;
        for(int i = 1; i < totalPlayTime - advTime + 1; i++){
            sumWatchingTime -= times[i-1];
            sumWatchingTime += times[i+advTime-1];
            if(sumWatchingTime > maxWatchingTime){
                maxWatchingTime = sumWatchingTime;
                maxWatchingTimeIdx = i;
            }
        }
        
        return convertTimeIntToString(maxWatchingTimeIdx);
    }
}