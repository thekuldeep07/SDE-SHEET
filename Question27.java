import java.util.HashMap;

public class Question27 {
    
    public static int findSubarraySumK(int[] nums , int k){
        int ans=0;
        int sum=0;
        HashMap<Integer,Integer> hm = new HashMap<>();
        int n = nums.length;
        for(int i =0 ; i <  n ; i++){
            sum+=nums[i];
            if(sum==k){
                ans+=1;
            }
            int y = sum-k;
            if (hm.containsKey(y)){
                ans+=hm.get(y);
            }

            if (hm.get(sum)!=null){
                hm.put(sum, hm.get(sum)+1);
            }
            else{
                hm.put(sum, 1);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] nums = {9, 4, 20, 3, 10, 5};
        System.out.println(findSubarraySumK(nums, 33));
    }
}
