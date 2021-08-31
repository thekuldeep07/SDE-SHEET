import java.util.HashMap;


class Question25{
    public static int findSubarrayZeroSum(int[] nums){
        int ans=0;
        int s=0;
        HashMap<Integer,Integer> hmp = new HashMap<Integer,Integer>();
        for(int i =0 ; i < nums.length;i++){
            s+=nums[i];
            if(s==0){
                ans=i+1;
            }
            else{
                if (hmp.containsKey(s)){
                    ans=Math.max(ans, i-hmp.get(s));
                }
                else{
                    hmp.put(s, i);
                }
            }
        }
    return ans;
    }
    public static void main(String[] args) {
        int[] nums = {15, -2, 2, -8, 1, 7, 10, 23};
        System.out.println(findSubarrayZeroSum(nums));
    }
}