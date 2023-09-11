import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class Solution
{
    public int solution(int []A, int []B)
    {
        List<Integer> listA = new ArrayList<>();
        List<Integer> listB = new ArrayList<>();
        
        for(int i : A){
            listA.add(i);
        }
        
        for(int i : B){
            listB.add(i);
        }
        
        Collections.sort(listA);
        Collections.sort(listB, (e1,e2)->e2-e1);
        
        int sum = 0;
        for(int i = 0; i < listA.size(); i++){
            sum += listA.get(i) * listB.get(i);
        }

        return sum;
    }
}