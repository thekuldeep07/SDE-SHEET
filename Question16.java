public class Question16 {
    public static boolean searcMatrix(int[][] nums , int ele){
        int n= nums.length;
        int m = nums[0].length;
        int lp =0 ;
        int hp = (n*m)-1;
        while(lp<=hp){
            int mid = lp +(hp-lp)/2;
            if(nums[mid/m][mid%m]== ele){
                return true;
            }
            if(nums[mid/m][mid%m]<ele){
                lp=mid+1;
            }
            else{
                hp=mid-1;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[][] nums = {
            {1,3,5,7},
    {10,11,16,20},
    {23,30,34,50}
        };

        System.out.println(searcMatrix(nums,7));
    }
    
}
