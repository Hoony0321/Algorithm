import java.util.*;

class Song {
    int id;
    String genre;
    int play;
    
    public Song(int id, String genre, int play){
        this.id = id;
        this.genre = genre;
        this.play = play;
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String,List<Song>> songMap = new HashMap<>();
        
        for(int i = 0; i < genres.length; i++){
            if(!songMap.containsKey(genres[i])){
                songMap.put(genres[i], new ArrayList<>());
            }
            songMap.get(genres[i]).add(new Song(i, genres[i], plays[i]));
        }
        
        // songMap play 순으로 정렬
        Map<String,Integer> playMap = new HashMap<>();
        for(String genre : songMap.keySet()){
            songMap.get(genre).sort((a,b) -> Integer.compare(b.play, a.play));
            
            int totalPlay = 0;
            for(Song song : songMap.get(genre)){
                totalPlay += song.play;
            }
            
            playMap.put(genre,totalPlay);
        }
        
        // 많이 재생된 genre 순으로 정렬
        List<String> genrePlayList = new ArrayList<>(playMap.keySet());
        genrePlayList.sort((a,b) -> Integer.compare(playMap.get(b), playMap.get(a)));
        
        List<Integer> answer = new ArrayList<>();
        for(String genre : genrePlayList){
            answer.add(songMap.get(genre).get(0).id);
            if(songMap.get(genre).size() > 1){
                answer.add(songMap.get(genre).get(1).id);
            }
        }

   
        return answer.stream().mapToInt(x -> x.intValue()).toArray();
    }
}