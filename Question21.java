public class Question21 {
    public static int findReversePair(int[] nums){
        int n = nums.length;
        int[] temp = new int[n];
        int c=0;
        c=mergeSort(nums,temp,0,n-1);
        return c;
    }

    public static int mergeSort(int[] nums, int[] temp , int left , int right){
        int c=0;
        if (left < right){
            int mid = left+((right-left)>>1);
           
            c+=mergeSort(nums, temp, left, mid);
            c+=mergeSort(nums, temp, mid+1, right);
            System.out.print(c);
            c+=merge(nums, temp, left,mid, right);

        }

        return c;

    }

    public static int merge(int[] nums, int[] temp , int left , int mid , int right){
        int c=0;
        int i=left,k=left;
        int j = mid+1;

        while(i<=mid && j<=right){
            if(nums[i]>2*nums[j]){
                c=c+(mid-i+1);
                j++;
            }
            else{
                i++;
            }
        }
         i=left;
         j = mid+1;

        while (i <= mid && j <=right){
            if (nums[i]<=nums[j]){
                temp[k]=nums[i];
                k+=1;
                i+=1;
            }
            else{
                temp[k]=nums[j];
                k+=1;
                j+=1;
                
            }
        while (i<=mid){
            temp[k]=nums[i];
                k+=1;
                i+=1;
        }  
        
        while(j<=right){
            temp[k]=nums[j];
                k+=1;
                j+=1;
        }

        for(int z = left;z<=right;z++){
            nums[z]=temp[z];
        }

        }
        
        return c;
    }

    public static void main(String[] args) {
        int[] ques = {1,3,2,3,1};
        System.out.println(findReversePair(ques));
    }
    
}
