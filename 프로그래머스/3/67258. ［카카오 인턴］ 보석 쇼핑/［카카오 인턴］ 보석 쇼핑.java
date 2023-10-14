import java.util.*;

class Solution {
    Set<String> gemSet = new HashSet<>();
    
    public int[] getSection(String[] gems, int size){
        int totalGem = 0;
        Queue<String> queue = new LinkedList<>();
        Map<String, Integer> gemMap = new HashMap<>();
        
        for(int i = 0; i < gems.length; i++){
            // 보석 추가
            queue.add(gems[i]);
            gemMap.put(gems[i], gemMap.getOrDefault(gems[i], 0)+1);
            if(gemMap.get(gems[i]) == 1) totalGem += 1;
            
            // 보석 삭제
            if(queue.size() > size){
                String removeGem = queue.poll();
                gemMap.put(removeGem, gemMap.get(removeGem) -1);
                if(gemMap.get(removeGem) == 0) totalGem -= 1;
            }
            
            // System.out.println(gemMap);
            // System.out.println(totalGem);
            
            // 모든 보석이 포함되어 있는지 확인
            if(totalGem == gemSet.size()) return new int[]{i-size+2,i+1};
            
        }
        
        return new int[]{};
    }
    
    public int[] solution(String[] gems) {
        int[] answer = {};
            
        for(String gem : gems){
            gemSet.add(gem);
        }

        
        // 구간 크기 구하기
        int start = 0;
        int end = gems.length;
        while(start <= end){
            int mid = (start + end) / 2;
            // System.out.println(String.format("mid : %d", mid));
            
            // 불가능한 개수
            if(mid < gemSet.size()){
                start = mid + 1;
                continue;
            }
            
            // 가능한 구간
            int[] section = getSection(gems, mid);
            
            // 가능한 구간 없음
            if(section.length == 0) start = mid + 1;
            // 가능한 구간 있음
            else{
                end = mid - 1;
                answer = section;
            } 
        }
        
        return answer;
    }
}