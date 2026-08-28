import java.util.*;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        //선언
        Map<Integer, Integer> dict = new HashMap<>();
        
        //카운트
        for (int a: array){
            dict.put( a, dict.getOrDefault(a,0) + 1);
        }
        
        int feq = 0;
        
        for (int k : dict.keySet()){
            if (dict.get(k) > feq){
                feq = dict.get(k);
                answer = k;
            }
        }
        
        int cnt = 0;
        for (int k : dict.keySet()){
            if (dict.get(k) == feq){
                cnt++;
            }
            if(cnt >1){
                return -1;
            }
        }
        
        
        
        //System.out.println(feq);
        return answer;
    }
}