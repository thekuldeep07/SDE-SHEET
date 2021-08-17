public class Question18 {
    public static void findMajority(int[] nums){
        int count=0;
        int maj_index=0;
        for(int i =0 ; i < nums.length;i++){
            if(nums[i]==nums[maj_index]){
                count+=1;
            }
            else{
                count-=1;
            }
            if(count==0){
                maj_index=i;
                count=1;
            }
        }
        int c=0;
        for(int i =0 ; i < nums.length;i++){
            if(nums[i]==nums[maj_index]){
                c+=1;
            }

        }
        if (c > nums.length/2){
            System.out.println(nums[maj_index]);
        }
        else{
            System.out.println("not found");
        }

    }

    public static void main(String[] args) {
        int[] nums ={7,7,5,7,5,1,7};
        findMajority(nums);
    }    
}
