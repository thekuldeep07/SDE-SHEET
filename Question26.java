import java.util.HashMap;

class Question26{
    public static int countSubarrayXorK(int[] nums , int k){
        HashMap<Integer,Integer> hm = new HashMap<>();
        int ans=0;
        int xor=0;
        int n = nums.length;
        for(int i =0 ; i < n ; i++){
            xor=xor^nums[i];
            if (xor == k){
                ans+=1;
            }
            int y = xor^k;
            if(hm.containsKey(y)){
                ans+=hm.get(y);
            }

            if (hm.get(xor)!=null){
                hm.put(xor, hm.get(xor)+1);
            }
            else{
                hm.put(xor, 1);
            }

        }

        return ans;

    }
    public static void main(String[] args) {
        int[] nums ={4,2,2,6,4};
        System.out.println(countSubarrayXorK(nums, 6));
    }
}