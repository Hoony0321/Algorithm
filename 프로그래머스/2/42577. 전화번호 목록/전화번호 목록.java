import java.util.*;

class Solution {
    public boolean solution(String[] phoneBook) {
        Map<String, Boolean> map = new HashMap<>();
        
        for (String number : phoneBook) {
            map.put(number, true);
        }

        for (String number : phoneBook) {
            for (int i = 1; i < number.length(); i++) {
                if (map.containsKey(number.substring(0, i))) {
                    return false;
                }
            }
        }

        return true;
    }
}