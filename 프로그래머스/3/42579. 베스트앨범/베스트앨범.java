import java.util.*;

class GenrePlayItem {
    String genre;
    int totalPlays;
    PriorityQueue<int[]> playQueue;
    
    public GenrePlayItem(String genre){
        this.genre = genre;
        totalPlays = 0;
        playQueue = new PriorityQueue<int[]>((o1,o2) -> {
            return o2[1] - o1[1];
        });
    }
    
    public void addItem(int[] item){
        this.totalPlays += item[1];
        playQueue.add(item);
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String,GenrePlayItem> genrePlayMap = new HashMap<>();
        int size = genres.length;
        
        for(int i = 0; i < size; i++){
            if(genrePlayMap.containsKey(genres[i])){
                genrePlayMap.get(genres[i]).addItem(new int[]{i,plays[i]});
            }
            else{
                genrePlayMap.put(genres[i], new GenrePlayItem(genres[i]));
                genrePlayMap.get(genres[i]).addItem(new int[]{i,plays[i]});
            }
        }
        
        PriorityQueue<GenrePlayItem> genreOrderQueue = new PriorityQueue<GenrePlayItem>((o1,o2) -> {
            return o2.totalPlays - o1.totalPlays;
        });
        for(Map.Entry<String,GenrePlayItem> item : genrePlayMap.entrySet()){
            genreOrderQueue.add(item.getValue());
        }
        
        List<Integer> answerList = new ArrayList<>();
        while(!genreOrderQueue.isEmpty()){
            PriorityQueue<int[]> playQueue = genreOrderQueue.poll().playQueue;;
            
            int count = 0;
            while(!playQueue.isEmpty() && count < 2){
                answerList.add(playQueue.poll()[0]);
                count++;
            }
        }
        
        int[] answer = new int[answerList.size()];
        for(int i = 0; i < answerList.size(); i++){
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}