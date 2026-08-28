class Solution {
    public int[] solution(int[] numbers) {
        //System.out.println(numbers.length);
        int l = numbers.length;
            
        int[] answer = new int[l];
        
        for (int i=0;i<numbers.length; i++){
            answer[i] = numbers[i] *2;
        }
        return answer;
    }
}