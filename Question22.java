import java.util.HashMap;

public class Question22 {
    public static void find2Sum(int[] nums , int target){
        HashMap<Integer,Integer> hm = new HashMap<>();
        for(int i =0 ; i < nums.length ;i++){
            int temp = target - nums[i];
            if(!hm.containsKey(temp)){
                hm.put(nums[i], i);
            }
            else{
                System.out.println(hm.get(temp)+" "+i);
            }
        }

    }
    public static void main(String[] args) {
        int[] nums = {2,0,7,8};
        int target=9;
        find2Sum(nums, target);

    }
    
}
