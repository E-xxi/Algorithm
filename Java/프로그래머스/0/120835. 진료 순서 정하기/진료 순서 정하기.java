import java.util.*;

class Solution {
    public int[] solution(int[] emergency) {
        //응급도 높은 순서대로 정렬
        int[] answer = new int[emergency.length];
        Map<Integer, Integer> emerNum = new HashMap<>();
        
        for(int i=0; i<emergency.length; i++){
            for (int j = 0; j<emergency.length; j++){
                if(emergency[i] <= emergency[j]){
                    answer[i] ++;
                }
            }
        }
        return answer;
    }
}