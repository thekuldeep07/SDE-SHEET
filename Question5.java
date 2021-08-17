class Question5{
    public static void main(String[] args) {
        int[] nums = {5,4,-1,7,8};

        System.out.println(findSum(nums));
    }

    public static int findSum(int[] nums){

        int l = nums.length;
        if(l==1){
            return nums[0];
        }

        int max_so_far = nums[0],max_ending_here=nums[0];

        for(int i =1 ; i < l ;i++){
            max_so_far=Math.max(nums[i], max_so_far+nums[i]);
            if(max_so_far>max_ending_here){
                max_ending_here=max_so_far;
            }

        }
        return max_ending_here;
        
    }
}