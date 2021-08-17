class Question11 {

    public static void nextPermutation(int[] nums){
        int n = nums.length;
        int i =n-2;
        while (i >=0){
            if (nums[i]<nums[i+1]){
                break;
            }
            i--;
        }
        if(i>=0){
            int j=n-1;
            while (nums[j]<=nums[i]){
                j--;
            }
            swap(nums,i,j);

        }

        reverse(nums,i+1,n-1);
        printArr(nums);

    }
    public static void swap(int[] nums,int i,int j){
        int temp;
        temp=nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
    }

    public static void reverse(int[] nums,int i , int n){
        while(i<n){
            swap(nums, i++, n--);
        }
    }

    public static void printArr(int[] nums){
        for(int i=0;i<nums.length;i++){
            System.out.print(nums[i]);
        }
    }




    public static void main(String[] args) {
        int nums[]={1,3,2};
        nextPermutation(nums);
    }

    
}
